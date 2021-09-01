#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Tue Aug 31 14:36:20 2021
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
expName = 'joplin_rebuild'  # from the Builder filename that created this script
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
    originPath='/Volumes/shares/Cabi/exp/joplin/joplin1/joplin_rebuild.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[2560, 1440], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
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

# Initialize components for Routine "welcome"
welcomeClock = core.Clock()
#define random seeds
import random
random_seed = expInfo(['participant'])
random.seed(random_seed)

#set paths to stimulus sets
stim_set1 = '/Volumes/shares/Cabi/stimuli/cartoon_animals/Set1'
stim_set2 = '/Volumes/shares/Cabi/stimuli/cartoon_animals/Set2'

#define categories
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
print(randpro)
welcome_text = visual.TextStim(win=win, name='welcome_text',
    text='welc_text',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
welcome_key = keyboard.Keyboard()

# Initialize components for Routine "train_instruct1"
train_instruct1Clock = core.Clock()
train_inst1_text = visual.TextStim(win=win, name='train_inst1_text',
    text='inst1_train_text',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
train_inst1_key = keyboard.Keyboard()

# Initialize components for Routine "train_instruct2"
train_instruct2Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text="'You will complete 8 runs of the training phase. Between each run, you will be given the opportunity to take a break. You may take as long as you need before returning to the experiemnt. /n/nPress SPACE to continue. '",
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "welcome"-------
continueRoutine = True
# update component parameters for each repeat
if expInfo['session'] == '001':
    welc_text = u'Welcome to the experiment! \n\n You will first complete a training phase where you will be presented images of cartoon animals and asked to determine whether they belong to the %s group or the %s group.\n\n You will not know which group the animals belong to at first. However, you will be given feedback on your answer, which you can then use to help you group the animals.\n\n Press SPACE to continue with the instructions.' % (session_cat['categorya'], session_cat['categoryb'])
if expInfo['session'] == '002':
    welc_text = u'Welcome to the experiment!\n\n Similar to the last session, you will start by completing a training phase where you will group cartoon animals into two different groups. This time, you will be asked to determine if the animal belongs to the %s group or the %s group. Remember, you will not know which group the animal belongs to at first, but will be given feedback on your answers that you can then use to help you group the animals.\n\n Press SPACE to continue with the instructions.' % (session_cat['categorya'], session_cat['categoryb'])
welcome_key.keys = []
welcome_key.rt = []
_welcome_key_allKeys = []
# keep track of which components have finished
welcomeComponents = [welcome_text, welcome_key]
for thisComponent in welcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcome"-------
while continueRoutine:
    # get current time
    t = welcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcomeClock)
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
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome"-------
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if welcome_key.keys in ['', [], None]:  # No response was made
    welcome_key.keys = None
thisExp.addData('welcome_key.keys',welcome_key.keys)
if welcome_key.keys != None:  # we had a response
    thisExp.addData('welcome_key.rt', welcome_key.rt)
thisExp.nextEntry()
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "train_instruct1"-------
continueRoutine = True
# update component parameters for each repeat
inst1_train_text = u'For each image, you will have 3 seconds to give your response before the computer automatically moves to the next screen.\n\n To select %s, press "f".\n To select %s, press "j".\n\n Press "f" or "j" to continue with the instructions.' % (session_cat['categorya'], session_cat['categoryb'])
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
        theseKeys = train_inst1_key.getKeys(keyList=['space'], waitRelease=False)
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
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
train_instruct2Components = [text]
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
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = train_instruct2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=train_instruct2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
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
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)

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
