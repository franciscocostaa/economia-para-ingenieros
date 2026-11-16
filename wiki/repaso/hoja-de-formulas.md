# Hoja de fórmulas · Segundo parcial

## Valor tiempo del dinero

Sintaxis cátedra: todo a mano con `^`; únicas funciones `SUM`, `IRR`, `POWER`, `IF`, `ROUND`. Cargá los datos en celdas y referencialas con `$`; no tipees tasas redondeadas a mano.

### Tasas — dividí una sola vez, después exponente

| De → a | Fórmula | Excel |
|---|---|---|
| TNA → tasa del período que capitaliza | i_cap = TNA/m · m = capitalizaciones/año: anual 1, semestral 2, trimestral 4, mensual 12, diaria 360 | `=TNA/m` |
| TNA → TEA | (1+TNA/m)^m − 1 | `=(1+TNA/m)^m-1` |
| Efectiva de plazo p → plazo q | (1+i_p)^(q/p) − 1 · cambiar de período es **exponente, nunca dividir** | `=(1+ip)^(q/p)-1` |
| Dan la cuota o el flujo, falta la tasa | TIR del flujo: + lo recibido en 0, − los pagos | `=IRR(rango)` |
| Perpetuidad (pagás C para siempre por P) | i = C/P | `=C/P` |
| Inflación f (Fisher) | i_real = (1+i_nom)/(1+f) − 1 | `=(1+i)/(1+f)-1` |

⚠ Lo que me equivoqué: TNA 30% **diaria** → TEM = (1+0,30/360)^30 − 1 = 2,53% (NO 0,30/12). Semestral → mensual = (1+i_sem)^(1/6) − 1 (NO /6). Y 0,08/12 = 0,667%, cuidá la coma (no 6,67%).

### Valuar flujos

| Caso | VP (hoy) | VF (en la fecha n) |
|---|---|---|
| Pago único C en la fecha n | C/(1+i)^n | C·(1+i)^n |
| n cuotas iguales vencidas | C·a(n,i), con a(n,i) = (1−(1+i)^−n)/i | C·s(n,i), con s(n,i) = ((1+i)^n−1)/i |
| Despejar la cuota / el depósito | cuota = VP/a(n,i) | depósito meta = VF/s(n,i) |
| Cuotas anticipadas (pago al inicio) | multiplicá el VP por (1+i) | |
| Perpetuidad · creciente al g | C/i · C/(i−g) con i>g | |

⚠ Sumá **todos** los flujos, incluido el de hoy: el pago en t=0 va sin descontar. Me lo olvidé más de una vez.

### Préstamos — el cuadro de marcha

Fila a fila: **saldo inicial → interés = i × saldo inicial → amortización → cuota = interés + amortización → saldo final = saldo inicial − amortización**. La tasa i va en el período de la cuota: convertila antes de armar el cuadro.

⚠ **El saldo baja por la AMORTIZACIÓN, no por la cuota.** La cuota también paga interés, y el interés no cancela deuda: saldo nuevo = saldo viejo − amortización (jamás − cuota entera).
⚠ El interés se calcula sobre el **saldo inicial** del período, que es el saldo final del período anterior.
✔ Control que nunca falla: el saldo llega a **0** en la última cuota. Si no da 0, el saldo está mal armado.

| Sistema | Qué queda fijo | Cuota | Interés | Amortización | Saldo tras k cuotas |
|---|---|---|---|---|---|
| Francés | la cuota | P·i/(1−(1+i)^−n) | i·saldo (baja) | cuota − interés (sube) | C·a(n−k,i) = VP de lo que falta |
| Alemán | la amortización | interés + amort (baja) | i·saldo (baja) | P/n (fija) | P·(1−k/n) |
| Americano / bullet | el saldo | P·i; la última suma + P | P·i (constante) | 0 hasta la última, que devuelve P | P |
| Directo | el interés | (P + P·i·n)/n | P·i siempre (sobre P original) | P/n (fija) | P·(1−k/n) |

Ejemplo francés (P = 20300, i = 2%, cuota = 3624,07): saldo tras la cuota 1 = 20300 − (3624,07 − 406) = **17081,93**. El error sería hacer 20300 − 3624,07 = 16675,93.

Qué pide la fecha: interés de una cuota → columna interés · capital amortizado hasta k → P − saldo (= suma de las amortizaciones) · deuda para cancelar hoy → el saldo = VP de las cuotas que faltan = C·a(n−k,i).

### Comparar alternativas (misma fecha, misma tasa)

- **Qué préstamo conviene** · menor TEA, o menor VP de los pagos descontados a una misma tasa. Control: un préstamo descontado a su propia tasa da exactamente P.
- **Precancelar** · saldo a la fecha = VP de las cuotas que faltan. ⚠ Penalidad = % × el **monto que cancelás**, no sobre el saldo total. Renegocio: deuda nueva = saldo − cancelado; cuota nueva = deuda/a(n′, i′).
- **Contado vs financiado** · VP de costos = pago de hoy + Σ pago_k/(1+i)^k, con i la tasa de oportunidad (la billetera o inversión alternativa). Gana el menor VP, a igual horizonte.
- **Indiferencia** · igualá los dos VP y despejá (precio, alquiler, tipo de cambio). Compra en divisa en la fecha k: VP = precio × TC/(1+i)^k si pagás en k, o precio × TC si pagás hoy. Aclará cuál.
- Costo hundido o alquiler ya pagado: no entra en la decisión. Si cambió la situación, compará desde hoy con los pagos que faltan.

Fuentes [T03] [G05] [R02] [R03]

## Evaluación de proyectos

Armá columnas 0 a n con flujos **incrementales** (con proyecto − sin proyecto). ⚠ Sumá TODOS los ítems de inversión (ej.: planta + tanques + cargadero + instalación): uno olvidado rompe la amortización, el año 0 y el FEO. Costos hundidos y prorrateos → fuera. Costo de oportunidad y canibalización → dentro.

### Cuadro período a período (plantilla de la cátedra, mismo orden que P3)

| Concepto | Cómo se calcula |
|---|---|
| Ventas | precio × unidades + otros ingresos operativos incrementales |
| (−) Costos variables | costo variable unitario × unidades |
| (−) Costos fijos | costos fijos incrementales (sumá otros egresos, restá ahorros) |
| (−) Amortización | (costo capitalizado − rezago)/vida contable, desde la puesta en servicio |
| = UAII | ventas − CV − CF − amortización (el EBITDA es lo mismo sin restar amortización) |
| (−) Impuesto a las ganancias | τ × UAII (si da negativo, es ahorro fiscal cuando se aproveche) |
| = Utilidad neta | UAII − IG |
| (+) Amortización | se devuelve: no fue salida de caja |
| = Flujo operativo (FEO) | UN + amortización = (ventas − costos)(1 − τ) + amortización × τ |
| (−) Inversión | compra, instalación capitalizable y reposiciones, cada una en su fecha |
| (−/+) Variación de capital de trabajo | − la variación del CT; si el CT sube, consume caja |
| (+) Recupero de capital de trabajo | al cierre. ⚠ SIN impuesto: es plata tuya que vuelve, no una ganancia |
| (+) Valor residual neto del activo | VM − τ(VM − VL), con VL = costo − amortización acumulada |
| = Flujo de fondos neto | suma de todo lo anterior con su signo |
| Factor de descuento · FF descontado | 1/(1+TREMA)^t · FF × factor |

CT neto = inventarios + créditos a clientes (× %ventas) − deudas a proveedores (× %costos). Variación = CT del período − CT anterior (el primer CT va en el año 0).

### Análisis que salen del mismo cuadro

- **VAN** = `SUM`(fila de FF descontado), o `=FC0+VNA(i;FC1:FCn)`. VAN > 0 → invertir.
- **TIR** = `IRR`(fila de FF neto, de 0 a n). Flujo convencional: TIR > TREMA → invertir.
- **TIRM** = (VF de los positivos / VP de los |negativos|)^(1/n) − 1 · **IR** = VP futuro / inversión inicial (si toda la inversión va en 0).
- **Recupero** = acumular el FF neto (simple) o el FF descontado hasta pasar a positivo. Exposición = el mayor déficit acumulado.
- **Sensibilidad**: poné VAN = 0 y despejá el precio, volumen, costo o inversión límite. **CAE / VAE** (vidas distintas): elegí el mayor VAE = VAN/a(n,i) o el menor CAE = VP de costos/a(n,i).

τ = impuesto a las ganancias · i = TREMA por período · VM = valor de mercado · VL = valor de libros · CT = capital de trabajo.
Fuentes [T04] [G04] [G05] [R02] [R03]
