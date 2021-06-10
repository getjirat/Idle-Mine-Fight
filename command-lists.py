class game():
  class workspace():
    class gameobjectstorage():
      def addtoworkspace(object_name,x,y):
        addsprite = ""
        addsprite = pygame.image.load("assets/game/workspace/gameobjectstorage/",object_name,".png")
        screen.blit(addsprite,(x,y))
