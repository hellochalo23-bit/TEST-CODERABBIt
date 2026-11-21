"use server";
import { auth, db } from "./context.ts";

export async function deleteInvoice(id: string) {
  const session = await auth();
  if (!session?.user) throw new Error("Sign-in required");
  await db.invoice.deleteMany({ where: { id, ownerId: session.user.id } });
}
