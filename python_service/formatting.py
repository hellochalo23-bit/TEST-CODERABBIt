def invoice_label(identifier):
    padded = format(identifier, "04d")
    return "inv-" + padded
