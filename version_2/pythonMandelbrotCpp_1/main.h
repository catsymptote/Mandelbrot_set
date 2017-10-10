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

LIBDLL bool if_true(float a);

LIBDLL int sum_int(int a, int b);

LIBDLL float csum_float(float a, float b);

#ifdef __cplusplus
}
#endif

#endif // __MAIN_H__
