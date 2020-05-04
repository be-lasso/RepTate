======================================
Tutorial NLVE Application Command Line
======================================

.. toctree::
   :maxdepth: 2

Rolie-Poly shear flow
---------------------

#. Comment the following line for command line mode (with graphical windows)::
    
    console batch
    
#. First create LVE application to fit Maxwell Modes::
    
    new LVE
    new
    open data/DOW/Linear_Rheology_TTS\DOWLDPEL150R_160C.tts
    theory_new MaxwellModesFrequency
    nmodes=8
    fit
    up
    up
    up
    
#. Create NLVE Application::
    
    new NLVE
    
#. Create Dataset::

    new
    
#. Add files to the dataset (master curve tts files)::

    open data\DOW\Non-Linear_Rheology\Start-up_Shear\My_dow150-160-*
    
#. Plot the files using the default LVE Application view::

    plot
    
#. Create new theory::
    
    theory_new RoliePoly
    
#. Return to the main application manager::

    up
    up
    up
    
#. Copy the Maxwell modes previously calculated::

    copymodes LVE1.DataSet01.MaxwellModesFrequency01 NLVE2.DataSet01.RoliePoly01
    
#. Return to the RoliePoly Theory::
    
    switch NLVE2
    switch DataSet01
    theory_switch RoliePoly01
    
#. Calculate the theory to the data files (in this case, shift according to WLF)::

    calculate
    
#. Save theory predictions::

    save
    
#. Exit Reptate (the y answer is needed)::

    quit
