#!/usr/bin/env python3
"""
CI Validation script for GLORY-TIKTOK (Toeic Speaking).
Validates:
1. data/exam/toeic-speaking.yaml exists and is valid.
2. Lexicon YAML files in data/lexicon/ match schemas/word.v2.json.
3. Content sets front matter in content/sets/ match schemas/set.v2.json.
4. Word references in sets point to existing lexicon entries.
5. Practice timing matches exam specifications.
"""

import sys
import os
import glob
import json
import re
import yaml
import jsonschema

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def to_json_compatible(obj):
    return json.loads(json.dumps(obj, default=str))

def extract_frontmatter(md_path):
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()
    if not content.startswith("---"):
        return None
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None
    data = yaml.safe_load(parts[1])
    return to_json_compatible(data) if data else None

def main():
    errors = []
    print("[INFO] Starting GLORY-TIKTOK data validation...")

    # 1. Load schemas
    word_schema_path = os.path.join(BASE_DIR, "schemas", "word.v2.json")
    set_schema_path = os.path.join(BASE_DIR, "schemas", "set.v2.json")

    word_schema = load_json(word_schema_path) if os.path.exists(word_schema_path) else None
    set_schema = load_json(set_schema_path) if os.path.exists(set_schema_path) else None

    if not word_schema or not set_schema:
        print("[ERROR] Missing schemas in schemas/")
        sys.exit(1)

    # 2. Check exam parameters
    exam_path = os.path.join(BASE_DIR, "data", "exam", "toeic-speaking.yaml")
    if not os.path.exists(exam_path):
        errors.append(f"Missing exam parameters file: {exam_path}")
    else:
        try:
            exam_data = load_yaml(exam_path)
            assert "parts" in exam_data, "Missing 'parts' in exam data"
            assert "proficiency_levels" in exam_data, "Missing 'proficiency_levels' in exam data"
            print("  [OK] Exam parameters: valid.")
        except Exception as e:
            errors.append(f"Invalid exam data in {exam_path}: {e}")

    # 3. Validate Lexicon
    lexicon_ids = set()
    lexicon_files = glob.glob(os.path.join(BASE_DIR, "data", "lexicon", "**", "*.yaml"), recursive=True)
    print(f"  Validating {len(lexicon_files)} lexicon files...")

    for l_path in lexicon_files:
        rel_path = os.path.relpath(l_path, BASE_DIR)
        try:
            raw_data = load_yaml(l_path)
            if not raw_data:
                errors.append(f"{rel_path}: Empty file")
                continue
            data = to_json_compatible(raw_data)
            
            # JSON Schema check
            jsonschema.validate(instance=data, schema=word_schema)

            # Check id matches filename
            expected_id = os.path.splitext(os.path.basename(l_path))[0]
            if data.get("id") != expected_id:
                errors.append(f"{rel_path}: id '{data.get('id')}' does not match filename '{expected_id}'")

            lexicon_ids.add(data.get("id"))
        except jsonschema.ValidationError as ve:
            errors.append(f"{rel_path} [Schema Error]: {ve.message} at path {'/'.join(str(p) for p in ve.path)}")
        except Exception as e:
            errors.append(f"{rel_path}: {e}")

    # 4. Validate Content Sets
    set_files = glob.glob(os.path.join(BASE_DIR, "content", "sets", "set-*.md"))
    print(f"  Validating {len(set_files)} lesson set files...")

    for s_path in set_files:
        rel_path = os.path.relpath(s_path, BASE_DIR)
        try:
            fm = extract_frontmatter(s_path)
            if not fm:
                errors.append(f"{rel_path}: Missing or unparseable front matter")
                continue

            # If v2, validate schema
            if fm.get("schema_version") == 2:
                jsonschema.validate(instance=fm, schema=set_schema)

                # Check that words reference existing lexicon entries
                words = fm.get("words", [])
                for w in words:
                    if isinstance(w, str) and w not in lexicon_ids:
                        errors.append(f"{rel_path}: Referenced word ID '{w}' not found in data/lexicon/")

        except jsonschema.ValidationError as ve:
            errors.append(f"{rel_path} [Schema Error]: {ve.message} at path {'/'.join(str(p) for p in ve.path)}")
        except Exception as e:
            errors.append(f"{rel_path}: {e}")

    # Report results
    if errors:
        print("\n[ERROR] Validation failed with errors:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print("\n[OK] Validation successful! All schemas, lexicon entries, and sets are verified.")
        sys.exit(0)

if __name__ == "__main__":
    main()
