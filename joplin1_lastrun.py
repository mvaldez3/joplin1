#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on Wed Jul 28 14:01:28 2021
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('2021.1.4')


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
psychopyVersion = '2021.1.4'
expName = 'joplin1'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Volumes/shares/Cabi/exp/joplin/joplin1/joplin1_lastrun.py',
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
    size=[2560, 1440], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1,1,1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Welcome_Initializing_Screen"
Welcome_Initializing_ScreenClock = core.Clock()
# # run randpro_select to randomly select prototype for the experiment
import stim_file_script as sf
random_proto = sf.randpro_select('/Volumes/shares/Cabi/exp/joplin/joplin1/stim_files/Prototype.csv', None)
welcome_text = visual.TextStim(win=win, name='welcome_text',
    text='Insert welcome text.\n\nPress SPACE to proceed',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
welcome_key = keyboard.Keyboard()

# Initialize components for Routine "recodeTrain"
recodeTrainClock = core.Clock()
#use random prototype to build stimulus set
sf.stim_build('/Volumes/shares/Cabi/exp/joplin/joplin1/stim_files/dev_train.csv', random_proto)
os.rename('/Volumes/shares/Cabi/exp/joplin/joplin1/data/_stimfile.csv', filename + '_stimfile_train.csv')

# Initialize components for Routine "stimTrain"
stimTrainClock = core.Clock()
train_image = visual.ImageStim(
    win=win,
    name='train_image', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.05, 0.1), size=[0.45, 0.675],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-1.0)
train_key = keyboard.Keyboard()
batmans_text = visual.TextStim(win=win, name='batmans_text',
    text='',
    font='Open Sans',
    pos=[-.35,-.35], height=0.08, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
robins_text = visual.TextStim(win=win, name='robins_text',
    text='',
    font='Open Sans',
    pos=[0.35,-0.35], height=0.08, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
feedback_text = visual.TextStim(win=win, name='feedback_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "fix1000"
fix1000Clock = core.Clock()
ITIstim = visual.ShapeStim(
    win=win, name='ITIstim', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "recodeTest"
recodeTestClock = core.Clock()

# Initialize components for Routine "stimTest"
stimTestClock = core.Clock()
test_image = visual.ImageStim(
    win=win,
    name='test_image', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.05, 0.1), size=[0.45,0.675],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-1.0)
test_key = keyboard.Keyboard()
batmans_text_test = visual.TextStim(win=win, name='batmans_text_test',
    text='Batmans',
    font='Open Sans',
    pos=[-0.35,-0.35], height=0.08, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
robins_text_test = visual.TextStim(win=win, name='robins_text_test',
    text='Robins',
    font='Open Sans',
    pos=[0.35,-0.35], height=0.08, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "fix1000"
fix1000Clock = core.Clock()
ITIstim = visual.ShapeStim(
    win=win, name='ITIstim', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "debrief_thankyou"
debrief_thankyouClock = core.Clock()
end_text = visual.TextStim(win=win, name='end_text',
    text='Add defbrief/thank you\n\nPress Space to continue',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
end_key = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Welcome_Initializing_Screen"-------
continueRoutine = True
# update component parameters for each repeat
welcome_key.keys = []
welcome_key.rt = []
_welcome_key_allKeys = []
# keep track of which components have finished
Welcome_Initializing_ScreenComponents = [welcome_text, welcome_key]
for thisComponent in Welcome_Initializing_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Welcome_Initializing_ScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Welcome_Initializing_Screen"-------
while continueRoutine:
    # get current time
    t = Welcome_Initializing_ScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Welcome_Initializing_ScreenClock)
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
    if welcome_key.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
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
    for thisComponent in Welcome_Initializing_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome_Initializing_Screen"-------
for thisComponent in Welcome_Initializing_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('welcome_text.started', welcome_text.tStartRefresh)
thisExp.addData('welcome_text.stopped', welcome_text.tStopRefresh)
# check responses
if welcome_key.keys in ['', [], None]:  # No response was made
    welcome_key.keys = None
thisExp.addData('welcome_key.keys',welcome_key.keys)
if welcome_key.keys != None:  # we had a response
    thisExp.addData('welcome_key.rt', welcome_key.rt)
thisExp.addData('welcome_key.started', welcome_key.tStartRefresh)
thisExp.addData('welcome_key.stopped', welcome_key.tStopRefresh)
thisExp.nextEntry()
# the Routine "Welcome_Initializing_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "recodeTrain"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
recodeTrainComponents = []
for thisComponent in recodeTrainComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
recodeTrainClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "recodeTrain"-------
while continueRoutine:
    # get current time
    t = recodeTrainClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=recodeTrainClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in recodeTrainComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "recodeTrain"-------
for thisComponent in recodeTrainComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "recodeTrain" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_train = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(filename + '_stimfile_train.csv'),
    seed=None, name='trials_train')
thisExp.addLoop(trials_train)  # add the loop to the experiment
thisTrials_train = trials_train.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_train.rgb)
if thisTrials_train != None:
    for paramName in thisTrials_train:
        exec('{} = thisTrials_train[paramName]'.format(paramName))

for thisTrials_train in trials_train:
    currentLoop = trials_train
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_train.rgb)
    if thisTrials_train != None:
        for paramName in thisTrials_train:
            exec('{} = thisTrials_train[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "stimTrain"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    # rename the stim_id to match image names and file path
    train_stim = '/Volumes/shares/Cabi/stimuli/cartoon_animals/Set1/' + str(stim_id.replace('\'', '')) + '.jpg'
    
    train_image.setImage(train_stim)
    train_key.keys = []
    train_key.rt = []
    _train_key_allKeys = []
    batmans_text.setText('Batmans')
    robins_text.setText('Robins')
    # keep track of which components have finished
    stimTrainComponents = [train_image, train_key, batmans_text, robins_text]
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
            if tThisFlipGlobal > train_image.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                train_image.tStop = t  # not accounting for scr refresh
                train_image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(train_image, 'tStopRefresh')  # time at next scr refresh
                train_image.setAutoDraw(False)
        
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
        
        # *batmans_text* updates
        if batmans_text.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            batmans_text.frameNStart = frameN  # exact frame index
            batmans_text.tStart = t  # local t and not account for scr refresh
            batmans_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(batmans_text, 'tStartRefresh')  # time at next scr refresh
            batmans_text.setAutoDraw(True)
        if batmans_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > batmans_text.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                batmans_text.tStop = t  # not accounting for scr refresh
                batmans_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(batmans_text, 'tStopRefresh')  # time at next scr refresh
                batmans_text.setAutoDraw(False)
        
        # *robins_text* updates
        if robins_text.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            robins_text.frameNStart = frameN  # exact frame index
            robins_text.tStart = t  # local t and not account for scr refresh
            robins_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(robins_text, 'tStartRefresh')  # time at next scr refresh
            robins_text.setAutoDraw(True)
        if robins_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > robins_text.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                robins_text.tStop = t  # not accounting for scr refresh
                robins_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(robins_text, 'tStopRefresh')  # time at next scr refresh
                robins_text.setAutoDraw(False)
        
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
    trials_train.addData('train_image.started', train_image.tStartRefresh)
    trials_train.addData('train_image.stopped', train_image.tStopRefresh)
    # check responses
    if train_key.keys in ['', [], None]:  # No response was made
        train_key.keys = None
        # was no response the correct answer?!
        if str(correct_key).lower() == 'none':
           train_key.corr = 1;  # correct non-response
        else:
           train_key.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_train (TrialHandler)
    trials_train.addData('train_key.keys',train_key.keys)
    trials_train.addData('train_key.corr', train_key.corr)
    if train_key.keys != None:  # we had a response
        trials_train.addData('train_key.rt', train_key.rt)
    trials_train.addData('train_key.started', train_key.tStartRefresh)
    trials_train.addData('train_key.stopped', train_key.tStopRefresh)
    trials_train.addData('batmans_text.started', batmans_text.tStartRefresh)
    trials_train.addData('batmans_text.stopped', batmans_text.tStopRefresh)
    trials_train.addData('robins_text.started', robins_text.tStartRefresh)
    trials_train.addData('robins_text.stopped', robins_text.tStopRefresh)
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    if not train_key.keys:
        feedback = "Oops...you failed to respond within the alloted time"
    elif train_key.corr:
        feedback = f"Correct. It was {category.upper()}"
    else:
        feedback = f"Incorrect. It was {category.upper()}"
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
            if tThisFlipGlobal > feedback_text.tStartRefresh + 3.0-frameTolerance:
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
    trials_train.addData('feedback_text.started', feedback_text.tStartRefresh)
    trials_train.addData('feedback_text.stopped', feedback_text.tStopRefresh)
    
    # ------Prepare to start Routine "fix1000"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fix1000Components = [ITIstim]
    for thisComponent in fix1000Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fix1000Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fix1000"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fix1000Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fix1000Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ITIstim* updates
        if ITIstim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ITIstim.frameNStart = frameN  # exact frame index
            ITIstim.tStart = t  # local t and not account for scr refresh
            ITIstim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ITIstim, 'tStartRefresh')  # time at next scr refresh
            ITIstim.setAutoDraw(True)
        if ITIstim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ITIstim.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                ITIstim.tStop = t  # not accounting for scr refresh
                ITIstim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ITIstim, 'tStopRefresh')  # time at next scr refresh
                ITIstim.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fix1000Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fix1000"-------
    for thisComponent in fix1000Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_train.addData('ITIstim.started', ITIstim.tStartRefresh)
    trials_train.addData('ITIstim.stopped', ITIstim.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_train'


# ------Prepare to start Routine "recodeTest"-------
continueRoutine = True
# update component parameters for each repeat
# recode the test stimuli in relation to randomly selected prototype
sf.stim_build('/Volumes/shares/Cabi/exp/joplin/joplin1/stim_files/test_stim1.csv', random_proto)
os.rename('/Volumes/shares/Cabi/exp/joplin/joplin1/data/_stimfile.csv', filename + '_stimfile_test.csv')
# keep track of which components have finished
recodeTestComponents = []
for thisComponent in recodeTestComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
recodeTestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "recodeTest"-------
while continueRoutine:
    # get current time
    t = recodeTestClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=recodeTestClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in recodeTestComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "recodeTest"-------
for thisComponent in recodeTestComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "recodeTest" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_test = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(filename + '_stimfile_test.csv'),
    seed=None, name='trials_test')
thisExp.addLoop(trials_test)  # add the loop to the experiment
thisTrials_test = trials_test.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_test.rgb)
if thisTrials_test != None:
    for paramName in thisTrials_test:
        exec('{} = thisTrials_test[paramName]'.format(paramName))

for thisTrials_test in trials_test:
    currentLoop = trials_test
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_test.rgb)
    if thisTrials_test != None:
        for paramName in thisTrials_test:
            exec('{} = thisTrials_test[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "stimTest"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    stim_test = '/Volumes/shares/Cabi/stimuli/cartoon_animals/Set1/' + str(stim_id.replace('\'', '')) + '.jpg'
    test_image.setImage(stim_test)
    test_key.keys = []
    test_key.rt = []
    _test_key_allKeys = []
    # keep track of which components have finished
    stimTestComponents = [test_image, test_key, batmans_text_test, robins_text_test]
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
            if tThisFlipGlobal > test_image.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                test_image.tStop = t  # not accounting for scr refresh
                test_image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(test_image, 'tStopRefresh')  # time at next scr refresh
                test_image.setAutoDraw(False)
        
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
        
        # *batmans_text_test* updates
        if batmans_text_test.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            batmans_text_test.frameNStart = frameN  # exact frame index
            batmans_text_test.tStart = t  # local t and not account for scr refresh
            batmans_text_test.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(batmans_text_test, 'tStartRefresh')  # time at next scr refresh
            batmans_text_test.setAutoDraw(True)
        if batmans_text_test.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > batmans_text_test.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                batmans_text_test.tStop = t  # not accounting for scr refresh
                batmans_text_test.frameNStop = frameN  # exact frame index
                win.timeOnFlip(batmans_text_test, 'tStopRefresh')  # time at next scr refresh
                batmans_text_test.setAutoDraw(False)
        
        # *robins_text_test* updates
        if robins_text_test.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            robins_text_test.frameNStart = frameN  # exact frame index
            robins_text_test.tStart = t  # local t and not account for scr refresh
            robins_text_test.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(robins_text_test, 'tStartRefresh')  # time at next scr refresh
            robins_text_test.setAutoDraw(True)
        if robins_text_test.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > robins_text_test.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                robins_text_test.tStop = t  # not accounting for scr refresh
                robins_text_test.frameNStop = frameN  # exact frame index
                win.timeOnFlip(robins_text_test, 'tStopRefresh')  # time at next scr refresh
                robins_text_test.setAutoDraw(False)
        
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
    trials_test.addData('test_image.started', test_image.tStartRefresh)
    trials_test.addData('test_image.stopped', test_image.tStopRefresh)
    # check responses
    if test_key.keys in ['', [], None]:  # No response was made
        test_key.keys = None
        # was no response the correct answer?!
        if str(correct_key).lower() == 'none':
           test_key.corr = 1;  # correct non-response
        else:
           test_key.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_test (TrialHandler)
    trials_test.addData('test_key.keys',test_key.keys)
    trials_test.addData('test_key.corr', test_key.corr)
    if test_key.keys != None:  # we had a response
        trials_test.addData('test_key.rt', test_key.rt)
    trials_test.addData('test_key.started', test_key.tStartRefresh)
    trials_test.addData('test_key.stopped', test_key.tStopRefresh)
    trials_test.addData('batmans_text_test.started', batmans_text_test.tStartRefresh)
    trials_test.addData('batmans_text_test.stopped', batmans_text_test.tStopRefresh)
    trials_test.addData('robins_text_test.started', robins_text_test.tStartRefresh)
    trials_test.addData('robins_text_test.stopped', robins_text_test.tStopRefresh)
    
    # ------Prepare to start Routine "fix1000"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fix1000Components = [ITIstim]
    for thisComponent in fix1000Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fix1000Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fix1000"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fix1000Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fix1000Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ITIstim* updates
        if ITIstim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ITIstim.frameNStart = frameN  # exact frame index
            ITIstim.tStart = t  # local t and not account for scr refresh
            ITIstim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ITIstim, 'tStartRefresh')  # time at next scr refresh
            ITIstim.setAutoDraw(True)
        if ITIstim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ITIstim.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                ITIstim.tStop = t  # not accounting for scr refresh
                ITIstim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ITIstim, 'tStopRefresh')  # time at next scr refresh
                ITIstim.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fix1000Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fix1000"-------
    for thisComponent in fix1000Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_test.addData('ITIstim.started', ITIstim.tStartRefresh)
    trials_test.addData('ITIstim.stopped', ITIstim.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_test'


# ------Prepare to start Routine "debrief_thankyou"-------
continueRoutine = True
# update component parameters for each repeat
end_key.keys = []
end_key.rt = []
_end_key_allKeys = []
# keep track of which components have finished
debrief_thankyouComponents = [end_text, end_key]
for thisComponent in debrief_thankyouComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
debrief_thankyouClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "debrief_thankyou"-------
while continueRoutine:
    # get current time
    t = debrief_thankyouClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=debrief_thankyouClock)
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
    
    # *end_key* updates
    waitOnFlip = False
    if end_key.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        end_key.frameNStart = frameN  # exact frame index
        end_key.tStart = t  # local t and not account for scr refresh
        end_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_key, 'tStartRefresh')  # time at next scr refresh
        end_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_key.status == STARTED and not waitOnFlip:
        theseKeys = end_key.getKeys(keyList=['space'], waitRelease=False)
        _end_key_allKeys.extend(theseKeys)
        if len(_end_key_allKeys):
            end_key.keys = _end_key_allKeys[-1].name  # just the last key pressed
            end_key.rt = _end_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in debrief_thankyouComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "debrief_thankyou"-------
for thisComponent in debrief_thankyouComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('end_text.started', end_text.tStartRefresh)
thisExp.addData('end_text.stopped', end_text.tStopRefresh)
# check responses
if end_key.keys in ['', [], None]:  # No response was made
    end_key.keys = None
thisExp.addData('end_key.keys',end_key.keys)
if end_key.keys != None:  # we had a response
    thisExp.addData('end_key.rt', end_key.rt)
thisExp.addData('end_key.started', end_key.tStartRefresh)
thisExp.addData('end_key.stopped', end_key.tStopRefresh)
thisExp.nextEntry()
# the Routine "debrief_thankyou" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# get rid of unecessary conditions file
os.remove(filename + '_stimfile_train.csv')
os.remove(filename + '_stimfile_test.csv')

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
