import mysql.connector
import psycopg2

class Personnel:
    def __init__(self, id, nom, prenom, username, email, phone, departement, date_arrivee, date_depart, ecole, convention, password, role, observations):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.username = username
        self.email = email
        self.phone = phone
        self.departement = departement
        self.date_arrivee = date_arrivee
        self.date_depart = date_depart
        self.ecole = ecole 
        self.convention = convention
        self.password = password
        self.role = role
        self.observations = observations



    def save(self, cursor):
        try:
            sql = """
            INSERT INTO personnels (nom, prenom, username, email, phone, departement, date_arrivee, date_depart, ecole, convention, password, role, observations) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id;
            """
            cursor.execute(sql, (self.nom, self.prenom, self.username, self.email, self.phone, self.departement, self.date_arrivee, self.date_depart, self.ecole, self.convention, self.password, self.role, self.observations))
            
            # Récupérer l'ID généré
            new_id = cursor.fetchone()[0]
            print(f"Personnel inséré avec succès, ID: {new_id}")
        
        except psycopg2.Error as e:
            print(f"Erreur lors de l'insertion de Personnel dans la BD: {e}")


    def update(self, cursor):
        try:
            sql = """
            UPDATE personnels 
            SET 
                nom=%s, 
                prenom=%s, 
                username=%s, 
                email=%s, 
                phone=%s, 
                departement=%s, 
                date_arrivee=%s, 
                date_depart=%s, 
                ecole=%s, 
                convention=%s, 
                password=%s, 
                role=%s, 
                observations=%s 
            WHERE id=%s
            """
            # Correction du nom de colonne "observations" et de l'ordre des champs
            cursor.execute(sql, (
                self.nom, 
                self.prenom, 
                self.username,  # Correction ici
                self.email, 
                self.phone, 
                self.departement, 
                self.date_arrivee, 
                self.date_depart, 
                self.ecole, 
                self.convention, 
                self.password, 
                self.role, 
                self.observations,  # Correction du nom
                self.id
            ))
        except mysql.connector.Error as e:
            print(f"Erreur lors de la modification de Personnel dans la bd: {e}")
            
            