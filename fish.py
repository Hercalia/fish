# #takeown /f "D:\Program Files" /r /d y, Adminstrator run
# #icacls "D:\Program Files" /grant %username%:F /t
# import pygame
# from pygame import image, transform;import random;
# import os
# import time
# import numpy as np
# from functools import lru_cache


# # Initialize Pygame
# pygame.init()
# pygame.time
# # Screen dimensions
# ratio = 12/9
# screen_width = 1200
# screen_height = screen_width / ratio
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("🇭🇮🇫🇱🇦🇷🇾 (🇸🇮🇲🇺🇱🇦🇹🇮🇴🇳)")
# icon = image.load(os.path.join('assets', 'logo.webp'))
# icon = transform.scale(icon, (128, 128))
# pygame.display.set_icon(icon)
# # Colors 
# # 
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# BLUE = (0, 0, 255)
# LIGHT_BLUE = (173, 216, 230)
# # @lru_cache(maxsize=1024)

# def retruescale(x,y,ascale):
#     wsx = (x-(screen_width/2-zoomx)-screen_width/2) * ascale + screen_width/2;wsy = (y-(screen_height/2-zoomy)-screen_height/2) * ascale + screen_height/2
#     return wsx,wsy
# # class Water:
# #     def __init__(self, width, height, num_points):
# #         self.width = width
# #         self.height = height
# #         self.num_points = num_points
# #         self.points = [(random.randint(0, width), random.randint(100, height),(random.randint(0,255),random.randint(0,255),random.randint(100,255))) for _ in range(num_points)]
# #         self.texture = self.generate_voronoi_texture()
# #     def generate_voronoi_texture(self):
# #         texture = pygame.Surface((self.width, self.height))
# #         # Create a grid of coordinates
# #         x_coords, y_coords = np.meshgrid(np.arange(self.width), np.arange(self.height))
# #         grid_coords = np.stack([x_coords, y_coords], axis=-1)
# #         # Extract points and colors
# #         points = np.array([(p[0], p[1]) for p in self.points])
# #         colors = np.array([p[2] for p in self.points])
# #         # Calculate the distance from each grid point to all points
# #         distances = np.sqrt(((grid_coords[:, :, np.newaxis, :] - points[np.newaxis, np.newaxis, :, :]) ** 2).sum(axis=3))
# #         # Determine the closest point for each grid point
# #         closest_point_indices = np.argmin(distances, axis=2)
# #         # Generate the texture based on the closest points
# #         texture_array = pygame.surfarray.pixels3d(texture)
# #         for i in range(self.num_points):
# #             mask = (closest_point_indices == i)
# #             distance_to_closest = distances[:, :, i][mask]
# #             brightness = np.minimum(255, (distance_to_closest / 2).astype(int)) * 4
# #             brightness = np.minimum(brightness, 160)
# #             cpoint = colors[i]
# #             color = np.array([cpoint], dtype=np.uint8)
# #             texture_array[mask.T] = color  # Transpose the mask to match the texture array dimensions
# #         return texture
# #     def draw(self, screen):
# #         screen.blit(self.texture, (0, 0))
# class Food:
#     def __init__(self, x, y):
#         self.position = [x, y]
#         self.image = transform.scale(image.load(os.path.join('assets', 'goldbar.png')), (16, 16))
        
# class Boid:
#     def __init__(self, screen_width:int, screen_height:int, separation_resolve=0.2, alignment_resolve=0.03, cohesion_resolve=0.02, top_speed=4.5, fishima=None, x=None, y=None, fish_type='fish',width=36,height=16,bx=0,by=0,bex=screen_width,bey=screen_height,fleft = False,ftop = False):
#         self.screen_width = screen_width
#         self.screen_height = screen_height
#         self.position = [x, y]
#         self.velocity = [5, 5]
#         self.velocity[0]*= round(random.choice([-1,1]),2)
#         self.velocity[1]*= round(random.choice([-1,1]),2)
#         self.angle = np.degrees(np.atan2(self.velocity[1], -self.velocity[0]))
#         self.max_speed = top_speed
#         self.min_speed = 1
#         # self.speed_x = screen_width/(screen_width/2.5)
#         # self.speed_y = screen_height/(screen_height/2.5)#for 16:9, 675
#         # self.speed_x = 1
#         # self.speed_y = 1
#         self.barrierx = bx
#         self.barriery = by
#         self.barrierex = bex
#         self.barrierey = bey
#         self.separation_resolve = separation_resolve
#         self.alignment_resolve = alignment_resolve
#         self.cohesion_resolve = cohesion_resolve
#         self.fwidth = width
#         self.fheight = height
#         self.image = transform.scale(image.load(fishima), (width, height))
#         self.image = transform.flip(self.image, fleft, ftop)
#         self.fish_type = fish_type  # Add fish type attribute
#         self.allowmove = True
#         # self.trail = []
#         # self.frame = 0
#         # self.sframe = 36
#     @lru_cache(maxsize=3000)
#     def bdistance(self, other_boid):
#         return np.sqrt((self.position[0] - other_boid.position[0]) ** 2 + (self.position[1] - other_boid.position[1]) ** 2)
#     @lru_cache(maxsize=3000)
#     def posdistance(self, fipos=(0,0),lipos=None):
#         return np.sqrt((lipos[0] - fipos[0]) ** 2 + (lipos[1] - fipos[1]) ** 2)
#     def bcalc_angle(self, target=(0,0)):
#         return np.arctan2(target[1] - self.position[1], target[0] - self.position[0])
#     @lru_cache(maxsize=3000)
#     def poscalc_angle(self, target=(0,0),target2=(0,0)):
#         return np.degrees(np.arctan2(target2[1] - target[1], target2[0] - target[0]))
#     def update_position(self):
#         self.check_bounds()
#         self.limit_speed()
#         self.position[0] += self.velocity[0]#*self.speed_x
#         self.position[1] += self.velocity[1]#*self.speed_y

#         # self.frame += 1
#         # if self.frame % 2 == 0:
#         #     self.trail.append([self.position[0], self.position[1], self.sframe])  # Change to list
#         # self.frame %= 2
#         # for trail in self.trail:
#         #     trail[2] -= 1
#         #     if trail[2] < 0:
#         #         self.trail.remove(trail)

#     def check_bounds(self):       
#         margin = 32 # Distance from the edge to start turning
#         turn_factor = 0.25
#         if self.position[0] < margin:
#             self.velocity[0] += turn_factor
#             # self.position[0] = self.screen_width - margin
#         elif self.position[0] > self.screen_width - margin:
#             self.velocity[0] -= turn_factor
#             # self.position[0] =  margin
#         if self.position[1] < margin:
#             self.velocity[1] += turn_factor
#             # self.position[1] = self.screen_height - margin
#         elif self.position[1] > self.screen_height - margin:
#             self.velocity[1] -= turn_factor
#             # self.position[1] = margin

#         # if (self.position[0] < 0 or self.position[0] > self.screen_width or self.position[1] < 0 or self.position[1] > self.screen_height) and self.campzone == 0:
#         #     angle = math.atan2(self.position[1] - self.screen_height / 2, self.position[0] - self.screen_width / 2)
#         #     self.velocity[0] -= math.cos(angle)*turn_factor
#         #     self.velocity[1] -= math.sin(angle)*turn_factor
#         #     # self.position[0] = min(self.screen_width, max(0, self.position[0]))
#         #     # self.position[1] = min(self.screen_height, max(0, self.position[1]))
#         #todo old code top
#         #todo new code bottom
#         if self.position[0] < self.barrierx+margin or self.position[0] > self.barrierex-margin or self.position[1] < self.barriery+margin or self.position[1] > self.barrierey-margin:
#             angle = np.radians(self.poscalc_angle((0,0),(self.velocity[0],self.velocity[1])))
#             jdir_left = 0
#             jdir_right = 0
#             valid_left = False
#             valid_right = False

#             valid_left_count = 0
#             valid_right_count = 0

#             for k in range(0, 24):
#                 x_left = self.position[0]
#                 y_left = self.position[1]
#                 x_right = self.position[0]
#                 y_right = self.position[1]
#                 rj_left = np.radians(jdir_left)
#                 rj_right = np.radians(-jdir_right)
#                 x_left += np.cos(angle + rj_left) * 32
#                 y_left += np.sin(angle + rj_left) * 32
#                 x_right += np.cos(angle + rj_right) * 32
#                 y_right += np.sin(angle + rj_right) * 32
                
#                 if x_left >= self.barrierx and x_left <= self.barrierex and y_left >= self.barriery and y_left <= self.barrierey:
#                     valid_left = True
#                     valid_left_count += 1
#                 if x_right >= self.barrierx and x_right <= self.barrierex and y_right >= self.barriery and y_right <= self.barrierey:
#                     valid_right = True
#                     valid_right_count += 1

#                 if valid_left or valid_right:
#                     break

#                 jdir_left += 5
#                 jdir_right += 5

#             if valid_left and valid_right:
#                 if valid_left_count < valid_right_count:
#                     chosen_direction = rj_left
#                 elif valid_right_count < valid_left_count:
#                     chosen_direction = rj_right
#                 else:
#                     chosen_direction = random.choice([rj_left, rj_right])
#             elif valid_left:
#                 chosen_direction = rj_left
#             elif valid_right:
#                 chosen_direction = rj_right
#             else:
#                 chosen_direction = 0

#             if chosen_direction != 0:
#                 stre = self.posdistance((0, 0), (self.velocity[0], self.velocity[1]))
#                 angle += chosen_direction
#                 self.velocity[0] = stre * np.cos(angle)
#                 self.velocity[1] = stre * np.sin(angle)
#     # def move_random_direction(self):
#     #     dist = np.hypot(self.velocity[0], self.velocity[1])
#     #     self.angle = math.atan2(self.velocity[1], self.velocity[0])
#     #     self.angle += random.uniform(-0.5, 0.5)
#     #     self.velocity[0] = dist * math.cos(self.angle)*2
#     #     self.velocity[1] = dist * math.sin(self.angle)*2
    
#     def apply_separation(self, boids, separation_distance):
#         positions = [boid.position for boid in boids if boid != self and self.bdistance(boid) < separation_distance]
#         if not positions:return
#         # avg_pos = np.mean(positions, axis=0)
#         # dstx = avg_pos[0] - self.position[0];dsty = avg_pos[1] - self.position[1]
#         # distance = np.linalg.norm(avg_pos - self.position)
#         # self.velocity[0] -= self.separation_resolve * (dstx / distance) * 72
#         # self.velocity[1] -= self.separation_resolve * (dsty / distance) * 72
#         # return
#         '''V1 of separation'''
#         # for pos in positions:
#         #     totx = pos[0] - self.position[0]
#         #     toty = pos[1] - self.position[1]
#         #     totdist = self.posdistance((0, 0), (totx, toty))
#         #     self.velocity[0] -= (totx / totdist) * self.separation_resolve
#         #     self.velocity[1] -= (toty / totdist) * self.separation_resolve
#         '''V2 of separation'''
#         totxy = np.array(positions) - self.position
#         totdist = np.linalg.norm(totxy, axis=1)
#         semivel = np.sum(totxy / totdist[:, None], axis=0)
#         self.velocity[0] -= semivel[0] * self.separation_resolve
#         self.velocity[1] -= semivel[1] * self.separation_resolve
        
            

        

#         # move_vector = np.sum(self.position - close_boids, axis=0)
#         # disttoself = np.linalg.norm(move_vector)/(separation_distance*2)
#         # if disttoself < 0.8:
#         #     disttoself = 0.8
#         # dire = np.arctan2(move_vector[1], move_vector[0])
#         # self.velocity[0] += np.cos(dire)*self.separation_resolve*(separation_distance/disttoself)
#         # self.velocity[1] += np.sin(dire)*self.separation_resolve*(separation_distance/disttoself)
#         # self.velocity[0] += move_vector[0] * self.separation_resolve
#         # self.velocity[1] += move_vector[1] * self.separation_resolve
#         #optimize with numpy 

#         # move_x, move_y = 0, 0
#         # for other_boid in boids:
#         #     if other_boid != self and self.distance(other_boid) < separation_distance:
#         #         move_x += self.position[0] - other_boid.position[0]
#         #         move_y += self.position[1] - other_boid.position[1]
#         # self.velocity[0] += move_x * self.separation_resolve  # Apply a smaller fraction for smoother separation
#         # self.velocity[1] += move_y * self.separation_resolve  # Apply a smaller fraction for smoother separation

#     def apply_alignment(self, boids, alignment_distance):
#         velocities = [boid.velocity for boid in boids if boid != self and self.bdistance(boid) < alignment_distance and boid.fish_type == self.fish_type]
#         if not velocities:return
#         avg_velocity = np.mean(velocities, axis=0)
#         self.velocity[0] += (avg_velocity[0] - self.velocity[0]) * self.alignment_resolve
#         self.velocity[1] += (avg_velocity[1] - self.velocity[1]) * self.alignment_resolve
#         """ALIGNMENT def """
#         # avg_velocity_x, avg_velocity_y = 0, 0
#         # count = 0
#         # for other_boid in boids:
#         #     if other_boid != self and self.distance(other_boid) < alignment_distance and other_boid.fish_type == self.fish_type:
#         #         avg_velocity_x += other_boid.velocity[0]
#         #         avg_velocity_y += other_boid.velocity[1]
#         #         count += 1
#         # if count > 0:
#         #     avg_velocity_x /= count
#         #     avg_velocity_y /= count
#         #     self.velocity[0] += (avg_velocity_x - self.velocity[0]) * self.alignment_resolve
#         #     self.velocity[1] += (avg_velocity_y - self.velocity[1]) * self.alignment_resolve
#         # angle calc and abs(self.poscalc_angle((0,0),(boid.velocity[0],boid.velocity[1]))-self.bcalc_angle(boid.position)) < 60

#     def apply_cohesion(self, boids, cohesion_distance):
#         positions = [boid.position for boid in boids if boid != self and self.bdistance(boid) < cohesion_distance and boid.fish_type == self.fish_type ]
#         if not positions:return
#         avg_position = np.mean(positions, axis=0)
#         self.velocity[0] += (avg_position[0] - self.position[0]) * self.cohesion_resolve
#         self.velocity[1] += (avg_position[1] - self.position[1]) * self.cohesion_resolve
#         """COHESION def """
#         # avg_position_x, avg_position_y = 0, 0
#         # count = 0
#         # for other_boid in boids:
#         #     if other_boid != self and self.distance(other_boid) < cohesion_distance and other_boid.fish_type == self.fish_type:
#         #         avg_position_x += other_boid.position[0]
#         #         avg_position_y += other_boid.position[1]
#         #         count += 1
#         # if count > 0:
#         #     avg_position_x /= count
#         #     avg_position_y /= count
#         #     self.velocity[0] += (avg_position_x - self.position[0]) * self.cohesion_resolve
#             # self.velocity[1] += (avg_position_y - self.position[1]) * self.cohesion_resolve 
#             # and abs(self.poscalc_angle((0,0),(boid.velocity[0],boid.velocity[1]))-self.bcalc_angle(boid.position)) < 60
#     def apply_mouse_repulsion(self, mouse_pos, repulsion_distance, repulsion_strength):
#         distance_to_mouse = np.sqrt((self.position[0] - mouse_pos[0]) ** 2 + (self.position[1] - mouse_pos[1]) ** 2)
#         if distance_to_mouse < repulsion_distance:
#             angle = np.radians(self.poscalc_angle(mouse_pos,(self.position[0],self.position[1])))
#             strength = 2000/(distance_to_mouse+0.0000001)
#             if strength > 256:
#                 strength = 256
#             move_x = np.cos(angle)*strength
#             move_y = np.sin(angle)*strength
#             self.velocity[0] += move_x * repulsion_strength
#             self.velocity[1] += move_y * repulsion_strength
#     def limit_speed(self):
#         speed = self.posdistance((0, 0),(self.velocity[0], self.velocity[1]))
#         if speed > self.max_speed:
#             self.velocity[0] = (self.velocity[0] / speed) * self.max_speed
#             self.velocity[1] = (self.velocity[1] / speed) * self.max_speed
#         if speed < self.min_speed:
#             self.velocity[0] = (self.velocity[0] / speed) * self.min_speed
#             self.velocity[1] = (self.velocity[1] / speed) * self.min_speed
#     def find_food(self,x,y, foods, food_distance):
#         if len(foods) == 0:return None, None, None  # return None if no food is found
#         food_positions = np.array([[food.position[0], food.position[1]] for food in foods])
#         distances = np.sqrt((food_positions[:, 0] - x) ** 2 + (food_positions[:, 1] - y) ** 2)
#         if np.any(distances < food_distance):
#             closest_food_index = np.argmin(distances)
#             closest_food = foods[closest_food_index]
#             foodx, foody = closest_food.position
#             return foodx, foody, distances[closest_food_index]  # return the food and distance
#         return None, None, None  # return None if no food is found
    
#     def draw(self, screen,scale=1):      
#         sx,sy = retruescale(self.position[0],self.position[1],scale)
#         self.newimage = transform.scale(self.image, (int(self.fwidth*scale), int(self.fheight*scale)))
#         if self.velocity[0] < 0:self.newimage = transform.flip(self.newimage, False, True)
#         angle = self.poscalc_angle((self.velocity[1], self.velocity[0]),(0,0)) +90
#         self.newimage = transform.rotate(self.newimage,  angle)
#         nfwidth = self.newimage.get_width()
#         nfheight = self.newimage.get_height()
#         sx -=nfwidth/2
#         sy -= nfheight/2
#         # self.newimage = transform.rotate(self.newimage, self.angle)
#         if not (sx < -nfwidth*2 or sx > screen_width or sy< -nfheight*2 or sy > screen_height):
#             if scale > 0.1: screen.blit(self.newimage, (sx, sy))
#             else:pygame.draw.circle(screen, (255, 0, 0), (int(sx), int(sy)), 3)

#         # angle = np.radians(self.calculate_angle(target2=(self.velocity[0], self.velocity[1])))
#         # fsx,fsy = retruescale(self.position[0]+np.cos(angle)*10,self.position[1]+np.sin(angle)*10,scale)
#         # lefx,lefy = retruescale(self.position[0]+np.cos(angle+np.pi/2)*4,self.position[1]+np.sin(angle+np.pi/2)*4,scale)
#         # rigx,rigy = retruescale(self.position[0]-np.cos(angle+np.pi/2)*4,self.position[1]-np.sin(angle+np.pi/2)*4,scale)
#         # if self.fish_type == 'Gadidae Loan No':
#         #     color = (25, 255, 255)
#         # elif self.fish_type == 'Salmonidae':
#         #     color =  (200, 190, 120)
#         # else:
#         #     color = (255, 255, 255)
#         # pygame.draw.polygon(screen,color, [(rigx,rigy),(fsx,fsy),(lefx,lefy)], 0)
# class Zone:
#     def __init__(self, x, y, width, height,name=None):
#         self.rect = pygame.Rect(x, y, width, height)
#         self.name = name

#     def draw(self, screen):
#         pygame.draw.rect(screen, (0, 255, 0), self.rect, 2)
# # Main loop
# # @lru_cache(maxsize=None)

# def main():
#     global screen
#     global zones
#     global cx,cy,zoomx,zoomy
#     cx = screen_width/2
#     cy = screen_height/2
#     clock = pygame.time.Clock()
#     separation_distance = 54#32
#     alignment_distance = 55
#     cohesion_distance = 60
#     separation_resolve = 0.22#0.032
#     alignment_resolve = 0.06
#     cohesion_resolve = 0.024
#     repulsion_distance = 100
#     repulsion_strength = 0.05
#     top_speed = 5
#     fishima = os.path.join('assets', 'cod.png')
#     salmonela = os.path.join('assets', 'salmon.png')
#     tunala = os.path.join('assets', 'rainbow_fish.png')
#     background = os.path.join('assets', 'water.png')
#     font = pygame.font.Font(None, 36)
#     background = transform.scale(image.load(background), (screen_width, screen_height))
#     boids = []
#     zones = []
#     # vowels = ['a', 'e', 'i', 'o', 'u']
#     # consonants = ["b", "c", "d", "g", "h" , "k", "l", "m", "n", "p", "r", "s", "t", "v" , "y",]
#     # deconsonants = ["ef", "ieq"]
#     # lakhi = ["Ari", "vav","xav"]
#     # staria = ["zonea","ionea"]
#     val = 0
#     # for i in range(0):
#     #     rasx = random.randint(-60000, 60000) + screen_width // 2
#     #     rasy = random.randint(-60000, 60000) + screen_height // 2
#     #     dist = (np.hypot(rasx - screen_width / 2, rasy - screen_height / 2)/1000)
#     #     rasx -= screen_width // 2
#     #     rasy -= screen_height // 2
#     #     rasx *= dist**0.2
#     #     rasy *= dist**0.2
#     #     rasx += screen_width // 2
#     #     rasy += screen_height // 2
#     #     if dist > 1000:
#     #         dist = 1000
#     #     if dist < 1:
#     #         dist = 1 
#     #     raex = random.randint(50, 180)*dist**0.7 + screen_width // 2
#     #     raey = random.randint(50, 180)*dist**0.7 + screen_height // 2
#     #     angle = random.randint(0, 360)
#     #     for j in range(1):
#     #         angle += random.uniform(-5, 5)
#     #         tsx = math.cos((angle/180)*math.pi)*200
#     #         tsy = math.sin((angle/180)*math.pi)*200
#     #         rasx += tsx
#     #         rasy += tsy
#     #         name = random.choice(staria) + " "
#     #         for i in range(9):
#     #             if i % 2 == 0 and i != 0:
#     #                 name += random.choice(consonants)
#     #             elif i % 2 == 1 :
#     #                 name += random.choice(vowels)
#     #             elif i != 7:
#     #                 name += random.choice(deconsonants)
#     #             else:
#     #                 name += random.choice(lakhi)
#     #         zones.append(Zone(rasx, rasy, raex, raey,name=name))
#     zoomx = screen_width/2
#     zoomy = screen_height/2
#     scale = 1
#     listoffoods = []
#     def NewRturnM_scale(x,y,ascale):
#         msx = (x -screen_width/2)/ ascale + screen_width/2 + (screen_width/2 - zoomx);msy = (y -screen_height/2)/ ascale + screen_height/2 + (screen_height/2 - zoomy)
#         return msx,msy
#     for i in range(96):
#         randomwidth = random.uniform(32,34)
#         randomheight = int(randomwidth*16/36)
#         randomspx = random.uniform(-screen_width/2, screen_width/2) + screen_width // 2
#         randomspy = random.uniform(-screen_height/2, screen_height/2) + screen_height // 2
#         boids.append(Boid(screen_width, screen_height, separation_resolve, alignment_resolve, cohesion_resolve, top_speed, fishima, randomspx, randomspy, fish_type='Gadidae Loan No',width=randomwidth,height=randomheight,fleft=True))
#     # for i in range(24):
#     #     randomwidth = random.uniform(32,34)
#     #     randomheight = int(randomwidth*16/45)
#     #     randomspx = random.uniform(-screen_width/2, screen_width/2) + screen_width // 2
#     #     randomspy = random.uniform(-screen_height/2, screen_height/2) + screen_height // 2
#     #     boids.append(Boid(screen_width, screen_height, separation_resolve, alignment_resolve, cohesion_resolve, top_speed, salmonela, randomspx, randomspy, fish_type='Salmonidae',width=randomwidth,height=randomheight))
#         # randomwidth = random.uniform(14,72)
#         # randomheight = int(randomwidth*16/14)
#         # boids.append(Boid(screen_width, screen_height, separation_resolve, alignment_resolve, cohesion_resolve, top_speed, tunala, random.uniform(0, screen_width), random.uniform(0, screen_height), fish_type='rainbow',width=randomwidth,height=randomheight))
#     running = True
#     # water = Water(600, 450, 60)
#     # water = transform.scale(water.texture, (screen_width, screen_height))
#     startpos = None
#     endpos = None
#     mouse_x,mouse_y = pygame.mouse.get_pos()
#     aascale = 1
#     msx , msy = NewRturnM_scale(mouse_x,mouse_y,aascale)
#     prevsx = msx
#     prevsy = msy
#     rframe = 0
#     natboid = np.array([])
#     noneboids = []
#     icon = pygame.image.load(os.path.join('assets', 'logo.webp'))
#     icon = pygame.transform.scale(icon, (screen_width, screen_height))
#     esceed = False
#     lframe = 120
#     esctimer = 60

#     for i in range(lframe+esctimer):
#         if esceed:
#             break
#         i = max(0,i)
#         ie = 255-i/(lframe/255)
#         screen.fill((45, 233, 199))
#         icon.set_alpha(ie)
#         screen.blit(icon, (0, 0))
#         pygame.display.flip()

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 esceed = True  
#         clock.tick(120)
#     timerr = 1
#     curtime = time.time()
    
#     while running:
#         aascale = abs(scale)
#         rascale = min(1,aascale)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False

#                 # if event.key == pygame.K_m:
#                 #     startpos = pygame.mouse.get_pos()
#                 #     sx = (startpos[0]  - screen_width/2)/ aascale + screen_width/2+ (screen_width/2 - zoomx)
#                 #     sy = (startpos[1] -screen_height/2)/ aascale + screen_height/2 + (screen_height/2 - zoomy)
#                 #     startpos = (sx,sy)
#                 # if event.key == pygame.K_n:
#                 #     endpos = pygame.mouse.get_pos()
#                 #     sx = (endpos[0]  - screen_width/2)/ aascale + screen_width/2+ (screen_width/2 - zoomx)
#                 #     sy = (endpos[1] -screen_height/2)/ aascale + screen_height/2 + (screen_height/2 - zoomy)
#                 #     endpos = (sx,sy)
#         wsx,wsy = retruescale(0,0,rascale)
#         screen.fill(BLACK)
#         pygame.draw.rect(screen, (0, 100, 255), (wsx,wsy, screen_width*rascale, screen_height*rascale))
#         # pygame.draw.circle(screen, (0, 80, 255), (int(screen_width/2), int(screen_height/2)), 1*aascale)

        
#         mouse_x,mouse_y = pygame.mouse.get_pos()
#         # if startpos is not None and endpos is not None:
#         #     name = random.choice(staria) + " "
#         #     for i in range(9):
#         #         if i % 2 == 0 and i != 0:
#         #             name += random.choice(consonants)
#         #         elif i % 2 == 1 :
#         #             name += random.choice(vowels)
#         #         elif i != 7:
#         #             name += random.choice(deconsonants)
#         #         else:
#         #             name += random.choice(lakhi)
#         #     if startpos[0] < endpos[0]:
#         #         zones.append(Zone(startpos[0], startpos[1], endpos[0]-startpos[0], endpos[1]-startpos[1],name=name))
#         #     else:
#         #         zones.append(Zone(endpos[0], endpos[1], startpos[0]-endpos[0], startpos[1]-endpos[1],name=name))
#             # startpos = None
#             # endpos = None
#         msx,msy = NewRturnM_scale(mouse_x,mouse_y,aascale)
#         # print(sx,sy,startpos,endpos)
#         # print(sx,sy)
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_UP]:
#             zoomy += 100
#         if keys[pygame.K_DOWN]:
#             zoomy -= 100
#         if keys[pygame.K_LEFT]:
#             zoomx += 100
#         if keys[pygame.K_RIGHT]:
#             zoomx -= 100
#         if keys[pygame.K_w]:
#             listoffoods.append(Food(msx,msy))
#         if keys[pygame.K_s]:
#             listdst = np.array([np.sqrt((food.position[0] - msx) ** 2 + (food.position[1] - msy) ** 2) for food in listoffoods])
#             if np.any(listdst < 100):
#                 listoffoods.pop(np.argmin(listdst))
#         if keys[pygame.K_e]:
#             val += 0.05 * 2
#         if keys[pygame.K_q]:
#             val -= 0.05 * 2
#         if keys[pygame.K_d]:
#             if keys[pygame.K_1]:
#                 separation_resolve += 0.05
#             if keys[pygame.K_2]:
#                 separation_resolve -= 0.05
#             separation_resolve = round(separation_resolve,16)
#             for boid in boids:
#                 boid.separation_resolve = separation_resolve
#             print(separation_resolve)

#         if keys[pygame.K_a]:
#             if keys[pygame.K_1]:
#                 alignment_resolve += 0.05
#             if keys[pygame.K_2]:
#                 alignment_resolve -= 0.05
#             alignment_resolve = round(alignment_resolve,16)
#             for boid in boids:
#                 boid.alignment_resolve = alignment_resolve
#             print(alignment_resolve)

#         if keys[pygame.K_c]:
#             if keys[pygame.K_1]:
#                 cohesion_resolve += 0.05
#             if keys[pygame.K_2]:
#                 cohesion_resolve -= 0.05
#             cohesion_resolve = round(cohesion_resolve,16)
#             for boid in boids:
#                 boid.cohesion_resolve = cohesion_resolve
#             print(cohesion_resolve)

        
#         if keys[pygame.K_f]:prf = True;pygame.draw.circle(screen, (255, 0, 0), (mouse_x, mouse_y), 100, 5)
#         else:prf = False
        
        
#         for boid in natboid:
#             boid.allowmove = False
#             boid.position[0] += msx - prevsx;boid.position[1] += msy - prevsy
#         nboids = np.array(boids)
#         listdst = np.array([np.sqrt((boid.position[0] - msx) ** 2 + (boid.position[1] - msy) ** 2) for boid in nboids])
#         if prf:natboid = nboids[listdst < (100/aascale)];noneboids = nboids[listdst >= (100/aascale)] 
#         else:
#             natboid = np.array([]);noneboids = nboids
#         for boid in noneboids:boid.allowmove = True

#         # for boid in boids:
#         #     if not boid.allowmove:
#         #         boid.position[0] += msx - prevsx
#         #         boid.position[1] += msy - prevsy
#         #     dist = np.hypot(boid.position[0] - msx, boid.position[1] - msy)
#         #     if dist < 100/aascale and prf:
#         #         boid.allowmove = False
#         #     else:
#         #         boid.allowmove = True
#         scale = (2**(val))
#         # cx = zoomx*scale
#         # cy = zoomy*scale

#         # for zone in zones:
#         #     asx = (zone.rect[0]-(screen_width/2-zoomx)-screen_width/2) * aascale + screen_width/2
#         #     asy = (zone.rect[1]-(screen_height/2-zoomy)-screen_height/2) * aascale + screen_height/2

#         #     if zone.rect[2]*aascale < 3 or zone.rect[3]*aascale < 3:
#         #         pygame.draw.circle(screen, (0, 255, 0), (int(asx), int(asy)), 1)
#         #     else:
#         #         pygame.draw.rect(screen, (0, 255, 0), (asx,asy,zone.rect[2]*aascale,zone.rect[3]*aascale))
#         #     # if zone.rect.collidepoint(sx,sy):
#         #     #     print(zone.name)
#         if pygame.mouse.get_pressed()[0]:
#             pygame.draw.circle(screen, (255, 0, 0), (mouse_x,mouse_y), repulsion_distance,5)
#             def mouserpress(strength):
#                 aboid = np.array(boids)
#                 listdst = np.array([np.sqrt((boid.position[0] - msx) ** 2 + (boid.position[1] - msy) ** 2) for boid in aboid])
#                 aboid = aboid[np.where(listdst < repulsion_distance/aascale)]
#                 for boid in aboid:
#                     boid.apply_mouse_repulsion((msx,msy), repulsion_distance/aascale, strength)
#             if keys[pygame.K_x]:
#                 mouserpress(-repulsion_strength/aascale)
#             else:mouserpress(repulsion_strength/aascale)
#         # pygame.draw.circle(screen, (255, 0, 0), (int(sx), int(sy)), 10, 5)
#         # print(sx,sy,scale)
#         # @lru_cache(maxsize=2000)
#         def boidsim():
#             """Main boid simulation loop"""
#             # for boid in boids:
#             #     if boid.allowmove:
#             #         for i in range(len(boid.trail)-1):
#             #             rx = (boid.trail[i][0]-(screen_width/2-zoomx)-screen_width/2) * aascale + screen_width/2
#             #             ry = (boid.trail[i][1]-(screen_height/2-zoomy)-screen_height/2) * aascale + screen_height/2
#             #             erx = (boid.trail[i+1][0]-(screen_width/2-zoomx)-screen_width/2) * aascale + screen_width/2
#             #             ery = (boid.trail[i+1][1]-(screen_height/2-zoomy)-screen_height/2) * aascale + screen_height/2
#             #             c = (255/boid.sframe)*i
#             #             pygame.draw.line(screen, (c, c, c), (rx, ry), (erx, ery), 1)
#             for boid in boids:
#                 if boid.allowmove:
#                     boid.apply_separation(boids, separation_distance)
#                     boid.apply_alignment(boids, alignment_distance)
#                     boid.apply_cohesion(boids, cohesion_distance)
#                     # foodx ,foody,dist = boid.find_food(boid.position[0],boid.position[1],listoffoods, 32)
#                     # if foodx is not None or foody is not None:
#                     #     direction = np.arctan2(foody - boid.position[1], foodx - boid.position[0])
#                     #     boid.velocity[0] += np.cos(direction)*0.6
#                     #     boid.velocity[1] += np.sin(direction)*0.6

#                     boid.velocity[0]*=0.999
#                     boid.velocity[1]*=0.999
#                     boid.update_position()
#                     # if abs(boid.velocity[0]) >2 and abs(boid.velocity[1]) >2:
#                     #     boid.velocity[0]*=0.99
#                     #     boid.velocity[1]*=0.99
#                     #     # pygame.draw.circle(screen, (255, 255, 255), (int(trail[0]), int(trail[1])), 1)
#                 # else:
#                 #     boid.trail = []
#                 boid.draw(screen,scale=aascale)
#         boidsim()
#         for food in listoffoods:
#             x,y = retruescale(food.position[0],food.position[1],aascale)
#             screen.blit(food.image, (x, y))
#         if mouse_x < 120:
#             timerr = time.time();delta = timerr - curtime;curfps = 1/delta
#             truefps = clock.get_fps();var = round(truefps-curfps,2);textfps = font.render(f"Fps:{round(truefps,1)}|{round(curfps,1)}||{var}",True,(255,215,0));screen.blit(textfps, (10, 10));curtime = timerr
#             # rframe =round(rframe+var,2)
#             # pygame.draw.circle(screen, (255, 0, 0), (200,(var*10)+screen_height/2), 6)
#         prevsx = msx;prevsy = msy
#         pygame.display.flip()
#         clock.tick(120)
#     pygame.quit()
# if __name__ == "__main__":
#     main()
#takeown /f "D:\Program Files" /r /d y, Adminstrator run
#icacls "D:\Program Files" /grant %username%:F /t
import pygame;
import random;
import os
import time as tm;
import numpy as np;
from functools import lru_cache;


# def lru_cache():
# Initialize Pygame
pygame.init()
# Screen dimensions
ratio = 12/9
screen_width = 1200
screen_height = screen_width / ratio
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("🇭🇮🇫🇱🇦🇷🇾 (🇸🇮🇲🇺🇱🇦🇹🇮🇴🇳)")
icon = pygame.image.load(os.path.join('assets', 'logo.webp'))
icon = pygame.transform.scale(icon, (128, 128))
pygame.display.set_icon(icon)
# Colors 
# 
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# BLUE = (0, 0, 255)
# LIGHT_BLUE = (173, 216, 230)
# @lru_cache(maxsize=1024)

def retruescale(x,y,ascale):
    # wsx = (x-(screen_width/2-zoomx)-screen_width/2) * ascale + screen_width/2;wsy = (y-(screen_height/2-zoomy)-screen_height/2) * ascale + screen_height/2
    rews = ((x-(screen_width/2-zoomx)-screen_width/2) * ascale + screen_width/2),(y-(screen_height/2-zoomy)-screen_height/2) * ascale + screen_height/2
    return rews
class Food:
    def __init__(self, x, y):
        self.position = [x, y]
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'goldbar.png')), (16, 16)) 
class Boid:
    def __init__(self, screen_width:int, screen_height:int, separation_resolve=0.2, alignment_resolve=0.03, cohesion_resolve=0.02, top_speed=4.5, fishima=None, x=None, y=None, fish_type='fish',width=36,height=16,bx=0,by=0,bex=screen_width,bey=screen_height,fleft = False,ftop = False):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.position = np.array([x, y], dtype=float)
        self.velocity = np.array([top_speed,top_speed], dtype=float)
        self.velocity[0] *= round(random.choice([-1, 1]), 2)
        self.velocity[1] *= round(random.choice([-1, 1]), 2)
        self.angle = np.degrees(np.atan2(self.velocity[1], -self.velocity[0]))
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
        self.image = pygame.transform.scale(pygame.image.load(fishima), (width, height))
        self.image = pygame.transform.flip(self.image, fleft, ftop)
        self.fish_type = fish_type  # Add fish type attribute
        self.allowmove = True
        # self.trail = []
        # self.frame = 0
        # self.sframe = 36
    @lru_cache(maxsize=3000)
    def bdistance(self, other_boid):
        return np.hypot(self.position[0] - other_boid.position[0], self.position[1] - other_boid.position[1])
    @lru_cache(maxsize=3000)
    def posdistance(self, fipos=(0,0),lipos=None):
        return np.sqrt((lipos[0] - fipos[0]) ** 2 + (lipos[1] - fipos[1]) ** 2)
    def bcalc_angle(self, target=(0,0)):
        return np.arctan2(target[1] - self.position[1], target[0] - self.position[0])
    @lru_cache(maxsize=3000)
    def poscalc_angle(self, target,target2):
        return np.degrees(np.arctan2(target2[1] - target[1], target2[0] - target[0]))
    def update_position(self):
        self.check_bounds()
        self.limit_speed()
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        # self.position += self.velocity
        # self.frame += 1
        # if self.frame % 2 == 0:
        #     self.trail.append([self.position[0], self.position[1], self.sframe])  # Change to list
        # self.frame %= 2
        # for trail in self.trail:
        #     trail[2] -= 1
        #     if trail[2] < 0:
        #         self.trail.remove(trail)

    def check_bounds(self):       
        margin = 24 # Distance from the edge to start turning
        turn_factor = 0.25
        if self.position[0] < margin:
            self.velocity[0] += turn_factor
            # self.position[0] = self.screen_width - margin
        elif self.position[0] > self.screen_width - margin:
            self.velocity[0] -= turn_factor
            # self.position[0] =  margin
        if self.position[1] < margin:
            self.velocity[1] += turn_factor
            # self.position[1] = self.screen_height - margin
        elif self.position[1] > self.screen_height - margin:
            self.velocity[1] -= turn_factor
            # self.position[1] = margin

        # if (self.position[0] < 0 or self.position[0] > self.screen_width or self.position[1] < 0 or self.position[1] > self.screen_height) and self.campzone == 0:
        #     angle = math.atan2(self.position[1] - self.screen_height / 2, self.position[0] - self.screen_width / 2)
        #     self.velocity[0] -= math.cos(angle)*turn_factor
        #     self.velocity[1] -= math.sin(angle)*turn_factor
        #     # self.position[0] = min(self.screen_width, max(0, self.position[0]))
        #+     # self.position[1] = min(self.screen_height, max(0, self.position[1]))
        #+ old code top
        #+ new code bottom
        def check_bounde(x,y):
            return x >= self.barrierx and x <= self.barrierex and y >= self.barriery and y<= self.barrierey
        if self.position[0] < self.barrierx+margin or self.position[0] > self.barrierex-margin or self.position[1] < self.barriery+margin or self.position[1] > self.barrierey-margin:
            angle = np.radians(self.poscalc_angle((0,0),(self.velocity[0],self.velocity[1])))
            jdir_left = 0
            jdir_right = 0
            valid_left = False
            valid_right = False

            valid_left_count = 0
            valid_right_count = 0
            chosen_direction = 0
            for k in range(0, 18):
                x_left = self.position[0]
                y_left = self.position[1]
                x_right = self.position[0]
                y_right = self.position[1]
                rj_left = np.radians(jdir_left)
                rj_right = np.radians(-jdir_right)
                x_left += np.cos(angle + rj_left) * 32
                y_left += np.sin(angle + rj_left) * 32
                x_right += np.cos(angle + rj_right) * 32
                y_right += np.sin(angle + rj_right) * 32
                
                if check_bounde(x_left,y_left):
                    valid_left = True
                    valid_left_count += 1
                if check_bounde(x_right,y_right):
                    valid_right = True
                    valid_right_count += 1

                if valid_left or valid_right:
                    break

                jdir_left += 5
                jdir_right += 5

            if valid_left and valid_right:
                if valid_left_count < valid_right_count:
                    chosen_direction = rj_left
                elif valid_right_count < valid_left_count:
                    chosen_direction = rj_right
                else:
                    chosen_direction = random.choice([rj_left, rj_right])
            elif valid_left:
                chosen_direction = rj_left
            elif valid_right:
                chosen_direction = rj_right

            if chosen_direction != 0:
                stre = self.posdistance((0, 0), (self.velocity[0], self.velocity[1]))
                angle += chosen_direction
                self.velocity[0] = stre * np.cos(angle)
                self.velocity[1] = stre * np.sin(angle)
    # def move_random_direction(self):
    #     dist = np.hypot(self.velocity[0], self.velocity[1])
    #     self.angle = math.atan2(self.velocity[1], self.velocity[0])
    #     self.angle += random.uniform(-0.5, 0.5)
    #     self.velocity[0] = dist * math.cos(self.angle)*2
    #     self.velocity[1] = dist * math.sin(self.angle)*2
    
    def apply_separation(self, boids, separation_distance):
        positions = [boid.position-self.position for boid in boids if boid != self and self.bdistance(boid) < separation_distance]
        if not positions:return
        '''V1 of separation'''
        # for pos in positions:
        #     totx = pos[0] - self.position[0]
        #     toty = pos[1] - self.position[1]
        #     totdist = self.posdistance((0, 0), (totx, toty))
        #     self.velocity[0] -= (totx / totdist) * self.separation_resolve
        #     self.velocity[1] -= (toty / totdist) * self.separation_resolve
        '''V2 of separation'''
        # totxy = np.array(positions) - self.position
        totdist = np.linalg.norm(positions, axis=1)
        semivel = np.sum(positions / totdist[:, np.newaxis], axis=0)
        self.velocity -= semivel * self.separation_resolve
        

        # move_x, move_y = 0, 0
        # for other_boid in boids:
        #     if other_boid != self and self.distance(other_boid) < separation_distance:
        #         move_x += self.position[0] - other_boid.position[0]
        #         move_y += self.position[1] - other_boid.position[1]
        # self.velocity[0] += move_x * self.separation_resolve  # Apply a smaller fraction for smoother separation
        # self.velocity[1] += move_y * self.separation_resolve  # Apply a smaller fraction for smoother separation

    def apply_alignment(self, boids, alignment_distance):
        """ALIGNMENT def"""
        velocities = [boid.velocity for boid in boids if boid != self and self.bdistance(boid) < alignment_distance #and boid.fish_type == self.fish_type 
                    #  and abs(self.poscalc_angle((0,0),(boid.velocity[0],boid.velocity[1]))-np.degrees(self.bcalc_angle(boid.position))) < 60
                    ]
        if not velocities:return
        avg_velocity = np.mean(velocities, axis=0)
        self.velocity[0] += (avg_velocity[0] - self.velocity[0]) * self.alignment_resolve
        self.velocity[1] += (avg_velocity[1] - self.velocity[1]) * self.alignment_resolve


    def apply_cohesion(self, boids, cohesion_distance):
        positions =  [boid.position for boid in boids if boid != self and self.bdistance(boid) < cohesion_distance #and boid.fish_type == self.fish_type
                    #  and abs(self.poscalc_angle((0,0),(boid.velocity[0],boid.velocity[1]))-np.degrees(self.bcalc_angle(boid.position))) < 60
                    ]
        if not positions:return
        avg_position = np.mean(positions, axis=0)
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
    def apply_mouse_repulsion(self, mouse_pos, repulsion_distance, repulsion_strength):
        distance_to_mouse = np.sqrt((self.position[0] - mouse_pos[0]) ** 2 + (self.position[1] - mouse_pos[1]) ** 2)
        if distance_to_mouse < repulsion_distance:
            angle = np.radians(self.poscalc_angle(mouse_pos,(self.position[0],self.position[1])))
            strength = 2000/(distance_to_mouse+0.0000001)
            if strength > 256:
                strength = 256
            move_x = np.cos(angle)*strength
            move_y = np.sin(angle)*strength
            self.velocity[0] += move_x * repulsion_strength
            self.velocity[1] += move_y * repulsion_strength
    def limit_speed(self):
        speed = self.posdistance((0, 0),(self.velocity[0], self.velocity[1]))
        if speed > self.max_speed:
            self.velocity[0] = (self.velocity[0] / speed) * self.max_speed
            self.velocity[1] = (self.velocity[1] / speed) * self.max_speed
        if speed < self.min_speed:
            self.velocity[0] = (self.velocity[0] / speed) * self.min_speed
            self.velocity[1] = (self.velocity[1] / speed) * self.min_speed
    def find_food(self,x,y, foods, food_distance):
        if len(foods) == 0:return None, None, None  # return None if no food is found
        food_positions = np.array([[food.position[0], food.position[1]] for food in foods])
        distances = np.sqrt((food_positions[:, 0] - x) ** 2 + (food_positions[:, 1] - y) ** 2)
        if np.any(distances < food_distance):
            closest_food_index = np.argmin(distances)
            closest_food = foods[closest_food_index]
            foodx, foody = closest_food.position
            return foodx, foody, distances[closest_food_index]  # return the food and distance
        return None, None, None  # return None if no food is found  
    def draw(self, screen,scale=1):      
        # sx,sy = retruescale(self.position[0],self.position[1],scale)
        # self.newimage = transform.scale(self.image, (int(self.fwidth*scale), int(self.fheight*scale)))
        # if self.velocity[0] < 0:self.newimage = transform.flip(self.newimage, False, True)
        # angle = self.poscalc_angle((self.velocity[1], self.velocity[0]),(0,0)) +90
        # self.newimage = transform.rotate(self.newimage,  angle)
        # nfwidth = self.newimage.get_width()
        # nfheight = self.newimage.get_height()
        # sx -=nfwidth/2
        # sy -= nfheight/2
        # # self.newimage = transform.rotate(self.newimage, self.angle)
        # if not (sx < -nfwidth*2 or sx > screen_width or sy< -nfheight*2 or sy > screen_height):
        #     if scale > 0.1: screen.blit(self.newimage, (sx, sy))
        #     else:pygame.draw.circle(screen, (255, 0, 0), (int(sx), int(sy)), 3)
        angle = np.radians(self.poscalc_angle((0,0),(self.velocity[0], self.velocity[1])))
        fsx,fsy = retruescale(self.position[0]+np.cos(angle)*10,self.position[1]+np.sin(angle)*10,scale)
        lefx,lefy = retruescale(self.position[0]+np.cos(angle+np.pi/2)*4,self.position[1]+np.sin(angle+np.pi/2)*4,scale)
        rigx,rigy = retruescale(self.position[0]-np.cos(angle+np.pi/2)*4,self.position[1]-np.sin(angle+np.pi/2)*4,scale)
        if self.fish_type == 'Gadidae':
            color = (25, 255, 255)
        elif self.fish_type == 'Salmonidae':
            color =  (200, 190, 120)
        else:
            color = (255, 255, 255)
        pygame.draw.polygon(screen,color, [(rigx,rigy),(fsx,fsy),(lefx,lefy)], 0)
class Zone:
    def __init__(self, x, y, width, height,name=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.name = name

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect, 2)
# Main loop
def main():
    global screen
    global zones
    global cx,cy,zoomx,zoomy
    cx = screen_width/2
    cy = screen_height/2
    clock = pygame.time.Clock()
    separation_distance = 55#32
    alignment_distance = 56.5
    cohesion_distance = 57.5
    separation_resolve = 0.22#0.032
    alignment_resolve = 0.06
    cohesion_resolve = 0.024
    repulsion_distance = 100
    repulsion_strength = 0.05
    top_speed = 5
    fishima = os.path.join('assets', 'cod.png')
    salmonela = os.path.join('assets', 'salmon.png')
    tunala = os.path.join('assets', 'rainbow_fish.png')
    background = os.path.join('assets', 'water.png')
    font = pygame.font.Font(None, 36)
    background = pygame.transform.scale(pygame.image.load(background), (screen_width, screen_height))
    boids = []
    zones = []
    # vowels = ['a', 'e', 'i', 'o', 'u']
    # consonants = ["b", "c", "d", "g", "h" , "k", "l", "m", "n", "p", "r", "s", "t", "v" , "y",]
    # deconsonants = ["ef", "ieq"]
    # lakhi = ["Ari", "vav","xav"]
    # staria = ["zonea","ionea"]
    val = 0
    # for i in range(0):
    #     rasx = random.randint(-60000, 60000) + screen_width // 2
    #     rasy = random.randint(-60000, 60000) + screen_height // 2
    #     dist = (np.hypot(rasx - screen_width / 2, rasy - screen_height / 2)/1000)
    #     rasx -= screen_width // 2
    #     rasy -= screen_height // 2
    #     rasx *= dist**0.2
    #     rasy *= dist**0.2
    #     rasx += screen_width // 2
    #     rasy += screen_height // 2
    #     if dist > 1000:
    #         dist = 1000
    #     if dist < 1:
    #         dist = 1 
    #     raex = random.randint(50, 180)*dist**0.7 + screen_width // 2
    #     raey = random.randint(50, 180)*dist**0.7 + screen_height // 2
    #     angle = random.randint(0, 360)
    #     for j in range(1):
    #         angle += random.uniform(-5, 5)
    #         tsx = math.cos((angle/180)*math.pi)*200
    #         tsy = math.sin((angle/180)*math.pi)*200
    #         rasx += tsx
    #         rasy += tsy
    #         name = random.choice(staria) + " "
    #         for i in range(9):
    #             if i % 2 == 0 and i != 0:
    #                 name += random.choice(consonants)
    #             elif i % 2 == 1 :
    #                 name += random.choice(vowels)
    #             elif i != 7:
    #                 name += random.choice(deconsonants)
    #             else:
    #                 name += random.choice(lakhi)
    #         zones.append(Zone(rasx, rasy, raex, raey,name=name))
    zoomx = screen_width/2
    zoomy = screen_height/2
    scale = 1
    listoffoods = []
    def NewRturnM_scale(x,y,ascale):
        msx = (x -screen_width/2)/ ascale + screen_width/2 + (screen_width/2 - zoomx);msy = (y -screen_height/2)/ ascale + screen_height/2 + (screen_height/2 - zoomy)
        return msx,msy
    for i in range(96):
        randomwidth = random.uniform(32,34)
        randomheight = int(randomwidth*16/36)
        randomspx = random.uniform(-screen_width/2, screen_width/2) + screen_width // 2
        randomspy = random.uniform(-screen_height/2, screen_height/2) + screen_height // 2
        boids.append(Boid(screen_width, screen_height, separation_resolve, alignment_resolve, cohesion_resolve, top_speed, fishima, randomspx, randomspy, fish_type='Gadidae',width=randomwidth,height=randomheight,fleft=True))
    # for i in range(24):
    #     randomwidth = random.uniform(32,34)
    #     randomheight = int(randomwidth*16/45)
    #     randomspx = random.uniform(-screen_width/2, screen_width/2) + screen_width // 2
    #     randomspy = random.uniform(-screen_height/2, screen_height/2) + screen_height // 2
    #     boids.append(Boid(screen_width, screen_height, separation_resolve, alignment_resolve, cohesion_resolve, top_speed, salmonela, randomspx, randomspy, fish_type='Salmonidae',width=randomwidth,height=randomheight))
        # randomwidth = random.uniform(14,72)
        # randomheight = int(randomwidth*16/14)
        # boids.append(Boid(screen_width, screen_height, separation_resolve, alignment_resolve, cohesion_resolve, top_speed, tunala, random.uniform(0, screen_width), random.uniform(0, screen_height), fish_type='rainbow',width=randomwidth,height=randomheight))
    running = True
    # water = Water(600, 450, 60)
    # water = transform.scale(water.texture, (screen_width, screen_height))
    startpos = None
    endpos = None
    mouse_x,mouse_y = pygame.mouse.get_pos()
    aascale = 1
    msx , msy = NewRturnM_scale(mouse_x,mouse_y,aascale)
    prevsx = msx
    prevsy = msy
    rframe = 0
    # arrayy = np.array([12,12])
    # narray = arrayy / np.array([12,12])
    natboid = np.array([])
    noneboids = []
    icon = pygame.image.load(os.path.join('assets', 'logo.webp'))
    icon = pygame.transform.scale(icon, (screen_width, screen_height))
    esceed = False
    lframe = 120
    esctimer = 60
    for i in range(lframe+esctimer):
        if esceed:
            break
        i = max(0,i)
        ie = 255-i/(lframe/255)
        screen.fill((45, 233, 199))
        icon.set_alpha(ie)
        screen.blit(icon, (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                esceed = True  
        clock.tick(120)
    timerr = 1
    curtime = tm.time()
    while running:
        aascale = abs(scale)
        rascale = min(1,aascale)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                # if event.key == pygame.K_m:
                #     startpos = pygame.mouse.get_pos()
                #     sx = (startpos[0]  - screen_width/2)/ aascale + screen_width/2+ (screen_width/2 - zoomx)
                #     sy = (startpos[1] -screen_height/2)/ aascale + screen_height/2 + (screen_height/2 - zoomy)
                #     startpos = (sx,sy)
                # if event.key == pygame.K_n:
                #     endpos = pygame.mouse.get_pos()
                #     sx = (endpos[0]  - screen_width/2)/ aascale + screen_width/2+ (screen_width/2 - zoomx)
                #     sy = (endpos[1] -screen_height/2)/ aascale + screen_height/2 + (screen_height/2 - zoomy)
                #     endpos = (sx,sy)
        screen.fill((0,0,0))
        pygame.draw.rect(screen, (0, 100, 255), (*retruescale(0,0,rascale), screen_width*rascale, screen_height*rascale))
        # pygame.draw.circle(screen, (0, 80, 255), (int(screen_width/2), int(screen_height/2)), 1*aascale)
        mouse_x,mouse_y = pygame.mouse.get_pos()
        # if startpos is not None and endpos is not None:
        #     name = random.choice(staria) + " "
        #     for i in range(9):
        #         if i % 2 == 0 and i != 0:
        #             name += random.choice(consonants)
        #         elif i % 2 == 1 :
        #             name += random.choice(vowels)
        #         elif i != 7:
        #             name += random.choice(deconsonants)
        #         else:
        #             name += random.choice(lakhi)
        #     if startpos[0] < endpos[0]:
        #         zones.append(Zone(startpos[0], startpos[1], endpos[0]-startpos[0], endpos[1]-startpos[1],name=name))
        #     else:
        #         zones.append(Zone(endpos[0], endpos[1], startpos[0]-endpos[0], startpos[1]-endpos[1],name=name))
            # startpos = None
            # endpos = None
        msx,msy = NewRturnM_scale(mouse_x,mouse_y,aascale)
        # print(sx,sy,startpos,endpos)
        # print(sx,sy)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            zoomy += 100
        if keys[pygame.K_DOWN]:
            zoomy -= 100
        if keys[pygame.K_LEFT]:
            zoomx += 100
        if keys[pygame.K_RIGHT]:
            zoomx -= 100
        if keys[pygame.K_w]:
            listoffoods.append(Food(msx,msy))
        if keys[pygame.K_s]:
            listdst = np.array([np.sqrt((food.position[0] - msx) ** 2 + (food.position[1] - msy) ** 2) for food in listoffoods])
            if np.any(listdst < 100):
                listoffoods.pop(np.argmin(listdst))
        if keys[pygame.K_e]:
            val += 0.05 * 2
        if keys[pygame.K_q]:
            val -= 0.05 * 2
        if keys[pygame.K_d]:
            if keys[pygame.K_1]:
                separation_resolve += 0.05
            if keys[pygame.K_2]:
                separation_resolve -= 0.05
            separation_resolve = round(separation_resolve,16)
            for boid in boids:
                boid.separation_resolve = separation_resolve
            print(separation_resolve)

        if keys[pygame.K_a]:
            if keys[pygame.K_1]:
                alignment_resolve += 0.05
            if keys[pygame.K_2]:
                alignment_resolve -= 0.05
            alignment_resolve = round(alignment_resolve,16)
            for boid in boids:
                boid.alignment_resolve = alignment_resolve
            print(alignment_resolve)

        if keys[pygame.K_c]:
            if keys[pygame.K_1]:
                cohesion_resolve += 0.05
            if keys[pygame.K_2]:
                cohesion_resolve -= 0.05
            cohesion_resolve = round(cohesion_resolve,16)
            for boid in boids:
                boid.cohesion_resolve = cohesion_resolve
            print(cohesion_resolve)

        
        if keys[pygame.K_f]:prf = True;pygame.draw.circle(screen, (255, 0, 0), (mouse_x, mouse_y), 100, 5)
        else:prf = False
        
        
        for boid in noneboids:boid.allowmove = True
        for boid in natboid:
            boid.allowmove = False
            boid.position[0] += msx - prevsx;boid.position[1] += msy - prevsy
        nboids = np.array(boids)
        listdst = np.array([np.sqrt((boid.position[0] - msx) ** 2 + (boid.position[1] - msy) ** 2) for boid in nboids])
        if prf:natboid = nboids[listdst < (100/aascale)];noneboids = nboids[listdst >= (100/aascale)] 
        else:
            natboid = np.array([]);noneboids = nboids


        # for boid in boids:
        #     if not boid.allowmove:
        #         boid.position[0] += msx - prevsx
        #         boid.position[1] += msy - prevsy
        #     dist = np.hypot(boid.position[0] - msx, boid.position[1] - msy)
        #     if dist < 100/aascale and prf:
        #         boid.allowmove = False
        #     else:
        #         boid.allowmove = True
        scale = (2**(val))
        if pygame.mouse.get_pressed()[0]:
            pygame.draw.circle(screen, (255, 0, 0), (mouse_x,mouse_y), repulsion_distance,5)
            def mouserpress(strength):
                aboid = np.array(boids)
                listdst = np.array([np.sqrt((boid.position[0] - msx) ** 2 + (boid.position[1] - msy) ** 2) for boid in aboid])
                aboid = aboid[np.where(listdst < repulsion_distance/aascale)]
                for boid in aboid:
                    boid.apply_mouse_repulsion((msx,msy), repulsion_distance/aascale, strength)
            if keys[pygame.K_x]:
                mouserpress(-repulsion_strength/aascale)
            else:mouserpress(repulsion_strength/aascale)
        # pygame.draw.circle(screen, (255, 0, 0), (int(sx), int(sy)), 10, 5)
        # print(sx,sy,scale)
        # @lru_cache(maxsize=2000)
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
            #             pygame.draw.line(screen, (c, c, c), (rx, ry), (erx, ery), 1)
            for boid in boids:
                if boid.allowmove:
                    boid.apply_separation(boids, separation_distance)
                    boid.apply_alignment(boids, alignment_distance)
                    boid.apply_cohesion(boids, cohesion_distance)
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
                    #     # pygame.draw.circle(screen, (255, 255, 255), (int(trail[0]), int(trail[1])), 1)
                # else:

                #     boid.trail = []
                boid.draw(screen,scale=aascale)
        boidsim()
        for food in listoffoods:
            x,y = retruescale(food.position[0],food.position[1],aascale)
            screen.blit(food.image, (x, y))
        if mouse_x < 120:
            timerr = tm.time();delta = timerr - curtime;curfps = 1/delta
            truefps = clock.get_fps()
            var = round(truefps-curfps,2)
            textfps = font.render(f"Fps:{round(truefps,1)}|{round(curfps,1)}||{var}",True,(255,215,0))
            screen.blit(textfps, (10, 10));curtime = timerr
            # rframe =round(rframe+var,2)
            # pygame.draw.circle(screen, (255, 0, 0), (200,(var*10)+screen_height/2), 6)
        prevsx = msx;prevsy = msy
        pygame.display.flip()
        clock.tick(120)
    pygame.quit()
if __name__ == "__main__":
    main()
