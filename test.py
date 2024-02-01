import mysql.connector
import pygame
import sys
from product_manager import Product_Manager
from global_def import Global
pygame.init()

class Product(Global): 
    def __init__(self):
        Global.__init__(self) 
        self.connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="azerty",
        database="store"
        )
        self.cursor = self.connection.cursor()
        self.manager = Product_Manager()
        self.width, self.height = 800, 600
        self.rect_color = self.white
        self.rect_width = 300
        self.rect_height = 100
        self.rect_speed = 100
        self.num_rectangles = 5
        self.rectangles_position = 260
        self.img_back = pygame.image.load(r"img/menu1.jpg")
        self.screen = pygame.display.set_mode((self.width, self.height))

    
    def draw_rectangles(self, x_position):
        sql = "SELECT COUNT(*) AS nb FROM product"
        self.cursor.execute(sql)
        nb = self.cursor.fetchone()
        name_product = self.manager.name_product()
        description_product = self.manager.description_product()

        # Créer un dictionnaire associant chaque rectangle à son image respective
        images = {
            0: pygame.image.load("img/menu15.png"),
            1: pygame.image.load("img/menu16.png"), 
            2: pygame.image.load("img/menu17.png"), 
            3: pygame.image.load("img/menu18.png"), 
            4: pygame.image.load("img/menu16.png"), 
        }

        if nb:
            nb = nb[0]
            for i in range(nb):
                rect = pygame.Rect(x_position + i * (self.rect_width + 70), self.height // 2 - self.rect_height // 2, self.rect_width, self.rect_height)
                pygame.draw.rect(self.screen, self.rect_color, rect)

                str_name = name_product[i][0]
                result1 = str_name + ' '
                str_name = description_product[i][0]
                result2 = str_name + ' '
                rect2 = pygame.Rect(230, 450, 300, 20)

                if rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.rect(self.screen, self.black, rect, 2)
                    self.text_center1(result2, self.back_color, rect2, 0)
                    if i in images:
                        image = images[i]
                        image = pygame.transform.scale(image,(110,119))    
                        self.screen.blit(image, (300, 100))
                self.text_center2(result1, self.black, rect, 0)



    def image1(self):
        self.text_c5("product",self.black,340,8)
        pygame.draw.line(self.screen,self.red,(270,32),(530,32),1)
        self.text_c3("PRODUCT",self.red,270,38)
        pygame.draw.line(self.screen,self.red,(270,88),(530,88),1)
        name = pygame.image.load(r"img/menu13.png")
        name = name.convert_alpha()
        name = pygame.transform.scale(name,(800,120))        
        self.screen.blit(name,(0,400))

    def product_run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.rectangles_position += self.rect_speed
                    elif event.key == pygame.K_LEFT:
                        self.rectangles_position -= self.rect_speed
                        
            self.screen.fill(self.back_color)
            self.image1()
            self.draw_rectangles(self.rectangles_position)
            
            pygame.display.flip()
            pygame.time.Clock().tick(60)
            
run=Product()
run.product_run()