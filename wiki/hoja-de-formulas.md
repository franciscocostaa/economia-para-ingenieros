# Hoja de fórmulas

Único material de consulta permitido en el parcial del 17/11/2026 (ver [modalidad](temas/segundo-parcial.md#modalidad-del-parcial-del-17112026)). Está pensada para imprimirse y usarse al lado de la planilla, así que prioriza densidad sobre explicación: el desarrollo de cada tema está en la página enlazada.

**Estado:** completas las secciones de tasas, préstamos, series y evaluación de proyectos. Las de costos, análisis financiero y contabilidad están en el nivel mínimo y se amplían al trabajar los verdadero/falso.

La columna "Excel" usa la sintaxis de la cátedra: todo a mano con `^`, sin funciones financieras. Las únicas funciones que aparecen en las resoluciones oficiales son `SUM`, `IRR`, `POWER`, `IF` y `ROUND` [R02] [R03].

---

## Reglas de oro

1. **Nunca sumes ni compares montos de fechas distintas.** Primero llevalos todos al mismo momento.
2. **Para cambiar el plazo de una tasa se usa el exponente, nunca la división.** Dividir es interés simple.
3. **La tasa y el plazo tienen que estar en la misma unidad de tiempo** antes de entrar a cualquier fórmula.
4. **El costo de un préstamo se compara por tasa efectiva, no por total pagado ni por cuota** [T03, p. 28].
5. **Si hay gastos, comisiones o seguros, el comparador es el costo financiero total, no la tasa** [T03, p. 34].
6. **En un flujo de proyecto no van los intereses**: el costo del financiamiento ya está en la tasa de descuento [T04, p. 19].
7. **Ante un dato ambiguo, escribí el supuesto y seguí**: el parcial lo pide explícitamente [P02, p. 1].

---

## 1. Tasas

Ver [valor tiempo del dinero](temas/valor-tiempo-del-dinero.md).

| Concepto | Fórmula | Excel |
|---|---|---|
| Interés simple | $M = C\,(1 + i\,n)$ [T03, p. 2] | `=C*(1+i*n)` |
| Interés compuesto | $M = C\,(1 + i)^n$ [T03, p. 2] | `=C*(1+i)^n` |
| Tasa proporcional del período | $i_m = TNA / m$, con $m$ = capitalizaciones por año [T03, p. 9] | `=TNA/m` |
| Tasa efectiva anual | $TEA = (1 + TNA/m)^m - 1$ [T03, p. 9] | `=(1+TNA/m)^m-1` |
| **Cambio de plazo de una tasa efectiva** | $1 + i_q = (1 + i_p)^{q/p}$ [G01, p. 3] | `=(1+ip)^(q/p)-1` |
| Tasa vencida ↔ adelantada | $(1 + i)(1 - d) = 1$ [T03, p. 8] | `=1-1/(1+i)` |
| Tasa real (Fisher, exacta) | $1 + i_r = (1 + i_n)/(1 + f)$ [T03, p. 12] | `=(1+in)/(1+f)-1` |
| Tasa nominal desde real | $1 + i_n = (1 + i_r)(1 + f)$ [T03, p. 33] | `=(1+ir)*(1+f)-1` |
| Costo financiero total | tasa interna de retorno del flujo real del préstamo, con todos los gastos [T03, p. 34] | `=IRR(rango)` |

**Ejemplo de capitalización cruzada** (el caso del parcial 16/06/2026): tasa nominal anual 12,5 % con capitalización trimestral, cuotas mensuales [R03].

- Trimestral efectiva: $12{,}5\%/4 = 3{,}125\%$ → `=B7/4`
- Mensual efectiva: $(1{,}03125)^{1/3} - 1 = 1{,}031\%$ → `=(1+B17)^(1/3)-1`
- Anual efectiva: $(1{,}03125)^4 - 1 = 13{,}098\%$ → `=(1+B17)^4-1`

**Trampas:** la tasa nominal anual no sirve para comparar ofertas con distinta capitalización [T03, p. 10]. Una tasa *directa* se aplica siempre sobre el capital original, incluso sobre lo ya devuelto: parece barata y no lo es [T03, p. 7].

---

## 2. Series de pagos

| Concepto | Fórmula | Excel |
|---|---|---|
| Valor futuro / presente de un monto | $F = P(1+i)^n$ ; $P = F/(1+i)^n$ [T03, p. 15] | `=P*(1+i)^n` ; `=F/(1+i)^n` |
| **Factor de actualización de una anualidad** | $a(n,i) = \dfrac{1 - (1+i)^{-n}}{i}$ | `=(1-(1+i)^-n)/i` |
| Valor presente de $n$ cuotas iguales vencidas | $VP = C \cdot a(n,i)$ | `=C*(1-(1+i)^-n)/i` |
| Factor de capitalización de una anualidad | $s(n,i) = \dfrac{(1+i)^n - 1}{i}$ | `=((1+i)^n-1)/i` |
| Anualidad adelantada | vale $(1+i)$ veces la vencida [X01] | `=VP_vencida*(1+i)` |
| Perpetuidad constante | $VP = F/i$ [G05, p. 1] | `=F/i` |
| Perpetuidad creciente a tasa $g$ | $VP = F/(i - g)$, con $F$ = **primer** flujo; requiere $i > g$ [G05, p. 1] | `=F/(i-g)` |

**Regla crítica de ubicación temporal:** las fórmulas de anualidad y perpetuidad dan el valor **un período antes del primer flujo**. Si el primer flujo está en $t = 11$, el resultado está parado en $t = 10$ y hay que dividirlo por $(1+i)^{10}$ para llevarlo a hoy [G05, p. 1].

---

## 3. Préstamos

Ver [valor tiempo del dinero](temas/valor-tiempo-del-dinero.md). Notación del cuadro de marcha: $S_t$ saldo, $I_t$ interés, $A_t$ amortización de capital, $C_t$ cuota.

**Identidades que valen en todos los sistemas:**

$$I_t = i \cdot S_{t-1} \qquad C_t = I_t + A_t \qquad S_t = S_{t-1} - A_t$$

El interés de la cuota $t$ se calcula sobre el saldo **anterior** al pago.

| Sistema | Qué es constante | Capital adeudado | Fórmulas |
|---|---|---|---|
| **Americano / bullet** | la cuota (solo interés) | **no baja nunca** hasta el final [T03, p. 22] | $C_t = i\,P$ ; $C_n = i\,P + P$ |
| **Alemán** | la amortización | baja en línea recta | $A = P/n$ ; $S_k = P\,(1 - k/n)$ |
| **Francés** | la cuota total | baja despacio al principio | $C = P \cdot \dfrac{i}{1 - (1+i)^{-n}}$ |
| **Directo** | la cuota | baja, pero el interés se cobra igual sobre $P$ [T03, p. 22] | costo real $>$ tasa declarada |

| Cálculo | Excel |
|---|---|
| Saldo del alemán tras $k$ cuotas | `=P*(1-k/n)` [R03] |
| Cuota del francés | `=P*i/(1-(1+i)^-n)` [R03] |
| Saldo del francés tras $k$ cuotas | `=C*(1-(1+i)^-(n-k))/i` |
| Amortización del francés, mes a mes | $A_{t+1} = A_t(1+i)$, con $A_1 = C - iP$ |

**Control de calidad:** si desplegás el cuadro completo, el saldo después de la última cuota tiene que dar exactamente 0.

**Refinanciar** = tomar el saldo adeudado a una fecha como capital de un préstamo nuevo, con otra tasa, plazo y sistema. Del préstamo viejo solo viaja el saldo. Si hay varios préstamos, los saldos se suman porque están medidos en la misma fecha [R03].

**Comparar alternativas de financiación:** llevar todas las tasas a la misma tasa efectiva (en general anual) y elegir la menor. El sistema de amortización por sí solo no cambia el costo: con la misma tasa, americano, alemán y francés cuestan lo mismo aunque el total pagado sea distinto [T03, p. 28]. La excepción es el directo.

---

## 4. Evaluación de proyectos

Ver [evaluación de proyectos](temas/evaluacion-de-proyectos.md).

### 4.1 Qué entra y qué no entra en el flujo

Prueba de la cátedra: un concepto entra **solo si está presente con el proyecto y ausente sin él** [G05, p. 3].

| Partida | ¿Entra? | Motivo |
|---|---|---|
| Estudio o consultora ya pagados | **No** | costo hundido |
| Costos fijos de estructura prorrateados | **No** | existen igual sin el proyecto |
| Sueldos de personal ya en nómina | **No** | no son un egreso incremental [R03] |
| Intereses del préstamo | **No** | ya están en la tasa de descuento [T04, p. 19] |
| Terreno o activo propio ocioso | **Sí** | costo de oportunidad |
| Ventas quitadas a otro producto propio | **Sí** | canibalización |
| Capital de trabajo | **Sí** | inversión que se recupera al final |
| Amortización contable | **Solo su efecto fiscal** | no es egreso, pero baja el impuesto |
| Impuesto a las ganancias | **Sí** | el flujo es después de impuestos |

Tabla verificada en [T04, p. 20].

### 4.2 Del cuadro de resultados al flujo

El cuadro de resultados se arma por lo **devengado** porque sobre él se calcula el impuesto; el flujo se arma por lo **percibido** [G05, p. 4].

```
  Ventas
− Costos variables
− Costos fijos incrementales
− Amortización                 ← no es caja, pero baja el impuesto
= Resultado operativo
− Impuesto a las ganancias
= Utilidad neta
+ Amortización                 ← se devuelve, no era caja
= Flujo económico operativo
```

Tres formas equivalentes de llegar al mismo flujo operativo [G05, p. 2]:

$$FEO = UN + A = (V - C)(1-t) + A\,t = V - C - t\,(V - C - A)$$

El término $A \cdot t$ es el **escudo fiscal** de la amortización.

### 4.3 Capital de trabajo

| Concepto | Fórmula |
|---|---|
| Nivel de capital de trabajo del año | créditos con clientes − deudas con proveedores [R03] |
| Créditos del año | % sobre las **ventas** del año |
| Deudas del año | % sobre los **costos variables** del año |
| Lo que va al flujo | la **variación** respecto del año anterior, con signo negativo |
| Recupero | el nivel acumulado, con signo positivo, en el último año |

Si se recupera menos de lo invertido, la diferencia es una pérdida deducible: recuperar el 80 % de 100 con $t = 30\%$ da $80 + 20 \cdot 0{,}3 = 86$ [G04, p. 1].

### 4.4 Venta del activo al final (valor residual)

$$FEE_{BU} = VR_m - t\,(VR_m - VL) \qquad VL = \text{valor de origen} - \text{amortizaciones acumuladas}$$

Excel: `=VRm-t*(VRm-VL)` [R03]. Funciona en los dos sentidos: si se vende **por debajo** del valor de libros, el paréntesis es negativo y el impuesto se convierte en un ahorro. Amortización anual $= (\text{valor de origen} - \text{valor de rezago contable}) / \text{vida fiscal}$ [T01, p. 45].

### 4.5 Criterios de decisión

| Criterio | Fórmula | Regla | Excel |
|---|---|---|---|
| **Valor actual neto** | $\sum_{j=0}^{n} FC_j/(1+i)^j$ [T04, p. 25] | aceptar si $> 0$ [T04, p. 34] | fila de factores `=1/(1+$i$)^t` y después `=SUM(...)` [R03] |
| **Tasa interna de retorno** | tasa que anula el valor actual neto [T04, p. 38] | aceptar si $>$ tasa de corte [T04, p. 43] | `=IRR(rango)` |
| Tasa interna modificada | $(VF_{ingresos}/VP_{egresos})^{1/n} - 1$ [T04, p. 58] | aceptar si $>$ tasa de corte | |
| Índice de rentabilidad | $1 + VAN/I$ [T04, p. 57] | aceptar si $> 1$ | |
| Período de recupero | $k + \dfrac{|\text{acumulado en } k|}{\text{flujo en } k+1}$ [T04, p. 61] | menor es mejor | |
| Valor o costo anual equivalente | $VAN / a(n,i)$ [T04, p. 70] | **obligatorio** para comparar vidas distintas [G05, p. 5] | |
| Máxima exposición | flujo acumulado más negativo [T04, p. 68] | mide el endeudamiento máximo | |

**No uses `VNA`/`NPV`**: esa función supone el primer flujo en $t = 1$ y descuenta de más la inversión inicial. La cátedra arma una fila de factores de descuento y suma [R03].

**Trampas de la tasa interna de retorno:** hay varias si el flujo cambia de signo más de una vez [T04, p. 50]; en una **desinversión** (cobrás primero, pagás después) la regla se invierte y conviene si es **menor** que la tasa de corte [T04, p. 52]; ignora la escala al comparar proyectos excluyentes, donde hay que analizar el incremental [T04, p. 56].

### 4.6 Tasa de descuento

- **Tasa de retorno esperada mínima aceptable**: rendimiento mínimo exigido; es el costo de oportunidad de los fondos [T04, p. 43].
- **Costo promedio ponderado del capital**: pondera el costo de cada fuente por su proporción, con la deuda **después de impuestos** [T04, p. 11]. Ejemplo: $\tfrac13 \cdot 6\% + \tfrac23 \cdot 9\% = 8\%$ [T04, p. 12].
- **Coherencia tasa-flujo**: flujos en moneda constante con tasa real, flujos en moneda corriente con tasa nominal. Mezclarlos cuenta la inflación dos veces [T04, p. 9].

---

## 5. Costos

Ver [costos](temas/costos.md).

| Concepto | Fórmula |
|---|---|
| Margen de contribución unitario | precio de venta − costo variable unitario |
| Punto de equilibrio en unidades | $Q^* = CF / MC$ [R03] |
| Punto de equilibrio en pesos | $CF / (MC/\text{precio})$ |
| Condición de equilibrio | ingreso total = costo total [T05, p. 19] |

Lectura de $Q^* = CF/MC$ para los verdadero/falso: el punto de equilibrio **sube** si suben los costos fijos o si baja el margen de contribución, y **baja** en los casos inversos. Si el costo variable unitario **baja**, el margen de contribución **sube** y el punto de equilibrio **baja**; el error contrario aparece repetido en resoluciones de alumnos [X06] [X07] [X08] (ver [dudas y conflictos](dudas-y-conflictos.md)).

**Costos no relevantes para decidir:** hundidos y prorrateados. La eliminación de un producto se decide por su margen de contribución, no por los fijos de estructura que se le asignaron [G05, p. 3].

---

## 6. Análisis financiero

Ver [análisis financiero](temas/analisis-financiero.md).

| Índice | Fórmula |
|---|---|
| Liquidez corriente | activo corriente / pasivo corriente [T02, p. 21] |
| Prueba ácida | (activo corriente − inventarios) / pasivo corriente [T02, p. 21] |
| Período promedio de cobranza | créditos por ventas × días / ventas a crédito [T02, p. 24] |
| Período promedio de pago | deudas comerciales × días / compras [T02, p. 25] |
| Rotación de inventarios | costo de ventas / inventario promedio [T02, p. 26] |
| Rotación de activos | ventas / activo [T02, p. 26] |
| **Ciclo de caja** | días de inventario + días de cobro − días de pago [T02, p. 27] |
| Endeudamiento | deuda total / activo [T02, p. 29] |
| Cobertura de intereses | resultado operativo / intereses [T02, p. 30] |
| Rentabilidad del patrimonio | resultado neto / patrimonio neto [T02, p. 34] |
| Capital de trabajo (fondo de maniobra) | activo corriente − pasivo corriente [T01, p. 35] |
| Necesidades operativas de fondos | créditos con clientes + inventarios − proveedores [R03] |

**Du Pont** [T02, p. 42]:

$$ROE = \frac{RN}{\text{Ventas}} \times \frac{\text{Ventas}}{\text{Activos}} \times \frac{\text{Activos}}{PN}$$

margen (eficiencia económica) × rotación (eficiencia operativa) × apalancamiento.

**Apalancamiento financiero** [T02, p. 43]:

$$ROE = RO + (RO - i)\,\frac{\text{Pasivo}}{PN}$$

Si la rentabilidad operativa supera el costo de la deuda, endeudarse **sube** la rentabilidad del accionista — y también su riesgo, porque amplifica las variaciones en los dos sentidos.

---

## 7. Información contable

Ver [información contable](temas/informacion-contable.md).

- **Ecuación contable:** activo = pasivo + patrimonio neto; toda operación la mantiene [T01, p. 20].
- **Devengado:** los efectos se reconocen cuando ocurren, no cuando entra o sale la plata [T01, p. 17]. De acá sale el verdadero/falso más repetido: **se puede tener utilidad positiva y caja negativa**, y viceversa.
- **Amortización:** gasto **no monetario**. No es una salida de caja ni un ahorro en efectivo; su único efecto sobre el flujo es bajar el impuesto [T04, p. 20].
- **Resultado por venta de un bien de uso:** precio de venta − valor de libros [R01].
- Cascada del estado de resultados: resultado antes de intereses, impuestos y amortizaciones → antes de intereses e impuestos → antes de impuestos → después de impuestos [T01, p. 33].

---

## Fuentes

T01, T02, T03, T04, T05, G01, G04, G05, R01, R02, R03, P02; no oficiales: X01, X06, X07, X08.
