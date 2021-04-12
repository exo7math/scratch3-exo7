#!/usr/bin/python3
# -*- coding: utf-8 -*-

#------------------------------------------
# Le chiffre de Vigenère
#------------------------------------------

####################################################
## Pour le chapitre

def vigenere(mot,cle):                   # Clé est du type [n_1,...,n_k]
    message_code = []
    k = len(cle)                         # Longueur de la clé
    i = 0                                # Rang dans le bloc   
    for lettre in mot:                   # Pour chaque lettre 
        nomb = ord(lettre)-65            # Lettre devient nb de 0 à 25
        nomb_code = (nomb+cle[i]) % 26   # Vigenère : on ajoute n_i
        lettre_code = chr(nomb_code+65)  # On repasse aux lettres
        i=(i+1) % k                      # On passe au rang suivant
        message_code.append(lettre_code) # Ajoute lettre au message                   
    message_code = "".join(message_code) # Revient à chaine caractères
    return(message_code)
    
#print("Vigenère a dit : ",vigenere("AAABBBCCC",[0,1,2,0]))
#print(vigenere(vigenere("AAABBBCCC",[0,1,2,0]),[-0,-1,-2,-0]))

####################################################
## Vrai code


# Chiffrement de Vigenère (pour un mot ou une phrase)
# cle est la liste [n_1,n_2,...,n_k]
def vigenere_bis(mot,cle):
    message_code = []
    k = len(cle)                             # longueur de la clé
    i = 0                                    # rang dans le bloc
    # Pour chaque lettre 
    for lettre in mot: 
        if lettre == " ":                    # On ne touche pas aux espaces 
            lettre_code = " "
        else:
            nomb = ord(lettre)-65            # Lettre devient nombre de 0 à 25
            nomb_code = (nomb+cle[i]) % 26   # Chiffrement de Vigenère : on ajoute n_i
            lettre_code = chr(nomb_code+65)  # On repasse aux lettres
            i=(i+1) % k                      # On passe au rang suivant
        message_code.append(lettre_code)     # On ajoute la lettre codée au message                   
    message_code = "".join(message_code)     # On revient à une chaine de caractère
    return(message_code)
    
   
# Déchiffrement de Vigenère (pour un mot ou une phrase)
def decode_vigenere_bis(mot,cle):
    return vigenere_bis(mot,[-n for n in cle]) 

# Exemple


mot = "A VAINCRE SANS PERIL ON TRIOMPHE SANS GLOIRE"
cle =[4,11,7]
mot_code = vigenere_bis(mot,cle)
print("Départ : ",mot, "Clé : ", cle)
print("Codé : ", mot_code)
print("Décodé : ",decode_vigenere_bis(mot_code,cle))



####################################################
# Affichage et tri


# Statistiques (pour un mot ou une phrase)
def statistiques(phrase):
    liste_stat = [0 for x in range(26)]      # On part d'une liste avec des 0
    for lettre in phrase:                    # On parcourt la phrase
        i = ord(lettre)-65
        if 0 <= i < 26:          # Si c'est une vraie lettre
          liste_stat[i] = liste_stat[i] + 1
    return(liste_stat)

# Tri des statistiques   
def tri_statistiques(liste):
    pastri = []                  # Liste avec lettre en face
    for i in range(26):
        pastri.append( (chr(65+i), liste[i]) )  
    tri = sorted(pastri, key=lambda freq: freq[1], reverse=True )
    return(tri)

# Test
phrase="LA VIE C EST COMME UNE BICYCLETTE IL FAUT AVANCER POUR NE PAS PERDRE L EQUILIBRE"

#print("Statistiques de la phrase :", phrase)
liste = statistiques(phrase)
#print(liste)   
#print(tri_statistiques(liste))   

    
# Test 
phrase1=[phrase[i] for i in range(0,len(phrase),3)]
phrase2=[phrase[i] for i in range(1,len(phrase),3)]
phrase3=[phrase[i] for i in range(2,len(phrase),3)]
#print(phrase1)
#print(phrase2)
#print(phrase3)
liste1 = statistiques(phrase1)
liste2 = statistiques(phrase2)
liste3 = statistiques(phrase3)
#print(liste1, liste2, liste3)

#print(tri_statistiques(liste1)[0:5])

#print(tri_statistiques(liste2)[0:5])

#print(tri_statistiques(liste3)[0:5])

#print(tri_statistiques(statistiques(phrase)))


 
    
