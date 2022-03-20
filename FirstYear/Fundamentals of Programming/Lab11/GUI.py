import sys

import pygame
from pygame.locals import *

from BattleField.BattleField import BattleField
from BattleShips.BattleShips import BattleShips
import time
# font = pygame.font.SysFont(None, 40)


# def draw_text(text, font, color, surface, x, y):
#     text_object = font.render(text, 1, color)
#     text_rectangle = text_object.get_rect()
#     text_rectangle.topleft = (x, y)
#     surface.blit(text_object, text_rectangle)


class GUI:
    def __init__(self):
        self.resolution = (720, 720)
        self.title = "Battleships"
        self.screen = None
        self.click = False
        pygame.init()
        pygame.display.set_caption(self.title)
        self.screen = pygame.display.set_mode(self.resolution)
        self.font = pygame.font.SysFont(None, 40)
        self.left_start_deploying_ships = 160
        self.top_start_deploying_ships = 160
        self.dimension = 40
        self.rotate = False
        self.battleships = None
        self.background = pygame.image.load("C:/Users/Teo/PycharmProjects/a11-alexteo24/images/ocean.jpg")
        self.grid_dimension_attack = 30
        self.p1_left_start_grid = 30
        self.p_top_start_grid = 210
        self.p2_left_start_grid = 370
        self.attack_status = False

    def start_gui(self):
        self.main_menu()

    @staticmethod
    def draw_text(text, font, color, surface, x, y):
        text_object = font.render(text, 1, color)
        text_rectangle = text_object.get_rect()
        text_rectangle.topleft = (x, y)
        surface.blit(text_object, text_rectangle)

    def drawGrid(self, left_start, top_start, dimension):
        for x in range(10):
            for y in range(10):
                rectangle = pygame.Rect(left_start + x * dimension, top_start + y * dimension,
                                        dimension, dimension)
                pygame.draw.rect(self.screen, (200, 200, 200), rectangle, 1)
    
    @staticmethod
    def get_grid_coord(mouse_x, mouse_y, left_start, top_start, dimension):
        if left_start <= mouse_x < left_start + dimension * 10:
            if top_start <= mouse_y < top_start + dimension * 10:
                # print((mouse_y - top_start) // dimension + 1, (mouse_x - left_start) // dimension + 1)
                return (mouse_y - top_start) // dimension + 1, (mouse_x - left_start) // dimension + 1
        return False

    def mark_ship(self, row, column, mouse_x, mouse_y, dimension, ocean):
        row = row
        column = column
        coord_x = (mouse_x // self.dimension) * self.dimension + 10
        coord_y = (mouse_y // self.dimension) * self.dimension + 5
        for i in range(0, dimension):
            self.draw_text(ocean[row][column], self.font, (255, 255, 255),
                           self.screen,
                           coord_x, coord_y)
            if not self.rotate:
                coord_x += self.dimension
                column += 1
            else:
                coord_y += self.dimension
                row += 1

    def first_player_lay_ships(self):
        running = True
        click = False
        dimension = 2
        number_three_ships = 2
        self.drawGrid(self.left_start_deploying_ships, self.top_start_deploying_ships, self.dimension)
        while running:
            self.draw_text('First player will lay his ships', self.font, (255, 255, 255), self.screen, 160, 100)
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if click:
                if self.get_grid_coord(mouse_x, mouse_y, self.left_start_deploying_ships,
                                       self.top_start_deploying_ships, 40):
                    if dimension < 5:
                        if dimension == 3:
                            if number_three_ships == 1:
                                try:
                                    pygame.display.update()
                                    row, column = self.get_grid_coord(mouse_x, mouse_y, self.left_start_deploying_ships,
                                                                      self.top_start_deploying_ships, 40)
                                    self.battleships.set_first_player_ships(row, column, dimension, self.rotate)
                                    self.mark_ship(row, column, mouse_x, mouse_y, dimension,
                                                   self.battleships.first_player.ocean_data)
                                    self.rotate = False
                                    number_three_ships -= 1
                                    dimension += 1
                                except Exception:
                                    pygame.display.update()
                            elif number_three_ships > 0:
                                try:
                                    pygame.display.update()
                                    row, column = self.get_grid_coord(mouse_x, mouse_y, self.left_start_deploying_ships,
                                                                      self.top_start_deploying_ships, 40)
                                    self.battleships.set_first_player_ships(row, column, dimension, self.rotate)
                                    self.mark_ship(row, column, mouse_x, mouse_y, dimension,
                                                   self.battleships.first_player.ocean_data)
                                    self.rotate = False
                                    number_three_ships -= 1
                                except Exception:
                                    pygame.display.update()
                        else:
                            try:
                                pygame.display.update()
                                row, column = self.get_grid_coord(mouse_x, mouse_y, self.left_start_deploying_ships,
                                                                  self.top_start_deploying_ships, 40)
                                self.battleships.set_first_player_ships(row, column, dimension, self.rotate)
                                self.mark_ship(row, column, mouse_x, mouse_y, dimension,
                                               self.battleships.first_player.ocean_data)
                                self.rotate = False
                                dimension += 1
                            except Exception:
                                pygame.display.update()
                    else:
                        try:
                            pygame.display.update()
                            row, column = self.get_grid_coord(mouse_x, mouse_y, self.left_start_deploying_ships,
                                                              self.top_start_deploying_ships, 40)
                            self.battleships.set_first_player_ships(row, column, dimension, self.rotate)
                            self.mark_ship(row, column, mouse_x, mouse_y, dimension,
                                           self.battleships.first_player.ocean_data)
                            self.rotate = False
                            dimension += 1
                            pygame.display.update()
                            time.sleep(1)
                            running = False
                        except Exception:
                            pygame.display.update()

            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_r:
                        self.rotate = not self.rotate
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                pygame.display.update()

    def second_player_lay_ships(self):
        running = True
        click = False
        dimension = 2
        number_three_ships = 2
        self.screen.blit(self.background, (0, 0))
        self.drawGrid(self.left_start_deploying_ships, self.top_start_deploying_ships, self.dimension)
        pygame.display.update()
        while running:
            self.draw_text('Second player will lay his ships', self.font, (255, 255, 255), self.screen, 160, 100)
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if click:
                if self.get_grid_coord(mouse_x, mouse_y, self.left_start_deploying_ships,
                                       self.top_start_deploying_ships, 40):
                    if dimension < 5:
                        if dimension == 3:
                            if number_three_ships == 1:
                                try:
                                    pygame.display.update()
                                    row, column = self.get_grid_coord(mouse_x, mouse_y, self.left_start_deploying_ships,
                                                                      self.top_start_deploying_ships, 40)
                                    self.battleships.set_second_player_ships(row, column, dimension, self.rotate)
                                    self.mark_ship(row, column, mouse_x, mouse_y, dimension,
                                                   self.battleships.second_player.ocean_data)
                                    self.mark_ship(row, column, mouse_x, mouse_y, dimension,
                                                   self.battleships.second_player.ocean_data)
                                    self.rotate = False
                                    number_three_ships -= 1
                                    dimension += 1
                                except Exception:
                                    pygame.display.update()
                            elif number_three_ships > 0:
                                try:
                                    pygame.display.update()
                                    row, column = self.get_grid_coord(mouse_x, mouse_y, self.left_start_deploying_ships,
                                                                      self.top_start_deploying_ships, 40)
                                    self.battleships.set_second_player_ships(row, column, dimension, self.rotate)
                                    self.mark_ship(row, column, mouse_x, mouse_y, dimension,
                                                   self.battleships.second_player.ocean_data)
                                    self.mark_ship(row, column, mouse_x, mouse_y, dimension,
                                                   self.battleships.second_player.ocean_data)
                                    self.rotate = False
                                    number_three_ships -= 1
                                except Exception:
                                    pygame.display.update()
                        else:
                            try:
                                pygame.display.update()
                                row, column = self.get_grid_coord(mouse_x, mouse_y, self.left_start_deploying_ships,
                                                                  self.top_start_deploying_ships, 40)
                                self.battleships.set_second_player_ships(row, column, dimension, self.rotate)
                                self.mark_ship(row, column, mouse_x, mouse_y, dimension,
                                               self.battleships.second_player.ocean_data)
                                self.mark_ship(row, column, mouse_x, mouse_y, dimension,
                                               self.battleships.second_player.ocean_data)
                                self.rotate = False
                                dimension += 1
                            except Exception:
                                pygame.display.update()
                    else:
                        try:
                            pygame.display.update()
                            row, column = self.get_grid_coord(mouse_x, mouse_y, self.left_start_deploying_ships,
                                                              self.top_start_deploying_ships, 40)
                            self.battleships.set_second_player_ships(row, column, dimension, self.rotate)
                            self.mark_ship(row, column, mouse_x, mouse_y, dimension,
                                           self.battleships.second_player.ocean_data)
                            self.rotate = False
                            dimension += 1
                            pygame.display.update()
                            time.sleep(1)
                            running = False
                        except Exception:
                            pygame.display.update()
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_r:
                        self.rotate = not self.rotate
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                pygame.display.update()

    # def reveal_destroyed_ship(self, row, column, mouse_x, mouse_y):
    #     dimension = self.grid_dimension_attack
    #     coordinates_row = [-dimension, - dimension, 0, dimension, dimension, dimension, 0, -dimension]
    #     coordinates_column = [0, dimension, dimension, dimension, 0, -dimension, -dimension, -dimension]
    #     row_surroundings = [-1, -1, 0, 1, 1, 1, 0, -1]
    #     column_surroundings = [0, 1, 1, 1, 0, -1, -1, -1]
    #     for index in range(0, len(self.battleships.second_player.guy_ships_locations)):
    #         locations = self.battleships.second_player.gui_ships_locations[index]
    #         if [row, column] in locations:
    #             for row_column in locations:
    #                 row_index = row_column[0]
    #                 column_index = row_column[1]
    #                 for i in range(0, 8):
    #                     coord_x = ((mouse_x - self.p2_left_start_grid % dimension) // dimension) * dimension + \
    #                               self.p2_left_start_grid % dimension + 5 + coordinates_row[i]
    #                     coord_y = ((mouse_y - self.p_top_start_grid % dimension) // dimension) * dimension + 5 + coordinates_column[i]
    #                     surrounding_row = row_index + row_surroundings[i]
    #                     surrounding_column = column_index + column_surroundings[i]
    #                     if self.battleships.second_player.masked_ocean[surrounding_row][surrounding_column] != 'X':
    #                         self.draw_text('O', self.font, (0, 255, 0), self.screen, coord_x, coord_y)

    def first_player_attack(self, row, column, mouse_x, mouse_y, dimension):
        pygame.display.update()
        # length = len(self.battleships.second_player.ships_locations)
        self.attack_status = self.battleships.first_player_attack(row, column)
        self.mark_hit_or_miss(row, column, mouse_x, mouse_y, dimension, self.battleships.second_player.masked_ocean, 2)
        # if len(self.battleships.second_player.ships_locations) != length:
        #     self.reveal_destroyed_ship(row, column, mouse_x, mouse_y)
        pygame.display.update()

    def second_player_attack(self, row, column, mouse_x, mouse_y, dimension):
        pygame.display.update()
        self.attack_status = self.battleships.second_player_attack(row, column)
        pygame.display.update()
        self.mark_hit_or_miss(row, column, mouse_x, mouse_y, dimension, self.battleships.first_player.masked_ocean, 1)

    def mark_hit_or_miss(self, row, column, mouse_x, mouse_y, dimension, ocean, player):
        if player == 1:
            coord_x = ((mouse_x - self.p2_left_start_grid % dimension) // dimension) * dimension + \
                      self.p2_left_start_grid % dimension + 5
        else:
            coord_x = ((mouse_x - self.p1_left_start_grid % dimension) // dimension) * dimension + \
                      self.p1_left_start_grid % dimension + 5
        coord_y = ((mouse_y - self.p_top_start_grid % dimension) // dimension) * dimension + 5
        if not self.attack_status:
            color = (0, 255, 0)
        else:
            color = (255, 0, 0)
        self.draw_text(ocean[row][column], self.font, color,
                       self.screen,
                       coord_x, coord_y)

    def playing_game(self):
        running = True
        label = self.font.render("Players will start attacking!", True, (255, 255, 255))
        self.screen.blit(label, (160, 100))
        self.draw_text("Player 1 attack here", self.font, (255, 255, 255), self.screen, 50, 175)
        self.drawGrid(self.p1_left_start_grid, self.p_top_start_grid, self.grid_dimension_attack)
        self.draw_text("Player 2 attack here", self.font, (255, 255, 255), self.screen, 370, 175)
        self.drawGrid(self.p2_left_start_grid, self.p_top_start_grid, self.grid_dimension_attack)
        pygame.display.update()
        time.sleep(1)
        who_will_attack = True
        self.click = False
        while running:
            anyone_won = self.battleships.check_if_anyone_won()
            if anyone_won == -1:
                if who_will_attack:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if self.click:
                        if self.get_grid_coord(mouse_x, mouse_y, 30, 210, 30):
                            row, column = self.get_grid_coord(mouse_x, mouse_y, 30, 210, 30)
                            try:
                                self.first_player_attack(row, column, mouse_x, mouse_y, 30)
                                who_will_attack = not who_will_attack
                                pygame.display.update()
                            except Exception:
                                pygame.display.update()
                else:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if self.click:
                        if self.get_grid_coord(mouse_x, mouse_y, 370, 210, 30):
                            row, column = self.get_grid_coord(mouse_x, mouse_y, 370, 210, 30)
                            try:
                                self.second_player_attack(row, column, mouse_x, mouse_y, 30)
                                who_will_attack = not who_will_attack
                                pygame.display.update()
                            except Exception:
                                pygame.display.update()
            else:
                if anyone_won:
                    time.sleep(1)
                    self.screen.blit(self.background, (0, 0))
                    self.draw_text("Congratulations! Player one won!", self.font, (255, 255, 255), self.screen, 150,
                                   300)
                    pygame.display.update()
                    time.sleep(5)
                    break
                else:
                    time.sleep(1)
                    self.screen.blit(self.background, (0, 0))
                    self.draw_text("Congratulations! Player two won!", self.font, (255, 255, 255), self.screen, 150,
                                   300)
                    pygame.display.update()
                    time.sleep(5)
                    break

            self.click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            pygame.display.update()

    def start_game(self):
        running = True
        ship_placed = False
        self.battleships = BattleShips(BattleField(), BattleField())
        while running:
            if not ship_placed:
                self.first_player_lay_ships()
                pygame.display.update()
                self.second_player_lay_ships()
                self.screen.blit(self.background, (0, 0))
                ship_placed = True
                self.playing_game()
                pygame.display.update()
                break
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            pygame.display.update()

    def main_menu(self):
        while True:
            self.screen.blit(self.background, (0, 0))
            mouse_x, mouse_y = pygame.mouse.get_pos()

            start_game_button = pygame.Rect(260, 260, 200, 50)
            if start_game_button.collidepoint(mouse_x, mouse_y):
                if self.click:
                    self.start_game()
            # pygame.draw.rect(screen, (0, 0, 0), start_game_button)
            self.draw_text('Start game', self.font, (255, 255, 255), self.screen, 285, 275)

            quit_button = pygame.Rect(260, 420, 200, 50)
            if quit_button.collidepoint(mouse_x, mouse_y):
                if self.click:
                    pygame.quit()
                    sys.exit()
            # pygame.draw.rect(screen, (0, 0, 0), quit_button)
            self.draw_text('Quit', self.font, (255, 255, 255), self.screen, 325, 435)

            self.click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True
            pygame.display.update()
