
import numpy as np
import open3d as o3d
import os
import glob
from pypcd import pypcd
import shutil

def viz_mayavi(velo_path,out_path):
    velo_bins = glob.glob(velo_path + '/*.pcd')
    print(velo_bins)
    velo_bins.sort()
    num_frames = len(velo_bins)
    velo_files = {i: velo_bins[i] for i in range(len(velo_bins))}
    for i in range(num_frames):
        pc = pypcd.PointCloud.from_path(velo_files[i])
        np_x = (np.array(pc.pc_data['x'], dtype=np.float32)).astype(np.float32)
        np_y = (np.array(pc.pc_data['y'], dtype=np.float32)).astype(np.float32)
        np_z = (np.array(pc.pc_data['z'], dtype=np.float32)).astype(np.float32)
        np_i = (np.array(pc.pc_data['intensity'], dtype=np.float32)).astype(np.float32) / 255
        points_32 = np.transpose(np.vstack((np_x, np_y, np_z, np_i)))
        filepath, fullfilename=os.path.split(velo_files[i])
        fname,ext = os.path.splitext(fullfilename)
        print(fname)
        points_32.tofile(out_path + fname + '.bin')
        print(out_path + os.path.basename(out_path + fname + '.bin'),'done')
        
        

if __name__=="__main__":
    # velo_path = '16line_3d_pcd/3d-pcd/'
    # out_path = 'real_16line_3d_bin_pypcd/'
    input_pcd_path="/media/binyu/WD_BLACK1/2022CIAC/pre_match/train/pcd_ascii_test"
    output_bin_path="/media/binyu/WD_BLACK1/2022CIAC/pre_match/train/bin_test"
    if os.path.exists(output_bin_path):
        shutil.rmtree(output_bin_path)
        os.mkdir(output_bin_path)

    for sub_folder in os.listdir(input_pcd_path):
        sub_folder_full = os.path.join(input_pcd_path, sub_folder) + '/pcd/'

        os.mkdir(os.path.join(output_bin_path, sub_folder))
        save_folder_full = os.path.join(output_bin_path, sub_folder) + '/pcd/'
        os.mkdir(save_folder_full)

        # for pcd in os.listdir(sub_folder_full):
        viz_mayavi(sub_folder_full, out_path=save_folder_full)

    # velo_path = "/media/binyu/WD_BLACK1/2022CIAC/pre_match/train/pcd_ascii/2020-07-18-10-34-31_9-follow/pcd/"  
    # out_path = '/media/binyu/WD_BLACK1/2022CIAC/pre_match/train/bin/2020-07-18-10-34-31_9-follow/pcd/'

    
    # for sub_folder in os.listdir(input_pcd_path):
    #     sub_folder_full = os.path.join(input_pcd_path, sub_folder) + '/pcd'
    # # velo_path = 'igear_pcd_000965/'  
    # # out_path = 'igear_pcd_tobin/'
    # if not os.path.exists(out_path):
    #     os.makedirs(out_path)
    # viz_mayavi(velo_path,out_path)

