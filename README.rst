INTRODUCTION
============

This project contains a set of scripts for SEO guys.
This fork is done to add some specific features.

HOW TO INSTALL
==============

you must have git, python with setuptools, firefox and java.

execute this command::

    git clone git://github.com/toutpt/gaselenium.git
    cd gaselenium
    python bootstrap.py
    bin/buildout
    java -jar selenium.jar

gaselenium.py script
====================

This script parse a sitemap and visit all url listed.

    bin/python gaselenium.py http://monsite.com/sitemap.xml

googletest script
=================

Test your website SEO using google. you can check if your website is in the first page agains keywords.
keywords file must be a txt file with one search by line.

for example::

    inextcom
    agence web nantes
    création site internet nantes
    formation magento

To execute it from inside this project, execute::

    bin/python googletest.py http://www.inextcom.fr /home/toutpt/tmp/inextcom.txt

bingtest script
===============

Same as googletest, but for bing. Thanks to `Thomas Simon <mailto:thomas.simon@inextcom.fr>`_ for this contribution.

baidutest script
================

Same as googletest, but for baidu.

