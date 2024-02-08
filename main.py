import pygame
import sys
from fichier.global_def import Global
from fichier.add import Add
from fichier.product import Product

class Menu(Global): 

    def __init__(self): 
        Global.__init__(self)
        self.product = Product()
        self.add = Add()
        self.running = True
        self.add_time = 0

    def menu_run(self):
        self.options_menu()       
      
    def rect_white_menu(self, rect, text, pos):
        
        menu_text = self.police_c2.render(text, True, self.black)
        if rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.screen, self.white, rect.inflate(10, 10), border_radius=10)
            if pos==(430 - 100, 255 + 0 * 65, 220, 50):
                self.image("baguette",r"img/menu2.png",90,119,200,190)
                self.text_c5("product",self.black,350,285)
            elif pos==(470 - 100, 255 + 1 * 65, 220, 50):
                self.image("baguette",r"img/menu2.png",90,119,200,255)
                self.text_c5("add",self.black,375,350)
            elif pos==(467- 100, 250 + 2 * 65, 220, 50):
                self.image("baguette",r"img/menu2.png",90,119,200,320)
                self.text_c5("quit",self.black,370,415)
        else:
            pygame.draw.rect(self.screen, self.white, rect, border_radius=10)
        self.screen.blit(menu_text, pos) 
        
    def title(self):
        pygame.draw.line(self.screen,self.red,(190,88),(630,88),1)
        pygame.draw.line(self.screen,self.red,(190,32),(630,32),1)
        self.image("trace",r"img/menu3.png",150,500,330,0)
        self.image("tapis",r"img/menu5.png",800,100,0,500)
        self.text_c3("SHOP",self.red,190,38)
        self.text_c3("SUSHI",self.red,480,38)
        

    def deplacer_image(self,image, x, y):
        self.screen.blit(image, (x, y))
        
    def options_menu(self):
        self.running = True
        img_back = pygame.image.load(r"img/menu1.jpg").convert()
        tour = pygame.time.Clock()
        image_x = -400 
        image_x2 = image_x-800
        image_x3 = image_x-1200
        image_x4 = image_x-1600
        image_x5 = image_x-2000
        image_x6 = image_x-2400
        image_x7 = image_x-2800

        option_rects = [
            pygame.Rect(self.screen_width // 2 - 100, 250 + i * 65, 220, 50) for i in range(4)
        ]
        option_texts = ["PRODUCT", "ADD", "QUIT"]
        image_x = -400 
        while self.running:
            self.screen.blit(img_back, (0, 0))     
            self.image("assiette",r"img/menu4.png",239,230,-90,250)
            self.image("assiette",r"img/menu4.png",239,230,670,250)
            
            self.title()
            for i, (rect, text) in enumerate(zip(option_rects, option_texts)):
                if text == "PRODUCT":
                    position = (430 - 100, 255 + i * 65, 220, 50)
                elif text == "ADD":
                    position = (470 - 100, 255 + i * 65, 220, 50)
                else:
                    position = (467- 100, 250 + i * 65, 220, 50)

                self.rect_white_menu(rect, text, position)                
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for i, item in enumerate(option_texts):
                        rect = option_rects[i]
                        if rect.collidepoint(mouse_pos):
                            if item == "PRODUCT":
                                self.product.product_running = True
                                self.product.product_run()
                            elif item == "ADD":
                                self.add.add_running = True
                                self.add.run()
                            elif item == "QUIT":
                                pygame.quit()
                                sys.exit()

            self.deplacer_image(self.sushi1, image_x, 500)
            self.deplacer_image(self.sushi2, image_x2, 500)
            self.deplacer_image(self.sushi3, image_x3, 500)           
            self.deplacer_image(self.sushi4, image_x4, 500)
            self.deplacer_image(self.sushi5, image_x5, 500)
            self.deplacer_image(self.sushi6, image_x6, 500)
            self.deplacer_image(self.sushi7, image_x7, 500)
            image_x += 7
            image_x2 += 7
            image_x3 += 7
            image_x4 += 7
            image_x5 += 7
            image_x6 += 7
            image_x7 += 7
            tour.tick(100)
            
            if image_x7 > self.screen_width:
                image_x = -400 
                image_x2 = image_x-800
                image_x3 = image_x-1200
                image_x4 = image_x-1600
                image_x5 = image_x-2000
                image_x6 = image_x-2400
                image_x7 = image_x-2800

            pygame.display.update()
            self.clock.tick(60)

test_menu = Menu()
test_menu.menu_run()



# CREATE DATABASE store;
# SHOW Databases;

# USE store;

# CREATE TABLE product(
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     name VARCHAR(255),
#     description TEXT,
#     price INT,
#     quantity INT,
#     id_category INT 
#     );

# SHOW COLUMNS
# FROM product;

# INSERT INTO product(name,description,price,quantity,id_category) VALUES
# ('Maki-sushi', "Rouleau de riz farci enroulés d'algue nori séchée", 8, 30,1),
# ('Sashimi',"Tranches de poisson cru.", 6, 50,1),
# ('Uramaki',"Momposé de saumon et d'avocat", 8, 40,1),
# ('Temaki-sushi',"Riz, fruits de mer et poissons cuits enfermés dans un cône", 20, 10,1),
# ('Sauce Soja', 'Mélange de soja et de blé', 2, 100, 1);

# SELECT *
# FROM product;

# CREATE TABLE category (
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     name VARCHAR(255)
#     ); 

# SHOW COLUMNS
# FROM category;

# INSERT INTO category(name) VALUES
# ('Sushi'),
# ('Sauce')
# ; 

# SELECT *
# FROM category; 

# SELECT employe.nom, employe.prenom, employe.salaire, service.nom as service
# FROM employe
# JOIN service ON employe.id_service = service.id

# UPDATE product 
# SET id_category = 2
# WHERE id = 5;
