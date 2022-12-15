import gym
import pygame
from gym.utils.play import play

mapping = {(pygame.K_LEFT,): 0, (pygame.K_RIGHT,): 1}
play(gym.make("CartPole-v1", render_mode="rgb_array"), fps=5, keys_to_action=mapping)
