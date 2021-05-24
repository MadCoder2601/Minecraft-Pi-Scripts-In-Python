from mcpi import minecraft

stone = 1

mc = minecraft.Minecraft.create()

pos = mc.player.getPos()

x, y, z = mc.player.getPos()

mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, stone)
