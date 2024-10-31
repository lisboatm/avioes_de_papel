# README - Campeonato de Aviões de Papel

## Descrição

Este programa determina se a quantidade de folhas de papel especial compradas pela diretora é suficiente para atender a todos os competidores em um campeonato de aviões de papel. O campeonato contará com um número específico de competidores, e cada competidor receberá uma quantidade fixa de folhas de papel. O programa calcula se o total de folhas compradas é suficiente.

## Problema

Dada a quantidade de competidores (C), a quantidade de folhas de papel especial compradas (P), e a quantidade de folhas que cada competidor deve receber (F), o programa deve verificar se:

- \( P \geq C \times F \)

## Entrada

A entrada consiste em uma única linha contendo três números inteiros positivos:

- \( C \) (1 ≤ C ≤ 1000): O número de competidores.
- \( P \) (1 ≤ P ≤ 1000): A quantidade de folhas de papel especial compradas pela diretora.
- \( F \) (1 ≤ F ≤ 1000): A quantidade de folhas de papel que cada competidor deve receber.

## Saída

O programa deve imprimir uma única linha com um dos seguintes caracteres:

- `'S'` se a quantidade de folhas compradas é suficiente.
- `'N'` se a quantidade de folhas compradas não é suficiente.

## Exemplo de Entrada e Saída

### Exemplo 1
- **Entrada:**
  ```
  10 100 10
  ```
- **Saída:**
  ```
  S
  ```

### Exemplo 2
- **Entrada:**
  ```
  10 90 10
  ```
- **Saída:**
  ```
  N
  ```

### Exemplo 3
- **Entrada:**
  ```
  5 40 2
  ```
- **Saída:**
  ```
  S
  ```

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Copie o código fornecido para um arquivo Python (ex: `campeonato_aviões.py`).
3. Execute o arquivo no terminal ou prompt de comando:
   ```bash
   python campeonato_aviões.py
   ```
4. Insira os valores de entrada conforme o formato especificado.

## Considerações Finais

Este problema foi inspirado na OBI - Olimpíada Brasileira de Informática 2009, Fase 1, Nível 1. É um ótimo exercício para praticar lógica de programação e manipulação de entradas e saídas.
