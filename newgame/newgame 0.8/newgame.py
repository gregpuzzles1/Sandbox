#!/usr/bin/env python
# -*- coding: ascii -*-
#
#newgame v.0.8 (08-11-2011) 
#copyright by Michail (michailgames.com)

import pygame, sys, os
import classes
from pygame.locals import *

try:
    os.environ['SDL_VIDEO_CENTERED']='1'
except:
    pass

pygame.init()

g=classes.Master()
g.width=600
g.height=400
g.clock=pygame.time.Clock()
g.mode=0
g.waiting=0
g.maxroom=0
g.deaths=0
g.load()
g.render_scores()
g.keys={"right":0, "left":0, "x":0}

#pygame.display.set_icon(data.images.icon)
g.window=pygame.display.set_mode((g.width, g.height))
pygame.display.set_caption("newgame")
g.screen=pygame.display.get_surface()
pygame.mouse.set_visible(False)

def input(events):
    for event in events:
        if event.type==KEYDOWN and event.key==K_x:
            g.keys["x"]=2
        if event.type==KEYUP and event.key==K_x:
            g.keys["x"]=0
        if event.type==KEYDOWN and event.key==K_LEFT:
            g.keys["left"]=2
        if event.type==KEYUP and event.key==K_LEFT:
            g.keys["left"]=0
        if event.type==KEYDOWN and event.key==K_RIGHT:
            g.keys["right"]=2
        if event.type==KEYUP and event.key==K_RIGHT:
            g.keys["right"]=0
        if event.type==QUIT:
            sys.exit(0)
        if g.mode==0:
            if event.type==KEYDOWN and event.key==27:
                sys.exit(0)
            elif event.type==KEYDOWN:
                g.mode=1
                g.startgame()
        if g.mode==1:
            if event.type==KEYDOWN and event.key==27:
                g.die()
        if g.mode==3 and g.waiting==0:
            if event.type==KEYDOWN:
                g.mode=0
            
def action():
    if g.mode==1:
        if g.keys["left"]>0:
            g.player.accelarate_left()
        else:
            g.player.slow_left()
        if g.keys["right"]>0:
            g.player.accelarate_right()
        else:
            g.player.slow_right()
        #vertical
        g.player.vspeed+=g.player.gravity
        if g.player.vspeed>g.player.maxfallspeed:
            g.player.vspeed=g.player.maxfallspeed
        for bumper in g.bumpers:
            if (g.player.x+g.player.w>bumper.x and g.player.x<bumper.x+bumper.w and
            g.player.y+g.player.h>bumper.y and g.player.y<bumper.y+bumper.h):
                g.player.vspeed=-20
                g.player.jumping=1
        if g.player.vspeed>=0:
            g.player.jumping=0
        for wall in g.walls+g.platforms:
            if g.player.x+g.player.w>wall.x and g.player.x<wall.x+wall.w:
                if g.player.vspeed>0:
                    if g.player.y+g.player.h<=wall.y:
                        if g.player.y+g.player.h+g.player.vspeed>wall.y:
                            g.player.vspeed=wall.y-g.player.y-g.player.h
        for wall in g.walls+g.platforms:
            if g.player.x+g.player.w>wall.x and g.player.x<wall.x+wall.w:
                if g.player.y+g.player.h==wall.y and g.keys["x"]==2:
                    g.player.jump()
        for wall in g.walls:
            if g.player.x+g.player.w>wall.x and g.player.x<wall.x+wall.w:
                if g.player.vspeed<0:
                    if g.player.y>wall.y:
                        if g.player.y+g.player.vspeed<wall.y+wall.h:
                            g.player.vspeed=wall.y+wall.h-g.player.y
        if g.keys["x"]==0 and g.player.jumping==1:
            g.player.stopjump()
        g.player.y+=g.player.vspeed
        for f in g.fires:
            if f.hspeed==0:
                    f.maxhspeed*=-1
                    f.hspeed=f.maxhspeed
            for wall in g.walls:
                if f.hspeed<0:
                    if f.y+f.h>wall.y and f.y<wall.y+wall.h:
                        if f.x>wall.x:
                            if f.x+f.hspeed<wall.x+wall.w:
                                f.hspeed=wall.x+wall.w-f.x
                elif f.hspeed>0:
                    if f.y+f.h>wall.y and f.y<wall.y+wall.h:
                        if f.x<wall.x:
                            if f.x+f.w+f.hspeed>wall.x:
                                f.hspeed=wall.x-f.x-f.w
            f.x+=f.hspeed
            if f.vspeed==0:
                    f.maxvspeed*=-1
                    f.vspeed=f.maxvspeed
            for wall in g.walls:
                if f.vspeed<0:
                        if f.x+f.w>wall.x and f.x<wall.x+wall.w:
                            if f.y>wall.y:
                                if f.y+f.vspeed<wall.y+wall.h:
                                    f.vspeed=wall.y+wall.h-f.y
                elif f.vspeed>0:
                    if f.x+f.w>wall.x and f.x<wall.x+wall.w:
                        if f.y<wall.y:
                            if f.y+f.h+f.vspeed>wall.y:
                                f.vspeed=wall.y-f.y-f.h
            f.y+=f.vspeed
            if (g.player.x+g.player.w>f.x and g.player.x<f.x+f.w
            and g.player.y+g.player.h>f.y and g.player.y<f.y+f.h):
                g.die()
        #platforms
        for platform in g.platforms:
            platform.accelarate()
            for wall in g.walls+g.platforms:
                if platform.y==wall.y:
                    if platform.v>0 and platform.x<wall.x:
                        if platform.x+platform.w+platform.v>wall.x:
                            platform.v=wall.x-platform.x-platform.w
                    if platform.v<0 and platform.x>wall.x:
                        if platform.x+platform.v<wall.x+wall.w:
                            platform.v=wall.x+wall.w-platform.x
            platform.x+=platform.v
            if (g.player.x+g.player.w>platform.x and
            g.player.x<platform.x+platform.w):
                if g.player.y+g.player.h==platform.y:
                    g.player.hspeed2=platform.v
        #horizontal
        for wall in g.walls:
            if g.player.hspeed2<0:
                if g.player.y+g.player.h>wall.y and g.player.y<wall.y+wall.h:
                    if g.player.x>wall.x:
                        if g.player.x+g.player.hspeed2<wall.x+wall.w:
                            g.player.hspeed2=wall.x+wall.w-g.player.x
            elif g.player.hspeed2>0:
                if g.player.y+g.player.h>wall.y and g.player.y<wall.y+wall.h:
                    if g.player.x<wall.x:
                        if g.player.x+g.player.w+g.player.hspeed2>wall.x:
                            g.player.hspeed2=wall.x-g.player.x-g.player.w
        g.player.x+=g.player.hspeed2
        g.player.hspeed2=0
        for wall in g.walls:
            if g.player.hspeed<0:
                if g.player.y+g.player.h>wall.y and g.player.y<wall.y+wall.h:
                    if g.player.x>wall.x:
                        if g.player.x+g.player.hspeed<wall.x+wall.w:
                            g.player.hspeed=wall.x+wall.w-g.player.x
            elif g.player.hspeed>0:
                if g.player.y+g.player.h>wall.y and g.player.y<wall.y+wall.h:
                    if g.player.x<wall.x:
                        if g.player.x+g.player.w+g.player.hspeed>wall.x:
                            g.player.hspeed=wall.x-g.player.x-g.player.w
        g.player.x+=g.player.hspeed
        #end
        for exit in g.exits:
            if (g.player.x+g.player.w>exit.x and g.player.x<exit.x+exit.w and
            g.player.y+g.player.h>exit.y and g.player.y<exit.y+exit.h):
                g.nextroom()
        for button in g.buttons:
            if (g.player.x+g.player.w>button.x and g.player.x<button.x+button.w and
            g.player.y+g.player.h>button.y and g.player.y<button.y+button.h):
                for laser in g.lasers:
                    if laser.peace==0:
                        laser.peace=180
        for spike in g.spikes:
            if (g.player.x+g.player.w>spike.x and g.player.x<spike.x+spike.w
            and g.player.y+g.player.h>spike.y and g.player.y<spike.y+spike.h):
                g.die()
        for las in g.lasers:
            las.peaceful()
            if las.peace==0:
                if (g.player.x+g.player.w>las.x and g.player.x<las.x+las.w
                and g.player.y+g.player.h>las.y and g.player.y<las.y+las.h):
                    g.die()
    if g.mode==2:
        g.waiting-=1
        if g.waiting==0:
            g.mode=0
    if g.mode==3:
        if g.waiting>0:
            g.waiting-=1
    if g.keys["left"]==2:
        g.keys["left"]=1
    if g.keys["right"]==2:
        g.keys["right"]=1
    if g.keys["x"]==2:
        g.keys["x"]=1

def draw():
    if g.mode==0:
        g.screen.blit(classes.title, (0, 0))
        g.screen.blit(classes.logo, (0, 32))
        g.screen.blit(g.img_beaten, (400, 320))
        g.screen.blit(g.img_deaths, (400, 350))
    elif g.mode in (1, 2):
        g.screen.fill((255, 255, 255))
        for exit in g.exits:
            g.screen.blit(exit.img, (exit.x, exit.y))
        for platform in g.platforms:
            g.screen.blit(platform.img, (platform.x, platform.y))
        for laser in g.lasers:
            if laser.peace==0:
                g.screen.blit(laser.img, (laser.x, laser.y))
        for button in g.buttons:
            g.screen.blit(button.img, (button.x, button.y))
        for fire in g.fires:
            g.screen.blit(fire.img, (fire.x, fire.y))
        for bumper in g.bumpers:
            g.screen.blit(bumper.img, (bumper.x, bumper.y))
        g.screen.blit(g.player.img, (g.player.x, g.player.y))
        for wall in g.walls:
            g.screen.blit(wall.img, (wall.x, wall.y))
        for spike in g.spikes:
            g.screen.blit(spike.img, (spike.x, spike.y))
    elif g.mode==3:
        g.screen.blit(classes.end, (0, 0))
    pygame.display.flip()

def main():
    while 1:
        input(pygame.event.get())
        action()
        draw()
        g.clock.tick(30)
    
if __name__ == "__main__":
    main()