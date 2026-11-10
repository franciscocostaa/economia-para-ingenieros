# La empresa y los costos

## Alcance de las fuentes

- La única teoría oficial de costos es T05: 23 diapositivas de 2009, en su mayoría esquemas y tablas sin desarrollo escrito [T05, p. 1]. Se revisaron visualmente todas las páginas.
- La página 20 de T05 es solo un gráfico (el texto extraído aparece vacío): es el gráfico de **punto de pseudo-equilibrio** de un producto $i$ [T05, p. 20]. No tiene título ni explicación.
- T05 no escribe fórmulas de margen de contribución ni de punto de equilibrio en unidades; solo plantea $IT = CT$ [T05, p. 19]. La fórmula $Q^* = CF/MC$ aparece en la resolución oficial del parcial del 16/06/2026 [R03] (hoja P1).
- La interpretación de las zonas del pseudo-equilibrio y del sistema ABC que se toma en los parciales viene de resoluciones **no oficiales** de alumnos [X02] (hoja Ejercicio 1) y del compilado de verdadero/falso [X08]. Se señalan como tales en cada caso.

## Contabilidad de presentación y contabilidad de gestión

| Enfoque | Qué entiende por costo |
|---|---|
| Contabilidad de presentación | Una medida de los recursos usados o sacrificados para un determinado propósito [T05, p. 2] |
| Contabilidad de gestión | Costos del producto: los que la empresa asigna a los productos fabricados [T05, p. 2] |

T01 hace la misma distinción como contabilidad financiera (custodia, medición del resultado, mirada hacia atrás) frente a contabilidad gerencial (planificación, presupuestos, costos, mirada hacia adelante) [T01, p. 12]. Ver [informacion-contable.md](informacion-contable.md).

## Costos de fabricación

Los costos de fabricación tienen tres componentes que se cargan al producto [T05, p. 3]:

- **Materia prima o materiales directos (MP, MD)**: se convierten en parte integral del producto y se pueden rastrear en él con facilidad. Ejemplo: la radio instalada en un auto [T05, p. 4].
- **Mano de obra directa (MOD)**: costos de mano de obra que se rastrean con facilidad en el producto. Ejemplo: salarios de los obreros de la línea de montaje [T05, p. 5].
- **Gastos generales de fabricación (GGF)**: costos de fabricación que no se pueden rastrear directamente a las unidades producidas. Incluyen la mano de obra indirecta (mantenimiento, porteros, vigiladores) y los materiales indirectos (lubricantes, elementos de limpieza de la planta) [T05, p. 6].

Los **costos no relacionados con la fabricación** son los gastos de comercialización y ventas (obtener el pedido y despachar el producto) y los gastos administrativos (gerenciales, organizacionales, empleados) [T05, p. 7].

## Costos del producto y costos del período

- **Costos del producto**: MD, MOD y GGF. Quedan en **inventarios** (hoja de balance) y, cuando se vende, pasan al **costo de la mercadería vendida** del cuadro de resultados [T05, p. 8].
- **Costos del período**: no se incluyen en el costo del producto. Van directo al cuadro de resultados como gastos [T05, p. 8].

Flujo del costo [T05, p. 9]:

1. Las compras entran al inventario de MP.
2. La MP pasa a productos en proceso (PP), donde se suman la MOD y los GGF.
3. PP pasa a productos terminados (PT).
4. Al vender, PT pasa al costo de la mercadería vendida del cuadro de resultados.
5. Los gastos de administración y ventas son costos del período y van a GAV en el cuadro de resultados.

T01 describe las cuentas transitorias de producción que acumulan esos costos mientras avanza la transformación [T01, p. 52]. Esto es coherente con el principio de lo devengado: los costos vinculados a ingresos se imputan al período de esos ingresos y los vinculados a períodos, al período correspondiente [T01, p. 17].

## Clasificaciones de costos

### Fijos y variables

Dentro de un **rango relevante** de actividad [T05, p. 10]:

| Costo | Total | Unitario |
|---|---|---|
| Variable | CVT cambia cuando cambia el nivel de actividad | CVU permanece igual en grandes rangos de actividad |
| Fijo | CFT permanece igual cuando cambia el nivel de actividad | CFU disminuye a medida que el nivel aumenta |

La diapositiva marca con un globo la pregunta "¿Rango relevante?" [T05, p. 10]. **Inferencia:** fuera de ese rango un costo fijo puede saltar de escalón (por ejemplo, alquilar más superficie). La resolución no oficial de un verdadero/falso sobre el alquiler del galpón lo considera fijo aunque suba por escalones [X08] (ítem 34).

### Directos e indirectos

- **Directos**: se rastrean fácil y sencillamente a una unidad de producto u otro objeto de costo. Ejemplos: MD y MOD [T05, p. 12].
- **Indirectos**: no se pueden rastrear con facilidad hasta una unidad de producto. Ejemplo: GGF [T05, p. 12].

### Propios y comunes (asignados o prorrateados)

T05 no los define con palabras, pero los usa en el gráfico de pseudo-equilibrio: $F_{i\ propios}$ y $F_{i\ asignados}$ [T05, p. 20].

- **Fijos propios** del producto: desaparecen si se deja de hacer el producto.
- **Fijos asignados (prorrateados, comunes, de estructura)**: son costos de la empresa, en general de estructura o de administración, que se reparten entre productos con algún coeficiente. Si el producto o proyecto no se hace, no desaparecen; solo se reasignan a otros productos. Por eso no se consideran en las decisiones [G05, p. 3].
- La guía de práctica separa los "fijos erogables propios" de los "fijos erogables prorrateados" en el ejercicio 4 de evaluación de proyectos [G01, p. 7]. El resultado oficial excluye los prorrateados del flujo (ver el ejemplo numérico más abajo) [G04, p. 1].

### Otras clasificaciones enumeradas en T05

T05 solo enumera estas categorías, sin definirlas [T05, p. 11]: recurrentes y no recurrentes; directo e indirecto; estándar; contable y efectivo; hundido; de oportunidad; gastos frente a inversión. Las definiciones que siguen se completan con otras fuentes:

- **Costo estándar**: técnica de control de costos y presupuestario. Anticipa cuánto deberían valer los factores de fabricación de un producto a partir de estudios técnico-económicos [T05, p. 16].
- **Costo contable y costo efectivo (erogable)**: los costos erogables implican una salida de efectivo; la depreciación es un consumo contable de bienes de uso [T01, p. 33]. Por eso no todos los costos de fabricación generan flujo de efectivo; la amortización fabril no lo hace (no oficial) [X08] (ítem 42).
- **Costo hundido**: ya fue incurrido y no cambia con la decisión, así que no entra en el flujo de caja [T04, p. 20]. Ejemplo oficial: el estudio de reingeniería ya pagado no modifica el flujo ni el VAN [G04, p. 2].
- **Costo de oportunidad**: lo que se obtendría usando el recurso en otra alternativa. Ejemplo: un terreno propio ocioso, que podría alquilarse o venderse [T04, p. 20]. Un verdadero/falso clásico intercambia ambas definiciones: dice que el costo hundido es "el máximo ingreso que un bien podría producir si se aplicara a otro fin". Es falso, porque esa es la definición del costo de oportunidad (no oficial) [X08] (ítem 31).
- **Conocimiento general (no está en el material):** los costos recurrentes se repiten en cada período (insumos, sueldos) y los no recurrentes ocurren una sola vez (puesta en marcha). Un gasto se imputa al resultado del período; una inversión se activa y se consume en varios períodos.

## Sistemas de costeo

T05 menciona tres sistemas: directo, por absorción y por actividades [T05, p. 11].

| Componente del costo total | Costeo por absorción | Costeo directo |
|---|---|---|
| Materia prima | sí | sí |
| Mano de obra directa | sí | sí |
| GGF variables | sí | sí |
| GGF fijos | sí | no |
| Gastos de administración, comercialización y finanzas | no | no |

Fuente de la tabla: [T05, p. 14] y [T05, p. 15].

- El **costeo por absorción** carga al producto todos los costos de fabricación, fijos y variables [T05, p. 14].
- El **costeo directo** (variable) carga solo los costos de fabricación variables [T05, p. 15].
- **Inferencia:** en costeo directo los GGF fijos se tratan como costo del período. Por eso este sistema es el que se alinea con el margen de contribución.
- **Conocimiento general (no está en el material):** cuando la producción difiere de las ventas, absorción y directo dan resultados distintos, porque en absorción parte de los GGF fijos queda en el inventario.

Atención: "costo directo" (rastreable al producto, [T05, p. 12]) no es lo mismo que "costeo directo" (sistema que solo incluye costos variables de fabricación, [T05, p. 15]). Los GGF variables son indirectos y, aun así, entran en el costeo directo.

### Costeo basado en actividades (ABC)

- El esquema es costos → consumo de recursos → actividades → objetos de costo (productos, clientes). Se usan **varias bases de distribución** para asignar gastos a productos [T05, p. 17].
- Es un modelo gerencial, no contable. Los recursos los consumen las actividades y a las actividades las consumen los objetos de costo. Considera todos los costos y gastos como recursos y muestra la empresa como un conjunto de actividades o procesos, no como una jerarquía departamental. Asigna costos a productos o servicios según el consumo de actividades [T05, p. 18].
- **En los parciales:** el 2C2010 preguntó si "el ABC adjudica los costos indirectos de fabricación con respecto a una base de volumen o de actividad (horas-hombre, horas-máquina, dólares-material)" [X02] (hoja Ejercicio 1, ítem f). La resolución no oficial responde "Verdadero" y justifica con la cadena recursos → actividades → productos [X02]. La respuesta es discutible (ver la sección de errores frecuentes).

## Margen de contribución y punto de equilibrio

### Definiciones y fórmulas

El punto de equilibrio se da cuando $IT = CT$: es el volumen $q^*$ con beneficio nulo. El gráfico muestra una recta de ingresos que nace en el origen, una de costos fijos horizontal y la de costo total, que parte de CF y crece con el volumen [T05, p. 19].

Con precio $p$, costo variable unitario $cv$ y costos fijos $CF$, todo constante:

- Ingreso total: $IT = p\,q$.
- Costo total: $CT = CF + cv\,q$.
- **Margen de contribución unitario**: $mc = p - cv$ [R03] (hoja P1).
- Margen de contribución total: $MC = (p - cv)\,q$. Beneficio: $B = (p - cv)\,q - CF$.
- **Equilibrio en unidades**: $q^* = \dfrac{CF}{p - cv}$ [R03] (hoja P1).
- **Equilibrio en pesos**: $V^* = p\,q^* = \dfrac{CF}{1 - cv/p}$. Al cociente $(p - cv)/p$ se lo llama razón de contribución. **Conocimiento general (no está en el material).**

Condiciones de uso (**Inferencia** a partir del rango relevante de [T05, p. 10]): las relaciones deben ser lineales (precio y $cv$ constantes dentro del rango relevante); tiene que cumplirse $p > cv$; se analiza un solo producto o una mezcla fija; y lo producido es lo vendido.

### Punto de pseudo-equilibrio

El gráfico de [T05, p. 20] se refiere a un producto $i$ dentro de una empresa con varios productos:

- Recta de ventas: $V = p\,Q$.
- Recta de costo "propio": $F_{i\ propios} + w_i Q_i$, donde $w_i$ es el costo variable unitario del producto.
- Recta de costo "completo": parte de $F_{i\ propios} + F_{i\ asignados}$ y tiene la misma pendiente $w_i$.
- $Q_{i\ pseudoeq}$ es el corte de las ventas con la recta propia; $Q_{i\ eq}$, el corte con la recta completa. El eje queda dividido en tres zonas: "A", "B" y "C".

La recta superior está rotulada en la diapositiva como "$F_{i\ propios} + w_i Q_i$", igual que la inferior, aunque arranca en $F_{i\ propios} + F_{i\ asignados}$. **Inferencia:** el rótulo correcto es $F_{i\ propios} + F_{i\ asignados} + w_i Q_i$.

Fórmulas (**Inferencia**: se obtienen igualando las rectas del gráfico):

$$Q_{i\ pseudoeq} = \frac{F_{i\ propios}}{p - w_i} \qquad Q_{i\ eq} = \frac{F_{i\ propios} + F_{i\ asignados}}{p - w_i}$$

Lectura de las zonas:

| Zona | Volumen | Qué cubre el producto | Implicancia para decidir |
|---|---|---|---|
| A | $Q < Q_{pseudoeq}$ | No cubre sus costos variables más sus fijos propios | Eliminarlo mejora el resultado de la empresa, porque desaparecen sus costos propios y los asignados siguen igual (**Inferencia**, coherente con [G05, p. 3]) |
| B | $Q_{pseudoeq} < Q < Q_{eq}$ | Cubre variables y fijos propios y aporta algo a los fijos comunes, aunque no llegue a cubrir lo que se le asigna | Conviene mantenerlo: eliminarlo haría perder esa contribución (no oficial, [X02] ítem g; [X08] ítem 44) |
| C | $Q > Q_{eq}$ | Cubre también los fijos asignados | Situación deseable a largo plazo (no oficial, [X02]) |

La resolución no oficial agrega: "debajo de él no se debe producir, y a largo plazo se quiere estar por encima del equilibrio" [X02] (hoja Ejercicio 1). **Inferencia:** la decisión de eliminar un producto se toma contra el pseudo-equilibrio, no contra el equilibrio. Los fijos prorrateados son comunes y no cambian al eliminar el producto, así que no cuentan para la decisión. Así lo resuelven, sin fuente oficial, varios parciales [X03] [X04] [X05], y lo respalda la explicación oficial sobre costos prorrateados [G05, p. 3].

### Ejemplo numérico

**Inferencia:** ejemplo construido con los datos del ejercicio 4 de proyectos [G01, p. 7]. La guía no pide el equilibrio.

- Datos: $p = 20$ $/u; $cv = 8$ $/u; fijos erogables propios = 60.000 $/año; fijos erogables prorrateados = 5.000 $/año; máquina de 200.000 $ amortizada en 4 años con valor residual de 20.000 $, es decir 45.000 $/año [G01, p. 7].
- Margen de contribución: $mc = 12$ $/u; razón de contribución = 12/20 = 0,6.
- Fijos propios de los años 1 a 4 (erogables + amortización): 60.000 + 45.000 = 105.000 $. Pseudo-equilibrio: $105.000/12 = 8.750$ u, equivalentes a $105.000/0{,}6 = 175.000$ $.
- Sumando los prorrateados: $110.000/12 \approx 9.167$ u, equivalentes a 183.333 $.
- Con un volumen previsto de 35.000 u/año [G01, p. 7], el producto está en la zona C.
- El resultado oficial del flujo para los años 1 a 4, 265.500 $ [G04, p. 1], se reproduce solo **sin** los 5.000 $ prorrateados: $(35.000 \times 12 - 60.000) - 0{,}30 \times (360.000 - 45.000) = 265.500$. **Inferencia** verificada con esos datos.

## Análisis de sensibilidad del equilibrio

**Inferencia** a partir de $q^* = CF/(p - cv)$, salvo donde se cita otra cosa:

| Cambio (lo demás constante) | Efecto en $mc$ | Efecto en $q^*$ | Fuente |
|---|---|---|---|
| Sube $p$ | sube | baja | |
| Baja $p$ | baja | sube (si $p \le cv$, no hay equilibrio) | |
| Sube $cv$ | baja | sube | |
| Baja $cv$ | sube | baja | Ver el error de [X08] (ítem 3) |
| Sube $CF$ | igual | sube en la misma proporción | |
| Baja $CF$ | igual | baja | (no oficial) [X08] (ítem 7) |
| Sube $cv$, $p$ sube lo mismo ($mc$ constante) y sube $CF$ | igual | sube | [P02, p. 1], [R03] |

- Un cambio en $p$ o en $cv$ de la misma magnitud mueve $q^*$ igual, porque solo importa la diferencia $p - cv$.
- **Inferencia:** en pesos no pasa lo mismo, porque $V^* = CF/(1 - cv/p)$. Si $p$ sube y $mc$ se mantiene constante, $q^*$ no cambia pero $V^*$ sube.
- **Inferencia:** un cambio en los fijos asignados mueve $Q_{eq}$ pero no $Q_{pseudoeq}$, así que no altera la decisión de mantener o eliminar el producto.
- Con el ejemplo anterior (equilibrio total de 9.167 u, **Inferencia**):
  - Con $p = 22$: $mc = 14$ y $q^* = 110.000/14 \approx 7.857$ u.
  - Con $cv = 10$: $mc = 10$ y $q^* = 11.000$ u.
  - Con fijos propios un 10 % más altos (115.500 $): $q^* = 120.500/12 \approx 10.042$ u.

## Costo del ciclo de vida y optimización del diseño

- **Ciclo de vida:** el costo de un cambio de diseño sube en escalones a medida que el cambio llega más tarde. Las etapas son evaluación de necesidades, diseño conceptual, diseño detallado, producción o construcción y operación [T05, p. 21].
- **Optimización del diseño:** se identifica la variable de diseño que más pesa en el costo, se expresa el costo como $C = aX + b/X + k$, se deriva, se iguala a cero y se verifica con la segunda derivada que el punto sea un mínimo [T05, p. 22]. **Inferencia:** para esa forma, $X^* = \sqrt{b/a}$ y $C'' = 2b/X^3 > 0$.
- **Ejemplo del avión:** $CT = 0{,}04\,n\,v^{3/2} + 300.000\,n/v$ [T05, p. 23]. La diapositiva da $v = 490{,}68$ mph [T05, p. 23], pero el cálculo correcto es otro:
  - Primera derivada: $0{,}06\,n\,v^{1/2} = 300.000\,n/v^2$, de donde $v^{5/2} = 5 \times 10^6$ y $v^* \approx 478{,}2$ mph.
  - Segunda derivada: $0{,}03\,n\,v^{-1/2} + 600.000\,n\,v^{-3}$, positiva para todo $v > 0$.
  - Ver la nota en errores frecuentes.

## Procedimiento típico en parciales

En los segundos parciales los costos aparecen como verdaderos/falsos con justificación obligatoria [P02, p. 1] [X02].

1. Identificar la variable que se mueve ($p$, $cv$, $CF$, fijos asignados) y qué se mantiene constante.
2. Escribir $mc = p - cv$ y $q^* = CF/mc$, y ver hacia dónde va cada término [R03].
3. En preguntas de eliminar o mantener un producto, separar los fijos propios de los asignados y comparar contra el pseudo-equilibrio [T05, p. 20] [G05, p. 3].
4. En preguntas de flujo de caja, separar lo erogable de lo no erogable (amortizaciones) y descartar costos hundidos y prorrateados [G04, p. 2] [G05, p. 3].
5. Desconfiar de "siempre" y "todos": suelen hacer falso el enunciado [R03] (hoja P1, ítem c).

## Errores frecuentes y advertencias

- **Justificación incorrecta en el compilado no oficial:** ante "una reducción en los costos variables por unidad disminuye el margen de contribución y aumenta el punto de equilibrio", la respuesta "Falso" es correcta. Pero la justificación dice que "un aumento en los costos variables implica un aumento en el margen de contribución", y eso está mal [X08] (ítem 3). Lo correcto: como $mc = p - cv$, una **reducción** de $cv$ **aumenta** el $mc$ y **reduce** $q^* = CF/mc$. La misma justificación errónea está copiada en [X06] (ítem n) y [X07] (ítem c).
- **ABC y bases de volumen:** asignar los costos indirectos con una única base de volumen (horas-hombre, horas-máquina, pesos de material) es lo típico del costeo tradicional. El ABC usa varias bases, cada una ligada al consumo de actividades [T05, p. 17] [T05, p. 18]. La respuesta "Verdadero" de [X02] (ítem f) se apoya en la mención "o de actividad", pero su justificación no explica las bases de volumen. **Inferencia:** en un examen conviene justificar distinguiendo ambas cosas.
- **No confundir costo hundido con costo de oportunidad** [T04, p. 20] [X08] (ítem 31).
- **No incluir los fijos prorrateados** en decisiones de eliminar productos ni en flujos de proyectos [G05, p. 3] [G04, p. 1].
- **Costo directo no es lo mismo que costeo directo** (ver Sistemas de costeo).
- **Errores en la diapositiva del avión:** el óptimo es $v^* \approx 478{,}2$ mph, no 490,68 mph. La segunda derivada correcta es $0{,}03\,n/v^{1/2} + 600.000\,n/v^3$, no $0{,}028/v^{1/2} - 300.000/v^3$ [T05, p. 23]. Con la expresión de la diapositiva, evaluada en 490,68, se obtiene un valor negativo (cerca de −0,0013), que contradice la conclusión de la propia diapositiva. Aun así, la conclusión de que es un mínimo es correcta.
- **Rango relevante:** las clasificaciones fijo/variable valen solo dentro del rango relevante [T05, p. 10].

## Relación con otros temas

- [informacion-contable.md](informacion-contable.md): costos del producto en inventarios y CMV, devengado, cuentas de producción [T01, p. 17] [T01, p. 52].
- [analisis-financiero.md](analisis-financiero.md): **Inferencia:** el margen sobre ventas de la rentabilidad operativa (ROA = margen × rotación, no oficial [X08], ítem 30) depende de la estructura de costos fijos y variables.
- [evaluacion-de-proyectos.md](evaluacion-de-proyectos.md): costos relevantes (incrementales), hundidos, de oportunidad y prorrateados en el flujo de fondos [T04, p. 20] [G05, p. 3].
- [valor-tiempo-del-dinero.md](valor-tiempo-del-dinero.md): el costo de oportunidad del capital como tasa de descuento [T04, p. 43].
- [segundo-parcial.md](segundo-parcial.md): verdaderos/falsos de costos y equilibrio [P02, p. 1] [X08].

## Fuentes

- Oficiales: T05 (fuente principal), T01, T04, G01, G04, G05, P02, R03.
- No oficiales: X02, X03, X04, X05, X06, X07, X08.
