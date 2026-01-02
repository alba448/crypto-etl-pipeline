## 🚀 Crypto ETL Pipeline

Este proyecto replica un flujo de datos profesional similar a los arquitectados en entornos de **Cloud Native**.

### Características principales:

* **Extracción:** Consumo de la API de **CoinGecko** para obtener datos financieros.
* **Transformación:** Uso de **Pandas** para la limpieza de tipos, manejo de nulos y generación de métricas de volatilidad.
* **Carga:** Almacenamiento optimizado en **AWS S3** en formato **Parquet** (columnar) para mejorar la eficiencia de futuras consultas (como AWS Athena o Apache Spark).
* **Infraestructura:** Preparado para ejecución local consistente mediante **Docker** y **LocalStack** para la emulación de servicios Cloud.

### Conceptos de Ingeniería de Datos aplicados:

* [cite_start]**Estándares de calidad de datos:** Implementación de validaciones y métricas de integridad similares a los estándares **Datum** utilizados en entornos bancarios[cite: 3].
* **Seguridad:** Gestión profesional de credenciales mediante el manejo de variables de entorno.
* **Calidad de Software:** Estructura de código modularizada siguiendo principios de **Clean Code** para facilitar el mantenimiento y la escalabilidad.