

def sort_data(number,read,write,sor,da,data):
    while True: 
        d=number()
        if d=='1':
            print(*da(0,read()),sep='\n')    
        elif d=='2':
            print(*da(1,read()),sep='\n')        
        elif d=='3':
            print(*da(2,read()),sep='\n')    
        elif d=='4':
            print(*sor(input('Введите № класса: '),read()),sep='')   
        elif d=='5':
            print(*read(),sep='')
        elif d=='6':
            print(*sor(input('Введите фамилию ученика:'),read()),sep='')    
        elif d=='7':
            write(data())
        elif d=='8':
            print('До встречи!')        
            break  

  

        
