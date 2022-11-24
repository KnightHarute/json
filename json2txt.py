"""
Description: This .py helps to convert label into txt format
Create by Lin, 20221025
"""
import os
import json as js
import shutil


json_folder = 'E:/BaiduNetdiskDownload/game3/train/json'
txt_folder = 'E:/BaiduNetdiskDownload/game3/train/txt'

"""
[{'tracker_id': 1, 'type': 'car', 'center': {'x': -24.279348608273, 'y': -5.2423334117426, 'z': -2.0024138048457}, 
   'size': {'long': 4.4529558208129, 'wide': 2.0601687376725, 'high': 1.6085875282425}, 'rotation': 0.28096828192226}, 
 ...
]
“0”代表行人、“1”代表骑行者、“2”代表小车、“3”代表大车
ObjectLength表示三维边界框的长、ObjectWidth表示三维边界框的宽、ObjectHeight表示三维边界框的高；
CenterX表示三维边界框的中心点x、CenterY表示三维边界框的中心点y、CenterZ表示三维边界框的中心点z;
Yaw表示三维边界框航向角

KITTI Format:
type: 0
truncated: 1
occluded: 2
alpha: 3
bbox: 4-7
dimensions: 8-10   hwl
location: 11-13    xyz
rotation_y: 14
score: 15
"""


def convert_json2txt(json, save_path):
    json_id = json[:-5]
    # print(json_id)
    txt_full = save_path + '/' + json_id + '.txt'
    txt_writer = open(txt_full, 'w+')

    json_full = os.path.join(sub_folder_full, json)

    with open(json_full) as f:
        annos = js.load(f)
        print(annos)
        for anno in annos:
            print(anno.keys())  # dict_keys(['tracker_id', 'type', 'center', 'size', 'rotation'])
            tracker_id, type_, center, size, rotation = anno['tracker_id'], anno['type'], anno['center'], \
                                                        anno['size'], anno['rotation']
            print(size, center)
            l, w, h = size['long'], size['wide'], size['high']  # {'long': 4.4529558208129, 'wide': 2.0601687376725, 'high': 1.6085875282425}
            x, y, z = center['x'], center['y'], center['z']
            txt_writer.write('{} {} {} {} {} {} {} {} {} {} {} {} {} {} {}\n'.format(type_, 0, 0, 0, 0, 0, 0, 0, l, w, h, x, y, z, rotation))

    txt_writer.close()


if __name__ == '__main__':

    if os.path.exists(txt_folder):
        shutil.rmtree(txt_folder)
        os.mkdir(txt_folder)

    for sub_folder in os.listdir(json_folder):
        sub_folder_full = os.path.join(json_folder, sub_folder) + '/pcd'

        os.mkdir(os.path.join(txt_folder, sub_folder))
        save_folder_full = os.path.join(txt_folder, sub_folder) + '/pcd'
        os.mkdir(save_folder_full)

        for json in os.listdir(sub_folder_full):
            convert_json2txt(json, save_path=save_folder_full)
            # exit()