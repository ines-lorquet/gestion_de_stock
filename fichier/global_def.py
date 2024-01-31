import pygame
class Global:

    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Pokémon")
        self.clock = pygame.time.Clock()
        self.white = "#ffffff"
        self.beige = "#f5d3b8"
        self.grey = "#3c3c3c"   
        self.orange = "#ff6702"
        self.black = "#0e0f10"
        self.blue = "#375daa"
        self.yellow = "#ffcc01"
        self.green = "#488030"
        self.brown = "#e09828"
        self.pink = "#f8a8b0"
        self.red = "#dd2b2b"
        self.green2 = "#61e002"
        self.sushi1 = pygame.image.load("img/menu6.png")
        self.sushi2 = pygame.image.load("img/menu7.png")
        self.sushi3 = pygame.image.load("img/menu8.png")
        self.sushi4 = pygame.image.load("img/menu9.png")
        self.sushi5 = pygame.image.load("img/menu10.png")
        self.sushi6 = pygame.image.load("img/menu11.png")
        self.sushi7 = pygame.image.load("img/menu12.png")
        self.police_c1 = pygame.font.Font("JAPAB___.TTF",10)
        self.police_c2 = pygame.font.Font("Neug Asia.ttf",30)  
        self.police_c3 = pygame.font.Font("Neug Asia.ttf",50)
        self.police_c5 = pygame.font.Font("Japanese.ttf",20)
        self.police_c4 = pygame.font.Font("JAPAB___.TTF",80)

        
#def text  
    def text_c1(self,text, color, x, y):
        text_surface = self.police_c1.render(text, True, color)
        self.screen.blit(text_surface, (x, y))

    def text_c2(self,text, color, x, y):
        text_surface = self.police_c2.render(text, True, color)
        self.screen.blit(text_surface, (x, y))

    def text_c3(self,text, color, x, y):
        text_surface = self.police_c3.render(text, True, color)
        self.screen.blit(text_surface, (x, y))

    def text_c4(self,text, color, x, y):
        text_surface = self.police_c4.render(text, True, color)
        self.screen.blit(text_surface, (x, y))
        
    def text_c5(self,text, color, x, y):
        text_surface = self.police_c5.render(text, True, color)
        self.screen.blit(text_surface, (x, y))

#def image
    def image(self,name,path,a,b,x,y):
        name = pygame.image.load(path)
        name = name.convert_alpha()
        name = pygame.transform.scale(name,(a,b))        
        self.screen.blit(name,(x,y))
        
    def img_back(self,name,path):
        name =  pygame.image.load(path).convert_alpha()
        L_name, H_name = name.get_size()
        name = pygame.transform.scale(name, (L_name,H_name))
        x =(self.screen_width - L_name)//2
        y = (self.screen_height - H_name)//2
        self.screen.blit(name, (x, y))
    
# def rectangle   
             
        # Rectangle 
    def rect(self,nom, x1,y1,x2,y2):   
        nom = pygame.Rect(x1,y1,x2,y2)

              # Rectangle Radius
    def rect_radius(self,radius,color,x1,y1,x2,y2):
        r = radius
        pygame.draw.rect(self.screen,color,(x1,y1,x2,y2),border_radius = r)


"""
CREATE DATABASE LaPlateforme2;

USE LaPlateforme2;

CREATE TABLE product (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    description TEXT,
    price INT,
    quantity INT,
    id_category INT
    );
    
DESCRIBE product;

CREATE TABLE category (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255)
    );
    
DESCRIBE category;

INSERT INTO product(name,description,price,quantity,id_category) VALUES
('Jambon','Le Jambon Fumé, cuisse entière du cochon.', 3,100,1),
('Chorizo','Chorizo sec de boeuf et de porc fait maison', 4, 50, 1),
('Saucisson','Saucisson sec enrobé aux herbes', 4, 120, 1),
('Bacon','Bacon Fumé au bois de hêtre', 2, 200, 1),
('Salami','Salami de volaille à la graisse végétale', 3, 20, 1),
('Ice Tea',' Ice Tea saveur pêche', 2, 300, 2);

SELECT * FROM product;

UPDATE product
SET description = 'Chorizo sec de boeuf et de porc fait maison'
WHERE id = 2;

INSERT INTO category (name) VALUES
('Charcuterie'),
('Boisson'),
('Fromage');

SELECT * FROM category;

SELECT employe.nom, employe.prenom, employe.salaire, service.nom as service
FROM employe
JOIN service ON employe.id_service = service.id

"""
