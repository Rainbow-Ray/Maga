import calendar
import openpyxl

import pandas as pd
from great_tables import GT,loc, style

cal = calendar.LocaleTextCalendar(locale='ru')

oct = cal.formatmonth(2025, 10)
for i in oct:
    i

cal = calendar.Calendar()

oct = cal.monthdatescalendar(2025,10)

month = []
for w in oct:
    week = []
    for d in w:
        week.append(d.day)
    month.append(week)

df = pd.DataFrame(month)

df = df.rename(columns={
    0: 'Пн',
    1: 'Вт',
    2: 'Ср',
    3: 'Чт',
    4: 'Пт',
    5: 'Сб',
    6: 'Вс',

})

start_date = 10
end_date = 10



def tablde():
    tb = (
        GT(df)
        .tab_header(title="Октябрь")
        .fmt_integer(columns=['Пн','Вт','Ср', 'Чт', 'Пт','Сб','Вс'], compact=True)
        .tab_style(locations=loc.header(),
                   style=[style.text(font='overdoze sans'),
                          style.borders(sides='all', color='#000000', style='dashed', weight='2px')
                          ])

        .tab_style(locations=loc.body(columns=['Пн', 'Вт'], rows=[0]),
                   style = [
                            style.text(color="gray", weight="thin", )])
        .tab_style(locations=loc.body(columns=['Сб','Вс'], rows=[4]),
                   style = [style.text(color="gray", weight="thin")])
        .tab_style(locations=loc.body(),
                   style = [style.text( align='center', v_align='middle'), ])
    )
    tb.show()
