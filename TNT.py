from mcpi import minecraft

from time import sleep

mc = minecraft.Minecraft.create()

pos = mc.player.getPos()

x, y, z = mc.player.getPos()

timer = 0

mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, 46, 1)

while True:
	timer = timer + 1
	sleep(1)
	if timer == 120:
		quit()
