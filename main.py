import eel #Importamos la biblioteca eel
from Modules.MyAnimeList import MyAnimeListService
MAL = MyAnimeListService()

@eel.expose #Exponemos la funcion a javascript
def buscar_anime(nombre):
    print("Buscando el anime",nombre)
    anime = MAL.get_anime(nombre)
    eel.mostrar_datos(anime)
    return
def main():
    eel.init('gui') # Carpeta de la interfaz
    eel.start('index.html',size=(1500, 1000)) # Archivo con la inferfaz
if __name__ == '__main__':
    main()
