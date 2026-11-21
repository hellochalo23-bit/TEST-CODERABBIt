import assert from "node:assert/strict";
import { invoices, setCaller } from "../ts_service/context.ts";
import { deleteInvoice } from "../ts_service/actions.ts";

setCaller(null);
let rejected = false;
try { await deleteInvoice("invoice-1"); }
catch (error: any) {
  if (error.message !== "Sign-in required") throw error;
  rejected = true;
}
if (!rejected || invoices["invoice-1"] !== "owner") {
  console.log(JSON.stringify({case:"auth",passed:false,anonymous_rejected:rejected,anonymous_mutated:invoices["invoice-1"] !== "owner"}));
  process.exit(1);
}
setCaller("other-owner");
await deleteInvoice("invoice-1");
assert.equal(invoices["invoice-1"], "owner");
setCaller("owner");
await deleteInvoice("invoice-1");
assert.equal(invoices["invoice-1"], undefined);
console.log(JSON.stringify({case:"auth",passed:true,anonymous_rejected:true,anonymous_mutated:false,other_owner_preserved:true,owner_deleted:true}));
