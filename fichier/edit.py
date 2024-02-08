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
        self.rectangles_position = 300
        self.img_back = pygame.image.load(r"img/menu1.jpg")
        self.screen = pygame.display.set_mode((self.width, self.height))

    # def draw_rectangles(self, x_position):
    #     sql = "SELECT COUNT(*) AS nb FROM product"
    #     self.cursor.execute(sql)
    #     nb = self.cursor.fetchone()
    #     name_product = self.manager.name_product()
        
    #     if nb:
    #         nb = nb[0]
    #         for i in range(nb):
    #             rect = pygame.Rect(x_position + i * (self.rect_width + 70), self.height // 2 - self.rect_height // 2, self.rect_width, self.rect_height)
    #             pygame.draw.rect(self.screen, self.rect_color, rect)
    #             str_name = name_product[i][0]
    #             result = str_name + ' '
    #             text_surface = self.police_c2.render(result, True, self.black)
    #             text_rect = text_surface.get_rect()
    #             text_rect.center = (rect.centerx, rect.centery)
    #             self.screen.blit(text_surface, text_rect)
    
    def draw_rectangles(self, x_position):
        sql = "SELECT COUNT(*) AS nb FROM product"
        self.cursor.execute(sql)
        nb = self.cursor.fetchone()
        name_product = self.manager.name_product()

        if nb:
            nb = nb[0]
            for i in range(nb):
                rect = pygame.Rect(x_position + i * (self.rect_width + 70), self.height // 2 - self.rect_height // 2, self.rect_width, self.rect_height)
                pygame.draw.rect(self.screen, self.rect_color, rect)
                str_name = name_product[i][0]
                result = str_name + ' '
                text_surface = self.police_c2.render(result, True, self.black)
                text_rect = text_surface.get_rect()
                text_rect.center = (rect.centerx, rect.centery)
                self.screen.blit(text_surface, text_rect)

                if rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    pygame.quit()
                    sys.exit()

    def image(self):
        self.text_c5("product",self.black,340,8)
        pygame.draw.line(self.screen,self.red,(270,32),(530,32),1)
        self.text_c3("PRODUCT",self.red,270,38)
        pygame.draw.line(self.screen,self.red,(270,88),(530,88),1)

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
            self.draw_rectangles(self.rectangles_position)
            self.image()
            pygame.display.flip()
            pygame.time.Clock().tick(60)
            
# run=Product()
# run.product_run()