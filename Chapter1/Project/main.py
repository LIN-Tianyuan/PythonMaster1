"""
1.Concevoir une classe permettant l'encapsulation des données.
2.Concevoir une classe qui définit les fonctions liées à la lecture de fichiers
et utilise des sous-classes pour mettre en oeuvre des foctions spécifiques.
3.Lire des fichiers, produire des objets de données.
4.Effectuer des calculs logiques à partir des données requises
(calculer les ventes pour chaque jour)
5.Graphique via PyEcharts
"""

from file_define import TextFileReader, JSONFileReader
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType
text_file_reader = TextFileReader("January2023SalesData.txt")
json_file_reader = JSONFileReader("February2023SalesData.txt")

jan_data:list = text_file_reader.read_data()
feb_data:list = json_file_reader.read_data()
# Combiner deux mois de données en une seule liste
all_data:list = jan_data + feb_data


# {"2023-01-01":1234}
data_dict = {}
for record in all_data:
    if record.date in data_dict.keys():
        data_dict[record.date] += int(record.money)
    else:
        data_dict[record.date] = int(record.money)


# Visualisation développement de cartes
bar = Bar(init_opts=InitOpts(theme=ThemeType.WHITE))
bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("Sales", list(data_dict.values()), label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title="Daily Sales")
)
bar.render("Daily sales bar chart.html")