# -*- coding: utf-8 -*-
"""
/***************************************************************************
 mapIcons
                                 A QGIS plugin
 This plugin provides a wide range of map icons
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2025-03-25
        copyright            : (C) 2025 by Syracuse University
        email                : bdasari@syr.edu
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
    """Load mapIcons class from file mapIcons.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .map_icons import mapIcons
    return mapIcons(iface)
