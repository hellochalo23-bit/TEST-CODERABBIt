export function invoiceLabel(identifier: number): string {
  return "inv-" + String(identifier).padStart(4, "0");
}
