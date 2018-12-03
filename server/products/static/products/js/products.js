const renderProduct = ({id, title, image}) => (
  `
    <div class="catalog">
      <img class="product__image" src="${ image }">
      <a class="product__link" href="/products/${ id }">
      ${ title }
      </a>
  </div>
  `
);