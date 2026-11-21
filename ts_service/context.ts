// In-memory auth/ORM doubles. This module is not a deployed Next.js server.
export const invoices: Record<string, string> = { "invoice-1": "owner" };
let caller: string | null = null;
export function setCaller(value: string | null) { caller = value; }
export async function auth() { return caller ? { user: { id: caller } } : null; }
export const db = {
  invoice: {
    async delete({ where }: { where: { id: string } }) {
      delete invoices[where.id];
    },
    async deleteMany({ where }: { where: { id: string; ownerId: string } }) {
      if (invoices[where.id] === where.ownerId) delete invoices[where.id];
    },
  },
};
