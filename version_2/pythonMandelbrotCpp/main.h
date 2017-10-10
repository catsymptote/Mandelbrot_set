#ifndef __MAIN_H__
#define __MAIN_H__

#include <windows.h>

/*  To use this exported function of dll, include this header
 *  in your project.
 */

#ifdef BUILD_DLL
    #define DLL_EXPORT __declspec(dllexport)
#else
    #define DLL_EXPORT __declspec(dllimport)
#endif


#ifdef __cplusplus
extern "C"
{
#endif

bool DLL_EXPORT if_true(float a);
int DLL_EXPORT sum_int(int a, int b);
float DLL_EXPORT csum_float(float a, float b);
int* DLL_EXPORT array_test();

//int* DLL_EXPORT function();

//void DLL_EXPORT SomeFunction(const LPCSTR sometext);

#ifdef __cplusplus
}
#endif

#endif // __MAIN_H__
