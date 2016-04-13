import matplotlib.pyplot as plt

landmarks1 = [[300, 300], [300, 303], [300, 307], [302, 312], [300, 313], [301, 320], [300, 322], [300, 326],
             [300, 328], [300, 331], [301, 335], [300, 340], [300, 345]]

landmarks2 = [[300, 300], [300, 303], [300, 307], [302, 312], [300, 313], [301, 320], [300, 322], [300, 326],
             [300, 328], [300, 331], [301, 335], [300, 340], [300, 345],
             [200, 100], [205, 110], [211, 122], [217, 120], [221, 125], [224, 130], [225, 127],
             [224, 130], [225, 132], [231, 132], [237, 135], [238, 135], [244, 138], [245, 137],
             [246, 138], [246, 138], [242, 142], [227, 145], [245, 145], [251, 148], [252, 147]]

landmarks = [[200, 100], [205, 110], [211, 122], [217, 120], [221, 125], [224, 130], [225, 127],
                         [224, 130], [225, 132], [231, 132], [237, 135], [238, 135], [244, 138], [245, 137],
                          [246, 138], [246, 138], [242, 142], [227, 145], [245, 145], [251, 148], [252, 147]]

def leastSquares(landmarks):
        Exy = Ex = Ey = Ex2 = 0
        for sth in landmarks:
            Exy = Exy + sth[0]*sth[1]
            Ex = Ex + sth[0]
            Ey = Ey + sth[1]
            Ex2 = Ex2 + sth[0]**2

        n = len(landmarks)
        a = (n*Exy - Ex*Ey)/(n*Ex2 - Ex**2)
        b = Ey/n - a*Ex/n

        return [a, b]

class claster:
    def __init__(self):
        self.points = []

    def addOrNotAdd(self, point):
        if len(self.points) < 3:
            self.points.append(point)
            return True
        else:
            diff = self.points[-1]
            pass



for sth in landmarks:
    pass#plt.plot(sth[0],   sth[1], '*')

a, b = leastSquares(landmarks)
if a < 0.1:
        x0 = landmarks[0][0]
        y0 = landmarks[0][1]
        x1 = landmarks[len(landmarks) - 1][0]
        y1 = landmarks[len(landmarks) - 1][1]
else:
        x0 = landmarks[0][0]
        y0 = a*x0 + b

        x1 = landmarks[len(landmarks) - 1][0]
        y1 = a*x1 + b

plt.plot(landmarks[len(landmarks) - 1][0], landmarks[len(landmarks) - 1][1], 'x')
plt.plot([x0, y0], [x1, y1], 'r')
plt.plot([0, 1],'.', [500, 500], '.')
plt.show()




