import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


def distribucion_categoricas(df, columnas_categoricas, relativa=False, mostrar_valores=False):
    num_columnas = len(columnas_categoricas)
    num_filas = (num_columnas // 2) + (num_columnas % 2)

    fig, axes = plt.subplots(num_filas, 2, figsize=(12, 4 * num_filas))
    axes = axes.flatten() 

    for i, col in enumerate(columnas_categoricas):
        ax = axes[i]
        if relativa:
            total = df[col].value_counts().sum()
            serie = df[col].value_counts().apply(lambda x: x / total)
            sns.barplot(x=serie.index, y=serie, ax=ax, palette='viridis', hue=serie.index, legend=False)
            
            # Configura el eje Y en formato de porcentaje
            ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1, decimals=0))
            
            if mostrar_valores:
                for p in ax.patches:
                    height = p.get_height()
                    ax.annotate(f'{height * 100:.0f}%', (p.get_x() + p.get_width() / 2., height), 
                                ha='center', va='center', fontsize=8, xytext=(0, 5), textcoords='offset points')
        else:
            serie = df[col].value_counts()
            sns.barplot(x=serie.index, y=serie, ax=ax, palette='viridis', hue=serie.index, legend=False)
            ax.set_ylabel('')
            
            if mostrar_valores:
                for p in ax.patches:
                    height = p.get_height()
                    ax.annotate(f'{height:.0f}', (p.get_x() + p.get_width() / 2., height), 
                                ha='center', va='center', fontsize=8, xytext=(0, 5), textcoords='offset points')

        ax.set_title(f'Distribución de {col}')
        ax.set_xlabel('', fontsize=5)
        ax.tick_params(axis='x', rotation=45)
        ax.set_ylabel('', fontsize=5)
        ax.tick_params(axis='both', labelsize=8)

    for j in range(i + 1, num_filas * 2):
        axes[j].axis('off')

    plt.tight_layout()
    plt.show()



def grouped_boxplots(df, cat_col, num_col):
    unique_cats = df[cat_col].unique()
    num_cats = len(unique_cats)
    group_size = 5

    for i in range(0, num_cats, group_size):
        subset_cats = unique_cats[i:i+group_size]
        subset_df = df[df[cat_col].isin(subset_cats)]
        
        plt.figure(figsize=(8, 4))
        sns.boxplot(x=cat_col, y=num_col, data=subset_df)
        plt.title(f'Boxplots of {num_col} for {cat_col} (Group {i//group_size + 1})')
        plt.xticks(rotation=45)
        plt.tick_params(axis='both', labelsize=8)
        plt.show()

def plot_categorical_numerical_relationship(df, categorical_col, numerical_col, show_values=False, measure='mean'):
    # Calcula la medida de tendencia central (mean o median)
    if measure == 'median':
        grouped_data = df.groupby(categorical_col)[numerical_col].median()
    else:
        # Por defecto, usa la media
        grouped_data = df.groupby(categorical_col)[numerical_col].mean()

    # Ordena los valores
    grouped_data = grouped_data.sort_values(ascending=False)

    # Si hay más de 5 categorías, las divide en grupos de 5
    if grouped_data.shape[0] > 5:
        unique_categories = grouped_data.index.unique()
        num_plots = int(np.ceil(len(unique_categories) / 5))

        for i in range(num_plots):
            # Selecciona un subconjunto de categorías para cada gráfico
            categories_subset = unique_categories[i * 5:(i + 1) * 5]
            data_subset = grouped_data.loc[categories_subset]

            # Crea el gráfico
            plt.figure(figsize=(8, 4))
            ax = sns.barplot(x=data_subset.index, y=data_subset.values)

            # Añade títulos y etiquetas
            plt.title(f'Relación entre {categorical_col} y {numerical_col} - Grupo {i + 1}')
            plt.xlabel("")
            plt.ylabel('')
            plt.xticks(rotation=45)
            ax.tick_params(axis='both', labelsize=8)

            # Mostrar valores en el gráfico
            if show_values:
                for p in ax.patches:
                    ax.annotate(f'{p.get_height():.1f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                                ha='center', va='center', fontsize=8, color='black', xytext=(0, 5),
                                textcoords='offset points')

            # Muestra el gráfico
            plt.show()
    else:
        # Crea el gráfico para menos de 5 categorías
        plt.figure(figsize=(8, 4))
        ax = sns.barplot(x=grouped_data.index, y=grouped_data.values)

        # Añade títulos y etiquetas
        plt.title(f'Relación entre {categorical_col} y {numerical_col}')
        plt.xlabel("")
        plt.ylabel("")
        plt.xticks(rotation=45)
        ax.tick_params(axis='both', labelsize=8)

        # Mostrar valores en el gráfico
        if show_values:
            for p in ax.patches:
                ax.annotate(f'{p.get_height():.1f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                            ha='center', va='center', fontsize=8, color='black', xytext=(0, 5),
                            textcoords='offset points')

        # Muestra el gráfico
        plt.show()


def plot_categorical(df, cat_col1, cat_col2, relative_freq=False, show_values=True, size_group=5):
    # Prepare the data
    count_data = df.groupby([cat_col1, cat_col2]).size().reset_index(name='count')
    
    if relative_freq:
        # Calculate total counts for relative frequency
        total_counts = df.groupby(cat_col1).size()
        # Calculate relative count as a percentage
        count_data['relative_count'] = count_data.apply(lambda x: x['count'] / total_counts[x[cat_col1]], axis=1)

    # Create the plot
    plt.figure(figsize=(8, 5))
    ax = sns.barplot(x=cat_col1, y='relative_count' if relative_freq else 'count', hue=cat_col2, data=count_data)

    # Add titles and labels
    plt.title(f'Relación entre {cat_col1} y {cat_col2}')
    plt.xlabel('')
    plt.ylabel('' if relative_freq else '')
    plt.xticks(rotation=45)
    ax.tick_params(axis='both', labelsize=8)
    # Format the y-axis and values on the graph
    if relative_freq:
        ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))

    # Add values above the bars
    if show_values:
        for p in ax.patches:
            # Format the value based on relative_freq
            value = '{:.0f}%'.format(100 * p.get_height()) if relative_freq else '{}'.format(int(p.get_height()))
            # Only add annotation if value is greater than 0
            if p.get_height() > 0:
                x = p.get_x() + p.get_width() / 2
                y = p.get_height()
                ax.annotate(value, (x, y), ha='center', va='center', fontsize=8, color='black', xytext=(0, 5),
                            textcoords='offset points')

    # Move the legend outside of the plot
    plt.legend(title=cat_col2, bbox_to_anchor=(1, 1), loc='upper left')

    # Adjust layout to make room for the legend
    plt.tight_layout()

    # Show the plot
    plt.show()


def cardinalidad(df, umbral_categoria, umbral_continua):
    result_data = []

    for col in df.columns:
        cardinalidad = df[col].nunique()
        porcentaje_cardinalidad = cardinalidad / len(df) * 100

        if cardinalidad == 2:
            valoracion = "Binaria"
        elif cardinalidad < umbral_categoria:
            valoracion = "Categórica"
        elif cardinalidad >= umbral_categoria:
            if porcentaje_cardinalidad >= umbral_continua:
                valoracion = "Numérica Continua"
            else:
                valoracion = "Numérica Discreta"

        result_data.append({'Columna': col, 'Cardinalidad': cardinalidad,
                            '% Cardinalidad': porcentaje_cardinalidad, 'Valoración': valoracion})

    result_df = pd.DataFrame(result_data)
    return result_df


def grafico_dispersion_con_correlacion(data, x, y, hue):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=data, x=x, y=y, hue=hue, palette="coolwarm")
    correlacion = data[x].corr(data[y])
    plt.title(f'Gráfico de dispersión entre {x} y {y}\nCorrelación: {correlacion:.2f}', fontsize=12)
    plt.xlabel(x, fontsize=12)
    plt.ylabel(y, fontsize=12)
    plt.legend(title="estancia media", title_fontsize=8)
    plt.show()