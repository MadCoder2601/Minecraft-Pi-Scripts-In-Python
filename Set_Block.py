from mcpi import minecraft

mc = minecraft.Minecraft.create()

pos = mc.player.getPos()

x, y, z = mc.player.getPos()

mc.setBlock(x-1, y, z, 1)
