# PRINCÍPIOS DE DESIGN

* DbC - Design by Contract
* Programação Defensiva


# PROGRAMAÇÃO DEFENSIVA

Neste estilo de programação, o objetivo é tornar cada parte do código (objetos, métodos ou funções) capazes de se proteger contra entradas inválidas (ANAYA, p. 78). 

Então a principal estratégia é como lidar com os erros para cenários que podemos esperar que ocorram e como lidar com erros que nunca deverão ocorrer.
Não deixar o programa falhar silenciosamente, mas de maneira graciosa é uma boa prática para aumentar a qualidade do software (ANAYA, p. 88). O programa pode mostrar uma mensagem de erro padrão e também registrar (em arquivos logs) os detalhes do erro interno. Então os erros podem ser fontes de informação preciosa para os desenvolvedores e até mesmo para os usuários.

Esta técnica pode ser combinada outros princípios de design, um comlementando o outro, como no caso com o DbC.


## 1. ERROR HANDLING

Procedimentos de tratamento de erros são um recursos para quando identificados causas potenciais de erros. Este tipo de evento é muito frequente em casos de **entrada de dados**.

O ideia por detrás do tratamento de erros é <u>responder graciosamente</u> a erros esperados na tentativa de ou fazer o programa continuar a execução ou decidir por interromper o programa caso o erro seja incontornável.

Algumas aboradagens possíveis de tratatamento de erros são:

1. Substituição de valores
2. Log de erro
3. Manuseio de exceções

### 1.1. Substituição de Valor

Uma das formas de tratar erros é através do controle dos valores que são usados como entradas e saídas das entidades.


### 2. ASSERTION

Quando o erro não pode ser contornado, ou seja, o programa não pode se auto-curar (*self-heal*) e a melhor solução é interromper a execução do programa, a estratégia de fazer falhar rapidamente e fazer o erro ser notado pode ser usado no programa. Com isso, ele pode ser economizado recursos e identificado um ponto para melhoria nas próximas versões.

O mecanismo de `assertion` é então usado em situações que nunca deveriam ocorrer, indicando um condição impossível para o funcionamento do programa. Com isso, é possível evitar outros problemas causados por uma falha e o consumo de processamento sobre premissas falsas (ANAYA, p. 88).

**COMPARAÇÃO COM *EXCEPTION HANDLING***

A implementação do `assertion` pode ser semelhante a uma declaração condicional com `raise` (*exception raising*).

```python
if condition:
    raise Exception
```

A principal diferença está que o *exception handling* é usado usualmente para lidar com <u>situações indesejadas em relação à <b>lógica de negócio</b> que o programa deve considerar</u>. Enquanto isso, o `assertion` é como um mecanismo de auto-verificação no códiugo, para verificar a sua precisão. Desta maneira, o *exception raising* é muito mais frequente do que o `assertion`.


**IMPLEMENTAÇÃO**

O `assertion` é uma condição Booleana que deve ser verdadeira para que o programa esteja correto. A falha por `AssertionError` indica que um defeito conhecido foi revelado.

Com isso em mente é possível concluir algumas boas práticas do uso do `assertion`:

* Não devem ser usados para validar a lógica do negócio;
* Não deve ser usado como um mecanismo de controle de fluxo (*control flow*);
* Não usar o `except AssertionError` para **contornar um problema**. Isso pode ser confuso para o leitor. Nestes casos, o recomendado é usar erros mais específicos.
* Ao invés do programa quebrar diretamente, construir uma falha elegante: 
    * mensagem de erro genérico; 
    * registro de log com detalhes internos do erro.
* Quando uma parte errada é encontrada no programa, ele deve ser finalizado. 
* Não usar uma chamadas de função diretamente como validação da `assertion`. Isso dificulta a validação no debuging. Tente usar **expressões com variáveis locais**.


```python
# Má prática
try:
    assert condition.holds(), "Condition is not satisfied"
except AssertionError:
    alternative_procedure()
```

```python
# Boa prática
result = condition.holds()
assert result > 0, f"Error with {result}"
```