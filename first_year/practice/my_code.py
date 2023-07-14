import csv

from get_median_frame import make_frame

from hist_median_frame import make_hist


from openpyxl import load_workbook

import pandas as pd


def get_data(list_min, list_hour, list_folders, bad_videos):
    with open('data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)

        for i in range(len(list_hour)):
            for j in range(len(list_min) - 1):
                print(f'HERE {list_hour[i]}.{list_min[j]}')
                if (f'{list_hour[i]}.{list_min[j]}' in bad_videos):
                    continue

                if (list_min[j] == '55'):
                    path = f'{list_hour[i]}.{list_min[j]}.00-{list_hour[i + 1]}.{list_min[j + 1]}.00[R][0@0][0]'
                else:
                    path = f'{list_hour[i]}.{list_min[j]}.00-{list_hour[i]}.{list_min[j + 1]}.00[R][0@0][0]'

                frame_folder = list_folders[i]
                video_folder = f'video/archive{list_hour[i]}'
                make_frame(path, frame_folder, video_folder)
                data = make_hist(path, frame_folder)

                writer.writerow(data)


def input_to_excel(excel_file, csv_file):
    workbook = load_workbook(filename=excel_file)
    ws4 = workbook["Sheet1"]

    start_row = 4
    with open(csv_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader, None)

        for row in csv_reader:
            available_status = ws4.cell(row=start_row, column=10).value
            while (available_status is not None):
                start_row += 1
                available_status = ws4.cell(row=start_row, column=10).value

            ws4.cell(row=start_row, column=12).value = row[0]
            ws4.cell(row=start_row, column=13).value = row[1]
            ws4.cell(row=start_row, column=14).value = row[2]
            ws4.cell(row=start_row, column=15).value = f'{row[3]}; {row[4]}'
            ws4.cell(row=start_row, column=16).value = f'{row[5]}; {row[6]}'

            for i in range(6):
                print(row[i])
            start_row += 1

    workbook.save(excel_file)


if __name__ == '__main__':
    list_min = ['00', '05', '10', '15', '20', '25', '30',
                '35', '40', '45', '50', '55', '00']
    list_hour = ['08', '09', '10', '11']
    list_folders = ['8.00-9.00 06.07.2023',
                    '9.00-10.00 06.07.2023',
                    '10.00-11.00 06.07.2023',
                    '11.00-12.00 06.07.2023']
    bad_videos = ['08.05', '08.35', '08.40', '09.35', '09.40',
                  '09.45', '09.55', '10.40', '10.45', '11.55']
    header = ['math expect, disperc, sqrt mean, max_x, max_y, min_x, min_y']
    get_data(list_min, list_hour, list_folders, bad_videos)

    excel_file = '8.00-12.00 06.07.2023\Разметка видео.xlsx'
    input_to_excel(excel_file, 'data.csv')
