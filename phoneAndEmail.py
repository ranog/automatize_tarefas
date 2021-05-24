"""
phoneAndEmail.py – Encontra números de telefone e endereços de email no clipboard.

Projeto: extrator de números de telefone e de endereços de email

Suponha que você tenha a tarefa maçante de localizar todos os números de telefone e endereços de 
email em uma página web ou um documento extenso. Se fizer rolagens manualmente pela página, você
 poderá acabar fazendo a pesquisa por bastante tempo. Porém, se você tivesse um programa que 
 pudesse pesquisar o texto em seu clipboard em busca de números de telefone e de endereços de 
 email, seria possível simplesmente pressionar CTRL -A para selecionar todo o texto, CTRL -C para
  copiá-lo para o clipboard e então executar o seu programa. Ele poderia substituir o texto no 
  clipboard somente pelos números de telefone e pelos endereços de email encontrados. Sempre que 
  estiver diante de um novo projeto, pode ser tentador mergulhar diretamente na escrita do código. 
  No entanto, com muita frequência, será melhor dar um passo para trás e considerar o quadro geral. 
  Recomendo inicialmente definir um plano geral para o que seu programa deverá fazer. Não pense 
  ainda no código propriamente dito – você poderá se preocupar com ele depois. Neste momento, 
  atenha-se aos aspectos mais gerais. Por exemplo, seu extrator de números de telefone e de 
  endereços de email deverá fazer o seguinte:

• Obter o texto do clipboard.
• Encontrar todos os números de telefone e os endereços de email no texto.
• Colá-los no clipboard.

Agora você poderá começar a pensar em como isso funcionará no código. O código deverá fazer o 
seguinte:

• Usar o módulo pyperclip para copiar e colar strings.
• Criar duas regexes: uma para corresponder a números de telefone e outra para endereços de email.
• Encontrar todas as correspondências, e não apenas a primeira, para ambas as regexes.
• Formatar as strings correspondentes de forma elegante em uma única string a ser colada no 
clipboard.
• Exibir algum tipo de mensagem caso nenhuma correspondência tenha sido encontrada no texto.

Essa lista é como um roadmap (mapa) do projeto. À medida que escrever o código, você poderá focar 
em cada um desses passos separadamente. Cada passo é razoavelmente administrável e está expresso em
 termos de tarefas que você já sabe fazer em Python.
"""

import pyperclip, re

phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?  # código de área
        (\s|-|\.)?          # separador
        (\d{3})             # primeiros 3 dígitos
        (\s|-|\.)?          # separador
        (\d{4})             # últimos 4 dígitos
        (\s*(exp|x|exp.)\s*(\d{2,5}))?  # extensão
        )'''.re.VERBOSE)

# Cria a regex para email.
emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+   # nome do usuário
        @                   # símbolo @
        [a-zA-Z0-9.-]+      # nome do domínio
        (\.[a-zA-Z]{2,4})   # ponto seguido de outros caracteres
        )''', re.VERBOSE)

# TODO: Encontra correspondências no texto do clipboard.
# TODO: Copia os resultados para o clipboard.
