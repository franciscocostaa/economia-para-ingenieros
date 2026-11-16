# Valor tiempo del dinero (cálculo financiero)

Las citas a T03 usan el número de página del PDF; a partir de la diapositiva 14 el número impreso en la diapositiva es uno menor.

## Idea central

Un peso hoy no vale lo mismo que un peso mañana: antes de comparar flujos de distintos momentos hay que llevarlos a un mismo momento (en general, a valor presente) con la tasa adecuada [T03, p. 39]. Toda tasa relevante en finanzas se expresa y se compara en términos compuestos [T03, p. 3].

## Interés simple y compuesto

- **Simple**: el interés se calcula siempre sobre el capital inicial: $M = C\,(1 + i\,n)$ [T03, p. 2].
- **Compuesto**: el interés de cada período se suma al capital y empieza a generar interés: $M = C\,(1 + i)^n$ [T03, p. 2].
- Ejemplo: $1.000 al 10% anual durante 2 años da $1.200 con interés simple y $1.210 con compuesto [T03, p. 2]; a los 10 años la diferencia ya es de $593 [T03, p. 3].
- En la guía el interés simple aparece en créditos puntuales: un crédito de proveedor de $30.000 que devenga 3,5% simple mensual durante 3 meses [G01, p. 4] se cancela con $30.000 × (1 + 0,035 × 3) = $33.150 (cálculo de un borrador no oficial [X09]).

## Tasas

### Qué compone una tasa

Tasa libre de riesgo más una prima por riesgo; a mayor riesgo, mayor tasa exigida; además incorpora la inflación esperada [T03, p. 5]. Tasas altas enfrían la economía: pocos proyectos superan el rendimiento financiero y se reduce la oferta de crédito [T03, p. 5].

### Formas de presentar una tasa

T03 ordena las preguntas que hay que hacerse ante cualquier tasa: sobre saldos o directa, vencida o adelantada, proporcional/nominal/efectiva, equivalente y real [T03, p. 6].

- **Sobre saldos**: se aplica sobre lo que efectivamente se debe en cada momento; es el criterio por defecto [T03, p. 7].
- **Directa**: se aplica siempre sobre el capital original; es una forma "marketinera" que parece más barata de lo que es [T03, p. 7] (ver Sistema directo más abajo).

### Vencida y adelantada (tasa de descuento)

- **Vencida** ($i$): se aplica sobre el saldo al inicio del período; es el criterio por defecto [T03, p. 8].
- **Adelantada** ($d$), o tasa de descuento: se aplica sobre el saldo al cierre del período [T03, p. 8].
- Relación: $(1 + i)(1 - d) = 1$ [T03, p. 8].
- Ejemplo: de $100 hoy a $110 en t = 1, la tasa vencida es 110/100 − 1 = 10% y la adelantada 1 − 100/110 = 9,09%; sobre el mismo flujo la adelantada siempre es menor [T03, p. 8].

### Nominal, proporcional y efectiva

- **TNA**: tasa nominal anual, el número que se publica [T03, p. 9].
- **Tasa proporcional** (TP): $TP = TNA / m$, con $m$ = capitalizaciones por año. Toda TP es efectiva para su propio período (TNA/12 es la efectiva mensual si la capitalización es mensual) [T03, p. 9].
- **Tasa efectiva anual**: $TEA = (1 + TP)^m - 1$; supera a la TNA apenas hay más de una capitalización por año [T03, p. 9].
- Ejemplo: A ofrece TNA 60% con capitalización mensual (TP 5%, TEA 79,6%) y B ofrece TNA 65% con capitalización semestral (TP 32,5%, TEA 75,6%): B tiene mayor TNA pero menor TEA [T03, p. 10]. La TNA sola nunca alcanza para comparar ofertas con distinta frecuencia de capitalización [T03, p. 10].

### Tasas equivalentes

- Dos tasas son equivalentes si, aplicadas al mismo capital durante el mismo plazo, producen el mismo monto; lo que se conserva es la TEA, no el número nominal [T03, p. 11].
- Fórmula general con capitalizaciones cada $k$ y cada $p$ días: $\left(1 + TNA_k \tfrac{k}{365}\right)^{365/k} = \left(1 + TNA_p \tfrac{p}{365}\right)^{365/p}$ [T03, p. 11].
- Ejemplo: TNA 24% con capitalización mensual equivale a una TNA con capitalización trimestral de $((1{,}02)^3 - 1) \times 4 = 24{,}48\%$ [T03, p. 11].
- Regla práctica para cambiar de plazo una tasa efectiva: $1 + i_{q} = (1 + i_{p})^{q/p}$. Así se resuelven G01 ej. 1 (TEM equivalente a una trimestral) y ej. 8a (de 30 a 80 días: $1{,}02^{80/30} - 1 = 5{,}42\%$) [G01, p. 3] [G01, p. 4] [G03, p. 1]. La resolución oficial del parcial 16/06/2026 usa la misma regla: TNA 12,5% con capitalización trimestral → TET 3,125% → $TEM = 1{,}03125^{1/3} - 1 = 1{,}031\%$ [R03].

### Tasa real e inflación (Fisher)

- La tasa real mide el resultado en poder adquisitivo [T03, p. 12].
- Exacta: $(1 + i_r) = (1 + i_n)/(1 + f)$; aproximación para tasas bajas: $i_r \approx i_n - f$ [T03, p. 12]. Con $i_n$ = 5% y $f$ = 4%: aproximada 1%, exacta 0,96% [T03, p. 12].
- Relación de Fisher, escrita al revés: $(1 + i_{nom}) = (1 + i_{real})(1 + \text{infl.})$; con 10% real y 8% de inflación, $i_{nom}$ = 18,8% [T03, p. 33].
- Préstamo indexado: $1.000 a 2 años, 10% real, 8% de inflación, sistema americano. En moneda constante el flujo es −1.000 / +100 / +1.100 (VAN al 10% real = 0); en moneda corriente es −1.000 / +108 / +1.283,04 (VAN al 18,8% nominal = 0) [T03, p. 32]. Regla: flujos en moneda constante se descuentan con tasa real; flujos en moneda corriente, con tasa nominal [T03, p. 32].
- Los créditos UVA funcionan así: la tasa se aplica sobre el capital ajustado por inflación [T03, p. 33] [T03, p. 37].

## Valor presente y valor futuro

- **Capitalización** (llevar al futuro): $F = P(1 + i)^n$. **Actualización** (traer al presente): $P = F/(1 + i)^n$; el cálculo se llama descuento [T03, p. 15] [T03, p. 14].
- **Varios flujos**: $P = \sum_t F_t/(1 + i)^t$ [T03, p. 16]. Ejemplo: edificio con flujos −170.000, −100.000 y +320.000 a 5% anual → VP −170.000, −95.238 y +290.249; VAN = $25.011 [T03, p. 16].
- **Despejar tasa o plazo**: $i = (F/P)^{1/n} - 1$ y $n = \ln(F/P)/\ln(1 + i)$; en planilla, funciones RATE/TASA y NPER (modelo de libro de texto, no oficial) [X01].

### Anualidades (rentas constantes)

**Conocimiento general (no está en el material):** el valor presente de $n$ cuotas iguales $C$ vencidas (la primera en t = 1) es $VP = C \cdot a(n, i)$, con el factor de actualización $a(n, i) = \dfrac{1 - (1 + i)^{-n}}{i}$; el valor futuro en t = n es $VF = C \cdot s(n, i)$, con $s(n, i) = \dfrac{(1 + i)^n - 1}{i}$.

- La notación $a(n, i)$ aparece en el material: la resolución oficial del parcial calcula la cuota francesa como $C = P \cdot i / (1 - (1 + i)^{-n})$ [R03], y los borradores de alumnos escriben "cuota = P / a(n,i)" [X09] y "VAE = VAN / a(vida, trema)" [X09] (no oficiales).
- **Anualidad adelantada** (cuotas al inicio de cada período): vale $(1 + i)$ veces la vencida. Ejemplo no oficial: $100 por 3 años al 5% → VP 272,33 si es vencida y 285,94 si es adelantada; VF 315,25 y 331,01 [X01].
- Con capitalización no anual, $n$, $i$ y la cuota deben expresarse en el mismo período (por ejemplo, semestres y tasa semestral) [X01] (no oficial).

### Perpetuidades y perpetuidad creciente

- **Perpetuidad constante**: $VP = F/i$ [G05, p. 1]. Ejemplo no oficial: $100 por año al 5% vale $2.000; al 10%, $1.000 [X01].
- **Perpetuidad creciente** a tasa $g$ (cada flujo es $(1 + g)$ veces el anterior): $VP = F/(i - g)$, donde $F$ es el **primer** flujo [G05, p. 1]. Requiere $i > g$ (**Inferencia:** si no, la serie no converge).
- **Desde qué período se obtiene el VP**: la fórmula da el valor **un período antes del primer flujo**. Si el primer flujo está en t = 11, la fórmula da el VP en t = 10; si estuviera en t = 35, lo da en t = 34 y para llevarlo a t = 0 hay que dividir por $(1 + i)^{34}$ [G05, p. 1]. **Inferencia:** lo mismo vale para $a(n, i)$, que también da el valor un período antes de la primera cuota.
- G05 remite a la sección 3.6 de un "apunte de Economía Empresaria" que no está en el repositorio [G05, p. 1].

## Sistemas de amortización de préstamos

Al definir un préstamo hay que fijar cuándo y cuánto se devuelve de capital, si se indexa, si la tasa es fija o variable y cuándo se paga el interés [T03, p. 21]. Hay infinitas alternativas; las más usadas son americano, alemán, francés, directo e indexado [T03, p. 22].

Notación del cuadro de marcha: $S_{t}$ saldo al final del período $t$, $I_t = i \cdot S_{t-1}$ interés, $A_t$ amortización de capital, cuota $C_t = I_t + A_t$, $S_t = S_{t-1} - A_t$. **Inferencia:** es la estructura que usan la resolución oficial y los borradores [R03] [X09].

| Sistema | Amortización de capital | Interés | Cuota |
|---|---|---|---|
| Americano (bullet) | todo en el último pago | sobre el saldo, que no baja | solo interés; la última incluye el capital [T03, p. 22] |
| Alemán | constante: $A = P/n$ | baja porque el saldo baja [T03, p. 22] | decreciente |
| Francés | creciente | decreciente | constante [T03, p. 22] |
| Directo | constante | siempre sobre el capital original [T03, p. 22] | constante |
| Indexado | capital y/o cuotas ajustados por un índice [T03, p. 22] | | |

### Caso base de T03: $1.000, 2 años, 10% anual (flujos del acreedor)

| Sistema | Cuota año 1 | Cuota año 2 | Total pagado | Tasa efectiva |
|---|---|---|---|---|
| Americano | 100,00 | 1.100,00 | 1.200,00 | 10,00% |
| Alemán | 600,00 | 550,00 | 1.150,00 | 10,00% |
| Francés | 576,19 | 576,19 | 1.152,38 | 10,00% |
| Directo | 600,00 | 600,00 | 1.200,00 | 13,07% |

Fuente: [T03, p. 29]; detalle de cada sistema en [T03, p. 24], [T03, p. 25], [T03, p. 26] y [T03, p. 27]. En el francés, la amortización es 476,19 y 523,81 y el interés 100,00 y 52,38 [T03, p. 26].

Conclusión de la cátedra: el sistema cambia **cuándo** se paga, no siempre **cuánto** cuesta. Total pagado distinto no significa costo distinto; lo que compara es la tasa efectiva. Americano, alemán y francés rinden exactamente 10%; el directo no, porque cobra interés sobre capital ya devuelto: la TIR de −1.000 / +600 / +600 es 13,07% [T03, p. 28] [T03, p. 29].

### Fórmulas por sistema

- **Americano/bullet**: $C_t = i \cdot P$ para $t < n$ y $C_n = i \cdot P + P$ (borrador no oficial [X11]). Ejemplo oficial: bullet de $500.000 al 6% semestral paga $30.000 de interés por semestre [R03].
- **Alemán**: $A = P/n$; saldo tras $k$ cuotas $S_k = P(1 - k/n)$; $I_t = i \cdot S_{t-1}$. Ejemplo oficial: $1.000.000 en 48 cuotas mensuales a TEM 1,031% → $A$ = 20.833,33; saldo tras 11 cuotas 770.833; interés de la cuota 12 = 7.947,30; saldo tras 12 cuotas 750.000 [R03].
- **Francés**: $C = P \cdot \dfrac{i}{1 - (1 + i)^{-n}}$ [R03]. **Conocimiento general (no está en el material):** el saldo tras $k$ cuotas es el VP de las cuotas que faltan, $S_k = C \cdot a(n - k, i)$; la amortización crece a razón $(1 + i)$: $A_{t+1} = A_t(1 + i)$, con $A_1 = C - i P$.
- Ejemplo no oficial de cuadro francés: $1.000 al 6% en 3 cuotas → cuota 374,11; interés 60,00 / 41,15 / 21,18; amortización 314,11 / 332,96 / 352,93 [X01].

### Comparar préstamos

Para elegir entre dos préstamos se comparan tasas efectivas en el mismo período, no totales pagados. En el parcial 16/06/2026 la cátedra compara un alemán (TNA 12,5% con capitalización trimestral → TEA 13,10%) con un bullet (6% semestral → TEA 12,36%) y elige el bullet por menor TEA [P02, p. 1] [R03].

### Refinanciación y pagos extraordinarios

- **Refinanciar** = tomar el saldo adeudado en una fecha como nuevo capital y armar un préstamo nuevo con otra tasa, plazo o sistema (**Inferencia** a partir de los ejercicios). Ejemplo oficial: a fin de diciembre de 2026 se suman el saldo del alemán (750.000) y el capital del bullet (500.000) = $1.250.000 y se refinancian en francés a 25 cuotas al 0,5% mensual → cuota $53.314,80 [P02, p. 1] [R03].
- Variante "misma cuota, nueva tasa": si sube la tasa y la cuota no cambia, se despeja el nuevo plazo $n = -\ln(1 - S \cdot i / C)/\ln(1 + i)$ (**Conocimiento general (no está en el material)**); da un $n$ no entero (G01 ej. 4e: entre 46 y 47 períodos [G03, p. 1]).
- **Pago extraordinario**: reduce el saldo; si se mantiene el plazo, se recalcula la cuota sobre el saldo remanente y se ahorran intereses (G01 ej. 6 [G01, p. 4] [G03, p. 1]).

## Costo financiero total (CFT)

- Tasa "all in cost": resume todo lo que cuesta un préstamo, no solo el interés: gastos, seguros, comisiones e impuestos [T03, p. 34].
- Cálculo: (1) explicitar el flujo de fondos del préstamo, (2) incluir todos los conceptos, (3) calcular la TIR del flujo resultante [T03, p. 34].
- Ejemplo: $1.000 a un período al 10%, con 2% de gastos de otorgamiento (cobrados al inicio) y gastos administrativos del 4% de la cuota: $CFT = 1{,}10 \times 1{,}04 / 0{,}98 - 1 = 16{,}73\%$ [T03, p. 34].
- **CFT vs TEA** (G01 ej. 7): la TEA solo considera intereses; la tasa semestral pactada resuelve $100 = 10/(1+i) + 60/(1+i)^2 + 5/(1+i)^3 + 55/(1+i)^4$ (da 10%), mientras que el CFT semestral resuelve la misma ecuación con **98** a la izquierda, porque por la comisión de $2 se recibió menos dinero. Por eso el CFT supera a la TEA; luego se anualiza: $(1 + CFT_{sem})^2 - 1$ [G05, p. 1] [G05, p. 2].
- Ejemplo de tarjeta: saldo $5.000 refinanciado en francés con TNA 30% y TEA 34,50%; con $109,59 de gastos de otorgamiento y 0,40% de seguro de vida, el CFT va de 75,72% (3 cuotas) a 58,02% (12 cuotas) y sube a 61,91% en 24 cuotas porque ahí la TNA es 34% [T03, p. 35]. Los gastos fijos pesan más cuanto menor es la cuota [T03, p. 35].
- El BCRA recomienda comparar siempre el CFT y no solo la TNA publicitada [T03, p. 38].

## Contado o financiado

La empresa debe financiarse con deuda solo si es más barata que su costo de oportunidad del capital. Numéricamente: armar el flujo de cada financiación, descontarlo con el costo de oportunidad del capital propio y comparar el VP total con el precio de contado [G05, p. 2]. En G01 ej. 9 el equipo cuesta $703.661 financiado contra $710.000 de contado, así que conviene financiar [G03, p. 1].

## Procedimiento típico

1. Dibujar la línea de tiempo con signo y momento de cada flujo; fijar la unidad de período (mes, trimestre, semestre, año).
2. Convertir la tasa dada a una tasa **efectiva del mismo período** que los flujos (TNA → TP → equivalente).
3. Si hay inflación, trabajar todo en moneda constante con tasa real o todo en moneda corriente con tasa nominal [T03, p. 32].
4. Elegir la herramienta: VP/VF de un flujo, anualidad, perpetuidad (VP un período antes del primer flujo [G05, p. 1]), cuadro de marcha del préstamo o TIR (para CFT o tasa implícita).
5. Llevar todo a la misma fecha antes de sumar o comparar.
6. Para decidir, comparar VP o tasas efectivas, nunca totales nominales [T03, p. 29].

## Errores frecuentes

- Comparar TNA con distinta capitalización en lugar de TEA [T03, p. 10].
- Usar la TP de un período con flujos de otro período sin convertirla.
- Olvidar que la fórmula de perpetuidad (o de anualidad) da el valor un período antes del primer flujo y no descontar el tramo restante a t = 0 [G05, p. 1].
- En la perpetuidad creciente, poner en el numerador un flujo que no es el primero.
- Tomar la TEA como costo del préstamo cuando hay comisiones o gastos: el costo es el CFT [G05, p. 2].
- Juzgar un sistema de amortización por el total pagado [T03, p. 29].
- Mezclar flujos nominales con tasa real o al revés [T03, p. 32].
- Contar mal el período de descuento de un pago (ver CONFLICTOS: un borrador descuenta el crédito de proveedor de G01 ej. 9 un mes de menos [X09]).

## Guía de ejercicios

Consignas en [G01, p. 3] (ej. 1 a 4), [G01, p. 4] (ej. 5 a 9) y [G01, p. 5] (ej. 10). La numeración de G03 coincide con la de G01 Parte 1 para los ejercicios 1 a 9: se verificó recalculando cada resultado. G03 no trae el ej. 10; su resultado figura en G05.

| Ej. | Qué pide | Herramienta | Resultado oficial |
|---|---|---|---|
| 1 | Comparar dos préstamos (TNA 14% cap. mensual vs. 18% cap. trimestral): costo efectivo mensual y anual, y cuota de $5.000 en 24 meses | TP, tasa equivalente, TEA; cuota francesa | A: TEM 1,17%, TEA 14,93%, cuota $240,10; B: TEM 1,48%, TEA 19,25%, cuota $249,00 [G03, p. 1] |
| 2 | Ahorro anual durante 10 años (10%) para financiar: a) perpetuidad de $100.000 desde el año 11; b) perpetuidad creciente al 2%; c) renta de 20 años desde el año 11 | Perpetuidad, perpetuidad creciente y anualidad valuadas en t = 10; luego cuota con $s(10, 10\%)$ | a) $62.700; b) $78.400; c) $53.400 [G03, p. 1] (redondeados a centenas) |
| 3 | Galpón: vender hoy en $100.000 o alquilar y vender al final del año 4 (9%) | VP de flujos | 3 años de alquiler: VP $94.640, conviene vender; 4 años: VP $105.270, conviene alquilar [G03, p. 1] |
| 4 | Préstamo francés de $3.000.000, 60 cuotas al 2%: cuota, amortizado al período 2, saldo tras 20 cuotas, refinanciación a 2,5% en 40 cuotas, plazo con cuota fija y tasa 2,5% | Cuadro francés, saldo como VP de cuotas restantes, refinanciación, despeje de $n$ | Solo e): 46 < n < 47 [G03, p. 1]. **Inferencia** (cálculo propio, reproducido por [X13]): a) $86.303,90; b) $53.133,87; c) $2.360.884; d) $94.048,74; e) n ≈ 46,64 |
| 5 | Máquina de $200 en 8 cuotas trimestrales más 2 refuerzos (cada uno = 2 cuotas) con la 4.ª y la 8.ª; TNA 12% cap. trimestral | VP de anualidad más VP de refuerzos; TP trimestral 3% | En el 4.º trimestre se pagan $57,90 [G03, p. 1] |
| 6 | Préstamo de 30 cuotas de $10.000 al 6%; con la cuota 12 se cancela la mitad del saldo y se sigue con cuota nueva | Saldo francés, recálculo de cuota, intereses totales | Intereses pagados $126.489; ahorro $35.862 [G03, p. 1] |
| 7 | $100 con comisión de $2, dos amortizaciones anuales de $50 e interés nominal 20% pagadero semestralmente: costo anual | CFT como TIR del flujo neto recibido | CFT 10,83% semestral = 22,80% anual [G03, p. 1]; explicación en [G05, p. 1] |
| 8 | a) Tasa de 80 días equivalente a 2% a 30 días; b) tasa real anual y de 30 días con 7% anual cap. cada 180 días e inflación 3% (año de 365) | Tasas equivalentes por días; Fisher | a) 5,42%; b) real anual 4,004%, real 30 días 0,323% [G03, p. 1] |
| 9 | Equipo de $710.000 financiado con alemán, francés, crédito de proveedor a interés simple y saldo propio; costo de oportunidad 3,25% mensual | Cuadros alemán y francés, interés simple, VP con costo de oportunidad | Costó $703.661 financiado; conviene financiar [G03, p. 1] |
| 10 | Deuda al 6% anual cap. mensual: 17 pagos de $50, refuerzos de $80 en los meses 3 a 15 cada 3 meses y pago final de $95,25 en el mes 18 | VP de anualidad más flujos puntuales; tasa mensual 0,5% | $1.282,53 [G05, p. 2] (falta en G03). [X13] llega al mismo total |

## Resolución no oficial de la guía 6

[X13] es la planilla de Andy (`Finanzas_Guia_2_Res.xlsx`), con una hoja por ejercicio. Donde [G03] redondea, esta planilla deja el valor sin redondear: cuotas del ejercicio 1 de $240,06 y $248,99; ahorros del ejercicio 2 de $62.745, $78.432 y $53.419; pago del 4.º trimestre del ejercicio 5 de $57,83. Esas diferencias ya estaban anotadas contra [G03, p. 1].

En el ejercicio 8 reproduce el 4,004 % real anual y el 0,323 % a 30 días de [G03, p. 1]. Lo hace con $m = 365/180$ dentro de $(1 + \mathrm{TNA}/m)^m - 1$, y después Fisher. La otra lectura, $(1 + \mathrm{TNA}/2)^{365/180} - 1$, da 4,102 % y 0,331 %.

En el ejercicio 9 descuenta el crédito de proveedor en el mes 4 y obtiene $703.661, el resultado oficial [G03, p. 1]. El borrador [X09] descuenta un mes de menos.

En el ejercicio 7 escribe la ecuación del CFT que da la cátedra, $98 = 10/(1+i) + 60/(1+i)^2 + 5/(1+i)^3 + 55/(1+i)^4$ [G05, p. 2], pero no la resuelve: carga una tasa semestral del 11 % y anualiza a 23,21 %. El resultado oficial es 10,83 % semestral y 22,80 % anual [G03, p. 1]. Para ese ejercicio hay que usar [G03], no [X13].

## Relación con otros temas

- [Evaluación de proyectos](evaluacion-de-proyectos.md): VAN, TIR y VAE son aplicaciones directas del VP, la anualidad y la TIR de este tema.
- [Análisis financiero](analisis-financiero.md): costo de la deuda, apalancamiento y comparación con la rentabilidad del activo.
- [Información contable](informacion-contable.md): intereses como resultado financiero y saldos de deuda en el balance.
- [Costos](costos.md): costo de oportunidad del capital como tasa de descuento.
- [Segundo parcial](segundo-parcial.md): los parciales recientes incluyen préstamos alemán/bullet, comparación por TEA y refinanciación francesa [P02, p. 1].

## Fuentes

- T03: diapositivas oficiales de VTD, C2 2026 (fórmulas y ejemplos verificados sobre el PDF).
- G01: guía práctica, Parte 1 (ejercicios 1 a 10).
- G03: resultados numéricos oficiales de la guía VTD.
- G05: respuestas de la cátedra a preguntas frecuentes (perpetuidades, CFT, contado vs. financiado, resultado del ej. 10).
- P02 y R03: segundo parcial 16/06/2026 y su resolución oficial (alemán, bullet, refinanciación).
- X01 (no oficial): modelo Excel de libro de texto (anualidades, perpetuidad, cuadro francés).
- X09 (no oficial): borrador de G01 ej. 9.
- X11 (no oficial): borrador de préstamos alemán y bullet del parcial 16/06/2026.
- X13 (no oficial): guía 6 resuelta por Andy.
