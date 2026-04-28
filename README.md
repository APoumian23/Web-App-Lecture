# Análisis de Anuncios de Venta de Coches

## Descripción del proyecto

Esta aplicación web permite explorar de forma interactiva un conjunto de datos de anuncios de venta de coches usados en Estados Unidos. El dataset contiene información sobre más de 51,000 vehículos, incluyendo precio, kilometraje, modelo, condición, tipo de combustible y más.

## Funcionalidades de la aplicación

- **Histograma**: Visualiza la distribución del kilometraje (odómetro) de los vehículos anunciados.
- **Gráfico de dispersión**: Explora la relación entre el kilometraje y el precio de los vehículos.
- **Controles interactivos**: Casillas de verificación para seleccionar qué gráficos mostrar.

## Conjunto de datos

El archivo `vehicles_us.csv` contiene las siguientes columnas principales:
- `price`: Precio del vehículo
- `model_year`: Año del modelo
- `model`: Modelo del vehículo
- `condition`: Condición del vehículo
- `odometer`: Kilometraje
- `type`: Tipo de vehículo
- `paint_color`: Color

## Tecnologías utilizadas

- **Python**: Lenguaje de programación principal
- **Streamlit**: Framework para la aplicación web
- **Plotly Express**: Librería para visualizaciones interactivas
- **Pandas**: Manipulación y análisis de datos

## Estructura del proyecto

```
.
├── README.md
├── app.py
├── vehicles_us.csv
├── requirements.txt
└── notebooks
    └── EDA.ipynb
```

## Cómo ejecutar localmente

1. Crea un entorno virtual:
```bash
python -m venv vehicles_env
source vehicles_env/bin/activate  # En Mac/Linux
vehicles_env\Scripts\activate     # En Windows
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Ejecuta la aplicación:
```bash
streamlit run app.py
```

## URL de la aplicación

[Acceder a la aplicación web en Render](https://<APP_NAME>.onrender.com/)
