
<div align="center">

# Relatório de Bugs
### Calculadora Científica em Python

**Projeto acadêmico · Testes de software · TDD**

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/status-em%20an%C3%A1lise-orange)
![TDD](https://img.shields.io/badge/metodologia-TDD-purple)

</div>

---

## Sobre o projeto

Este documento apresenta os defeitos identificados durante a análise do código-fonte `Calculadora.py`, desenvolvido em Python.

Cada ocorrência está documentada com sua identificação, localização, descrição, passos para reprodução, resultados esperado e obtido, severidade, impacto e sugestão de correção.

> **Nota:** os defeitos foram inicialmente identificados por análise estática do código. Os roteiros de reprodução e as evidências devem ser confirmados por execução no ambiente local antes da entrega final.

## Visão geral dos defeitos

| ID | Defeito | Severidade | Status |
|:--|:--|:--:|:--:|
| BUG-001 | Resultado incorreto na adição | Média | Identificado |
| BUG-002 | Cálculo incorreto do fatorial | Alta | Selecionado para TDD |
| BUG-003 | Função inexistente no logaritmo natural | Alta | Identificado |
| BUG-004 | Aceitação de zero no logaritmo | Média | Identificado |
| BUG-005 | Opção de seno não implementada | Média | Identificado |
| BUG-006 | Função de cosseno não definida | Alta | Identificado |
| BUG-007 | Função de tangente não definida | Alta | Identificado |
| BUG-008 | Ausência de tratamento para divisão por zero | Média | Identificado |
| BUG-009 | Logaritmo calculado na base incorreta | Alta | Identificado |

## Índice

1. [BUG-001 — Adição](#bug-001--resultado-incorreto-na-operação-de-adição)
2. [BUG-002 — Fatorial](#bug-002--cálculo-incorreto-do-fatorial)
3. [BUG-003 — Logaritmo natural](#bug-003--chamada-de-função-inexistente-no-logaritmo-natural)
4. [BUG-004 — Logaritmo de zero](#bug-004--aceitação-de-zero-no-logaritmo-de-base-10)
5. [BUG-005 — Seno](#bug-005--opção-de-seno-exibida-no-menu-mas-não-implementada)
6. [BUG-006 — Cosseno](#bug-006--chamada-de-função-não-definida-na-opção-de-cosseno)
7. [BUG-007 — Tangente](#bug-007--chamada-de-função-não-definida-na-opção-de-tangente)
8. [BUG-008 — Divisão](#bug-008--ausência-de-tratamento-para-divisão-por-zero)
9. [BUG-009 — Logaritmo de base 10](#bug-009--uso-de-logaritmo-natural-na-função-de-logaritmo-de-base-10)

---


##  Relatórios individuais

<details>
<summary><strong>BUG-001 — Resultado incorreto na operação de adição</strong>  Média</summary>

**Localização:** `Calculadora.py`, linha 4 — função `adicao(x, y)`.

**Descrição:**

A expressão `x + np.add(x, y)` soma o primeiro operando ao resultado da operação `x + y`. Dessa forma, a função calcula `2x + y`, em vez de realizar somente `x + y`.

**Passos para reprodução:**

1. Executar o programa em um ambiente Python com NumPy instalado.
2. Chamar `adicao(2, 3)` ou selecionar a opção 1 e informar os valores 2 e 3.
3. Observar o resultado.

**Resultado esperado:** `5`.

**Resultado obtido:** `7`.

**Impacto:** compromete a confiabilidade da operação de adição, apresentando resultados matematicamente incorretos.

**Sugestão de correção:** retornar a soma de `x` e `y` uma única vez.

**Evidências:** adicionar captura de tela ou log da execução.

**Data de identificação:** 09/11/2026.

**Status:** identificado por análise estática; reprodução pendente.

</details>

<details>
<summary><strong>BUG-002 — Cálculo incorreto do fatorial</strong> 🔴 Alta · Selecionado para TDD</summary>

**Localização:** `Calculadora.py`, linhas 23–27 — função `fatorial(x)`.

**Descrição:**

O laço utiliza `range(x+1)`, que começa em zero. Como o acumulador é multiplicado por zero na primeira iteração, o resultado final é zero para entradas inteiras não negativas.

**Passos para reprodução:**

1. Executar o programa em um ambiente Python.
2. Chamar `fatorial(5)` ou selecionar a opção 7 e informar 5.
3. Observar o resultado.

| Entrada | Resultado esperado | Resultado obtido |
|:--|--:|--:|
| `fatorial(5)` | 120 | 0 |
| `fatorial(0)` | 1 | 0 |

**Impacto:** a funcionalidade de fatorial não produz resultados matematicamente válidos para entradas inteiras não negativas.

**Sugestão de correção:** ajustar o intervalo de iteração para multiplicar apenas os inteiros positivos necessários, preservando o caso `0! = 1`.

**Evidências:**
- RED: 3 testes falharam na implementação original.
- GREEN: 3 testes passaram após a correção.
- Regressão: teste adicional para `fatorial(6) = 720`.

**Data de identificação:** 09/11/2026.

**Status:** corrigido e validado por TDD.

</details>

<details>
<summary><strong>BUG-003 — Chamada de função inexistente no logaritmo natural</strong> 🔴 Alta</summary>

**Localização:** `Calculadora.py`, linha 32 — função `logaritmo_natural(x)`.

**Descrição:**

A implementação chama `np.ln(x)`. O NumPy disponibiliza `np.log(x)` para calcular o logaritmo natural, mas não possui a função `np.ln`.

**Passos para reprodução:**

1. Executar o programa em um ambiente com NumPy instalado.
2. Chamar `logaritmo_natural(1)` ou selecionar a opção 8 e informar 1.
3. Observar a exceção.

**Resultado esperado:** retornar `0`, pois `ln(1) = 0`.

**Resultado obtido:** exceção `AttributeError`, devido à chamada a `np.ln`.

**Impacto:** impede a execução da operação de logaritmo natural para entradas positivas.

**Sugestão de correção:** utilizar a função do NumPy correspondente ao logaritmo natural.

**Evidências:** anexar o traceback apresentado no terminal.

**Data de identificação:** 09/11/2026.

**Status:** identificado por análise estática; reprodução pendente.

</details>

<details>
<summary><strong>BUG-004 — Aceitação de zero no logaritmo de base 10</strong> 🟡 Média</summary>

**Localização:** `Calculadora.py`, linhas 34–37 — função `logaritmo_base10(x)`.

**Descrição:**

A validação rejeita valores menores que zero (`x < 0`), mas permite que zero prossiga para o cálculo. O logaritmo de zero não está definido no conjunto dos números reais.

**Passos para reprodução:**

1. Executar o programa em um ambiente com NumPy instalado.
2. Chamar `logaritmo_base10(0)` ou selecionar a opção 9 e informar zero.
3. Observar o retorno ou aviso produzido pelo NumPy.

**Resultado esperado:** rejeitar zero e informar que o argumento deve ser positivo.

**Resultado obtido:** a entrada chega a `np.log(0)`, podendo produzir `-inf` e aviso de divisão por zero.

**Impacto:** permite uma entrada fora do domínio matemático da operação e pode apresentar um valor não finito.

**Sugestão de correção:** rejeitar valores menores ou iguais a zero.

**Evidências:** registrar a saída e os avisos do terminal.

**Data de identificação:** 09/11/2026.

**Status:** identificado por análise estática; reprodução pendente.

</details>

<details>
<summary><strong>BUG-005 — Opção de seno exibida no menu, mas não implementada</strong> 🟡 Média</summary>

**Localização:** `Calculadora.py`, linha 52 e função `calculadora_cientifica()`.

**Descrição:**

O menu apresenta a opção `10. Seno`, mas não existe um bloco condicional que trate a escolha `'10'`. A opção cai no bloco `else`, que informa que a operação é inválida.

**Passos para reprodução:**

1. Iniciar o programa.
2. Digitar `10` no menu.
3. Observar a mensagem exibida.

**Resultado esperado:** solicitar um ângulo e apresentar o seno correspondente.

**Resultado obtido:** `Operação inválida. Tente novamente.`

**Impacto:** uma funcionalidade anunciada ao usuário não pode ser utilizada.

**Sugestão de correção:** implementar o tratamento da opção 10 e a função de cálculo correspondente, definindo também a unidade angular esperada.

**Evidências:** registrar a interação com o menu no terminal.

**Data de identificação:** 09/11/2026.

**Status:** identificado por análise estática; reprodução pendente.

</details>

<details>
<summary><strong>BUG-006 — Chamada de função não definida na opção de cosseno</strong> 🔴 Alta</summary>

**Localização:** `Calculadora.py`, linhas 53 e 93–95.

**Descrição:**

Ao selecionar a opção 11, o programa chama `cosseno(x)`, mas não há definição dessa função no código fornecido.

**Passos para reprodução:**

1. Iniciar o programa.
2. Digitar `11` no menu.
3. Informar um valor para o ângulo.
4. Observar a exceção.

**Resultado esperado:** calcular e apresentar o cosseno do ângulo informado.

**Resultado obtido:** exceção `NameError`, pois `cosseno` não está definido.

**Impacto:** a operação de cosseno não pode ser concluída.

**Sugestão de correção:** implementar a função `cosseno` e definir se a entrada será recebida em graus ou radianos.

**Evidências:** anexar o traceback apresentado no terminal.

**Data de identificação:** 09/11/2026.

**Status:** identificado por análise estática; reprodução pendente.

</details>

<details>
<summary><strong>BUG-007 — Chamada de função não definida na opção de tangente</strong> 🔴 Alta</summary>

**Localização:** `Calculadora.py`, linhas 54 e 97–99.

**Descrição:**

Ao selecionar a opção 12, o programa chama `tangente(x, radianos=False)`, mas não há definição da função `tangente` no código fornecido.

**Passos para reprodução:**

1. Iniciar o programa.
2. Digitar `12` no menu.
3. Informar um valor para o ângulo.
4. Observar a exceção.

**Resultado esperado:** calcular e apresentar a tangente do ângulo informado.

**Resultado obtido:** exceção `NameError`, pois `tangente` não está definida.

**Impacto:** a operação de tangente não pode ser concluída.

**Sugestão de correção:** implementar a função `tangente`, incluindo o tratamento dos ângulos nos quais a tangente não está definida.

**Evidências:** anexar o traceback apresentado no terminal.

**Data de identificação:** 09/11/2026.

**Status:** identificado por análise estática; reprodução pendente.

</details>

<details>
<summary><strong>BUG-008 — Ausência de tratamento para divisão por zero</strong>  Média</summary>

**Localização:** `Calculadora.py`, linhas 12–13 — função `divisao(x, y)`.

**Descrição:**

A função realiza diretamente a operação `x / y`, sem verificar se o divisor é zero ou apresentar uma mensagem controlada para essa situação.

**Passos para reprodução:**

1. Executar o programa em um ambiente Python.
2. Chamar `divisao(1, 0)` ou selecionar a opção 4 e informar 1 e 0.
3. Observar o comportamento.

**Resultado esperado:** informar que não é possível dividir por zero, sem interromper inesperadamente a interação.

**Resultado obtido:** com os valores convertidos para `float` pelo menu, a operação provoca `ZeroDivisionError`.

**Impacto:** uma entrada inválida pode interromper a execução normal da calculadora.

**Sugestão de correção:** verificar se o divisor é zero antes da operação e tratar a situação de forma consistente com as demais funções.

**Evidências:** anexar o traceback apresentado no terminal.

**Data de identificação:** 09/11/2026.

**Status:** identificado por análise estática; reprodução pendente.

</details>

<details>
<summary><strong>BUG-009 — Logaritmo calculado na base incorreta</strong> 🔴 Alta</summary>

**Localização:** `Calculadora.py`, linha 37 — função `logaritmo_base10(x)`.

**Descrição:**

A função utiliza `np.log(x)`, que calcula o logaritmo natural, embora o nome da função e a opção do menu indiquem logaritmo na base 10.

**Passos para reprodução:**

1. Executar o programa em um ambiente com NumPy instalado.
2. Chamar `logaritmo_base10(100)` ou selecionar a opção 9 e informar 100.
3. Comparar o resultado com o valor matemático esperado para base 10.

| Comportamento | Resultado |
|:--|--:|
| Esperado | 2 |
| Obtido | Aproximadamente 4,60517 |

**Impacto:** a função apresenta resultados incorretos para uma operação científica anunciada como logaritmo de base 10.

**Sugestão de correção:** utilizar a função do NumPy específica para logaritmo na base 10.

**Evidências:** registrar a saída do terminal.

**Data de identificação:** 09/11/2026.

**Status:** identificado por análise estática; reprodução pendente.

</details>


---

## Plano de correção com TDD

O **BUG-002 — Cálculo incorreto do fatorial** foi selecionado para demonstrar a metodologia *Test-Driven Development*.

A correção seguirá o ciclo:

| Etapa | Atividade | Evidência esperada |
|:--|:--|:--|
| 🔴 RED | Escrever um teste que represente o comportamento correto e executá-lo antes da correção. | Teste falhando pelo defeito identificado. |
| 🟢 GREEN | Alterar minimamente a implementação para atender ao teste. | Teste passando. |
| 🔵 REFACTOR | Melhorar o código, se necessário, sem alterar o comportamento esperado. | Todos os testes continuam passando. |

Após a execução e validação, o status do BUG-002 deverá ser atualizado para **Resolvido**, acompanhado dos resultados dos testes.

---

<div align="center">

**Relatório de acompanhamento da atividade**

*Análise de defeitos · Python · Testes automatizados · TDD*

</div>
