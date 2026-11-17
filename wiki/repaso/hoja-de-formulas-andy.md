# Hoja de fórmulas de Andy · Segundo parcial

Organizada por **tipo de problema de examen**. Primero los tipos del Problema 1 (valor tiempo del dinero) y del Problema 2 (evaluación de proyectos), cada uno con los parciales en los que salió (`practica/segundo-parcial/*.md`: 2C2010, 1C2018, 2C2018, 1C2023, 2C2024, 1C2025, 2C2025 y 1C2026). Después, un anexo con **todas las fórmulas que Andy usó** en sus resoluciones: guías 5, 6 y 7 [X12] [X13] [X14] y parciales 1C2025, 2C2025, 2C2024 y 1C2026 (`practica/segundo-parcial/*-Solucion-Andy.xlsx`). Todo es material no oficial, contrastado con la cátedra [T03] [T04] [G05] [R02] [R03].

En la columna Excel se usan **nombres** (i, n, P, TREMA…) en lugar de celdas: reemplazalos por la celda de tu bloque de Datos. Para resolver alcanzan las cuentas (+ − * / ^) y cuatro funciones: `SUM`, `NPV` (VNA), `IRR` (TIR) y, solo para despejar n, `LN`.

Para imprimir: `python3 scripts/hoja_formulas_pdf.py --andy` → `output/pdf/hoja-de-formulas-andy.pdf`.

## Problema 1 · Valor tiempo del dinero

### 0 · Antes de calcular

- **Línea de tiempo** · t = 0 es hoy (compra, préstamo o decisión). Cuotas **vencidas** (fin de mes) salvo que diga "adelantadas" o "en el acto" (t = 0). Marcá en qué mes cae cada fecha que te piden.
- **Tasa de comparación** · la de quien decide: lo que rinde su plata (costo de oportunidad) o lo que le cuesta conseguirla. Las tasas de cada préstamo solo sirven para armar sus cuotas.
- **i y n en el mismo período** · cuotas mensuales → TEM; anuales → TEA; semestrales → tasa semestral.

### 1 · Tasas (cambiar de plazo = exponente, nunca dividir)

| Dato → busco | Fórmula | Excel |
|---|---|---|
| TNA con m capitalizaciones → tasa del período | i = TNA/m (m: 12 mensual, 4 trimestral, 2 semestral) | `=TNA/m` |
| TNA → TEA | (1 + TNA/m)^m − 1 | `=(1+TNA/m)^m-1` |
| TEA → TEM | (1 + TEA)^(1/12) − 1 | `=(1+TEA)^(1/12)-1` |
| TEM → TEA | (1 + TEM)^12 − 1 | `=(1+TEM)^12-1` |
| Tasa trimestral → TEM (1C2026) | (1 + i_trim)^(1/3) − 1 | `=(1+itrim)^(1/3)-1` |
| TNA con capitalización diaria → TEM (2C2025) | (1 + TNA/360)^30 − 1 | `=(1+TNA/360)^30-1` |
| Efectiva de p días → q días | (1 + i_p)^(q/p) − 1 | `=(1+ip)^(q/p)-1` |

⚠ TNA 28 % mensual → TEM = 0,28/12 sí (es la tasa del período). TEA 42 % → TEM = 1,42^(1/12) − 1, NO 0,42/12.

### Tipo A · Elegir entre formas de pago o préstamos

Salió en 2C2024 (contado vs. 3 financiaciones), 1C2023 (bullet vs. francés vs. perpetuidad), 1C2026 a) (alemán vs. bullet) y 1C2018 a) (descuento por pagar contado). Guía 6, ej. 9.

Receta: **una tabla por opción** y gana la de **menor VP Total**. Ejemplo, opción A del 2C2024 (i = TEM de oportunidad 2,9653 %):

| Fila | Mes 0 | Mes 1 | Mes 2 | Excel |
|---|---|---|---|---|
| Pago | 9.000.000 | 9.000.000 | 9.000.000 | dato o cuota del sistema |
| Factor | 1 | 0,9712 | 0,9432 | `=1/(1+i)^Mes` |
| VP | 9.000.000 | 8.740.813 | 8.489.090 | `=Pago*Factor` |
| **VP Total** | **26.229.902** | | | `=SUM(VP)` |

- **Con NPV** · VP = `=NPV(i,pagos 1…n)+pago 0` (NPV toma el primer valor como t = 1).
- **Cuotas desiguales con incógnita X (2C2024 b, guía 6 ej. 5)** · fila "pago en X" (1, o 3 si cae refuerzo) → Factor Total = Σ(veces X × v^t) → **X = Precio / Factor Total**.
- **Sistema alemán** · cuota_t = P/n + saldo_(t−1) × i. **Francés** · C = i·P/(1 − (1 + i)^−n) · `=i*P/(1-(1+i)^-n)`.
- **Bullet (americano)** · cada período paga P·i; el último P·i + P. **Perpetuidad** · VP = C/i; creciente: C/(i − g).
- **Control con tasas** · financiarse le gana al contado si su TEA < la tasa de oportunidad (2C2024: B 31,9 % y C 35,8 % < 42 %). El costo de un francés con cuota dada es su TIR: `=IRR(-P, C, …, C)` (1C2023).
- **Descuento por pagar contado (1C2018)** · VP de las cuotas a la tasa de la financiación − precio contado; en % = descuento / VP.

- **Sin tasa de oportunidad (1C2026 a: alemán vs. bullet)** · se comparan las TEA, llevadas al mismo período: el que tiene menor TEA es más barato por peso y por año (bullet 12,36 % < alemán 13,10 %). Escribí el supuesto: con una tasa de oportunidad k, ganaría el de menor VP por peso prestado, y eso depende de k. Con k > 12,6 % gana el bullet; con k menor gana el alemán, que se cancela antes.

⚠ La menor TEA NO es siempre la mejor: importa también cuánto y cuánto tiempo financia (TEA 30 % por 1 mes ahorra menos que TEA 35 % por 12). Si hay tasa de oportunidad, ordená por VP. ⚠ Sumar pagos sin descontar no decide nada. ⚠ Descontar cada préstamo a su propia tasa da siempre el monto prestado: usá una tasa común.

### Tipo B · Cuadro de marcha, interés y saldo

Salió en 1C2018 b) (total amortizado, francés), 2C2018 (cuota francés y alemán), 1C2023 b) (composición de la cuota 3), 1C2025 e) f) (cuotas 1 y 2 alemán y saldo) y 1C2026 a) (interés del mes 12).

| Fila | Alemán | Francés | Bullet |
|---|---|---|---|
| Saldo inicial | P; después = saldo final anterior | igual | P siempre |
| Interés | saldo inicial × i | saldo inicial × i | P × i |
| Amortización | P/n (fija) | cuota − interés (crece) | 0; la última = P |
| Cuota | interés + amortización (baja) | fija | P·i; la última P·i + P |
| Saldo final | saldo inicial − amortización | saldo inicial − amortización | P hasta la última |
| Saldo tras k cuotas | P·(1 − k/n) | C·(1 − (1 + i)^−(n − k))/i | P |

- **Total amortizado tras k** · P − saldo_k (1C2018: 20.300 − 13.799,49 = 6.500,51).
- **Interés de una cuota** · columna interés de esa cuota (1C2026: cuota 12 = saldo tras 11 × TEM).
- **Bullet con cupones semestrales (1C2026)** · n en semestres (4 años = 8), tasa semestral; en el año t vencen los cupones 2t − 1 y 2t.
- **Con la calculadora** (`laboratorio/calculadora_andy.xlsx`, pestaña Calculadora de Préstamos) · Préstamo, Períodos y Tasa **del período de la cuota** (C3, C4, C5). Un préstamo por vez: anotá los resultados antes de cargar el siguiente. 1C2026: alemán 1.000.000 · 48 · TEM 1,0310 % → período 12; bullet 500.000 · 8 · 6 % → período 2; francés 1.250.000 · 25 · 0,5 %. La TEM y las TEA salen de la pestaña Conversor de Tasas.

⚠ El saldo baja por la **amortización**, no por la cuota. ✔ Control: saldo final de la última cuota = 0.

### Tipo C · Refinanciar, precancelar o cancelar

Salió en 2C2018 (precancela 50 % con penalidad y refinancia en alemán anual), 1C2025 (alemán → francés y cancelación), 1C2026 b) (dos préstamos → un francés) y 2C2010 b) (deuda al año).

- **Paso 1 · saldo a la fecha** · el del cuadro (o la fórmula del tipo B). Si son varios préstamos, sumá los saldos (1C2026: 750.000 + 500.000).
- **Paso 2 · lo que se paga hoy** · monto precancelado + penalidad = % × saldo + % penalidad × monto precancelado (2C2018).
- **Paso 3 · nuevo préstamo** · sobre lo que queda; con su tasa en el período de sus cuotas (2C2018: cuotas anuales → TEA). La cuota k nueva cae en el mes k + (cuotas viejas pagadas).
- **¿Conviene refinanciar?** · VP de las cuotas nuevas a la tasa VIEJA < saldo viejo → conviene (1C2025). Equivale a tasa nueva < tasa vieja.
- **VP de toda la operación** · fila de flujos (+ préstamo, − cuotas, − cancelación) × factor a la tasa pedida → SUM.

⚠ Más pesos de interés por un plazo más largo no dicen si conviene.

### Tipo D · Comprar o alquilar (2C2025)

- **VP alquilar** · alquiler mensual × a(n, TEM), con a(n, i) = (1 − (1 + i)^−n)/i · `=A*(1-(1+i)^-n)/i`. Si VP alquilar > precio contado → comprar.
- **Tabla por usos** · una fila por cantidad de partidos; la primera fila con VP > precio es la respuesta.
- **Tipo de cambio de indiferencia** · precio = VP alquiler k meses + USD × TC/(1 + i)^k → TC = (precio − VP alq)·(1 + i)^k/USD.
- **Costo hundido** · lo ya pagado no entra: se decide desde hoy.

### Tipo E · Ahorrar para un objetivo y financiar el resto (2C2010)

- **VF de depósitos A** · A·s(n, i), s(n, i) = ((1 + i)^n − 1)/i · `=A*((1+i)^n-1)/i`. Depósitos mensuales con TEM; anuales con TEA.
- **Saldo** · costo − ahorros; capitalizado mientras no se paga: saldo·(1 + i)^t. **Cuota** · francés sobre ese saldo.
- **VP para retirarse (guía 6 ej. 2)** · C/i, C/(i − g) o C·a(n, i) → depósito = VP/s(n, i).

### Tipo F · Tasa real (2C2018 4, 1C2023 c)

- **Fisher** · r = (1 + i)/(1 + inflación) − 1, las dos efectivas del mismo plazo · `=(1+i)/(1+infl)-1`.

⚠ Con la TEA, no con la TNA (la inflación es efectiva anual).

## Problema 2 · Evaluación de proyectos

### 0 · ¿Qué entra al flujo? (salió en todos los parciales)

| Concepto | ¿Entra? | Parciales |
|---|---|---|
| Estudio o consultora ya hecho | NO: costo hundido (ΔVAN = 0) | 2010, 2018-C2, 2023, 2024, 2025-C1, 2025-C2, 2026 |
| Costos prorrateados o personal que ya está | NO: no son incrementales | 2018-C1, 2026 |
| Ingreso que se deja de cobrar | SÍ, restando: costo de oportunidad o canibalización | 2010 (alquiler), 2018-C2 y 2023 (gas), 2024 (plateas viejas) |
| Comisión % de ventas | SÍ, como costo | 2010 |
| Fletes, instalación, puesta a punto | SÍ, a la inversión amortizable | 2018-C2, 2023, 2024 |

### 1 · Auxiliar (columna izquierda)

| Auxiliar | Fórmula | Excel |
|---|---|---|
| Base amortizable | inversión (+ fletes, instalación) − valor de rezago contable | `=Inv-VRC` |
| Amortización anual | base / VU contable; 0 después de la VU contable | `=Base/VU` |
| Valor libro al vender en t | inversión − amortización × años amortizados (mín. VRC) | `=Inv-Amort*t` |
| Resultado venta BU | valor de venta − valor libro (+ gravado; − ahorra impuesto) | `=VM-VL` |
| Recupero Kt · pérdida Kt | Kt × % recupero · Kt − recupero | `=Kt*rec` · `=Kt-Rec` |

### 2 · Cuadro de resultados (años 1…n)

| Fila | Cómo |
|---|---|
| Ingresos | precio × volumen (por mercado si hay mezcla, 2018-C2: mín. 70 % local) |
| (−) Costos | variables (unitario × volumen), fijos, personal, alquiler, comisión, ingreso perdido |
| **= EBITDA** | `=SUM(ingresos y costos del año)` |
| (±) Resultado venta BU | solo el año de la venta |
| (−) Pérdida Kt | Kt no recuperado, el último año (supuesto de Andy: deducible) |
| (−) Amortización | cada año de VU contable |
| **= EBIT** | EBITDA + resultado venta − pérdida Kt − amortización |
| (−) I.G. | `=-EBIT*IG` (EBIT negativo → ahorro, la empresa tiene otras ganancias) |
| **= Utilidad neta** | EBIT − I.G. |

### 3 · Flujo de fondos y VAN (años 0…n)

| Fila | t = 0 | Años 1…n |
|---|---|---|
| EBITDA | 0 | = EBITDA del cuadro |
| (−) Inversión BU | −inversión | pagos en etapas en su año (2025-C2: 40 % / 60 %) |
| (+) Venta BU | | valor de venta bruto el año de venta |
| (±) Kt | −Kt | −ΔKt cada año si Kt es % de ventas o costos; + recupero el último año |
| (−) I.G. | | = I.G. del cuadro |
| **= FF** | `=SUM(filas)` | `=SUM(filas)` |
| **VAN** | `=NPV(TREMA,FF1:FFn)+FF0` | VAN > 0 → se acepta |
| **TIR** | `=IRR(FF0:FFn)` | TIR > TREMA ↔ VAN > 0 |

⚠ NPV toma el primer valor como t = 1: el FF del año 0 va afuera, sumado. ✔ Control en años normales: FF = EBITDA·(1 − IG) + IG·amortización.

### 4 · Variantes que tomaron

- **Horizonte ≠ VU contable (2018-C1, 2024, 2010)** · amortizás solo los años de VU contable; si el proyecto termina antes, vendés con VL > 0 y la pérdida ahorra impuesto (2024: VL 1.040, venta 300 → −740).
- **Kt como % de ventas o costos (2010, 2026)** · Kt_t = % créditos × ventas_t − % deudas × CV_t; en el flujo va la **variación** −(Kt_t − Kt_(t−1)) y se recupera al final. Idea: cada año cobrás lo que te debían del año anterior y pagás lo que debías, así que solo ponés lo que **aumenta** el agujero. 1C2026: año 1 me deben 300 y debo 100 → pongo 200; año 2 me deben 600 y debo 200 (falta 400), recupero los 200 netos del año 1 → pongo 200 más; años 3 a 5 → 0; al final vuelven 400. Ventas a cobrar al año siguiente: el último cobro cae en n + 1 (2010).
- **Inversión en etapas (2025-C2)** · cada pago en su año; la amortización arranca sobre el total.
- **FEO + FEE (2025-C2, guía 7)** · FEO = (ventas − costos)(1 − IG) + IG·amort.; FEE (BU) = VM − IG·(VM − VL); FEE (Kt) = recupero + IG·pérdida Kt.

### 5 · Preguntas extra

- **Costo hundido (1C2025 g)** · ΔVAN = 0. Sin estudio cambia el riesgo, no el VAN.
- **Otra vida contable (2C2025 b)** · amortizar en más años da el mismo escudo total pero más tarde → VAN **menor**. Δescudo_t = Δamort_t × IG; ΔVAN = Σ Δescudo_t/(1 + TREMA)^t.
- **Valor límite (1C2025 h: alquiler)** · 1) ΔFF por $1 de gasto = −(1 − IG); 2) ΔVAN por $1 = ΔFF × a(n, TREMA); 3) Δ límite = VAN / |ΔVAN por $1|. ✔ Control: con ese valor, VAN = 0.

IG = tasa de impuesto a las ganancias · VM = valor de mercado · VL = valor libro · VRC = valor de rezago contable · Kt = capital de trabajo · BU = bien de uso · v^t = 1/(1 + i)^t.

## Anexo · Todas las fórmulas que usó Andy

### Guía 5 · Información contable y análisis financiero [X12]

| Fórmula | Excel | Ej. |
|---|---|---|
| Amortización acumulada = años × (costo / vida útil) | `=Años*(Costo/VU)` | 2 |
| Valor libro = costo − amortización acumulada; resultado por venta = VM − VL | `=Costo-AmortAc` · `=VM-VL` | 2 |
| Valor residual = 10 % × costo; amortización = (costo − residual) / VU | `=(Costo-VR)/VU` | 3 |
| Diferencia de deducciones ΔD = D_II − D_I; efecto fiscal = 35 % × ΔD | `=DII-DI` · `=IG*DeltaD` | 3 |
| Intereses devengados = saldo × tasa | `=Saldo*i` | 4, 6 |
| Pasivo corriente = deudas comerciales + bancarias | `=DCom+DBanc` | 5, 7 |
| Liquidez corriente = AC / PC → AC = PC × índice | `=PC*LiqCorr` | 5 |
| Prueba ácida = (AC − inventario) / PC → inventario = AC − índice × PC | `=AC-Seca*PC` | 5 |
| Liquidez absoluta = disponibilidades / PC | `=Absoluta*PC` | 5 |
| Créditos por ventas = AC − disponibilidades − inventario | `=AC-Disp-Inv` | 5 |
| Ventas = créditos / plazo de cobro × 360 | `=Cred/Plazo*360` | 5 |
| Costo de ventas = inventario / días de inventario × 360 | `=Inv/Dias*360` | 5 |
| EBIT = ventas − costo − gastos − amortizaciones | `=V-CMV-Gastos-Amort` | 5 |
| Cobertura de intereses = EBIT / intereses | `=EBIT/Int` | 5, 6 |
| Utilidad neta = ROE × PN; IG = UAI − UN | `=ROE*PN` | 5 |
| EBIT desde la utilidad neta = UN / (1 − IG) + intereses | `=UN/(1-IG)+Int` | 6 |
| Capital de trabajo = AC − PC | `=AC-PC` | 7 |
| Necesidad de fondos = Δactivos − Δpasivos espontáneos | `=DeltaA-DeltaP` | 7 |

### Guía 6 · Valor tiempo del dinero [X13]

| Fórmula | Excel | Ej. |
|---|---|---|
| TEA = (1 + TNA/m)^m − 1; TEM = (1 + TEA)^(1/12) − 1 | `=(1+TNA/m)^m-1` · `=(1+TEA)^(1/12)-1` | 1, 8 |
| Cuota francés = i·P/(1 − (1 + i)^−n) | `=(i*P)/(1-(1+i)^-n)` | 1, 4, 9 |
| Factor de acumulación s(n, i) = ((1 + i)^n − 1)/i | `=((1+i)^n-1)/i` | 2 |
| VP perpetuidad = C/i; creciente = C/(i − g) | `=C/i` · `=C/(i-g)` | 2 |
| VP renta = C·(1 − (1 + i)^−n)/i | `=C*(1-(1+i)^-n)/i` | 2, 3, 6, 10 |
| VP de un pago = F/(1 + i)^n | `=F/(1+i)^n` | 3, 9, 10 |
| Interés de la cuota 1 = P × i; amortización = cuota − interés | `=P*i` · `=C-Int` | 4 |
| Saldo tras k cuotas = C·(1 − (1 + i)^−(n − k))/i | `=C*(1-(1+i)^-(n-k))/i` | 4, 6 |
| Cuotas que faltan: n = −ln(1 − i·D/C)/ln(1 + i) | `=-LN(1-i*D/C)/LN(1+i)` | 4 |
| Factor v^t = 1/(1 + i)^t; X = precio / Σ factores | `=1/(1+i)^t` · `=P/SUM(f)` | 5 |
| Nueva cuota tras pago extra = i·(saldo − pago)/(1 − (1 + i)^−(n − k)) | `=(i*S)/(1-(1+i)^-(n-k))` | 6 |
| Intereses pagados = total pagado − capital | `=Pagado-P` | 6 |
| Flujo con comisión: t0 = monto − comisión; cupón = TNA/2 × saldo | `=P-Com` · `=-(TNA/2)*Saldo` | 7 |
| TEA desde la semestral = (1 + i_s)^2 − 1 | `=(1+is)^2-1` | 7 |
| m = 365/180 (capitaliza cada 180 días) | `=365/180` | 8 |
| Cambio de plazo = (1 + i)^(q/p) − 1 | `=(1+i)^(q/p)-1` | 8 |
| Tasa real = (1 + i)/(1 + infl) − 1; real a 30 días = (1 + r)^(30/365) − 1 | `=(1+i)/(1+infl)-1` | 8 |
| Alemán: amortización = P/n; interés = saldo × i; cuota = int + amort | `=P/n` · `=S*i` · `=Int+Amort` | 9 |
| Interés simple (crédito de proveedor) = M·i·n | `=M*i*n` | 9 |
| VP de refuerzos R cada k meses, N veces = R·v^k·(1 − v^(kN))/(1 − v^k), v = (1 + i)^−1 | `=R*(1+i)^-k*(1-((1+i)^-k)^N)/(1-(1+i)^-k)` | 10 |

### Guía 7 · Evaluación de proyectos [X14]

| Fórmula | Excel | Ej. |
|---|---|---|
| Amortización fiscal = (inversión − VRC)/VU | `=(Inv-VRC)/VU` | 1, 2, 4–7 |
| Valor libro = inversión − amortización × años | `=Inv-Amort*t` | 1, 4–6 |
| Resultado venta = VM − VL | `=VM-(Inv-t*Amort)` | 1, 4–7 |
| FEO = EBIT·(1 − IG) + amortización | `=EBIT*(1-IG)+Amort` | 1, 5–7 |
| FEE (BU) = VM − IG × resultado venta | `=VM-Res*IG` | 1, 7 |
| FEE (Kt) = recupero + IG × pérdida Kt | `=Rec+IG*Perd` | 6, 7 |
| Inversión total = compra + instalación (base amortizable) | `=-(Compra+Inst)` | 2 |
| Gasto en t = 0 neto de impuesto = −G·(1 − IG) | `=-(G-G*IG)` | 2 |
| Venta de máquina vieja neta = V − IG·(V − VL) | `=V-V*IG` (con VL = 0) | 2 |
| Escudo fiscal = amortización × IG; ΔVAN = Σ Δescudo × factor | `=Amort*IG` · `=SUM(...)` | 3 |
| Ventas = volumen × precio; costo variable = volumen × costo unitario | `=Q*P` · `=-Q*CVu` | 4 |
| Recupero Kt = Kt × % recupero; pérdida Kt = Kt − recupero | `=Kt*rec` · `=Kt-Kt*rec` | 4, 6, 7 |
| EBITDA = SUM(ingresos y costos); EBIT = EBITDA + otros − amortización | `=SUM(...)` | 4–7 |
| I.G. = −EBIT × IG; UN = EBIT + I.G. | `=-EBIT*IG` · `=EBIT+IG` | 4–7 |
| FF = SUM de las filas del año | `=SUM(...)` | 1–7 |

### Parciales resueltos por Andy (1C2025, 2C2025, 2C2024, 1C2026)

| Fórmula | Excel | Parcial |
|---|---|---|
| TEM = (1 + TNA/360)^30 − 1; TEA = (1 + TEM)^12 − 1 | `=(1+TNA/360)^30-1` | 2C2025 P1 |
| VP alquiler = alquiler × a(n, TEM); margen = precio − VP; VF = VP·(1 + i)^n; TC = VF/USD | `=A*a` · `=M*(1+i)^n` · `=VF/USD` | 2C2025 P1 |
| TEM = (1 + TEA)^(1/12) − 1; TEM = TNA/12 | `=(1+TEA)^(1/12)-1` · `=TNA/12` | 1C2025, 2C2024 P1 |
| Cuadro alemán y francés (tipo B); VP operación = SUM(flujo × factor) | `=SUM(VP)` | 1C2025 P1 |
| VP de cada opción = SUM(pago × factor); X = precio / factor total | `=SUM(VP)` · `=P/FT` | 2C2024 P1 |
| Base amortizable = infraestructura + paneles − VRC; inversión por etapas = % × paneles | `=Infra+Pan-VRC` · `=Pan*Pct` | 2C2025 P2 |
| Ingreso incremental = nuevos × precio − perdidos × precio viejo | `=N*P-Np*Pv` | 2C2024 P2 |
| VAN = NPV(TREMA; FF1..FFn) + FF0; TIR = IRR(FF0..FFn) | `=NPV(TREMA,FF)+FF0` · `=IRR(FF)` | 2C2025, 1C2025, 2C2024 P2 |
| ΔFF por $1 de alquiler = −1 + IG; ΔVAN = ΔFF × a(n, TREMA); ΔA = −VAN/ΔVAN | `=-1+IG` · `=-VAN/dVAN` | 1C2025 P2 |
| i_trim = TNA/4; TEM = (1 + i_trim)^(1/3) − 1; TEA = (1 + i_trim)^4 − 1; TEA bullet = (1 + i_s)^2 − 1 | `=(1+itrim)^(1/3)-1` · `=(1+is)^2-1` | 1C2026 P1 |
| Alemán: interés cuota 12 = saldo inicial × TEM; saldo tras 12 = P·(1 − 12/n); bullet: cupón = P × i_s | `=S*i` · `=P*i` | 1C2026 P1 |
| Saldo a refinanciar = saldo alemán + capital bullet; cuota francés = i·S/(1 − (1 + i)^−n) | `=i*S/(1-(1+i)^-n)` | 1C2026 P1 |
| Kt_t = % créd. × ventas − % deudas × CV; inversión en Kt = Kt_(t−1) − Kt_t; recupero = Kt_n | `=V*pc-CV*pd` · `=KtAnt-Kt` | 1C2026 P2 |

Fuentes [X12] [X13] [X14] (guías de Andy, no oficiales); parciales en `practica/segundo-parcial/`; cátedra [T03] [T04] [G05] [R02] [R03].
