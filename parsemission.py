
class ParticleSystem(object):
    """Holds the position and name of ptf file for a particle system in a level"""
    def __init__(self, ptfFile, particlePos):
        self.ptfFile = ptfFile
        self.particlePos = particlePos

    def __repr__(self):
        return "Particle System '" + self.ptfFile + "' at " + str(self.particlePos)

class Model(object):
    """Holds the position and name of model file for a model in a level"""
    def __init__(self, modelName, modelPos):
        self.modelName = modelName
        self.modelPos = modelPos

    def __repr__(self):
        return "Model '" + self.modelName + "' at " + str(self.modelPos)

def parseMissionFile(filename):
    """Returns a list of ParticleSystem and Model objects with file names and positions of objects in the level
    from the .mission file."""
    f = open(filename, "r")
    file = f.read()
    f.close()
    models = []  #model name: pos

    for line in file.split("\n"):  #go through each line
        lineContents = line.split(":")
        pos = lineContents[1].split(",")
        if lineContents[0].startswith("particle"):
            models.append(ParticleSystem(ptfFile = lineContents[0][8:], particlePos = (float(pos[0]), float(pos[1]), float(pos[2]))))
        else:
            models.append(Model(modelName = lineContents[0], modelPos = (float(pos[0]), float(pos[1]), float(pos[2]))))

    return models

if __name__ == "__main__":
    print(str(parseMissionFile("models/m1.mission")))