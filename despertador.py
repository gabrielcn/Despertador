import datetime
import pygame

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

    # Verifique se é hora de tocar o alarme
    if agora.strftime("%H:%M") == horario:
        # Tocar a música de alarme
        pygame.mixer.music.play()
