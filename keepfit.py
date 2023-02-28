import sys
import sqlite3

from PyQt5 import uic, QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication, QSlider, QVBoxLayout, QInputDialog, QColorDialog

from datetime import datetime, timedelta

from keepfit_design import Login_design, MainPage_design, Anketa_design

import csv


if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


con = sqlite3.connect("users_info.db")

cur = con.cursor()

con_ui = sqlite3.connect("users_info.db")
cur_ui = con_ui.cursor()


class Login(QMainWindow, Login_design):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_back.hide()
        self.btn_login.hide()
        self.lb_reg.hide()
        self.lb_log.hide()
        self.lb_pass.hide()
        self.lb_email.hide()
        self.le_email.hide()
        self.le_pass.hide()
        self.btn_register.hide()

        self.pixmap = QPixmap('images/main_logo.png')
        self.image = QLabel(self)
        self.image.move(60, 180)
        self.image.resize(500, 145)
        self.image.setPixmap(self.pixmap)
        self.setWindowTitle('Добро пожаловать')

        self.btn_reg.clicked.connect(self.btn_register_pressed)
        self.btn_log.clicked.connect(self.btn_login_pressed)
        self.btn_back.clicked.connect(self.btn_back_pressed)
        self.btn_login.clicked.connect(self.login_in_acc)
        self.btn_register.clicked.connect(self.reg_new_acc)

    def btn_login_pressed(self):
        self.image.move(60, 70)
        self.motivation_speech.hide()
        self.btn_log.hide()
        self.btn_register.hide()
        self.btn_reg.hide()
        self.lb_reg.hide()
        self.lb_log.show()
        self.lb_email.show()
        self.lb_pass.show()
        self.le_email.show()
        self.le_pass.show()
        self.btn_login.show()
        self.btn_back.show()

        self.extra_label_pass.setText('')
        self.extra_label_email.setText('')
        self.extra_label_email.show()
        self.extra_label_pass.show()
        self.setWindowTitle('Вход')

    def btn_register_pressed(self):
        self.image.move(60, 70)
        self.motivation_speech.hide()
        self.btn_log.hide()
        self.btn_reg.hide()
        self.btn_login.hide()
        self.lb_log.hide()
        self.lb_reg.show()
        self.lb_email.show()
        self.lb_pass.show()
        self.le_email.show()
        self.le_pass.show()
        self.btn_register.show()
        self.btn_back.show()

        self.extra_label_pass.setText('')
        self.extra_label_email.setText('')
        self.extra_label_email.show()
        self.extra_label_pass.show()
        self.setWindowTitle('Регистрация')

    def btn_back_pressed(self):
        self.image.move(60, 180)
        self.motivation_speech.show()
        self.btn_back.hide()
        self.btn_login.hide()
        self.lb_reg.hide()
        self.lb_log.hide()
        self.lb_pass.hide()
        self.lb_email.hide()
        self.le_email.hide()
        self.le_pass.hide()
        self.btn_register.hide()
        self.extra_label_email.hide()
        self.extra_label_pass.hide()
        self.btn_log.show()
        self.btn_reg.show()
        self.setWindowTitle('Добро пожаловать')

    def check_password(self, password):
        if len(password) >= 8:
            if not password.isupper() and not password.islower() and not password.isdigit() and not password.isalpha():
                return True

    def check_email(self, email):
        if '@' in email:
            username, domen = map(str, email.split('@'))
            if username and domen and '.' in domen:
                return True

    def login_in_acc(self):
        if not self.le_email.text() and not self.le_pass.text():
            self.extra_label_email.setText('Введите e-mail')
            self.extra_label_pass.setText('Введите пароль')
        elif self.le_email.text() and not self.le_pass.text():
            self.extra_label_email.setText('')
            self.extra_label_pass.setText('Введите пароль')
        elif not self.le_email.text() and self.le_pass.text():
            self.extra_label_email.setText('Введите e-mail')
            self.extra_label_pass.setText('')
        else:
            self.extra_label_pass.setText('')
            self.extra_label_email.setText('')
            emails = cur.execute("""SELECT email
                                    FROM users
                                """).fetchall()
            if not self.check_email(self.le_email.text()):
                self.extra_label_email.setText('Введён некорректный e-mail')
            if (self.le_email.text(),) not in emails:
                self.extra_label_email.setText('Аккаунта с такой почтой не существует')
            else:
                ind_email = emails.index((self.le_email.text(),))
                passwords = cur.execute("""SELECT password
                                        FROM users
                                        """).fetchall()
                corr_password = passwords[ind_email]
                if corr_password[0] != self.le_pass.text():
                    self.extra_label_pass.setText('Неверный пароль')
                else:
                    self.extra_label_pass.setText('')
                    self.close()
                    self.ex = MainPage(self.le_email.text())
                    self.ex.show()

    def reg_new_acc(self):
        if not self.le_email.text() and not self.le_pass.text():
            self.extra_label_email.setText('Введите e-mail')
            self.extra_label_pass.setText('Введите пароль')
        elif self.le_email.text() and not self.le_pass.text():
            self.extra_label_email.setText('')
            self.extra_label_pass.setText('Введите пароль')
        elif not self.le_email.text() and self.le_pass.text():
            self.extra_label_pass.setText('')
            self.extra_label_email.setText('Введите e-mail')
        else:
            emails = cur.execute("""SELECT email
                                                FROM users
                                            """).fetchall()
            if not self.check_password(self.le_pass.text()) and not self.check_email(self.le_email.text()):
                self.extra_label_pass.setText('Пароль слишком простой')
                self.extra_label_email.setText('Введен некорректный e-mail')
            elif not self.check_email(self.le_email.text()):
                self.extra_label_pass.setText('')
                self.extra_label_email.setText('Введен некорректный e-mail')
            elif not self.check_password(self.le_pass.text()):
                self.extra_label_pass.setText('Пароль слишком простой')
                self.extra_label_email.setText('')
            else:
                if (self.le_email.text(),) in emails:
                    self.extra_label_email.setText('Аккаунт с такой почтой уже существует')
                else:
                    self.extra_label_pass.setText('')
                    self.extra_label_email.setText('')
                    email = self.le_email.text()
                    password = self.le_pass.text()
                    self.close()
                    self.ex = Anketa(email, password)
                    self.ex.show()


class MainPage(QMainWindow, MainPage_design):
    def __init__(self, email):
        super().__init__()
        self.setupUi(self)
        self.email = email


        self.pixmap_water = QPixmap('images/water.png')
        self.image_water.setPixmap(self.pixmap_water)

        self.pixmap_d = QPixmap('images/diet.png')
        self.image_d.setPixmap(self.pixmap_d)

        self.pixmap_work = QPixmap('images/workout.png')
        self.image_work.setPixmap(self.pixmap_work)

        self.pixmap_s = QPixmap('images/sleeping.png')
        self.image_s.setPixmap(self.pixmap_s)

        self.pixmap_u = QPixmap('images/user.png')
        self.image_u.setPixmap(self.pixmap_u)

        self.logotip = QPixmap('images/logo_in_app.png')
        self.label.setPixmap(self.logotip)

        self.pixmap_man = QPixmap('images/strong_man.png')
        self.image_strong_man.setPixmap(self.pixmap_man)

        self.setWindowTitle('Тренировки')

        self.metod_lbl.hide()
        self.count_lbl.hide()
        self.count_of_work.hide()
        self.sinerg_rb.hide()
        self.antog_rb.hide()
        self.btn_creating_pr.hide()
        self.day1.hide()
        self.day2.hide()
        self.day3.hide()
        self.day4.hide()
        self.day5.hide()
        self.day6.hide()
        self.day7.hide()
        self.endurance_img.hide()
        self.endurance_info.hide()
        self.btn_backtomainwork.hide()
        self.endurance_name.hide()
        self.workonendurance.hide()
        self.backfromendurance.hide()
        self.power_img.hide()
        self.power_info.hide()
        self.power_name.hide()
        self.workonpower.hide()
        self.backfrompower.hide()
        self.massa_img.hide()
        self.massa_info.hide()
        self.massa_name.hide()
        self.workonmassa.hide()
        self.backfrommassa.hide()
        self.activity.hide()
        self.activity_lbl.hide()
        self.activity_slider.hide()
        self.female_w.hide()
        self.image_bottle.hide()
        self.male_w.hide()
        self.recomendation_lbl.hide()
        self.result_water.hide()
        self.water_name.hide()
        self.water_info.hide()
        self.weight.hide()
        self.weight_slider.hide()
        self.weight_lbl.hide()
        self.image_calories.hide()
        self.diet_name.hide()
        self.weigth_for_diet.hide()
        self.weight_sb_for_diet.hide()
        self.kg_lbl.hide()
        self.height_sb_for_diet.hide()
        self.height_for_diet.hide()
        self.sm_lbl.hide()
        self.age_sb_for_diet.hide()
        self.age_for_diet.hide()
        self.year_lbl_2.hide()
        self.activity_for_diet.hide()
        self.count_activity_diet.hide()
        self.get_result_diet.hide()
        self.result_for_diet.hide()
        self.your_calories_is_lbl.hide()
        self.info_for_diet.hide()
        self.male_for_diet.hide()
        self.female_for_dieet.hide()
        self.gender_lbl.hide()
        self.sleeping_name.hide()
        self.need__wakeup_in.hide()
        self.razdelitel_for_time.hide()
        self.hours.hide()
        self.minute.hide()
        self.result_sleeping.hide()
        self.or_lbl.hide()
        self.when_wakeup_if.hide()
        self.result_now_sleeping.hide()
        self.time1.hide()
        self.time2.hide()
        self.time3.hide()
        self.time4.hide()
        self.time5.hide()
        self.time6.hide()
        self.go_bed_in.hide()
        self.image_sleeping.hide()
        self.profile_fon.hide()
        self.profile_logo.hide()
        self.name_surname.hide()
        self.fit_lvl.hide()
        self.settings_image.hide()
        self.btn_settings.hide()
        self.weight_user.hide()
        self.weight_user_lbl.hide()
        self.height_user.hide()
        self.height_user_lbl.hide()
        self.gender_user.hide()
        self.gender_user_lbl.hide()
        self.lvl_user.hide()
        self.lvl_user_lbl.hide()
        self.goal_user.hide()
        self.goal_user_lbl.hide()
        self.max_dips.hide()
        self.max_dips_lbl.hide()
        self.max_squats.hide()
        self.max_squats_lbl.hide()
        self.max_pullups.hide()
        self.max_pushups.hide()
        self.max_pullups_lbl.hide()
        self.max_pushups_lbl.hide()
        self.physic_data_lbl.hide()
        self.black_profile_settings.hide()
        self.white_profile_settings.hide()
        self.btn_backtoprofile.hide()
        self.your_profile_lbl.hide()
        self.us_name_settings.hide()
        self.user_name_settings_lbl.hide()
        self.email_settings.hide()
        self.email_settings_lbl.hide()
        self.city_settings.hide()
        self.city_settings_lbl.hide()
        self.country_settings.hide()
        self.country_settings_lbl.hide()
        self.name_settings.hide()
        self.name_settings_lbl.hide()
        self.surname_settings.hide()
        self.surname_settings_lbl.hide()
        self.btn_workoutprogram.clicked.connect(self.creating_workout_page)
        self.btn_creating_pr.clicked.connect(self.creating_program)
        self.btn_backtomainwork.clicked.connect(self.back_to_main_workout)
        self.btn_vynosliv.clicked.connect(self.endurance)
        self.backfromendurance.clicked.connect(self.back_from_endurance)
        self.btn_power.clicked.connect(self.power)
        self.backfrompower.clicked.connect(self.back_from_power)
        self.btn_massa.clicked.connect(self.massa)
        self.backfrommassa.clicked.connect(self.back_from_massa)
        self.btn_s.clicked.connect(self.show_workout_fon)
        self.btn_water.clicked.connect(self.water_page)
        self.btn_d.clicked.connect(self.diet_page)
        self.get_result_diet.clicked.connect(self.get_calories)
        self.btn_work.clicked.connect(self.sleeping_page)
        self.result_sleeping.clicked.connect(self.sleeping_result)
        self.result_now_sleeping.clicked.connect(self.sleeping_now_results)
        self.btn_u.clicked.connect(self.profile_page)
        self.gender_user.clicked.connect(self.input_physic_data)
        self.weight_user.clicked.connect(self.input_physic_data)
        self.height_user.clicked.connect(self.input_physic_data)
        self.lvl_user.clicked.connect(self.input_physic_data)
        self.goal_user.clicked.connect(self.input_physic_data)
        self.max_dips.clicked.connect(self.input_physic_data)
        self.max_pushups.clicked.connect(self.input_physic_data)
        self.max_squats.clicked.connect(self.input_physic_data)
        self.max_pullups.clicked.connect(self.input_physic_data)
        self.btn_settings.clicked.connect(self.profile_settings)
        self.btn_backtoprofile.clicked.connect(self.back_to_profile)
        self.btn_u.clicked.connect(self.run_profile)

    def run_profile(self):
        gender_lst = cur_ui.execute(f"""SELECT gender
                                    FROM user_data
                                    WHERE email in ('{self.email}')
                                """).fetchone()

        height_lst = cur_ui.execute(f"""SELECT height
                                            FROM user_data
                                            WHERE email in ('{self.email}')
                                        """).fetchone()
        weight_lst = cur_ui.execute(f"""SELECT weight
                                            FROM user_data
                                            WHERE email in ('{self.email}')
                                        """).fetchone()
        lvl_lst = cur_ui.execute(f"""SELECT fit_lvl
                                            FROM user_data
                                            WHERE email in ('{self.email}')
                                        """).fetchone()
        goal_lst = cur_ui.execute(f"""SELECT goal
                                            FROM user_data
                                            WHERE email in ('{self.email}')
                                        """).fetchone()
        push_lst = cur_ui.execute(f"""SELECT pushups
                                            FROM user_data
                                            WHERE email in ('{self.email}')
                                        """).fetchone()
        pull_lst = cur_ui.execute(f"""SELECT pullups
                                            FROM user_data
                                            WHERE email in ('{self.email}')
                                        """).fetchone()
        squats_lst = cur_ui.execute(f"""SELECT squats
                                            FROM user_data
                                            WHERE email in ('{self.email}')
                                        """).fetchone()
        dips_lst = cur_ui.execute(f"""SELECT dips
                                            FROM user_data
                                            WHERE email in ('{self.email}')
                                        """).fetchone()
        self.gender_user.setText(str(gender_lst[0]))
        self.weight_user.setText(str(weight_lst[0]))
        self.height_user.setText(str(height_lst[0]))
        self.lvl_user.setText(str(lvl_lst[0]))
        self.goal_user.setText(str(goal_lst[0]))
        self.max_pushups.setText(str(push_lst[0]))
        self.max_pullups.setText(str(pull_lst[0]))
        self.max_dips.setText(str(dips_lst[0]))
        self.max_squats.setText(str(squats_lst[0]))
        self.fit_lvl.setText(lvl_lst[0])

        with open('data.csv', encoding='utf8') as csvfile:
            reading = csvfile.readlines()
            for i in reading:
                i = i.split(';')
                if i[0] == self.email:
                    user_name = i[1]
                    fullname = i[2]
                    country = i[3]
                    city = i[4]
            self.us_name_settings.setText(user_name)
            self.name_settings.setText(fullname.split()[0])
            self.surname_settings.setText(fullname.split()[1])
            self.country_settings.setText(country)
            self.city_settings.setText(city)
            self.email_settings.setText(self.email)
            self.name_surname.setText(fullname)
            self.profile_logo.setText(fullname[0] + fullname.split()[1][0])

    def show_main_btns(self):
        self.btn_water.show()
        self.btn_d.show()
        self.btn_work.show()
        self.btn_u.show()
        self.btn_s.show()
        self.image_d.show()
        self.image_u.show()
        self.image_s.show()
        self.image_work.show()
        self.image_water.show()

    def hide_main_btns(self):
        self.btn_water.hide()
        self.btn_d.hide()
        self.btn_work.hide()
        self.btn_u.hide()
        self.btn_s.hide()
        self.image_d.hide()
        self.image_u.hide()
        self.image_s.hide()
        self.image_work.hide()
        self.image_water.hide()

    def show_workout_fon(self):
        self.setWindowTitle('Тренировки')
        self.image_strong_man.show()
        self.help_lbl.show()
        self.hide_sleeping_fon()
        self.hide_profile_fon()
        self.hide_diet_fon()
        self.hide_water_fon()
        self.btn_water.show()
        self.show_main_btns()
        self.btn_workoutprogram.show()
        self.label.show()
        self.btn_vynosliv.show()
        self.btn_massa.show()
        self.btn_power.show()
        self.worklearn_lbl.show()

    def hide_workout_fon(self):
        self.image_strong_man.hide()
        self.help_lbl.hide()
        self.label.hide()
        self.btn_power.hide()
        self.btn_vynosliv.hide()
        self.btn_massa.hide()
        self.btn_workoutprogram.hide()
        self.btn_water.hide()
        self.btn_d.hide()
        self.btn_work.hide()
        self.btn_u.hide()
        self.btn_s.hide()
        self.image_d.hide()
        self.image_u.hide()
        self.image_s.hide()
        self.image_work.hide()
        self.image_water.hide()
        self.worklearn_lbl.hide()
        self.image_sleeping.hide()

    def hide_water_fon(self):
        self.activity.hide()
        self.activity_lbl.hide()
        self.activity_slider.hide()
        self.female_w.hide()
        self.image_bottle.hide()
        self.male_w.hide()
        self.recomendation_lbl.hide()
        self.result_water.hide()
        self.water_name.hide()
        self.water_info.hide()
        self.weight.hide()
        self.weight_slider.hide()
        self.weight_lbl.hide()

    def hide_diet_fon(self):
        self.image_calories.hide()
        self.diet_name.hide()
        self.weigth_for_diet.hide()
        self.weight_sb_for_diet.hide()
        self.kg_lbl.hide()
        self.height_sb_for_diet.hide()
        self.height_for_diet.hide()
        self.sm_lbl.hide()
        self.age_sb_for_diet.hide()
        self.age_for_diet.hide()
        self.year_lbl_2.hide()
        self.activity_for_diet.hide()
        self.count_activity_diet.hide()
        self.get_result_diet.hide()
        self.result_for_diet.hide()
        self.your_calories_is_lbl.hide()
        self.info_for_diet.hide()
        self.male_for_diet.hide()
        self.female_for_dieet.hide()
        self.gender_lbl.hide()

    def hide_sleeping_fon(self):
        self.sleeping_name.hide()
        self.need__wakeup_in.hide()
        self.razdelitel_for_time.hide()
        self.hours.hide()
        self.minute.hide()
        self.result_sleeping.hide()
        self.or_lbl.hide()
        self.when_wakeup_if.hide()
        self.result_now_sleeping.hide()
        self.time1.hide()
        self.time2.hide()
        self.time3.hide()
        self.time4.hide()
        self.time5.hide()
        self.time6.hide()
        self.go_bed_in.hide()
        self.image_sleeping.hide()

    def hide_profile_fon(self):
        self.profile_fon.hide()
        self.profile_logo.hide()
        self.name_surname.hide()
        self.fit_lvl.hide()
        self.settings_image.hide()
        self.btn_settings.hide()
        self.weight_user.hide()
        self.weight_user_lbl.hide()
        self.height_user.hide()
        self.height_user_lbl.hide()
        self.gender_user.hide()
        self.gender_user_lbl.hide()
        self.lvl_user.hide()
        self.lvl_user_lbl.hide()
        self.goal_user.hide()
        self.physic_data_lbl.hide()
        self.goal_user_lbl.hide()
        self.max_dips.hide()
        self.max_dips_lbl.hide()
        self.max_squats.hide()
        self.max_squats_lbl.hide()
        self.max_pullups.hide()
        self.max_pushups.hide()
        self.max_pullups_lbl.hide()
        self.max_pushups_lbl.hide()

    def creating_workout_page(self):
        self.setWindowTitle('Программа тренировок')
        self.hide_workout_fon()

        self.metod_lbl.show()
        self.count_lbl.show()
        self.count_of_work.show()
        self.sinerg_rb.show()
        self.antog_rb.show()
        self.btn_creating_pr.show()
        self.day1.show()
        self.day2.show()
        self.day3.show()
        self.day4.show()
        self.day5.show()
        self.day6.show()
        self.day7.show()
        self.btn_backtomainwork.show()

    def back_to_main_workout(self):
        self.setWindowTitle('Добро пожаловать')
        self.show_workout_fon()

        self.metod_lbl.hide()
        self.count_lbl.hide()
        self.count_of_work.hide()
        self.sinerg_rb.hide()
        self.antog_rb.hide()
        self.btn_creating_pr.hide()
        self.day1.hide()
        self.day2.hide()
        self.day3.hide()
        self.day4.hide()
        self.day5.hide()
        self.day6.hide()
        self.day7.hide()
        self.btn_backtomainwork.hide()

    def back_from_endurance(self):
        self.setWindowTitle('Тренировки')
        self.endurance_info.hide()
        self.workonendurance.hide()
        self.endurance_name.hide()
        self.backfromendurance.hide()
        self.endurance_img.hide()

        self.show_workout_fon()

    def back_from_power(self):
        self.setWindowTitle('Тренировки')
        self.show_workout_fon()

        self.power_img.hide()
        self.power_info.hide()
        self.power_name.hide()
        self.workonpower.hide()
        self.backfrompower.hide()

    def back_from_massa(self):
        self.setWindowTitle('Тренировки')
        self.show_workout_fon()

        self.massa_img.hide()
        self.massa_info.hide()
        self.massa_name.hide()
        self.workonmassa.hide()
        self.backfrommassa.hide()

    def creating_program(self):
        if self.antog_rb.isChecked():
            self.antog_rb.setStyleSheet("color: rgb(255, 255, 255);")
            self.sinerg_rb.setStyleSheet("color: rgb(255, 255, 255);")
            if self.count_of_work.currentText() == '3 раза в неделю':
                self.day1.setText('День 1: Грудь, Спина, Пресс')
                self.day2.setText('День 2: Отдых')
                self.day3.setText('День 3: Бицепс, Трицепс, Плечи, Пресс')
                self.day4.setText('День 4: Отдых')
                self.day7.setText('День 5: Ноги, Пресс')
                self.day6.setText('День 6: Отдых')
                self.day5.setText('День 7: Отдых')
            else:
                self.day1.setText('День 1: Грудь, Спина, Пресс')
                self.day2.setText('День 2: Бицепс, Трицепс, Плечи')
                self.day3.setText('День 3: Ноги, Пресс')
                self.day4.setText('День 4: Отдых')
                self.day7.setText('День 5: Грудь, Спина, Пресс')
                self.day6.setText('День 6: Бицепс, Трицепс, Плечи')
                self.day5.setText('День 7: Ноги, Пресс')
        elif self.sinerg_rb.isChecked():
            self.antog_rb.setStyleSheet("color: rgb(255, 255, 255);")
            self.sinerg_rb.setStyleSheet("color: rgb(255, 255, 255);")
            if self.count_of_work.currentText() == '3 раза в неделю':
                self.day1.setText('День 1: Грудь, Трицепс, Пресс')
                self.day2.setText('День 2: Отдых')
                self.day3.setText('День 3: Бицепс, Спина, Пресс')
                self.day4.setText('День 4: Отдых')
                self.day7.setText('День 5: Ноги, Плечи, Пресс')
                self.day6.setText('День 6: Отдых')
                self.day5.setText('День 7: Отдых')
            else:
                self.day1.setText('День 1: Грудь, Трицепс, Пресс')
                self.day2.setText('День 2: Бицепс, Спина')
                self.day3.setText('День 3: Ноги, Плечи, Пресс')
                self.day4.setText('День 4: Отдых')
                self.day7.setText('День 5: Грудь, Трицепс, Пресс')
                self.day6.setText('День 6: Бицепс, Спина')
                self.day5.setText('День 7: Ноги, Плечи, Пресс')
        else:
            self.antog_rb.setStyleSheet("color: rgb(255, 50, 50);")
            self.sinerg_rb.setStyleSheet("color: rgb(255, 50, 50);")

    def endurance(self):
        self.setWindowTitle('Выносливость')
        self.pixmap_endurace = QPixmap('images/endurance.png')
        self.endurance_img.setPixmap(self.pixmap_endurace)
        self.hide_workout_fon()

        self.endurance_img.show()
        self.endurance_info.show()
        self.workonendurance.show()
        self.endurance_name.show()
        self.backfromendurance.show()

    def power(self):
        self.setWindowTitle('Сила')
        self.hide_workout_fon()

        self.pixmap_power = QPixmap('images/power.png')
        self.power_img.setPixmap(self.pixmap_power)

        self.power_img.show()
        self.power_info.show()
        self.power_name.show()
        self.workonpower.show()
        self.backfrompower.show()

    def massa(self):
        self.setWindowTitle('Масса')
        self.hide_workout_fon()
        self.pixmap_massa = QPixmap('images/muscle.png')
        self.massa_img.setPixmap(self.pixmap_massa)

        self.massa_img.show()
        self.massa_info.show()
        self.massa_name.show()
        self.workonmassa.show()
        self.backfrommassa.show()

    def water_page(self):
        self.setWindowTitle('Вода')
        self.pixmap_bottle = QPixmap('images/bottle_water.png')
        self.image_bottle.setPixmap(self.pixmap_bottle)
        self.hide_diet_fon()
        self.hide_profile_fon()
        self.hide_workout_fon()
        self.hide_sleeping_fon()
        self.show_main_btns()
        self.activity.show()
        self.activity_lbl.show()
        self.activity_slider.show()
        self.female_w.show()
        self.image_bottle.show()
        self.male_w.show()
        self.recomendation_lbl.show()
        self.result_water.show()
        self.water_name.show()
        self.water_info.show()
        self.weight.show()
        self.weight_slider.show()
        self.weight_lbl.show()

        self.male_w.setChecked(True)
        self.male_w.clicked.connect(self.female_male_clicked)
        self.female_w.clicked.connect(self.female_male_clicked)

        self.weight_slider.setMaximum(150)
        self.weight_slider.setMinimum(20)

        self.weight_slider.setTickInterval(5)
        self.weight_slider.setPageStep(5)
        self.weight_slider.valueChanged.connect(self.slider_moving)

        self.activity_slider.setMaximum(10)
        self.activity_slider.setMinimum(0)
        self.activity_slider.setPageStep(1)
        self.activity_slider.valueChanged.connect(self.slider_moving)

    def slider_moving(self):
        sender = self.sender()
        if sender == self.weight_slider:
            self.weight.setText(f'{self.weight_slider.value()} кг')
            if self.male_w.isChecked():
                formula = round((self.weight_slider.value() * 0.03 + self.activity_slider.value() * 0.5), 1)
                self.result_water.setText(f'{formula} литра в день')
            else:
                formula = round((self.weight_slider.value() * 0.0025 + self.activity_slider.value() * 0.4), 1)
                self.result_water.setText(f'{formula} литра в день')
        else:
            self.activity.setText(f'{self.activity_slider.value()} ч')
            if self.male_w.isChecked():
                formula = round((self.weight_slider.value() * 0.03 + self.activity_slider.value() * 0.5), 1)
                self.result_water.setText(f'{formula} литра в день')
            else:
                formula = round((self.weight_slider.value() * 0.0025 + self.activity_slider.value() * 0.4), 1)
                self.result_water.setText(f'{formula} литра в день')

    def female_male_clicked(self):
        sender = self.sender()
        if sender == self.male_w:
            formula = round((self.weight_slider.value() * 0.03 + self.activity_slider.value() * 0.5), 1)
            self.result_water.setText(f'{formula} литра в день')
        else:
            formula = round((self.weight_slider.value() * 0.025 + self.activity_slider.value() * 0.4), 1)
            self.result_water.setText(f'{formula} литра в день')

    def diet_page(self):
        self.setWindowTitle('Питание')
        self.pixmap_diet = QPixmap('images/calories.png')
        self.image_calories.setPixmap(self.pixmap_diet)
        self.hide_water_fon()
        self.hide_profile_fon()
        self.hide_sleeping_fon()
        self.hide_workout_fon()
        self.show_main_btns()
        self.image_calories.show()
        self.diet_name.show()
        self.weigth_for_diet.show()
        self.weight_sb_for_diet.show()
        self.kg_lbl.show()
        self.height_sb_for_diet.show()
        self.height_for_diet.show()
        self.sm_lbl.show()
        self.age_sb_for_diet.show()
        self.age_for_diet.show()
        self.year_lbl_2.show()
        self.activity_for_diet.show()
        self.count_activity_diet.show()
        self.get_result_diet.show()
        self.result_for_diet.show()
        self.your_calories_is_lbl.show()
        self.info_for_diet.show()
        self.male_for_diet.show()
        self.female_for_dieet.show()
        self.gender_lbl.show()

    def get_calories(self):
        gender = False
        if not self.male_for_diet.isChecked() and not self.female_for_dieet.isChecked():
            self.gender_lbl.setStyleSheet('color: rgb(255, 25, 25)')
            self.male_for_diet.setStyleSheet('color: rgb(255, 25, 25)')
            self.female_for_dieet.setStyleSheet('color: rgb(255, 25, 25)')
        else:
            self.gender_lbl.setStyleSheet('color: rgb(255, 255, 255)')
            self.male_for_diet.setStyleSheet('color: rgb(255, 255, 255)')
            self.female_for_dieet.setStyleSheet('color: rgb(255, 255, 255)')
            gender = True
        if gender:
            if self.activity_for_diet.currentText() == 'минимум/отсутствие физ. активности':
                k = 1.2
            elif self.activity_for_diet.currentText() == '1-3 раза в неделю':
                k = 1.3
            elif self.activity_for_diet.currentText() == '3-5 раз в неделю':
                k = 1.5
            elif self.activity_for_diet.currentText() == '6-7 раз в неделю':
                k = 1.7
            else:
                k = 1.8
            if self.male_for_diet.isChecked():
                self.result_for_diet.setText(str(round((66 + (13.7 * self.weight_sb_for_diet.value()) +
                                                        (5 * self.height_sb_for_diet.value()) -
                                                        (6.8 * self.age_sb_for_diet.value())) * k)) + ' ккал/день')
            else:
                self.result_for_diet.setText(str(round((665 + (9.6 * self.weight_sb_for_diet.value()) +
                                                        (1.8 * self.height_sb_for_diet.value()) -
                                                        (4.7 * self.age_sb_for_diet.value())) * k)) + ' ккал/день')

    def sleeping_page(self):
        self.setWindowTitle('Сон')
        self.pixmap_sleeping = QPixmap('images/sleep.png')
        self.image_sleeping.setPixmap(self.pixmap_sleeping)
        self.hide_diet_fon()
        self.hide_workout_fon()
        self.hide_profile_fon()
        self.hide_water_fon()
        self.show_main_btns()
        self.sleeping_name.show()
        self.need__wakeup_in.show()
        self.razdelitel_for_time.show()
        self.hours.show()
        self.minute.show()
        self.result_sleeping.show()
        self.or_lbl.show()
        self.when_wakeup_if.show()
        self.result_now_sleeping.show()
        self.time1.show()
        self.time2.show()
        self.time3.show()
        self.time4.show()
        self.time5.show()
        self.time6.show()
        self.go_bed_in.show()
        self.image_sleeping.show()

    def sleeping_result(self):
        self.go_bed_in.setText('Ложитесь в:')
        hour = self.hours.currentText()
        minute = self.minute.currentText()
        time = datetime.strptime(f'{hour}:{minute}', '%H:%M')
        self.time1.setText(str(time - timedelta(hours=9)).split()[1][:-3])
        self.time2.setText(str(time - timedelta(hours=7, minutes=30)).split()[1][:-3])
        self.time3.setText(str(time - timedelta(hours=6)).split()[1][:-3])
        self.time4.setText(str(time - timedelta(hours=4, minutes=30)).split()[1][:-3])
        self.time5.setText(str(time - timedelta(hours=3)).split()[1][:-3])
        self.time6.setText(str(time - timedelta(hours=1, minutes=30)).split()[1][:-3])

    def sleeping_now_results(self):
        self.go_bed_in.setText('Вставайте в:')
        time = datetime.now()
        self.time6.setText(str(time + timedelta(hours=9)).split()[1][:-10])
        self.time5.setText(str(time + timedelta(hours=7, minutes=30)).split()[1][:-10])
        self.time4.setText(str(time + timedelta(hours=6)).split()[1][:-10])
        self.time3.setText(str(time + timedelta(hours=4, minutes=30)).split()[1][:-10])
        self.time2.setText(str(time + timedelta(hours=3)).split()[1][:-10])
        self.time1.setText(str(time + timedelta(hours=1, minutes=30)).split()[1][:-10])

    def profile_page(self):
        self.setWindowTitle('Профиль')
        self.pixmap_settings = QPixmap('images/settings.png')
        self.settings_image.setPixmap(self.pixmap_settings)
        self.hide_diet_fon()
        # self.hide_water_fon()
        self.hide_workout_fon()
        self.hide_sleeping_fon()
        self.show_main_btns()
        self.profile_fon.show()
        self.profile_logo.show()
        self.name_surname.show()
        self.fit_lvl.show()
        self.physic_data_lbl.show()
        self.settings_image.show()
        self.btn_settings.show()
        self.weight_user.show()
        self.weight_user_lbl.show()
        self.height_user.show()
        self.height_user_lbl.show()
        self.gender_user.show()
        self.gender_user_lbl.show()
        self.lvl_user.show()
        self.lvl_user_lbl.show()
        self.goal_user.show()
        self.goal_user_lbl.show()
        self.max_dips.show()
        self.max_dips_lbl.show()
        self.max_squats.show()
        self.max_squats_lbl.show()
        self.max_pullups.show()
        self.max_pushups.show()
        self.max_pullups_lbl.show()
        self.max_pushups_lbl.show()

    def input_physic_data(self):
        sender = self.sender()
        if sender == self.gender_user:
            gender, ok_pressed = QInputDialog.getItem(
                self, "Пол", "",
                ("Мужской", "Женский"), 1, False)
            if ok_pressed:
                self.gender_user.setText(gender)
                cur_ui.execute(f"""UPDATE user_data
                                    SET gender = '{gender}'
                                    WHERE email in ('{self.email}')
                                """)
                con_ui.commit()
        elif sender == self.weight_user:
            weight, ok_pressed = QInputDialog.getInt(
                self, "Пол", "",
                25, 25, 250, 1)
            if ok_pressed:
                self.weight_user.setText(str(weight))
                cur_ui.execute(f"""UPDATE user_data
                                    SET weight = '{weight}'
                                    WHERE email in ('{self.email}')
                                """)
                con_ui.commit()
        elif sender == self.height_user:
            height, ok_pressed = QInputDialog.getInt(
                self, "Пол", "",
                75, 75, 220, 1)
            if ok_pressed:
                self.height_user.setText(str(height))
                cur_ui.execute(f"""UPDATE user_data
                                    SET weight = '{height}'
                                    WHERE email in ('{self.email}')
                                """)
                con_ui.commit()
        elif sender == self.lvl_user:
            lvl, ok_pressed = QInputDialog.getItem(
                self, "Пол", "",
                ("Начинающий", "Базовый", "Продвинутый"), 1, False)
            if ok_pressed:
                self.lvl_user.setText(lvl)
                self.fit_lvl.setText(lvl)
                cur_ui.execute(f"""UPDATE user_data
                                    SET fit_lvl = '{lvl}'
                                    WHERE email in ('{self.email}')
                                """)
                con_ui.commit()
        elif sender == self.goal_user:
            goal, ok_pressed = QInputDialog.getItem(
                self, "Пол", "",
                ("Набор массы", "Прокачка силы", "Сжигание жира"), 1, False)
            if ok_pressed:
                self.goal_user.setText(goal)
                cur_ui.execute(f"""UPDATE user_data
                                    SET goal = '{goal}'
                                    WHERE email in ('{self.email}')
                                """)
                con_ui.commit()
        elif sender == self.max_pushups:
            push, ok_pressed = QInputDialog.getInt(
                self, "Пол", "",
                0, 0, 999, 1)
            if ok_pressed:
                self.max_pushups.setText(str(push))
                cur_ui.execute(f"""UPDATE user_data
                                                SET pushups = '{push}'
                                                WHERE email in ('{self.email}')
                                            """)
        elif sender == self.max_pullups:
            pull, ok_pressed = QInputDialog.getInt(
                self, "Пол", "",
                0, 0, 999, 1)
            if ok_pressed:
                self.max_pullups.setText(str(pull))
                cur_ui.execute(f"""UPDATE user_data
                                                            SET pullups = '{pull}'
                                                            WHERE email in ('{self.email}')
                                                        """)
        elif sender == self.max_squats:
            squats, ok_pressed = QInputDialog.getInt(
                self, "Пол", "",
                0, 0, 999, 1)
            if ok_pressed:
                self.max_squats.setText(str(squats))
                cur_ui.execute(f"""UPDATE user_data
                                                            SET squats = '{squats}'
                                                            WHERE email in ('{self.email}')
                                                        """)
        elif sender == self.max_dips:
            dips, ok_pressed = QInputDialog.getInt(
                self, "Пол", "",
                0, 0, 999, 1)
            if ok_pressed:
                self.max_dips.setText(str(dips))
                cur_ui.execute(f"""UPDATE user_data
                                                            SET dips = '{dips}'
                                                            WHERE email in ('{self.email}')
                                                        """)



    def profile_settings(self):
        self.setWindowTitle('Настройки')
        self.profile_logo.setGeometry(QtCore.QRect(290, 30, 111, 111))
        self.hide_profile_fon()
        self.btn_u.hide()
        self.btn_water.hide()
        self.btn_work.hide()
        self.btn_s.hide()
        self.btn_d.hide()
        self.image_u.hide()
        self.image_d.hide()
        self.image_s.hide()
        self.image_water.hide()
        self.image_work.hide()
        self.black_profile_settings.show()
        self.white_profile_settings.show()
        self.btn_backtoprofile.show()
        self.your_profile_lbl.show()
        self.us_name_settings.show()
        self.user_name_settings_lbl.show()
        self.email_settings.show()
        self.email_settings_lbl.show()
        self.city_settings.show()
        self.city_settings_lbl.show()
        self.country_settings.show()
        self.country_settings_lbl.show()
        self.name_settings.show()
        self.name_settings_lbl.show()
        self.surname_settings.show()
        self.surname_settings_lbl.show()
        self.profile_logo.show()

    def back_to_profile(self):
        self.profile_logo.setGeometry(QtCore.QRect(50, 40, 111, 111))
        self.show_main_btns()
        self.black_profile_settings.hide()
        self.white_profile_settings.hide()
        self.btn_backtoprofile.hide()
        self.your_profile_lbl.hide()
        self.us_name_settings.hide()
        self.user_name_settings_lbl.hide()
        self.email_settings.hide()
        self.email_settings_lbl.hide()
        self.city_settings.hide()
        self.city_settings_lbl.hide()
        self.country_settings.hide()
        self.country_settings_lbl.hide()
        self.name_settings.hide()
        self.name_settings_lbl.hide()
        self.surname_settings.hide()
        self.surname_settings_lbl.hide()

        self.profile_fon.show()
        self.profile_logo.show()
        self.name_surname.show()
        self.fit_lvl.show()
        self.physic_data_lbl.show()
        self.settings_image.show()
        self.btn_settings.show()
        self.weight_user.show()
        self.weight_user_lbl.show()
        self.height_user.show()
        self.height_user_lbl.show()
        self.gender_user.show()
        self.gender_user_lbl.show()
        self.lvl_user.show()
        self.lvl_user_lbl.show()
        self.goal_user.show()
        self.goal_user_lbl.show()
        self.max_dips.show()
        self.max_dips_lbl.show()
        self.max_squats.show()
        self.max_squats_lbl.show()
        self.max_pullups.show()
        self.max_pushups.show()
        self.max_pullups_lbl.show()
        self.max_pushups_lbl.show()


class Anketa(QMainWindow, Anketa_design):
    def __init__(self, email, password):
        super().__init__()
        self.setupUi(self)
        self.email = str(email)
        self.password = str(password)
        self.setWindowTitle('Регистрация')
        self.info_user_lbl.hide()
        self.btn_ready.clicked.connect(self.btn_ready_pressed)

    def btn_ready_pressed(self):
        lvl = False
        goal = False
        gender = False
        u_name = False
        name = False
        country = False
        city = False
        if not self.beginner_anketa.isChecked() and not self.intermediate_anketa.isChecked() and \
                not self.advanced_anketa.isChecked():
            self.beginner_anketa.setStyleSheet('color: rgb(255, 50, 50);'
                                               'font: 75 14pt "Times New Roman";')
            self.intermediate_anketa.setStyleSheet('color: rgb(255, 50, 50);'
                                                   'font: 75 14pt "Times New Roman";')
            self.advanced_anketa.setStyleSheet('color: rgb(255, 50, 50);'
                                               'font: 75 14pt "Times New Roman";')
        else:
            self.beginner_anketa.setStyleSheet('color: rgb(255, 255, 255);'
                                               'font: 75 14pt "Times New Roman";')
            self.intermediate_anketa.setStyleSheet('color: rgb(255, 255, 255);'
                                                   'font: 75 14pt "Times New Roman";')
            self.advanced_anketa.setStyleSheet('color: rgb(255, 255, 255);'
                                               'font: 75 14pt "Times New Roman";')
            lvl = True
        if not self.massa_anketa.isChecked() and not self.strngth_anketa.isChecked() and \
                not self.fat_anketa.isChecked():
            self.massa_anketa.setStyleSheet('color: rgb(255, 50, 50);'
                                            'font: 75 14pt "Times New Roman";')
            self.strngth_anketa.setStyleSheet('color: rgb(255, 50, 50);'
                                              'font: 75 14pt "Times New Roman";')
            self.fat_anketa.setStyleSheet('color: rgb(255, 50, 50);'
                                          'font: 75 14pt "Times New Roman";')
        else:
            self.massa_anketa.setStyleSheet('color: rgb(255, 255, 255);'
                                            'font: 75 14pt "Times New Roman";')
            self.strngth_anketa.setStyleSheet('color: rgb(255, 255, 255);'
                                              'font: 75 14pt "Times New Roman";')
            self.fat_anketa.setStyleSheet('color: rgb(255, 255, 255);'
                                          'font: 75 14pt "Times New Roman";')
            goal = True
        if not self.male_anketa.isChecked() and not self.female_anketa.isChecked():
            self.male_anketa.setStyleSheet('color: rgb(255, 50, 50);'
                                           'font: 75 14pt "Times New Roman";')
            self.female_anketa.setStyleSheet('color: rgb(255, 50, 50);'
                                             'font: 75 14pt "Times New Roman";')
        else:
            self.male_anketa.setStyleSheet('color: rgb(255, 255, 255);'
                                           'font: 75 14pt "Times New Roman";')
            self.female_anketa.setStyleSheet('color: rgb(255, 255, 255);'
                                             'font: 75 14pt "Times New Roman";')
            gender = True
        if not self.user_name_ank.text():
            self.user_name_lbl_anketa.setStyleSheet("color: rgb(255, 50, 50);\n"
                                                    "background-color: rgba(255, 255, 255, 0);\n"
                                                    "font: 75 10pt \"Times New Roman\";")
        else:
            self.user_name_lbl_anketa.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                    "background-color: rgba(255, 255, 255, 0);\n"
                                                    "font: 75 10pt \"Times New Roman\";")
            u_name = True
        if not self.fullname_ank.text():
            self.fullname_lbl_anketa.setStyleSheet("color: rgb(255, 50, 50);\n"
                                                   "background-color: rgba(255, 255, 255, 0);\n"
                                                   "font: 75 10pt \"Times New Roman\";")
        else:
            self.fullname_lbl_anketa.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                   "background-color: rgba(255, 255, 255, 0);\n"
                                                   "font: 75 10pt \"Times New Roman\";")
            name = True
        if not self.country_ank.text():
            self.country_lbl_anketa.setStyleSheet("color: rgb(255, 50, 50);\n"
                                                  "background-color: rgba(255, 255, 255, 0);\n"
                                                  "font: 75 10pt \"Times New Roman\";")
        else:
            self.country_lbl_anketa.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                  "background-color: rgba(255, 255, 255, 0);\n"
                                                  "font: 75 10pt \"Times New Roman\";")
            country = True
        if not self.city_ank.text():
            self.city_lbl_anketa.setStyleSheet("color: rgb(255, 50, 50);\n"
                                               "background-color: rgba(255, 255, 255, 0);\n"
                                               "font: 75 10pt \"Times New Roman\";")
        else:
            self.city_lbl_anketa.setStyleSheet("color: rgb(255, 255, 255);\n"
                                               "background-color: rgba(255, 255, 255, 0);\n"
                                               "font: 75 10pt \"Times New Roman\";")
            city = True
        if goal and lvl and gender and city and country and name and u_name:
            if self.male_anketa.isChecked():
                gender = self.male_anketa.text()
            else:
                gender = self.female_anketa.text()
            if self.beginner_anketa.isChecked():
                lvl = self.beginner_anketa.text()
            elif self.intermediate_anketa.isChecked():
                lvl = self.intermediate_anketa.text()
            else:
                lvl = self.advanced_anketa.text()
            if self.massa_anketa.isChecked():
                goal = self.massa_anketa.text()
            elif self.strngth_anketa.isChecked():
                goal = self.strngth_anketa.text()
            else:
                goal = self.fat_anketa.text()
            check1 = True
            check2 = True
            with open('data.csv', encoding='utf8', mode='r') as csvfile:
                reading = csvfile.readlines()
                for i in reading:
                    i = i.split(';')[:-1]
                    if i[1] == self.user_name_ank.text():
                        self.info_user_lbl.show()
                        check1 = False
                        break
            if len(self.fullname_ank.text().split()) < 2:
                self.fullname_lbl_anketa.setStyleSheet("color: rgb(255, 50, 50);\n"
                                                       "background-color: rgba(255, 255, 255, 0);\n"
                                                       "font: 75 10pt \"Times New Roman\";")
                check2 = False
            else:
                self.fullname_lbl_anketa.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                       "background-color: rgba(255, 255, 255, 0);\n"
                                                       "font: 75 10pt \"Times New Roman\";")
                check2 = True
            if check1 and check2:
                with open('data.csv', encoding='utf8', mode='a') as csvfile:
                    writer = csv.writer(csvfile, delimiter=';', lineterminator='\n')
                    writer.writerow(
                        [self.email, str(self.user_name_ank.text()), str(self.fullname_ank.text()), str(self.country_ank.text()),
                         str(self.city_ank.text())])
                cur_ui.execute(f"""INSERT INTO user_data
                                                                   (email, gender, weight, height, fit_lvl, goal, pushups, pullups, squats, dips)
                                                                    VALUES
                                                                   ('{self.email}', '{gender}', '{self.weight_sp_anketa.value()}', '{self.height_sb_anketa.value()}', '{lvl}', '{goal}', '{self.push_anketa.value()}', '{self.pull_anketa.value()}', '{self.squats_anketa.value()}', '{self.dips_anketa.value()}')""")
                con_ui.commit()

                cur.execute(f"""INSERT INTO users
                                                          (email, password)
                                                          VALUES
                                                          ('{self.email}', '{str(self.password)}')""")
                con.commit()


                self.close()
                self.ex = MainPage(self.email)
                self.ex.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Login()
    ex.show()
    sys.exit(app.exec_())
