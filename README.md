# Automação de testes - Sauce Demo

Projeto base para automação de testes web com Selenium + Pytest, seguindo a estrutura de Page Objects.

## Estrutura

- `tests/pages`: objetos de página
- `tests/transactions`: fluxos de negócio
- `tests/specs`: cenários de teste
- `features/`: exemplos em Gherkin para uso com Behave / BDD

## Como executar

1. Crie o ambiente virtual:
   `python -m venv venv`
2. Ative o ambiente:
   `venv\Scripts\activate`
3. Instale dependências:
   `pip install -r requirements.txt`
4. Rode os testes:
   `pytest -q`

## Usuários de exemplo

- `standard_user` / `secret_sauce`
- `locked_out_user` / `secret_sauce`
