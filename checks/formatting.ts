import assert from "node:assert/strict";
import { invoiceLabel } from "../ts_service/formatting.ts";
assert.deepEqual([0, 1, 1500, 90000].map(invoiceLabel), ["inv-0000", "inv-0001", "inv-1500", "inv-90000"]);
console.log("TypeScript invoice formatting unchanged");
