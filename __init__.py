# -*- coding: utf-8 -*-
"""
/***************************************************************************
 HarmonyQGIS
                                 A QGIS plugin
 Access the Harmony service broker to process and download Earth science data
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-04-05
        copyright            : (C) 2020 by James Norton
        email                : jamesnorton@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load HarmonyQGIS class from file HarmonyQGIS.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .harmony_qgis import HarmonyQGIS
    return HarmonyQGIS(iface)
