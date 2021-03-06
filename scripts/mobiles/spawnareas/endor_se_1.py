# Spawn Area file created with PSWG Planetary Spawn Tool
import sys
from java.util import Vector

def addSpawnArea(core):
	dynamicGroups = Vector()
	dynamicGroups.add('endor_bark_mite')
	dynamicGroups.add('endor_bloodseeker')
	dynamicGroups.add('endor_bolle')
	dynamicGroups.add('endor_donkuwah')
	dynamicGroups.add('endor_jinda')
	core.spawnService.addDynamicSpawnArea(dynamicGroups, 5500, -5500, 3500, 'endor')
	return
