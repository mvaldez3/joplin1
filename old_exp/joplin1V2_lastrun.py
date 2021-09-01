#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on Mon Aug 16 13:52:48 2021
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
    size=[1280, 720], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color='white', colorSpace='rgb',
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

# Initialize components for Routine "welcome_initializing"
welcome_initializingClock = core.Clock()
#import packages necessary for scripts
import pandas
import csv

# import the script and use the randpro_select function to establish a random prototype for the rest of the experiment
import recode_stim_script as rs
randpro = rs.randpro_select('/Volumes/shares/Cabi/exp/joplin/joplin1/stim_files/prototype.csv')
print(randpro)
welcome_text = visual.TextStim(win=win, name='welcome_text',
    text='Welcome to the experiment!\n\nBefore starting, PLEASE TURN OFF AND PUT AWAY YOUR CELL PHONE and ensure there are no other distractions present in your environment. Please read all on-screen instructions carefully.\n\nFirst we would like you to know about your rights as a participant.\n\nPress SPACE to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
welcome_key = keyboard.Keyboard()

# Initialize components for Routine "build_stim_train"
build_stim_trainClock = core.Clock()
# run the create_train_set to create the training set, recoded to match the prototype
#output will be /data/_training_stim
rs.create_train_set('/Volumes/shares/Cabi/exp/joplin/joplin1/stim_files/train_file.csv', randpro)

# this refers to the training file that will be needed to create the generalization sets
training_stimuli = '/Volumes/shares/Cabi/exp/joplin/joplin1/data/_training_stim.csv'


# Initialize components for Routine "stimTrain"
stimTrainClock = core.Clock()
train_image = visual.ImageStim(
    win=win,
    name='train_image', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.05, 0.1), size=[0.4,0.6],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-1.0)
batmans_train = visual.TextStim(win=win, name='batmans_train',
    text='Batmans',
    font='Open Sans',
    pos=(-0.35, -0.35), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
robins_train = visual.TextStim(win=win, name='robins_train',
    text='Robins',
    font='Open Sans',
    pos=(0.35, -0.35), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
train_key = keyboard.Keyboard()

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
feedback_text = visual.TextStim(win=win, name='feedback_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
fix1000 = visual.ShapeStim(
    win=win, name='fix1000', vertices='cross',
    size=(0.2, 0.2),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "run_break"
run_breakClock = core.Clock()
run_break_text = visual.TextStim(win=win, name='run_break_text',
    text='You will now be given a short break before continuing the experiment. When you are ready to proceed, press SPACE.\n',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
break_key = keyboard.Keyboard()

# Initialize components for Routine "build_stim_test"
build_stim_testClock = core.Clock()
#run the gen_build function to produce a generalization set. Will output to /data/genfile1 and data/genfile2
import generalization_build_script as gb
gen_set = gb.gen_build(training_stimuli, '/Volumes/shares/Cabi/exp/joplin/joplin1/stim_files/prototype.csv', 10)

#recode the gen files to match the prototype
rs.stim_build('/Volumes/shares/Cabi/exp/joplin/joplin1/data/genfile1.csv', randpro)
os.rename('/Volumes/shares/Cabi/exp/joplin/joplin1/data/_stimfile.csv', '/Volumes/shares/Cabi/exp/joplin/joplin1/data/genfile1.csv')
rs.stim_build('/Volumes/shares/Cabi/exp/joplin/joplin1/data/genfile2.csv', randpro)
os.rename('/Volumes/shares/Cabi/exp/joplin/joplin1/data/_stimfile.csv', '/Volumes/shares/Cabi/exp/joplin/joplin1/data/genfile2.csv')


# Initialize components for Routine "stimTest"
stimTestClock = core.Clock()
test_image = visual.ImageStim(
    win=win,
    name='test_image', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.05, 0.1), size=[0.4,0.6],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-1.0)
batmans_test = visual.TextStim(win=win, name='batmans_test',
    text='Batmans',
    font='Open Sans',
    pos=(-0.35, -0.35), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
robins_test = visual.TextStim(win=win, name='robins_test',
    text='Robins',
    font='Open Sans',
    pos=(0.35, -0.35), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
test_key = keyboard.Keyboard()

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
fix1000 = visual.ShapeStim(
    win=win, name='fix1000', vertices='cross',
    size=(0.2, 0.2),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "run_break"
run_breakClock = core.Clock()
run_break_text = visual.TextStim(win=win, name='run_break_text',
    text='You will now be given a short break before continuing the experiment. When you are ready to proceed, press SPACE.\n',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
break_key = keyboard.Keyboard()

# Initialize components for Routine "debrief"
debriefClock = core.Clock()
debrief_text = visual.TextStim(win=win, name='debrief_text',
    text='Thank you for participating in this experiment. We are interested in how people both remember details of specific experiences and how they build general knowledge. The task you completed today involved learning to sort stimuli into categories. In doing so, you needed to form a general idea of what members of each category were like – that is memory for generalities. However, you may have also learned to identify individual category members – that is memory specificity. We are interested in how well people are able to learn both types of information – generalities and specifics – from the same set of stimuli. Do you have any questions about the experiment?',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
end_key = keyboard.Keyboard()

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
# the Routine "welcome_initializing" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "build_stim_train"-------
continueRoutine = True
# update component parameters for each repeat
# Take the training set and input into the cond_file_build function. This functino will add all the necessary components to the file, like the category and correct key response.
rs.cond_file_build(training_stimuli)

#rename the file to train_conditions and use this file for the loop.
os.rename('/Volumes/shares/Cabi/exp/joplin/joplin1/data/_cond_file.csv', '/Volumes/shares/Cabi/exp/joplin/joplin1/data/_train_cond.csv')
# keep track of which components have finished
build_stim_trainComponents = []
for thisComponent in build_stim_trainComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
build_stim_trainClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "build_stim_train"-------
while continueRoutine:
    # get current time
    t = build_stim_trainClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=build_stim_trainClock)
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
    for thisComponent in build_stim_trainComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "build_stim_train"-------
for thisComponent in build_stim_trainComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "build_stim_train" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
train_runs = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('train_cond.xlsx'),
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
        trialList=data.importConditions(train_set),
        seed=None, name='train_trials')
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
        train_stim = ('/Volumes/shares/Cabi/stimuli/cartoon_animals/Set1/' + str(stim_id.replace(' ', '')) + '.jpg')
        train_image.setImage(train_stim)
        train_key.keys = []
        train_key.rt = []
        _train_key_allKeys = []
        # keep track of which components have finished
        stimTrainComponents = [train_image, batmans_train, robins_train, train_key]
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
            
            # *batmans_train* updates
            if batmans_train.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                batmans_train.frameNStart = frameN  # exact frame index
                batmans_train.tStart = t  # local t and not account for scr refresh
                batmans_train.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(batmans_train, 'tStartRefresh')  # time at next scr refresh
                batmans_train.setAutoDraw(True)
            if batmans_train.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > batmans_train.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    batmans_train.tStop = t  # not accounting for scr refresh
                    batmans_train.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(batmans_train, 'tStopRefresh')  # time at next scr refresh
                    batmans_train.setAutoDraw(False)
            
            # *robins_train* updates
            if robins_train.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                robins_train.frameNStart = frameN  # exact frame index
                robins_train.tStart = t  # local t and not account for scr refresh
                robins_train.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(robins_train, 'tStartRefresh')  # time at next scr refresh
                robins_train.setAutoDraw(True)
            if robins_train.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > robins_train.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    robins_train.tStop = t  # not accounting for scr refresh
                    robins_train.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(robins_train, 'tStopRefresh')  # time at next scr refresh
                    robins_train.setAutoDraw(False)
            
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
        if not train_key.keys:
            feedback = 'Oops...you failed to respons within the alloted time'
        elif train_key.corr == 1:
            feedback = 'Correct, the answer was ' + category
        else:
            feedback = 'Incorrect, the answer was ' + category
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


# ------Prepare to start Routine "build_stim_test"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
build_stim_testComponents = []
for thisComponent in build_stim_testComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
build_stim_testClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "build_stim_test"-------
while continueRoutine:
    # get current time
    t = build_stim_testClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=build_stim_testClock)
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
    for thisComponent in build_stim_testComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "build_stim_test"-------
for thisComponent in build_stim_testComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "build_stim_test" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
test_runs = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('test_cond.xlsx'),
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
        trialList=data.importConditions(gen_file),
        seed=None, name='test_trials')
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
        test_stim = ('/Volumes/shares/Cabi/stimuli/cartoon_animals/Set1/' + str(stim_id.replace(' ', '')) + '.jpg')
        test_image.setImage(test_stim)
        test_key.keys = []
        test_key.rt = []
        _test_key_allKeys = []
        # keep track of which components have finished
        stimTestComponents = [test_image, batmans_test, robins_test, test_key]
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
            
            # *batmans_test* updates
            if batmans_test.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                batmans_test.frameNStart = frameN  # exact frame index
                batmans_test.tStart = t  # local t and not account for scr refresh
                batmans_test.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(batmans_test, 'tStartRefresh')  # time at next scr refresh
                batmans_test.setAutoDraw(True)
            if batmans_test.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > batmans_test.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    batmans_test.tStop = t  # not accounting for scr refresh
                    batmans_test.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(batmans_test, 'tStopRefresh')  # time at next scr refresh
                    batmans_test.setAutoDraw(False)
            
            # *robins_test* updates
            if robins_test.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                robins_test.frameNStart = frameN  # exact frame index
                robins_test.tStart = t  # local t and not account for scr refresh
                robins_test.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(robins_test, 'tStartRefresh')  # time at next scr refresh
                robins_test.setAutoDraw(True)
            if robins_test.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > robins_test.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    robins_test.tStop = t  # not accounting for scr refresh
                    robins_test.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(robins_test, 'tStopRefresh')  # time at next scr refresh
                    robins_test.setAutoDraw(False)
            
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


# ------Prepare to start Routine "debrief"-------
continueRoutine = True
# update component parameters for each repeat
end_key.keys = []
end_key.rt = []
_end_key_allKeys = []
# keep track of which components have finished
debriefComponents = [debrief_text, end_key]
for thisComponent in debriefComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
debriefClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "debrief"-------
while continueRoutine:
    # get current time
    t = debriefClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=debriefClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *debrief_text* updates
    if debrief_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        debrief_text.frameNStart = frameN  # exact frame index
        debrief_text.tStart = t  # local t and not account for scr refresh
        debrief_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(debrief_text, 'tStartRefresh')  # time at next scr refresh
        debrief_text.setAutoDraw(True)
    
    # *end_key* updates
    waitOnFlip = False
    if end_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
    for thisComponent in debriefComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "debrief"-------
for thisComponent in debriefComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('debrief_text.started', debrief_text.tStartRefresh)
thisExp.addData('debrief_text.stopped', debrief_text.tStopRefresh)
# check responses
if end_key.keys in ['', [], None]:  # No response was made
    end_key.keys = None
thisExp.addData('end_key.keys',end_key.keys)
if end_key.keys != None:  # we had a response
    thisExp.addData('end_key.rt', end_key.rt)
thisExp.addData('end_key.started', end_key.tStartRefresh)
thisExp.addData('end_key.stopped', end_key.tStopRefresh)
thisExp.nextEntry()
# the Routine "debrief" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
os.remove(filename + '_test_stim.csv')
os.remove(filename + '_train_stim.csv')
#os.remove('/Volumes/shares/Cabi/exp/joplin/joplin1/data/genfile1.csv')
os.rename('/Volumes/shares/Cabi/exp/joplin/joplin1/data/_genfile1.csv')
os.rename('/Volumes/shares/Cabi/exp/joplin/joplin1/data/_genfile2.csv')
#os.rename('/Volumes/shares/Cabi/exp/joplin/joplin1/data/genfile2.csv')

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
