#include "fonction_filtres.h"

using namespace std;

int main(int n, char* argv[]){
    if (argv[1] == "convolution"){
        convolution(argv[2],argv[3],argv[4]);
    }

    if (argv[1] == "filtre"){
        filtre(argv[2],argv[3],argv[4]);
    }

}