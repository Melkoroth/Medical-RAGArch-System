import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import pandas as pd

def generate_sample_visualizations():
    # Datos de ejemplo
    data = pd.DataFrame({
        'x': range(10),
        'y': [value ** 2 for value in range(10)]
    })

    # Gráfico con Matplotlib
    plt.figure(figsize=(6, 4))
    plt.plot(data['x'], data['y'], marker='o', linestyle='-')
    plt.title('Ejemplo de Gráfico con Matplotlib')
    plt.savefig("matplotlib_example.png")

    # Gráfico con Seaborn
    sns.set(style="darkgrid")
    sns.lineplot(x="x", y="y", data=data).set_title("Ejemplo con Seaborn")
    plt.savefig("seaborn_example.png")

    # Gráfico con Altair
    chart = alt.Chart(data).mark_line().encode(x='x', y='y').properties(title="Ejemplo con Altair")
    chart.save("altair_example.json")

generate_sample_visualizations()
