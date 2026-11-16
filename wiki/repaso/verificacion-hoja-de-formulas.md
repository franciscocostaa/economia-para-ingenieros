# Verificación de la hoja de fórmulas del segundo parcial

Revisión de cobertura de la [hoja de fórmulas](hoja-de-formulas.md). Se revisaron las consignas prácticas catalogadas, sus variantes de tema y las preguntas de repaso relacionadas. La verificación numérica se concentró en los problemas de proyectos y en las variantes de valor tiempo de la guía. Los resultados de los parciales antiguos se contrastaron con sus resoluciones no oficiales. Los borradores [X09–X11] corresponden a consignas ya incluidas. Una columna de X10 carece de enunciado identificado. [Catálogo de fuentes](../../material/catalogo.tsv)

## Evaluación de proyectos

La estructura P3 alcanza para **armar el flujo** de los diez casos de examen (ocho parciales, con dos temas en los dos oficiales). Para completar todas las consignas de la guía hacen falta los tres enfoques de FEO/FEE y el procedimiento por edades de reemplazo. Los siguientes pasos sirven como complemento directo de la segunda carilla.

### Cómo cargar casos que se salen de MAXIMILIEN

1. **Fecha final.** Dibujá columnas hasta el último cobro o pago. Si el último crédito se cobra después del cierre operativo, en ese año poné ventas y FEO en cero. Llevá el CT a cero para liberar el saldo por la fila 39 o mantené el saldo y recuperalo en la 40. Usá un solo método. Si hay una venta de activos en otra fecha, va en la 41 de esa fecha. [G05, p. 4] [X02] [R03]
2. **Compará escenarios antes de cargar 29–32.** Para varios mercados, calculá cantidad × precio por mercado y sumá. Si te dan una restricción comercial, calculá primero la mezcla factible. Restá el margen que se pierde y sumá los ahorros como costos negativos. Un estudio comprometido se excluye aunque se pague más adelante. Una comisión condicionada al proyecto se incluye en el año correspondiente. [T04, p. 20] [G05, p. 3] [X02] [X04] [X05]
3. **Activos y reemplazos.** Anotá cada activo por separado con costo capitalizado, fecha en servicio, años de amortización, rezago contable y fecha de venta. Sumá sus amortizaciones en 32. El precio de compra va en 38 en las fechas de pago. Venta y reposición pueden coincidir en una columna, en 41 y 38 respectivamente. Si te dan valores de libros año a año, la amortización es el VL inicial menos el VL final de cada año, para un activo sin altas ni bajas en ese intervalo. [G01, pp. 6–10] [R02] [R03]
4. **CT e impuesto.** Si el CT inicial es fijo, cargalo en 49 en el año 0, mantené el saldo hasta el cierre y recuperalo en 40. Si te dan plazos, proyectá saldos pendientes. Identificá si la pérdida fiscal puede usarse y en qué fecha. Con un recupero parcial, aplicá el ahorro sobre el faltante si suponés deducibilidad y aprovechamiento. Los resultados de la guía usan ese supuesto. [G04, p. 1] [G05, p. 4] [R03]
5. **Si piden tres enfoques.** Estos son reordenamientos algebraicos de las fórmulas de la cátedra, suponiendo que los efectos fiscales se aprovechan en el período. Con M = ventas menos costos operativos erogables, A = amortización, τ = tasa y R = recupero, usá la misma cifra en la fila final por cualquiera de las tres vías. [G01, pp. 7–9] [G04, p. 1] [G05, p. 2] [T04, pp. 19–20] [R03]

| Concepto | Desde el resultado contable | Desde caja e impuesto | Desde el escudo fiscal |
|---|---|---|---|
| FEO, fila 37 | (M − A)(1 − τ) + A | M − τ(M − A) | M(1 − τ) + Aτ |
| FEE del activo, fila 41 | VL + (VM − VL)(1 − τ) | VM − τ(VM − VL) | VM(1 − τ) + τVL |
| FEE del CT, fila 40 | CT + (R − CT)(1 − τ) | R − τ(R − CT) | R(1 − τ) + τCT |

6. **Si piden vida económica.** Hacé una copia de P3 para cada edad candidata n. Poné la inversión en 0, los costos operativos y las amortizaciones hasta n, y la venta neta al final de n. Calculá CAE = −VAN/a(n,i), con flujos de costo negativos, y elegí el menor CAE entre ciclos repetibles. [G01, p. 10] [G05, pp. 4–5]
7. **Si piden sensibilidad.** Modificá el dato original y recalculá todas las filas dependientes. Un precio puede cambiar ventas, impuesto y CT. La amortización cambia el impuesto y el valor de libros. Para un alquiler anual adicional constante con deducción inmediata y sin otros efectos, el aumento límite es VAN inicial / [(1 − τ)·a(n,i)]. Si cambia el tratamiento fiscal, buscá el valor que hace VAN = 0 en el cuadro completo. Distinguí aumento y nuevo nivel. [T04, p. 35] [G05, p. 2] [X07] [R02]

### Cobertura por parcial

| Parcial | Problema de valor tiempo del dinero | Problema de proyectos con P3 |
|---|---|---|
| [2C2010](../../practica/segundo-parcial/2010-C2.md) [X02] | Capitalizá por separado los depósitos mensuales y anuales hasta el ingreso. Capitalizá el saldo durante la carrera y armá el francés. El saldo para cancelar es el VP de las cuotas restantes a la fecha de cancelación. | **NIKITA.** Cargá dos mercados, comisión sobre ventas y alquiler sacrificado. Excluí el estudio ya comprometido. Reventa de la máquina en 41 del año 5, último cobro en año 6. VAN recalculado **39.904,64**. |
| [1C2018](../../practica/segundo-parcial/2018-C1.md) [X03] | Sumá en cada mes la cuota y su refuerzo. VP financiado menos precio contado da el descuento en dinero. Para el francés, amortizado = capital inicial − saldo tras cuota 2. | **Máquina dedicada.** CT en 0 y recupero del 70 %. Amortización en años 1–3, operación hasta 5. VAN **15.042,09**, si la pérdida de CT es deducible. |
| [2C2018](../../practica/segundo-parcial/2018-C2.md) [X04] | Francés mensual, precancelación y alemán anual. Penalidad = porcentaje × capital precancelado. Aplicá Fisher a tasas anuales comparables. | **Super Gas.** Como exportar paga más, usá 70 % local y 30 % exportación si se vende toda la producción. Restá el gas natural que se deja de vender y capitalizá la instalación. VAN **1.033.625,76** con deducción de la pérdida de CT. |
| [1C2023](../../practica/segundo-parcial/2023-C1.md) [X05] | Bullet, francés con tasa implícita y perpetuidad. Hallá la TIR del francés con sus cuotas efectivas, luego la tasa real. El bullet en dólares requiere un supuesto cambiario para compararlo en pesos. | **Dale Gas.** Repite la estructura de Super Gas. Mismo VAN con los mismos supuestos. |
| [2C2024](../../practica/segundo-parcial/2024-C2.md) [X06] | Cuotas adelantadas, vencidas con refuerzos y alemán. Calculá la cuota con la tasa de la financiación y compará los planes a la tasa de oportunidad. | **San Cachano.** Restá las entradas de la tribuna vieja que se pierden. Venta de gradas debajo del VL en año 6. VAN **3.293,78**. |
| [1C2025](../../practica/segundo-parcial/2025-C1.md) [X07] | Alemán → francés → cancelación. Para el VP total, registrá el desembolso recibido, cuotas y cancelación en sus fechas. | **LAUNI.** CT inicial y recupero del 90 %. Igualá el VAN a cero para hallar el aumento de alquiler. VAN base **3.923,29** con deducción de la pérdida de CT. Aumento límite del alquiler **1.671,97** por año. |
| [2C2025, ambos temas](../../practica/segundo-parcial/2025-C2.md) [P01] [R02] | Compará comprar y alquilar con VP por cantidad de partidos. Igualá VP para el tipo de cambio máximo y desplazá el año 0 si se cancela el viaje. | **SolArGen.** Inversión en 0 y 1, operación hasta 15, sin CT. Probá dos calendarios de amortización. Con amortización a 10 años, VAN **−97,87** (Tema 1) y **+1,88** (Tema 2), en millones de pesos. A 15 años baja a **−181,63** y **−78,66**, respectivamente. |
| [1C2026, ambos temas](../../practica/segundo-parcial/2026-C1.md) [P02, pp. 1–2] [R03] | Alemán mensual y bullet semestral. Aclarar si se pide el interés de diciembre o el acumulado del año. Sumá saldos después de los pagos para refinanciar. | **MAXIMILIEN.** La P3 se aplica directo. El Tema 2 supone que se aprovecha la pérdida fiscal del año 1. VAN **535,07** (Tema 1) y **497,56** (Tema 2). |

Los VAN de la tabla son recálculos. [R02] resuelve SolArGen con el Tema 2 y [R03] resuelve MAXIMILIEN con el Tema 2. [X02–X07] son resoluciones de alumnos.

### Guía G01, proyectos y reemplazo

| Ejercicio | Aplicación de la segunda carilla y paso adicional |
|---|---|
| 2.1 | CT inicial y recupero parcial, venta debajo de VL. Separá FEO (37) y FEE (40 + 41). VAN 572,37. [G01, p. 6] [G04, p. 1] |
| 2.2 | Gatoturro. Compra y venta de la máquina anterior en 0. Capacitación deducible en 37 en 0, ahorros como costo negativo y CT inicial. VAN 2.782,34. [G01, p. 6] [G04, p. 1] |
| 2.3 | Dos calendarios. Cargá las amortizaciones dadas en 32. Al mantener todo lo demás igual, descontá solo la diferencia de escudos τ·ΔA. ΔVAN 1.984,13 con la corrección de la cátedra. [G01, pp. 6–7] [G05, p. 2] |
| 2.4 | La segunda máquina entra en 38 del año 5 y la venta de la primera en 41. Reiniciá el calendario de amortización. El CT sigue hasta el año 10. VAN aproximado 977.498. [G01, p. 7] [G04, p. 1] |
| 2.5 | Automatización. Operación por ahorro de costos, sin ventas adicionales. Mostrá las tres expresiones de FEO. VAN 3.860,27. [G01, p. 7] [G04, p. 1] |
| 2.6 | Operación de 5 años, amortización de 10, venta debajo de VL y CT parcial. Mostrá los tres enfoques de FEO y FEE. VAN recalculado 237,39. [G01, pp. 7–8] [G04, p. 1] |
| 2.7 | Tapitas. Capacitá en 0 como gasto, cargá el ahorro solo por lo que cambia, y calculá FEO y FEE con los tres enfoques. El costo del estudio ya comprometido cancela entre escenarios. Para amortización a 6 años, recalculá el escudo y VL. VAN 1.313.225 siguiendo el escenario oficial, que omite ventas de excedentes. Si se supone producción adicional, hay que modelar su margen y declarar el supuesto. [G01, pp. 8–9] [G04, pp. 1–2] [G05, p. 3] |
| 2.8 | Vida económica. Un cuadro por edad 1–5, VL y reventa dados. **Inferencia:** menor CAE a los 4 años, $16.043,22/año, aprovechando el efecto fiscal de costos y amortización. [G01, p. 10] [G05, pp. 4–5] |
| 2.9 | Reemplazo óptimo. Calculá mantenimiento, VM(n) y VL(n) para cada ciclo. **Inferencia:** menor CAE a 1 año, $42.500/año, bajo repetibilidad y aprovechamiento fiscal. [G01, p. 10] [G05, pp. 4–5] |

### Consignas adicionales de las diapositivas

- **T04, p. 78, ejercicio 1.** Cargá los flujos dados directamente en 42 y calculá VAN, TIR y recupero. VAN 91,40, TIR 21,65 % y recupero simple 2,17 años con interpolación.
- **T04, p. 78, ejercicio 2.** Usá Fisher de la primera carilla. Para pasar cada flujo real a nominal multiplicá por (1 + inflación)^t. Al descontar a tasa nominal del 40,4 % o a tasa real del 8 %, el VAN es 7,00 en ambos casos.
- **T04, p. 78, ejercicio 3.** Usá el precio de equilibrio de la p. 35. Si cae de 45 a 40 y se mantienen cantidad y demás supuestos del modelo, cae el VAN y queda por debajo de cero. Para un VAN numérico hace falta reconstruir el perfil anual y el tratamiento de costos del modelo. [T04, pp. 35, 78]

## Valor tiempo del dinero · guía G01

| Ejercicio | Qué hacés con la primera carilla |
|---|---|
| 1.1 | Convertí cada TNA en TEM y TEA, y calculá ambas cuotas con P/a. [G01, p. 3] [G03, p. 1] |
| 1.2 | Valuá cada renta al año 10 y dividí por s(10,i). [G01, p. 3] [G03, p. 1] |
| 1.3 | Compará cobro por venta hoy con VP de 3 o 4 alquileres más venta en el año 4. [G01, p. 3] [G03, p. 1] |
| 1.4 | Cuota, capital amortizado, saldo y refinanciación salen del cuadro. Para el inciso e, con saldo S, cuota C y nueva tasa i, usá n = −ln(1−i·S/C)/ln(1+i), si C > i·S, o Excel NPER(i;−C;S). Da 46,64 períodos teóricos. Si se exige un plan discreto, quedan 46 cuotas completas y un último pago menor. [G01, p. 3] [G03, p. 1] |
| 1.5 | Cuota base desconocida con refuerzos proporcionales. Si en cada período se paga mₖ veces la cuota C, entonces C = VP / Σ[mₖ/(1+i)^k]. En los trimestres 4 y 8 el multiplicador es 3. [G01, p. 4] [G03, p. 1] |
| 1.6 | Calculá el saldo tras cuota 12, cancelá la mitad y recalculá la cuota sobre la otra mitad. Interés total = suma de intereses de ambos cuadros o total pagado − principal original, sin comisiones. Ahorro = interés original − interés nuevo. [G01, p. 4] [G03, p. 1] |
| 1.7 | Construí el flujo semestral con el capital neto de comisión. Aplicá TIR y anualizá. [G01, p. 4] [G03, p. 1] [G05, p. 1] |
| 1.8 | Tasa equivalente por días, luego Fisher a la misma base. [G03] y [X13] toman m = 365/180 dentro de (1+TNA/m)^m−1 y publican 4,004 % real anual y 0,323 % a 30 días. La otra lectura, (1+TNA/2)^(365/180)−1, da 4,102 % y 0,331 %. [G01, p. 4] [G03, p. 1] [X13] |
| 1.9 | Un cuadro por deuda y una línea de tiempo conjunta. Aporte propio en 0 = contado − créditos. Interés simple del proveedor por tres meses, desembolso de devolución en mes 4. Descontá todo al costo de oportunidad. [G01, p. 4] [G03, p. 1] |
| 1.10 | Sumá el VP de los pagos base, el de los refuerzos y el del pago final. [G01, p. 5] [G05, p. 2] |

Si la consigna pide **tasa adelantada**, d = i/(1+i). Si pide volver de efectiva periódica a **TNA** para m capitalizaciones, TNA = m·i. Si pide un flujo **indexado**, calculá la cuota real y multiplicá cada pago por el índice de precios acumulado a su fecha. [T03, pp. 8–12, 32]

## GP5 y verdadero/falso

La GP5 exige un balance y un cuadro de resultados por devengado, y usa fórmulas de índices que no están en las dos carillas. Los V/F también piden justificar sobre costos, caja, liquidez y apalancamiento. La [wiki contable](../temas/informacion-contable.md), la [tabla de índices](../temas/analisis-financiero.md) y el [banco de V/F por parcial](../../practica/segundo-parcial/banco-vf.md) cubren esos procedimientos. [G02] [R01] [T01] [T02] [T05]

| GP5 | Procedimiento |
|---|---|
| 1 | Registrá cada movimiento, separá caja de devengado y calculá el costo de ventas por FIFO. Cerrá el balance comprobando Activo = Pasivo + PN y armá el estado de resultados. |
| 2 | Por cada activo, calculá VL y resultado por venta = precio − VL. Separá el precio entre caja (60 %) y crédito (40 %). |
| 3 | Compará deducción inmediata y amortización fiscal. Diferencia anual de IG = tasa × diferencia de resultados imponibles. |
| 4 | Armá el calendario de interés devengado del prestamista y prestatario. El principal modifica deuda y caja. |
| 5 | Despejá AC, inventario y caja desde los tres índices de liquidez. Despejá ventas y CMV con los días de crédito e inventario. Reconstruí EBIT, intereses, resultado antes de IG e impuesto. |
| 6 | Intereses = deuda × tasa. Resultado neto = ventas × margen neto. EBIT = resultado neto/(1 − τ) + intereses. Compará EBIT/intereses con el mínimo bancario. |
| 7 | Fondo de maniobra = AC − PC. Necesidad adicional = Δcréditos + Δinventarios − Δproveedores. La deuda comercial proyectada requiere suponer qué parte de las compras sigue pendiente al cierre. |
