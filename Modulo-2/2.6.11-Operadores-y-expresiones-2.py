hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))
   
hour += (mins + dura) // 60 
mins = (mins + dura) % 60   

print ("La hora cuando acabe el evento será:", hour,":", mins, "Lean usogui")   