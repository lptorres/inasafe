"""
InaSAFE Disaster risk assessment tool developed by AusAid and World Bank
- **Shake Event Test Cases.**

Contact : ole.moller.nielsen@gmail.com

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'tim@linfiniti.com'
__version__ = '0.5.0'
__date__ = '2/08/2012'
__copyright__ = ('Copyright 2012, Australia Indonesia Facility for '
                 'Disaster Reduction')

import os
import unittest
from utils import shakemapExtractDir
from shake_data import ShakeData
from shake_event import ShakeEvent


class TestShakeEvent(unittest.TestCase):
    def test_eventFilePath(self):
        """Test eventFilePath works"""
        myShakeId = '20120726022003'
        myExpectedPath = os.path.join(shakemapExtractDir(), 'event.xml')
        myShakeData = ShakeData(myShakeId)
        myShakeData.extract()
        myShakeEvent = ShakeEvent(myShakeId)
        myPath = myShakeEvent.eventFilePath()
        self.assertEquals(myExpectedPath, myPath)


if __name__ == '__main__':
    unittest.main()