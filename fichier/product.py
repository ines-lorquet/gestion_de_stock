import mysql.connector
import pygame
import sys
from fichier.product_manager import Product_Manager
from fichier.global_def import Global
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
        self.img_back = pygame.image.load(r"img/menu1.png")
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.product_running = True
        self.new_quantity = ""
        self.new_price = ""
        self.entry_change = 0
    
    def draw_rectangles(self, x_param):
        sql = "SELECT COUNT(*) AS nb FROM product"
        self.cursor.execute(sql)
        nb = self.cursor.fetchone()
        name_product = self.manager.name_product()
        description_product = self.manager.description_product()
        quantity_product = self.manager.quantity_product()
        price_product = self.manager.price_product()
        self.modify = self.manager.id_product()

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
                self.bin = self.image("bin","img/menu22.png",40,49,x_param + i * (self.rect_width + 200)+400,300)
                self.pen = self.image("pen","img/menu2.jpg",40,49,x_param + i * (self.rect_width + 200)+400,350)
                
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
                str_name6 = self.modify[i][0]
                str_name6 = str(str_name6)
                result6 = str_name6 + ' '
                
                # Nombre / total produit
                self.text_center3(str(i+1),self.black,rect,-140,130)
                self.text_center3("/",self.black,rect,-160,130)
                self.text_center3(str(nb),self.black,rect,-180,130)
                
                # Passage souris sur le rectangle
                if rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.rect(self.screen, self.black, rect, 2)
                    self.text_center1(result2, self.white, rect2, -70)
                    if (
                        self.new_price != ""
                        and self.new_quantity != ""
                    ):
                        
                        self.new = True
                    
                    # Affichage Image Produit
                    if i in images:
                        image = images[i]
                        image = pygame.transform.scale(image,(80,79))
                        self.screen.blit(image, (x_param + i * (self.rect_width + 200), 170))
                        
                for event in pygame.event.get():
                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        
                        if self.pen.collidepoint(event.pos) and self.new==True:
                            # print("id = ", result6)
                            self.manager.modify_product(result6,self.new_price,self.new_quantity)
                            
                        if self.bin.collidepoint(event.pos):
                            self.bin =self.image("bin","img/menu22.png",400,409,x_param + i * (self.rect_width + 200),390)
                            self.delete_nb = self.manager.id_product()
                            str_name5 = self.delete_nb[i][0]
                            str_name5 = str(str_name5)
                            result5 = str_name5 + ' '
                            # print(result5)
                            self.manager.delete_product(result5)
                            
                        if self.change_p_rect.collidepoint(event.pos):
                            self.change_p_rect = pygame.draw.rect(self.screen, self.grey, (x_param + i * (self.rect_width + 200)+220, 400, 120, 40))
                            print("price")
                            self.entry_change = 1
                        else:
                            self.change_p_rect = pygame.draw.rect(self.screen, self.white, (x_param + i * (self.rect_width + 200)+220, 400, 120, 40))
                            
                        if self.change_q_rect.collidepoint(event.pos):
                            self.change_q_rect = pygame.draw.rect(self.screen, self.grey, (x_param + i * (self.rect_width + 200)+50, 400, 120, 40))
                            print("quantity")
                            self.entry_change = 2
                        else:
                            self.change_q_rect = pygame.draw.rect(self.screen, self.white, (x_param + i * (self.rect_width + 200)+50, 400, 120, 40))
                            
                    elif event.type == pygame.KEYDOWN:
                        if self.entry_change == 1:
                            if event.unicode.isdigit():
                                self.new_price = self.new_price + event.unicode
                            if event.key == pygame.K_BACKSPACE:
                                self.new_price = self.new_price[:-1]

                        elif self.entry_change == 2:
                            if event.unicode.isdigit():
                                self.new_quantity = self.new_quantity + event.unicode
                            if event.key == pygame.K_BACKSPACE:
                                self.new_quantity = self.new_quantity[:-1]


                self.text_center2(result1, self.black, rect, 90)

                #Rectangle quantité et prix
                #Prix
                self.text_center3("Price", self.black, rect, -80,0)
                pygame.draw.rect(self.screen, self.black, (x_param + i * (self.rect_width + 200)+50, 320, 120, 40),2)
                self.text_center3(str(result4),self.black,rect,-85,-43)

                self.text_center3("Change P", self.black, rect, -80,-85)
                self.change_q_rect = pygame.draw.rect(self.screen, self.white, (x_param + i * (self.rect_width + 200)+50, 400, 120, 40))
                pygame.draw.rect(self.screen, self.black, (x_param + i * (self.rect_width + 200)+50, 400, 120, 40),2)
                self.text_center3(self.new_price,self.black,rect,-85,-120)

                #Quantité
                self.text_center3("Quantity", self.black, rect, 90,0)
                rect3 = pygame.draw.rect(self.screen, self.black, (x_param + i * (self.rect_width + 200)+220, 320, 120, 40),2)
                self.text_center3(str(result3),self.black,rect,85,-43)

                self.text_center3("Change Q", self.black, rect, 90,-85)
                self.change_p_rect = pygame.draw.rect(self.screen, self.black, (x_param + i * (self.rect_width + 200)+220, 400, 120, 40),2)
                self.text_center3(self.new_quantity,self.black,rect,85,-120)
                
                self.right = self.image("baguette", r"img/menu23.png", 100, 119, 650, 65)
                self.left = self.image("baguette", r"img/menu24.png", 100, 119, 50, 65)
                
    def image1(self):
        self.text_c5("product",self.black,340,8)
        pygame.draw.line(self.screen,self.red,(270,32),(530,32),1)
        self.text_c3("PRODUCT",self.red,270,38)
        pygame.draw.line(self.screen,self.red,(270,88),(530,88),1)
        self.image("trace","img/menu13.png",800,120,0,470)
        self.back = self.text_c1("BACK",self.red,720,15)
        self.table_back =self.image("table quit","img/menu26.png",100,59,700,30)
        
    def product_run(self):
        self.product_running = True
        while self.product_running:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.product_running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.right.collidepoint(event.pos):
                        self.rectangles_position -= self.rect_speed
                    elif self.left.collidepoint(event.pos):
                        self.rectangles_position += self.rect_speed
                    # elif self.back.collidepoint(event.pos) or self.table_back.collidepoint(event.pos):
                    #     self.product_running = False

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
            
# run=Product()
# run.product_run()