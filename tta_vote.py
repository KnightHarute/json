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
#             for j in range(len(submission_pd)):
            print(submission_pd.loc[0,'Predicted'])
            for (j,k) in zip(submission_json,range(len(submission_pd))):
                if str(submission_pd.loc[k,'Predicted']) in submission_json[str(j)]:
#                 if submission_json[str(j)][str(submission_pd.loc[j,'Predicted'])]:
                    submission_json[str(submission_pd.loc[k,'id'])].update({str(submission_pd.loc[k,'Predicted']):submission_pd.loc[k,'score']+submission_json[str(j)][str(submission_pd.loc[k,'Predicted'])]})
                else:
                    submission_json[str(submission_pd.loc[k,'id'])].update({str(submission_pd.loc[k,'Predicted']):submission_pd.loc[k,'score']})

    return submission_json


glob_files = "res101_resize_fp16_s672_normstd_enhance_total7_ep101_tta_pillow_bicubic_test/"
submission_json = read_files(glob_files)
