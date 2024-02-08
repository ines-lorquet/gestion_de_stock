import mysql.connector
import pygame
from global_def import Global
from product_manager import Product_Manager

class Food(Global):
    def __init__(self):
        Global.__init__(self)
        self.manager = Product_Manager()
        self.name = ""
        self.description = ""
        self.price = ""
        self.quantity = ""
        self.id_category = ""
        self.entry = 0

        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="azerty",
            database="store"
        )
        self.cursor = self.connection.cursor()

        pygame.init()

    def rect(self, color, x1, y1, x2, y2):   
        return pygame.Rect(x1, y1, x2, y2), color

    def input(self):
        self.input_name = pygame.draw.rect(self.screen, self.black, (250, 250, 120, 40), 2)
        self.input_description = pygame.draw.rect(self.screen, self.black, (210, 430, 380, 40), 2)
        self.input_price = pygame.draw.rect(self.screen, self.black, (420, 345, 120, 40), 2)
        self.input_quantity = pygame.draw.rect(self.screen, self.black, (250, 345, 120, 40), 2)
        self.input_id_category= pygame.draw.rect(self.screen, self.black, (420, 250, 120, 40), 2)
        # self.check= self.rect2(self.screen,self.red, 400, 390, 700,60)
        
    def text(self):
        self.texte(20, self.name, self.red, 300, 270)
        self.texte(20, self.description, self.red, 400, 450)
        self.texte(20, self.price, self.red,420, 345)
        self.texte(20, self.quantity, self.red, 250, 345)
        self.texte(20, self.id_category, self.red, 420, 250)
        
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
        en_cours = True
        while en_cours:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    en_cours = False
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
                    elif self.check.collidepoint(event.pos):
                        if self.name != "" and self.description != "" and self.price != "" and self.quantity != "" and self.id_category != "":
                            self.manager.add_product(self.name, self.description, self.price, self.quantity, self.id_category)

                elif event.type == pygame.KEYDOWN:
                    if self.entry == 1:
                        if event.unicode.isalpha():
                            self.name = self.name + event.unicode
                            self.name = self.name.capitalize()
                    elif self.entry == 2:
                        if event.unicode.isalpha():
                            self.description = self.description + event.unicode
                            self.description = self.description.capitalize()
                    elif self.entry == 3:
                        if event.unicode.isdigit():
                            self.price = self.price + event.unicode
                    elif self.entry == 4:
                        if event.unicode.isdigit():
                            self.quantity = self.quantity + event.unicode
                    elif self.entry == 5:
                        if event.unicode.isdigit():
                            self.id_category = self.id_category + event.unicode

            self.display_design()
            
            pygame.display.flip()
            pygame.display.update()

food = Food()
food.run()
