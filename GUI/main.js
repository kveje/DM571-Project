// BaseInstance for the API
const instance = axios.create({
  baseURL: "http://localhost:5000",
  headers: { Authorization: "123456789" },
});
const ApiKey = "123456789";

// Constant UserID for illustrative purposes (since a user platform has been omitted in the example)
const uid = "123";
var basket = [];

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
      element.price.toFixed(2) +
      ` kr.</p>
      <select class="custom-select custom-select-lg" id="amount-` +
      element.id +
      `">
      <option>1</option>
      <option>2</option>
      <option>3</option>
      <option>4</option>
      <option>5</option>
    </select>
        <a id="purchase-` +
      element.id +
      `"class="btn btn-primary" onclick="addToBasket(` +
      element.id +
      `)">
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
  if (document.body.id === "products") {
    instance
      .get("/inventory")
      .then((response) => {
        products = response.data;
        showProducts(products);
      })
      .catch((error) => {
        console.error(error);
        document.getElementById("ProductPage").innerHTML =
          "<h2>Vi kan desværre ikke komme i kontakt med serveren</h2>";
      });
  }
}

function getBasket() {
  instance
    .get("/user/" + uid + "/basket")
    .then((response) => {
      basket = response.data;
      showBasket(basket);
    })
    .catch((error) => {
      console.log(error);
    });
}

function showBasket(basket) {
  let totalAmount = 0;
  let basketHtml = `<li class="list-group-item">
  <div class="row">
    <strong class="col-2">Varenummer</strong>
    <strong class="col-3">Produktnavn</strong>
    <strong class="col-2">Antal</strong>
    <strong class="col-2">Stykpris</strong>
    <strong class="col-3">Pris</strong>
  </div>
</li>`;
  basket.forEach((element) => {
    basketHtml +=
      `<li class="list-group-item">
    <div class="row">
      <p class="col-2">` +
      element.id +
      `</p>
      <p class="col-3">` +
      element.name +
      `</p>
      <p class="col-2">` +
      element.amount.toFixed(2) +
      `</p>
      <p class="col-2">` +
      element.price.toFixed(2) +
      `</p>
      <p class="col-2">` +
      (element.amount * element.price).toFixed(2) +
      `</p>
      <a class="col-1 btn btn-danger" onClick="removeFromBasket(` +
      element.id +
      `)"> Fjern
      </a>
    </div>
  </li>`;
    totalAmount += element.amount * element.price;
  });

  basketHtml +=
    `<li class="list-group-item">
  <div class="row">
    <p class="col-9">Total</p>
    <p id="total" class="col-3">` +
    totalAmount.toFixed(2) +
    `</p>
  </div>
</li>`;
  if (document.body.id == "basket") {
    document.getElementById("BasketPage").innerHTML = basketHtml;
  }
  document.getElementById("price-badge").innerHTML =
    totalAmount.toFixed(2) + " kr.";
}

// Handles the action when 'Tilføj til kurv' is used
function addToBasket(productId) {
  amount = parseInt(document.getElementById("amount-" + productId).value);
  for (var j = 0; j < basket.length; j++) {
    if (basket[j].id == productId) {
      amount += basket[j].amount;
    }
  }
  var body = {
    item_id: productId,
    item_amount: amount,
  };
  console.log(body);
  instance
    .post("/user/" + uid + "/basket", body)
    .then((response) => {
      basket = response.data;
      showBasket(basket);
    })
    .catch((error) => {
      if (error.response.status == 403) {
        console.log("Unfortunately we don't have more in stock");
      } else if (error.response.status == 400) {
        console.log("Internal error on server");
      } else if (error.response.status == 401) {
        console.log("Unauthorized apiKey");
      } else {
        console.log(error);
      }
    });
}

function removeFromBasket(productId) {
  var body = {
    item_id: productId,
  };
  instance
    .delete("/user/" + uid + "/basket", { data: body })
    .then((response) => {
      basket = response.data;
      showBasket(basket);
    })
    .catch((error) => {
      console.log(error);
    });
}

// Handles the action when 'Gennemfør ordrer' is used
function purchase() {
  if (basket.length === 0) {
    console.log("The basket is empty");
  } else {
    instance
      .post("/user/" + uid + "/order")
      .then((response) => {
        console.log(response.data);
        basket = [];
        showBasket(basket);
      })
      .catch((error) => {
        console.log(error);
      });
  }
}

// What happens on refresh/loads
getInventory();
getBasket();
