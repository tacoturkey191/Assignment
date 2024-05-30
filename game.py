import pygame
import sqlite3
pygame.init




# this name implies 4 other games and at least one other edition. 
# of course, these games do not exist, and i think that's funny.
pygame.display.set_caption('Space Runner 5: Ultimate Edition')




class datastore():
    def __init__(self):
        self.conn = sqlite3.connect("Assignment.db")
        self.cur = self.conn.cursor()

        sql = """CREATE TABLE IF NOT EXISTS
                users(userid INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)"""
        self.cur.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS
                    scores(scoreid INTEGER PRIMARY KEY  AUTOINCREMENT,
                    username TEXT, score INTEGER)"""
        self.cur.execute(sql)

    def users_to_db(self, username, password):
        print("users to db method called")
        self.cur.execute(
            """
                INSERT INTO users(username, password)
                VALUES (:Username, :Password)

            """,
            {
                'Username':username,
                'Password':password
            }
        )
        self.conn.commit

    def login_check(self, user, pw):
        results = self.cur.execute("""
                SELECT userid from users
                WHERE username = :username
                AND password = :password
                """,
                {
                    'username':user,
                    'password':pw
                }
            )
        rows = results.fetchall()
        print(rows)
        self.id = rows[0][0]
        print(self.id)



ds = datastore()
ds.users_to_db("Tom", "secret")

username = input('Username: ')
password = input('Password: ')
user = ds.login_check(username, password)
win = pygame.display.set_mode((1212, 608))
bg = pygame.image.load('bg.png')
animation = [pygame.image.load('player_ship0.png'), pygame.image.load('player_ship1.png'),pygame.image.load('player_ship2.png')]


# player class
class player(object):
    
    def __init__(self,x,y,width,height,):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.flyCount = -1
       
# this is so pygame knows what to draw
    def draw(self, win):
        if self.flyCount >= 2:
            self.flyCount = -1
        self.flyCount += 1
        win.blit(animation[self.flyCount], (self.x,self.y))

class midEnemy(object):
    def __init__(self,x,y,width,height, end, ):
        self.x = x
        self.y = y
        self.aniCount = -1
        self.end = end 
        self.path = [self.x, self.y, end]
        self.width = width
        self.height = height
        self.animation = [pygame.image.load("enemy_ship0.png")]




def redrawGameWindow():
    win.blit(bg, (0,0))
    ship.draw(win)

    pygame.display.update()
    

# variables
run = True
ship = player(500, 300, 32, 32)
# main loop:
while run:

    #closes the game safely
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Movement controls
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        ship.y -= ship.vel
    if keys[pygame.K_DOWN]:
        ship.y += ship.vel
    if keys[pygame.K_LEFT]:
        ship.x -= ship.vel
    if keys[pygame.K_RIGHT]:
        ship.x += ship.vel


    # calls the code we wrote before that blits objects onto the window.
    redrawGameWindow()


pygame.quit







