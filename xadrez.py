class Peca:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao  # (linha, coluna)

    def mover(self, destino):
        raise NotImplementedError("Cada peça deve implementar sua própria lógica de movimento.")

class Torre(Peca):
    def mover(self, destino):
        # Movimento horizontal ou vertical
        return self.posicao[0] == destino[0] or self.posicao[1] == destino[1]

class Cavalo(Peca):
    def mover(self, destino):
        dx = abs(self.posicao[0] - destino[0])
        dy = abs(self.posicao[1] - destino[1])
        return (dx, dy) in [(1, 2), (2, 1)]

def testar_movimentos():
    print("=== Teste de Movimentos ===")

    torre = Torre("Torre", (0, 0))
    print(f"Torre de {torre.posicao} para (0, 5):", "✅ Válido" if torre.mover((0, 5)) else "❌ Inválido")
    print(f"Torre de {torre.posicao} para (3, 3):", "✅ Válido" if torre.mover((3, 3)) else "❌ Inválido")

    cavalo = Cavalo("Cavalo", (1, 1))
    print(f"Cavalo de {cavalo.posicao} para (2, 3):", "✅ Válido" if cavalo.mover((2, 3)) else "❌ Inválido")
    print(f"Cavalo de {cavalo.posicao} para (3, 3):", "✅ Válido" if cavalo.mover((3, 3)) else "❌ Inválido")

if __name__ == "__main__":
    testar_movimentos()
Adiciona lógica de movimentação de Torre e Cavalo
