import glob
import pandas as pd
import numpy as np
import json
test_metadata = '../herbarium-2022-fgvc9/test_metadata.json'

def read_files(glob_files):
    with open(test_metadata) as json_file:
        test_meta = json.load(json_file)

        test_ids = [image['image_id'] for image in test_meta]

        test_df = pd.DataFrame({
            "test_id" : test_ids,
        })
    
    submission_json = {}
    submission_json_new ={}
    
#     for i, glob_file in enumerate(glob(glob_files)):
    for i, files in enumerate(glob.glob(glob_files+"*.json")):
        with open(files) as json_file:
            pred_result = json.load(json_file)
            df_pred = np.asarray(pred_result['pred_label'])
            df_score = np.asarray(pred_result['pred_score'])
        submission_pd = pd.DataFrame({"id": test_df['test_id'], "Predicted": df_pred, "score":df_score})
        if i == 0:
            for j in range(len(submission_pd)):
                submission_json[str(submission_pd.loc[j,'id'])] ={str(submission_pd.loc[j,'Predicted']):submission_pd.loc[j,'score']}
        else:
            for j in range(len(submission_pd)):
                submission_json_new[str(submission_pd.loc[j,'id'])] ={str(submission_pd.loc[j,'Predicted']):submission_pd.loc[j,'score']}
#             for k in submission_json_new.keys():
#                 if submission_json_new[str(k)].keys() == submission_json[str(k)].keys():
#                     update_score = list(submission_json_new['0'].values())[0] + list(submission_json_new['1'].values())[0]
# #                     submission_json[str(k)][list(submission_json['0'].keys())[0]] = update_score
#                     update_str = {str(k):{list(submission_json['0'].keys())[0]:update_score}}
#                     submission_json.update(update_str)
#             for (j,k) in zip(submission_json,range(len(submission_pd))):
# #                 print(j,k)
# #                 print(submission_json[str(j)])
# #                 print(submission_pd.loc[k,'Predicted'])
#                 if str(submission_pd.loc[k,'Predicted']) in submission_json[str(j)]:
# #                 if submission_json[str(j)][str(submission_pd.loc[j,'Predicted'])]:
#                     submission_json[submission_pd.loc[k,'id']].update({str(submission_pd.loc[k,'Predicted']):submission_pd.loc[k,'score']+submission_json[str(j)][str(submission_pd.loc[k,'Predicted'])]})
#                 else:
#                     submission_json[submission_pd.loc[k,'id']].update({str(submission_pd.loc[k,'Predicted']):submission_pd.loc[k,'score']})

    return submission_json,submission_json_new
#         count_index_score(files, save_csv_path)
#         print(files,'writing to', save_csv_path,'done')

glob_files = "res101_resize_fp16_s672_normstd_enhance_total7_ep101_tta_pillow_bicubic_test/"
submission_json,submission_json_new = read_files(glob_files)
