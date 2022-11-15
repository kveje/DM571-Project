const baseUrl = "http://127.0.0.1:5000";
var basketId = "";

// Shows the given products in the html format
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

// Gets inventory from API and shows the products on the product page
function getInventory() {
  axios
    .get(baseUrl + "/inventory")
    .then((response) => {
      products = response.data.data;
      console.log(`GET inventory`, products);
      showProducts(products);
    })
    .catch((error) => console.error(error));
}

// Handles the action when 'Tilføj til kurv' is used
function addToBasket(productId) {
  console.log(productId);
}

// Handles the action when 'Gennemfør ordrer' is used
function purchase(basketId) {
  console.log(basketId);
}

// What happens on refresh/loads
getInventory();
