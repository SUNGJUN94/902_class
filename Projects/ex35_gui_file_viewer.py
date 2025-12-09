# tkinter file choice & viewer

# 기능요구
#1. 파일선택 버튼을 누르면 엑셀파일을 선택할 수 있어야 함.
#2. 선택한 파일경로는 Entry 요소에 보여야 함
#3. '파일일기'버튼을 누르면 해당경로의 엑셀을 pandas로 읽어야 함.
#4. '그래프보기'버튼을 누르면 숫자데이터들이 선그래프로 보여야 함
#5. '엑셀데이터보기'버튼을 누르면 다시 표 형태의 데이터가 보여야 함.

#0. 필요한 라이브러 추가
from tkinter import *

#1. 최상위 윈도우 위젯 만들기
window= Tk()
window.title('엑셀 파일 뷰어')
window.geometry('800x600-100+50')

#2. 파일 선택 영역 Frame
frame_top= Frame(window)
frame_top.pack(fill='x', padx=10, pady=5)

#3. 파일경로를 직접 입력하거나 선택된 파일경로가 보여지는 Entry 위젯
entry= Entry(frame_top, width=60) #너비는 60글자 사이즈
entry.pack(side='left', padx=5)

#4. 파일선택 버튼
btn_file_chooser= Button(frame_top)
btn_file_chooser.pack(side='left', padx=5)



window.mainloop()

