import os

def print_menu(sub_menu = 0, map_loaded = True):
  
    if map_loaded:
        match sub_menu:
            case 0:
                print("Vad önskar du göra")
                print("1.   ladda ny karta")
                print("2.   Kör simulering")
            case 1:
                map_files = [file for file in os.listdir("maps") if file.endswith(".csv")]
                print("Välj fil:")
                i = 1
                for map in map_files:
                    print(f"{i}. {map[:-4]}")
                    i += 1

            case 2:
                print("Välj agoritm")
                print("1. Standard")
                print("2. Spiral")
    else:
        print("Ladda karta")
        map_files = [file for file in os.listdir("maps") if file.endswith(".csv")]
        print("Välj fil:")
        i = 1
        for map in map_files:
            print(f"{i}. {map[:-4]}")
            i += 1
        
