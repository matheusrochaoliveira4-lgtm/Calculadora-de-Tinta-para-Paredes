import math

def calcular_latas_e_valor(area_metros_quadrados):
    """
    Calcula a quantidade de latas de tinta e o custo total
    com base na área em metros quadrados.

    Args:
        area_metros_quadrados (float): A área a ser pintada em m².

    Returns:
        tuple: Uma tupla contendo (numero_latas, custo_total).
    """
    rendimento_por_litro = 3  # m² por litro
    litros_por_lata = 18    # litros por lata
    preco_por_lata = 120.00 # R$ por lata

    litros_necessarios = area_metros_quadrados / rendimento_por_litro
    latas_necessarias = math.ceil(litros_necessarios / litros_por_lata)
    valor_total = latas_necessarias * preco_por_lata

    return latas_necessarias, valor_total

if __name__ == "__main__":
    try:
        area_input = float(input("Digite a área a ser pintada em m²: "))
        if area_input < 0:
            print("A área não pode ser um valor negativo.")
        else:
            latas, valor = calcular_latas_e_valor(area_input)
            print(f"Você precisará de {latas} lata(s) de tinta.")
            print(f"O custo total será de R${valor:.2f}.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número para a área.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")