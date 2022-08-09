import ui_chart
from PySide2.QtWidgets import *
from PySide2.QtCharts import *
from PySide2.QtGui import *
from PySide2.QtCore import *
import csv_read


def setup(chartviews, parent_frames, ui):
    font = QFont()
    font.setFamily("Arial")
    font.setPointSize(8)
    font.setBold(False)
    global chart_sex
    chart_sex = ui_chart.my_pie_chart(
        chartviews[0], parent_frames[0], ui)
    chart_sex.load_data(["Boys", "Girls"], csv_read.sex_ratio)
    chart_sex.chart.setTitle("Sex Ratio")
    chart_sex.chart.setFont(font)

    global chart_nationality
    chart_nationality = ui_chart.my_pie_chart(
        chartviews[1], parent_frames[1], ui)
    chart_nationality.load_data(csv_read.nation_name, csv_read.nation_ratio)
    chart_nationality.pie.setPieStartAngle(120)
    chart_nationality.pie.setPieEndAngle(480)
    chart_nationality.chart.setTitle("Nationality Distribution")
    chart_nationality.chart.setFont(font)

    global chart_birthplace
    chart_birthplace = ui_chart.my_pie_chart(
        chartviews[2], parent_frames[2], ui)
    chart_birthplace.load_data(csv_read.place_name, csv_read.place_ratio)
    chart_birthplace.pie.setPieStartAngle(120)
    chart_birthplace.pie.setPieEndAngle(480)
    chart_birthplace.chart.setTitle("Birthplace Distribution")
    chart_birthplace.chart.setFont(font)

    global chart_school_level
    chart_school_level = ui_chart.my_bar_chart(
        chartviews[3], parent_frames[3], ui)
    mmax=chart_school_level.load_data(
        csv_read.school_level_name, csv_read.school_level_num)
    chart_school_level.values.setRange(0, mmax)
    chart_school_level.values.setTickInterval(5)
    chart_school_level.values.setTitleText("Count")
    chart_school_level.chart.setTitle("School Level Distribution")
    chart_school_level.chart.setFont(font)

    global chart_academic_year
    chart_academic_year = ui_chart.my_bar_chart(
        chartviews[4], parent_frames[4], ui)
    mmax=chart_academic_year.load_data(
        csv_read.academic_name, csv_read.academic_num)
    chart_academic_year.values.setRange(0, mmax)
    chart_academic_year.values.setTickInterval(5)
    chart_academic_year.values.setTitleText("Count")
    chart_academic_year.chart.setTitle("Academic Year Distribution")
    chart_academic_year.chart.setFont(font)

    global chart_subject
    chart_subject = ui_chart.my_bar_chart(
        chartviews[5], parent_frames[5], ui)
    mmax=chart_subject.load_data(
        csv_read.subject_name, csv_read.subject_num)
    chart_subject.values.setRange(0, mmax)
    chart_subject.values.setTickInterval(5)
    chart_subject.values.setTitleText("Count")
    chart_subject.chart.setTitle("Subject Distribution")
    chart_subject.chart.setFont(font)

    global chart_semester
    chart_semester = ui_chart.my_bar_chart(
        chartviews[6], parent_frames[6], ui)
    mmax=chart_semester.load_data(
        csv_read.semester_name, csv_read.semester_num)
    chart_semester.values.setRange(0, mmax)
    chart_semester.values.setTickInterval(5)
    chart_semester.values.setTitleText("Count")
    chart_semester.chart.setTitle("Semester Distribution")
    chart_semester.chart.setFont(font)

    global chart_relation
    chart_relation = ui_chart.my_pie_chart(
        chartviews[7], parent_frames[7], ui)
    chart_relation.load_data(csv_read.relation_name, csv_read.relation_ratio)
    chart_relation.chart.setTitle("Relation Ratio")
    chart_relation.chart.setFont(font)

    global chart_raise_hands
    chart_raise_hands = ui_chart.my_bar_chart(
        chartviews[8], parent_frames[8], ui)
    chart_raise_hands.load_data2(
        csv_read.raise_hands_name, csv_read.raise_hands_num)
    chart_raise_hands.values.setRange(0, max(csv_read.raise_hands_num))
    chart_raise_hands.values.setTickCount(20)
    chart_raise_hands.values.setTitleText("Probability")
    chart_raise_hands.types.setTitleText("Raise Hands times")
    chart_raise_hands.chart.setTitle("Raise Hands Distribution")
    chart_raise_hands.chart.setFont(font)

    global chart_visit_resource
    chart_visit_resource = ui_chart.my_bar_chart(
        chartviews[9], parent_frames[9], ui)
    chart_visit_resource.load_data2(
        csv_read.visit_resource_name, csv_read.visit_resource_num)
    chart_visit_resource.values.setRange(0, max(csv_read.visit_resource_num))
    chart_visit_resource.values.setTickCount(20)
    chart_visit_resource.values.setTitleText("Probability")
    chart_visit_resource.types.setTitleText("Visit Resource times")
    chart_visit_resource.chart.setTitle("Visit Resource Distribution")
    chart_visit_resource.chart.setFont(font)

    global chart_discussion
    chart_discussion = ui_chart.my_bar_chart(
        chartviews[10], parent_frames[10], ui)
    chart_discussion.load_data2(
        csv_read.discussion_name, csv_read.discussion_num)
    chart_discussion.values.setRange(0, max(csv_read.discussion_num))
    chart_discussion.values.setTickCount(20)
    chart_discussion.values.setTitleText("Probability")
    chart_discussion.types.setTitleText("Discussion times")
    chart_discussion.chart.setTitle("Discussion Distribution")
    chart_discussion.chart.setFont(font)

    global chart_parent_answer
    chart_parent_answer = ui_chart.my_pie_chart(
        chartviews[11], parent_frames[11], ui)
    chart_parent_answer.load_data(
        csv_read.parent_answer_name, csv_read.parent_answer_ratio)
    chart_parent_answer.chart.setTitle("Parent Answer Survey Result")
    chart_parent_answer.chart.setFont(font)

    global chart_parent_satisfy
    chart_parent_satisfy = ui_chart.my_pie_chart(
        chartviews[12], parent_frames[12], ui)
    chart_parent_satisfy.load_data(
        csv_read.parent_satisfy_name, csv_read.parent_satisfy_ratio)
    chart_parent_satisfy.chart.setTitle("Parent Satisfactory Survey Result")
    chart_parent_satisfy.chart.setFont(font)

    global chart_announcement
    chart_announcement = ui_chart.my_bar_chart(
        chartviews[13], parent_frames[13], ui)
    chart_announcement.load_data2(
        csv_read.announcement_name, csv_read.announcement_num)
    chart_announcement.values.setRange(0, max(csv_read.announcement_num))
    chart_announcement.values.setTickCount(20)
    chart_announcement.values.setTitleText("Probability")
    chart_announcement.types.setTitleText("Announcement times")
    chart_announcement.chart.setTitle("Announcement Distribution")
    chart_announcement.chart.setFont(font)

    global chart_absent
    chart_absent = ui_chart.my_pie_chart(
        chartviews[14], parent_frames[14], ui)
    chart_absent.load_data(csv_read.absent_name, csv_read.absent_ratio)
    chart_absent.chart.setTitle("Absent Ratio")
    chart_absent.chart.setFont(font)

    global chart_class
    chart_class = ui_chart.my_bar_chart(
        chartviews[15], parent_frames[15], ui)
    mmax=chart_class.load_data(
        csv_read.class_name, csv_read.class_num)
    chart_class.values.setRange(0, mmax)
    chart_class.values.setTickInterval(5)
    chart_class.values.setTitleText("Count")
    chart_class.chart.setTitle("Class Division")
    chart_class.chart.setFont(font)
    


def finish_draw_all():
    chart_sex.finish_draw()
    chart_nationality.finish_draw()
    chart_birthplace.finish_draw()
    chart_school_level.finish_draw()
    chart_academic_year.finish_draw()
    chart_subject.finish_draw()
    chart_semester.finish_draw()
    chart_relation.finish_draw()
    chart_raise_hands.finish_draw()
    chart_visit_resource.finish_draw()
    chart_announcement.finish_draw()
    chart_discussion.finish_draw()
    chart_parent_answer.finish_draw()
    chart_parent_satisfy.finish_draw()
    chart_absent.finish_draw()
    chart_class.finish_draw()
