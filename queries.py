# -*- coding: utf-8 -*-
# @Author: torres
# @Date:   2020-02-20 13:50:13
# @Last Modified by:   torres
# @Last Modified time: 2020-02-20 18:03:48

def name(data, name):
	return [*data[data['Name'].str.startswith(name)].T.to_dict().values()]

def younger_than(data, age):
	return [*data[data['Age'] < age].T.to_dict().values()]

def team_info(data, name):
	return [*data[data['Club'] == name].T.to_dict().values()]