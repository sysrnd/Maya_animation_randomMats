#arturoalcibia@hotmail.com
import maya.cmds as cmds
'''
Skin = (1, 0.8, 0.8) - (1, 0.55, 0.55)
B = (0, 0, 0)
W = (1, 1, 1) - (1, 1, 1)
'''
SkinMat = ''
BMat = ''
WMat = ''

'''
if random assignation happens again
'''
try:
	if len(matList) > 0:
		for x in matList:
			cmds.delete(x)
except:
	pass
SkinList = ['MANO', 'BRAZO','PIERNA', 'ENCIA', 'LENGUA', 'CABEZA']
BList = ['PANTALON','SACO', 'CEJAS', 'CABELLO']
WList = ['FALDA', 'BLUSA','CORBATA', 'CAMISA', 'PLAYERA', 'CHAMARRA', 'CHALECO', 'VESTIDO', 'DIENTE']

matList = []

for mat in range(0, 3):
	shader=cmds.shadingNode("lambert",asShader=True)
	matList.append(shader)
	if mat == 0:
		SkinMat = shader
		cmds.setAttr(shader + ".color", 1.0, 0.8, 0.8, type="double3")
	elif mat == 1:
		BMat = shader
		cmds.setAttr(shader + ".color", 0, 0, 0, type="double3")
	else:
		WMat = shader
		cmds.setAttr(shader + ".color", 1, 1, 1, type="double3")

for geo in cmds.ls(et='mesh'):
	geoParent = cmds.listRelatives(geo, p=True)[0]
	if cmds.getAttr(geoParent + '.visibility') == 1:
		for index, names in enumerate(SkinList):
			if geo.upper().find(names.upper()) != -1:
				cmds.select(cl=True)
				cmds.select(geo)
				cmds.hyperShade(assign=SkinMat)
		for index, names in enumerate(BList):
			if geo.upper().find(names.upper()) != -1:
				cmds.select(cl=True)
				cmds.select(geo)
				cmds.hyperShade(assign=BMat)
		for index, names in enumerate(WList):
			if geo.upper().find(names.upper()) != -1:
				cmds.select(cl=True)
				cmds.select(geo)
				cmds.hyperShade(assign=WMat)