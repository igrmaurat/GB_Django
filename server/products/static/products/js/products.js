const renderProduct = ({id, title, image}) => (
  `
    <div class="catalog">
      <img class="product__image" src="${ image }">
      <span class="product__name">
          ${ title }
      </span>
      <a class="product__link" href="/products/${ id }">
      </a>
  </div>
  `
);