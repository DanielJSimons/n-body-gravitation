import pygame
import math

G = 1  # adjustable parameter

class Body(pygame.sprite.Sprite):
    def __init__(self, mass, radius, start_position, color, x_vel, y_vel):    #attribute
        super().__init__()

        self.radius = radius
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)  # Create a transparent surface
        self.rect = self.image.get_rect(center=start_position)
        pygame.draw.circle(self.image, color, (radius, radius), radius)

        self.mass = mass
        self.radius = radius
        self.x_pos = start_position[0]
        self.y_pos = start_position[1]

        self.x_vel = x_vel
        self.x_acc = 0
        self.y_vel = y_vel
        self.y_acc = 0

        self.track_points = []  # List to store the track points

    def set_y_vel(self, value):     #method
        self.y_vel = value

    def set_x_vel(self, value):
        self.x_vel = value

    def set_y_acc(self, value):
        self.y_acc = value

    def set_x_acc(self, value):
        self.x_acc = value

    def change_x_pos(self, value):
        self.x_pos += value

    def change_y_pos(self, value):
        self.y_pos += value

    def change_x_vel(self, value):
        self.x_vel += value

    def change_y_vel(self, value):
        self.y_vel += value

    def update_pos(self):
        self.rect.center = (round(self.x_pos), round(self.y_pos))

    def animate(self):
        self.change_x_vel(self.x_acc)
        self.change_y_vel(self.y_acc)

        self.change_x_pos(self.x_vel)
        self.change_y_pos(self.y_vel)

        self.update_pos()
        
    def gravitate(self, otherbody):
        dx = abs(self.x_pos - otherbody.x_pos)
        dy = abs(self.y_pos - otherbody.y_pos)

        if dx < self.radius * 2 and dy < self.radius * 2:
            pass

        else:
            try:
                r = math.sqrt(dx ** 2 + dy ** 2)
                a = G * otherbody.mass / r ** 2
                theta = math.asin(dy / r)

                if self.y_pos > otherbody.y_pos:
                    self.set_y_acc(-math.sin(theta) * a)
                else:
                    self.set_y_acc(math.sin(theta) * a)

                if self.x_pos > otherbody.x_pos:
                    self.set_x_acc(-math.cos(theta) * a)
                else:
                    self.set_x_acc(math.cos(theta) * a)
            except ZeroDivisionError:
                pass
"""   
    def gravitate(self, otherbody):
        dx = otherbody.x_pos - self.x_pos
        dy = otherbody.y_pos - self.y_pos
        dist_squared = dx ** 2 + dy ** 2
        dist = math.sqrt(dist_squared)

        force = G * self.mass * otherbody.mass / dist_squared
        acceleration = force / self.mass

        self.x_vel += dx / dist * acceleration
        self.y_vel += dy / dist * acceleration

        
    def gravitate_reset(self):
        self.acceleration = pygame.Vector2(0,0)
        self.velocity = pygame.Vector2(0,0)
        
class QuadtreeNode:
    def __init__(self, bounds):
        self.bounds = bounds
        self.children = [None, None, None, None]
        self.objects = []
        
class Quadtree:
    def __init__(self, bounds, max_objects_per_node=4, max_levels=8):
        self.root = QuadtreeNode(bounds)
        self.max_objects_per_node = max_objects_per_node
        self.max_levels = max_levels
        
    def clear(self):
        self.root = QuadtreeNode(self.root.bounds)
        
        
    def insert(self, obj):
        self._insert_recursive(obj, self.root)
        
    def _insert_recursive(self, obj, node):
        if len(node.objects) < self.max_objects_per_node or len(node.children) == self.max_levels:
            node.objects.append(obj)
        else: 
            if node.children[0] is None:
                self._split_node(node)
            for i in range(4):
                if self._intersects(obj, node.children[i].bounds):
                    self._insert_recursive(obj, node.children[i])
   
    def _split_node(self, node):
        x = node.bounds.x
        y = node.bounds.y
        half_width = node.bounds.width // 2
        half_height = node.bounds.height // 2

        node.children[0] = QuadtreeNode(pygame.Rect(x + half_width, y, half_width, half_height))
        node.children[1] = QuadtreeNode(pygame.Rect(x, y, half_width, half_height))
        node.children[2] = QuadtreeNode(pygame.Rect(x, y + half_height, half_width, half_height))
        node.children[3] = QuadtreeNode(pygame.Rect(x + half_width, y + half_height, half_width, half_height))
        
        for obj in node.objects:
            for i in range(4):
                if self._intersects(obj, node.children[i].bounds):
                    self._insert_recursive(obj, node.children[i])
        node.objects = []

    def _intersects(self, obj, bounds):
        return obj.rect.colliderect(bounds)
    
    def query(self, obj):
        collisions = []
        self._query_recursive(obj, self.root, collisions)
        return collisions
    
    def _query_recursive(self, obj, node, collisions):
        if node is None:
            return

        for other_obj in node.objects:
            if obj is not other_obj and self._intersects(obj, other_obj):
                collisions.append((obj, other_obj))

        for child_node in node.children:
            if child_node is not None and self._intersects(obj, child_node.bounds):
                self._query_recursive(obj, child_node, collisions)
"""