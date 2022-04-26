def horas_de_sono():
    h_1 = int(input('Hora em que você foi dormir: '))
    m_1 = int(input('Minuto em que você foi dormir: '))
    h_2 = int(input('Hora em que você despertou: '))
    m_2 = int(input('Minuto em que você despertou: '))
    
    h_1 = h_1*60
    h_2 = h_2*60
    if h_1 > 12:
        print('Você dormiu por {} horas'.format(int((h_2 + m_2 + 1440 - h_1 - m_1)/60)))
        
    else:
        print('Você dormiu por {} horas'.format(int((h_2 + m_2 + 720 - h_1 - m_1)/60)))

horas_de_sono()
