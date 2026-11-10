# Evaluación de proyectos

## Qué es un proyecto de inversión

Un proyecto de inversión es "cualquier sacrificio de recursos hoy, con la esperanza de recibir algún beneficio en el futuro": se pospone consumo (sacrificio), se compara hoy con futuro (tiempo), se asume riesgo (esperanza) y se busca recupero más retorno (beneficio) [T04, p. 2]. El estudio completo abarca viabilidad comercial, técnica, legal, operativa, económica, financiera y ambiental/social [T04, p. 3]; la evaluación financiera sirve para evitar malos proyectos, no rechazar los buenos y medir riesgos [T04, p. 4].

Los dos insumos básicos son el **flujo de caja libre** del proyecto (comportamiento más probable de ingresos y egresos en el tiempo) y los **criterios de decisión** [T04, p. 5].

### Tipos de alternativas

- **Dependientes**: se aceptan ambas o ninguna (ERP + servidores) [T04, p. 22].
- **Independientes**: si hay fondos, se aprueban todas las rentables [T04, p. 22].
- **Mutuamente excluyentes**: aceptar A implica rechazar B (máquina alemana o china) [T04, p. 22].

Antes de evaluar, la prioridad es detectar las alternativas disponibles [T04, p. 21].

## Flujo de caja versus beneficio contable

El beneficio contable incluye devengamientos y depreciaciones y depende de criterios contables ("una opinión"); el flujo de caja es dinero que entra y sale ("un hecho") [T04, p. 15]. En el flujo de fondos se pone siempre lo percibido/pagado (cash); el cuadro de resultados se arma con lo devengado porque sobre él se calcula el impuesto [G05, p. 4]. Ver [información contable](informacion-contable.md).

### Flujo incremental, costos hundidos y costo de oportunidad

- En una empresa existente, el flujo se arma sobre base **incremental**: diferencia entre los flujos con y sin proyecto [T04, p. 16].
- Prueba práctica de la cátedra: un costo o ingreso entra al flujo solo si está presente con el proyecto y ausente sin él; si está en ambos casos, no entra [G05, p. 3].

| Partida | ¿Entra? | Motivo |
|---|---|---|
| Estudio ya pagado | No | Costo hundido |
| Terreno propio ocioso | Sí | Costo de oportunidad (alquiler o venta) |
| Capital de trabajo | Sí | Inversión que se recupera al final |
| Intereses del préstamo | No | El costo del financiamiento está en la tasa |
| Ventas quitadas a otro producto | Sí | Canibalización |
| Amortización contable | Solo su efecto fiscal | No es egreso, pero reduce el impuesto |
| Impuesto a las ganancias | Sí | El flujo es después de impuestos |

Tabla verificada visualmente en [T04, p. 20].

- **Costos prorrateados** (estructura asignada por costeo): no entran, porque si el proyecto no se hace el costo no desaparece, solo se reasigna [G05, p. 3]. Ejemplos en la guía: fijos prorrateados de $5.000/año [G01, p. 7] y el técnico prorrateado de $10.000/año [G01, p. 9]. Ver [costos](costos.md).
- **Costos hundidos**: el estudio de reingeniería de $40.000 no modifica el flujo ni el VAN, cualquiera sea su monto [G04, p. 2].
- **Enfoque marginal**: si un ingreso ocurre igual con o sin proyecto (la suba de precio de las botellas), no se incluye; sí se incluye el ahorro de costos que genera el proyecto [G05, p. 3].

## Componentes del flujo de fondos

La guía práctica nombra los bloques del flujo como **FEO** (flujo económico operativo) y **FEE** (flujo de la inversión al final: valor de rezago de bienes de uso y recupero de capital de trabajo) [G01, p. 6] [G04, p. 1].

### Flujo económico operativo (FEO)

La cátedra lo expresa como $FFO = (V - C - G)(1 - t) + A \cdot t$, donde $A \cdot t$ es el **escudo impositivo** de las amortizaciones [G05, p. 2]. La guía pide calcular el FEO "con los tres enfoques" [G01, p. 7]; **Inferencia:** los tres enfoques equivalentes son:

1. Desde el resultado: $FEO = UN + A = (V - C - A)(1 - t) + A$.
2. Directo: $FEO = V - C - IG$, con $IG = t\,(V - C - A)$.
3. Escudo fiscal: $FEO = (V - C)(1 - t) + A \cdot t$ [G05, p. 2].

Ejemplo: ingresos netos de egresos $550/año, amortización $60/año, $t = 30\%$: $FEO = 550 \cdot 0{,}7 + 60 \cdot 0{,}3 = 403$ [G01, p. 6] [G04, p. 1].

### Inversiones en bienes de uso y capital de trabajo

- Bienes de uso (BU): egreso en el momento en que se paga; si el pago se difiere, el egreso se ubica en el período del pago (paneles pagados 40% en $t=0$ y 60% en $t=1$) [P01] [R02] (hoja Ej2).
- Gastos no amortizables en $t = 0$ (capacitación) se deducen y generan ahorro de impuesto: $-4.000 \cdot (1 - 0{,}4) = -2.400$ [G01, p. 6]; con $t = 20\%$, $-2.000 \cdot 0{,}8 = -1.600$ [G04, p. 1].
- Capital de trabajo (Kt/WK): es una inversión que se recupera al final [T04, p. 20]. Refleja el desfasaje entre ventas y cobranzas, compensado por el desfasaje entre costos y pagos; alternativamente se pueden poner cobranzas en lugar de ventas [G05, p. 4]. Cuando varía con las ventas, se invierte la **variación** del Kt de cada año (créditos menos deudas con proveedores) [R03] (hoja P3).

### Valor residual (rezago) y su efecto impositivo

Al vender un BU, el impuesto se paga (o se ahorra) sobre la diferencia entre valor de mercado y valor de libros:

$$FEE_{BU} = VR_m - t\,(VR_m - VL)$$

donde $VL$ es el valor de libros al momento de la venta. La resolución oficial del parcial usa exactamente esta fórmula [R03] (hoja P3). **Inferencia:** también puede escribirse $VR_m(1-t) + t \cdot VL$ o $VL + (VR_m - VL)(1-t)$ (los otros dos enfoques que pide la guía).

- Venta con ganancia: valor de mercado $15.000$, $VL = 0$, $t = 40\%$: $15.000 \cdot 0{,}6 = 9.000$ [G01, p. 6].
- Venta con pérdida: valor de mercado $800$, $VL = 1.000 - 3 \cdot 60 = 820$; la pérdida de 20 ahorra $6$ de impuesto, $FEE_{BU} = 806$ [G01, p. 6] [G04, p. 1].
- Venta de la máquina vieja en un reemplazo: entra en $t = 0$ neta de impuesto ($10.000$ con $VL = 0$ e $IG = 40\%$ aportan $6.000$) [G01, p. 6].

### Recupero de capital de trabajo

Si se recupera menos que lo invertido, la diferencia es una pérdida deducible: invertir 100 y recuperar 80% con $t = 30\%$ da $FEE_{KT} = 80 + 20 \cdot 0{,}3 = 86$ [G04, p. 1]; con 200, 80% y 35%: $160 + 40 \cdot 0{,}35 = 174$ [G04, p. 1]. **Inferencia:** el tratamiento fiscal de la pérdida surge de reproducir los resultados oficiales; el enunciado no lo explicita.

### Amortizaciones como escudo fiscal

La amortización no es egreso de caja, pero reduce el impuesto [T04, p. 20]. Amortizar más rápido no cambia la suma de impuestos, pero adelanta el ahorro; por valor tiempo del dinero, baja el valor presente de los impuestos y **aumenta el VAN** [G04, p. 2]. A la inversa, amortizar en más años da menor escudo en los primeros años y menor VAN [R02] (hoja Ej2). Para comparar dos esquemas de amortización ceteris paribus basta con descontar la diferencia de $A \cdot t$ año a año [G05, p. 2] [G05, p. 3].

### Impuesto a las ganancias

Se calcula sobre el resultado del cuadro (devengado), después de amortizaciones [G05, p. 4]. Si el resultado de un año es negativo, la resolución oficial computa un impuesto negativo (ahorro fiscal para la empresa) [R03] (hoja P3). **Inferencia:** esto supone que la empresa tiene otras ganancias contra las cuales compensar.

## Procedimiento para armar el flujo de fondos

1. Identificar qué es incremental: descartar costos hundidos, prorrateados e ingresos que ocurren igual sin proyecto; sumar costos de oportunidad y canibalización [T04, p. 20] [G05, p. 3].
2. Armar el **cuadro de resultados** de cada año (devengado) para calcular el impuesto [G05, p. 4].
3. Pasar del resultado al **FEO** sumando la amortización [T04, p. 19].
4. Agregar inversiones en BU y capital de trabajo (con signo negativo) en el período en que se pagan [T04, p. 19] [R03] (hoja P3).
5. Agregar el **FEE** en el último año: valor residual neto de impuesto y recupero de Kt [G04, p. 1].
6. Sumar por año para obtener el flujo de fondos neto (FFN), descontarlo a la TREMA y aplicar los criterios [R03] (hoja P3).

### Cuadro de resultados → flujo de caja libre (T04)

| Concepto | $ millones |
|---|---|
| Ventas | 1.000 |
| − Costos operativos | −600 |
| − Amortización (no es caja) | −100 |
| = Resultado operativo (EBIT) | 300 |
| − Impuesto a las ganancias (35%) | −105 |
| = Utilidad operativa neta (NOPAT) | 195 |
| + Amortización | 100 |
| − Aumento de capital de trabajo | −30 |
| − Inversión en bienes de capital | −50 |
| = Flujo de caja libre | 215 |

Verificado visualmente en [T04, p. 19]. Los intereses no se restan: el costo del financiamiento ya está en la tasa de descuento y restarlo lo contaría dos veces [T04, p. 19].

### Ejemplo completo (guía, ejercicio 1)

Datos: BU $1.000$, vida fiscal 10 años, rezago contable $400$ ($A = 60$/año), vida técnica y comercial 3 años, valor de mercado al final $800$, Kt $100$ con recupero 80%, ingresos netos $550$/año, $t = 30\%$, TREMA 10% [G01, p. 6].

Cuadro de resultados (años 1 a 3):

| Concepto | $ |
|---|---|
| Ingresos netos de egresos | 550 |
| − Amortización | −60 |
| = Resultado antes de impuestos | 490 |
| − IG (30%) | −147 |
| = Utilidad neta | 343 |
| + Amortización | 60 |
| = FEO | 403 |

Flujo de fondos:

| Año | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Inversión BU | −1.000 | | | |
| Inversión Kt | −100 | | | |
| FEO | | 403 | 403 | 403 |
| FEE (BU) | | | | 806 |
| FEE (Kt) | | | | 86 |
| FFN | −1.100 | 403 | 403 | 1.295 |

$VAN(10\%) = 572{,}37 > 0$: se acepta [G04, p. 1]. Recalculado: 572,37.

## Tasa de descuento (TREMA)

- La tasa de descuento establece la equivalencia del decisor: lo hace indiferente entre $1 hoy y $(1+i)$ dentro de un período [T04, p. 6].
- **TREMA** (tasa de retorno esperada mínima aceptable): ganancia mínima que el inversor exige para financiar el proyecto, considerando inflación y riesgo; depende de origen de los fondos, costo de la deuda, exigencia de los accionistas, riesgo y horizonte [T04, p. 8]. Es el costo de oportunidad de los fondos [T04, p. 43].
- **WACC** (costo promedio ponderado del capital): tasa apropiada para el VAN; pondera el costo de cada fuente por su proporción [T04, p. 10]. La deuda se toma **después de impuestos** [T04, p. 11] [T04, p. 12]. Ejemplo: deuda $10.000$ al 6% neto y acciones $20.000$ al 9%: $WACC = \tfrac{1}{3} \cdot 6\% + \tfrac{2}{3} \cdot 9\% = 8\%$ [T04, p. 12].
- Costo del capital propio con CAPM más riesgo país: $K_e = 5{,}28 + 1{,}10 \cdot 4{,}23 + 5{,}86 = 15{,}79\%$; $K_d$ neto $= 9\% \cdot 0{,}65 = 5{,}85\%$; con 60/40, $WACC = 11{,}82\%$ [T04, p. 14].
- **Coherencia tasa-flujo**: $(1 + i_{nom}) = (1 + i_{real})(1 + \pi)$. Flujos reales con tasa real y nominales con tasa nominal dan el mismo VAN (7,0); flujos nominales descontados a tasa real sobreestiman el VAN (65,8) porque cuentan dos veces la inflación [T04, p. 9]. Ver [valor tiempo del dinero](valor-tiempo-del-dinero.md).

## Criterios de decisión

T04 enumera: VAN, TIR, TER/TIRM, período de recupero, valor anual/CAE, máxima exposición e índice de rentabilidad [T04, p. 23], además de la tasa contable de retorno [T04, p. 73].

### Valor actual neto (VAN)

$$VAN = \sum_{j=0}^{n} \frac{FC_j}{(1+i)^j}$$

Verificado visualmente en [T04, p. 25]. Mide en pesos de hoy el excedente por encima del costo de financiar el proyecto (explícito o de oportunidad) [T04, p. 24].

- Regla: $VAN > 0$ recupera la inversión, rinde la TREMA y genera excedente; $VAN = 0$ rinde exactamente la TREMA; $VAN < 0$ no alcanza la TREMA [T04, p. 34].
- Ejemplo: $-22.000$; $10.000$; $20.000$ al 12%: $VAN \approx 2.870$ [T04, p. 26]. Interpretado como préstamo al proyecto, sobra un remanente de $3.603$ en el año 2, cuyo valor presente es $2.872$ [T04, p. 30].
- Supone reinversión de los flujos intermedios a la tasa de descuento [T04, p. 37].
- El VAN depende del inversor (de su tasa) [T04, p. 48] y aumenta el valor de mercado de la firma, que capturan principalmente los accionistas [T04, p. 32].

### Tasa interna de retorno (TIR)

Es la tasa que anula el VAN: $\sum FC_j/(1+TIR)^j = 0$ [T04, p. 38]. Para el ejemplo anterior, $TIR = 20{,}74\%$ [T04, p. 40].

- Regla: $TIR > TREMA$, aceptar; $TIR < TREMA$, rechazar [T04, p. 43].
- Supone reinversión a la propia TIR [T04, p. 46]; es propia de la inversión, no del inversor [T04, p. 48].
- Problemas: TIR múltiples si el flujo cambia de signo más de una vez [T04, p. 50]; en una **desinversión** (ingreso primero, egresos después) la regla se invierte: conviene si $TIR < TREMA$ [T04, p. 52] [T04, p. 55]; ignora la escala en excluyentes [T04, p. 56].
- **Análisis incremental**: A ($-100$; $130$) tiene TIR 30% y VAN 18,18; B ($-1.000$; $1.250$) tiene TIR 25% y VAN 136,36. La TIR del incremental B − A es 24,4% > 10%, así que se elige B, como con el VAN [T04, p. 56].

### TIRM y TER

- **TIRM**: egresos llevados a $t=0$ con la tasa de financiamiento, ingresos capitalizados al final con la TREMA; $TIRM = (VF_{ingresos}/VP_{egresos})^{1/n} - 1$. Da un valor único y es menor que la TIR si $TIR > TREMA$ [T04, p. 58].
- **TER** del proyecto LOMAS ($-100$; $10$; $60$; $80$; TREMA 10%): ingresos capitalizados a $158{,}1$ en el año 3, $TER = 16{,}5\%$ frente a $TIR \approx 18\%$ [T04, p. 60].

### Índice de rentabilidad (IR)

$IR = VP_{flujos\ futuros}/I = 1 + VAN/I$; se acepta si $IR > 1$. Con racionamiento de capital se ordena por IR hasta agotar el presupuesto (P1 y P2 usan 100 y suman VAN 30); con proyectos indivisibles o excluyentes hay que comparar combinaciones [T04, p. 57].

### Período de recupero simple (PRS) y descontado (PRD)

Tiempo que tarda el proyecto en devolver la inversión; mide riesgo y liquidez [T04, p. 61]. Se interpola linealmente dentro del año en que el acumulado cambia de signo:

$$PR = k + \frac{|\text{acumulado al fin del año } k|}{\text{flujo del año } k+1}$$

- PRS de $-100$; $40$; $50$; $30$: $2 + 10/30 = 2$ años y 4 meses [T04, p. 61].
- PRD del mismo flujo al 10%: 2 años, 11 meses y 26 días [T04, p. 66].
- Flujo $-100$; $10$; …; $60$: PRS = 4 y PRD = 4,8 [T04, p. 67].
- Limitaciones: ignora los flujos posteriores al recupero y, el simple, el valor tiempo del dinero [T04, p. 61] [T04, p. 65]. Elegir por menor PR puede llevar a la peor alternativa (C recupera en 1 año pero no genera nada más) [T04, p. 63] [T04, p. 64].

### Máxima exposición

Valor más negativo del flujo acumulado: máximo endeudamiento que provoca el proyecto ($270$ en el ejemplo) [T04, p. 68].

### Valor anual equivalente (VAE) y costo anual equivalente (CAE)

$$VAE = \frac{VAN}{a(n, i)}, \qquad a(n,i) = \frac{1 - (1+i)^{-n}}{i}$$

Se acepta si $VAE \geq 0$; en proyectos de costos el VA es el **CAE** [T04, p. 70] [T04, p. 71]. Ejemplo: $2.872/1{,}690 = 1.699{,}6$ [T04, p. 71].

Para comparar alternativas de **vidas distintas**, no se comparan VAN sino VAE/CAE [G05, p. 5]:

| | Equipo A | Equipo B |
|---|---|---|
| Inversión | 100.000 | 150.000 |
| Costo operativo anual | 20.000 | 12.000 |
| Vida (años) | 3 | 5 |
| VP de costos al 12% | 148.037 | 193.257 |
| CAE | 61.635 | 53.611 |

B tiene mayor VP de costos pero menor costo por año: conviene B [T04, p. 72] (verificado visualmente y recalculado). El método supone que el proyecto se repite [T04, p. 77]; la misma lógica (hipótesis de repetibilidad) se usa para hallar la vida económica y el período óptimo de reemplazo [G05, p. 4] [G05, p. 5].

### Tasa contable de retorno (TCR)

$TCR = \text{utilidad promedio anual}/\text{inversión promedio}$: $12.000/40.000 = 30\%$ [T04, p. 73] [T04, p. 74]. No considera el valor tiempo del dinero [T04, p. 75]; para el mismo equipo, con flujo de caja de $28.000$/año, $TIR = 22{,}1\%$ y $VAN(12\%) = 20.934$ [T04, p. 76].

### Síntesis

| Criterio | Regla | Limitación |
|---|---|---|
| VAN | > 0 | Depende de la tasa; no da % |
| TIR | > costo del capital | Múltiples TIR, escala, reinversión |
| TIRM/TER | vs. TREMA | Requiere tasa de reinversión |
| IR | > 1 | Excluyentes e indivisibles |
| Recupero | Menor es mejor | Ignora valor tiempo y flujos posteriores |
| VAE/CAE | Mayor VAE / menor CAE | Supone repetición |
| TCR | Mayor es mejor | Base contable, sin valor tiempo |

Resumido de [T04, p. 77].

## Financiamiento y flujo del accionista

En el material oficial, el flujo del proyecto **no** incluye intereses: el costo de la deuda (después de impuestos) entra a través de la tasa (WACC) [T04, p. 19] [T04, p. 20]. Una forma de verlo: si el proyecto se financia al 10%, el flujo de financiar sumado al del proyecto deja un excedente cuyo valor presente es el VAN [T04, p. 33]. La decisión de contado versus financiado se resuelve descontando el flujo de cada financiación al costo del capital propio y comparando con el precio de contado [G05, p. 2].

**Conocimiento general (no está en el material):** el "flujo del accionista" (o del inversor) agrega al flujo del proyecto el préstamo recibido, las cuotas pagadas y el ahorro fiscal de los intereses, y se descuenta al costo del capital propio $K_e$. T04 C2 2026 y la guía no desarrollan este enfoque.

## Análisis de sensibilidad y punto de indiferencia

- **Perfil del VAN**: el VAN cae al subir la tasa y corta el eje en la TIR [T04, p. 36] [T04, p. 45].
- **Sensibilidad a una variable**: en el pozo de Vaca Muerta, VAN(15%) de 0,0, 7,8 y 15,7 US$ M para precios de 45, 60 y 75 US$/bbl [T04, p. 35]; +100 pb de riesgo país suben la WACC 0,6 pp [T04, p. 14].
- **Punto de indiferencia (equilibrio)**: valor de la variable que hace $VAN = 0$. En el pozo, el precio de equilibrio es US$ 45: a ese precio la TIR es 15% y el proyecto es "indiferente" frente a la tasa exigida [T04, p. 35] [T04, p. 45]. En el parcial 2025 se pide el tipo de cambio máximo que hace conveniente esperar, alquilar en el ínterin y comprar en el exterior frente a comprar hoy en el país [P01]; la resolución lo obtiene dividiendo la diferencia de valores presentes entre ambas alternativas por el precio en dólares [R02] (hoja Ej1).
- **Inferencia:** el procedimiento general es expresar el VAN en función de la variable incierta, igualarlo a cero (o igualar los VAN/CAE de dos alternativas) y despejar.

## Guía de ejercicios

Guía práctica, Parte 2, de [G01, p. 6] a [G01, p. 9]; resultados oficiales en [G04, p. 1] [G04, p. 2]. La numeración de G04 (1 a 7) coincide con la del cuerpo de G01 (2.1 a 2.7); el índice de G01 lista solo 2.1 a 2.6 [G01, p. 2].

1. **Fabricación de un producto** (BU 1.000, Kt 100, 3 años, IG 30%): FEO, FEE y VAN al 10%. Resultado: FEO = 403; FEE(BU) = 806; FEE(KT) = 86; VAN(10%) = 572,37, se acepta [G04, p. 1].
2. **Gatoturro, reemplazo de máquina** (enfoque fiscal, IG 40%): VAN al 10%. Resultado: FFN = −49.400; 11.800 (años 1-4); 23.800 (año 5); VAN(10%) = 2.782, se acepta; además PRS = 4,1 y PRD = 4,8 [G04, p. 1]. Recalculado: VAN = 2.782,34; PRS = 4,09; PRD = 4,81.
3. **Dos esquemas de amortización** de $100.000 (lineal vs. 40/30/20/10), TREMA 15%, IG 40%: diferencia de VAN. G04 informa ΔVAN = $1.994 [G04, p. 1], pero la cátedra publicó la errata: el valor correcto es **$1.984** [G05, p. 2]. Recalculado: 1.984,13.
4. **Nuevo producto 10 años con máquina de 5 años** (se recompra en el año 5; fijos prorrateados excluidos): VAN al 15%. Resultado: FFN = −280.000; 265.500 (años 1-4); 75.500 (año 5); 265.500 (años 6-9); 344.300 (año 10); VAN(15%) = $977.000, se acepta [G04, p. 1]. Recalculado: 977.498.
5. **Automatización** (estudio previo de $5.000 hundido, ahorro 22.000/año, IG 34%): ¿hacerlo? Resultado: FEO = 19.960; FEE = 13.200; VAN(10%) = 3.860, se acepta [G04, p. 1].
6. **Máquina con vida fiscal 10 años usada 5** (estudio de $105 hundido, IG 35%): FEO, FEE(BU), FEE(Kt) con tres enfoques y VAN al 20%. Resultado: FEO = 425; inversión BU 1.000 y FEE(BU) = 240; inversión Kt 200 y FEE(KT) = 174; VAN(20%) = 237,41, se acepta [G04, p. 1]. Recalculado: 237,39.
7. **Tapitas propias** (enfoque marginal, reingeniería hundida, técnico prorrateado excluido, IG 20%): FEO/FEE, VAN y dos preguntas conceptuales. Resultado: FEO(t=0) = −1.600; FEO(1-5) = 394.400; FEE(BU) = 52.000; FEE(KT) = 12.000; VAN(10%) = 1.313.225; (c) el estudio es costo hundido y no cambia el VAN; (d) amortizar en 6 años aumenta el VAN [G04, p. 1] [G04, p. 2].

La guía continúa con **análisis de reemplazo** (vida económica y período óptimo de reemplazo, ejercicios 2.8 y 2.9) [G01, p. 10], sin resultados en G04; la cátedra indica resolverlos con CAE [G05, p. 4] [G05, p. 5]. G01 no contiene una parte de contabilidad: el encabezado "Contabilidad" de la p. 2 precede al índice de VTD, proyectos y reemplazo [G01, p. 2].

### Borrador no oficial del ejercicio 4

X10 (no oficial) calcula un VAN de 649,175 para el ejercicio 4 [X10]. **Inferencia:** las unidades son miles de pesos (649,175 miles = $649.175), coherentes con G04; la diferencia es de **flujo**: X10 toma solo seis valores (−280; 265,5 × 4; 344,3) como años 0 a 5, omitiendo el año 5 con recompra (75,5) y los años 6 a 9, y adelantando el flujo final del año 10 al año 5. Con el horizonte completo de 10 años se obtiene el resultado oficial (977.498).

## Errores frecuentes

- Restar intereses en el flujo del proyecto cuando la tasa ya es una WACC [T04, p. 19].
- Incluir costos hundidos (estudios ya pagados) o costos prorrateados [T04, p. 20] [G05, p. 3].
- Tomar la amortización como egreso de caja en lugar de usar solo su efecto fiscal [T04, p. 20].
- Olvidar el impuesto sobre la diferencia entre valor de mercado y valor de libros en la venta de BU [R03] (hoja P3).
- Olvidar la reinversión cuando la vida del equipo es menor que la del proyecto (ejercicio 4) [G04, p. 1].
- Mezclar flujos nominales con tasas reales [T04, p. 9].
- Elegir entre excluyentes por TIR sin análisis incremental [T04, p. 56], o comparar VAN de proyectos con vidas distintas en lugar de VAE/CAE [G05, p. 5].
- Aplicar la regla "TIR > TREMA" a un flujo de desinversión [T04, p. 55].

## Relación con otros temas

- [Valor tiempo del dinero](valor-tiempo-del-dinero.md): factores de actualización, anualidades y tasas equivalentes que usa el VAN y el CAE.
- [Información contable](informacion-contable.md): cuadro de resultados, amortizaciones y devengado.
- [Costos](costos.md): costos fijos, variables, prorrateados y relevantes.
- [Análisis financiero](analisis-financiero.md): costo de la deuda, apalancamiento y rentabilidad del accionista.
- [Segundo parcial](segundo-parcial.md): problemas de proyectos de parciales anteriores.

## Fuentes

- T04: diapositivas "Evaluación de proyectos", C2 2026.
- G01: guía práctica (rev. mayo 2012), Parte 2 y análisis de reemplazo.
- G04: resultados numéricos de la guía de proyectos.
- G05: respuestas a preguntas frecuentes (errata del ejercicio 3, prorrateados, enfoque marginal, capital de trabajo, reemplazo).
- P01, R02, R03: segundos parciales 2025-2026 y sus resoluciones oficiales (ejemplos de flujo y de punto de indiferencia).
- X10: borrador no oficial de VAN/CAE.
