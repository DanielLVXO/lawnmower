def print_menu(map_loaded = True, sub_menu = 0):
  
    if map_loaded:
        match sub_menu:
            case 0:
                print("Vad önskar du göra")
                print("1.   ladda ny karta")
                print("2.   Kör simulering")
            case 1:
                print("Välj fil:")
                print("1. ...")
                print("2. ...")
            case 2:
                print("Välj agoritm")
                print("1. Standard")
                print("2. Spiral")
    else:
        print("Vad önskar du att göra")
        print("1.   ladda karta")
        
