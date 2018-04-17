export class Database {
  constructor(fileName = "../../products.json") {
    let products = require(fileName);
    this.productsById = new Map(products.map(p => [p.productId, p]));
  }

  getProduct(productId) {
    return this.productsById.get(productId);
  }
}
