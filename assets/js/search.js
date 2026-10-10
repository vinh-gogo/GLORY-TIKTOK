/* Glory 01 — lõi tìm kiếm (ADR-007). Nạp /search-index.json một lần, chuẩn hóa tiếng Việt không dấu.
 * Khóa chỉ mục: i=id l=lemma p=IPA s=loại từ b=band t=chủ đề m=nghĩa c=collocations y=từ đồng nghĩa */
(function () {
  'use strict';

  var cfg = {};
  try { cfg = JSON.parse(document.getElementById('glory-cfg').textContent) || {}; } catch (e) { cfg = {}; }
  var BANDS = cfg.bands || {};

  function norm(s) {
    return String(s == null ? '' : s)
      .toLowerCase()
      .normalize('NFD').replace(/[\u0300-\u036f]/g, '')
      .replace(/đ/g, 'd')
      .replace(/\s+/g, ' ')
      .trim();
  }

  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  var indexPromise = null;
  function loadIndex() {
    if (!indexPromise) {
      indexPromise = fetch('/search-index.json', { credentials: 'same-origin' })
        .then(function (r) { if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); })
        .then(function (list) {
          list.forEach(function (w) {
            w._l = norm(w.l);
            w._m = norm(w.m);
            w._c = (w.c || []).map(norm);
            w._y = (w.y || []).map(norm);
          });
          return list;
        });
      indexPromise.catch(function () { indexPromise = null; });
    }
    return indexPromise;
  }

  /* Điểm khớp cao hơn = ưu tiên hơn. Mọi từ khóa phải khớp ở đâu đó. */
  function scoreWord(w, tokens) {
    var total = 0;
    for (var i = 0; i < tokens.length; i++) {
      var t = tokens[i], s = 0, j;
      if (w._l === t) s = 100;
      else if (w._l.indexOf(t) === 0) s = 80;
      else if (w._l.indexOf(t) > -1) s = 60;
      if (!s) { for (j = 0; j < w._c.length; j++) { if (w._c[j].indexOf(t) > -1) { s = 40; break; } } }
      if (!s) { for (j = 0; j < w._y.length; j++) { if (w._y[j].indexOf(t) > -1) { s = 30; break; } } }
      if (!s && w._m.indexOf(t) > -1) s = 20;
      if (!s) return 0;
      total += s;
    }
    return total;
  }

  /* opts: {q, band, topic} → mảng từ đã lọc & sắp xếp */
  function find(list, opts) {
    opts = opts || {};
    var tokens = norm(opts.q).split(' ').filter(Boolean);
    var out = [];
    for (var i = 0; i < list.length; i++) {
      var w = list[i];
      if (opts.band && w.b !== opts.band) continue;
      if (opts.topic && (w.t || []).indexOf(opts.topic) < 0) continue;
      if (tokens.length) {
        var s = scoreWord(w, tokens);
        if (!s) continue;
        out.push({ w: w, s: s });
      } else {
        out.push({ w: w, s: 0 });
      }
    }
    if (tokens.length) {
      out.sort(function (a, b) { return b.s - a.s || (a.w._l < b.w._l ? -1 : a.w._l > b.w._l ? 1 : 0); });
    }
    return out.map(function (x) { return x.w; });
  }

  /* Markup phải khớp layouts/_partials/wcard.html */
  function cardHTML(w) {
    var label = BANDS[w.b] || w.b;
    return '<a class="wcard" href="/words/' + esc(w.i) + '/">' +
      '<span class="wcard-head"><strong class="wcard-lemma">' + esc(w.l) + '</strong><span class="wcard-ipa">' + esc(w.p) + '</span></span>' +
      '<span class="wcard-meta"><span class="wcard-pos">' + esc(w.s) + '</span><span class="band band-' + esc(w.b) + '">' + esc(label) + '</span></span>' +
      '<span class="wcard-mean">' + esc(w.m) + '</span></a>';
  }

  window.Glory = { norm: norm, esc: esc, loadIndex: loadIndex, find: find, cardHTML: cardHTML, cfg: cfg };

  /* ---- Trang /search/ ---- */
  var form = document.getElementById('search-form');
  if (!form) return;
  var input = document.getElementById('search-q');
  var status = document.getElementById('search-status');
  var box = document.getElementById('search-results');
  var PAGE = 30, shown = PAGE, results = [], timer = null;

  function render() {
    var slice = results.slice(0, shown);
    box.innerHTML = slice.map(cardHTML).join('');
    if (results.length > shown) {
      box.insertAdjacentHTML('beforeend', '<p class="center" style="grid-column:1/-1"><button type="button" class="btn" id="search-more">Xem thêm</button></p>');
      document.getElementById('search-more').addEventListener('click', function () { shown += PAGE; render(); });
    }
  }

  function run() {
    var q = input.value;
    if (!norm(q)) { box.innerHTML = ''; status.textContent = ''; return; }
    status.textContent = 'Đang tìm…';
    loadIndex().then(function (list) {
      if (q !== input.value) return;
      results = find(list, { q: q });
      shown = PAGE;
      status.textContent = results.length ? results.length + ' kết quả' : 'Không có kết quả cho “' + q + '”. Thử từ khóa ngắn hơn hoặc không dấu.';
      render();
    }).catch(function () {
      status.textContent = 'Không tải được dữ liệu tìm kiếm. Hãy kiểm tra kết nối rồi thử lại.';
    });
  }

  function syncURL() {
    var q = input.value.trim();
    var url = location.pathname + (q ? '?q=' + encodeURIComponent(q) : '');
    try { history.replaceState(null, '', url); } catch (e) { /* bỏ qua */ }
  }

  input.addEventListener('input', function () {
    clearTimeout(timer);
    timer = setTimeout(function () { syncURL(); run(); }, 150);
  });
  form.addEventListener('submit', function (e) { e.preventDefault(); syncURL(); run(); });

  var m = /[?&]q=([^&]*)/.exec(location.search);
  if (m) { try { input.value = decodeURIComponent(m[1].replace(/\+/g, ' ')); } catch (e) { input.value = ''; } run(); }
})();
