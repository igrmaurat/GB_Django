const renderItem = ({title}, count) => (
`
<li class="product-item">
    <span class="product-item__title">${title}</span>
    <span class="product-item__count">${count}</span>
</li>
`
);