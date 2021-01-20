import numpy as np

#for문 2개로 파일 입출력 범위 조절
for j in range(3):
    for i in range(10):
        # load data
        load_dir =  'C:\\Users\\범\\Documents\\MATLAB\\facedb\\woo\\0{0}{1}.ply'.format(j,i)
        origin = np.loadtxt(load_dir, dtype='double', skiprows=10)
        points = origin[:, 0:3]
        labels = origin[:, 3:]

        # process data
        points = points / 100
        n = labels.shape[0]
        output_labels = np.zeros([n], dtype=int)

        for k in range(labels.shape[0]):
            w = labels[k, :]
            if (w[0] == 0) & (w[1] == 0) & (w[2] == 255):
                output_labels[k] = 0

            elif (w[0] == 255) & (w[1] == 0) & (w[2] == 0):
                output_labels[k] = 1

            elif (w[0] == 0) & (w[1] == 255) & (w[2] == 0):
                output_labels[k] = 2

            else:
                output_labels[k] = 3

        # save data
        save_dir_pts = 'D:\\facedb\\FaceDB_pre_process\\points\\{0}{1}.pts'.format(j, i)
        save_dir_seg = 'D:\\facedb\\FaceDB_pre_process\\points_label\\{0}{1}.seg'.format(j, i)
        np.savetxt(save_dir_pts, points, fmt='%.10f')
        np.savetxt(save_dir_seg, output_labels, fmt='%d')



print("done")







