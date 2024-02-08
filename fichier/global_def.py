import pygame
class Global:

    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Shop Sushi")
        self.clock = pygame.time.Clock()
        self.back_color = "#e4dfcc"
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
        self.police_c1 = pygame.font.Font("Neug Asia.ttf",20)
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

    # def image(self,name,path,a,b,x,y):
    #     name = pygame.image.load(path)
    #     name = name.convert_alpha()
    #     name = pygame.transform.scale(name,(a,b))        
    #     self.screen.blit(name,(x,y))
    def image(self, name, path, width, height, x, y):
        image = pygame.image.load(path)
        image = pygame.transform.scale(image, (width, height))
        rect = image.get_rect(topleft=(x, y))
        self.screen.blit(image, rect)
        return rect

    def text_center2(self,text,color,rect,nb):
        text_surface = self.police_c2.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (rect.centerx, rect.centery - nb)
        self.screen.blit(text_surface, text_rect)
        
    def text_center1(self,text,color,rect,nb):
        text_surface = self.police_c1.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (rect.centerx, rect.centery - nb)
        self.screen.blit(text_surface, text_rect)
        
    def text_center3(self,text,color,rect,nb1,nb2):
        text_surface = self.police_c1.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (rect.centerx - nb1, rect.centery - nb2)
        self.screen.blit(text_surface, text_rect)

    def texte(self, texte_size, texte_content, color, x, y):
        pygame.font.init()   # modifier police
        Texte = pygame.font.Font("Neug Asia.ttf", texte_size).render(texte_content, True, color)
        Texte_rect = Texte.get_rect(center=(x, y))
        self.screen.blit(Texte, Texte_rect)
        
    def rect(self,nom, x1,y1,x2,y2):   
        nom = pygame.Rect(x1,y1,x2,y2)
    
    def rect2(self,surface, color, x1, y1, x2, y2):   
        rect = pygame.Rect(x1,y1,x2,y2)
        pygame.draw.rect(surface, color, rect)
        return rect
    #           # Rectangle Radius
    # def rect_radius(self,radius,color,x1,y1,x2,y2):
    #     r = radius
    #     pygame.draw.rect(self.screen,color,(x1,y1,x2,y2),border_radius = r)

    # def img_back(self,name,path):
    #     name =  pygame.image.load(path).convert_alpha()
    #     L_name, H_name = name.get_size()
    #     name = pygame.transform.scale(name, (L_name,H_name))
    #     x =(self.screen_width - L_name)//2
    #     y = (self.screen_height - H_name)//2
    #     self.screen.blit(name, (x, y))