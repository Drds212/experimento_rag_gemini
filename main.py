from rag_con_gemini import alimentar_cerebro, preguntar


print(f'{'-'*30}RAG con gemini{'-'*30}')
print('1._ Para subir informacion')
print('2._ Para consultar a la IA')
print()

opcion = int(input(':'))
if opcion == 1 or opcion == 2:
    match opcion:
        case 1:
            texto = input('Escriba un texto para agregar a la base de datos: \n')
            if texto:
                alimentar_cerebro(texto)
            else : print('No se admite un texto vacio')
        
        case 2:    
            print("\n--- CONSULTA ---")
            duda_usuario = input('Escriba su consulta: ')
            print(preguntar(duda_usuario))

else:print('opcion no valida')