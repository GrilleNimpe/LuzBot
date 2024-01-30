// NOTE : compiler avec l'option -lpng : gpp exemple.cpp -o exemple.exe -lpng

#include "../png_io.h"
#include "../fonctions.h"
#include<iostream>
#include<string>
#include <fstream>
using namespace std;

/*
Rôle : Passer une image en convolution.
Entrée : nom_fichier : Chaine de caractère correspondant à un nom d'image PNG.
matrice_f : Chaine de caractère correspondant au nom d'un fichier txt contenant une matrice
sortie_f : Chaine de caractère correspondant au nom de l'image de sortie
Sortie : Rien
Précondition : nom_fichier doit correspondre au nom d'un fichier PNG présent dans le dossier courant.
sortie_f doit finir par ".png" et avoir une longueur > 4, matrice_f doit correspondre au nom d'un fichier txt présent dans le dossier convolution_matrices.

Signature : procédure convolution(Ⓔ nom_fichier : Chaine de caractère, Ⓔ matrice_f : Chaine de caractère, Ⓔ sortie_f : Chaine de caractère)
*/

void convolution(string nom_fichier,string matrice_f,string sortie_f){
    size_t i,j;
    float a,b,c,d,e,f,g,h,k;
    RVBint pixeltmp;
    const string dossier =  "filtre_matrices/";
    ifstream monFlux(dossier+matrice_f);
    monFlux >> a >> b >> c >> d >> e >> f >> g >> h >> k;

    Image_PNG img_ini = charger_PNG(nom_fichier); // chargement de l'image dans le fichier d'entrée donné
    Image_PNG img_tmp= creer_PNG(img_ini.hauteur+2, img_ini.largeur+2);//création de img_tmp : img_ini mais avec des bords noirs pour ne pas faire de cas spécifiques (bords et coins).
    Image_PNG img_convolution= creer_PNG(img_ini.hauteur, img_ini.largeur);

    for(i = 1;i != img_tmp.hauteur-1;i++){ // Parcours des ligne de la matrices.
        for(j = 1;j != img_tmp.largeur-1;j++){ // Parcours chaque élément de la ligne (parcours des colonnes).
            // Création de img_tmp
            img_tmp.pixels[i][j] = identite(img_ini.pixels[i-1][j-1]);
        }
    }
    for(i = 1;i != img_tmp.hauteur-1;i++){ // Parcours des ligne de la matrices.
        for(j = 1;j != img_tmp.largeur-1;j++){ // Parcours chaque élément de la ligne (parcours des colonnes).
            // On fait la convolution
            pixeltmp = addition9(multiplication(a,img_tmp.pixels[i-1][j-1]),multiplication(b,img_tmp.pixels[i-1][j]),multiplication(c,img_tmp.pixels[i-1][j+1]),multiplication(d,img_tmp.pixels[i][j-1]),multiplication(e,img_tmp.pixels[i][j]),multiplication(f,img_tmp.pixels[i][j+1]),multiplication(g,img_tmp.pixels[i+1][j-1]),multiplication(h,img_tmp.pixels[i+1][j]),multiplication(k,img_tmp.pixels[i+1][j+1]));
            img_convolution.pixels[i-1][j-1] = verif_pixel(pixeltmp);
        }
    }
    sauver_PNG(sortie_f, img_convolution);
}

/*
//---------------------------------------[ TEST CONVOLUTION ]----------------------------------------------------
Entrée                       Sortie  Affichage                                                    Justification
256-trash.png ;              rien    trash_convolution.png correspond bien à 256-trash.png avec   cas général 
convolution ; -1 ; -1 ; -1 ;         un filtre flou 
-1 ; -1 ; -1 ; flou.txt                  
; trash_convolution.png                                                                             

*/
