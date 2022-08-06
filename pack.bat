call conda activate pyside2
pyinstaller -F -w main.py ^
-p csv_read.py ^
-p files_rc.py ^
-p load_in.py ^
-p save_png.py ^
-p ui_chart.py ^
-p ui_page_1.py ^
-p ui_page_2.py ^
-p ui_sytle.py ^
--hidden-import csv_read ^
--hidden-import files_rc ^
--hidden-import load_in ^
--hidden-import save_png ^
--hidden-import ui_chart ^
--hidden-import ui_page_1 ^
--hidden-import ui_page_2 ^
--hidden-import ui_style
