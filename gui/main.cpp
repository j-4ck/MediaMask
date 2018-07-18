#include <windows.h>
#include <iostream>
#include <stdlib.h>
#include <string.h>
#define FILE_MENU_NEW 1
#define FILE_MENU_OPEN 2
#define FILE_MENU_EXIT 3
#define FILE_MENU_HELP 4
#define DEC_COM 5
#define ENC_COM 6

using namespace std;
HWND button;
// GUI VERSION
LRESULT CALLBACK WindowProcedure(HWND,UINT,WPARAM,LPARAM);

void AddMenus(HWND);
void AddControls(HWND);

HMENU hMenu;
HWND hEdit;
HWND hEdit2;

int WINAPI WinMain(HINSTANCE hInst , HINSTANCE hPrevInst, LPSTR args,int ncmdshow)
{
    //system("mode 17,9");
    MessageBox(NULL,"Welcome to MediaMask","MediaMask",MB_OK);
    WNDCLASSW wc = {0};

    wc.hbrBackground = (HBRUSH)COLOR_WINDOW; // BG COLOR OF THE WINDOW
    wc.hCursor = LoadCursor(NULL, IDC_ARROW); // TYPE OF CURSOR
    wc.hInstance = hInst;
    wc.lpszClassName = L"myWindowClass";//PREFIX + CLASS NAME
    wc.lpfnWndProc = WindowProcedure;
    if(!RegisterClassW(&wc))
        return -1;
    CreateWindowW(L"myWindowClass",L"MediaMask",WS_OVERLAPPEDWINDOW | WS_VISIBLE,100,100,500,300,NULL,NULL,NULL,NULL);
    MSG msg = {0};
    while( GetMessage(&msg,NULL,NULL,NULL))
    {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }
    return 0;
}

LRESULT CALLBACK WindowProcedure(HWND hWnd,UINT msg,WPARAM wp,LPARAM lp)
{
    switch (msg)
    {
        case WM_COMMAND:
            switch(wp){
                case FILE_MENU_EXIT:
                    //MessageBeep(MB_OK);
                    DestroyWindow(hWnd);
                    break;
                /*
                case FILE_MENU_NEW:
                    MessageBeep(MB_ICONASTERISK);
                    break;
                */

                case DEC_COM:
                        {
                            char finalCommand[100] = "python MediaMask(cpp_compat).py d ";
                            char space[100] = " ";
                            wchar_t fname[100];
                            wchar_t password[100];
                            char charFname[100];
                            char charPassword[100];
                            GetWindowTextW(hEdit,fname,sizeof(fname));
                            GetWindowTextW(hEdit2,password,sizeof(password));
                            wcstombs(charFname,fname,sizeof(charFname));
                            wcstombs(charPassword,password,sizeof(charPassword));
                            strcat(finalCommand, charFname);
                            strcat(finalCommand, space);
                            strcat(finalCommand, charPassword);
                            system(finalCommand);                    //CONVERT WIDE CHARS TO REGULAR CHARS
                            MessageBox(NULL,"File Decrypted!","MediaMask",MB_OK);
                            break;
                        }
                case ENC_COM:
                    {
                        char finalCommand[100] = "python MediaMask(cpp_compat).py e ";
                        char space[100] = " ";
                        wchar_t fname[100];
                        wchar_t password[100];
                        char charFname[100];
                        char charPassword[100];
                        GetWindowTextW(hEdit,fname,sizeof(fname));
                        GetWindowTextW(hEdit2,password,sizeof(password));
                        wcstombs(charFname,fname,sizeof(charFname));
                        wcstombs(charPassword,password,sizeof(charPassword));
                        strcat(finalCommand, charFname);
                        strcat(finalCommand, space);
                        strcat(finalCommand, charPassword);
                        system(finalCommand);                    //CONVERT WIDE CHARS TO REGULAR CHARS
                        MessageBox(NULL,"File Encrypted!","MediaMask",MB_OK);
                        break;
                    }
            }
            break;
        case WM_CREATE: //when window is created
            AddMenus(hWnd);
            AddControls(hWnd);
            break;
        case WM_DESTROY:
            PostQuitMessage(0);
            break;
        default:
            return DefWindowProcW(hWnd,msg,wp,lp);
    }
}


void AddMenus(HWND hWnd){
    hMenu = CreateMenu(); //create a menu
    HMENU hFileMenu = CreateMenu();
    HMENU hSubMenu = CreateMenu();
    HMENU hSubMenu2 = CreateMenu();
    HMENU hSubMenu3 = CreateMenu();
    AppendMenu(hMenu,MF_POPUP,(UINT_PTR)hFileMenu,"File");
    AppendMenu(hMenu,MF_POPUP,(UINT_PTR)hSubMenu2,"Help");

    //AppendMenu(hFileMenu,MF_STRING,FILE_MENU_NEW,"New");
    AppendMenu(hFileMenu,MF_POPUP,(UINT_PTR)hSubMenu,"Options");
    AppendMenu(hFileMenu,MF_SEPARATOR,NULL,NULL);
    AppendMenu(hFileMenu,MF_STRING,FILE_MENU_EXIT,"Kill");

    AppendMenu(hSubMenu,MF_STRING,ENC_COM,"Encryption");
    AppendMenu(hSubMenu,MF_STRING,DEC_COM,"Decryption");

    AppendMenu(hSubMenu2,MF_POPUP,(UINT_PTR)hSubMenu3,"Help menu");
    AppendMenu(hSubMenu3,MF_STRING,NULL,"1st) Enter the chosen filename");
    AppendMenu(hSubMenu3,MF_STRING,NULL,"2nd) Enter the required password credentials");
    AppendMenu(hSubMenu3,MF_STRING,NULL,"3rd) Click either 'encryption' or 'decryption' depending on your requirements");
    AppendMenu(hSubMenu3,MF_STRING,NULL,"Note: When encrypting, the filename will have 'e_' appended to it. Removed when decrypting.");
    SetMenu(hWnd,hMenu);
}

void AddControls(HWND hWnd){

    CreateWindowW(L"static",L"Filename:",WS_VISIBLE | WS_CHILD | WS_BORDER | SS_CENTER ,200,50,100,25,hWnd,NULL,NULL,NULL); // above text
    hEdit = CreateWindowW(L"edit",L"",WS_VISIBLE | WS_CHILD | WS_BORDER | ES_MULTILINE | ES_AUTOVSCROLL |  ES_AUTOHSCROLL, 150,70,200,20,hWnd,NULL,NULL,NULL); // text box
    CreateWindowW(L"static",L"Password:",WS_VISIBLE | WS_CHILD | WS_BORDER | SS_CENTER ,200,100,100,25,hWnd,NULL,NULL,NULL);
    hEdit2 = CreateWindowW(L"edit",L"",WS_VISIBLE | WS_CHILD | WS_BORDER | ES_MULTILINE | ES_AUTOVSCROLL |  ES_AUTOHSCROLL, 150,120,200,20,hWnd,NULL,NULL,NULL);
}
