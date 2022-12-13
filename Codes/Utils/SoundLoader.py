import pygame
import os
class SoundLoader:
    # 載入音樂、音效
    sound = "../Sound"
    shoot_sound = pygame.mixer.Sound(os.path.join("%s" % sound, "shoot.wav"))
    gun_sound = pygame.mixer.Sound(os.path.join(sound, "pow1.wav"))
    shield_sound = pygame.mixer.Sound(os.path.join(sound, "pow0.wav"))
    die_sound = pygame.mixer.Sound(os.path.join(sound, "rumble.ogg"))
    expl_sounds = [
        pygame.mixer.Sound(os.path.join(sound, "expl0.wav")),
        pygame.mixer.Sound(os.path.join(sound, "expl1.wav"))
    ]
    pygame.mixer.music.load(os.path.join(sound, "background.ogg"))
    pygame.mixer.music.set_volume(0.4)
