import maya.cmds as cmds
import Utils.os_Find_Env.findEnv_app as findEnv

class randomMatsAssign(object):
	def __init__(self):

		self.checkForExistingMaterials()

		self.SkinList = ['MANO', 'BRAZO','PIERNA', 'ENCIA', 'LENGUA', 'CABEZA']
		self.BList = ['PANTALON','SACO', 'CEJAS', 'CABELLO', 'ZAPATO']
		self.WList = ['FALDA', 'BLUSA','CORBATA', 'CAMISA', 'PLAYERA', 'CHAMARRA', 'CHALECO', 'VESTIDO', 'DIENTE']
		self.eyesList = ['OJO', 'RETINA']
		self.skippedWords = ['WRAP', 'BS', 'WIRE']

		self.skin = (1.0, 0.8, 0.8)
		self.black = (0, 0, 0)
		self.white = (1, 1, 1)

		#to modify it just add a new entry to the dict
		self.MatsRelation = {
							'skinMat_za': (self.assignMatColor ,self.SkinList, self.skin), 
							'blackMat_za': (self.assignMatColor ,self.BList, self.black), 
							'whiteMat_za': (self.assignMatColor ,self.WList, self.white),
							'eyesMat_za': (self.assignMatTexture ,self.eyesList, None)
							}

		self.matList = {}

	def main(self):
		geoInScene = self.scanForGeo()

		for geoP in geoInScene:
			mat = self.assignKeyDict(geoP)
			
			if mat != None:
				self.MatsRelation[mat[0]][0](mat)


	def checkForExistingMaterials(self):
		
		'''
		TODO: change to search by name
		'''

		try:
			if len(self.matList) > 0:
				for x in matList:
					cmds.delete(x)
		except:
			pass
	@undoManagerCh
	def assignKeyDict(self, geo):

		valid = True
		mat = []
		
		for skippedWord in self.skippedWords:
			if geo.upper().find(skippedWord.upper()) != -1:
				valid = False

		if valid == False:
			return None
			
		for key, lists in self.MatsRelation.iteritems():
			for word in lists[1]:
				if geo.upper().find(word.upper()) != -1:

					mat.append(key)
					mat.append(geo)

		if len(mat) > 0:
			return mat

	def createMat(self, key):
		'''
		scan for mat or create if it cant find one
		'''
		mat = key[0]
		color = self.MatsRelation[key[0]][2]

		print mat
		
		if cmds.objExists(mat) == True:
			return mat
		else:
			shader = cmds.shadingNode("lambert",asShader=True, n=mat)
			cmds.setAttr(shader + ".color", *color, type="double3")
		
		return mat

	def assignMatColor(self, key):

		shader = self.createMat(key)
		
		cmds.select(cl=True)
		cmds.select(key[1])
		cmds.hyperShade(assign=shader)


	def assignMatTexture(self, key):
		'''
		'''

		print 'textureee'

	def scanForGeo(self):
		'''
		'''

		geoInScene = []

		for geo in cmds.ls(et='mesh'):
			geoParent = cmds.listRelatives(geo, p=True)[0]
			if geoParent not in geoInScene:
				geoInScene.append(geoParent)

		return geoInScene

assign = randomMatsAssign()
assign.main()