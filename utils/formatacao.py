def formatar_moeda(valor: float) -> str:
  return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")