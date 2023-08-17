# PROGRAMA DE E-COMMERCE DE FARMÁCIA
import sef_layouts


def mostrar_menu():
    # Exibe layout predefinido do menu
    layout_menu = sef_layouts.menu()
    print(layout_menu)



if __name__ == '__main__':
    print('======== SISTEMA DE E-COMMERCE DE FARMÁRCIA ========')
    mostrar_menu()
