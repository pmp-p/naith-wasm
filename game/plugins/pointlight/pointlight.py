# Copyright Tom SF Haines, Reinier de Blois
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


from pandac.PandaModules import VBase4
from pandac.PandaModules import PointLight as PPointLight


class PointLight:
    """Creates a simple point light"""

    def __init__(self, manager, xml):
        self.light = PPointLight("plight")
        self.lightNode = render.attachNewNode(self.light)

        self.reload(manager, xml)

    def reload(self, manager, xml):
        color = xml.find("color")
        if color != None:
            self.light.setColor(VBase4(float(color.get("r")), float(color.get("g")), float(color.get("b")), 1.0))

        pos = xml.find("pos")
        if pos != None:
            self.lightNode.setPos(render, float(pos.get("x")), float(pos.get("y")), float(pos.get("z")))

    def start(self):
        render.setLight(self.lightNode)

    def stop(self):
        render.clearLight(self.lightNode)
