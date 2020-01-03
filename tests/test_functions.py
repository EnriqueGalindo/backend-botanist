#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import main
import datetime


class TestFunctions(unittest.TestCase):

    def setUp(self):
        self.start_date = (6 - datetime.datetime.day(datetime.datetime.now())) + datetime.datetime.now()
        self.weeks = 12
        
    def test_no_weekends(self):
        '''checks to make sure that no plants are being watered on a weekend'''
        schedule = main.create_plant_array(
            self.weeks, self.start_date
            )
        for plant in schedule:
            for date in sorted(plant['schedule']):
                self.assertNotEqual(date.weekday(), 5)
                self.assertNotEqual(date.weekday(), 6)

    def test_timedeltas(self):
        '''checks to make sure that the distance between waterings for any given plant
        is no more or less than one day from its desired watering interval'''
        schedule = watering_schedule.create_plant_array(
            self.weeks, self.start_date
            )
        for plant in schedule:
            date_list = plant['schedule']
            delta = datetime.timedelta(days=plant['water_after'])
            prev_day = date_list[0]
            for date in date_list[1:]:
                self.assertTrue(
                    date - prev_day >= delta - watering_schedule.one_day
                    )
                self.assertTrue(
                    date - prev_day <= delta + watering_schedule.one_day
                    )
                prev_day = date
