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

sys.path.append(".")
from RepTate.core.CmdBase import CmdBase, CalcMode
from RepTate.gui.QApplicationManager import QApplicationManager

# from ApplicationManager import * #solved the issue with the matplot window not opening on Mac
from PyQt5.QtWidgets import QApplication
from time import time, sleep
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
    ex.handle_new_app("TTS")

    # Open a Dataset
    pi_dir = "data%sPI_LINEAR%sosc%s" % ((os.sep,) * 3)
    ex.applications["TTS1"].new_tables_from_files(
        [
            pi_dir + "PI223k-14c_-45C_FS2_PP10.osc",
            pi_dir + "PI223k-14c_-40C_FS_PP10.osc",
            pi_dir + "PI223k-14c_-30C_FS_PP10.osc",
            pi_dir + "PI223k-14_-10C_FS_PP10.osc",
            pi_dir + "PI223k-14c_-20C_FS_PP10.osc",
            pi_dir + "PI223k-14b_0C_FS4_PP10.osc",
            pi_dir + "PI223k-14_10C_FS_PP10.osc",
            pi_dir + "PI223k-14b_25C_FS3_PP10.osc",
            pi_dir + "PI223k-14_25C_FS3_PP10.osc",
            pi_dir + "PI223k-14c_30C_FS3_PP10.osc",
            pi_dir + "PI223k-14_40C_FS_PP10.osc",
            pi_dir + "PI223k-14_50C_FS_PP10.osc",
        ]
    )

    # Open a theory
    ex.applications["TTS1"].datasets["Set1"].new_theory("Automatic TTS Shift")
    # Minimize the theory
    ex.applications["TTS1"].datasets["Set1"].handle_actionMinimize_Error()
    # Open a theory
    ex.applications["TTS1"].datasets["Set1"].new_theory("WLF Shift")
    # Minimize the theory
    ex.applications["TTS1"].datasets["Set1"].handle_actionMinimize_Error()

    sys.exit(app.exec_())


if __name__ == "__main__":
    start_RepTate(sys.argv[1:])
