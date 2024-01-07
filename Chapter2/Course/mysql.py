from pymysql import Connection

# Obtenir l'objet de connexion à la base de données MySQL
conn = Connection(
    host='localhost',    # Nom d'hôte(ou adresse IP)
    port=3306,           # Port par défaut 3306
    user='root',         # Nom du compte
    password=''          # Mot de passe
)

# Informations sur le logiciel d'impression de la base de données MySQL
print(conn.get_server_info())
# Fermer la connexion à la base de données
conn.close()