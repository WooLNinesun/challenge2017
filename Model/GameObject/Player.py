from model_const import *
class player(object):
    def __init__(self, name, index, AI = None):
        # basic data
        self.name = nam
        self.index = index
        self.mode = 1
        self.modeTimer = 0
        # 0 = attack
        # 1 = defense
        self.power = 30
        self.score = 0
        self.skillcard = None
        self.takeball = -1
        self.is_AI = is_AI
        self.AI = AI

        # move data
        self.position = playerInitPos[index]
        self.direction = 0        
        
        #mask data
        self.isMask = False
        self.maskTimer = 0

        #freeze data
        self.isFreeze = False
        self.freezeTimer = 0
        
        #invisible data
        self.isVisible = True
        self.invisibleTime = 0

    def freeze(self, freezeTime):
        self.isFreeze = True
        self.freezeTimer = freezeTime
        self.direction = 0

    def hide(self):
        self.isVisible = True
        self.invisibleTime = invisibleTime 

    def setBarrier(self):
        self.power -= barrierPowerCost
        return (self.position, self.direction)

    def shot(self):
        ballIndex = self.takeball
        self.takeball = -1
        return (ballIndex, self.direction)

    def changeDirection(self, direction):
        self.direction = direction

    def reSetMask(self):
        self.isMask = False
        self.maskTimer = 0

    def tickCheck(self):
        self.position[0] += dirConst[self.direction][0]*playerSpeed
        self.position[1] += dirConst[self.direction][1]*playerSpeed
        if self.isFreeze == True:
            self.freezeTimer = self.freezeTimer - 1
            self.direction = 0
            if self.freezeTimer == 0:
                self.isFreeze = False

        if self.power <= powerMax:
            self.power += 1
        if self.modeTimer > 0:
            self.modeTimer = self.modeTimer - 1

        if self.position[0] < 47 or self.position[0] > 693 :
            self.direction = dirConst[0][self.direction]
        elif self.position[1] < 47 or self.position[1] > 693 :
            self.direction = dirConst[1][self.direction]

        if self.isMask == True:
            self.maskTimer = self.maskTimer - 1
        if self.maskTimer == 0:    
            self.isMask == False

    def bump(self, target):
        outData = []
        if (self.direction[0]-target.direction[0])**2+(self.direction[1]-target.direction[1])**2 <= playerBumpDistance**2:
            selfFreeze = True
            targetFreeze = True
            if self.mode != target.mode:
                if self.mode == 1:
                    selfFreeze == False
                elif target.mode == 1:
                    targetFreeze == False
            
            if self.isMask == True && selfFreeze == True:
                selfFreeze = False
                self.reSetMask()

            if target.isMask == True && targetFreeze == True:
                targetFreeze == False
                target.reSetMask()

            
            if selfFreeze == True:
                self.freeze()
                if self.takeball != -1:
                    outData.append( (self.takeball, self.direction) )
            if targetFreeze == True:
                target.freeze()
                if target.takeball != -1:
                    outData.append( (target.takeball, target.direction) )

        return outData