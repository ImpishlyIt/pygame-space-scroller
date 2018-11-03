import sys, pygame, random
pygame.init()

bg = pygame.image.load("images/background.jpg")
myfont = pygame.font.SysFont('Comic Sans MS', 15)
bigfont = pygame.font.SysFont('Comic Sans MS', 30)

size = width, height = 640, 480
scalarspd = 8
shipmvmult = 64
speed = scalarspd * -1, 0
speed2 = speed[0] - 4, 0
speed3 = speed[0] - 2, 0
up = 0, -1 * shipmvmult
down = 0, 1 * shipmvmult
warpspeed = -1, 0

screen = pygame.display.set_mode(size)

bullet = pygame.image.load("images/bullet.png")
bullet2 = pygame.image.load("images/bullet.png")
bullet3 = pygame.image.load("images/bullet.png")
ship = pygame.image.load("images/ship.png")
warp = pygame.image.load("images/timewarp.png")

blipsz = 10

bliph = random.randint(blipsz, 480 - blipsz)
bliph2 = random.randint(blipsz, 480 - blipsz)
bliph3 = random.randint(blipsz, 480 - blipsz)
bliph4 = random.randint(blipsz, 480 - blipsz)

shiprect = ship.get_rect()
bliprect = bullet.get_rect(bottom=bliph, left = 640)
bliprect2 = bullet.get_rect(bottom=bliph2, left = 640)
bliprect3 = bullet.get_rect(bottom=bliph3, left = 640)
warprect = warp.get_rect(bottom = bliph4, left = 640)

ticks = 0
tickwarp = 0

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: quit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP: shiprect = shiprect.move(up)
			if event.key == pygame.K_DOWN: shiprect = shiprect.move(down)
			if event.key == pygame.K_q: quit()

	if (bliprect.left < 1):
		bliph = random.randint(blipsz, 480 - blipsz)
		bliprect = bullet.get_rect(bottom=bliph, left = 640)
	if (bliprect2.left < 1):
		bliph2 = random.randint(blipsz, 480 - blipsz)
		bliprect2 = bullet2.get_rect(bottom=bliph2, left = 640)
	if (bliprect3.left < 1):
		bliph3 = random.randint(blipsz, 480 - blipsz)
		bliprect3 = bullet3.get_rect(bottom=bliph3, left = 640)
	if (warprect.left < 1):
		bliph4 = random.randint(blipsz, 480 - blipsz)
		warprect = warp.get_rect(bottom = bliph4, left = 640)
	bliprect = bliprect.move(speed)
	bliprect2 = bliprect2.move(speed2)
	bliprect3 = bliprect3.move(speed3)
	warprect = warprect.move(warpspeed)
	ticks += 1
	if (shiprect.colliderect(bliprect) or shiprect.colliderect(bliprect2) or shiprect.colliderect(bliprect3)): break
	if (shiprect.colliderect(warprect)):
		tickwarp = ticks
		scalarspd = scalarspd / 2
	if ticks == tickwarp + 10:
		scalarspd = 8
	screen.blit(bg, (0, 0))
	screen.blit(bullet, bliprect)
	screen.blit(bullet2, bliprect2)
	screen.blit(bullet3, bliprect3)
	screen.blit(ship, shiprect)
	screen.blit(warp, warprect)
	pygame.display.flip()

print("Your score: " + str(ticks) + ".")
name = input("Enter your initials: ")
f = open("db/leaderboard.txt", "r+")
oldnames = ["", "", "", "", "", "", "", "", "", ""]
oldscores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
k = 0
placed = False
screen.fill((0, 0, 0))
for i in range(0, 9):
	oldnames[i] = f.readline().strip()
	oldscores[i] = f.readline().strip()
	if ticks > int(oldscores[i]):
		k = i + 1
		placed = True
		break
f.seek(0)
f2 = open("temp/leaderboard.tmp", "w+")
for j in range(1, 2*k - 1):
	f2.write(f.readline())
f2.write(name + "\n" + str(ticks) + "\n")
for j2 in range(2*k + 1, 21):
	f2.write(f.readline())
f.close()
f2.seek(0)
f3 = open("db/leaderboard.txt", "w+")
new = f2.read()
f3.write(new)
f3.seek(0)
f2.close()
textout = ["Leaderboard:", "", "", "", "", "", "", "", "", "", ""]
for i in range(1, 11):
	textout[i] += str((i)) + ": " + f3.readline().strip() + " - "
	textout[i] += f3.readline().strip()
f3.close()
screen.blit(bg, (0, 0))
for j in range(0, 11):
	screen.blit(myfont.render(textout[j], False, (255, 255, 255)), (50, 40 * j))
screen.blit(bigfont.render("Your Score:", False, (255, 255, 255)), (400, 0))
screen.blit(bigfont.render(str(ticks), False, (120, 255, 120)), (550, 50))
if placed:
	screen.blit(bigfont.render(("You are #" + str(k)), False, (120, 255, 120)), (400, 100))
screen.blit(bigfont.render("Press any button to close...", False, (200, 100, 90)), (200, 400))
pygame.display.flip()
print("Good job!")
while 1:
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN: quit()
