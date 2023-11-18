import argparse
import requests
import json
import datetime

def analyser_commande():
    parser = argparse.ArgumentParser(description="Extraction de valeurs historiques pour un ou plusieurs symboles boursiers.")
    parser.add_argument('symboles', nargs='+', help='Nom des symboles boursiers')
    parser.add_argument('-d', '--début', type=str, help='Date de début (format: AAAA-MM-JJ)')
    parser.add_argument('-f', '--fin', type=str, help='Date de fin (format: AAAA-MM-JJ)')
    parser.add_argument('-v', '--valeur', choices=['fermeture', 'ouverture', 'min', 'max', 'volume'], default='fermeture', help='La valeur désirée (par défaut: fermeture)')
    return parser.parse_args()

