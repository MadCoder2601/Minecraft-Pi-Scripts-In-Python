from mcpi.minecraft import Minecraft

from time import sleep

mc = Minecraft.create()

pos = mc.player.getPos()

while True:
	x, y, z = mc.player.getPos()

	this_block = mc.getBlock(x, y, z)
	
	this_block = str(this_block)

	print(this_block + " is the id for the block that your standing in") # This will print the block id that your standing in
	
	sleep(1)
	
	block_beneath = mc.getBlock(x, y-1, z)
	
	block_beneath = str(block_beneath)
	
	print(block_beneath + " is the id for the block that your standing on") # This will print the block id that is under you
	
	sleep(1)
