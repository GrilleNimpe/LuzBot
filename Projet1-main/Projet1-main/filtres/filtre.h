// NOTE : compiler avec l'option -lpng : gpp exemple.cpp -o exemple.exe -lpng

#include "../png_io.h"
#include "../fonctions.h"
#include <iostream>
#include <string>
#include <fstream>
using namespace std;


/*
Rôle : Passer une image en filtre.
Entrée : nom_fichier : Chaine de caractère correspondant à un nom d'image PNG.
matrice_f : Chaine de caractère correspondant au nom d'un fichier txt contenant une matrice
sortie_f : Chaine de caractère correspondant au nom de l'image de sortie
Sortie : Rien
Précondition : nom_fichier doit correspondre au nom d'un fichier PNG présent dans le dossier courant.
sortie_f doit finir par ".png" et avoir une longueur > 4, matrice_f doit correspondre au nom d'un fichier txt présent dans le dossier filtre_matrices.

Signature : procédure filtre(Ⓔ nom_fichier : Chaine de caractère, Ⓔ matrice_f : Chaine de caractère, Ⓔ sortie_f : Chaine de caractère)
*/

void filtre(string nom_fichier,string matrice_f,string sortie_f){
    size_t i,j;
    float a,b,c,d,e,f,g,h,k;
    RVBint pixeltmp;
    const string dossier =  "filtre_matrices/";
    ifstream monFlux(dossier+matrice_f);
    monFlux >> a >> b >> c >> d >> e >> f >> g >> h >> k;

    Image_PNG img_ini = charger_PNG(nom_fichier); // chargement de l'image dans le fichier d'entrée donné
    Image_PNG img_filtre = creer_PNG(img_ini.hauteur, img_ini.largeur);

    for(i = 0;i != img_ini.hauteur;i++){ // Parcours des ligne de la matrices.
        for(j = 0;j != img_ini.largeur;j++){ // Parcours chaque élément de la ligne (parcours des colonnes).
            pixeltmp = multiplication_matrices(img_ini.pixels[i][j],a,b,c,d,e,f,g,h,k);
            img_filtre.pixels[i][j] = verif_pixel(pixeltmp);
        }
    }
    sauver_PNG(sortie_f, img_filtre);
}

/* Tests réalisés avec le programme principal :

Entrée                       Sortie  Affichage                                                    Justification
256-trash.png ;              rien    trash_filtre.png correspond bien à 256-trash.png avec un     cas général 
sepia.txt ;                          filtre sepia
trash_filtre.png                       
*/
