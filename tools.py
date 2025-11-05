
# transfert :

# entrer dans le transfert 
# sélectionner le client à qui envoyer l'argent
# sélectionner le montant à envoyer
# afficher le message de verification de notre action
# retirer la somme du compte du premier client
# ajouter la meme somme au deuxieme client

def transfert():
    print("Bienvenue dans votre page de transfert !")
    destinataire = input("Entrez l'ID du destinataire : ")
    montant_str = input("Entrez le montant à transférer : ")


montant = float(montant_str)
if montant <= 0:
    print("Le montant doit être supérieur à 0.")
else:
    print(f"Le transfert de {montant:.2f} vers le compte de {destinataire} a été effectué avec succès !")
print("Retour vers le menu principal...")
    

    #retrait:
#- choisisser un montant 
#si retrait fait:
#- retirer le montant au solde + noter la date dans un historique

monant = input("Choisissez un montant : ")
message_grosses_coupures : input("Voulez vous des grosses coupures? ")
def message_grosses_coupures() : 
    if 

    #depot:
>>>>>>> Stashed changes
#- rentrer un montant 
#si depot fait: 
#- ajouter le montant au solde + noter la date dans un historique 
import data
from data import *



import datetime

x = datetime.datetime.now()
print(x) 


# reponse_message_depot_verif 

def rep_is_yes (rep):
    return rep in yes_responses

def rep_is_no (rep):
    return not (rep_is_yes (rep)) 

def save_depot_in_historique ():
    pass

def propose_depot ():
    message_depot = "Choisissez un montant "
    montant_depot = input(message_depot) 
    return montant_depot

def add_amount_to_account ():
    montant_depot () 

def fonctionnement_depot ():
    propose_depot ()
    print(message_depot_verif) 
    while rep_is_yes :
        add_amount_to_account
        save_depot_in_historique
        return return_to_accueil
    else :
        rep_is_no
        propose_depot
    








fonctionnement_depot ()
