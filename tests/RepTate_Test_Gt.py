# RepTate: Rheology of Entangled Polymers: Toolkit for the Analysis of Theory and Experiments
# --------------------------------------------------------------------------------------------------------
#
# Authors:
#     Jorge Ramirez, jorge.ramirez@upm.es
#     Victor Boudara, victor.boudara@gmail.com
#
# Useful links:
#     http://blogs.upm.es/compsoftmatter/software/reptate/
#     https://github.com/jorge-ramirez-upm/RepTate
#     http://reptate.readthedocs.io
#
# --------------------------------------------------------------------------------------------------------
#
# Copyright (2017-2020): Jorge Ramirez, Victor Boudara, Universidad Politécnica de Madrid, University of Leeds
#
# This file is part of RepTate.
#
# RepTate is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# RepTate is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with RepTate.  If not, see <http://www.gnu.org/licenses/>.
#
# --------------------------------------------------------------------------------------------------------
"""Module Reptate

Main program that launches the GUI.

"""
import os
import sys
import getopt

sys.path.append(".")
from RepTate.gui.QApplicationManager import QApplicationManager

# from ApplicationManager import * #solved the issue with the matplot window not opening on Mac
from PyQt5.QtWidgets import QApplication
from time import time, sleep
from RepTate.core.CmdBase import CmdBase, CalcMode
import logging


def start_RepTate(argv):
    """
    Main RepTate application. 
    
    :param list argv: Command line parameters passed to Reptate
    """
    loglevel = logging.DEBUG
    GUI = True
    QApplication.setStyle("Fusion")  # comment that line for a native look
    # for a list of available styles: "from PyQt5.QtWidgets import QStyleFactory; print(QStyleFactory.keys())"

    app = QApplication(sys.argv)

    # FOR DEBUGGING PURPOSES: Set Single or MultiThread (default)
    CmdBase.calcmode = CalcMode.singlethread

    ex = QApplicationManager(loglevel=loglevel)
    ex.setStyleSheet("QTabBar::tab { color:black; height: 22px; }")

    ex.show()

    ########################################################
    # THE FOLLOWING LINES ARE FOR TESTING A PARTICULAR CASE
    # Open a particular application
    ex.handle_new_app("Gt")

    #####################
    # TEST MaxwellModesTime
    # Open a Dataset
    gt_dir = "data%sGt%s" % ((os.sep,) * 2)
    ex.applications["Gt1"].new_tables_from_files(
        [gt_dir + "C0224_NVT_450K_1atm.gt",]
    )
    # Open a theory
    ex.applications["Gt1"].datasets["Set1"].new_theory("Maxwell Modes")
    # Minimize the theory
    ex.applications["Gt1"].datasets["Set1"].handle_actionMinimize_Error()

    ex.applications["Gt1"].datasets["Set1"].new_theory("Rouse")
    # # Minimize the theory
    ex.applications["Gt1"].datasets["Set1"].handle_actionMinimize_Error()

    sys.exit(app.exec_())


if __name__ == "__main__":
    start_RepTate(sys.argv[1:])
