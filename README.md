# Estimación de Tiempos de Gobierno combinando Herramientas Estadísticas y Mecánica Gravitacional Clásica a partir de Sistemas de Voto por Periodos

---

# Modelo Matemático ($D \in [7, 2579]$ días)

**Definición de constantes:**

* Mínimo absoluto ($D_{\text{min}}$): $7$ días ($1$ semana)
* Máximo absoluto ($D_{\text{máx}}$): $2579$ días ($7$ años)
* Rango Total ($R$): $2579 - 7 = 2572$ días

**Definición de variables:**

* $n$: número total de votantes
* $a_i$: límite inferior del intervalo de preferencia del votante $i$, con $a_i \in [7, 2579]$ (días)
* $b_i$: límite superior del intervalo de preferencia del votante $i$, con $b_i \in [a_i, 2579]$ (días)
* $m_i$: punto medio del intervalo de preferencia del votante $i$, definido como $m_i = \frac{a_i+b_i}{2}$

---

1. **Peso por Convicción ($w_i$):**

$$w_i = 1 - \frac{b_i - a_i}{R}$$


2. **Centro de Gravedad Inicial ($t_0$):**

$$t_0 = \frac{\sum_{i=1}^{n} w_i \cdot m_i}{\sum_{i=1}^{n} w_i} \quad \text{donde } m_i = \frac{a_i + b_i}{2}$$


3. **Ancla del Grupo Inferior ($t_{\text{low}}$):**

$$t_{\text{low}} = \frac{\sum_{m_i < t_0} w_i \cdot m_i}{\sum_{m_i < t_0} w_i}$$


4. **Índice Continuo de Dispersión ($S$):**

$$S = \frac{2·\sigma}{R} \quad \text{donde } \sigma = \sqrt{\frac{\sum_{i=1}^{n} w_i (m_i - t_0)^2}{\sum_{i=1}^{n} w_i}}$$


5. **Fuerza de Atracción Gravitacional ($W$):**

$$W = 0.6375 \cdot S^2$$


6. **tiempo Final de Mandato ($t$):**

$$t = (1 - W) \cdot t_0 + W \cdot t_{\text{low}}$$



---

# Criterios de Diseño y Justificación Normativa

El comportamiento de este sistema se debe a cinco decisiones de diseño elegidas intencionadamente para lograr el equilibrio social deseado:

**1. Dominio Temporal $[7, 2579]$ días**
Fijar un mínimo de 1 semana ($7$ días) y un máximo de $7$ años ($2579$ días) es una convención institucional que acota el mandato a un rango acotado, evitando periodos extremadamente breves o prolongados.

**2. Atenuación Lineal de la Indiferencia ($w_i$)**
Asumir que la convicción decae en proporción directa al ancho del intervalo $[a_i, b_i]$ es una simplificación intencionada para anular por completo la influencia de los votos indiferentes que abarcan el rango entero $[7, 2579]$.

**3. Respuesta Cuadrática a la Polarización ($S^2$)**
El uso del exponente $2$ sobre el índice $S$ reserva la fuerza de atracción únicamente para divisiones sociales profundas. Si la comunidad presenta desviaciones leves, la fuerza de atracción es residual; si la sociedad se divide en dos bloques, la fuerza de atracción se incrementa exponencialmente.

**4. Calibración del Factor $F = 8.5$ (Fuerza Máxima de Atracción)**

* **4.1. Techo de seguridad del sistema (75%):** El modelo establece que ninguna minoría de protesta puede absorber el $100%$ de la decisión. Se fija un límite teórico donde la fuerza de atracción solo puede arrastrar el resultado hasta un 75% ($0.75$).
* **4.2. Selección del parámetro $F = 8.5$:** El parámetro $F$ (de $0$ a $10$) actúa como un regulador comunitario. Al seleccionar $F = 8.5$, se activa el 85% ($8.5 / 10$) de la fuerza de atracción máxima permitida por el sistema:

$$W_{\text{máx}} = 0.75 \times \left(\frac{F}{10}\right)$$


* **4.3. Tracción resultante:** Multiplicando el techo de seguridad por el nivel de severidad elegido, se obtiene la fuerza de atracción final:

$$\text{Tracción Máxima } (W_{\text{máx}}) = 0.75 \times 0.85 = \mathbf{0.6375 \quad }$$ (63.75%)



**5. Reparto de Fuerzas en Máxima Polarización**
En un escenario de máxima dispersión ($S = 1$), el grupo minoritario que vota por el mandato mínimo ejerce una fuerza de atracción del 63.75% sobre el resultado final, mientras que el grupo que apoya el mandato largo conserva un 36.25% (100% - 63.75%) de resistencia. Esto estabiliza el resultado extremo en $1$ año y $3$ meses ($473$ días) en lugar de colapsar la presidencia al límite inferior de $7$ días.
