let element = document.querySelector('#price');

let price = element.value;
let name_ = element.classList

let priceFormat = price.replace(',', '.')

element.value = priceFormat

document.querySelector('#price').addEventListener('keyup', (event) => {
  const el = event.target;
  if (el.value.includes(',')) {
    el.value = el.value.replace(/,/g, '.');
  }
});


