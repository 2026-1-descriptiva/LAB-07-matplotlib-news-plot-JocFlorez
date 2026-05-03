"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

from matplotlib import colors
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt



def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    plt.Figure()

    colors = {
        'Television': 'dimgray',
        'Newspaper': 'gray',
        'Radio': 'lightgray',
        'Internet': 'tab:blue',
    }

    zorder = {
        'Television': 1,
        'Newspaper': 1,
        'Radio': 1,
        'Internet': 2
    }

    linewidths = {
        'Television': 2,
        'Newspaper': 2,
        'Radio': 2,
        'Internet': 4
    }

    df = pd.read_csv("files/input/news.csv", index_col=0)

    for col in df.columns:
        plt.plot(df[col],
             color=colors[col],
             zorder=zorder[col],
             linewidth=linewidths[col],
             label=col)

    plt.title("How people get their news", fontsize=16)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    for col in df.columns:
        first_year = df.index[0]
        plt.scatter(
            x=first_year,
            y = df[col][first_year],
            color=colors[col],
            zorder=zorder[col],
        )

        plt.text(
            x=first_year - 0.2,
            y = df[col][first_year],
            s=col +  " " + str(df[col][first_year])+ "%",
            ha='right',
            va='center',
            color=colors[col],
        )

        last_year = df.index[-1]
        plt.scatter(
            x=last_year,
            y = df[col][last_year],
            color=colors[col],
            zorder=zorder[col],
        )

        plt.text(
            x=last_year + 0.2,
            y = df[col][last_year],
            s=str(df[col][last_year])+ "%",
            ha='left',
            va='center',
            color=colors[col],
        )

    plt.xticks(
        ticks=df.index,
        labels=df.index,
        ha='center',
    )

    plt.tight_layout()

    fig_path = Path("files/plots/news.png")
    fig_path.parent.mkdir(parents=True, exist_ok=True)

    plt.savefig(fig_path, dpi=300)
    plt.show()

    return print("Pregunta 01: Respuesta correcta")



if __name__ == "__main__":
    pregunta_01()