
(function(){
  const path = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('nav a[data-nav]').forEach(a => {
    const href = a.getAttribute('href');
    if ((path === '' && href.endsWith('index.html')) || href.endsWith(path)) {
      a.classList.add('active');
    }
  });
})();
(function(){
  const search = document.getElementById('newsSearch');
  if(!search) return;
  const cards = Array.from(document.querySelectorAll('[data-news-card]'));
  const empty = document.getElementById('newsEmpty');
  function apply(){
    const q = search.value.trim().toLowerCase();
    let visible = 0;
    cards.forEach(c => {
      const text = c.textContent.toLowerCase();
      const ok = !q || text.includes(q);
      c.style.display = ok ? '' : 'none';
      if(ok) visible++;
    });
    if(empty) empty.style.display = visible ? 'none' : '';
  }
  search.addEventListener('input', apply);
  apply();
})();
(function(){
  const form = document.getElementById('subscribeForm');
  const ok = document.getElementById('subscribeOk');
  if(!form || !ok) return;
  form.addEventListener('submit', (e)=>{
    e.preventDefault();
    ok.textContent = 'Rahmat! Obunangiz qabul qilindi.';
    ok.classList.add('success');
    form.reset();
  });
})();
(function(){
  const form = document.getElementById('contactForm');
  if(!form) return;
  form.addEventListener('submit', (e)=>{
    e.preventDefault();
    alert('Xabaringiz yuborildi! (demo)');
    form.reset();
  });
})();
