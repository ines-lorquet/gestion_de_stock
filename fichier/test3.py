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
        self.rect_width = 400
        self.rect_height = 300
        self.rect_speed = 300
        self.rectangles_position = 200
        self.img_back = pygame.image.load(r"img/menu1.jpg")
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.right = self.image("baguette", r"img/menu23.png", 100, 119, 650, 65)
        self.left = self.image("baguette", r"img/menu24.png", 100, 119, 50, 65)
    
    def draw_rectangles(self, x_param):
        sql = "SELECT COUNT(*) AS nb FROM product"
        self.cursor.execute(sql)
        nb = self.cursor.fetchone()
        name_product = self.manager.name_product()
        description_product = self.manager.description_product()
        quantity_product = self.manager.quantity_product()
        price_product = self.manager.price_product()

        images = {
            0: pygame.image.load("img/menu15.png"),
            1: pygame.image.load("img/menu16.png"), 
            2: pygame.image.load("img/menu17.png"), 
            3: pygame.image.load("img/menu18.png"), 
            4: pygame.image.load("img/menu19.png"), 
        }

        if nb:
            nb = nb[0]
            for i in range(nb):
                rect = pygame.Rect(x_param + i * (self.rect_width + 200), self.height // 2 - self.rect_height // 2, self.rect_width, self.rect_height)
                pygame.draw.rect(self.screen, self.rect_color, rect)
                self.bin =self.image("bin","img/menu22.png",40,49,x_param + i * (self.rect_width + 200)+400,390)
                bin_rect = pygame.Rect(x_param + i * (self.rect_width + 200) + 400, 390, 40, 49)
                if bin_rect.collidepoint(pygame.mouse.get_pos()):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:  # Vérifie si c'est un clic gauche
                            print("delete")
                            print(i)
                #Nom & Description produit 
                str_name1 = name_product[i][0]
                result1 = str_name1 + ' '
                str_name2 = description_product[i][0]
                result2 = str_name2 + ' '
                rect2 = pygame.Rect(230, 450, 300, 20)
                str_name3 = quantity_product[i][0]
                str_name3 = str(str_name3)
                result3 = str_name3 + ' '
                str_name4 = price_product[i][0]
                str_name4 = str(str_name4)
                result4 = str_name4 + ' '
                
                # Nombre / total produit
                self.text_center3(str(i+1),self.black,rect,-140,130)
                self.text_center3("/",self.black,rect,-160,130)
                self.text_center3(str(nb),self.black,rect,-180,130)
                
                #passage de la souris sur le rectangle
                if rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.rect(self.screen, self.black, rect, 2)
                    self.text_center1(result2, self.white, rect2, -70)
                    
               
                    
                    #Affichage Image Produit
                    if i in images:
                        image = images[i]
                        image = pygame.transform.scale(image,(80,79))
                        self.screen.blit(image, (x_param + i * (self.rect_width + 200), 170))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.bin.collidepoint(event.pos):
                            print("delete")
                            print(i)
                            # self.delete_nb = self.manager.display_product()
                            # self.manager.delete_product(self.delete_nb[nb])
                                   
                self.text_center2(result1, self.black, rect, 90)
                
                
                #Rectangle quantité et prix
                #Prix
                self.text_center3("Price", self.black, rect, -80,0)
                pygame.draw.rect(self.screen, self.black, (x_param + i * (self.rect_width + 200)+50, 320, 120, 40),2)
                self.text_center3(str(result4),self.black,rect,-85,-43)
                
                self.text_center3("Change P", self.black, rect, -80,-85)
                pygame.draw.rect(self.screen, self.black, (x_param + i * (self.rect_width + 200)+50, 400, 120, 40),2)
                
                #Quantité
                self.text_center3("Quantity", self.black, rect, 90,0)
                rect3 = pygame.draw.rect(self.screen, self.black, (x_param + i * (self.rect_width + 200)+220, 320, 120, 40),2)
                self.text_center3(str(result3),self.black,rect,85,-43)
                
                self.text_center3("Change Q", self.black, rect, 90,-85)
                pygame.draw.rect(self.screen, self.black, (x_param + i * (self.rect_width + 200)+220, 400, 120, 40),2)
                
                
    def image1(self):
        self.text_c5("product",self.black,340,8)
        pygame.draw.line(self.screen,self.red,(270,32),(530,32),1)
        self.text_c3("PRODUCT",self.red,270,38)
        pygame.draw.line(self.screen,self.red,(270,88),(530,88),1)
        self.image("trace","img/menu13.png",800,120,0,470)
        
    def product_run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.right.collidepoint(event.pos):
                        self.rectangles_position -= self.rect_speed
                    elif self.left.collidepoint(event.pos):
                        self.rectangles_position += self.rect_speed

            self.screen.fill(self.back_color)
            self.image1()
            self.draw_rectangles(self.rectangles_position)

            pygame.display.flip()
            pygame.time.Clock().tick(60)

run = Product()
run.product_run()