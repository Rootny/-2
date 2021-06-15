# Кодирование меток

импортировать  numpy  как  np
из  предварительной обработки импорта sklearn

input_labels  = [ 'красный' , 'черный' , 'красный' , 'зеленый' , 'черный' , 'желтый' , 'белый' ]

кодировщик  =  предварительная обработка . LabelEncoder ()

печать ( кодировщик . fit ( input_labels ))

test_labels  = [ 'зеленый' , 'красный' , 'черный' ]
encoded_values  =  кодировщик . преобразовать ( test_labels )
print ( " \ n Labels =" , test_labels )

print ( "Закодированные значения =" , список ( кодированные_значения ))

# декодировать случайного набора числел
encoded_values  = [ 3 , 0 , 4 , 1 ]
decoded_list  =  кодировщик . обратное_преобразование ( кодированные_значения )
print ( " \ n Encoded values ​​=" , encoded_values )

print ( "Decoded labels =" , list ( decoded_list ))
# декодировать значения
