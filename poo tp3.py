class Carte: # Définition de la classe
    "Une carte d'un jeu de 32 ou 52 cartes"
    def __init__(self,valeur,couleur): # méthode 1 : constructeur
        self.valeur=valeur # 1er attribut valeur {de 2 à 14 pour as}
        self.couleur=couleur # 2e attribut {'pique','carreau','coeur','trefle'}
    def getAttribut(self):
        return(self.valeur,self.couleur)
    def getCouleur(self):
        return(self.couleur)
    def getValeur(self):
        return(self.valeur)

    def setValeur(self,v):
        if 2<=v<=14:
            self.valeur=v
            return True
        else:
            return False
    def setCouleur(self,couleur):
         self.couleur=couleur
    
c2=Carte(13,'coeur')
print(c2.getAttribut())

c2.setValeur(8)
c2.setCouleur('carreau')
print(c2.getAttribut())
print(c2)




