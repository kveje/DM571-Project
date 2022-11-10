const Inventory = [
  {
    id: 1,
    stock_lvl_local: 5,
    stock_lvl_supplier: 5,
    supplier: "Supplier A",
    photo_url:
      "https://cdn.shopify.com/s/files/1/2807/7652/products/Nexgrill_Pro_Wok_website.png?v=1559905032",
    price: 20.0,
    name: "Wok",
    description: "Den Ægte Pande. Approved af det ægte karryfarvede folk!",
  },
  {
    id: 2,
    stock_lvl_local: 5,
    stock_lvl_supplier: 5,
    supplier: "Supplier A",
    photo_url:
      "https://upload.wikimedia.org/wikipedia/commons/3/38/Jamie_Oliver_%28cropped%29.jpg",
    price: 189.95,
    name: "Jamie Oliver",
    description:
      "Han laver mad på pander og fik skæld ud af en gonger fordi han ikke stegte gode ris",
  },
  {
    id: 3,
    stock_lvl_local: 5,
    stock_lvl_supplier: 5,
    supplier: "Supplier A",
    photo_url:
      "https://politiken.dk/imagevault/publishedmedia/4vnqctmr536aotcbtq58/combekk-pander3.jpg",
    price: 2.75,
    name: "GenbrugsPande",
    description:
      "Denne Pande er genbrugt og god for miljøet. God til vegansk mad",
  },
  {
    id: 4,
    stock_lvl_local: 5,
    stock_lvl_supplier: 5,
    supplier: "Supplier A",
    photo_url:
      "https://pandasia.dk/wp-content/uploads/Produkter/Non-food/hot-pot-fondue.jpg.webp",
    price: 649.95,
    name: "Selvvarmende Pande",
    description:
      "Denne Pande består af en lækker jern-legering, der bliver varm hvis man putter den i stikkontakten",
  },
  {
    id: 5,
    stock_lvl_local: 5,
    stock_lvl_supplier: 5,
    supplier: "Supplier A",
    photo_url:
      "https://www.kramogkanel.dk/wp-content/uploads/2020/01/1026569-Fiskars-Norden-cast-iron-frying-pan-26cm-1.jpg",
    price: 649.95,
    name: "Støbejernspande",
    description:
      "Denne Pande består af en lækker jern-legering - den giver hård jern",
  },
  {
    id: 6,
    stock_lvl_local: 5,
    stock_lvl_supplier: 5,
    supplier: "Supplier A",
    photo_url:
      "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Giant_Panda_2004-03-2.jpg/1280px-Giant_Panda_2004-03-2.jpg",
    price: 1000000.99,
    name: "Panda",
    description: "Denne pande er lidt delikat, men af god kinesisk kvalitet",
  },
];

var Basket = [];

function purchase(id) {
  console.log(id);
}

function showProducts(products) {
  let productHtml = "";
  products.forEach((element) => {
    productHtml +=
      `<div class="col-md-4 my-3">
    <div class="card">
      <div class="embed-responsive embed-responsive-16by9">
      <img class="card-img-top embed-responsive-item" src="` +
      element.photo_url +
      `" alt="Card image cap"/>
      </div>
      <div class="card-body">
        <h5 class="card-title">` +
      element.name +
      `</h5>
        <p class="card-text">` +
      element.description +
      `</p>
      <p class="">` +
      element.price +
      ` kr.</p>
        <a id="` +
      element.id +
      `"class="btn btn-primary" onclick="addToBasket(id)">
          Tilføj til kurv
        </a>
      </div>
    </div>
  </div>`;
  });
  document.getElementById("ProductPage").innerHTML = productHtml;
}

function addToBasket(id) {
  console.log(id);
}
