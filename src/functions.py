import pandas as pd
import openpyxl as xlsx
from pandas import DataFrame
import os


def import_dataframes():
    dataframes = []
    directory = 'data'

    for filename in os.scandir(directory):
        if filename.is_file():
            dataframes.append({'name': filename.name, 'data': pd.read_json(path_or_buf=filename.path, lines=True)})
    return dataframes


dataframes = import_dataframes()


def language_translate_to_xlsx(file_path):
    df_pivot = pd.read_json(path_or_buf='dataset/data/en-US.jsonl', lines=True, encoding='utf-8').get(
        ['id', 'utt', 'annot_utt'])
    df_lang = pd.read_json(path_or_buf=file_path, lines=True, encoding='utf-8').get(['id', 'utt', 'annot_utt'])

    workbook = xlsx.Workbook()
    worksheet = workbook.active

    worksheet['A1'] = 'id'
    worksheet['B1'] = 'utt'
    worksheet['C1'] = 'annot_utt'
    worksheet['D1'] = file_path[0:5] + '_utt'
    worksheet['E1'] = file_path[0:5] + '_annot_utt'

    for index, row in df_pivot.iterrows():
        cell = worksheet.cell(row=index + 2, column=1)
        cell.value = row['id'] + 1

        cell = worksheet.cell(row=index + 2, column=2)
        cell.value = row['utt']

        cell = worksheet.cell(row=index + 2, column=3)
        cell.value = row['annot_utt']

    for index, row in df_lang.iterrows():
        cell = worksheet.cell(row=index + 2, column=4)
        cell.value = row['utt']

        cell = worksheet.cell(row=index + 2, column=5)
        cell.value = row['annot_utt']

    workbook.save('outputs/xlsx/en-' + file_path[0:5] + '.xlsx')

#QUESTION 2
def partition_filter_on_languages():
    df_english = pd.read_json(path_or_buf='data/en-US.jsonl', lines=True)
    df_swahili = pd.read_json(path_or_buf='data/sw-KE.jsonl', lines=True)
    df_german = pd.read_json(path_or_buf='data/de-DE.jsonl', lines=True)

    df_english = df_english[df_english['partition'] == 'test']
    df_swahili = df_swahili[df_swahili['partition'] == 'train']
    df_german = df_german[df_german['partition'] == 'dev']

    df_english.to_json(r'outputs/en-US-test.jsonl', orient='records', lines=True)
    df_swahili.to_json(r'outputs/sw-KE-train.jsonl', orient='records', lines=True)
    df_german.to_json(r'outputs/de-DE-dev.jsonl', orient='records', lines=True)


def all_translations_to_json():
    df_pivot: DataFrame = pd.read_json(path_or_buf='data/en-US.jsonl', lines=True, encoding='utf-8')

    pivot_filtered: DataFrame = df_pivot[df_pivot['partition'] == 'train'].get(['id', 'utt'])

    pivot_filtered['translations'] = 'null'

    for index, row in pivot_filtered.iterrows():
        pivot_filtered.at[index, 'translations'] = get_translations_array(index)

    pivot_filtered.to_json(r'outputs/en-xx-train-set-translations.jsonl', orient='records', lines=True, indent=4,
                           force_ascii=False)


def get_translations_array(index):
    translations_list = {}

    for dataframe in dataframes:
        if dataframe['name'].contains('en-US'):
            continue

        abbreviation = dataframe['name'][0:5]

        translation: str = dataframe['data'][dataframe['data']['partition'] == 'train'].at[index, 'utt']

        translations_list[abbreviation] = translation

    return translations_list