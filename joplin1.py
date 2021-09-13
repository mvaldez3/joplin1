#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Mon Sep 13 16:29:27 2021
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'joplin1'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expInfo['session'], expName)

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Volumes/shares/Cabi/exp/joplin/joplin1/joplin1.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[2240, 1260], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='white', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "welcome_initializing"
welcome_initializingClock = core.Clock()
#import important packages
import random

#set random seed for experiment
random_seed = int(expInfo['participant'])
random.seed(random_seed)

#create list of random numbers to randomize run order for each participant
train_run_order = random.sample(range(1,100), 8)
print(train_run_order)
test_run_order = random.sample(range(1,100), 2)
print(test_run_order)

#define stimulus sets and categories
stim_set1 = '/Volumes/shares/Cabi/stimuli/cartoon_animals/Set1/'
stim_set2 = '/Volumes/shares/Cabi/stimuli/cartoon_animals/Set2/'
category1 = {'categorya': 'Batmans', 'categoryb': 'Robins'}
category2 = {'categorya': 'Wallaces', 'categoryb': 'Gromets'}
if expInfo['session'] == '001':
    if (int(expInfo['participant'])%4) == 0:
        stimulus_set = stim_set1
        session_cat = category1
    if (int(expInfo['participant'])%4) == 1:
        stimulus_set = stim_set2
        session_cat = category1
    if (int(expInfo['participant'])%4) == 2:
        stimulus_set = stim_set1
        session_cat = category2
    if (int(expInfo['participant'])%4) == 3:
        stimulus_set = stim_set2
        session_cat = category2

if expInfo['session'] == '002':
    if (int(expInfo['participant']) %4) == 0:
        stimulus_set = stim_set2
        session_cat = category2
    if (int(expInfo['participant'])%4) == 1:
        stimulus_set = stim_set1
        session_cat = category2
    if (int(expInfo['participant'])%4) == 2:
        stimulus_set = stim_set2
        session_cat = category1
    if (int(expInfo['participant'])%4) == 3:
        stimulus_set = stim_set1
        session_cat = category1

# define the image size depending on where the image is coming from
if stimulus_set == stim_set2:
    img_size = [0.55, 0.55]
if stimulus_set == stim_set1:
    img_size = [0.4,0.6]
# import the script and use the randpro_select function to establish a random prototype for the rest of the experiment
import stim_build as sb
randpro = sb.randpro_select('/Volumes/shares/Cabi/exp/joplin/joplin1/stim_files/prototype.csv', random_seed)
logging.log(randpro)
if expInfo['session'] == '001':
    welc_text = u'Welcome to the experiment! \n\n You will first complete a training phase where you will be presented images of cartoon animals and asked to determine whether they belong to the %s group or the %s group.\n\n You will not know which group the animals belong to at first. However, you will be given feedback on your answer, which you can then use to help you group the animals.\n\n Press SPACE to continue with the instructions.' % (session_cat['categorya'], session_cat['categoryb'])
if expInfo['session'] == '002':
    welc_text = u'Welcome to the experiment!\n\n Similar to the last session, you will start by completing a training phase where you will group cartoon animals into two different groups. This time, you will be asked to determine if the animal belongs to the %s group or the %s group. Remember, you will not know which group the animal belongs to at first, but will be given feedback on your answers that you can then use to help you group the animals.\n\n Press SPACE to continue with the instructions.' % (session_cat['categorya'], session_cat['categoryb'])
welcome_text = visual.TextStim(win=win, name='welcome_text',
    text=welc_text,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
welcome_key = keyboard.Keyboard()

# Initialize components for Routine "train_instruct1"
train_instruct1Clock = core.Clock()
inst1_train_text = u'For each image, you will have 3 seconds to give your response before the computer automatically moves to the next screen.\n\n To select %s, press "f".\n To select %s, press "j".\n\n Press "f" or "j" to continue with the instructions.' % (session_cat['categorya'], session_cat['categoryb'])
train_inst1_text = visual.TextStim(win=win, name='train_inst1_text',
    text=inst1_train_text,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
train_inst1_key = keyboard.Keyboard()

# Initialize components for Routine "train_instruct2"
train_instruct2Clock = core.Clock()
train_inst2_text = visual.TextStim(win=win, name='train_inst2_text',
    text='You will complete 8 runs of the training phase. Between each run, you will be given the opportunity to take a break. You may take as long as you need before returning to the experiemnt. \n\nPress SPACE to continue. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
train_inst2_key = keyboard.Keyboard()

# Initialize components for Routine "train_begin"
train_beginClock = core.Clock()
# run the create_train_set to create the training set, recoded to match the prototype
#output will be /data/_training_stim
sb.create_train_set('/Volumes/shares/Cabi/exp/joplin/joplin1/stim_files/train_file.csv', randpro)
os.rename('/Volumes/shares/Cabi/exp/joplin/joplin1/data/_training_stim.csv', filename + '_training_stim.csv')
# this refers to the training file that will be needed to create the generalization sets
training_stimuli = filename + '_training_stim.csv'

train_begin_text = visual.TextStim(win=win, name='train_begin_text',
    text='Press SPACE to start the training phase. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
train_begin_key = keyboard.Keyboard()

# Initialize components for Routine "stimTrain"
stimTrainClock = core.Clock()
train_image = visual.ImageStim(
    win=win,
    name='train_image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0.1), size=img_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-1.0)
catA_train = visual.TextStim(win=win, name='catA_train',
    text=session_cat["categorya"],
    font='Open Sans',
    pos=(-0.4, -0.35), height=0.075, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
catB_train = visual.TextStim(win=win, name='catB_train',
    text=session_cat["categoryb"],
    font='Open Sans',
    pos=(0.4, -0.35), height=0.075, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
train_key = keyboard.Keyboard()

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
feedback_text = visual.TextStim(win=win, name='feedback_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
fix1000 = visual.ShapeStim(
    win=win, name='fix1000', vertices='cross',
    size=(0.15, 0.15),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "run_break"
run_breakClock = core.Clock()
run_break_text = visual.TextStim(win=win, name='run_break_text',
    text='You will now be given a short break before continuing the experiment. \n\nWhen you are ready to proceed, press SPACE.\n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
break_key = keyboard.Keyboard()

# Initialize components for Routine "train_end"
train_endClock = core.Clock()
train_end_text = visual.TextStim(win=win, name='train_end_text',
    text='This concludes the training phase. Please let the researcher know you have finished and they will instruct you on the next phase of the experiment. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "test_instruct1"
test_instruct1Clock = core.Clock()
inst1_test_text = u'You will now begin the testing phase. This phase is identical to the training phase except you will not be given feedback on your answers.\n\n To select %s, press "f".\n To select %s, press "j".\n\n Press "f" or "j" to continue with the instructions.' % (session_cat['categorya'], session_cat['categoryb'])
test_inst1_text = visual.TextStim(win=win, name='test_inst1_text',
    text=inst1_test_text,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
test_inst1_key = keyboard.Keyboard()

# Initialize components for Routine "test_instruct2"
test_instruct2Clock = core.Clock()
test_inst2_text = visual.TextStim(win=win, name='test_inst2_text',
    text='You will complete 2 runs of the testing phase. Between each run, you will be given the opportunity to take a break. You may take as long as you need before returning to the experiment.\n\nPress SPACE to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
test_inst2_key = keyboard.Keyboard()

# Initialize components for Routine "test_begin"
test_beginClock = core.Clock()
#define input variables
prototype_file = '/Volumes/shares/Cabi/exp/joplin/joplin1/stim_files/prototype.csv'
num_rows2add = 10
num_proto = 2
num_train_stim = 14

#run gen_build function to produce generalization set. Will output two .csv files named genfile1 and genfile2
sb.gen_build(training_stimuli, prototype_file, randpro, num_rows2add, num_proto, num_train_stim, random_seed)
os.rename('/Volumes/shares/Cabi/exp/joplin/joplin1/data/genfile1.csv', filename + 'genfile1.csv')
os.rename('/Volumes/shares/Cabi/exp/joplin/joplin1/data/genfile2.csv', filename + 'genfile2.csv')

test_begin_text = visual.TextStim(win=win, name='test_begin_text',
    text='Press SPACE to start the testing phase. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
test_begin_key = keyboard.Keyboard()

# Initialize components for Routine "stimTest"
stimTestClock = core.Clock()
test_image = visual.ImageStim(
    win=win,
    name='test_image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0.1), size=img_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-1.0)
catA_test = visual.TextStim(win=win, name='catA_test',
    text=session_cat["categorya"],
    font='Open Sans',
    pos=(-0.4, -0.35), height=0.075, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
catB_test = visual.TextStim(win=win, name='catB_test',
    text=session_cat["categoryb"],
    font='Open Sans',
    pos=(0.4, -0.35), height=0.075, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
test_key = keyboard.Keyboard()

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
fix1000 = visual.ShapeStim(
    win=win, name='fix1000', vertices='cross',
    size=(0.15, 0.15),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "run_break"
run_breakClock = core.Clock()
run_break_text = visual.TextStim(win=win, name='run_break_text',
    text='You will now be given a short break before continuing the experiment. \n\nWhen you are ready to proceed, press SPACE.\n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
break_key = keyboard.Keyboard()

# Initialize components for Routine "test_end"
test_endClock = core.Clock()
test_end_text = visual.TextStim(win=win, name='test_end_text',
    text='You have finished the testing phase.\n\nYou will now complete a short demographics questionaire.\n\nPress SPACE to continue',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
test_end_key = keyboard.Keyboard()

# Initialize components for Routine "demo_form_instruct1"
demo_form_instruct1Clock = core.Clock()
demo_instr1_text = visual.TextStim(win=win, name='demo_instr1_text',
    text='While filling out the questionaire, please use the computer mouse to select the answer that applies to you. Use the red slider on the right of the screen to scroll to view more questions. Please make sure you answer all of the questions.\n\nWhen you have completed all of the questions, press ENTER/RETURN to submit your response. \n\nPress ENTER/RETURN to continue to the demographics questionaire.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
demo_inst1_key = keyboard.Keyboard()

# Initialize components for Routine "demoForm"
demoFormClock = core.Clock()
win.allowStencil = True
form = visual.Form(win=win, name='form',
    items='demo_form.xlsx',
    textHeight=0.03,
    font='Open Sans',
    randomize=False,
    style='dark',
    fillColor=None, borderColor=None, itemColor='white', 
    responseColor='white', markerColor='red', colorSpace='rgb', 
    size=(1, 0.7),
    pos=(0, 0.1),
    itemPadding=0.05
)
form_key = keyboard.Keyboard()
form_inst = visual.TextStim(win=win, name='form_inst',
    text='Press ENTER/RETURN to submit your response',
    font='Open Sans',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "demo_inst2"
demo_inst2Clock = core.Clock()
demo_inst2_text = visual.TextStim(win=win, name='demo_inst2_text',
    text='For the following open-ended questions, type your response using the keyboard and press ENTER/RETURN when you are finished. \n\nPress ENTER/RETURN to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
demo_inst2_key = keyboard.Keyboard()

# Initialize components for Routine "demo_2"
demo_2Clock = core.Clock()
demo2_instr_text = visual.TextStim(win=win, name='demo2_instr_text',
    text='What is your gender?',
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
demo2_submit_text = visual.TextStim(win=win, name='demo2_submit_text',
    text='Press ENTER/RETURN to submit response.',
    font='Open Sans',
    pos=(0, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
gender = visual.TextStim(win=win, name='gender',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "demo_3"
demo_3Clock = core.Clock()
demo3_instr = visual.TextStim(win=win, name='demo3_instr',
    text='What is your age?',
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
demo3_submit_text = visual.TextStim(win=win, name='demo3_submit_text',
    text='Press ENTER/RETURN to submit response.',
    font='Open Sans',
    pos=(0, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
age = visual.TextStim(win=win, name='age',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "demo_4"
demo_4Clock = core.Clock()
demo4_text = visual.TextStim(win=win, name='demo4_text',
    text='Was English the first language that you learned?\n\n\nIf yes, press Y.\nIf no, press N.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
demo4_key = keyboard.Keyboard()

# Initialize components for Routine "demo_5"
demo_5Clock = core.Clock()
dem05_text = visual.TextStim(win=win, name='dem05_text',
    text='What age did you begin learning English? \n(enter 0 for native speaker)',
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
demo5_submit_text = visual.TextStim(win=win, name='demo5_submit_text',
    text='Press ENTER/RETURN to submit response.',
    font='Open Sans',
    pos=(0, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
language = visual.TextStim(win=win, name='language',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "exp_end"
exp_endClock = core.Clock()
end_text = visual.TextStim(win=win, name='end_text',
    text='This concludes the experiment. Please let the researcher know you are finished and they will give you a short debrief of the experiment.\n \nThank you again for your participation!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "welcome_initializing"-------
continueRoutine = True
# update component parameters for each repeat
welcome_key.keys = []
welcome_key.rt = []
_welcome_key_allKeys = []
# keep track of which components have finished
welcome_initializingComponents = [welcome_text, welcome_key]
for thisComponent in welcome_initializingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcome_initializingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcome_initializing"-------
while continueRoutine:
    # get current time
    t = welcome_initializingClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcome_initializingClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome_text* updates
    if welcome_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_text.frameNStart = frameN  # exact frame index
        welcome_text.tStart = t  # local t and not account for scr refresh
        welcome_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_text, 'tStartRefresh')  # time at next scr refresh
        welcome_text.setAutoDraw(True)
    
    # *welcome_key* updates
    waitOnFlip = False
    if welcome_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_key.frameNStart = frameN  # exact frame index
        welcome_key.tStart = t  # local t and not account for scr refresh
        welcome_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_key, 'tStartRefresh')  # time at next scr refresh
        welcome_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(welcome_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(welcome_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if welcome_key.status == STARTED and not waitOnFlip:
        theseKeys = welcome_key.getKeys(keyList=['space'], waitRelease=False)
        _welcome_key_allKeys.extend(theseKeys)
        if len(_welcome_key_allKeys):
            welcome_key.keys = _welcome_key_allKeys[-1].name  # just the last key pressed
            welcome_key.rt = _welcome_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcome_initializingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome_initializing"-------
for thisComponent in welcome_initializingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if welcome_key.keys in ['', [], None]:  # No response was made
    welcome_key.keys = None
thisExp.addData('welcome_key.keys',welcome_key.keys)
if welcome_key.keys != None:  # we had a response
    thisExp.addData('welcome_key.rt', welcome_key.rt)
thisExp.addData('welcome_key.started', welcome_key.tStartRefresh)
thisExp.addData('welcome_key.stopped', welcome_key.tStopRefresh)
thisExp.nextEntry()
# the Routine "welcome_initializing" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "train_instruct1"-------
continueRoutine = True
# update component parameters for each repeat
train_inst1_key.keys = []
train_inst1_key.rt = []
_train_inst1_key_allKeys = []
# keep track of which components have finished
train_instruct1Components = [train_inst1_text, train_inst1_key]
for thisComponent in train_instruct1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
train_instruct1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "train_instruct1"-------
while continueRoutine:
    # get current time
    t = train_instruct1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=train_instruct1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *train_inst1_text* updates
    if train_inst1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        train_inst1_text.frameNStart = frameN  # exact frame index
        train_inst1_text.tStart = t  # local t and not account for scr refresh
        train_inst1_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(train_inst1_text, 'tStartRefresh')  # time at next scr refresh
        train_inst1_text.setAutoDraw(True)
    
    # *train_inst1_key* updates
    waitOnFlip = False
    if train_inst1_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        train_inst1_key.frameNStart = frameN  # exact frame index
        train_inst1_key.tStart = t  # local t and not account for scr refresh
        train_inst1_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(train_inst1_key, 'tStartRefresh')  # time at next scr refresh
        train_inst1_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(train_inst1_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(train_inst1_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if train_inst1_key.status == STARTED and not waitOnFlip:
        theseKeys = train_inst1_key.getKeys(keyList=['f', 'j'], waitRelease=False)
        _train_inst1_key_allKeys.extend(theseKeys)
        if len(_train_inst1_key_allKeys):
            train_inst1_key.keys = _train_inst1_key_allKeys[-1].name  # just the last key pressed
            train_inst1_key.rt = _train_inst1_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in train_instruct1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "train_instruct1"-------
for thisComponent in train_instruct1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if train_inst1_key.keys in ['', [], None]:  # No response was made
    train_inst1_key.keys = None
thisExp.addData('train_inst1_key.keys',train_inst1_key.keys)
if train_inst1_key.keys != None:  # we had a response
    thisExp.addData('train_inst1_key.rt', train_inst1_key.rt)
thisExp.nextEntry()
# the Routine "train_instruct1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "train_instruct2"-------
continueRoutine = True
# update component parameters for each repeat
train_inst2_key.keys = []
train_inst2_key.rt = []
_train_inst2_key_allKeys = []
# keep track of which components have finished
train_instruct2Components = [train_inst2_text, train_inst2_key]
for thisComponent in train_instruct2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
train_instruct2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "train_instruct2"-------
while continueRoutine:
    # get current time
    t = train_instruct2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=train_instruct2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *train_inst2_text* updates
    if train_inst2_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        train_inst2_text.frameNStart = frameN  # exact frame index
        train_inst2_text.tStart = t  # local t and not account for scr refresh
        train_inst2_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(train_inst2_text, 'tStartRefresh')  # time at next scr refresh
        train_inst2_text.setAutoDraw(True)
    
    # *train_inst2_key* updates
    waitOnFlip = False
    if train_inst2_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        train_inst2_key.frameNStart = frameN  # exact frame index
        train_inst2_key.tStart = t  # local t and not account for scr refresh
        train_inst2_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(train_inst2_key, 'tStartRefresh')  # time at next scr refresh
        train_inst2_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(train_inst2_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(train_inst2_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if train_inst2_key.status == STARTED and not waitOnFlip:
        theseKeys = train_inst2_key.getKeys(keyList=['space'], waitRelease=False)
        _train_inst2_key_allKeys.extend(theseKeys)
        if len(_train_inst2_key_allKeys):
            train_inst2_key.keys = _train_inst2_key_allKeys[-1].name  # just the last key pressed
            train_inst2_key.rt = _train_inst2_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in train_instruct2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "train_instruct2"-------
for thisComponent in train_instruct2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if train_inst2_key.keys in ['', [], None]:  # No response was made
    train_inst2_key.keys = None
thisExp.addData('train_inst2_key.keys',train_inst2_key.keys)
if train_inst2_key.keys != None:  # we had a response
    thisExp.addData('train_inst2_key.rt', train_inst2_key.rt)
thisExp.nextEntry()
# the Routine "train_instruct2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "train_begin"-------
continueRoutine = True
# update component parameters for each repeat
# Take the training set and input into the cond_file_build function. This functino will add all the necessary components to the file, like the category and correct key response.
sb.train_cond_file(training_stimuli, random_seed)

#rename the file to train_conditions and use this file for the loop.
os.rename('/Volumes/shares/Cabi/exp/joplin/joplin1/data/cond_file.csv', filename + '_train_cond.csv')
train_begin_key.keys = []
train_begin_key.rt = []
_train_begin_key_allKeys = []
# keep track of which components have finished
train_beginComponents = [train_begin_text, train_begin_key]
for thisComponent in train_beginComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
train_beginClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "train_begin"-------
while continueRoutine:
    # get current time
    t = train_beginClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=train_beginClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *train_begin_text* updates
    if train_begin_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        train_begin_text.frameNStart = frameN  # exact frame index
        train_begin_text.tStart = t  # local t and not account for scr refresh
        train_begin_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(train_begin_text, 'tStartRefresh')  # time at next scr refresh
        train_begin_text.setAutoDraw(True)
    
    # *train_begin_key* updates
    waitOnFlip = False
    if train_begin_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        train_begin_key.frameNStart = frameN  # exact frame index
        train_begin_key.tStart = t  # local t and not account for scr refresh
        train_begin_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(train_begin_key, 'tStartRefresh')  # time at next scr refresh
        train_begin_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(train_begin_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(train_begin_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if train_begin_key.status == STARTED and not waitOnFlip:
        theseKeys = train_begin_key.getKeys(keyList=['space'], waitRelease=False)
        _train_begin_key_allKeys.extend(theseKeys)
        if len(_train_begin_key_allKeys):
            train_begin_key.keys = _train_begin_key_allKeys[-1].name  # just the last key pressed
            train_begin_key.rt = _train_begin_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in train_beginComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "train_begin"-------
for thisComponent in train_beginComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if train_begin_key.keys in ['', [], None]:  # No response was made
    train_begin_key.keys = None
thisExp.addData('train_begin_key.keys',train_begin_key.keys)
if train_begin_key.keys != None:  # we had a response
    thisExp.addData('train_begin_key.rt', train_begin_key.rt)
thisExp.nextEntry()
# the Routine "train_begin" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
train_runs = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stim_files/train_runs_cond.xlsx'),
    seed=None, name='train_runs')
thisExp.addLoop(train_runs)  # add the loop to the experiment
thisTrain_run = train_runs.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrain_run.rgb)
if thisTrain_run != None:
    for paramName in thisTrain_run:
        exec('{} = thisTrain_run[paramName]'.format(paramName))

for thisTrain_run in train_runs:
    currentLoop = train_runs
    # abbreviate parameter names if possible (e.g. rgb = thisTrain_run.rgb)
    if thisTrain_run != None:
        for paramName in thisTrain_run:
            exec('{} = thisTrain_run[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    train_trials = data.TrialHandler(nReps=3.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(filename + train_set),
        seed=(int(expInfo['session']) + train_run_order[train_runs.thisN]), name='train_trials')
    thisExp.addLoop(train_trials)  # add the loop to the experiment
    thisTrain_trial = train_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrain_trial.rgb)
    if thisTrain_trial != None:
        for paramName in thisTrain_trial:
            exec('{} = thisTrain_trial[paramName]'.format(paramName))
    
    for thisTrain_trial in train_trials:
        currentLoop = train_trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrain_trial.rgb)
        if thisTrain_trial != None:
            for paramName in thisTrain_trial:
                exec('{} = thisTrain_trial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "stimTrain"-------
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        # define the image path for the image component
        train_stim = (stimulus_set + str(stim_id.replace(' ', '')) + '.jpg')
        
        train_image.setImage(train_stim)
        train_key.keys = []
        train_key.rt = []
        _train_key_allKeys = []
        # keep track of which components have finished
        stimTrainComponents = [train_image, catA_train, catB_train, train_key]
        for thisComponent in stimTrainComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        stimTrainClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "stimTrain"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = stimTrainClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=stimTrainClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *train_image* updates
            if train_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                train_image.frameNStart = frameN  # exact frame index
                train_image.tStart = t  # local t and not account for scr refresh
                train_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(train_image, 'tStartRefresh')  # time at next scr refresh
                train_image.setAutoDraw(True)
            if train_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > train_image.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    train_image.tStop = t  # not accounting for scr refresh
                    train_image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(train_image, 'tStopRefresh')  # time at next scr refresh
                    train_image.setAutoDraw(False)
            
            # *catA_train* updates
            if catA_train.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                catA_train.frameNStart = frameN  # exact frame index
                catA_train.tStart = t  # local t and not account for scr refresh
                catA_train.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(catA_train, 'tStartRefresh')  # time at next scr refresh
                catA_train.setAutoDraw(True)
            if catA_train.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > catA_train.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    catA_train.tStop = t  # not accounting for scr refresh
                    catA_train.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(catA_train, 'tStopRefresh')  # time at next scr refresh
                    catA_train.setAutoDraw(False)
            
            # *catB_train* updates
            if catB_train.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                catB_train.frameNStart = frameN  # exact frame index
                catB_train.tStart = t  # local t and not account for scr refresh
                catB_train.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(catB_train, 'tStartRefresh')  # time at next scr refresh
                catB_train.setAutoDraw(True)
            if catB_train.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > catB_train.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    catB_train.tStop = t  # not accounting for scr refresh
                    catB_train.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(catB_train, 'tStopRefresh')  # time at next scr refresh
                    catB_train.setAutoDraw(False)
            
            # *train_key* updates
            waitOnFlip = False
            if train_key.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                train_key.frameNStart = frameN  # exact frame index
                train_key.tStart = t  # local t and not account for scr refresh
                train_key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(train_key, 'tStartRefresh')  # time at next scr refresh
                train_key.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(train_key.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(train_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if train_key.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > train_key.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    train_key.tStop = t  # not accounting for scr refresh
                    train_key.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(train_key, 'tStopRefresh')  # time at next scr refresh
                    train_key.status = FINISHED
            if train_key.status == STARTED and not waitOnFlip:
                theseKeys = train_key.getKeys(keyList=['f', 'j'], waitRelease=False)
                _train_key_allKeys.extend(theseKeys)
                if len(_train_key_allKeys):
                    train_key.keys = _train_key_allKeys[-1].name  # just the last key pressed
                    train_key.rt = _train_key_allKeys[-1].rt
                    # was this correct?
                    if (train_key.keys == str(correct_key)) or (train_key.keys == correct_key):
                        train_key.corr = 1
                    else:
                        train_key.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stimTrainComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "stimTrain"-------
        for thisComponent in stimTrainComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if train_key.keys in ['', [], None]:  # No response was made
            train_key.keys = None
            # was no response the correct answer?!
            if str(correct_key).lower() == 'none':
               train_key.corr = 1;  # correct non-response
            else:
               train_key.corr = 0;  # failed to respond (incorrectly)
        # store data for train_trials (TrialHandler)
        train_trials.addData('train_key.keys',train_key.keys)
        train_trials.addData('train_key.corr', train_key.corr)
        if train_key.keys != None:  # we had a response
            train_trials.addData('train_key.rt', train_key.rt)
        
        # ------Prepare to start Routine "feedback"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        #rename the category to input into the feedback loop
        if category == 'categoryA':
            category_name = session_cat['categorya']
        if category == 'categoryB':
            category_name = session_cat['categoryb']
        
        
        if not train_key.keys:
            feedback = 'Oops...you failed to respond within the alloted time.'
        elif train_key.corr == 1:
            feedback = 'Correct.\n\n The answer was ' + category_name +'.'
        else:
            feedback = 'Incorrect.\n\n The answer was ' + category_name +'.'
        feedback_text.setText(feedback)
        # keep track of which components have finished
        feedbackComponents = [feedback_text]
        for thisComponent in feedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "feedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = feedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedback_text* updates
            if feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_text.frameNStart = frameN  # exact frame index
                feedback_text.tStart = t  # local t and not account for scr refresh
                feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
                feedback_text.setAutoDraw(True)
            if feedback_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_text.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_text.tStop = t  # not accounting for scr refresh
                    feedback_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(feedback_text, 'tStopRefresh')  # time at next scr refresh
                    feedback_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "feedback"-------
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # ------Prepare to start Routine "ITI"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        ITIComponents = [fix1000]
        for thisComponent in ITIComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ITIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "ITI"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ITIClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ITIClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix1000* updates
            if fix1000.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix1000.frameNStart = frameN  # exact frame index
                fix1000.tStart = t  # local t and not account for scr refresh
                fix1000.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix1000, 'tStartRefresh')  # time at next scr refresh
                fix1000.setAutoDraw(True)
            if fix1000.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix1000.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fix1000.tStop = t  # not accounting for scr refresh
                    fix1000.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fix1000, 'tStopRefresh')  # time at next scr refresh
                    fix1000.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ITIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ITI"-------
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()
        
    # completed 3.0 repeats of 'train_trials'
    
    
    # ------Prepare to start Routine "run_break"-------
    continueRoutine = True
    # update component parameters for each repeat
    break_key.keys = []
    break_key.rt = []
    _break_key_allKeys = []
    # keep track of which components have finished
    run_breakComponents = [run_break_text, break_key]
    for thisComponent in run_breakComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    run_breakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "run_break"-------
    while continueRoutine:
        # get current time
        t = run_breakClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=run_breakClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *run_break_text* updates
        if run_break_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            run_break_text.frameNStart = frameN  # exact frame index
            run_break_text.tStart = t  # local t and not account for scr refresh
            run_break_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(run_break_text, 'tStartRefresh')  # time at next scr refresh
            run_break_text.setAutoDraw(True)
        
        # *break_key* updates
        waitOnFlip = False
        if break_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            break_key.frameNStart = frameN  # exact frame index
            break_key.tStart = t  # local t and not account for scr refresh
            break_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break_key, 'tStartRefresh')  # time at next scr refresh
            break_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(break_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(break_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if break_key.status == STARTED and not waitOnFlip:
            theseKeys = break_key.getKeys(keyList=['space'], waitRelease=False)
            _break_key_allKeys.extend(theseKeys)
            if len(_break_key_allKeys):
                break_key.keys = _break_key_allKeys[-1].name  # just the last key pressed
                break_key.rt = _break_key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in run_breakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "run_break"-------
    for thisComponent in run_breakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if break_key.keys in ['', [], None]:  # No response was made
        break_key.keys = None
    train_runs.addData('break_key.keys',break_key.keys)
    if break_key.keys != None:  # we had a response
        train_runs.addData('break_key.rt', break_key.rt)
    # the Routine "run_break" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'train_runs'


# ------Prepare to start Routine "train_end"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
train_endComponents = [train_end_text, key_resp]
for thisComponent in train_endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
train_endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "train_end"-------
while continueRoutine:
    # get current time
    t = train_endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=train_endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *train_end_text* updates
    if train_end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        train_end_text.frameNStart = frameN  # exact frame index
        train_end_text.tStart = t  # local t and not account for scr refresh
        train_end_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(train_end_text, 'tStartRefresh')  # time at next scr refresh
        train_end_text.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['q'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in train_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "train_end"-------
for thisComponent in train_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "train_end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "test_instruct1"-------
continueRoutine = True
# update component parameters for each repeat
test_inst1_key.keys = []
test_inst1_key.rt = []
_test_inst1_key_allKeys = []
# keep track of which components have finished
test_instruct1Components = [test_inst1_text, test_inst1_key]
for thisComponent in test_instruct1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
test_instruct1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "test_instruct1"-------
while continueRoutine:
    # get current time
    t = test_instruct1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=test_instruct1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *test_inst1_text* updates
    if test_inst1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        test_inst1_text.frameNStart = frameN  # exact frame index
        test_inst1_text.tStart = t  # local t and not account for scr refresh
        test_inst1_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test_inst1_text, 'tStartRefresh')  # time at next scr refresh
        test_inst1_text.setAutoDraw(True)
    
    # *test_inst1_key* updates
    waitOnFlip = False
    if test_inst1_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        test_inst1_key.frameNStart = frameN  # exact frame index
        test_inst1_key.tStart = t  # local t and not account for scr refresh
        test_inst1_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test_inst1_key, 'tStartRefresh')  # time at next scr refresh
        test_inst1_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(test_inst1_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(test_inst1_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if test_inst1_key.status == STARTED and not waitOnFlip:
        theseKeys = test_inst1_key.getKeys(keyList=['f', 'j'], waitRelease=False)
        _test_inst1_key_allKeys.extend(theseKeys)
        if len(_test_inst1_key_allKeys):
            test_inst1_key.keys = _test_inst1_key_allKeys[-1].name  # just the last key pressed
            test_inst1_key.rt = _test_inst1_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in test_instruct1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "test_instruct1"-------
for thisComponent in test_instruct1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if test_inst1_key.keys in ['', [], None]:  # No response was made
    test_inst1_key.keys = None
thisExp.addData('test_inst1_key.keys',test_inst1_key.keys)
if test_inst1_key.keys != None:  # we had a response
    thisExp.addData('test_inst1_key.rt', test_inst1_key.rt)
thisExp.nextEntry()
# the Routine "test_instruct1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "test_instruct2"-------
continueRoutine = True
# update component parameters for each repeat
test_inst2_key.keys = []
test_inst2_key.rt = []
_test_inst2_key_allKeys = []
# keep track of which components have finished
test_instruct2Components = [test_inst2_text, test_inst2_key]
for thisComponent in test_instruct2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
test_instruct2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "test_instruct2"-------
while continueRoutine:
    # get current time
    t = test_instruct2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=test_instruct2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *test_inst2_text* updates
    if test_inst2_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        test_inst2_text.frameNStart = frameN  # exact frame index
        test_inst2_text.tStart = t  # local t and not account for scr refresh
        test_inst2_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test_inst2_text, 'tStartRefresh')  # time at next scr refresh
        test_inst2_text.setAutoDraw(True)
    
    # *test_inst2_key* updates
    waitOnFlip = False
    if test_inst2_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        test_inst2_key.frameNStart = frameN  # exact frame index
        test_inst2_key.tStart = t  # local t and not account for scr refresh
        test_inst2_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test_inst2_key, 'tStartRefresh')  # time at next scr refresh
        test_inst2_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(test_inst2_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(test_inst2_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if test_inst2_key.status == STARTED and not waitOnFlip:
        theseKeys = test_inst2_key.getKeys(keyList=['space'], waitRelease=False)
        _test_inst2_key_allKeys.extend(theseKeys)
        if len(_test_inst2_key_allKeys):
            test_inst2_key.keys = _test_inst2_key_allKeys[-1].name  # just the last key pressed
            test_inst2_key.rt = _test_inst2_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in test_instruct2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "test_instruct2"-------
for thisComponent in test_instruct2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if test_inst2_key.keys in ['', [], None]:  # No response was made
    test_inst2_key.keys = None
thisExp.addData('test_inst2_key.keys',test_inst2_key.keys)
if test_inst2_key.keys != None:  # we had a response
    thisExp.addData('test_inst2_key.rt', test_inst2_key.rt)
thisExp.nextEntry()
# the Routine "test_instruct2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "test_begin"-------
continueRoutine = True
# update component parameters for each repeat
test_begin_key.keys = []
test_begin_key.rt = []
_test_begin_key_allKeys = []
# keep track of which components have finished
test_beginComponents = [test_begin_text, test_begin_key]
for thisComponent in test_beginComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
test_beginClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "test_begin"-------
while continueRoutine:
    # get current time
    t = test_beginClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=test_beginClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *test_begin_text* updates
    if test_begin_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        test_begin_text.frameNStart = frameN  # exact frame index
        test_begin_text.tStart = t  # local t and not account for scr refresh
        test_begin_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test_begin_text, 'tStartRefresh')  # time at next scr refresh
        test_begin_text.setAutoDraw(True)
    
    # *test_begin_key* updates
    waitOnFlip = False
    if test_begin_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        test_begin_key.frameNStart = frameN  # exact frame index
        test_begin_key.tStart = t  # local t and not account for scr refresh
        test_begin_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test_begin_key, 'tStartRefresh')  # time at next scr refresh
        test_begin_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(test_begin_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(test_begin_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if test_begin_key.status == STARTED and not waitOnFlip:
        theseKeys = test_begin_key.getKeys(keyList=['space'], waitRelease=False)
        _test_begin_key_allKeys.extend(theseKeys)
        if len(_test_begin_key_allKeys):
            test_begin_key.keys = _test_begin_key_allKeys[-1].name  # just the last key pressed
            test_begin_key.rt = _test_begin_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in test_beginComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "test_begin"-------
for thisComponent in test_beginComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if test_begin_key.keys in ['', [], None]:  # No response was made
    test_begin_key.keys = None
thisExp.addData('test_begin_key.keys',test_begin_key.keys)
if test_begin_key.keys != None:  # we had a response
    thisExp.addData('test_begin_key.rt', test_begin_key.rt)
thisExp.nextEntry()
# the Routine "test_begin" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
test_runs = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stim_files/test_runs_cond.xlsx'),
    seed=None, name='test_runs')
thisExp.addLoop(test_runs)  # add the loop to the experiment
thisTest_run = test_runs.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTest_run.rgb)
if thisTest_run != None:
    for paramName in thisTest_run:
        exec('{} = thisTest_run[paramName]'.format(paramName))

for thisTest_run in test_runs:
    currentLoop = test_runs
    # abbreviate parameter names if possible (e.g. rgb = thisTest_run.rgb)
    if thisTest_run != None:
        for paramName in thisTest_run:
            exec('{} = thisTest_run[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    test_trials = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(filename + gen_file),
        seed=(int(expInfo['session']) + test_run_order[test_runs.thisN]), name='test_trials')
    thisExp.addLoop(test_trials)  # add the loop to the experiment
    thisTest_trial = test_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTest_trial.rgb)
    if thisTest_trial != None:
        for paramName in thisTest_trial:
            exec('{} = thisTest_trial[paramName]'.format(paramName))
    
    for thisTest_trial in test_trials:
        currentLoop = test_trials
        # abbreviate parameter names if possible (e.g. rgb = thisTest_trial.rgb)
        if thisTest_trial != None:
            for paramName in thisTest_trial:
                exec('{} = thisTest_trial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "stimTest"-------
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        test_stim = (stimulus_set + str(stim_id.replace(' ', '')) + '.jpg')
        test_image.setImage(test_stim)
        test_key.keys = []
        test_key.rt = []
        _test_key_allKeys = []
        # keep track of which components have finished
        stimTestComponents = [test_image, catA_test, catB_test, test_key]
        for thisComponent in stimTestComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        stimTestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "stimTest"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = stimTestClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=stimTestClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *test_image* updates
            if test_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                test_image.frameNStart = frameN  # exact frame index
                test_image.tStart = t  # local t and not account for scr refresh
                test_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(test_image, 'tStartRefresh')  # time at next scr refresh
                test_image.setAutoDraw(True)
            if test_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > test_image.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    test_image.tStop = t  # not accounting for scr refresh
                    test_image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(test_image, 'tStopRefresh')  # time at next scr refresh
                    test_image.setAutoDraw(False)
            
            # *catA_test* updates
            if catA_test.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                catA_test.frameNStart = frameN  # exact frame index
                catA_test.tStart = t  # local t and not account for scr refresh
                catA_test.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(catA_test, 'tStartRefresh')  # time at next scr refresh
                catA_test.setAutoDraw(True)
            if catA_test.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > catA_test.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    catA_test.tStop = t  # not accounting for scr refresh
                    catA_test.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(catA_test, 'tStopRefresh')  # time at next scr refresh
                    catA_test.setAutoDraw(False)
            
            # *catB_test* updates
            if catB_test.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                catB_test.frameNStart = frameN  # exact frame index
                catB_test.tStart = t  # local t and not account for scr refresh
                catB_test.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(catB_test, 'tStartRefresh')  # time at next scr refresh
                catB_test.setAutoDraw(True)
            if catB_test.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > catB_test.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    catB_test.tStop = t  # not accounting for scr refresh
                    catB_test.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(catB_test, 'tStopRefresh')  # time at next scr refresh
                    catB_test.setAutoDraw(False)
            
            # *test_key* updates
            waitOnFlip = False
            if test_key.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                test_key.frameNStart = frameN  # exact frame index
                test_key.tStart = t  # local t and not account for scr refresh
                test_key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(test_key, 'tStartRefresh')  # time at next scr refresh
                test_key.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(test_key.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(test_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if test_key.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > test_key.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    test_key.tStop = t  # not accounting for scr refresh
                    test_key.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(test_key, 'tStopRefresh')  # time at next scr refresh
                    test_key.status = FINISHED
            if test_key.status == STARTED and not waitOnFlip:
                theseKeys = test_key.getKeys(keyList=['f', 'j'], waitRelease=False)
                _test_key_allKeys.extend(theseKeys)
                if len(_test_key_allKeys):
                    test_key.keys = _test_key_allKeys[-1].name  # just the last key pressed
                    test_key.rt = _test_key_allKeys[-1].rt
                    # was this correct?
                    if (test_key.keys == str(correct_key)) or (test_key.keys == correct_key):
                        test_key.corr = 1
                    else:
                        test_key.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stimTestComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "stimTest"-------
        for thisComponent in stimTestComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if test_key.keys in ['', [], None]:  # No response was made
            test_key.keys = None
            # was no response the correct answer?!
            if str(correct_key).lower() == 'none':
               test_key.corr = 1;  # correct non-response
            else:
               test_key.corr = 0;  # failed to respond (incorrectly)
        # store data for test_trials (TrialHandler)
        test_trials.addData('test_key.keys',test_key.keys)
        test_trials.addData('test_key.corr', test_key.corr)
        if test_key.keys != None:  # we had a response
            test_trials.addData('test_key.rt', test_key.rt)
        
        # ------Prepare to start Routine "ITI"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        ITIComponents = [fix1000]
        for thisComponent in ITIComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ITIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "ITI"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ITIClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ITIClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix1000* updates
            if fix1000.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix1000.frameNStart = frameN  # exact frame index
                fix1000.tStart = t  # local t and not account for scr refresh
                fix1000.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix1000, 'tStartRefresh')  # time at next scr refresh
                fix1000.setAutoDraw(True)
            if fix1000.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix1000.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fix1000.tStop = t  # not accounting for scr refresh
                    fix1000.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fix1000, 'tStopRefresh')  # time at next scr refresh
                    fix1000.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ITIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ITI"-------
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'test_trials'
    
    
    # ------Prepare to start Routine "run_break"-------
    continueRoutine = True
    # update component parameters for each repeat
    break_key.keys = []
    break_key.rt = []
    _break_key_allKeys = []
    # keep track of which components have finished
    run_breakComponents = [run_break_text, break_key]
    for thisComponent in run_breakComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    run_breakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "run_break"-------
    while continueRoutine:
        # get current time
        t = run_breakClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=run_breakClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *run_break_text* updates
        if run_break_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            run_break_text.frameNStart = frameN  # exact frame index
            run_break_text.tStart = t  # local t and not account for scr refresh
            run_break_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(run_break_text, 'tStartRefresh')  # time at next scr refresh
            run_break_text.setAutoDraw(True)
        
        # *break_key* updates
        waitOnFlip = False
        if break_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            break_key.frameNStart = frameN  # exact frame index
            break_key.tStart = t  # local t and not account for scr refresh
            break_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break_key, 'tStartRefresh')  # time at next scr refresh
            break_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(break_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(break_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if break_key.status == STARTED and not waitOnFlip:
            theseKeys = break_key.getKeys(keyList=['space'], waitRelease=False)
            _break_key_allKeys.extend(theseKeys)
            if len(_break_key_allKeys):
                break_key.keys = _break_key_allKeys[-1].name  # just the last key pressed
                break_key.rt = _break_key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in run_breakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "run_break"-------
    for thisComponent in run_breakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if break_key.keys in ['', [], None]:  # No response was made
        break_key.keys = None
    test_runs.addData('break_key.keys',break_key.keys)
    if break_key.keys != None:  # we had a response
        test_runs.addData('break_key.rt', break_key.rt)
    # the Routine "run_break" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'test_runs'


# ------Prepare to start Routine "test_end"-------
continueRoutine = True
# update component parameters for each repeat
if expInfo['session'] == '001':
    continueRoutine = False
test_end_key.keys = []
test_end_key.rt = []
_test_end_key_allKeys = []
# keep track of which components have finished
test_endComponents = [test_end_text, test_end_key]
for thisComponent in test_endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
test_endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "test_end"-------
while continueRoutine:
    # get current time
    t = test_endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=test_endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *test_end_text* updates
    if test_end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        test_end_text.frameNStart = frameN  # exact frame index
        test_end_text.tStart = t  # local t and not account for scr refresh
        test_end_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test_end_text, 'tStartRefresh')  # time at next scr refresh
        test_end_text.setAutoDraw(True)
    
    # *test_end_key* updates
    waitOnFlip = False
    if test_end_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        test_end_key.frameNStart = frameN  # exact frame index
        test_end_key.tStart = t  # local t and not account for scr refresh
        test_end_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test_end_key, 'tStartRefresh')  # time at next scr refresh
        test_end_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(test_end_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(test_end_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if test_end_key.status == STARTED and not waitOnFlip:
        theseKeys = test_end_key.getKeys(keyList=['space'], waitRelease=False)
        _test_end_key_allKeys.extend(theseKeys)
        if len(_test_end_key_allKeys):
            test_end_key.keys = _test_end_key_allKeys[-1].name  # just the last key pressed
            test_end_key.rt = _test_end_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in test_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "test_end"-------
for thisComponent in test_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if test_end_key.keys in ['', [], None]:  # No response was made
    test_end_key.keys = None
thisExp.addData('test_end_key.keys',test_end_key.keys)
if test_end_key.keys != None:  # we had a response
    thisExp.addData('test_end_key.rt', test_end_key.rt)
thisExp.nextEntry()
# the Routine "test_end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "demo_form_instruct1"-------
continueRoutine = True
# update component parameters for each repeat
if expInfo['session'] == '001':
    continueRoutine = False
demo_inst1_key.keys = []
demo_inst1_key.rt = []
_demo_inst1_key_allKeys = []
# keep track of which components have finished
demo_form_instruct1Components = [demo_instr1_text, demo_inst1_key]
for thisComponent in demo_form_instruct1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
demo_form_instruct1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "demo_form_instruct1"-------
while continueRoutine:
    # get current time
    t = demo_form_instruct1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=demo_form_instruct1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *demo_instr1_text* updates
    if demo_instr1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demo_instr1_text.frameNStart = frameN  # exact frame index
        demo_instr1_text.tStart = t  # local t and not account for scr refresh
        demo_instr1_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demo_instr1_text, 'tStartRefresh')  # time at next scr refresh
        demo_instr1_text.setAutoDraw(True)
    
    # *demo_inst1_key* updates
    waitOnFlip = False
    if demo_inst1_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demo_inst1_key.frameNStart = frameN  # exact frame index
        demo_inst1_key.tStart = t  # local t and not account for scr refresh
        demo_inst1_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demo_inst1_key, 'tStartRefresh')  # time at next scr refresh
        demo_inst1_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(demo_inst1_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(demo_inst1_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if demo_inst1_key.status == STARTED and not waitOnFlip:
        theseKeys = demo_inst1_key.getKeys(keyList=['return'], waitRelease=False)
        _demo_inst1_key_allKeys.extend(theseKeys)
        if len(_demo_inst1_key_allKeys):
            demo_inst1_key.keys = _demo_inst1_key_allKeys[-1].name  # just the last key pressed
            demo_inst1_key.rt = _demo_inst1_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demo_form_instruct1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demo_form_instruct1"-------
for thisComponent in demo_form_instruct1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if demo_inst1_key.keys in ['', [], None]:  # No response was made
    demo_inst1_key.keys = None
thisExp.addData('demo_inst1_key.keys',demo_inst1_key.keys)
if demo_inst1_key.keys != None:  # we had a response
    thisExp.addData('demo_inst1_key.rt', demo_inst1_key.rt)
thisExp.nextEntry()
# the Routine "demo_form_instruct1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "demoForm"-------
continueRoutine = True
# update component parameters for each repeat
if expInfo['session'] == '001':
    continueRoutine = False
form_key.keys = []
form_key.rt = []
_form_key_allKeys = []
# keep track of which components have finished
demoFormComponents = [form, form_key, form_inst]
for thisComponent in demoFormComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
demoFormClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "demoForm"-------
while continueRoutine:
    # get current time
    t = demoFormClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=demoFormClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *form* updates
    if form.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        form.frameNStart = frameN  # exact frame index
        form.tStart = t  # local t and not account for scr refresh
        form.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(form, 'tStartRefresh')  # time at next scr refresh
        form.setAutoDraw(True)
    
    # *form_key* updates
    waitOnFlip = False
    if form_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        form_key.frameNStart = frameN  # exact frame index
        form_key.tStart = t  # local t and not account for scr refresh
        form_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(form_key, 'tStartRefresh')  # time at next scr refresh
        form_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(form_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(form_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if form_key.status == STARTED and not waitOnFlip:
        theseKeys = form_key.getKeys(keyList=['return'], waitRelease=False)
        _form_key_allKeys.extend(theseKeys)
        if len(_form_key_allKeys):
            form_key.keys = _form_key_allKeys[-1].name  # just the last key pressed
            form_key.rt = _form_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *form_inst* updates
    if form_inst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        form_inst.frameNStart = frameN  # exact frame index
        form_inst.tStart = t  # local t and not account for scr refresh
        form_inst.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(form_inst, 'tStartRefresh')  # time at next scr refresh
        form_inst.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demoFormComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demoForm"-------
for thisComponent in demoFormComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
form.addDataToExp(thisExp, 'rows')
form.autodraw = False
# check responses
if form_key.keys in ['', [], None]:  # No response was made
    form_key.keys = None
thisExp.addData('form_key.keys',form_key.keys)
if form_key.keys != None:  # we had a response
    thisExp.addData('form_key.rt', form_key.rt)
thisExp.nextEntry()
# the Routine "demoForm" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "demo_inst2"-------
continueRoutine = True
# update component parameters for each repeat
if expInfo['session'] == '001':
    continueRoutine = False
demo_inst2_key.keys = []
demo_inst2_key.rt = []
_demo_inst2_key_allKeys = []
# keep track of which components have finished
demo_inst2Components = [demo_inst2_text, demo_inst2_key]
for thisComponent in demo_inst2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
demo_inst2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "demo_inst2"-------
while continueRoutine:
    # get current time
    t = demo_inst2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=demo_inst2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *demo_inst2_text* updates
    if demo_inst2_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demo_inst2_text.frameNStart = frameN  # exact frame index
        demo_inst2_text.tStart = t  # local t and not account for scr refresh
        demo_inst2_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demo_inst2_text, 'tStartRefresh')  # time at next scr refresh
        demo_inst2_text.setAutoDraw(True)
    
    # *demo_inst2_key* updates
    waitOnFlip = False
    if demo_inst2_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demo_inst2_key.frameNStart = frameN  # exact frame index
        demo_inst2_key.tStart = t  # local t and not account for scr refresh
        demo_inst2_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demo_inst2_key, 'tStartRefresh')  # time at next scr refresh
        demo_inst2_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(demo_inst2_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(demo_inst2_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if demo_inst2_key.status == STARTED and not waitOnFlip:
        theseKeys = demo_inst2_key.getKeys(keyList=['return'], waitRelease=False)
        _demo_inst2_key_allKeys.extend(theseKeys)
        if len(_demo_inst2_key_allKeys):
            demo_inst2_key.keys = _demo_inst2_key_allKeys[-1].name  # just the last key pressed
            demo_inst2_key.rt = _demo_inst2_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demo_inst2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demo_inst2"-------
for thisComponent in demo_inst2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if demo_inst2_key.keys in ['', [], None]:  # No response was made
    demo_inst2_key.keys = None
thisExp.addData('demo_inst2_key.keys',demo_inst2_key.keys)
if demo_inst2_key.keys != None:  # we had a response
    thisExp.addData('demo_inst2_key.rt', demo_inst2_key.rt)
thisExp.nextEntry()
# the Routine "demo_inst2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "demo_2"-------
continueRoutine = True
# update component parameters for each repeat
if expInfo['session'] == '001':
    continueRoutine = False

modify = False
gender.text = ''
event.clearEvents('keyboard')

# keep track of which components have finished
demo_2Components = [demo2_instr_text, demo2_submit_text, gender]
for thisComponent in demo_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
demo_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "demo_2"-------
while continueRoutine:
    # get current time
    t = demo_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=demo_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    keys = event.getKeys()
    if len(keys):
        if 'space' in keys:
            gender.text = gender.text + ' '
        elif 'backspace' in keys:
            gender.text = gender.text[:-1]
        elif 'lshift' in keys or 'rshift' in keys:
            modify = True
        elif 'return' in keys:
            continueRoutine = False
        else:
            if modify:
                gender.text = gender.text + keys[0].upper()
                modify = False
            else:
                gender.text = gender.text + keys[0]
    
    # *demo2_instr_text* updates
    if demo2_instr_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demo2_instr_text.frameNStart = frameN  # exact frame index
        demo2_instr_text.tStart = t  # local t and not account for scr refresh
        demo2_instr_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demo2_instr_text, 'tStartRefresh')  # time at next scr refresh
        demo2_instr_text.setAutoDraw(True)
    
    # *demo2_submit_text* updates
    if demo2_submit_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demo2_submit_text.frameNStart = frameN  # exact frame index
        demo2_submit_text.tStart = t  # local t and not account for scr refresh
        demo2_submit_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demo2_submit_text, 'tStartRefresh')  # time at next scr refresh
        demo2_submit_text.setAutoDraw(True)
    
    # *gender* updates
    if gender.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gender.frameNStart = frameN  # exact frame index
        gender.tStart = t  # local t and not account for scr refresh
        gender.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gender, 'tStartRefresh')  # time at next scr refresh
        gender.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demo_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demo_2"-------
for thisComponent in demo_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData("gender_string", gender.text)
# the Routine "demo_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "demo_3"-------
continueRoutine = True
# update component parameters for each repeat
if expInfo['session'] == '001':
    continueRoutine = False

modify = False
age.text = ''
event.clearEvents('keyboard')
# keep track of which components have finished
demo_3Components = [demo3_instr, demo3_submit_text, age]
for thisComponent in demo_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
demo_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "demo_3"-------
while continueRoutine:
    # get current time
    t = demo_3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=demo_3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    keys = event.getKeys()
    if len(keys):
        if 'space' in keys:
            age.text = age.text + ' '
        elif 'backspace' in keys:
            age.text = age.text[:-1]
        elif 'lshift' in keys or 'rshift' in keys:
            modify = True
        elif 'return' in keys:
            continueRoutine = False
        else:
            if modify:
                age.text = age.text + keys[0].upper()
                modify = False
            else:
                age.text = age.text + keys[0]
    
    # *demo3_instr* updates
    if demo3_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demo3_instr.frameNStart = frameN  # exact frame index
        demo3_instr.tStart = t  # local t and not account for scr refresh
        demo3_instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demo3_instr, 'tStartRefresh')  # time at next scr refresh
        demo3_instr.setAutoDraw(True)
    
    # *demo3_submit_text* updates
    if demo3_submit_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demo3_submit_text.frameNStart = frameN  # exact frame index
        demo3_submit_text.tStart = t  # local t and not account for scr refresh
        demo3_submit_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demo3_submit_text, 'tStartRefresh')  # time at next scr refresh
        demo3_submit_text.setAutoDraw(True)
    
    # *age* updates
    if age.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        age.frameNStart = frameN  # exact frame index
        age.tStart = t  # local t and not account for scr refresh
        age.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(age, 'tStartRefresh')  # time at next scr refresh
        age.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demo_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demo_3"-------
for thisComponent in demo_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData("age_string", age.text)
# the Routine "demo_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "demo_4"-------
continueRoutine = True
# update component parameters for each repeat
if expInfo['session'] == '001':
    continueRoutine = False
demo4_key.keys = []
demo4_key.rt = []
_demo4_key_allKeys = []
# keep track of which components have finished
demo_4Components = [demo4_text, demo4_key]
for thisComponent in demo_4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
demo_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "demo_4"-------
while continueRoutine:
    # get current time
    t = demo_4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=demo_4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *demo4_text* updates
    if demo4_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demo4_text.frameNStart = frameN  # exact frame index
        demo4_text.tStart = t  # local t and not account for scr refresh
        demo4_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demo4_text, 'tStartRefresh')  # time at next scr refresh
        demo4_text.setAutoDraw(True)
    
    # *demo4_key* updates
    waitOnFlip = False
    if demo4_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demo4_key.frameNStart = frameN  # exact frame index
        demo4_key.tStart = t  # local t and not account for scr refresh
        demo4_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demo4_key, 'tStartRefresh')  # time at next scr refresh
        demo4_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(demo4_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(demo4_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if demo4_key.status == STARTED and not waitOnFlip:
        theseKeys = demo4_key.getKeys(keyList=['y', 'n'], waitRelease=False)
        _demo4_key_allKeys.extend(theseKeys)
        if len(_demo4_key_allKeys):
            demo4_key.keys = _demo4_key_allKeys[-1].name  # just the last key pressed
            demo4_key.rt = _demo4_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demo_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demo_4"-------
for thisComponent in demo_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if demo4_key.keys in ['', [], None]:  # No response was made
    demo4_key.keys = None
thisExp.addData('demo4_key.keys',demo4_key.keys)
if demo4_key.keys != None:  # we had a response
    thisExp.addData('demo4_key.rt', demo4_key.rt)
thisExp.nextEntry()
# the Routine "demo_4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "demo_5"-------
continueRoutine = True
# update component parameters for each repeat
if expInfo['session'] == '001':
    continueRoutine = False

modify = False
language.text = ''
event.clearEvents('keyboard')
# keep track of which components have finished
demo_5Components = [dem05_text, demo5_submit_text, language]
for thisComponent in demo_5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
demo_5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "demo_5"-------
while continueRoutine:
    # get current time
    t = demo_5Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=demo_5Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    keys = event.getKeys()
    if len(keys):
        if 'space' in keys:
            language.text = language.text + ' '
        elif 'backspace' in keys:
            language.text = language.text[:-1]
        elif 'lshift' in keys or 'rshift' in keys:
            modify = True
        elif 'return' in keys:
            continueRoutine = False
        else:
            if modify:
                language.text = language.text + keys[0].upper()
                modify = False
            else:
                language.text = language.text + keys[0]
    
    # *dem05_text* updates
    if dem05_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        dem05_text.frameNStart = frameN  # exact frame index
        dem05_text.tStart = t  # local t and not account for scr refresh
        dem05_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(dem05_text, 'tStartRefresh')  # time at next scr refresh
        dem05_text.setAutoDraw(True)
    
    # *demo5_submit_text* updates
    if demo5_submit_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demo5_submit_text.frameNStart = frameN  # exact frame index
        demo5_submit_text.tStart = t  # local t and not account for scr refresh
        demo5_submit_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demo5_submit_text, 'tStartRefresh')  # time at next scr refresh
        demo5_submit_text.setAutoDraw(True)
    
    # *language* updates
    if language.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        language.frameNStart = frameN  # exact frame index
        language.tStart = t  # local t and not account for scr refresh
        language.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(language, 'tStartRefresh')  # time at next scr refresh
        language.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demo_5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demo_5"-------
for thisComponent in demo_5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData("typedWord", language.text)
# the Routine "demo_5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "exp_end"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
exp_endComponents = [end_text]
for thisComponent in exp_endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
exp_endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "exp_end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = exp_endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=exp_endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_text* updates
    if end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text.frameNStart = frameN  # exact frame index
        end_text.tStart = t  # local t and not account for scr refresh
        end_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text, 'tStartRefresh')  # time at next scr refresh
        end_text.setAutoDraw(True)
    if end_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_text.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            end_text.tStop = t  # not accounting for scr refresh
            end_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end_text, 'tStopRefresh')  # time at next scr refresh
            end_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in exp_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "exp_end"-------
for thisComponent in exp_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
os.remove(filename + '_train_cond.csv')
os.remove(filename + 'genfile1.csv')
os.remove(filename + 'genfile2.csv')
os.remove(filename + '_training_stim.csv')

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
