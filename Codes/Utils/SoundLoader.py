import pygame
import os


class SoundLoader:
    # 載入音樂、音效
    Sound_folder = "../Sound"
    Expl = "../Sound/Expl"
    Pow = "../Sound/Pow"

    background_music = pygame.mixer.Sound(os.path.join(Sound_folder, "background.ogg"))

    # Shoot sound
    shoot_sound = pygame.mixer.Sound(os.path.join(Sound_folder, "shoot.wav"))

    # Gun sound (Pow)
    gun_sound = pygame.mixer.Sound(os.path.join(Pow, "pow1.wav"))
    shield_sound = pygame.mixer.Sound(os.path.join(Pow, "pow0.wav"))

    # Die sound
    die_sound = pygame.mixer.Sound(os.path.join(Sound_folder, "rumble.ogg"))

    # Expl sound
    expl_sounds = [
        pygame.mixer.Sound(os.path.join(Expl, "expl0.wav")),
        pygame.mixer.Sound(os.path.join(Expl, "expl1.wav"))
    ]

    # Background sound
    pygame.mixer.music.load(os.path.join(Sound_folder, "Background.ogg"))
    pygame.mixer.music.set_volume(0.4)
