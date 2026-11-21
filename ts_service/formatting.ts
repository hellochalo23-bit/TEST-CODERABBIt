export function invoiceLabel(identifier: number): string {
  const padded = String(identifier).padStart(4, "0");
  return `inv-${padded}`;
}
