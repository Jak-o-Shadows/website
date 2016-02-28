# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 14:50:02 2013

@author: Jak
"""

contents = """Installing Mezzenine on CentOS

Install:
	python
	python-devel
	libpng
	libpng-devel
	jpeg
	jpeg-devel
	freetype
	freetype-devel
	gcc
	
Create Virtualenv
	virtualenv verenv
Activate Virtualenv
	source verenv/bin/activate
Install Mezzanine using Pip
	pip install mezzanine
	
Troubleshooting:
	Oftentimes, you will get a huge error on installing mezzanine. If it is a gcc error, it is likely related to PIL, the python imaging library. Check you have installed everything
 """
title = "Installing Mezzenine on centOS -- Jak-o-Shadows Website"
filesNeeded = []
style = ""