// Получаем кнопки "+" и "-"
var plusBtn = document.querySelectorAll(".plus-btn");
var minusBtn = document.querySelectorAll(".minus-btn");

// Получаем поле ввода для количества товаров
var quantityInput = document.querySelector("input[name='quantity']");

// Обрабатываем клики на кнопку "+"
plusBtn.forEach(button => {
  button.addEventListener("click", function() {
    var quantity = parseInt(quantityInput.value);
    quantity += 1;
    quantityInput.value = quantity.toString();
  });
});

minusBtn.forEach(button => {
  button.addEventListener("click", function() {
    var quantity = parseInt(quantityInput.value);
    quantity -= 1;
    quantityInput.value = quantity.toString();
  });
});