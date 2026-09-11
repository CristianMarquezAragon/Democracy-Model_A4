**Modelo Matemático Definitivo ($D \in [7, 2579]$ días)**

1. **Peso por Convicción ($w_i$):**

$$w_i = 1 - \frac{b_i - a_i}{2572}$$


2. **Centro de Gravedad Inicial ($T_0$):**

$$T_0 = \frac{\sum_{i=1}^{n} w_i \cdot m_i}{\sum_{i=1}^{n} w_i} \quad \text{donde } m_i = \frac{a_i + b_i}{2}$$


3. **Ancla del Grupo Inferior ($T_{\text{low}}$):**

$$T_{\text{low}} = \frac{\sum_{m_i < T_0} w_i \cdot m_i}{\sum_{m_i < T_0} w_i}$$


4. **Índice Continuo de Dispersión ($S$):**

$$S = \frac{\sigma}{1286} \quad \text{donde } \sigma = \sqrt{\frac{\sum_{i=1}^{n} w_i \cdot (m_i - T_0)^2}{\sum_{i=1}^{n} w_i}}$$


5. **Fuerza de Atracción Gravitacional ($W$):**

$$W = 0.6375 \cdot S^2$$


6. **Tiempo Final de Mandato ($T$):**

$$T = (1 - W) \cdot T_0 + W \cdot T_{\text{low}}$$



---

**Desglose de Factores Arbitrarios y Criterios de Diseño**

El comportamiento exacto de este sistema se debe a **cinco decisiones normativas de diseño**, elegidas intencionadamente para lograr el equilibrio social deseado:

* **Dominio temporal $[7, 2579]$ días:** Fijar un mínimo de 1 semana (7 días) y un máximo de 7 años (2579 días) es una convención estética e institucional. No responde a una ley natural, sino al deseo de acotar el mandato a un rango elegante y comprensible.
* **Calibración del Factor $F = 8.5$:** Se eligió arbitrariamente para fijar la severidad de la comunidad. Ajusta la tracción de castigo máxima a un $63.75\%$ exactamente.
* **Techo de Contención ($0.75 \times 0.85 = 0.6375$):** Es el "freno de mano" del sistema. Se diseñó para que, incluso en el peor escenario de fractura social, el bloque que desea mandatos largos mantenga un $36.25\%$ de resistencia. Esto es lo que estabiliza el resultado en 1 año y 3 meses (473 días) en lugar de permitir que colapse a 7 días.
* **Respuesta Cuadrática ($S^2$):** El uso del exponente 2 sobre la dispersión es un sesgo de diseño deliberado. Hace que las desviaciones leves en las votaciones apenas generen castigo, reservando la gravedad del sistema únicamente para divisiones sociales profundas.
* **Atenuación Lineal de la Indiferencia ($w_i$):** Asumir que la convicción decae en proporción directa al ancho del intervalo $[a_i, b_i]$ es una simplificación matemática para anular por completo los votos indiferentes de rango entero $[7, 2579]$.
