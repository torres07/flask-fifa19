# -*- coding: utf-8 -*-
# @Author: torres
# @Date:   2020-02-19 16:49:12
# @Last Modified by:   torres
# @Last Modified time: 2020-02-20 18:15:54

from flask import Flask
from flask import jsonify, make_response, abort, request
import numpy as np
import pandas as pd

import queries

app = Flask(__name__)

# Columns that we are interested
cols = ['Name', 'Age', 'Photo', 'Nationality', 'Flag', 'Overall', 'Potential', 'Club', 'Club Logo', 'Value', 'Wage', 'Release Clause', 'Position', 'Jersey Number']
data = pd.read_csv('data/data.csv', usecols=cols)
data = data.dropna()

@app.errorhandler(404)
def not_found(error):
	"""Function to return a JSON message for 404 error instead of html page
	
	Args:
	    error (int): Error code
	
	Returns:
	    flask.make_response: JSON message
	"""
	return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/api/player/<name>', methods=['GET'])
def get_players_by_name(name):
	"""List information of player(s) that starts with given name
	
	Args:
	    name (string): Player name
	
	Returns:
	    flask.jsonify: Information about player(s)
	"""
	players = queries.name(data, name)

	return jsonify(players)

@app.route('/api/player/<int:age>', methods=['GET'])
def get_players_above_age(age):
	"""List information of player(s) that are younger that an age
	
	Args:
	    age (int): Age
	
	Returns:
	    flask.jsonify: Information abouts player(s)
	"""
	players = queries.younger_than(data, age)

	return jsonify(players)

@app.route('/api/team/<name>', methods=['GET'])
def get_team_by_name(name):
	"""Lists team players informations
	
	Args:
	    name (string): Team name
	
	Returns:
	    flask.jsonify: Information about team players
	"""
	teams = queries.team_info(data, name)
	
	return jsonify(teams)

if __name__ == '__main__':
	app.run(debug=True)