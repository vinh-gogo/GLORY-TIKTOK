/* Glory 01 — hành vi giao diện chung: tab bar, chia sẻ, phím ←/→ ở trang từ, lọc câu hay, nút đổi theme. */
(function () {
  'use strict';

  /* Tab bar: footer của PaperMod được cache theo layout nên gán trạng thái "đang xem" bằng JS. */
  var tabs = document.querySelectorAll('#tabbar .tab');
  var path = location.pathname;
  var alias = { '/words/': '/glossary/', '/levels/': '/glossary/', '/topics/': '/glossary/', '/sets/': '/glossary/' };
  var cur = path;
  Object.keys(alias).forEach(function (k) { if (path.indexOf(k) === 0) cur = alias[k]; });
  Array.prototype.forEach.call(tabs, function (a) {
    var href = a.getAttribute('href');
    if (cur === href || (href !== '/' && cur.indexOf(href) === 0)) a.setAttribute('aria-current', 'page');
  });

  /* Chia sẻ: Web Share nếu có, nếu không thì sao chép liên kết. */
  document.addEventListener('click', function (e) {
    var b = e.target.closest('[data-share]');
    if (!b) return;
    var url = b.getAttribute('data-url') || location.href;
    var title = b.getAttribute('data-title') || document.title;
    var old = b.textContent;
    function done(msg) { b.textContent = msg; setTimeout(function () { b.textContent = old; }, 1800); }
    if (navigator.share) {
      navigator.share({ title: title, url: url }).catch(function () { /* người dùng huỷ */ });
    } else if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(url).then(function () { done('Đã sao chép liên kết'); }, function () { done('Không sao chép được'); });
    } else {
      window.prompt('Sao chép liên kết:', url);
    }
  });

  /* Trang từ: phím ←/→ chuyển từ (chỉ desktop, bỏ qua khi đang nhập liệu). */
  document.addEventListener('keydown', function (e) {
    if (e.altKey || e.ctrlKey || e.metaKey || e.shiftKey) return;
    var tag = (document.activeElement && document.activeElement.tagName || '').toLowerCase();
    if (tag === 'input' || tag === 'textarea' || tag === 'select') return;
    var el = e.key === 'ArrowLeft' ? document.getElementById('wordNavPrev') :
             e.key === 'ArrowRight' ? document.getElementById('wordNavNext') : null;
    if (el) el.click();
  });

  /* Lọc theo chủ đề ở trang Câu hay. */
  var group = document.querySelector('[data-filter-group]');
  if (group) {
    var items = document.querySelectorAll('[data-filter-items] > [data-topic]');
    group.addEventListener('click', function (e) {
      var b = e.target.closest('[data-filter]');
      if (!b) return;
      var f = b.getAttribute('data-filter');
      Array.prototype.forEach.call(group.querySelectorAll('[data-filter]'), function (x) {
        x.setAttribute('aria-pressed', x === b ? 'true' : 'false');
      });
      Array.prototype.forEach.call(items, function (it) {
        it.hidden = !!f && it.getAttribute('data-topic') !== f;
      });
    });
  }

})();
