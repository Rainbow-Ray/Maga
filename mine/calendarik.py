import calendar
import openpyxl as ex
import pandas as pd
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.styles import PatternFill, Border, Side, Alignment, Protection, Font

font = Font(name='Century Gothic',
                size=20,
                bold=False,
                italic=False,
                vertAlign='baseline',
                underline='none',
                strike=False,
                color='FF000000')

black = 'FF000000'
lightGray = 'd8d8d8'
gray = 'a5a5a5'

thickOuterBorder= Side(border_style='thick',
                          color=black)
headerDashBorder = Side(border_style='mediumDashed', color=black)
headerGrayBorder = Side(border_style='thin', color=lightGray)
calDashBorder = Side(border_style='dashed', color=black)

border = Border(left=Side(border_style=None,
                          color='FF000000'),
                right=Side(border_style=None,
                           color='FF000000'),
                top=Side(border_style=None,
                         color='FF000000'),
                bottom=Side(border_style=None,
                            color='FF000000'),
                outline=Side(border_style=None,
                             color='FF000000'),
                vertical=Side(border_style=None,
                              color='FF000000'),
                horizontal=Side(border_style=None,
                               color='FF000000')
               )

alignment=Alignment(horizontal='center',
                    vertical='center',
                    text_rotation=0,
                    wrap_text=False,
                    shrink_to_fit=False,
                    indent=0)
number_format = 'General'

_year = 2025
_month = 11
daysColumn = {
    0: 'Пн',
    1: 'Вт',
    2: 'Ср',
    3: 'Чт',
    4: 'Пт',
    5: 'Сб',
    6: 'Вс',
}
def localeCal(_year, _month):
    cal = calendar.LocaleTextCalendar(locale='ru')
    month = cal.formatmonth(_year, _month)
    return cal, month

def dateCal(_year, _month):
    cal = calendar.Calendar()
    month = cal.monthdatescalendar(_year, _month)
    return cal, month

def calToList(month):
    monthList = []
    for w in month:
        week = []
        for d in w:
            week.append(d.day)
        monthList.append(week)
    return monthList

def CalToDf(month):
    df = pd.DataFrame(month)
    df = df.rename(columns= daysColumn)
    return df


def main():
    cal, month = dateCal(_year, _month)
    print(month)
    df = CalToDf(month)
    column = (df.columns.values)
    print(column)
    wb = ex.Workbook()
    ws = wb.active
    for h in df.columns:
        df[h] = df.apply(lambda cell: cell[h].day, axis=1)

    column = column.tolist()
    ws.append(column)
    for row in ex.utils.dataframe.dataframe_to_rows(df, header=False, index=False):
        ws.append(row)
    wb.save("pandas_openpyxl.xlsx")


main()

# def tablde():
# start_date = 10
# end_date = 10

#     tb = (
#         GT(df)
#         .tab_header(title="Октябрь")
#         .fmt_integer(columns=['Пн','Вт','Ср', 'Чт', 'Пт','Сб','Вс'], compact=True)
#         .tab_style(locations=loc.header(),
#                    style=[style.text(font='overdoze sans'),
#                           style.borders(sides='all', color='#000000', style='dashed', weight='2px')
#                           ])
#
#         .tab_style(locations=loc.body(columns=['Пн', 'Вт'], rows=[0]),
#                    style = [
#                             style.text(color="gray", weight="thin", )])
#         .tab_style(locations=loc.body(columns=['Сб','Вс'], rows=[4]),
#                    style = [style.text(color="gray", weight="thin")])
#         .tab_style(locations=loc.body(),
#                    style = [style.text( align='center', v_align='middle'), ])
#     )
#     tb.show()
