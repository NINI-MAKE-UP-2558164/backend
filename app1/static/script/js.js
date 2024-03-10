
let cartItems = [];
let cartCount = document.querySelector('.cart-count');
let cartContainer = document.getElementById('cart-container');
let cartClose = document.getElementById('cart-close');
let cartItemsList = document.getElementById('cart-items').querySelector('ul');
let cartTotal = document.getElementById('cart-total');

function updateCartCount() {
  cartCount.innerText = cartItems.length;
}

function updateCart() {
  // Limpiar lista de elementos del carrito
  cartItemsList.innerHTML = '';

  // Agregar cada elemento del carrito a la lista
  for (let item of cartItems) {
    let li = document.createElement('li');
    li.innerText = item.name + ' - $' + item.price.toFixed(2);
    cartItemsList.appendChild(li);
  }

  // Calcular total del carrito y mostrarlo
  let total = cartItems.reduce((acc, item) => acc + item.price, 0);
  cartTotal.innerText = 'Total: $' + total.toFixed(2);

  // Actualizar contador de elementos del carrito
  updateCartCount();
}

function addToCart(item) {
  cartItems.push(item);
  updateCart();
}

function toggleCart() {
  cartContainer.classList.toggle('show');
}

function initCart() {
  // Agregar evento de clic al ícono del carrito para mostrar/ocultar el carrito
  document.getElementById('cart-icon').addEventListener('click', toggleCart);

  // Agregar evento de clic al botón de cerrar para ocultar el carrito
  cartClose.addEventListener('click', toggleCart);

  // Agregar algunos productos al carrito de ejemplo
  addToCart({ name: 'Producto 1', price: 10 });
  addToCart({ name: 'Producto 2', price: 20 });
}

initCart();
