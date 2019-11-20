import random
import arcade
import os

SPRITE_SCALING = 0.2

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Final Lab"

VIEWPORT_MARGIN = 40

MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists

        self.player_list = None
        self.sprite_list = None

        self.score = 0

        # Set up the player
        self.player_sprite = None
        self.physics_engine = None
        self.view_bottom = 0
        self.view_left = 0

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.sprite_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite("character.png", 0.04)
        self.player_sprite.center_x = 500
        self.player_sprite.center_y = 350
        self.player_list.append(self.player_sprite)

        # Dinosaurs
        dinosaur = arcade.Sprite("dinosaur_green.png", 0.20)
        dinosaur.center_x = 360
        dinosaur.center_y = 500
        self.sprite_list.append(dinosaur)

        dinosaur = arcade.Sprite("dinosaur_tall2.png", 0.08)
        dinosaur.center_x = 620
        dinosaur.center_y = 470
        self.sprite_list.append(dinosaur)

        dinosaur = arcade.Sprite("dinosaur_long.png", 0.15)
        dinosaur.center_x = 500
        dinosaur.center_y = 200
        self.sprite_list.append(dinosaur)

        # Dinosaur room
        for x in range(200, 450, 24):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 50
            self.sprite_list.append(wall)
        for x in range(550, 800, 24):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 50
            self.sprite_list.append(wall)
        for y in range(650, 750, 24):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = 450
            wall.center_y = y
            self.sprite_list.append(wall)
        for y in range(650, 750, 24):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = 550
            wall.center_y = y
            self.sprite_list.append(wall)
        for x in range(200, 450, 24):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 650
            self.sprite_list.append(wall)
        for x in range(550, 800, 24):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 650
            self.sprite_list.append(wall)
        for y in range(50, 300, 24):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = 200
            wall.center_y = y
            self.sprite_list.append(wall)
        for y in range(400, 650, 24):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = 200
            wall.center_y = y
            self.sprite_list.append(wall)
        for y in range(50, 338, 24):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = 800
            wall.center_y = y
            self.sprite_list.append(wall)
        for y in range(434, 674, 24):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = 800
            wall.center_y = y
            self.sprite_list.append(wall)

        # Space Room

        for x in range(200, 450, 25):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 746
            self.sprite_list.append(wall)
        for x in range(550, 825, 25):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 750
            self.sprite_list.append(wall)
        for x in range(200, 825, 25):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 1200
            self.sprite_list.append(wall)
        for y in range(750, 1200, 25):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = 200
            wall.center_y = y
            self.sprite_list.append(wall)
        for y in range(750, 1225, 25):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = 825
            wall.center_y = y
            self.sprite_list.append(wall)
        for y in range(-50, 50, 25):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = 440
            wall.center_y = y
            self.sprite_list.append(wall)
        for y in range(-50, 50, 25):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = 550
            wall.center_y = y
            self.sprite_list.append(wall)

            # Space things
            space = arcade.Sprite("spaceship.png", 0.20)
            space.center_x = 360
            space.center_y = 970
            self.sprite_list.append(space)

            space = arcade.Sprite("planet.png", 0.1)
            space.center_x = 600
            space.center_y = 1100
            self.sprite_list.append(space)

            space = arcade.Sprite("telescope.png", 0.2)
            space.center_x = 700
            space.center_y = 850
            self.sprite_list.append(space)

        # Plant room

        for x in range(200, 1125, 25):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = -500
            self.sprite_list.append(wall)
        for x in range(200, 440, 25):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = -50
            self.sprite_list.append(wall)
        for x in range(550, 825, 25):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = -50
            self.sprite_list.append(wall)

        for y in range(-400, -50, 25):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = 800
            wall.center_y = y
            self.sprite_list.append(wall)

        for x in range(825, 1125, 25):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = -400
            self.sprite_list.append(wall)
        for y in range(-500, -375, 25):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = 1125
            wall.center_y = y
            self.sprite_list.append(wall)

        for y in range(-500, -50, 25):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = 200
            wall.center_y = y
            self.sprite_list.append(wall)

            # Plants

            plant = arcade.Sprite("cactus.png", 0.18)
            plant.center_x = 350
            plant.center_y = -250
            self.sprite_list.append(plant)

            plant = arcade.Sprite("flower.png", 0.06)
            plant.center_x = 600
            plant.center_y = -425
            self.sprite_list.append(plant)

            plant = arcade.Sprite("plant.png", 0.2)
            plant.center_x = 650
            plant.center_y = -200
            self.sprite_list.append(plant)

        # Animal room

        for y in range(50, 675, 25):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = -600
            wall.center_y = y
            self.sprite_list.append(wall)
        for x in range(100, 200, 25):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 290
            self.sprite_list.append(wall)
        for x in range(100, 200, 25):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 400
            self.sprite_list.append(wall)
        for y in range(50, 290, 25):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = 100
            wall.center_y = y
            self.sprite_list.append(wall)
        for y in range(400, 700, 25):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = 100
            wall.center_y = y
            self.sprite_list.append(wall)
        for x in range(-600, 100, 25):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 675
            self.sprite_list.append(wall)
        for x in range(-600, -500, 25):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 50
            self.sprite_list.append(wall)
        for x in range(-400, 100, 25):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 50
            self.sprite_list.append(wall)
        for y in range(-500, 50, 25):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = -400
            wall.center_y = y
            self.sprite_list.append(wall)
        for y in range(-500, 75, 25):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = -500
            wall.center_y = y
            self.sprite_list.append(wall)
        for x in range(-500, -400, 25):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = -500
            self.sprite_list.append(wall)

            # Animals
            animal = arcade.Sprite("kangaroo.png", 0.2)
            animal.center_x = -450
            animal.center_y = 200
            self.sprite_list.append(animal)

            animal = arcade.Sprite("giraffe.png", 0.2)
            animal.center_x = -150
            animal.center_y = 390
            self.sprite_list.append(animal)

            animal = arcade.Sprite("tiger.png", 0.2)
            animal.center_x = -450
            animal.center_y = 490
            self.sprite_list.append(animal)

            animal = arcade.Sprite("turkey.png", 0.2)
            animal.center_x = -100
            animal.center_y = 160
            self.sprite_list.append(animal)

            # Egypt room
        for y in range(38, 675, 25):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = 1500
            wall.center_y = y
            self.sprite_list.append(wall)
        for x in range(800, 900, 25):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 338
            self.sprite_list.append(wall)
        for x in range(800, 900, 25):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 434
            self.sprite_list.append(wall)
        for y in range(38, 363, 25):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = 900
            wall.center_y = y
            self.sprite_list.append(wall)
        for y in range(434, 675, 25):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = 900
            wall.center_y = y
            self.sprite_list.append(wall)
        for x in range(900, 1525, 25):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 675
            self.sprite_list.append(wall)
        for x in range(900, 1525, 25):
            wall = arcade.Sprite("greystone.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 38
            self.sprite_list.append(wall)

        # Egyptian things
        animal = arcade.Sprite("pharaoh.png", 0.4)
        animal.center_x = 1000
        animal.center_y = 210
        self.sprite_list.append(animal)

        animal = arcade.Sprite("pyramid.png", 0.35)
        animal.center_x = 1310
        animal.center_y = 475
        self.sprite_list.append(animal)

        # Rubies
        # ruby = arcade.Sprite("ruby.png", .05)
        # ruby.center_x = 210
        # ruby.center_y = 755
        # self.sprite_list.append(ruby)
        #
        # ruby = arcade.Sprite("ruby.png", .05)
        # ruby.center_x = 0
        # ruby.center_y = 0
        # self.sprite_list.append(ruby)

        # ruby = arcade.Sprite("ruby.png", .1)
        # ruby.center_x = 1050
        # ruby.center_y = -400
        # self.sprite_list.append(ruby)


        # Exit
        exit = arcade.Sprite("exit.png", 0.1)
        exit.center_x = -450
        exit.center_y = -450
        self.sprite_list.append(exit)


        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.sprite_list)

        # Set the background color
        arcade.set_background_color(arcade.color.LIGHT_CORNFLOWER_BLUE)

        # Set the viewport boundaries
        # These numbers set where we have 'scrolled' to.
        self.view_left = 0
        self.view_bottom = 0

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.sprite_list.draw()
        self.player_list.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        # --- Manage Scrolling ---

        # Keep track of if we changed the boundary. We don't want to call the
        # set_viewport command if we didn't change the view port.
        changed = False

        # Scroll left
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        # Make sure our boundaries are integer values. While the view port does
        # support floating point numbers, for this application we want every pixel
        # in the view port to map directly onto a pixel on the screen. We don't want
        # any rounding errors.
        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)

        # If we changed the boundary values, update the view port to match
        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left - 1,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom - 1)

        # fly_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
        #                                                     self.fly_list)
        #
        # Loop through each colliding sprite, remove it, and add to the score.
        # for fly in fly_hit_list:
        #     fly.remove_from_sprite_lists()
        #     self.score += 1
        #     arcade.play_sound(self.popping_sound)


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
