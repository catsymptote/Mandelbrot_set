#include "main.h"

#include <string>

#define LIBDLL extern "C" __declspec(dllexport)

LIBDLL bool if_true(float a)
{
    if (a > 1)
    {
        return true;
    }
    return false;
}

LIBDLL int sum_int(int a, int b)
{
    return a + b;
}

LIBDLL float csum_float(float a, float b)
{
    return a + b;
}


/// Returns some numbers
LIBDLL int* array_test()
//extern "C" int* function()
{
    int* information = new int[10];
    for(int k=0;k<10;k++)
    {
        information[k] = k;
    }
    return information;
}



/// Returns 2x2 from 3x3 array/list in Python


/*
LIBDLL bool image_color_finder(std::string file_dir)
{
    CImg<float> image("hills.png");
    CImgDisplay main_disp(image);
    float pixvalR = image(10,10,0,0); // read red val at coord 10,10
    float pixvalG = image(10,10,0,1); // read green val at coord 10,10
    float pixvalB = image(10,10,0,2); // read blue val at coord 10,10
    //std::cout << "R = " << pixvalR << ", G = " << pixvalG << ", B = " << pixvalB;

    //std::cin.ignore();
}
*/
