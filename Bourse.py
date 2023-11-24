import requests
from datetime import date

class ErreurDate(Exception):
    pass

class Bourse:
    def __init__(self):
        # Vous pouvez initialiser des variables nécessaires ici
        pass

    def prix(self, symbole, date):
        # Votre implémentation ici
        date_actuelle = date.today()

        if date > date_actuelle:
            raise ErreurDate("La date d'intérêt est postérieure à la date actuelle.")

        historique = self.produire_historique(symbole, date)
        return self.prix_recent(historique, date)

    def produire_historique(self, symboles, début, fin):
        # Méthode pour obtenir l'historique du symbole à partir du serveur
        url = f'https://pax.ulaval.ca/action/{symboles}/historique/'
        params = {
            
            'début': début,
            'fin': fin,
        }
        response = requests.get(url=url, params=params)

    def prix_recent(self, historique, date):
        # Méthode pour trouver le prix le plus récent avant la date d'intérêt
        dates = sorted(historique.keys(), reverse=True)
        for d in dates:
            if d <= str(date):
                return historique[d]['fermeture']
        raise ErreurDate("Aucune valeur de fermeture disponible avant la date spécifiée.")
