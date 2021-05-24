from mcpi import minecraft

mc = minecraft.Minecraft.create()

pos = mc.player.getPos()

x, y, z = mc.player.getPos()

mc.player.setPos(x, y+100, z)
