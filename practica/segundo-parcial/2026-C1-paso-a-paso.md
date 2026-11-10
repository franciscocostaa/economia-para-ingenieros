# Segundo parcial 1C2026 — resolución paso a paso

Recorrido guiado del parcial del 16/06/2026, pensado para alguien que **no cursó las clases**: cada término técnico se define la primera vez que aparece y cada paso explica *por qué* se hace, no solo *cómo*.

- **Respuestas y auditoría de la resolución oficial:** [2026-C1](2026-C1.md). Esta página enseña el camino; esa página tiene los números finales y la comparación contra [R03].
- **Fórmulas sueltas para consulta rápida:** [hoja de fórmulas](../../wiki/hoja-de-formulas.md).
- **Modalidad del parcial del 17/11/2026** (Excel, sin internet): [segundo parcial](../../wiki/temas/segundo-parcial.md#modalidad-del-parcial-del-17112026).

Se trabaja con los datos del **tema 1** [P02, p. 1]. Los del tema 2 están en [2026-C1](2026-C1.md#diferencias-entre-temas).

## Estado de avance

| Ejercicio | Estado |
|---|---|
| Problema 1 — préstamos | **Resuelto y explicado abajo** |
| Problema 2 — proyecto MAXIMILIEN (valor actual neto) | Pendiente; enunciado y resolución oficial en [2026-C1](2026-C1.md#problema-2-proyecto-maximilien-croissants) |
| Preguntas teóricas (10 verdadero/falso) | Pendiente; respuestas oficiales en [2026-C1](2026-C1.md#preguntas-teóricas-vf) |

**Orden sugerido:** los dos problemas primero y los verdadero/falso al final. Los problemas son mecánicos y se aprenden desde cero; los verdadero/falso exigen tener ya incorporados contabilidad, análisis financiero y costos, así que rinden más cuando los problemas ya enseñaron el vocabulario.

---

# Problema 1 — Préstamos

## Enunciado

> Una pyme tiene dos préstamos con el mismo banco, **ambos tomados a fin de diciembre de 2025**:
>
> **i. Préstamo alemán:** $1.000.000, 48 cuotas mensuales, tasa nominal anual 12,5 % con capitalización trimestral.
> **ii. Préstamo bullet:** $500.000, pagos semestrales, tasa semestral 6 %, a pagar en 4 años.
>
> **a)** ¿Cuánto pagará de interés con cada opción a fin de diciembre de 2026? ¿Cuál de los dos sistemas es más conveniente? Justifique numéricamente.
> **b)** El banco ofrece refinanciar el total adeudado entre ambos préstamos a fin de diciembre de 2026, con sistema francés en 25 cuotas al 0,5 % mensual. ¿Cuál es el saldo deudor total a esa fecha? ¿Cuál es la nueva cuota?

Detalle que se pasa por alto: la empresa **tiene los dos préstamos a la vez**, no está eligiendo entre ellos. Debe $1.500.000 en total. La pregunta "cuál conviene" es teórica: cuál de los dos mecanismos resulta más barato.

## Vocabulario

Todo préstamo se describe con un **cuadro de marcha**, que tiene siempre las mismas columnas:

| Concepto | Qué es |
|---|---|
| **Saldo** ($S$) | Lo que todavía se debe. Arranca en el capital prestado y baja a medida que se devuelve. |
| **Interés** ($I$) | El alquiler del dinero: $I_t = i \cdot S_{t-1}$, la tasa sobre lo que se debía **al inicio** del período. No baja la deuda. |
| **Amortización** ($A$) | La parte del pago que **sí** baja la deuda. |
| **Cuota** ($C$) | Lo que se paga en el período: $C_t = I_t + A_t$. |

> **Cuidado con la palabra "amortización":** en préstamos es la devolución de capital; en el Problema 2 es el desgaste contable de una máquina. Son conceptos sin relación entre sí.

Lo único que distingue a un sistema de otro es **cómo se reparte la devolución del capital en el tiempo** [T03, p. 21]:

- **Alemán:** la amortización es constante ($A = P/n$). Como el saldo baja parejo, el interés baja mes a mes y la **cuota es decreciente** [T03, p. 22].
- **Bullet** (la cátedra lo llama también *americano*): no se devuelve nada de capital hasta el final. Se pagan **solo intereses** y en el último pago se devuelve el capital entero [T03, p. 22]. Cada pago intermedio se llama **cupón**.
- **Francés** (aparece en el punto b): la **cuota es constante**; lo que crece es la amortización. Es el sistema de un crédito hipotecario típico.

Y el vocabulario de tasas, que es donde está la dificultad real del ejercicio:

| Término | Qué es |
|---|---|
| **Tasa nominal anual** | El número de cartel. Es una convención de etiquetado: no se aplica nunca directamente a nada. |
| **Capitalización** | Cada cuánto el interés devengado se suma al capital y empieza él mismo a generar interés. Es la fuente del efecto compuesto. |
| **Tasa proporcional** | Tasa nominal anual dividida por la cantidad de capitalizaciones por año. **Es la tasa efectiva de su propio período de capitalización** [T03, p. 9]. |
| **Tasa efectiva** (mensual, trimestral, anual) | La tasa real de ese plazo, con el compuesto adentro. Es la única comparable. |

---

## Paso 0 — La línea de tiempo

El paso que más gente saltea y donde más puntos se pierden. Antes de tocar una fórmula hay que contestar: **¿en qué momento estamos parados y qué número de pago es ese momento?**

Los dos préstamos se toman a fin de diciembre de 2025, que es $t = 0$. Convención por defecto salvo que digan lo contrario: **las cuotas son vencidas**, o sea que el primer pago cae al final del primer período, no el día que entregan la plata.

```
Alemán (mensual):
t=0        t=1        t=2              t=12             t=48
dic-25 ─── ene-26 ─── feb-26 ─ ... ─── dic-26 ─ ... ─── dic-29
(entrega)  1.ª cuota  2.ª cuota        12.ª cuota       última

Bullet (semestral, 4 años = 8 pagos):
t=0        s=1        s=2              s=8
dic-25 ─── jun-26 ─── dic-26 ─ ... ─── dic-29
(entrega)  1.er cupón 2.º cupón        8.º cupón + capital
```

→ **Fin de diciembre de 2026 es la cuota 12 del alemán y el 2.º cupón del bullet.**

## Paso 1 — Llevar todas las tasas a tasas efectivas

**Por qué existe este paso.** El enunciado da las dos tasas en formatos que no son comparables: del alemán, una tasa *nominal anual* con capitalización trimestral; del bullet, una tasa *efectiva semestral*. Comparar "12,5 %" contra "6 %" no significa nada.

**1.1 — Tasa efectiva trimestral del alemán.** Se divide por 4 porque la capitalización es trimestral. Como el trimestre *es* el período de capitalización, el resultado ya es efectivo:

$$TET = \frac{12{,}5\,\%}{4} = 3{,}125\,\% \qquad \texttt{B17: =B7/4}$$

**1.2 — Tasa efectiva mensual del alemán.** Acá está la incomodidad deliberada: **el préstamo capitaliza por trimestre pero paga por mes**. La pregunta a responder es *¿qué tasa mensual, aplicada 3 veces, da exactamente 3,125 %?*

$$(1 + TEM)^3 = 1{,}03125 \;\Longrightarrow\; TEM = (1{,}03125)^{1/3} - 1 = 1{,}031\,\% \qquad \texttt{B18: =(1+B17)\^(1/3)-1}$$

**Por qué no se divide por 3.** Dividir ($3{,}125/3 = 1{,}0417\,\%$) supone que el interés del mes 1 no genera interés en los meses 2 y 3: eso es interés simple. Como el interés compone, hace falta una tasa mensual **algo menor** para llegar al mismo 3,125 % trimestral. Verificación: $1{,}01031^3 = 1{,}03125$.

La regla general: **para cambiar el plazo de una tasa efectiva se pasa por el exponente, nunca dividiendo.**

$$1 + i_q = (1 + i_p)^{q/p}$$

**1.3 — Las dos tasas efectivas anuales**, que es lo que permite comparar:

$$TEA_{alemán} = (1{,}03125)^4 - 1 = 13{,}098\,\% \qquad \texttt{B19: =(1+B17)\^4-1}$$
$$TEA_{bullet} = (1{,}06)^2 - 1 = 12{,}36\,\% \qquad \texttt{B21: =(1+B11)\^2-1}$$

La tasa de cartel del alemán decía 12,5 %, pero lo que realmente se paga por año es 13,098 %. Esa diferencia **es** el efecto de capitalizar 4 veces al año, y es la razón por la que la tasa nominal no sirve para comparar ofertas con distinta frecuencia de capitalización [T03, p. 10].

Valores coincidentes con [R03] (hoja P2, celdas B17:B21).

## Paso 2 — Interés que paga cada préstamo en diciembre de 2026

**2.1 — Alemán.** Amortización constante: $A = 1.000.000/48 = 20.833{,}33$.

El interés de la cuota 12 se calcula sobre el saldo que había **antes** de pagarla, o sea tras 11 cuotas:

$$S_{11} = 1.000.000 \times \left(1 - \tfrac{11}{48}\right) = 770.833{,}33 \qquad \texttt{F6: =B6*(1-11/B9)}$$
$$I_{12} = 770.833{,}33 \times 1{,}031\,\% = \mathbf{\$7.947{,}30} \qquad \texttt{F7: =F6*B18}$$

**2.2 — Bullet.** El saldo nunca baja, así que todos los cupones son iguales:

$$I = 500.000 \times 6\,\% = \mathbf{\$30.000} \qquad \texttt{B22: =B10*B11}$$

## Paso 3 — ¿Cuál conviene?

**Respuesta: el bullet**, porque su tasa efectiva anual (12,36 %) es menor que la del alemán (13,098 %) [R03] (celda B29).

Acá está la trampa conceptual del ejercicio. El alemán paga $7.947 de interés en diciembre y el bullet $30.000, y sin embargo **el bullet es el más barato**. Los dos números no se pueden comparar por tres motivos:

1. **Los capitales son distintos** ($1.000.000 contra $500.000).
2. **Los períodos son distintos**: el número del alemán es el interés de *un mes*, el del bullet el de *un semestre*.
3. **El total pagado no mide el costo de un préstamo.** Para el mismo préstamo de $1.000 a 2 años al 10 %, el americano paga $1.200 en total, el alemán $1.150 y el francés $1.152,38, y los tres cuestan exactamente 10 % [T03, p. 28]. El sistema cambia **cuándo** se paga, no **cuánto cuesta**.

> **Lo único que compara costo de financiamiento es la tasa efectiva llevada al mismo período.** Es el precio de un peso por un año: comparable sin importar capital, plazo ni sistema.

**Las dos excepciones a tener presentes:**

- Si el enunciado menciona **gastos de otorgamiento, comisiones o seguros**, el comparador deja de ser la tasa efectiva y pasa a ser el **costo financiero total**, que se calcula como la tasa interna de retorno del flujo real del préstamo [T03, p. 34]. Ejemplo de la cátedra: $1.000 al 10 % con 2 % de gastos y 4 % sobre la cuota da un costo financiero total de 16,73 %.
- Si aparece la palabra **directo**, alerta: ese sistema cobra interés sobre capital ya devuelto, así que es más caro de lo que aparenta ($1.000 a 2 años "al 10 % directo" cuesta en realidad 13,07 % [T03, p. 29]).

### Sobre el supuesto que hay que declarar

La consigna dice *"cuánto pagará de interés a fin de diciembre de 2026"* y eso admite dos lecturas:

| Lectura | Alemán | Bullet |
|---|---|---|
| Interés de la cuota que vence en diciembre (la que toma [R03]) | $7.947,30 | $30.000 |
| Interés acumulado durante todo 2026 | $109.543,80 | $60.000 |

El parcial pide explícitamente escribir el supuesto cuando hay ambigüedad [P02, p. 1]. Se elige una lectura, se escribe una línea diciendo cuál y se resuelve.

**El supuesto es solo de la primera mitad de la pregunta.** La segunda mitad ("cuál conviene") no es ambigua y no depende del supuesto: tomando cualquiera de las dos lecturas, las tasas efectivas anuales son las mismas y gana el bullet. El supuesto no se elige para que dé una respuesta; se declara porque el enunciado no define un dato.

---

## Punto b) — Refinanciación

> **Refinanciar** = tomar lo que se debe en una fecha, cerrar el préstamo viejo y armar con ese monto **un préstamo nuevo** con otra tasa, otro plazo y otro sistema.

No se arrastra nada del pasado: ni la tasa vieja, ni el sistema viejo, ni las cuotas pagadas. Lo único que viaja es **un número: el saldo adeudado**, que pasa a ser el capital inicial del préstamo nuevo. Por eso el inciso tiene dos mitades separadas: cuánto se debe (mira hacia atrás) y cuál es la cuota nueva (mira hacia adelante, desde cero).

### Paso 1 — Saldo adeudado al 31/12/2026

**Alemán**, con $k = 12$ porque ya se pagó la cuota de diciembre:

$$S_{12} = 1.000.000 \times \left(1 - \tfrac{12}{48}\right) = \mathbf{\$750.000} \qquad \texttt{F14: =B6*(1-12/B9)}$$

Sin fórmula: el alemán devuelve el capital en 48 partes iguales y se pagaron 12, o sea un cuarto. Quedan tres cuartos.

**Bullet:** $\mathbf{\$500.000}$, el capital **entero**, intacto. Este es el punto conceptual del inciso: en el bullet **las cuotas no amortizan nada**. Los $30.000 semestrales fueron 100 % interés. Después de un año pagando puntualmente, la empresa debe exactamente lo mismo que el primer día.

> La diferencia entre **pagar** y **amortizar**: pagar es sacar plata del bolsillo, amortizar es bajar la deuda. En el bullet se paga sin amortizar; en el alemán se hacen las dos cosas.

**Total:**

$$S_{total} = 750.000 + 500.000 = \mathbf{\$1.250.000} \qquad \texttt{F16: =F14+F15}$$

Se pueden sumar **porque los dos saldos están medidos en la misma fecha**. Sumar montos del mismo instante es válido; sumar montos de fechas distintas es el error que invalidaba la comparación del punto a).

Control: la empresa debía $1.500.000 y amortizó $250.000 en el año (solo del alemán). Debe $1.250.000.

### Paso 2 — Cuota del sistema francés

**De dónde sale la fórmula.** Un préstamo es un **intercambio equivalente**: el banco da $P$ hoy y recibe $n$ cuotas de $C$. A la tasa pactada, las dos puntas valen lo mismo en valor presente.

$$P = \frac{C}{1+i} + \frac{C}{(1+i)^2} + \dots + \frac{C}{(1+i)^n} = C \cdot a(n,i)$$

donde $a(n,i) = \dfrac{1 - (1+i)^{-n}}{i}$ es el **factor de actualización de una anualidad**: cuánto vale hoy recibir $1 por período durante $n$ períodos.

> **Anualidad** = serie de pagos iguales y equiespaciados. El nombre engaña: no tienen que ser anuales.

Despejando $C$:

$$C = \frac{P}{a(n,i)} = P \cdot \frac{i}{1 - (1+i)^{-n}}$$

**Antes de reemplazar**, el chequeo de siempre: tasa y plazo en la misma unidad de tiempo. Tasa mensual del 0,5 % y 25 cuotas mensuales. Correcto.

$$C = 1.250.000 \times \frac{0{,}005}{1 - (1{,}005)^{-25}} = \mathbf{\$53.314{,}82}$$

```
F17: =F16*B14/(1-(1+B14)^-B13)
```

Es la celda textual de [R03]. Detalle de sintaxis: el signo menos va pegado a la referencia de celda dentro del exponente, sin paréntesis extra.

### Respuestas

| Pregunta | Respuesta |
|---|---|
| Saldo deudor total al 31/12/2026 | **$1.250.000** |
| Nueva cuota (francés, 25 cuotas, 0,5 % mensual) | **$53.314,82** |

### Si piden el cuadro de marcha

Probable ahora que el parcial se resuelve en planilla. Se arma con tres reglas que se arrastran hacia abajo:

$$I_t = i \cdot S_{t-1} \qquad A_t = C - I_t \qquad S_t = S_{t-1} - A_t$$

| Mes | Saldo inicial | Interés | Amortización | Cuota |
|---|---|---|---|---|
| 1 | 1.250.000,00 | 6.250,00 | 47.064,82 | 53.314,82 |
| 2 | 1.202.935,18 | 6.014,68 | 47.300,14 | 53.314,82 |
| 3 | 1.155.635,04 | 5.778,18 | 47.536,64 | 53.314,82 |
| … | | | | |
| 25 | 53.049,82 | 265,00 | 53.049,82 | 53.314,82 |

La cuota no se mueve, el interés baja y la amortización sube a razón de $(1+i)$ por mes. **Control de calidad: el saldo después de la última cuota tiene que dar exactamente 0.** Si no da, hay un error en la tasa o en el plazo.

### Pregunta de sensibilidad probable

No la piden, pero sale en una celda: ¿conviene refinanciar?

$$TEA_{refi} = (1{,}005)^{12} - 1 = 6{,}17\,\%$$

Contra 13,098 % y 12,36 % de los préstamos viejos: le están ofreciendo plata a menos de la mitad de precio, así que **conviene claramente**. Notar que la decisión se toma otra vez comparando tasas efectivas anualizadas, no cuotas ni totales pagados.

---

## Qué queda en la hoja de fórmulas

```
Equivalencia de tasas    1 + i_q = (1 + i_p)^(q/p)
Tasa efectiva anual      TEA = (1 + TNA/m)^m − 1
Saldo alemán tras k      S_k = P · (1 − k/n)
Saldo bullet             S = P   (nunca amortiza)
Cuota francesa           C = P · i / (1 − (1+i)^−n)
Cuadro de marcha         I_t = i·S_{t−1} ;  A_t = C − I_t ;  S_t = S_{t−1} − A_t
```

## Relación con otros temas

- [Valor tiempo del dinero](../../wiki/temas/valor-tiempo-del-dinero.md)
- [Hoja de fórmulas](../../wiki/hoja-de-formulas.md)
- [Segundo parcial](../../wiki/temas/segundo-parcial.md)
- [2026-C1: respuestas y auditoría de la resolución oficial](2026-C1.md)

## Fuentes

P02, R03, T03 (oficiales).
