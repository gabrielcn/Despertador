import datetime
import pygame

# Pergunte ao usuário quais dias da semana o alarme deve tocar
print("Em quais dias da semana o alarme deve tocar?")
print("(Digite os números dos dias, separados por vírgula)")
print("Seg - 0, Ter - 1, Qua - 2, Qui - 3, Sex - 4, Sab - 5, Dom - 6")
dias_semana = input()

# Converter a lista de dias da semana em números inteiros
dias_semana = [int(dia) for dia in dias_semana.split(",")]

# Pergunte ao usuário em que horário o alarme deve tocar
print("Em que horário o alarme deve tocar?")
print("(Digite o horário no formato HH:MM)")
horario = input()

# Pergunte ao usuário qual música de alarme deseja usar
print("Qual música de alarme deseja usar?")
print("(Digite o caminho completo para o arquivo de música)")
musica = input()

# Inicialize a biblioteca pygame
pygame.init()

# Carregue a música de alarme
pygame.mixer.music.load(musica)

# Crie um loop infinito para verificar a data e hora atuais
while True:
    # Obtenha a data e hora atuais
    agora = datetime.datetime.now()

    # Verifique se o dia da semana atual está na lista de dias em que o alarme deve tocar
    if agora.weekday() in dias_semana:
        # Verifique se é hora de tocar o alarme
        if agora.strftime("%H:%M") == horario:
            # Tocar a música de alarme
            pygame.mixer.music.play()
