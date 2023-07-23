"""
Faça um código em Python para resolver o seguinte desafio:

Cria uma variável com o seguinte texto: 
    "123, 2-234000, ABXD234234 e 23000".
Você deve retornar: 
    1-0000123000, 2-0000234000, 1-ABXD234234 e 1-0000023000,

sendo que o software deve ser em loop e identificar os casos
que precisa de cada manutenção.

Script deve ser comentado e se não conseguir ser finalizado
deve ser escrito em português os passos que iria ter que
adotar para conseguir fazer
"""
import re


def format_string(text: str) -> str:
    """
    Formata uma string no formato '{x}-{y}', onde x é um 
    caractere inicial e y são os 10 caracteres restantes.
    - Caso a string já possua um caractere inicial 'x', 
      apenas o utiliza.
    - Preenche com 3 zeros à direita e o tamanho que 
      sobrar à esquerda.
    - Caso já hajam 3 ou mais zeros à esquerda, apenas 
      os coloca à direita num total de até 10 dígitos.
    - Caso a string já tenha 10 dígitos, apenas coloca o 
      dígito inicial x.

    Args:
        text (str): A string a ser formatada.

    Returns:
        formatted_text (str): A string formatada.
    """
    # Obtém o caractere inicial
    initial_char = text[0] if text[1] == '-' else '1'

    # Remove padrẽs de prefixo no text original
    text = re.sub(r'^\d+-', '', text)

    # Preenche com zeros à esquerda se necessário
    if text[-3:] != '000' and len(text) < 10:
        text = text + '000'

    # Preenche com zeros à esquerda se necessário
    if len(text) < 10:
        text = text.zfill(10)

    # Obtém os 10 caracteres finais
    final_chars = text[-10:]

    # Formata a string no formato desejado
    formatted_string = f'{initial_char}-{final_chars}'

    return formatted_string


if __name__ == "__main__":
    EXEMPLO = "123, 2-234000, ABXD234234 e 23000"
    RETORNO = []

    for word in re.split(', | e ', EXEMPLO):
        RETORNO.append(format_string(word))

    FORMATED = f'{RETORNO[0]}, {RETORNO[1]}, {RETORNO[2]} e {RETORNO[3]}'

    assert FORMATED == '1-0000123000, 2-0000234000, 1-ABXD234234 e 1-0000023000'
