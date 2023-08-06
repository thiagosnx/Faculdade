# Similar ao Switch case o Python possui o match case, porem ele só retorna similaridades

estacao = "outono"

match estacao:
    
    case "primavera":
        print("Estação das Flores")
    case "verao":
        print("O Verao é quente")
    case "inverno":
        print("Estação das Flores")
    case "outono":
        print("O outono é sempre igual, as floques caem no quintal")
    case _:
        print("Digite uma estação válida")
        