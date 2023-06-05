# Projeto: Desafios de Otimização de Algoritmos

Este projeto tem como objetivo resolver problemas e otimizar algoritmos, desenvolvendo sua capacidade de implementar soluções para diversos problemas do dia a dia. Durante o projeto, você terá a oportunidade de exercitar habilidades como:

- Lógica de programação
- Capacidade de interpretação de problemas
- Capacidade de interpretação de um código legado
- Capacidade de otimização da resolução de problemas
- Resolver problemas e otimizar algoritmos sob pressão

## Configuração do Ambiente

Para garantir a qualidade do código, utilizaremos o linter Flake8, que segue as boas práticas de desenvolvimento, tornando o código mais legível e de fácil manutenção.

### Requisitos

- Python 3.10.6 ou versão anterior
- Pyenv (para controle de versões do Python)
- Ambiente virtual (virtualenv)

### Configuração do Ambiente Virtual

Siga os passos abaixo para configurar o ambiente virtual:

1. Crie o ambiente virtual:

```
python3 -m venv .venv
```

2. Ative o ambiente virtual:

```
source .venv/bin/activate
```

3. Instale as dependências do projeto:

```
python3 -m pip install -r dev-requirements.txt
```

Certifique-se de ativar o ambiente virtual sempre que estiver trabalhando no projeto.

### Execução dos Testes

Os testes são executados usando o pytest. Certifique-se de que o ambiente virtual esteja ativado antes de executar os testes.

Para executar todos os testes, utilize o seguinte comando:

```
python3 -m pytest
```

Caso deseje uma saída completa dos testes, você pode usar o seguinte comando:

```
python3 -m pytest -s -vv
```

Se desejar executar apenas um arquivo de testes específico, utilize o seguinte comando:

```
python3 -m pytest tests/nome_do_arquivo.py
```

Caso queira executar apenas uma função de teste específica, utilize o seguinte comando:

```
python3 -m pytest -k nome_da_func_de_tests
```

Para executar um teste específico de um arquivo, utilize o seguinte comando:

```
python3 -m pytest -x tests/nome_do_arquivo.py::test_nome_do_teste
```

## Desafios

Durante o projeto, você enfrentará os seguintes desafios:

1. Número de estudantes estudando no mesmo horário (Algoritmo de busca)
2. Criptografia de inversões (Testes)
3. Palíndromos (Recursividade)
4. Anagramas (Algoritmo de ordenação)
5. Encontrando números repetidos (Algoritmo de busca)
6. Palíndromos (Iteratividade)

## Como usar

Para clonar e testar o projeto em sua máquina, siga as etapas abaixo:

1. Clone o repositório:

```
git clone <URL_DO_REPOSITÓRIO>
```

2. Acesse o diretório do projeto:

```
cd <NOME_DO_DIRETÓRIO>
```

3. Configure o ambiente virtual:

```
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r dev-requirements.txt
```

4. Execute os testes:

```


python3 -m pytest
```

Agora você está pronto para explorar os desafios e otimizar os algoritmos propostos!

**Observação:** Certifique-se de ter o Python 3.10.6 ou uma versão anterior instalada em sua máquina para garantir compatibilidade com o projeto.
