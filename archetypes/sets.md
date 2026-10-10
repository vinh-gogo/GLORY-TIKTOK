---
schema_version: 3
title: "{{ replace .File.ContentBaseName "-" " " | title }}"
date: {{ .Date }}
draft: true
summary: "Mô tả ngắn: các từ vựng và collocations xuất hiện trong video."
topics: []   # slug trong data/topics.yaml, tối đa 3
# Dán link video thật. Link mẫu dạng .../video/1234567xxx sẽ bị coi là placeholder.
tiktok: ""
aliases: []
words:
  # ID từ vựng có trong data/lexicon/ (vd: deadline, workload, commute)
  - ""
---
