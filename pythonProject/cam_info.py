import numpy as np

#imagesize
panoImg = (1280,720)

#cameraMatrix
cameraMatrix = np.array([[679.1176670051829, 0, 630.8964554624615],
                         [0, 675.1683830691559, 373.7653437656825],
                         [0,0,1]])

#disCoeffs
disCoeffs = np.array([-0.4094444173515146, 0.2421557697649201, 0.001657031388808141, 0.0007985350528495049, -0.08329170939949609])

#backup
backup_poly = np.array([[]])

#mask
maskpoints2 = np.array([[[751, 700], [1196, 698], [565, 900], [429, 900]]])
# mask Now:
maskpoints1 = np.array([[[822,852], [1121, 852], [1675, 1080], [472, 1080]]])




#warpperspective_points
f_pts1 = np.float32([[0,200],[1280,200],[0,720],[1280,720]])
f_pts2 = np.float32([[100,100],[1180,100],[460,250],[860,250]])

r_pts1 = np.float32([[0,140],[1280,140],[0,720],[1280,720]])
r_pts2 = np.float32([[1280,53],[1280,667],[985,192],[980,526]])
r_mask = np.array([[[821,720], [965, 720], [1349, 970], [483, 970]]])

b_pts1 = np.float32([[0,200],[1280,200],[0,720],[1280,720]])
b_pts2 = np.float32([[1180,620],[100,620],[860,470],[460,470]])

l_pts1 = np.float32([[0,120],[1280,120],[0,720],[1280,720]])
l_pts2 = np.float32([[0,662],[0,60],[320,528],[320,191]])
l_mask = np.array([[[821,720], [965, 720], [1349, 970], [483, 970]]])

#car_imagesize
car_x = 200
car_y = 300

#corners
f_corners1 = np.array([[434,375],[660,392],[332,566],[705,593]])
f_corners2 = np.array([[400,200],[600,200],[400,600],[600,600]])