# Hoja de fórmulas · Segundo parcial

## Valor tiempo del dinero

### 1. Ubicá los flujos y convertí la tasa

- **Línea de tiempo** · Marcá fecha de decisión (0), cobros (+), pagos (−) y primera y última cuota. Elegí el período de las cuotas y expresá la tasa en ese mismo período.
- **Tasa efectiva** · Con m capitalizaciones/año, i_cap = TNA/m. TEA = (1+i_cap)^m − 1. Para pasar de duración p a duración q, i_q = (1+i_p)^(q/p) − 1.
- **Inflación** · 1+i_real = (1+i_nominal)/(1+inflación), con tasas del mismo período. Flujos en moneda corriente → tasa nominal. Flujos en moneda constante → tasa real.

### 2. Valuá el flujo o calculá la cuota de ahorro

- **Flujo único** · VF = VP(1+i)^n · VP = VF/(1+i)^n. Si el enunciado da interés simple, VF = VP(1+i·n).
- **Cuotas iguales** · a(n,i) = [1−(1+i)^(−n)]/i · s(n,i) = [(1+i)^n−1]/i. Con cuota C vencida, VP = C·a(n,i) y VF = C·s(n,i). Si es anticipada, multiplicá por (1+i).
- **Renta diferida o perpetua** · Valuá un período antes del primer cobro y trasladá ese valor a la fecha objetivo. Perpetuidad = C₁/i · Creciente = C₁/(i−g), con i > g y C₁ primer cobro.
- **Ahorro para una meta** · Valuá los retiros futuros en la fecha de la meta. Para n depósitos vencidos hasta esa fecha, depósito = meta/s(n,i).

### 3. Armá el cuadro de marcha del préstamo

| Período k | Saldo inicial | Interés | Amortización de capital | Cuota | Saldo final |
|---|---|---|---|---|---|
| 1, 2, …, n | S anterior (P al inicio) | I = i·S inicial | A según sistema | C = I + A | S final = S inicial − A |

- **Francés** · Cuota fija C = P/a(n,i) · A = C − I · Saldo después de k cuotas = C·a(n−k,i). Excel con P positivo → =−PAGO(i;n;P).
- **Alemán** · A = P/n · Cuota decreciente · S después de k cuotas = P(1−k/n). El interés de la cuota k usa el saldo al cierre de k−1.
- **Americano / bullet** · I = P·i en cada cupón. A = 0 hasta la última cuota, que suma P. **Directo** · A = P/n e I = P·i siempre, aun cuando baje el saldo.
- **Qué pide la fecha** · Interés de una cuota → columna I. Interés acumulado → sumar I del intervalo. Capital amortizado → P − S. Deuda tras pagar la cuota → saldo final.

### 4. Compará alternativas en la misma fecha

- **Refinanciar o precancelar** · Tomá el saldo a la fecha indicada, restá el capital que se cancela y aplicá al resto el nuevo plazo y la nueva tasa. Si piden conveniencia, compará el VP de los pagos pendientes con el VP del nuevo plan, incluidos los cargos.
- **Contado / cuotas / alquiler** · VP de costos = anticipo + Σ[pago_k/(1+i_op)^k]. Usá el costo de oportunidad i_op y elegí el menor VP a igual fecha, moneda y horizonte. Si cambia la decisión, evaluá desde la nueva fecha con los pagos futuros.
- **Valor de indiferencia** · Igualá ambos VP y despejá precio, alquiler o tipo de cambio. Si la compra en moneda extranjera ocurre en k, su VP es precio en divisa × TC/(1+i_op)^k.
- **Tasa implícita y CFT** · Excel → =TIR(rango de flujos) con capital neto recibido (+) en 0 y cuotas con cargos (−). Anualizá con (1+i)^m−1. Para comparar solo intereses, usá TEA. Con comisiones o seguros, compará el CFT anual.

P = capital inicial · n = número de cuotas o períodos · i = tasa efectiva por período · k = período evaluado.
Fuentes [T03, pp. 2, 9–12, 15–29, 34] [G05, pp. 1–2] [R02] [R03]

## Evaluación de proyectos

- **Alcance** · Armá columnas 0 a n con los flujos incrementales (con proyecto menos sin proyecto). Cargá 0 si una partida no aplica.
- **Qué entra** · Ingresos, egresos y ahorros incrementales. Incluí costo de oportunidad y canibalización. Hundidos y prorrateos sin cambio de caja → 0. Financiamiento → TREMA.

### 1. Plantilla de la cátedra · repetí el cálculo en cada período t

| Fila P3 | Concepto | Cómo se calcula |
|---|---|---|
| 28 | Unidades vendidas | Cantidad del período. Abrí por producto si hay varios. |
| 29 | Ventas | Σ(precio × unidades vendidas) + otros ingresos operativos incrementales. |
| 30 | (–) Costos variables | Σ(costo variable unitario × unidades). Como la fila se resta, un costo extra va positivo y un ahorro va negativo. |
| 31 | (–) Costos fijos | Costos fijos incrementales. Sumá otros egresos operativos y restá ahorros, antes de impuestos. |
| 32 | (–) Amortización | Por activo, (costo capitalizado − rezago contable)/vida contable. Desde la puesta en servicio hasta agotar la base. |
| 33 | = UAII (resultado operativo) | 29 − 30 − 31 − 32. El EBITDA es el mismo cálculo antes de restar 32. |
| 34 | (–) Impuesto a las ganancias (50%) | τ × UAII. Usá la tasa del enunciado. Si da negativo, computá el ahorro cuando pueda aprovecharse. |
| 35 | = Utilidad neta | 33 − 34. Un impuesto negativo se resta y aumenta el resultado. |
| 36 | (+) Amortización | Copiá 32. El desembolso por el activo se registra en 38. |
| 37 | = Flujo operativo | 35 + 36. |
| 38 | (–) Inversión en maquinaria | −pagos de compra, instalación capitalizable y reposiciones, cada uno en su fecha. |
| 39 | (–/+) Variación de capital de trabajo | −variación de CT (fila 50). Si el CT aumenta, consume caja. |
| 40 | (+) Recupero de capital de trabajo | Al cierre, monto recuperado + τ × monto perdido si la pérdida es deducible y aprovechable. |
| 41 | (+) Valor residual neto maquinaria | VM − τ(VM−VL) con efecto fiscal inmediato y aprovechable. VL = costo − amortización acumulada. |
| 42 | = FLUJO DE FONDOS NETO | Sumá 37 a 41 con sus signos. |
| 43 | Factor de actualización  1/(1+TREMA)^t | 1/(1+i)^t. i es la TREMA del enunciado por período. En 0, factor = 1. |
| 44 | Flujo de fondos descontado | 42 × 43. |
| 47 | Créditos con clientes (20% ventas) | Saldo por cobrar. Aplicá el porcentaje del enunciado sobre las ventas indicadas. |
| 48 | Deudas con proveedores (30% costos var.) | Saldo por pagar. Si dan % sobre CV, multiplicalo por los CV del período. |
| 49 | = Capital de trabajo neto | Inventarios + 47 − 48, más otros saldos operativos que indique el enunciado. |
| 50 | Variación de capital de trabajo | CT actual − CT previo. Para CT inicial, usá CT previo = 0. Si lo recuperás en 40, calculá el último saldo antes del recupero. |

- **Fechas especiales** · Venta del equipo viejo → 41 al vender. Gasto inicial deducible → FEO de 0 con efecto fiscal. IG diferido → ajustá el FEO al impuesto pagado.
### 2. Análisis que salen del mismo cuadro

- **VAN / TIR** · VAN = suma de 44 o FC₀+VNA(i;FC₁:FCₙ). VAN > 0 → invertir. TIR = TIR(fila 42, de 0 a n). Para un flujo convencional, TIR > TREMA → invertir.
- **TIRM / IR** · TIRM = (VF de positivos / VP absoluto de negativos)^(1/n) − 1. Usá tasas de reinversión y financiación, respectivamente. IR = VP futuro / inversión inicial si toda la inversión ocurre en 0.
- **Recupero / exposición** · Acumulá 42 (simple) o 44 (descontado). Recupero = último período antes de recuperar + saldo faltante/flujo siguiente. Exposición = magnitud del mayor déficit acumulado de 42.
- **Sensibilidad** · VAN = 0 para hallar precio, volumen, costo o inversión límite. Entre alternativas comparables, igualá los VAN. Si cambia la amortización, recalculá 32 a 37 y el valor de libros en 41.
- **VAE / CAE** · Si las alternativas son repetibles y duran distinto, elegí el mayor VAE = VAN/a(n,i) o el menor CAE = VP de costos/a(n,i).

τ = tasa del impuesto a las ganancias · i = TREMA por período · VM = valor de mercado · VL = valor de libros · CT = capital de trabajo.
Rótulos de P3 [R03]. Usá las tasas y porcentajes del enunciado. [T04, pp. 19–25, 34–38, 57–72] [G04, p. 1] [G05, pp. 2–5] [R02]
