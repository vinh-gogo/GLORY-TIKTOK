/* Glory 01 — lọc danh sách /glossary/. Trang tĩnh đã có 50 từ đầu; JS nạp chỉ mục khi người dùng thao tác.
 * Trạng thái lưu trên URL: ?q=&band=&topic= */
(function () {
  'use strict';
  var list = document.getElementById('gl-list');
  if (!list) return;

  var qEl = document.getElementById('gl-q');
  var moreBtn = document.getElementById('gl-more');
  var countEl = document.getElementById('gl-count');
  var bandBox = document.getElementById('gl-bands');
  var topicBox = document.getElementById('gl-topics');
  var panel = document.getElementById('gl-filter');
  var PAGE = 50;
  var state = { q: '', band: '', topic: '' };
  var shown = PAGE, data = null, loading = false, timer = null;

  if (moreBtn) moreBtn.hidden = false;

  function params() {
    var o = {}, s = location.search.replace(/^\?/, '');
    s.split('&').forEach(function (p) {
      if (!p) return;
      var kv = p.split('=');
      try { o[kv[0]] = decodeURIComponent((kv[1] || '').replace(/\+/g, ' ')); } catch (e) { /* bỏ qua */ }
    });
    return o;
  }

  function syncURL() {
    var parts = [];
    ['q', 'band', 'topic'].forEach(function (k) { if (state[k]) parts.push(k + '=' + encodeURIComponent(state[k])); });
    try { history.replaceState(null, '', location.pathname + (parts.length ? '?' + parts.join('&') : '')); } catch (e) { /* bỏ qua */ }
  }

  function markChips() {
    Array.prototype.forEach.call(bandBox.querySelectorAll('a'), function (a) {
      var on = (a.getAttribute('data-band') || '') === state.band;
      if (on) a.setAttribute('aria-current', 'true'); else a.removeAttribute('aria-current');
    });
    Array.prototype.forEach.call(topicBox.querySelectorAll('a'), function (a) {
      var on = a.getAttribute('data-topic') === state.topic;
      if (on) a.setAttribute('aria-current', 'true'); else a.removeAttribute('aria-current');
    });
  }

  function withData(cb) {
    if (data) return cb();
    if (loading) return;
    loading = true;
    countEl.textContent = 'Đang tải…';
    Glory.loadIndex().then(function (d) { data = d; loading = false; cb(); })
      .catch(function () { loading = false; countEl.textContent = 'Không tải được dữ liệu. Hãy thử lại.'; });
  }

  function render() {
    var res = Glory.find(data, state);
    var slice = res.slice(0, shown);
    list.innerHTML = slice.map(Glory.cardHTML).join('');
    countEl.textContent = res.length ? 'Hiển thị ' + slice.length + ' / ' + res.length + ' từ' : 'Không có từ phù hợp.';
    if (moreBtn) moreBtn.hidden = res.length <= shown;
  }

  function apply() { shown = PAGE; markChips(); syncURL(); withData(render); }

  qEl.addEventListener('input', function () {
    clearTimeout(timer);
    timer = setTimeout(function () { state.q = qEl.value; apply(); }, 150);
  });

  bandBox.addEventListener('click', function (e) {
    var a = e.target.closest('a'); if (!a) return;
    e.preventDefault();
    state.band = a.getAttribute('data-band') || '';
    apply();
  });

  topicBox.addEventListener('click', function (e) {
    var a = e.target.closest('a'); if (!a) return;
    e.preventDefault();
    var t = a.getAttribute('data-topic');
    state.topic = state.topic === t ? '' : t;
    apply();
  });

  if (moreBtn) moreBtn.addEventListener('click', function () {
    shown += PAGE;
    withData(render);
  });

  var p = params();
  if (p.q || p.band || p.topic) {
    state.q = p.q || ''; state.band = p.band || ''; state.topic = p.topic || '';
    qEl.value = state.q;
    if ((state.band || state.topic) && panel) panel.open = true;
    markChips();
    withData(render);
  }
})();
