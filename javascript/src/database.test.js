import { Database } from './database';

test('able to access product database', () => {
  let db = new Database();
  let sugar = db.getProduct("sugar");
  expect(sugar).toBeDefined();
  expect(sugar.price).toBe(0.65);
  expect(sugar.taxRate).toBe(0.07);
  expect(db.getProduct("red wine")).toBeDefined();
});
