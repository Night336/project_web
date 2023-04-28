const cartLink = document.querySelector('#cart-count');

cartLink.addEventListener('click', () => {
  const popup = document.querySelector('#cart-popup');
  popup.style.display = 'block';
  console.log("Привет");
});

document.addEventListener('keydown', (event) => {
    console.log('ескейп');
  const popup = document.querySelector('#cart-popup');
  if (event.key === 'Escape') {
    popup.style.display = 'none';
  }
});

document.addEventListener('click', (event) => {
  const popup = document.querySelector('#cart-popup');
  if (!popup.contains(event.target) && event.target !== cartLink) {
    popup.style.display = 'none';
  }
});