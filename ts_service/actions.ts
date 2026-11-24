"use server";
import { db } from "./context.ts";

export async function deleteInvoice(id: string) {
  await db.invoice.delete({ where: { id } });
}
