import pygame, sys, pygame_gui
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT, VIDEORESIZE


# class imports
from battle import Battle
from player import Player
from item import Item
from place import Place

w = 1140
h = 700

DISPLAYSURF = pygame.display.set_mode((w, h))
pygame.display.set_caption('UBC ARENA')
clock = pygame.time.Clock()

map = pygame.image.load('images/map_temp.png')
map = pygame.transform.scale(map, (916, 686))
bio = pygame.image.load('images/UBC-BIOL.jpg')

DISPLAYSURF.fill((0, 0, 0))

#TESTING CODE
# fungus = Item("Fungus", "damage", 20)
# potion = Item("Potion", "heal", 15)
# max = Player("Max", "Math", "Attacker")
# minnie = Player("Minnie", "Math", "Defender")
# battle = Battle(max, minnie)
# battle.useItem(max, fungus)
# print(minnie.HP)
# battle.useItem(minnie, potion)
# print(minnie.HP)
# bioBuilding = Place("BIOL", [fungus, potion], [])
# bioBuilding.dropItem(minnie)
# minnie.returnItemList()
#TESTING CODE

pygame.init()

my_player = Player("Me", "Math", "Attacker", "Hi, I'm TestPlayer.")
opponent = Player("Fountain Man", "Eng Phys", "God", "I am almighty.")
opponent.setLevel(100)
battle = Battle(my_player, opponent)


class PlayerImage(pygame.sprite.Sprite):

  def __init__(self):
    super(PlayerImage, self).__init__()
    self.surf = pygame.Surface((20, 20))
    img = pygame.image.load('images/Character.PNG')
    self.image = pygame.transform.scale(img, (50, 50))
    self.surf.fill((0, 0, 0))
    self.rect = self.surf.get_rect()

  def update(self, pressed_keys):
    update_profile_labels()
    update_stats()

    if pressed_keys[K_UP]:
      self.rect.move_ip(0, -5)
    if pressed_keys[K_DOWN]:
      self.rect.move_ip(0, 5)
    if pressed_keys[K_LEFT]:
      self.rect.move_ip(-5, 0)
    if pressed_keys[K_RIGHT]:
      self.rect.move_ip(5, 0)

    if self.rect.left < 0:
      self.rect.left = 0
    if self.rect.right > w:
      self.rect.right = w
    if self.rect.top < 0:
      self.rect.top = 0
    if self.rect.bottom > h:
      self.rect.bottom = h


player1 = PlayerImage()


#building locations
class Buildings(pygame.sprite.Sprite):

  def __init__(self, x, y):
    super(Buildings, self).__init__()
    self.surf = pygame.Surface((20, 20))
    img = pygame.image.load('images/BuildingLocations.png')
    self.image = pygame.transform.scale(img, (70, 50))
    self.surf.fill((0, 0, 0))
    self.rect = self.surf.get_rect(center=(x, y))


biolBuilding = Buildings(550, 320)
chemBuilding = Buildings(450, 100)
fountain = Buildings(340, 290)
# scarfe = Buildings()
# HenryAngus = Buildings()

#GUI
manager = pygame_gui.UIManager((1500, 700), 'theme.json')

# GUI--CharacterCreation
creation_panel = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect(
  300, 20, 300, 660),
                                             starting_layer_height=0,
                                             manager=manager)

name_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
  20, 20, 260, 20),
                                         text="Enter your name:",
                                         container=creation_panel,
                                         manager=manager)

enter_name = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(
  20, 60, 260, 30),
                                                 container=creation_panel,
                                                 manager=manager)

major_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
  20, 100, 260, 20),
                                          text="Choose your major:",
                                          container=creation_panel,
                                          manager=manager)

choose_major = pygame_gui.elements.UIDropDownMenu(
  relative_rect=pygame.Rect(20, 140, 260, 20),
  options_list=["Select", "Math", "English", "Computer Science", "Cognitive Systems", "Biology", "Psychology", "Chemistry", "Other"],
  starting_option="Select",
  container=creation_panel,
  manager=manager)

type_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
  20, 180, 260, 20),
                                         text="Choose your type:",
                                         container=creation_panel,
                                         manager=manager)

choose_type = pygame_gui.elements.UIDropDownMenu(
  relative_rect=pygame.Rect(20, 220, 260, 20),
  options_list=["Select", "Attacker", "Defender"],
  starting_option="Select",
  container=creation_panel,
  manager=manager)

bio_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
  20, 260, 260, 20),
                                        text="Tell us about yourself!",
                                        container=creation_panel,
                                        manager=manager)

enter_bio = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(
  20, 300, 260, 30),
                                                container=creation_panel,
                                                manager=manager)

start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
  20, 340, 260, 20),
                                            text="Start",
                                            container=creation_panel,
                                            manager=manager)

# creation_panel.hide()

# GUI--Profile
profile_panel = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect(
  930, 20, 200, 660),
                                            starting_layer_height=0,
                                            manager=manager)

my_name = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
  20, 20, 120, 20),
                                      text="MY NAME",
                                      container=profile_panel,
                                      manager=manager)

my_level = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
  120, 20, 40, 20),
                                       text="LV 5",
                                       container=profile_panel,
                                       manager=manager)

my_major = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
  20, 70, 160, 20),
                                       text="MY MAJOR",
                                       container=profile_panel,
                                       manager=manager)

my_type = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
  20, 90, 160, 20),
                                      text="MY TYPE",
                                      container=profile_panel,
                                      manager=manager)

my_hp = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
  20, 130, 160, 20),
                                    text="HP",
                                    container=profile_panel,
                                    manager=manager)

my_hp_bar = pygame_gui.elements.UIStatusBar(relative_rect=pygame.Rect(
  20, 150, 160, 20),
                                            container=profile_panel,
                                            manager=manager)

my_atk = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
  20, 190, 160, 20),
                                     text="ATK 0",
                                     container=profile_panel,
                                     manager=manager)

my_def = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
  20, 210, 160, 20),
                                     text="DEF 0",
                                     container=profile_panel,
                                     manager=manager)

my_lck = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
  20, 230, 160, 20),
                                     text="LCK 0",
                                     container=profile_panel,
                                     manager=manager)

profile_items_button = pygame_gui.elements.UIButton(
  relative_rect=pygame.Rect(20, 270, 160, 20), text="Items", container=profile_panel, manager=manager)

profile_messages_button = pygame_gui.elements.UIButton(
  relative_rect=pygame.Rect(20, 300, 160, 20), text="Inbox", container=profile_panel, manager=manager)

profile_friends_button = pygame_gui.elements.UIButton(
  relative_rect=pygame.Rect(20, 330, 160, 20), text="Friends", container=profile_panel, manager=manager)

profile_settings_button = pygame_gui.elements.UIButton(
  relative_rect=pygame.Rect(20, 360, 160, 20), text="Settings", container=profile_panel, manager=manager)

profile_panel.hide()

def update_profile_labels():
  my_name.set_text(my_player.name)
  my_level.set_text("LV " + str(my_player.level))
  my_major.set_text(my_player.major)
  my_type.set_text(my_player.type)
  my_hp_bar.percent_full = my_player.healthPercent()

def update_stats():
  my_atk.set_text("ATK " + str(my_player.ATK))
  my_def.set_text("DEF " + str(my_player.DEF))
  my_lck.set_text("LCK " + str(my_player.LCK))
  

# GUI--Talk
talk_panel = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect(
  100, 100, 300, 440),
                                           starting_layer_height=5,
                                           manager=manager)

talk_img_opponent = pygame.image.load('images/Player.png')

talk_image_opponent = pygame_gui.elements.UIImage(relative_rect=pygame.Rect(
  0, 0, 150, 150),
                                              image_surface=talk_img_opponent,
                                              container=talk_panel,
                                              manager=manager)

talk_opponent_name = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
  20, 190, 260, 20),
                                            text="PL NAME",
                                            container=talk_panel,
                                            manager=manager)

talk_opponent_level = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
  20, 210, 260, 20),
                                            text="LV PL",
                                            container=talk_panel,
                                            manager=manager)

talk_opponent_major = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
  20, 230, 260, 20),
                                            text="PL MAJ",
                                            container=talk_panel,
                                            manager=manager)

talk_opponent_type = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
  20, 250, 260, 20),
                                            text="PL TY",
                                            container=talk_panel,
                                            manager=manager)

talk_opponent_bio = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
  20, 270, 260, 20),
                                            text="PL BIO",
                                            container=talk_panel,
                                            manager=manager)

challenge_button = pygame_gui.elements.UIButton(
  relative_rect=pygame.Rect(20, 310, 260, 20), text="Challenge to a Battle", container=talk_panel, manager=manager)

message_button = pygame_gui.elements.UIButton(
  relative_rect=pygame.Rect(20, 350, 260, 20), text="Send Message", container=talk_panel, manager=manager)

add_friend_button = pygame_gui.elements.UIButton(
  relative_rect=pygame.Rect(20, 390, 260, 20), text="Send Friend Request", container=talk_panel, manager=manager)

talk_panel.hide()

def set_talk_opponent():
  talk_opponent_name.set_text(opponent.name)
  talk_opponent_level.set_text("LV " + str(opponent.level))
  talk_opponent_major.set_text(opponent.major)
  talk_opponent_type.set_text(opponent.type)
  talk_opponent_bio.set_text(opponent.bio)
  talk_image_opponent.set_image(talk_img_opponent)
  battle_image_opponent.set_image(talk_img_opponent)

# GUI--Battle
battle_panel = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect(
  100, 100, 600, 500),
                                           starting_layer_height=5,
                                           manager=manager)

battle_panel_me = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect(
  0, 0, 300, 400),
                                              starting_layer_height=6,
                                              container=battle_panel,
                                              manager=manager)

battle_panel_opponent = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect(
  300, 0, 300, 400),
                                                    starting_layer_height=6,
                                                    container=battle_panel,
                                                    manager=manager)

battle_img_me = pygame.image.load('images/Player.png')

battle_image_me = pygame_gui.elements.UIImage(relative_rect=pygame.Rect(
  0, 0, 150, 150),
                                              image_surface=battle_img_me,
                                              container=battle_panel_me,
                                              manager=manager)

battle_image_opponent = pygame_gui.elements.UIImage(
  relative_rect=pygame.Rect(0, 0, 150, 150),
  image_surface=talk_img_opponent,
  container=battle_panel_opponent,
  manager=manager)

battle_my_hp_bar = pygame_gui.elements.UIStatusBar(relative_rect=pygame.Rect(
  20, 150, 260, 20),
                                            container=battle_panel_me,
                                            manager=manager)

battle_opponent_hp_bar = pygame_gui.elements.UIStatusBar(relative_rect=pygame.Rect(
  20, 150, 260, 20),
                                            container=battle_panel_opponent,
                                            manager=manager)

battle_my_atk = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
  20, 190, 260, 20),
                                            text="ATK 0",
                                            container=battle_panel_me,
                                            manager=manager)

battle_my_def = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
  20, 230, 260, 20),
                                            text="DEF 0",
                                            container=battle_panel_me,
                                            manager=manager)

battle_my_lck = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
  20, 270, 260, 20),
                                            text="LCK 0",
                                            container=battle_panel_me,
                                            manager=manager)

attack_button = pygame_gui.elements.UIButton(
  relative_rect=pygame.Rect(20, 200, 260, 20), text="Attack", container=battle_panel_opponent, manager=manager)

special_attack_button = pygame_gui.elements.UIButton(
  relative_rect=pygame.Rect(20, 240, 260, 20), text="Special Attack", container=battle_panel_opponent, manager=manager)

item_button = pygame_gui.elements.UIButton(
  relative_rect=pygame.Rect(20, 280, 260, 20), text="Use Item", container=battle_panel_opponent, manager=manager)

surrender_button = pygame_gui.elements.UIButton(
  relative_rect=pygame.Rect(20, 320, 260, 20), text="Surrender", container=battle_panel_opponent, manager=manager)

leave_battle_button = pygame_gui.elements.UIButton(
  relative_rect=pygame.Rect(20, 360, 260, 20), text="Leave", container=battle_panel_opponent, manager=manager)

battle_flavor_text_1 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
  20, 420, 560, 20),
                                            text="FLAV TEXT",
                                            container=battle_panel,
                                            manager=manager)

battle_flavor_text_2 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
  20, 460, 560, 20),
                                            text="FLAV TEXT",
                                            container=battle_panel,
                                            manager=manager)

battle_panel.hide()

def setup_battle():
  battle_my_hp_bar.percent_full = my_player.healthPercent()
  battle_opponent_hp_bar.percent_full = opponent.healthPercent()
  battle_my_atk.set_text("ATK " + str(my_player.ATK))
  battle_my_def.set_text("DEF " + str(my_player.DEF))
  battle_my_lck.set_text("LCK " + str(my_player.LCK))

def battle_action(action):
  if action == "Attack":
    my_battle_text = battle.attack(my_player)
    battle_my_hp_bar.percent_full = my_player.healthPercent()
    battle_opponent_hp_bar.percent_full = opponent.healthPercent()
    if battle.checkBattleOver() == "Victory":
      my_battle_text += " You win!"
      battle_flavor_text_1.set_text(my_battle_text)
      leave_battle_button.show()
    else:
      opponent_battle_text = battle.attack(opponent)
      battle_my_hp_bar.percent_full = my_player.healthPercent()
      battle_opponent_hp_bar.percent_full = opponent.healthPercent()
      if battle.checkBattleOver() == "Defeat":
        opponent_battle_text += " You lose!"
        leave_battle_button.show()
      battle_flavor_text_1.set_text(my_battle_text)
      battle_flavor_text_2.set_text(opponent_battle_text)
    
  

# GUI--Map Buttons

fountain_button = pygame_gui.elements.ui_button.UIButton(
  relative_rect=pygame.Rect(340, 290, 100, 25), text="Enter", manager=manager)

fountain_button.hide()

biol_button = pygame_gui.elements.ui_button.UIButton(relative_rect=pygame.Rect(
  550, 320, 100, 25),
                                                     text="Enter",
                                                     manager=manager)

biol_button.hide()

chem_button = pygame_gui.elements.ui_button.UIButton(relative_rect=pygame.Rect(
  450, 100, 100, 25),
                                                     text="Enter",
                                                     manager=manager)

chem_button.hide()

# GUI--Map Panels

#fountain panel
fountain_panel = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect(
  10, 10, 900, 600),
                                             starting_layer_height=2,
                                             manager=manager)

fountain_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
  45, 0, 260, 20),
                                             text="Fountain",
                                             container=fountain_panel,
                                             manager=manager)

fountain_leave_button = pygame_gui.elements.ui_button.UIButton(
  relative_rect=pygame.Rect(410, 550, 100, 25),
  container=fountain_panel,
  text="Leave",
  manager=manager)

ftn_img = pygame.image.load('images/fountain2.jpg')
ftn_img = pygame.transform.scale(ftn_img, (900, 900))

character_img_ftn = pygame.image.load('images/FountainPerson.png')

fountain_image = pygame_gui.elements.UIImage(relative_rect=pygame.Rect(
  0, 30, 900, 500),
                                             image_surface=ftn_img,
                                             container=fountain_panel,
                                             manager=manager)

character_in_ftn = pygame_gui.elements.UIImage(relative_rect=pygame.Rect(
  500, 300, 450, 400),
                                               image_surface=character_img_ftn,
                                               container=fountain_panel,
                                               manager=manager)

talk_to_ftn_button = pygame_gui.elements.ui_button.UIButton(
  relative_rect=pygame.Rect(500, 400, 100, 25),
  container=fountain_panel,
  text="Talk",
  manager=manager)

fountain_panel.hide()

#biol panel
biol_panel = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect(
  10, 10, 900, 600),
                                         starting_layer_height=0,
                                         manager=manager)

biol_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
  45, 0, 260, 20),
                                         text="Biology Building",
                                         container=biol_panel,
                                         manager=manager)


biol_leave_button = pygame_gui.elements.ui_button.UIButton(
  relative_rect=pygame.Rect(410, 550, 100, 25),
  container=biol_panel,
  text="Leave",
  manager=manager)

biol_img = pygame.image.load('images/UBC-BIOL.jpg')
biol_img = pygame.transform.scale(biol_img, (700, 400))

biol_image = pygame_gui.elements.UIImage(relative_rect=pygame.Rect(
  0, 30, 900, 500),
                                         image_surface=biol_img,
                                         container=biol_panel,
                                         manager=manager)
character_img_bio = pygame.image.load('images/BioKid.png')
character_in_bio = pygame_gui.elements.UIImage(relative_rect=pygame.Rect(
  500, 300, 450, 400),
                                               image_surface=character_img_bio,
                                               container=biol_panel,
                                               manager=manager)

talk_to_biol_button = pygame_gui.elements.ui_button.UIButton(
  relative_rect=pygame.Rect(500, 400, 100, 25),
  container=biol_panel,
  text="Talk",
  manager=manager)

biol_panel.hide()

#chem panel
chem_panel = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect(
  10, 10, 900, 600),
                                         starting_layer_height=0,
                                         manager=manager)

chem_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
  45, 0, 260, 20),
                                         text="Chemistry Building",
                                         container=chem_panel,
                                         manager=manager)

chem_leave_button = pygame_gui.elements.ui_button.UIButton(
  relative_rect=pygame.Rect(410, 550, 100, 25),
  container=chem_panel,
  text="Leave",
  manager=manager)

chem_img = pygame.image.load('images/UBC-CHEM.jpg')
chem_img = pygame.transform.scale(chem_img, (700, 400))

chem_image = pygame_gui.elements.UIImage(relative_rect=pygame.Rect(
  0, 30, 900, 500),
                                         image_surface=chem_img,
                                         container=chem_panel,
                                         manager=manager)
character_img_chem = pygame.image.load('images/ChemStudent.png')

character_in_chem = pygame_gui.elements.UIImage(relative_rect=pygame.Rect(
  500, 300, 450, 400),
                                                image_surface=character_img_chem,
                                                container=chem_panel,
                                                manager=manager)

talk_to_chem_button = pygame_gui.elements.ui_button.UIButton(
  relative_rect=pygame.Rect(500, 400, 100, 25),
  container=chem_panel,
  text="Talk",
  manager=manager)

chem_panel.hide()

#while loop
running = True
while running:
  clock.tick(60)
  time_delta = clock.tick(60) / 1000.0

  for event in pygame.event.get():

    DISPLAYSURF.fill((255, 255, 255))

    if event.type == KEYDOWN:  # checks if user hit a key
      if event.key == K_ESCAPE:
        running = False
    if event.type == QUIT:
      running = False
    if event.type == VIDEORESIZE:
      DISPLAYSURF = pygame.display.set_mode((event.w, event.h),
                                            pygame.RESIZEABLE)

    if event.type == pygame_gui.UI_BUTTON_PRESSED:
      if event.ui_element == start_button:
        my_player = Player(enter_name.get_text(), choose_major.selected_option,
                           choose_type.selected_option, enter_bio.get_text())
        print(my_player.name + my_player.major + my_player.type +
              my_player.bio)
        creation_panel.hide()
        profile_panel.show()

      if event.ui_element == fountain_button:
        fountain_button.hide()
        fountain_panel.show()

      if event.ui_element == fountain_leave_button:
        fountain_button.hide()
        fountain_panel.hide()
        talk_panel.hide()

      if event.ui_element == biol_button:
        biol_button.hide()
        biol_panel.show()

      if event.ui_element == biol_leave_button:
        biol_button.hide()
        biol_panel.hide()
        talk_panel.hide()

      if event.ui_element == chem_button:
        chem_button.hide()
        chem_panel.show()

      if event.ui_element == chem_leave_button:
        chem_button.hide()
        chem_panel.hide()
        talk_panel.hide()

      #fountain talk
      if event.ui_element == talk_to_ftn_button:
        opponent = Player("Fountain Man", "Eng Phys", "God", "I am almighty.")
        talk_img_opponent = pygame.image.load('images/FountainPerson.png')
        set_talk_opponent()
        talk_to_ftn_button.hide()
        talk_panel.show()

      if event.ui_element == challenge_button:
        talk_panel.hide()
        battle_panel.show()

      if event.ui_element == surrender_button:
        battle_panel.hide()

      #biol talk
      if event.ui_element == talk_to_biol_button:
        opponent = Player("Bio kid", "Bio", "Tree", "I have become one with nature")
        talk_img_opponent = pygame.image.load('images/BioKid.png')
        set_talk_opponent()
        talk_to_biol_button.hide()
        talk_panel.show()

      if event.ui_element == challenge_button:
        talk_panel.hide()
        battle_panel.show()

      if event.ui_element == surrender_button:
        battle_panel.hide()

       #chem talk
      if event.ui_element == talk_to_chem_button:
        opponent = Player("Depressed chem student", "Chemistry", "Sleep Deprived", "I have 3 exams tomorrow")
        talk_img_opponent = pygame.image.load('images/ChemStudent.png')
        set_talk_opponent()
        talk_to_chem_button.hide()
        talk_panel.show()

      if event.ui_element == challenge_button:
        talk_panel.hide()
        setup_battle()
        battle = Battle(my_player, opponent)
        battle_panel.show()
        leave_battle_button.hide()

      if event.ui_element == attack_button:
        battle_action("Attack")
        

      if event.ui_element == surrender_button:
        battle_panel.hide()

      if event.ui_element == leave_battle_button:
        battle_panel.hide()
        leave_battle_button.hide()

    manager.process_events(event)

  manager.update(time_delta)

  pressed_keys = pygame.key.get_pressed()
  player1.update(pressed_keys)

  if pygame.sprite.collide_rect(player1, fountain):
    fountain_button.show()
    #t = Timer(10, fountain_button.hide())
  if (not (pygame.sprite.collide_rect(player1, fountain))):
    fountain_button.hide()
  if pygame.sprite.collide_rect(player1, biolBuilding):
    biol_button.show()
  if (not (pygame.sprite.collide_rect(player1, biolBuilding))):
    biol_button.hide()
  if pygame.sprite.collide_rect(player1, chemBuilding):
    chem_button.show()
  if (not (pygame.sprite.collide_rect(player1, chemBuilding))):
    chem_button.hide()

  DISPLAYSURF.blit(map, (0, 0))
  DISPLAYSURF.blit(player1.image, player1.rect)
  DISPLAYSURF.blit(biolBuilding.image, (550, 320))
  DISPLAYSURF.blit(chemBuilding.image, (450, 100))
  DISPLAYSURF.blit(fountain.image, (340, 290))
  manager.draw_ui(DISPLAYSURF)

  pygame.display.flip()
