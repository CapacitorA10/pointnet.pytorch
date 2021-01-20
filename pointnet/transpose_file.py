import numpy as np

#for문 2개로 파일 입출력 범위 조절
for j in range(2):
    for i in range(10):
        # load data
        load_dir =  'C:\\Users\\범\\PycharmProjects\\pointnet.pytorch\\face_db\\임시\\test_data\\labeled_test_pcd\\{0}{1}.ply'.format(j+8,i)
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
        save_dir_pts = 'C:\\Users\\범\\PycharmProjects\\pointnet.pytorch\\face_db\\임시\\test_data\\pts\\{0}{1}.pts'.format(j+8, i)
        save_dir_seg = 'C:\\Users\\범\\PycharmProjects\\pointnet.pytorch\\face_db\\임시\\test_data\\lab\\{0}{1}.seg'.format(j+8, i)
        np.savetxt(save_dir_pts, points, fmt='%.10f')
        np.savetxt(save_dir_seg, output_labels, fmt='%d')



print("done")







