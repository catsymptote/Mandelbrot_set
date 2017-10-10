#include "main.h"
#include<string>


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


/*
// a sample exported function
void DLL_EXPORT SomeFunction(const LPCSTR sometext)
{
    MessageBoxA(0, sometext, "DLL Message", MB_OK | MB_ICONINFORMATION);
}

extern "C" DLL_EXPORT BOOL APIENTRY DllMain(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpvReserved)
{
    switch (fdwReason)
    {
        case DLL_PROCESS_ATTACH:
            // attach to process
            // return FALSE to fail DLL load
            break;

        case DLL_PROCESS_DETACH:
            // detach from process
            break;

        case DLL_THREAD_ATTACH:
            // attach to thread
            break;

        case DLL_THREAD_DETACH:
            // detach from thread
            break;
    }
    return TRUE; // succesful
}
*/
