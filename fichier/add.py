import mysql.connector
import sys
import pygame
from fichier.global_def import Global
from fichier.product_manager import Product_Manager

class Add(Global):
    def __init__(self):
        Global.__init__(self)
        self.manager = Product_Manager()
        self.name = ""
        self.description = ""
        self.price = ""
        self.quantity = ""
        self.id_category = ""
        self.entry = 0
        self.add_time = 0
        self.check_v = False
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="azerty",
            database="store"
        )
        self.cursor = self.connection.cursor()
        self.add_running = True
        pygame.init()

    def rect(self, color, x1, y1, x2, y2):   
        return pygame.Rect(x1, y1, x2, y2), color

    def input(self):
        self.input_name = pygame.draw.rect(self.screen, self.black, (220, 250, 190, 40), 2)
        self.input_description = pygame.draw.rect(self.screen, self.black, (210, 430, 380, 40), 2)
        self.input_price = pygame.draw.rect(self.screen, self.black, (420, 345, 120, 40), 2)
        self.input_quantity = pygame.draw.rect(self.screen, self.black, (250, 345, 120, 40), 2)
        self.input_id_category= pygame.draw.rect(self.screen, self.black, (420, 250, 120, 40), 2)
        
        info_image_rect = self.image("information", "img/menu20.png", 25, 17, 530, 200)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if info_image_rect.collidepoint(mouse_x, mouse_y):
            self.rect3 = pygame.draw.rect(self.screen, self.white, (600, 180, 100, 100), 0)
            pygame.draw.rect(self.screen, self.black, self.rect3,2)
            self.text_center3("1 : Sushi", self.black, self.rect3, 0, 10)
            self.text_center3("2 : Sauce", self.black, self.rect3, 0, -10)

        self.text()
        
    def text(self):
        self.texte(20, self.name, self.black, 300, 270)
        self.texte(20, self.description, self.black, 400, 450)
        self.texte(20, self.price, self.black,480, 370)
        self.texte(20, self.quantity, self.black, 310, 370)
        self.texte(20, self.id_category, self.black, 470, 270)

    def image1(self):
        self.screen.fill(self.back_color)
        self.text_c5("add product",self.black,310,8)
        pygame.draw.line(self.screen,self.red,(200,32),(600,32),1)
        self.text_c3("ADD PRODUCT",self.red,200,38)
        pygame.draw.line(self.screen,self.red,(200,88),(600,88),1)
        self.image("trace","img/menu13.png",800,120,0,280)

    def display_design(self):
        self.image1()
        rect = pygame.Rect(200, 180, 400, 300)
        pygame.draw.rect(self.screen, self.white, rect)
        pygame.draw.rect(self.screen, self.black, rect, 2)
        self.text_center3("Name", self.black, rect, 90, 100) 
        self.text_center3("Price", self.black, rect, -80, 0)
        self.text_center3("Quantity", self.black, rect, 90, 0)        
        self.text_center3("Description", self.black, rect, 0, -80)
        self.text_center3("Category  1 or 2", self.black, rect, -80, 100)
        self.input()
        self.text()

    def run(self):
        self.add_running = True
        while self.add_running:
            self.display_design()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.add_running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_name.collidepoint(event.pos):
                        self.entry = 1
                    elif self.input_description.collidepoint(event.pos):
                        self.entry = 2
                    elif self.input_price.collidepoint(event.pos):
                        self.entry = 3
                    elif self.input_quantity.collidepoint(event.pos):
                        self.entry = 4
                    elif self.input_id_category.collidepoint(event.pos):
                        self.entry = 5

                elif event.type == pygame.KEYDOWN:
                    if self.entry == 1:
                        if event.unicode.isalpha():
                            self.name = self.name + event.unicode
                            self.name = self.name.capitalize()
                        if event.key == pygame.K_BACKSPACE:
                            self.name = self.name[:-1]

                    elif self.entry == 2:
                        if event.unicode:
                            self.description = self.description + event.unicode
                            self.description = self.description.capitalize()
                        if event.key == pygame.K_BACKSPACE:
                            self.description = self.description[:-1]

                    elif self.entry == 3:
                        if event.unicode.isdigit():
                            self.price = self.price + event.unicode
                        if event.key == pygame.K_BACKSPACE:
                            self.price = self.price[:-1]
                            
                    elif self.entry == 4:
                        if event.unicode.isdigit():
                            self.quantity = self.quantity + event.unicode
                        if event.key == pygame.K_BACKSPACE:
                            self.quantity = self.quantity[:-1]
                            
                    elif self.entry == 5:
                        if event.unicode.isdigit():
                            self.id_category = self.id_category + event.unicode
                        if event.key == pygame.K_BACKSPACE:
                            self.id_category = self.id_category[:-1]
            if (
                self.name != ""
                and self.description != ""
                and self.quantity != ""
                and self.price != ""
                and self.id_category != ""
                and self.id_category in ["1", "2"]
            ):
                self.check = self.image("check","img/menu21.png",90,99,370,480)
                if event.type == pygame.MOUSEBUTTONDOWN and self.add_time==0:
                    if self.check.collidepoint(event.pos):
                        self.check_v = True
                        self.check = self.image("check","img/menu25.png",100,109,370,480)
                        self.manager.add_product(self.name,self.description,self.price,self.quantity,self.id_category)
                        self.add_time = 1
                if self.check_v:
                    self.check = self.image("check","img/menu25.png",90,99,370,480)
                        
            pygame.display.flip()
            pygame.display.update()

# food = Add()
# food.run()