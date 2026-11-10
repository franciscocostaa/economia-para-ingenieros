# Segundo parcial

## Fuentes y autoridad

| Parcial | Enunciado | Resolución | Autoridad | Práctica |
|---|---|---|---|---|
| 2C2010 | imagen en [X02] | alumno [X02] | no oficial | [2010-C2](../../practica/segundo-parcial/2010-C2.md) |
| 1C2018 | imagen en [X03] | alumno [X03] | no oficial | [2018-C1](../../practica/segundo-parcial/2018-C1.md) |
| 2C2018 | imagen en [X04] | alumno [X04] | no oficial | [2018-C2](../../practica/segundo-parcial/2018-C2.md) |
| 1C2023 | imagen en [X05] | alumno [X05] | no oficial | [2023-C1](../../practica/segundo-parcial/2023-C1.md) |
| 2C2024 | imagen en [X06] | alumno [X06] | no oficial | [2024-C2](../../practica/segundo-parcial/2024-C2.md) |
| 1C2025 | imagen en [X07] | alumno [X07] | no oficial | [2025-C1](../../practica/segundo-parcial/2025-C1.md) |
| 11/11/2025 (2C2025) | [P01] | [R02] | cátedra | [2025-C2](../../practica/segundo-parcial/2025-C2.md) |
| 16/06/2026 (1C2026) | [P02, p. 1] | [R03] | cátedra | [2026-C1](../../practica/segundo-parcial/2026-C1.md) |

El compilado de verdadero/falso [X08] y los V/F oficiales de 2026 están revisados en el [banco de V/F](../../practica/segundo-parcial/banco-vf.md).

Las resoluciones oficiales mezclan temas: [R02] resuelve el problema 1 con los datos del tema 1 y el problema 2 con los del tema 2 de [P01]; [R03] hace lo mismo con [P02, p. 1] y [P02, p. 2]. Los temas faltantes están calculados en las páginas de práctica y marcados como inferencia. Con los datos del tema 1, el proyecto SolArGen de 2025 da VAN negativo, al revés que el tema 2 resuelto en [R02].

## Formato

- Sin calculadora; las dudas se resuelven con un supuesto justificado por escrito [P02, p. 1]. **Esto cambió para el parcial del 17/11/2026**: ver más abajo.
- Estructura casi fija: un ejercicio de V/F con justificación obligatoria (8 a 10 incisos), un problema de valor tiempo del dinero y un problema de evaluación de proyectos [P02, p. 1] [X05] [X07]. El parcial del 11/11/2025 no tuvo V/F [P01].
- Un V/F sin justificación se invalida [P02, p. 1].

## Modalidad del parcial del 17/11/2026

Anuncio de la cátedra en el campus ("Modalidad 2do. parcial 17-11-26"). **No hay un archivo de esta fuente en el repositorio**: el texto se transcribió de una captura de pantalla, así que no lleva ID de catálogo.

- El parcial **se resuelve en Excel**, en el archivo `EPI 2° Parcial 17-11-2026 cmd - Legajo 00000.xlsm` que se descarga de la Actividad habilitada. Hay que renombrarlo reemplazando `00000` por los cinco dígitos del legajo.
- **El archivo no abre con la computadora conectada a internet.** Hay que desconectarse antes de abrirlo y reconectarse recién al final para subirlo a la Actividad.
- Estructura: **dos ejercicios y un punto de verdadero/falso**. Cada ítem va en la hoja cuya solapa lleva su número; en las celdas **B1 y B2** de cada hoja van apellido, nombre y legajo.
- Los **enunciados se entregan impresos en papel** al comenzar.
- Único material de ayuda permitido: **una hoja de fórmulas** (ver [hoja de fórmulas](../hoja-de-formulas.md)). Prohibido cualquier otro apunte o ejercicio resuelto.
- Conviene grabar el archivo periódicamente durante la resolución.

**Inferencia:** al desaparecer la restricción de resolver sin calculadora, los datos pueden dejar de ser redondos y conviene desplegar los cuadros completos (marcha de un préstamo, flujo de fondos año por año) en lugar de buscar atajos de cálculo mental.

### Cómo escribe las planillas la cátedra

Relevado sobre las fórmulas de las dos resoluciones oficiales en planilla, [R02] y [R03]. Las únicas funciones de Excel que aparecen en todo el material son `SUM`, `IRR`, `POWER`, `IF` y `ROUND`: **el resto se escribe a mano con el operador `^`**.

| Cálculo | Fórmula tal como aparece en la planilla oficial |
|---|---|
| Tasa efectiva del período desde la TNA | `=B7/4` [R03] |
| Cambio de plazo de una tasa efectiva | `=(1+B17)^(1/3)-1` [R03] |
| TEA desde la tasa del período | `=(1+B17)^4-1` [R03] |
| Saldo de un préstamo alemán tras *k* cuotas | `=B6*(1-11/B9)` [R03] |
| Cuota del sistema francés | `=F16*B14/(1-(1+B14)^-B13)` [R03] |
| Factor de actualización de una anualidad | `=(POWER(1+D13,D8)-1)/(POWER(1+D13,D8)*D13)` [R02] |
| Factor de descuento del período *t* | `=1/(1+$B$19)^B27` [R03] |
| VAN | `=SUM(B44:G44)` sobre la fila de flujos ya descontados [R03] |
| TIR | `=IRR(B42:G42)` [R03] |
| Valor residual neto de impuestos | `=B15-B18*(B15-(B12-5*B14))` [R03] |
| Veredicto de la recomendación | `=IF(B22>0,"Se recomienda la inversión","No se recomienda la inversión")` [R02] |

Consecuencias prácticas:

- **No alcanza con saber manejar Excel: hay que saber las fórmulas.** Las funciones financieras `PAGO`/`PMT`, `VNA`/`NPV`, `VA`, `NPER` y `TASA`/`RATE` no se usan en ninguna resolución oficial.
- **El VAN se calcula en dos filas** (factores de descuento y después `SUM`), no con `VNA`. **Inferencia:** además de ser el estilo de la cátedra, evita el error de `VNA`, que supone el primer flujo en *t* = 1 y por lo tanto descuenta de más la inversión inicial si se la incluye en el rango.
- La cátedra arma un **bloque de parámetros** en las primeras filas y después referencia esas celdas con direcciones absolutas (`$B$9`), en vez de repetir los números dentro de las fórmulas [R03].
- El único cálculo iterativo que delega en una función es la TIR.

## Qué se evalúa

### Verdadero/falso

Mezclan [información contable](informacion-contable.md), [análisis financiero](analisis-financiero.md), [costos](costos.md) y flujo de fondos. Los enunciados se reciclan entre cuatrimestres [X08]. Los que más se repiten:

- Devengado vs. percibido: utilidad positiva con caja negativa; ventas no cobradas como ingreso [R03] [T01, p. 17].
- La amortización es un gasto no monetario y genera escudo fiscal [R03].
- Punto de equilibrio $Q^* = CF/MC$ ante cambios de precio, costo variable o costo fijo [R03] [T05, p. 19].
- Ciclo de caja, rotaciones y plazos de cobro y pago [T02, p. 27].
- Efecto de comprar bienes de uso (contado, a plazo, con aporte) sobre el activo total y la liquidez [T02, p. 21].
- Fondo de maniobra vs. NOF; capital de trabajo operativo negativo en empresas sanas [R03] [T01, p. 35].
- DuPont y apalancamiento financiero: el ROE puede subir aunque baje la rentabilidad operativa si RO > i [R03] [T02, p. 43].
- Costos hundidos, de oportunidad y prorrateados [T04, p. 20] [G05, p. 3].

### Problema de valor tiempo del dinero

Siempre gira alrededor de préstamos o financiaciones ([página](valor-tiempo-del-dinero.md)):

1. Convertir TNA a la tasa efectiva del período (TEM, TET, TEA) según la capitalización [R02] [R03].
2. Armar el cuadro del sistema pedido (alemán, francés, americano/bullet) o el saldo a una fecha [R03].
3. Comparar alternativas por TEA o por VP al costo de oportunidad [R03] [G05, p. 2].
4. Variantes frecuentes: refinanciación del saldo en francés [R03] [X07], contado vs. financiado [X06], comprar vs. alquilar con tipo de cambio de indiferencia [R02].

### Problema de evaluación de proyectos

Siempre es un VAN con flujo incremental ([página](evaluacion-de-proyectos.md)):

1. Excluir el estudio o consultora ya pagado (costo hundido): aparece en los cinco parciales recientes [R02] [R03] [X05] [X06] [X07].
2. Incluir costos de oportunidad y canibalización; excluir costos prorrateados [X04] [X06] [G05, p. 3].
3. Cuadro de resultados → impuesto → flujo: amortización como escudo fiscal, venta del activo al final gravada sobre el valor de libros, capital de trabajo y su recupero [R02] [R03].
4. Pregunta de sensibilidad o de cambio de supuesto (plazo de amortización, alquiler máximo) [R02] [X07].

## Advertencias

- Las resoluciones de alumnos tienen cálculos correctos pero varias justificaciones de V/F equivocadas, y los errores se copian de un año a otro (por ejemplo, el signo invertido entre costo variable y margen de contribución en [X06], [X07] y [X08]). El detalle está en [dudas y conflictos](../dudas-y-conflictos.md).
- Dos resoluciones no oficiales deducen del impuesto el capital de trabajo no recuperado; el material oficial no trata ese caso [X05] [X07].
- "Interés a fin de diciembre" en [P02, p. 1] admite dos lecturas; [R03] toma el de la cuota de diciembre. Ante ambigüedad, explicitar el supuesto, como pide el propio parcial.

## Fuentes

P01, P02, R02, R03, T01, T02, T04, T05, G05; no oficiales: X02–X08.
