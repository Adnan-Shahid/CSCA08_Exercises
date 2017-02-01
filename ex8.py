class LightSwitch(object):
    '''A light switch that can be turned on or off'''

    def __init__(self, state):
        '''(LightSwitch, string) -> NoneType
        creates a lightswitch with a default state that is given,
        the switch can either be turned on or off
        '''
        # Converts the string input of state into a boolean
        if (state == 'on'):
            self._state = True
        elif (state == 'off'):
            self._state = False

    def __str__(self):
        '''(LightSwitch) -> str
        returns a string representation of this switch
        '''
        # calling the state of the switch
        Output = ''
        # creates appropriate output for the switch state
        if (self._state):
            Output = 'I am on'
        else:
            Output = 'I am off'

        return Output

    def turn_on(self):
        '''(LightSwitch) -> NoneType
        Set this LightSwitch's state to be on'''
        # Turning on the switch
        self._state = True

    def turn_off(self):
        '''(LightSwitch) -> NoneType
        Set this LightSwitch's state to be off'''
        # Turning off the switch
        self._state = False

    def flip(self):
        '''(LightSwitch) -> NoneType
        Set this LightSwitch's state to be the opposite of what
        it currently is'''
        # Inverting the state of the switch
        self._state = not(self._state)

    def get_state(self):
        '''(LightSwitch) -> bool
        Returns the state of the lightswitch
        '''
        state = self._state
        return state


class SwitchBoard(object):
    '''A SwitchBoard that holds multiple LightSwitches'''
    def __init__(self, num_switches):
        '''(SwitchBoard, int, str)

        '''
        # Empty list of switches
        self._switches = []

        # creating num_switches amount of switches
        for i in range(num_switches):
            # create a switch
            new_switch = LightSwitch('off')
            # adding the switch to the list of switches
            self._switches.append(new_switch)

    def __str__(self):
        '''(SwitchBoard) -> str
        returns a string representation of the switchboard
        '''
        switches_on = ''
        for i in range(len(self._switches)):
            if ((self._switches[i].get_state()) == True):
                switches_on += (' ' + str(i))
        return ('The following switches are on: ' + switches_on)

    def flip(self, n):
        '''(SwitchBoard, int) -> NoneType
        flips the nth switch within the switchboard
        REQ: num of switches > 0
        REQ: the desired switch value has to be valid
        '''
        self._switch_num = n
        # makes sure the desired switch value is valid
        if (n < len(self._switches)):
            # flips the desired switch
            self._switches[self._switch_num].flip()

    def flip_every(self, n):
        '''(SwitchBoard, int) -> NoneType
        flips every nth switch within the switchboard
        REQ: num of switches > 0
        REQ: n > 0
        REQ: n < amount of switches in the switchboard
        '''
        # Counter variable
        self._incrementor = 0
        # flips every nth switch
        # makes sure it doesnt exceed the amount of switches
        while (self._incrementor < len(self._switches)):
            # flips the switch
            SwitchBoard.flip(self, self._incrementor)
            # incrementing the switch number by n
            self._incrementor = self._incrementor + n
