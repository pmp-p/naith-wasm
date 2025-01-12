# -*- coding: utf-8 -*-
# Copyright Reinier de Blois
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import posixpath
from pandac.PandaModules import Vec3
from pandac.PandaModules import Vec4
from pandac.PandaModules import BitMask32
from pandac.PandaModules import TransparencyAttrib


class Sky:
    """This loads a skydome/box/whatever the user specified."""

    def __init__(self, manager, xml):
        # Set the background color first
        background = xml.find("background")
        if background != None:
            self.bgColour = Vec4(float(background.get("r")), float(background.get("g")), float(background.get("b")), 1)
        else:
            self.bgColour = None

        # Get the path to load skies from...
        basePath = manager.get("paths").getConfig().find("skies").get("path")

        self.model = None
        skydome = xml.find("skydome")
        if skydome != None:
            self.model = loader.loadModel(posixpath.join(basePath, "skydome"))
            self.model.setLightOff(1)
            self.model.setShaderOff(1)
            self.model.setCompass()
            self.model.setBin("background", 10)
            self.model.setDepthWrite(False)
            self.model.setDepthTest(False)
            self.model.setColor(1, 1, 1, 1)
            self.model.setTexture(loader.loadTexture(posixpath.join(basePath, skydome.get("filename"))))
            self.model.setTag("sun", "True")
            self.model.reparentTo(base.cam)
            self.model.hide()

    def start(self):
        if self.bgColour != None:
            base.setBackgroundColor(self.bgColour)

        if self.model != None:
            self.model.show()
            self.model.hide(BitMask32.bit(1))  # Hide from the reflection camera
            self.model.hide(BitMask32.bit(2))  # Hide from the volumetric lighting camera
            self.model.hide(BitMask32.bit(3))  # Hide from the shadow camera(s), if any

    def stop(self):
        if self.model != None:
            self.model.hide()
