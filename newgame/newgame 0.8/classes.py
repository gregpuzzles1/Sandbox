import rooms, images, fonts
import pickle
from random import choice

title=images.title
logo=images.logo
end=images.end

class Master(object):
    def startgame(self):
        self.room=-1
        self.nextroom()
    def nextroom(self):
        self.room+=1
        if self.maxroom<self.room:
            self.maxroom=self.room
        self.walls=[]
        self.exits=[]
        self.spikes=[]
        self.lasers=[]
        self.fires=[]
        self.buttons=[]
        self.bumpers=[]
        self.platforms=[]
        try:
            for y in range(20):
                for x in range(30):
                    if rooms.levels[self.room][y][x]==1:
                        self.walls.append(Wall(20*x, 20*y))
                    elif rooms.levels[self.room][y][x]==2:
                        self.exits.append(Exit(20*x, 20*y))
                    elif rooms.levels[self.room][y][x]==3:
                        self.spikes.append(Spike(20*x, 20*y))
                    elif rooms.levels[self.room][y][x]==4:
                        self.lasers.append(Laser(20*x, 20*y))
                    elif rooms.levels[self.room][y][x]==5:
                        self.buttons.append(Button(20*x, 20*y))
                    elif rooms.levels[self.room][y][x]==6:
                        self.bumpers.append(Bumper(20*x, 20*y))
                    elif rooms.levels[self.room][y][x]==7:
                        self.fires.append(Fire(20*x, 20*y))
                    elif rooms.levels[self.room][y][x]==10:
                        self.start=(20*x, 20*y)
                    elif rooms.levels[self.room][y][x]==11:
                        self.platforms.append(Platform(20*x, 20*y, -2))
                    elif rooms.levels[self.room][y][x]==12:
                        self.platforms.append(Platform(20*x, 20*y, 2))
            self.player=Player(self.start)
        except IndexError:
            self.win()
    def die(self):
        self.player.img=images.dead
        self.mode=2
        self.waiting=20
        self.deaths+=1
        self.render_scores()
        self.save()
    def render_scores(self):
        self.img_beaten=fonts.normal.render("Levels beaten: "+str(self.maxroom),
                                            1, (80, 80, 150))
        self.img_deaths=fonts.normal.render("Deaths: "+str(self.deaths), 1,
                                         (80, 80, 150))
    def load(self):
        exist=True
        try:
            f=open(".score.obj", 'rb')
        except IOError:
            exist=False
        if exist:
            (self.maxroom, self.deaths)=pickle.load(f)
            f.close()
    def save(self):
        f=open(".score.obj", 'wb')
        pickle.dump((self.maxroom, self.deaths), f, -1)
        f.close()
    def win(self):
        self.mode=3
        self.waiting=20
        self.render_scores()
        self.save()

class Player(object):
    def __init__(self, (x, y)):
        self.x=x
        self.y=y
        self.w=20
        self.h=20
        self.hspeed=0
        self.hspeed2=0
        self.maxhspeed=5
        self.vspeed=0
        self.jumpspeed=-14
        self.maxfallspeed=20
        self.gravity=1
        self.jumping=0
        self.img=images.player
    def accelarate_left(self):
        if self.hspeed>-self.maxhspeed:
            self.hspeed-=1
    def slow_left(self):
        if self.hspeed<0:
            self.hspeed+=1
    def accelarate_right(self):
        if self.hspeed<self.maxhspeed:
            self.hspeed+=1
    def slow_right(self):
        if self.hspeed>0:
            self.hspeed-=1
    def jump(self):
        self.vspeed=self.jumpspeed
        self.jumping=1
    def stopjump(self):
        self.vspeed/=2
        self.jumping=0
        
class Wall(object):
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.w=20
        self.h=20
        self.img=images.wall
        
class Exit(object):
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.w=20
        self.h=20
        self.img=images.exit
        
class Spike(object):
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.w=20
        self.h=20
        self.img=images.spike
        
class Fire(object):
    def __init__(self, x, y):
        self.x=x+6
        self.y=y+6
        self.w=8
        self.h=8
        self.maxhspeed=choice((-1, 1))*4
        self.maxvspeed=choice((-1, 1))*4
        self.hspeed=self.maxhspeed
        self.vspeed=self.maxvspeed
        self.img=images.fire
        
class Platform(object):
    def __init__(self, x, y, v):
        self.x=x
        self.y=y
        self.maxv=-v
        self.v=0
        self.w=20
        self.h=20
        self.img=images.platform
    def accelarate(self):
        if self.v==0:
            self.maxv*=-1
        if self.v<self.maxv:
            self.v+=1
        elif self.v>self.maxv:
            self.v-=1

class Laser(object):
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.w=20
        self.h=20
        self.peace=0
        self.img=images.laser
    def peaceful(self):
        if self.peace>0:
            self.peace-=1
            
class Button(object):
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.w=20
        self.h=20
        self.img=images.button
        
class Bumper(object):
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.w=20
        self.h=20
        self.img=images.bumper