#include "png_io.h"
#include<iostream>
#include<string>
using namespace std;

struct RVBint {
	int rouge, vert, bleu;
};

// Effectuer l'addition de 9 pixels
RVBint addition9(RVBint pixel1, RVBint pixel2, RVBint pixel3, RVBint pixel4, RVBint pixel5, RVBint pixel6, RVBint pixel7, RVBint pixel8, RVBint pixel9){
    // Addition de chaque composants de neuf pixels (neuf car matrice 3*3).
    RVBint pixel_res;
    pixel_res.rouge = pixel1.rouge + pixel2.rouge + pixel3.rouge + pixel4.rouge + pixel5.rouge + pixel6.rouge + pixel7.rouge + pixel8.rouge + pixel9.rouge;
    pixel_res.vert = pixel1.vert + pixel2.vert + pixel3.vert + pixel4.vert + pixel5.vert + pixel6.vert + pixel7.vert + pixel8.vert + pixel9.vert;
    pixel_res.bleu = pixel1.bleu + pixel2.bleu + pixel3.bleu + pixel4.bleu + pixel5.bleu + pixel6.bleu + pixel7.bleu + pixel8.bleu + pixel9.bleu;
    return pixel_res;
}

// Effectuer la multiplication d'un pixel avec un float.
RVBint multiplication(float nb, RVB pixel_ini){
    RVBint pixel_res;
    // WARNING : conversion float-int => correspond à la
    // récupération de la partie entière pour le type unsigned char.
    pixel_res.rouge = pixel_ini.rouge * nb;
    pixel_res.vert = pixel_ini.vert * nb;
    pixel_res.bleu = pixel_ini.bleu * nb;
    return pixel_res;
}

// Effectuer une multiplcation matricielle entre une matrice 3*3 et une matrice 3*1
RVBint multiplication_matrices(RVB pixel1, float a, float b, float c, float d, float e, float f, float g, float h, float i){
    RVBint pixel_res;
    pixel_res.rouge = (pixel1.rouge * a + pixel1.vert * b + pixel1.bleu * c)/1;
    pixel_res.vert = (pixel1.rouge * d + pixel1.vert * e + pixel1.bleu * f)/1;
    pixel_res.bleu = (pixel1.rouge * g + pixel1.vert * h + pixel1.bleu * i)/1;
    return pixel_res;
}

// Effectuer l'addition de deux pixels.
RVBint addition(RVB pixel1, RVB pixel2){
    RVBint pixel_res;
    pixel_res.rouge = pixel1.rouge + pixel2.rouge;
    pixel_res.vert = pixel1.vert + pixel2.vert;
    pixel_res.bleu = pixel1.bleu + pixel2.bleu;
    return pixel_res;
}

// Faire la moyenne de 2 pixels
RVB identite(RVB pixel){
    RVB pixel_sortie;
    pixel_sortie.rouge = pixel.rouge;
    pixel_sortie.vert = pixel.vert;
    pixel_sortie.bleu = pixel.bleu;
    return pixel_sortie;
}

// S'assurer que les valeur RVB soient sur [0,255].
RVB verif_pixel(RVBint pixel){
    RVB pixel_sortie;
    // WARNING : conversion int-unsigned char => série de if else 
    // pour s'assurer que la conversion se passe au mieux.
    if (pixel.rouge < 0){
        pixel.rouge = 0;
    }
    if (pixel.vert < 0){
        pixel.vert = 0;
    }
    if (pixel.bleu < 0){
        pixel.bleu = 0;
    }
    if (pixel.rouge > 255){
        pixel.rouge = 255;
    }
    if (pixel.vert > 255){
        pixel.vert = 255;
    }
    if (pixel.bleu > 255){
        pixel.bleu = 255;
    }

    pixel_sortie.rouge = pixel.rouge;
    pixel_sortie.vert = pixel.vert;
    pixel_sortie.bleu = pixel.bleu;
    return pixel_sortie;
}
