# Laboratory_Project

Alunos:
- Arthur Barbosa
- Kevin Anderson
- Maria Júlia

## 1. What (O que é?)

Um projeto de automação em Python que usa Pandas como biblioteca para coletar automaticamente dados públicos de um site de Shows, usando os conjuntos de ferramentas do Selenium como web scraping, coletando e tratando os dados e exportando-os para um arquivo .csv.

## 2. Why (Por que?)

Podemos usar os dados coletados pelo código para outros fins, como, por exemplo, em um projeto de aplicativo de agenda cultural das cidades, como a de Maceió, tais dados poderiam estar organizados dentro desse aplicativo de modo que, os usuários pudessem olhar horários, categorias dos Shows, tabela de preço, datas, gráficos comparativos entre dados antigos. Assim como poderíamos usar os dados em outro site, compartilhar tais dados com outros desenvolvedores etc. 

Além de ser uma boa prática de automações em Python, criação de DataFrames e manipulação/análise de dados. O projeto pode futuramente ser manipulado para outras funcionalidades, como coletar dados de um site de jogos, ou de filmes/séries e usa-los da mesma forma citada anteriormente.

## 3. Who (Quem participa?)

- Desenvolvedores iniciantes ou intermediários que querem aprender Web scraping, automação e análise de dados
- Usuários que desejam acessar ou consultar os títulos, categorias, horários, datas e preços de Shows de Maceió

## 4. Where (Onde será usado?)
- O código pode ser executado em um sistema Windows e Linux.
- Os dados obtidos ficam disponíveis em um arquivo .csv que pode ser usado em qualquer planilha ou software de análise.
- Bem como pode ser usado como dados base para outros projetos, como um aplicativo específico para acessar informações sobre shows de uma cidade, o exemplo usado foi da cidade de Maceió, ou em um site que compara dados em diferentes datas, como comparar preços em determinados anos, por exemplo.

## 5. When (Quando usar?)

- Sempre que for necessário analisar, acessar ou manipular os dados públicos retirados pela automação, como, usar os dados para estar “por dentro” dos Shows, preços, datas e horários, assim como sempre que surgir a necessidade de usar tais dados para outros projetos, como sites, adicioná-los em outras listas / DataFrame, aplicativos etc.
- E quando for necessário coletar os dados de forma automática.

## 6. How (Como funciona?)

- O usuário clona o repositório no GitHub.
- Instala as dependências (pip install -r requirements.txt).
- Executa o script principal (python main.py).
- O programa acessa o site Ingresso Digital, procura por Maceió no espaço de busca, depois coleta os dados, como, títulos, categorias,  preços, datas, horários etc. E organiza os dados em listas e salva no arquivo mcz_eventos.csv.


