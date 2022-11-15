// BaseURL for the API
const instance = axios.create({
  baseURL: "http://127.0.0.1:5000",
  headers: { Authorization: "123456789" },
});
const baseUrl = "http://127.0.0.1:5000";
const ApiKey = "123456789";

// Constant UserID for illustrative purposes (since a user platform has been omitted in the example)
const userID = "123";

// Shows the given products in html format on the product page
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
  instance
    .get("/inventory")
    .then((response) => {
      products = response.data.data;
      console.log(`GET inventory`, products);
      showProducts(products);
    })
    .catch((error) => {
      console.error(error);
      document.getElementById("ProductPage").innerHTML =
        "<h2>Vi kan desværre ikke komme i kontakt med serveren</h2>";
    });
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
