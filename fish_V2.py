import pygame
from pygame import image, transform,RESIZABLE
import random
import math
import os
import numpy as np

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 1200
screen_height = screen_width * 600 // 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Boid Simulator")
icon = pygame.image.load(os.path.join('assets', 'fish.png'))
icon = pygame.transform.scale(icon, (32, 32))
pygame.display.set_icon(icon)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (173, 216, 230)
class Water:
    def __init__(self, width, height, num_points):
        self.width = width
        self.height = height
        self.num_points = num_points
        self.points = [(random.randint(0, width), random.randint(100, height),(random.randint(0,255),random.randint(0,255),random.randint(100,255))) for _ in range(num_points)]
        self.texture = self.generate_voronoi_texture()

    def generate_voronoi_texture(self):
        texture = pygame.Surface((self.width, self.height))

        # Create a grid of coordinates
        x_coords, y_coords = np.meshgrid(np.arange(self.width), np.arange(self.height))
        grid_coords = np.stack([x_coords, y_coords], axis=-1)

        # Extract points and colors
        points = np.array([(p[0], p[1]) for p in self.points])
        colors = np.array([p[2] for p in self.points])

        # Calculate the distance from each grid point to all points
        distances = np.sqrt(((grid_coords[:, :, np.newaxis, :] - points[np.newaxis, np.newaxis, :, :]) ** 2).sum(axis=3))

        # Determine the closest point for each grid point
        closest_point_indices = np.argmin(distances, axis=2)

        # Generate the texture based on the closest points
        texture_array = pygame.surfarray.pixels3d(texture)
        for i in range(self.num_points):
            mask = (closest_point_indices == i)
            distance_to_closest = distances[:, :, i][mask]
            brightness = np.minimum(255, (distance_to_closest / 2).astype(int)) * 4
            brightness = np.minimum(brightness, 160)
            cpoint = colors[i]
            color = np.array([cpoint], dtype=np.uint8)
            texture_array[mask.T] = color  # Transpose the mask to match the texture array dimensions

        return texture
    def draw(self, screen):
        screen.blit(self.texture, (0, 0))

class Boid:
    def __init__(self, screen_width, screen_height, separation_resolve=0.01, alignment_resolve=0.01, cohesion_resolve=0.01, top_speed=5, fishima=None, x=None, y=None, fish_type='fish',width=36,height=16):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.position = [x, y]
        self.velocity = [random.uniform(-10, 10), random.uniform(-10, 10)]
        self.angle = math.degrees(math.atan2(self.velocity[1], -self.velocity[0]))
        self.velocity = self.velocity
        self.max_speed = top_speed
        self.min_speed = 1
        self.speed_x = random.uniform(self.min_speed, self.max_speed)
        self.speed_y = random.uniform(self.min_speed, self.max_speed)
        self.separation_resolve = separation_resolve
        self.alignment_resolve = alignment_resolve
        self.cohesion_resolve = cohesion_resolve
        self.image = transform.scale(image.load(fishima), (width, height))
        self.fish_type = fish_type  # Add fish type attribute
        self.campzone=0
    def distance(self, other_boid):
        return np.sqrt((self.position[0] - other_boid.position[0]) ** 2 + (self.position[1] - other_boid.position[1]) ** 2)

    def update_position(self):
        self.check_bounds()
        self.limit_speed()
        self.position[0] += self.velocity[0] * self.speed_x
        self.position[1] += self.velocity[1] * self.speed_y

    def check_bounds(self):
        margin = 000  # Distance from the edge to start turning
        turn_factor = 0.45

        # if self.position[0] < margin:
        #     self.velocity[0] += turn_factor
        #     # self.position[0] = margin
        # elif self.position[0] > self.screen_width - margin:
        #     self.velocity[0] -= turn_factor
        #     # self.position[0] = self.screen_width - margin

        # if self.position[1] < margin:
        #     self.velocity[1] += turn_factor
        #     # self.position[1] = margin
        # elif self.position[1] > self.screen_height - margin:
        #     self.velocity[1] -= turn_factor
        #     # self.position[1] = self.screen_height - margin
        width = self.image.get_width()
        height = self.image.get_height()
        left_rect = pygame.Rect(self.position[0]-width/2, self.position[1], width/2, height)
        right_rect = pygame.Rect(self.position[0]+width/2, self.position[1], width/2, height)
        top_rect = pygame.Rect(self.position[0], self.position[1]-height/2, width, height/2)
        bottom_rect = pygame.Rect(self.position[0], self.position[1]+height/2, width, height/2)
        main_rect = pygame.Rect(self.position[0], self.position[1], width, height)
        base_rect = pygame.Rect(0, 0, self.screen_width, self.screen_height)
        self.campzone = 0
        if base_rect.colliderect(left_rect) and base_rect.colliderect(right_rect) and base_rect.colliderect(top_rect) and base_rect.colliderect(bottom_rect):
            self.campzone = 1
        else:
            for zone in zones:
                if (zone.colliderect(left_rect) and zone.colliderect(right_rect) and zone.colliderect(top_rect) and zone.colliderect(bottom_rect)) or zone.colliderect(main_rect):
                    self.campzone = 1
                else:
                    if zone.colliderect(left_rect):
                        self.velocity[0] -= 1
                        self.campzone = 1
                    if zone.colliderect(right_rect):
                        self.velocity[0] += 1
                        self.campzone = 1
                    if zone.colliderect(top_rect):
                        self.velocity[1] -= 1
                        self.campzone = 1
                    if zone.colliderect(bottom_rect):
                        self.velocity[1] += 1
                        self.campzone = 1

        if (self.position[0] < 0 or self.position[0] > self.screen_width or self.position[1] < 0 or self.position[1] > self.screen_height) and self.campzone == 0:
            angle = math.atan2(self.position[1] - self.screen_height / 2, self.position[0] - self.screen_width / 2)
            self.velocity[0] -= math.cos(angle)*turn_factor
            self.velocity[1] -= math.sin(angle)*turn_factor
            # self.position[0] = min(self.screen_width, max(0, self.position[0]))
            # self.position[1] = min(self.screen_height, max(0, self.position[1]))

    def move_random_direction(self):
        dist = np.hypot(self.velocity[0], self.velocity[1])
        self.angle = math.atan2(self.velocity[1], self.velocity[0])
        self.angle += random.uniform(-0.5, 0.5)
        self.velocity[0] = dist * math.cos(self.angle)*2
        self.velocity[1] = dist * math.sin(self.angle)*2

    def caculate_angle(self):
        angle = math.degrees(math.atan2(self.velocity[1], -self.velocity[0]))
        return angle
    def apply_separation(self, boids, separation_distance):
        move_x, move_y = 0, 0
        for other_boid in boids:
            if other_boid != self and self.distance(other_boid) < separation_distance:
                move_x += self.position[0] - other_boid.position[0]
                move_y += self.position[1] - other_boid.position[1]
        self.velocity[0] += move_x * self.separation_resolve  # Apply a smaller fraction for smoother separation
        self.velocity[1] += move_y * self.separation_resolve  # Apply a smaller fraction for smoother separation

    def apply_alignment(self, boids, alignment_distance):
        avg_velocity_x, avg_velocity_y = 0, 0
        count = 0
        for other_boid in boids:
            if other_boid != self and self.distance(other_boid) < alignment_distance and other_boid.fish_type == self.fish_type:
                avg_velocity_x += other_boid.velocity[0]
                avg_velocity_y += other_boid.velocity[1]
                count += 1
        if count > 0:
            avg_velocity_x /= count
            avg_velocity_y /= count
            self.velocity[0] += (avg_velocity_x - self.velocity[0]) * self.alignment_resolve
            self.velocity[1] += (avg_velocity_y - self.velocity[1]) * self.alignment_resolve

    def apply_cohesion(self, boids, cohesion_distance):
        avg_position_x, avg_position_y = 0, 0
        count = 0
        for other_boid in boids:
            if other_boid != self and self.distance(other_boid) < cohesion_distance and other_boid.fish_type == self.fish_type:
                avg_position_x += other_boid.position[0]
                avg_position_y += other_boid.position[1]
                count += 1
        if count > 0:
            avg_position_x /= count
            avg_position_y /= count
            self.velocity[0] += (avg_position_x - self.position[0]) * self.cohesion_resolve
            self.velocity[1] += (avg_position_y - self.position[1]) * self.cohesion_resolve
    def apply_mouse_repulsion(self, mouse_pos, repulsion_distance, repulsion_strength):
        distance_to_mouse = math.sqrt((self.position[0] - mouse_pos[0]) ** 2 + (self.position[1] - mouse_pos[1]) ** 2)
        if distance_to_mouse < repulsion_distance:
            angle = math.atan2(self.position[1] - mouse_pos[1], self.position[0] - mouse_pos[0])
            strength = 1000/(distance_to_mouse+0.00001)
            if strength > 256:
                strength = 256
            move_x = math.cos(angle)*strength
            move_y = math.sin(angle)*strength
            self.velocity[0] += move_x * repulsion_strength
            self.velocity[1] += move_y * repulsion_strength
            # print("Mouse repulsion")
        # elif distance_to_mouse < repulsion_distance*2:
        #     # print(f"not Mouse repulsion")
    def limit_speed(self):
        speed = math.sqrt(self.velocity[0] ** 2 + self.velocity[1] ** 2)
        self.velocity = self.velocity
        if speed > self.max_speed:
            self.velocity[0] = (self.velocity[0] / speed) * self.max_speed
            self.velocity[1] = (self.velocity[1] / speed) * self.max_speed
    def draw(self, screen,scale=1):     
        sx = (self.position[0]-(screen_width/2-zoomx)-screen_width/2) * scale + screen_width/2
        sy = (self.position[1]-(screen_height/2-zoomy)-screen_height/2) * scale + screen_height/2
        self.newimage = self.image
        self.newimage = transform.scale(self.newimage, (int(self.image.get_width()*scale), int(self.image.get_height()*scale)))
        if self.velocity[0] < 0:
            self.newimage = transform.flip(self.newimage, False, True)
        self.newimage = transform.rotate(self.newimage, math.degrees(math.atan2(self.velocity[1], -self.velocity[0])) +180)
        # self.newimage = transform.rotate(self.newimage, self.angle)
        if not (sx < -self.image.get_width() or sx > screen_width or sy< -self.image.get_height() or sy > screen_height):
            if scale > 0.1: 
                screen.blit(self.newimage, (sx, sy))
            else:
                pygame.draw.circle(screen, (255, 0, 0), (int(sx), int(sy)), 3)
    
        

# Main loop
def main():
    global screen
    global zones
    global cx,cy,zoomx,zoomy
    cx = screen_width/2
    cy = screen_height/2
    clock = pygame.time.Clock()
    separation_distance = 35
    alignment_distance = 50
    cohesion_distance = 65
    separation_resolve = 0.04
    alignment_resolve = 0.02
    cohesion_resolve = 0.02
    # separation_resolve = 0
    # alignment_resolve = 0
    # cohesion_resolve = 0
    repulsion_distance = 100
    repulsion_strength = 0.5
    top_speed = 5
    fishima = os.path.join('assets', 'fish.png')
    salmonela = os.path.join('assets', 'salmon.png')
    tunala = os.path.join('assets', 'rainbow_fish.png')
    background = os.path.join('assets', 'water.png')
    background = image.load(background)
    background = transform.scale(background, (screen_width, screen_height))
    boids = []
    zones = []
    for i in range(15):
        rasx = random.randint(-10000, 10000) + screen_width // 2
        rasy = random.randint(-10000, 10000) + screen_height // 2
        raex = random.randint(50, 80) + screen_width // 2
        raey = random.randint(50, 80) + screen_height // 2
        angle = random.randint(0, 360)
        for j in range(10):
            angle += random.uniform(-5, 5)
            tsx = math.cos((angle/180)*math.pi)*200
            tsy = math.sin((angle/180)*math.pi)*200
            rasx += tsx
            rasy += tsy
            zones.append(pygame.Rect(rasx, rasy, raex, raey))
    zoomx = screen_width/2
    zoomy = screen_height/2
    scale = 1
    for i in range(24):
        randomwidth = random.uniform(36,72)
        randomheight = int(randomwidth*16/36)
        boids.append(Boid(screen_width, screen_height, separation_resolve, alignment_resolve, cohesion_resolve, top_speed, fishima, random.uniform(0, screen_width), random.uniform(0, screen_height), fish_type='cod',width=randomwidth,height=randomheight))
        randomwidth = random.uniform(45,72)
        randomheight = int(randomwidth*16/45)
        boids.append(Boid(screen_width, screen_height, separation_resolve, alignment_resolve, cohesion_resolve, top_speed, salmonela, random.uniform(0, screen_width), random.uniform(0, screen_height), fish_type='salmon',width=randomwidth,height=randomheight))
        randomwidth = random.uniform(14,72)
        randomheight = int(randomwidth*16/14)
        boids.append(Boid(screen_width, screen_height, separation_resolve, alignment_resolve, cohesion_resolve, top_speed, tunala, random.uniform(0, screen_width), random.uniform(0, screen_height), fish_type='rainbow',width=randomwidth,height=randomheight))
    running = True
    # water = Water(600, 450, 60)
    # water = transform.scale(water.texture, (screen_width, screen_height))
    startpos = None
    endpos = None
    while running:
        aascale = abs(scale)
        if aascale == 0:
            aascale = 0.000000000000001
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    startpos = pygame.mouse.get_pos()
                    sx = (startpos[0]  - screen_width/2)/ aascale + screen_width/2
                    sy = (startpos[1] -screen_height/2)/ aascale + screen_height/2
                    startpos = (sx,sy)
                if event.key == pygame.K_n:
                    endpos = pygame.mouse.get_pos()
                    sx = (endpos[0]  - screen_width/2)/ aascale + screen_width/2
                    sy = (endpos[1] -screen_height/2)/ aascale + screen_height/2
                    endpos = (sx,sy)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        wsx = (-(screen_width/2-zoomx)-screen_width/2) * aascale + screen_width/2
        wsy = (-(screen_height/2-zoomy)-screen_height/2) * aascale + screen_height/2
        pygame.draw.rect(screen, (0, 255, 100), (wsx,wsy, screen_width*aascale*1, screen_height*aascale*1))
        mouse_x,mouse_y = pygame.mouse.get_pos()
        if startpos is not None and endpos is not None:
            if startpos[0] < endpos[0]:
                zones.append(pygame.Rect(startpos[0], startpos[1], endpos[0]-startpos[0], endpos[1]-startpos[1]))
            startpos = None
            endpos = None
        # swidth = zoomx-screen_width*scale/2
        # sheight = zoomy-screen_height*scale/2
        # sx = mouse_X * scale + swidth
        # sy = mouse_y * scale + sheight
        sx = (mouse_x  - screen_width/2)/ aascale + screen_width/2
        sy = (mouse_y -screen_height/2)/ aascale + screen_height/2

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            zoomy += 10
        if keys[pygame.K_DOWN]:
            zoomy -= 10
        if keys[pygame.K_LEFT]:
            zoomx += 10
        if keys[pygame.K_RIGHT]:
            zoomx -= 10
        if keys[pygame.K_e]:
            scale += 0.05
        if keys[pygame.K_q]:
            scale -= 0.05
        # cx = zoomx*scale
        # cy = zoomy*scale

        # sawater = transform.scale(water, (screen_width*scale*2, screen_height*scale*2))
        # screen.blit(sawater, (zoomx-screen_width*scale, zoomy-screen_height*scale))
        # sawater = transform.scale(water, (screen_width*aascale, screen_height*aascale))
        # screen.blit(sawater, (zoomx-screen_width*scale/2, zoomy-screen_height*scale/2))
        for zone in zones:
            asx = (zone[0]-(screen_width/2-zoomx)-screen_width/2) * aascale + screen_width/2
            asy = (zone[1]-(screen_height/2-zoomy)-screen_height/2) * aascale + screen_height/2

            pygame.draw.rect(screen, (0, 255, 0), (asx,asy,zone[2]*aascale,zone[3]*aascale))
        mousepressed = pygame.mouse.get_pressed()
        if mousepressed[0]:
            for boid in boids:
                boid.apply_mouse_repulsion((sx,sy), repulsion_distance, repulsion_strength)
                pygame.draw.circle(screen, (255, 0, 0), (mouse_x,mouse_y), repulsion_distance*aascale,5)
        # pygame.draw.circle(screen, (255, 0, 0), (int(sx), int(sy)), 10, 5)
        # print(sx,sy,scale)
        for boid in boids:
            boid.apply_separation(boids, separation_distance)
            boid.apply_alignment(boids, alignment_distance)
            boid.apply_cohesion(boids, cohesion_distance)
            boid.apply_mouse_repulsion((0,0), 75, 0.005)
            # boid.velocity[0]*=0.99
            # boid.velocity[1]*=0.99
            boid.update_position()
            if abs(boid.velocity[0]) >2 and abs(boid.velocity[1]) >2:
                boid.velocity[0]*=0.99
                boid.velocity[1]*=0.99
            boid.draw(screen,scale=aascale)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
