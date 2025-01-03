#takeown /f "D:\Program Files" /r /d y, Adminstrator run
#icacls "D:\Program Files" /grant %username%:F /t
import pygame as pg
from math import cos,sin,acos
from random import choice,randint
from functools import lru_cache
# Initialize pygame
pg.init()
# Screen dimensions
screen_width = 1200
screen_height = 900
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Haelifli (🇸🇮🇲🇺🇱🇦🇹🇮🇴🇳)")
icon = pg.image.load("assets\logo.webp")
icon = pg.transform.scale(icon, (128, 128))
pg.display.set_icon(icon)
atan2 = lambda y, x: acos(x / (x**2 + y**2)**0.5) if y >= 0 else -acos(x / (x**2 + y**2)**0.5)
# @lru_cache(maxsize=1024)

# def retruescale(x,y,ascale) -> tuple[float,float]:
#     # ((x-(screen_width/2-zoomx)-screen_width/2) * ascale + screen_width/2),(y-(screen_height/2-zoomy)-screen_height/2) * ascale + screen_height/2
#     # rews = ((x-(screen_width/2-zoomx)-screen_width/2) * ascale + screen_width/2),(y-(screen_height/2-zoomy)-screen_height/2) * ascale + screen_height/2
#     return((x-screen_width/2) * ascale + screen_width/2),(y-screen_height/2) * ascale + screen_height/2
retruescale = lambda x, y, ascale: ((x - screen_width / 2) * ascale + screen_width / 2, (y - screen_height / 2) * ascale + screen_height / 2)
NewRturnM_scale = lambda x, y, scale: ((x-screen_width/2)/ scale + screen_width/2,(y-screen_height/2)/ scale + screen_height/2)
class Food:
    def __init__(self, x, y):
        self.position = [x, y]
        self.image = pg.transform.scale(pg.image.load('assets\goldbar.png'), (16, 16)) 
class Boid:
    def __init__(self, screen_width, screen_height, 
                 separation_resolve=0.2, alignment_resolve=0.03, cohesion_resolve=0.02, top_speed=5, 
                 fishima=None, x=screen_width/2, y=screen_height/2, fish_type='fish',width=36,height=16,
                 bx=0,by=0,bex=screen_width,bey=screen_height,fleft = False,ftop = False):
        self.screen_width = screen_width
        self.screen_height = screen_height
        # self.position = np.array([x, y], dtype=float)
        # self.velocity = np.array([top_speed,top_speed], dtype=float)
        self.position = [x, y]
        self.velocity = [top_speed,top_speed]
        self.velocity[0] *= round(choice([-1, 1]), 10)
        self.velocity[1] *= round(choice([-1, 1]), 10)
        self.angle = atan2(self.velocity[1], -self.velocity[0])*3.1415926535897932/180
        self.max_speed = top_speed
        self.min_speed = 1
        self.barrierx = bx
        self.barriery = by
        self.barrierex = bex
        self.barrierey = bey
        self.separation_resolve = separation_resolve
        self.alignment_resolve = alignment_resolve
        self.cohesion_resolve = cohesion_resolve
        self.fwidth = width
        self.fheight = height
        self.image = pg.transform.scale(pg.image.load(fishima), (width, height))
        self.image = pg.transform.flip(self.image, fleft, ftop)
        self.fish_type = fish_type  # Add fish type attribute
        self.allowmove = True
        self.posdistance = lambda pos1, lpos: ((lpos[0] - pos1[0]) ** 2 + (lpos[1] - pos1[1]) ** 2) ** 0.5
        if self.fish_type == 'Gadidae':self.color = (25, 255, 255)
        elif self.fish_type == 'Salmonidae': self.color =  (200, 190, 120)
        else:self.color = (255, 255, 255)
        
        # self.trail = []
        # self.frame = 0
        # self.sframe = 36
    @lru_cache(maxsize=3000)
    def bdistance(self, oboid:tuple[float,float]):
        return ((oboid.position[0] - self.position[0]) ** 2 + (oboid.position[1] - self.position[1]) ** 2)**0.5
    @lru_cache(maxsize=3000)
    # def posdistance(self, pos1:tuple[float,float],lpos:tuple[float,float]):
    #     return ((lpos[0] - pos1[0]) ** 2 + (lpos[1] - pos1[1]) ** 2)**0.5
    def bcalc_angle(self, target=(0,0)):
        return atan2(target[1] - self.position[1], target[0] - self.position[0])
    @lru_cache(maxsize=3000)
    def poscalc_angle(self, target,target2):
        return atan2(target2[1] - target[1], target2[0] - target[0])
    def update_position(self):
        self.check_bounds()
        self.limit_speed()
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        # self.position += self.velocity
    # def trail_update(self):
    #     self.frame += 1
    #     if self.frame % 2 == 0:
    #         self.trail.append([self.position[0], self.position[1], self.sframe])  # Change to list
    #     self.frame %= 2
    #     for trail in self.trail:
    #         trail[2] -= 1
    #         if trail[2] < 0:
    #             self.trail.remove(trail)
    def check_bounds(self):       
        margin = 32 # Distance from the edge to start turning
        turn_factor = 0.2
        if self.position[0] < margin:self.velocity[0] += turn_factor
        elif self.position[0] > self.screen_width - margin:self.velocity[0] -= turn_factor
        if self.position[1] < margin:self.velocity[1] += turn_factor
        elif self.position[1] > self.screen_height - margin:self.velocity[1] -= turn_factor
        # def check_bounde(x,y):
        #     #self.posdistance((self.screen_width/2,self.screen_height/2),(x,y))<750
        #     return x >= self.barrierx and x <= self.barrierex and y >= self.barriery and y<= self.barrierey
        check_bounde = lambda x,y: x >= self.barrierx and x <= self.barrierex and y >= self.barriery and y<= self.barrierey
        if self.position[0] < self.barrierx+margin or self.position[0] > self.barrierex-margin or self.position[1] < self.barriery+margin or self.position[1] > self.barrierey-margin and not check_bounde(self.position[0],self.position[1]):
            angle = self.poscalc_angle((0,0),(self.velocity[0],self.velocity[1]))
            # rj_left = 0
            # rj_right = 0
            rj_dir = 0
            valid_left_count = 0
            valid_right_count = 0
            chosen_direction = 0
            l_left = []
            l_right = []
            for k in range(0, 22):
                # rj_left = (jdir_left)*180/3.1415926535897932
                # rj_right = (-jdir_right)*180/3.1415926535897932    
                if check_bounde(self.position[0]+cos(angle - rj_dir) * 32,self.position[1]+sin(angle - rj_dir) * 32):
                    valid_left_count += 1
                    l_left.append(-rj_dir)
                if check_bounde(self.position[0]+cos(angle + rj_dir) * 32,self.position[1]+sin(angle + rj_dir) * 32):
                    valid_right_count += 1
                    l_right.append(rj_dir)
                if valid_left_count>0 or valid_right_count>0:break
                # rj_left += 5*0.01745329251994329576
                # rj_right += 5*0.01745329251994329576
                rj_dir += 5*0.01745329251994329576
            if valid_left_count>0:aleft = sum(l_left)/valid_left_count
            if valid_right_count>0:aright = sum(l_right)/valid_right_count
            if valid_left_count>0 and valid_right_count>0:
                if valid_left_count < valid_right_count:chosen_direction = aright
                elif valid_right_count < valid_left_count:chosen_direction =aleft
                else:chosen_direction = choice([aleft,aright])
            elif valid_left_count>0:chosen_direction = aleft
            elif valid_right_count>0:chosen_direction = aright
            if chosen_direction != 0:
                sp = self.posdistance((0, 0), (self.velocity[0], self.velocity[1]))
                angle += chosen_direction
                self.velocity[0] = sp*cos(angle)
                self.velocity[1] = sp*sin(angle)
    # def move_random_direction(self):
    #     dist = np.hypot(self.velocity[0], self.velocity[1])
    #     self.angle = math.atan2(self.velocity[1], self.velocity[0])
    #     self.angle +=  uniform(-0.5, 0.5)
    #     self.velocity[0] = dist * math.cos(self.angle)*2
    #     self.velocity[1] = dist * math.sin(self.angle)*2
    def apply_separation(self, boids, separation_distance):
        # if not boids:return
        positions = [(boid.position[0]-self.position[0],boid.position[1]-self.position[1]) for boid in boids if boid != self and self.bdistance(boid) < separation_distance]
        if not positions:return
        '''V2 of separation'''
        # totxy = positions - np.array(self.position)
        # totdist = np.linalg.norm(positions, axis=1)
        # svel = np.sum(positions / np.linalg.norm(positions, axis=1)[:, np.newaxis], axis=0)
        # self.velocity -= np.sum(positions / np.linalg.norm(positions, axis=1)[:, np.newaxis], axis=0) * self.separation_resolve
        # self.velocity[0] -= sum(pos[0] / self.posdistance((0,0),(pos[0],pos[1])) for pos in positions) * self.separation_resolve
        # self.velocity[1] -= sum(pos[1] / self.posdistance((0,0),(pos[0],pos[1])) for pos in positions) * self.separation_resolve
        distances = [self.posdistance((0,0),(pos[0], pos[1])) for pos in positions]
        self.velocity[0] -= sum((pos[0]/dist) for pos, dist in zip(positions, distances)) * self.separation_resolve
        self.velocity[1] -= sum((pos[1]/dist) for pos, dist in zip(positions, distances)) * self.separation_resolve
        # move_x, move_y = 0, 0
        # for other_boid in boids:
        #     if other_boid != self and self.distance(other_boid) < separation_distance:
        #         move_x += self.position[0] - other_boid.position[0]
        #         move_y += self.position[1] - other_boid.position[1]
        # self.velocity[0] += move_x * self.separation_resolve  # Apply a smaller fraction for smoother separation
        # self.velocity[1] += move_y * self.separation_resolve  # Apply a smaller fraction for smoother separation
    def apply_alignment(self, boids, alignment_distance):
        """ALIGNMENT def"""
        velocities = [b for b in boids if b != self and self.bdistance(b) < alignment_distance #and boid.fish_type == self.fish_type 
                    # and (abs(self.poscalc_angle((0, 0), (b.velocity[0], b.velocity[1]))*180/3.1415926535897932 - ((self.bcalc_angle(b.position))*180/3.1415926535897932)) < 60 if self.poscalc_angle((0, 0), (b.velocity[0], b.velocity[1]))*180/3.1415926535897932 < 180 else abs((self.poscalc_angle((0, 0), (b.velocity[0], b.velocity[1]))*180/3.1415926535897932-360) - ((self.bcalc_angle(b.position))*180/3.1415926535897932)) < 60)
                    ]
        # velocities = [b for b in velocities if b.fish_type == self.fish_type]
        if not velocities:return
        avg_velocity = [sum(v.velocity[i]for v in velocities)/len(velocities)for i in [0,1]]
        self.velocity[0] += (avg_velocity[0] - self.velocity[0]) * self.alignment_resolve
        self.velocity[1] += (avg_velocity[1] - self.velocity[1]) * self.alignment_resolve
    def apply_cohesion(self, boids, cohesion_distance):
        positions =  [b for b in boids if b != self and self.bdistance(b) < cohesion_distance #and boid.fish_type == self.fish_type
                    # and (abs(self.poscalc_angle((0, 0), (b.velocity[0], b.velocity[1]))*180/3.1415926535897932 - ((self.bcalc_angle(b.position))*180/3.1415926535897932)) < 60 if self.poscalc_angle((0, 0), (b.velocity[0], b.velocity[1]))*180/3.1415926535897932 < 180 else abs((self.poscalc_angle((0, 0), (b.velocity[0], b.velocity[1]))*180/3.1415926535897932-360) - ((self.bcalc_angle(b.position))*180/3.1415926535897932)) < 60)
                    ]
        # positions = [b for b in positions if b.fish_type==self.fish_type]
        if not positions:return
        avg_position = [sum(p.position[i] for p in positions) / len(positions) for i in [0,1]]#np.mean(positions, axis=0)
        self.velocity[0] += (avg_position[0] - self.position[0]) * self.cohesion_resolve
        self.velocity[1] += (avg_position[1] - self.position[1]) * self.cohesion_resolve
        
        """COHESION def"""
        # avg_position_x, avg_position_y = 0, 0
        # count = 0
        # for other_boid in boids:
        #     if other_boid != self and self.distance(other_boid) < cohesion_distance and other_boid.fish_type == self.fish_type:
        #         avg_position_x += other_boid.position[0]
        #         avg_position_y += other_boid.position[1]
        #         count += 1
        # if count > 0:
        #     avg_position_x /= count
        #     avg_position_y /= count
        #     self.velocity[0] += (avg_position_x - self.position[0]) * self.cohesion_resolve
            # self.velocity[1] += (avg_position_y - self.position[1]) * self.cohesion_resolve 
    # def chase(self, boids,types,dst):
    #     position = [boid for boid in boids if boid != self and self.bdistance(boid) < dst]
    #     if not position:return
    #     fliposition = [boid.position for boid in position if boid.fish_type == types]
    #     if not fliposition:return
    #     closest_boid = min(fliposition, key=lambda pos: self.posdistance((0,0),(pos[0],pos[1])))
    #     # self.velocity[0] += (closest_boid[0] - self.position[0]) * self.cohesion_resolve
    #     # self.velocity[1] += (closest_boid[1] - self.position[1]) * self.cohesion_resolve
    #     self.velocity[0] += (closest_boid[0]-self.position[0]) / self.posdistance((self.position[0],self.position[1]),(closest_boid[0],closest_boid[1])) * 0.2
    #     self.velocity[1] += (closest_boid[1]-self.position[1]) / self.posdistance((self.position[0],self.position[1]),(closest_boid[0],closest_boid[1])) * 0.2
    # def avoid(self, boids,types,dst):
    #     position = [boid for boid in boids if boid != self and self.bdistance(boid) < dst]
    #     if not position:return
    #     fliposition = [[boid.position[_] - self.position[_] for _ in range(len(self.position))] for boid in position if boid.fish_type == types]
    #     if not fliposition:return
    #     # closest_boid = min(fliposition, key=lambda pos: self.posdistance((0,0),(pos[0],pos[1])))
    #     # # self.velocity[0] += (closest_boid[0] - self.position[0]) * self.cohesion_resolve
    #     # # self.velocity[1] += (closest_boid[1] - self.position[1]) * self.cohesion_resolve
    #     # self.velocity[0] -= (closest_boid[0]-self.position[0]) / self.posdistance((self.position[0],self.position[1]),(closest_boid[0],closest_boid[1])) * 0.3
    #     # self.velocity[1] -= (closest_boid[1]-self.position[1]) / self.posdistance((self.position[0],self.position[1]),(closest_boid[0],closest_boid[1])) * 0.3
    #     self.velocity[0] -= sum(pos[0] / self.posdistance((0,0),(pos[0],pos[1])) for pos in fliposition) * 0.3
    #     self.velocity[1] -= sum(pos[1] / self.posdistance((0,0),(pos[0],pos[1])) for pos in fliposition) * 0.3
    # def pos_avoid(self,dst,pos,reps):
    #     if self.posdistance((self.position[0],self.position[1]),(pos[0],pos[1])) < dst:
    #         self.velocity[0] -= (pos[0]-self.position[0]) / self.posdistance((self.position[0],self.position[1]),(pos[0],pos[1])) * reps
    #         self.velocity[1] -= (pos[1]-self.position[1]) / self.posdistance((self.position[0],self.position[1]),(pos[0],pos[1])) * reps
        
        
    def apply_mouse_repulsion(self, mouse_pos, repulsion_distance, repulsion_strength):
        distance_to_mouse = self.posdistance(mouse_pos,(self.position[0],self.position[1]))
        if distance_to_mouse < repulsion_distance:
            angle = self.poscalc_angle(mouse_pos,(self.position[0],self.position[1]))
            strength = 1000/(distance_to_mouse+1e-10)
            if strength > 256:
                strength = 256
            move_x = cos(angle)*strength
            move_y = sin(angle)*strength
            self.velocity[0] += move_x * repulsion_strength
            self.velocity[1] += move_y * repulsion_strength
    def limit_speed(self):
        
        # if not (self.position[0] < self.barrierx or self.position[0] > self.barrierex or self.position[1] < self.barriery or self.position[1] > self.barrierey):
        # if speed > self.max_speed:
        #     self.velocity[0] = (self.velocity[0] / speed) * self.max_speed
        #     self.velocity[1] = (self.velocity[1] / speed) * self.max_speed
        # # else:
        #     # if speed > self.max_speed*12:
        #         # self.velocity[0] = (self.velocity[0] / speed) * self.max_speed*12
        #         # self.velocity[1] = (self.velocity[1] / speed) * self.max_speed*12
        # if speed < self.min_speed:
        #     self.velocity[0] = (self.velocity[0] / speed) * self.min_speed
        #     self.velocity[1] = (self.velocity[1] / speed) * self.min_speed
        speed = self.posdistance((0, 0),(self.velocity[0], self.velocity[1]))
        def speddest(velocity,speed,set_speed):
            if speed < set_speed:
                velocity[0] = (velocity[0] / speed) * set_speed
                velocity[1] = (velocity[1] / speed) * set_speed
            return velocity
        # self.velocity = speddest(self.velocity,speed,self.min_speed)
        self.velocity = speddest(self.velocity,-speed,-self.max_speed)
    # def find_food(self,x,y, foods, food_distance):
    #     if len(foods) == 0:return None, None, None  # return None if no food is found
    #     food_positions = np.array([[food.position[0], food.position[1]] for food in foods])
    #     distances = np.sqrt((food_positions[:, 0] - x) ** 2 + (food_positions[:, 1] - y) ** 2)
    #     if np.any(distances < food_distance):
    #         closest_food_index = np.argmin(distances)
    #         closest_food = foods[closest_food_index]
    #         foodx, foody = closest_food.position
    #         return foodx, foody, distances[closest_food_index]  # return the food and distance
    #     return None, None, None  # return None if no food is found  
    def draw(self, screen,scale=1):      
        # sx,sy = retruescale(self.position[0],self.position[1],scale)
        # self.newimage = pg.transform.scale(self.image, (int(self.fwidth*scale), int(self.fheight*scale)))
        # if self.velocity[0] < 0:self.newimage = pg.transform.flip(self.newimage, False, True)
        # angle = self.poscalc_angle((self.velocity[1], self.velocity[0]),(0,0)) +90
        # self.newimage = pg.transform.rotate(self.newimage,  angle)
        # nfwidth = self.newimage.get_width()
        # nfheight = self.newimage.get_height()
        # sx-=nfwidth/2;sy-=nfheight/2
        # # self.newimage = transform.rotate(self.newimage, self.angle)
        # if not (sx < -nfwidth*2 or sx > screen_width or sy< -nfheight*2 or sy > screen_height):
        #     if scale > 0.2: screen.blit(self.newimage, (sx, sy))
        #     else:pg.draw.circle(screen, (255, 0, 0), (int(sx), int(sy)), 2)
        angle = self.poscalc_angle((0,0),(self.velocity[0], self.velocity[1]))#*0.01745329251994329576
        # pg.draw.circle(screen, self.color, retruescale(self.position[0], self.position[1], scale),int(4*scale))
        # pg.draw.line(screen, (255,255,0), retruescale(self.position[0], self.position[1], scale), retruescale(self.position[0] + self.velocity[0], self.position[1] + self.velocity[1], scale), int(2*scale))
        angle90 = angle+1.570796326794896
        right_a = cos(angle90);left_a = sin(angle90)

        # pg.draw.polygon(screen, color, [
        #     retruescale(self.position[0], self.position[1], scale),
        #     retruescale(self.position[0] + self.velocity[0]*4, self.position[1], scale),
        #     retruescale(self.position[0] + self.velocity[0]*4, self.position[1] + self.velocity[1]*4, scale),
        #     retruescale(self.position[0], self.position[1] + self.velocity[1]*4, scale)
        # ])
        pg.draw.polygon(screen,self.color, [retruescale(self.position[0]-right_a*4,self.position[1]-left_a*4,scale),retruescale(self.position[0]+cos(angle)*8,self.position[1]+sin(angle)*8,scale),retruescale(self.position[0]+right_a*5,self.position[1]+left_a*5,scale)])
        # pg.draw.polygon(screen,self.color, [(self.position[0]-right_a*5,self.position[1]-left_a*5),(self.position[0]+np.cos(angle)*10,self.position[1]+np.sin(angle)*10),(self.position[0]+right_a*5,self.position[1]+left_a*5)])
class Slider:
    def __init__(self,pos:tuple,size:tuple,val:float,minv:float,maxv:float,tyipe=None) -> None:
        self.pos = pos
        self.size = size

        self.sl_leftpos = self.pos[0] - (size[0]//2)
        self.sl_rightpos = self.pos[0] + (size[0]//2)
        self.sl_toppos = self.pos[1] - (size[1]//2)

        self.valtype = tyipe
        self.min = minv
        self.max = maxv
        

        self.init_val = (self.sl_rightpos - self.sl_leftpos) *val/self.max
        self.crect = pg.Rect(self.sl_leftpos,self.sl_toppos,self.size[0],self.size[1])
        self.brect = pg.Rect(self.sl_leftpos+self.init_val-5,self.sl_toppos,10,self.size[1])
        self.get_val = lambda: round(((self.brect.centerx-self.sl_leftpos)/(self.sl_rightpos-self.sl_leftpos))*(self.max-self.min)+self.min,13)
    def mov_slid(self,mousex):
        self.brect.centerx = mousex
    def draw(self,scr):
        pg.draw.rect(scr,(140,140,140),pg.Rect(self.sl_leftpos-3,self.sl_toppos,self.size[0]+6,self.size[1]))
        pg.draw.rect(scr,(100,100,100),pg.Rect(self.sl_leftpos-3,self.sl_toppos,self.size[0]+6,self.size[1]),2)
        pg.draw.rect(scr,(200,200,200),(self.sl_leftpos,self.pos[1]-5,(self.brect.centerx-self.sl_leftpos),10),0)
        pg.draw.rect(scr,(255,255,25),self.brect,border_radius=3) 
    def set_val(self,val):
        self.init_val = (self.sl_rightpos - self.sl_leftpos) *val/self.max
        self.crect = pg.Rect(self.sl_leftpos,self.sl_toppos,self.size[0],self.size[1])
        self.brect = pg.Rect(self.sl_leftpos+self.init_val-5,self.sl_toppos,10,self.size[1])
# Main loop
def main() -> None:
    global screen
    # global zoomx,zoomy
    clock = pg.time.Clock()
    t_dist = 1
    separation_distance = 55*t_dist#32
    alignment_distance = 56*t_dist
    cohesion_distance = 56*t_dist
    separation_resolve = 0.22#0.032
    alignment_resolve = 0.06
    cohesion_resolve = 0.025
    repulsion_distance = 30
    repulsion_strength = 0.05
    top_speed = 5
    # fishima = os.path.join('assets', 'cod.png')
    fishima = 'assets\cod.png'
    salmonela ='assets\salmon.png'
    tunala = 'assets\\rainbow.png'
    font = pg.font.SysFont(None, 32)
    boids = []
    movdist = 30
    # zoomx = screen_width/2
    # zoomy = screen_height/2
    scale = 1
    # listoffoods = []
    #return (x -screen_width/2)/ ascale + screen_width/2 + (screen_width/2 - zoomx),(y -screen_height/2)/ ascale + screen_height/2 + (screen_height/2 - zoomy)
    # def NewRturnM_scale(x,y,scale) -> tuple:
    #     return (x -screen_width/2)/ scale + screen_width/2,(y -screen_height/2)/ scale + screen_height/2
    
    for i in range(96):
        # randomwidth =  uniform(32,34)
        # randomheight = round(randomwidth*16/36)
        randomspx = randint(0, screen_width)
        randomspy = randint(0, screen_height)
        boids.append(Boid(screen_width, screen_height, separation_resolve, alignment_resolve, cohesion_resolve, top_speed, fishima, randomspx, randomspy, fish_type='Gadidae',width=36,height=16,fleft=True))
        # randomwidth = uniform(32,34)
        # randomheight = int(randomwidth*16/36)
        # randomspx = randint(0, screen_width)
        # randomspy =  randint(0, screen_height)
        # boids.append(Boid(screen_width, screen_height, separation_resolve, alignment_resolve, cohesion_resolve, top_speed, salmonela, randomspx, randomspy, fish_type='Salmonidae',width=randomwidth,height=randomheight))
    # for i in range(24):
    #     randomwidth =  uniform(32,34)
    #     randomheight = int(randomwidth*16/45)
    #     randomspx =  uniform(-screen_width/2, screen_width/2) + screen_width // 2
    #     randomspy =  uniform(-screen_height/2, screen_height/2) + screen_height // 2
    #     boids.append(Boid(screen_width, screen_height, separation_resolve, alignment_resolve, cohesion_resolve, top_speed, salmonela, randomspx, randomspy, fish_type='Salmonidae',width=randomwidth,height=randomheight))
        # randomwidth =  uniform(14,72)
        # randomheight = int(randomwidth*16/14)
        # boids.append(Boid(screen_width, screen_height, separation_resolve, alignment_resolve, cohesion_resolve, top_speed, tunala,  uniform(0, screen_width),  uniform(0, screen_height), fish_type='rainbow',width=randomwidth,height=randomheight))
    running = True
    # water = Water(600, 450, 60)
    # water = transform.scale(water.texture, (screen_width, screen_height))
    mouse_x,mouse_y = pg.mouse.get_pos()
    aascale = 1
    msx , msy = NewRturnM_scale(mouse_x,mouse_y,aascale)
    prevsx,prevsy = msx,msy
    # natboid = np.array([])
    # noneboids = []
    
    sliders = [Slider((screen_width-200,15),(400,20),separation_resolve,0,1,"sep"),
               Slider((screen_width-200,40),(400,20),alignment_resolve,0,1,"align"),
               Slider((screen_width-200,65),(400,20),cohesion_resolve,0,1,"cohes"),
               Slider((screen_width-200,90),(400,20),t_dist,0,2,"dist"),
               Slider((screen_width-200,115),(400,20),top_speed,0,20,"speed"),]
    icon = pg.image.load('assets\logo.webp')
    icon = pg.transform.scale(icon, (screen_width, screen_height))
    # esceed = False
    # lframe = 120
    # esctimer = 60
    # for i in range(lframe+esctimer):
    #     if esceed:
    #         break
    #     i = max(0,i)
    #     ie = 255-i/(lframe/255)
    #     screen.fill((45, 233, 199))
    #     icon.set_alpha(ie)
    #     screen.blit(icon, (0, 0))
    #     pg.display.flip()

    #     for event in pg.event.get():
    #         if event.type == pg.QUIT:
    #             esceed = True  
    #     clock.tick(120)
    # del esceed
    # del lframe
    # del esctimer
    # timerr = 1
    # curtime = tm.time()
    paused = False
    while running:
        aascale = abs(scale)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    paused = not paused
        screen.fill((0,0,0))
        pg.draw.circle(screen, (255, 100, 0), (screen_width/2, screen_height/2), 750*aascale,1)
        pg.draw.rect(screen, (0, 100, 255), (*retruescale(0,0,min(1.2,aascale)), screen_width*min(1.2,aascale), screen_height*min(1.2,aascale)),1)
        # pg.draw.circle(screen, (0, 80, 255), (int(screen_width/2), int(screen_height/2)), 1*aascale)
        mouse_x,mouse_y = pg.mouse.get_pos()
        msx,msy = NewRturnM_scale(mouse_x,mouse_y,aascale)
        keys = pg.key.get_pressed()
        # if keys[pg.K_UP]:
        #     zoomy += 100
        # if keys[pg.K_DOWN]:
        #     zoomy -= 100
        # if keys[pg.K_LEFT]:
        #     zoomx += 100
        # if keys[pg.K_RIGHT]:
        #     zoomx -= 100
        # if keys[pg.K_w]:
        #     listoffoods.append(Food(msx,msy))
        # if keys[pg.K_s]:
        #     listdst = np.array([np.sqrt((food.position[0] - msx) ** 2 + (food.position[1] - msy) ** 2) for food in listoffoods])
        #     if np.any(listdst < 100):
        #         listoffoods.pop(np.argmin(listdst))
        if keys[pg.K_e]:
            scale *= 2**0.25
        if keys[pg.K_q]:
            scale /= 2**0.25
        if keys[pg.K_r]:
            separation_resolve = 0.22
            alignment_resolve = 0.06
            cohesion_resolve = 0.025
            t_dist = 1
            separation_distance = 55*t_dist
            alignment_distance = 56.5*t_dist
            cohesion_distance = 57.5*t_dist
            top_speed = 5
            for slider in sliders:
                if slider.valtype == "sep":slider.set_val(separation_resolve)
                if slider.valtype == "align":slider.set_val(alignment_resolve)
                if slider.valtype == "cohes":slider.set_val(cohesion_resolve)
                if slider.valtype == "dist":slider.set_val(t_dist)
                if slider.valtype == "speed":slider.set_val(top_speed)
            for boid in boids:
                boid.separation_resolve = separation_resolve
                boid.alignment_resolve = alignment_resolve
                boid.cohesion_resolve = cohesion_resolve
                boid.max_speed = top_speed
            # if keys[pg.K_d]:
            #     if keys[pg.K_1]:
            #         separation_resolve += 0.05
            #     if keys[pg.K_2]:
            #         separation_resolve -= 0.05
            #     separation_resolve = round(separation_resolve,16)
            #     for boid in boids:
            #         boid.separation_resolve = separation_resolve
            #     print(separation_resolve)
            # if keys[pg.K_a]:
            #     if keys[pg.K_1]:
            #         alignment_resolve += 0.05
            #     if keys[pg.K_2]:
            #         alignment_resolve -= 0.05
            #     alignment_resolve = round(alignment_resolve,16)
            #     for boid in boids:
            #         boid.alignment_resolve = alignment_resolve
            #     print(alignment_resolve)
            # if keys[pg.K_c]:
            #     if keys[pg.K_1]:
            #         cohesion_resolve += 0.05
            #     if keys[pg.K_2]:
            #         cohesion_resolve -= 0.05
            #     cohesion_resolve = round(cohesion_resolve,16)
            #     for boid in boids:
            #         boid.cohesion_resolve = cohesion_resolve
            #     print(cohesion_resolve)
        if keys[pg.K_f]:prf = True;pg.draw.circle(screen, (255, 0, 0), (mouse_x, mouse_y), movdist, 5)
        else:prf = False
        for boid in boids:
            if not boid.allowmove:
                boid.position[0] += msx - prevsx
                boid.position[1] += msy - prevsy
            dist = ((boid.position[0] - msx) ** 2 + (boid.position[1] - msy) ** 2)**0.5
            boid.allowmove = False if dist < movdist/aascale and prf else True
        prevsx = msx;prevsy = msy
        if keys[pg.K_SPACE]:
            pg.draw.circle(screen, (255, 0, 0), (mouse_x,mouse_y), repulsion_distance,5)
            def mouserpress(strength):
                for boid in boids:
                    boid.apply_mouse_repulsion((msx,msy), repulsion_distance/aascale, strength)
            if keys[pg.K_x]:mouserpress(-repulsion_strength/aascale)
            else:mouserpress(repulsion_strength/aascale)
        def boidsim():
            """Main boid simulation loop"""
            # for boid in boids:
            #     if boid.allowmove:
            #         for i in range(len(boid.trail)-1):
            #             rx = (boid.trail[i][0]-(screen_width/2-zoomx)-screen_width/2) * aascale + screen_width/2
            #             ry = (boid.trail[i][1]-(screen_height/2-zoomy)-screen_height/2) * aascale + screen_height/2
            #             erx = (boid.trail[i+1][0]-(screen_width/2-zoomx)-screen_width/2) * aascale + screen_width/2
            #             ery = (boid.trail[i+1][1]-(screen_height/2-zoomy)-screen_height/2) * aascale + screen_height/2
            #             c = (255/boid.sframe)*i
            #             pg.draw.line(screen, (c, c, c), (rx, ry), (erx, ery), 1)
            for boid in boids:
                if boid.allowmove and not paused:
                    boid.apply_separation(boids, separation_distance)
                    boid.apply_alignment(boids, alignment_distance)
                    boid.apply_cohesion(boids, cohesion_distance)
                    # if boid.fish_type == 'Gadidae':boid.chase(boids,'Salmonidae',56)
                    # if boid.fish_type == 'Salmonidae':boid.avoid(boids,'Gadidae',81)
                    # foodx ,foody,dist = boid.find_food(boid.position[0],boid.position[1],listoffoods, 32)
                    # if foodx is not None or foody is not None:
                    #     direction = np.arctan2(foody - boid.position[1], foodx - boid.position[0])
                    #     boid.velocity[0] += np.cos(direction)*0.6
                    #     boid.velocity[1] += np.sin(direction)*0.6
                    # boid.velocity[0]*=0.999
                    # boid.velocity[1]*=0.999
                    boid.update_position()
                    # if abs(boid.velocity[0]) >2 and abs(boid.velocity[1]) >2:
                    #     boid.velocity[0]*=0.99
                    #     boid.velocity[1]*=0.99
                    #     # pg.draw.circle(screen, (255, 255, 255), (int(trail[0]), int(trail[1])), 1)
                # boid.trail_update()
                boid.draw(screen,scale=aascale)
        boidsim()
        # for food in listoffoods:
        #     x,y = retruescale(food.position[0],food.position[1],aascale)
        #     screen.blit(food.image, (x, y))
        if mouse_x < 120:
            # timerr = tm.time();curfps = 1/(timerr - curtime)
            truefps = clock.get_fps()
            textfps = font.render(f"Fps:{round(truefps,1)}",True,(255,215,0))
            screen.blit(textfps, (10, 10))#;curtime = timerr
        if paused:
            for slider in sliders:
                if slider.crect.collidepoint(mouse_x,mouse_y) :
                    t = font.render(f"{slider.valtype}:{slider.get_val()}",True,(255,215,0))
                    screen.blit(t, (slider.pos[0]-203-t.get_width(), slider.pos[1]-t.get_height()/2))
                    if pg.mouse.get_pressed()[0]:
                        slider.mov_slid(mouse_x)
                        if slider.valtype == "sep":
                            separation_resolve = slider.get_val()
                            for boid in boids:boid.separation_resolve = separation_resolve
                        if slider.valtype == "align":
                            alignment_resolve = slider.get_val()
                            for boid in boids:boid.alignment_resolve = alignment_resolve
                        if slider.valtype == "cohes":
                            cohesion_resolve = slider.get_val()
                            for boid in boids:boid.cohesion_resolve = cohesion_resolve
                        if slider.valtype == "speed":
                            top_speed = slider.get_val()
                            for boid in boids:boid.max_speed = top_speed
                        if slider.valtype == "dist":
                            t_dist = slider.get_val()
                            separation_distance = 55*t_dist
                            alignment_distance = 56.5*t_dist
                            cohesion_distance = 57.5*t_dist
                slider.draw(screen)
        pg.display.update()
        clock.tick(90) 
    pg.quit()
if __name__ == "__main__":
    main()
#python -c "import fish; fish.main()"
#python decoder.py build_ext --inplace
