from gl import Render

r = Render()
r.glInit(8000,6000)

r.load('./Ivy.obj', (1.2, 0.05), (3200, 3200))

r.glFinish("Ivy.bmp")