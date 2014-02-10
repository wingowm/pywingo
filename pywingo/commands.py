class WingoCommands(object):
    def __init__(self):
        assert False, 'cannot create WingoCommands directly'

    def AddWorkspace(self, Name):
        '''
Adds a new workspace to Wingo with a name Name. Note that a workspace name
must be unique with respect to other workspaces and must have non-zero length.

The name of the workspace that was added is returned.
        '''
        self._assert_arg_type('Name', Name, [basestring])

        arg_str = self._gribble_arg_str([Name])
        val = self.gribble('AddWorkspace %s' % arg_str)
        return self._from_str('AddWorkspace', val)

    def And(self, Op1, Op2):
        '''
Returns the logical AND of Op1 and Op2.

If Op1 or Op2 is not in {0, 1}, then a warning is logged and nil is returned.
        '''
        self._assert_arg_type('Op1', Op1, [int])
        self._assert_arg_type('Op2', Op2, [int])

        arg_str = self._gribble_arg_str([Op1, Op2])
        val = self.gribble('And %s' % arg_str)
        return self._from_str('And', val)

    def AutoCycle(self, Workspace):
        '''
Cycles to the next automatic tiling layout in the workspace specified by
Workspace.

Note that this command has no effect if the workspace is not visible.

Workspace may be a workspace index (integer) starting at 0, or a workspace
name.
        '''
        self._assert_arg_type('Workspace', Workspace, [int, basestring])

        arg_str = self._gribble_arg_str([Workspace])
        val = self.gribble('AutoCycle %s' % arg_str)
        return self._from_str('AutoCycle', val)

    def AutoMakeMaster(self, Workspace):
        '''
Switches the current window with the first master in the layout for the
workspace specified by Workspace.

Note that this command has no effect if the workspace is not visible.

Workspace may be a workspace index (integer) starting at 0, or a workspace
name.
        '''
        self._assert_arg_type('Workspace', Workspace, [int, basestring])

        arg_str = self._gribble_arg_str([Workspace])
        val = self.gribble('AutoMakeMaster %s' % arg_str)
        return self._from_str('AutoMakeMaster', val)

    def AutoMaster(self, Workspace):
        '''
Focuses the (first) master window in the layout for the workspace specified
by Workspace.

Note that this command has no effect if the workspace is not visible.

Workspace may be a workspace index (integer) starting at 0, or a workspace
name.
        '''
        self._assert_arg_type('Workspace', Workspace, [int, basestring])

        arg_str = self._gribble_arg_str([Workspace])
        val = self.gribble('AutoMaster %s' % arg_str)
        return self._from_str('AutoMaster', val)

    def AutoMastersFewer(self, Workspace):
        '''
Allows one fewer master window to fit into the master split.

Workspace may be a workspace index (integer) starting at 0, or a workspace
name.
        '''
        self._assert_arg_type('Workspace', Workspace, [int, basestring])

        arg_str = self._gribble_arg_str([Workspace])
        val = self.gribble('AutoMastersFewer %s' % arg_str)
        return self._from_str('AutoMastersFewer', val)

    def AutoMastersMore(self, Workspace):
        '''
Allows one more master window to fit into the master split.

Workspace may be a workspace index (integer) starting at 0, or a workspace
name.
        '''
        self._assert_arg_type('Workspace', Workspace, [int, basestring])

        arg_str = self._gribble_arg_str([Workspace])
        val = self.gribble('AutoMastersMore %s' % arg_str)
        return self._from_str('AutoMastersMore', val)

    def AutoNext(self, Workspace):
        '''
Moves focus to the next client in the layout.

Note that this command has no effect if the workspace is not visible.

Workspace may be a workspace index (integer) starting at 0, or a workspace
name.
        '''
        self._assert_arg_type('Workspace', Workspace, [int, basestring])

        arg_str = self._gribble_arg_str([Workspace])
        val = self.gribble('AutoNext %s' % arg_str)
        return self._from_str('AutoNext', val)

    def AutoPrev(self, Workspace):
        '''
Moves focus to the next client in the layout.

Note that this command has no effect if the workspace is not visible.

Workspace may be a workspace index (integer) starting at 0, or a workspace
name.
        '''
        self._assert_arg_type('Workspace', Workspace, [int, basestring])

        arg_str = self._gribble_arg_str([Workspace])
        val = self.gribble('AutoPrev %s' % arg_str)
        return self._from_str('AutoPrev', val)

    def AutoResizeMaster(self, Workspace, Amount):
        '''
Increases or decreases the size of the master split by Amount in the layout on
the workspace specified by Workspace.

Amount should be a ratio between 0.0 and 1.0.

Workspace may be a workspace index (integer) starting at 0, or a workspace
name.
        '''
        self._assert_arg_type('Workspace', Workspace, [int, basestring])
        self._assert_arg_type('Amount', Amount, [float])

        arg_str = self._gribble_arg_str([Workspace, Amount])
        val = self.gribble('AutoResizeMaster %s' % arg_str)
        return self._from_str('AutoResizeMaster', val)

    def AutoResizeWindow(self, Workspace, Amount):
        '''
Increases or decreases the size of the current window by Amount in the layout
on the workspace specified by Workspace.

Amount should be a ratio between 0.0 and 1.0.

Workspace may be a workspace index (integer) starting at 0, or a workspace
name.
        '''
        self._assert_arg_type('Workspace', Workspace, [int, basestring])
        self._assert_arg_type('Amount', Amount, [float])

        arg_str = self._gribble_arg_str([Workspace, Amount])
        val = self.gribble('AutoResizeWindow %s' % arg_str)
        return self._from_str('AutoResizeWindow', val)

    def AutoSwitchNext(self, Workspace):
        '''
Switches the current window with the next window in the layout.

Note that this command has no effect if the workspace is not visible.

Workspace may be a workspace index (integer) starting at 0, or a workspace
name.
        '''
        self._assert_arg_type('Workspace', Workspace, [int, basestring])

        arg_str = self._gribble_arg_str([Workspace])
        val = self.gribble('AutoSwitchNext %s' % arg_str)
        return self._from_str('AutoSwitchNext', val)

    def AutoSwitchPrev(self, Workspace):
        '''
Switches the current window with the previous window in the layout.

Note that this command has no effect if the workspace is not visible.

Workspace may be a workspace index (integer) starting at 0, or a workspace
name.
        '''
        self._assert_arg_type('Workspace', Workspace, [int, basestring])

        arg_str = self._gribble_arg_str([Workspace])
        val = self.gribble('AutoSwitchPrev %s' % arg_str)
        return self._from_str('AutoSwitchPrev', val)

    def AutoTile(self, Workspace):
        '''
Initiates automatic tiling on the workspace specified by Workspace. If tiling
is already active, the layout will be re-placed.

Note that this command has no effect if the workspace is not visible.

Workspace may be a workspace index (integer) starting at 0, or a workspace
name.
        '''
        self._assert_arg_type('Workspace', Workspace, [int, basestring])

        arg_str = self._gribble_arg_str([Workspace])
        val = self.gribble('AutoTile %s' % arg_str)
        return self._from_str('AutoTile', val)

    def AutoUntile(self, Workspace):
        '''
Stops automatic tiling on the workspace specified by Workspace, and restores
windows to their position and geometry before being tiled. If tiling is not
active on the specified workspace, this command has no effect.

Note that this command has no effect if the workspace is not visible.

Workspace may be a workspace index (integer) starting at 0, or a workspace
name.
        '''
        self._assert_arg_type('Workspace', Workspace, [int, basestring])

        arg_str = self._gribble_arg_str([Workspace])
        val = self.gribble('AutoUntile %s' % arg_str)
        return self._from_str('AutoUntile', val)

    def Close(self, Client):
        '''
Closes the window specified by Client.

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Client', Client, [int, basestring])

        arg_str = self._gribble_arg_str([Client])
        val = self.gribble('Close %s' % arg_str)
        return self._from_str('Close', val)

    def CycleClientChoose(self):
        '''
Activates the current choice in a cycle prompt.
        '''

        arg_str = self._gribble_arg_str([])
        val = self.gribble('CycleClientChoose %s' % arg_str)
        return self._from_str('CycleClientChoose', val)

    def CycleClientHide(self):
        '''
Hides (i.e., cancels) the current cycle prompt.
        '''

        arg_str = self._gribble_arg_str([])
        val = self.gribble('CycleClientHide %s' % arg_str)
        return self._from_str('CycleClientHide', val)

    def CycleClientNext(self, OnlyActiveWorkspace, OnlyVisible, ShowIconified):
        '''
Shows the cycle prompt for clients and advances the selection to the next
client. If the cycle prompt is already visible, then the selection is advanced
to the next client.

OnlyActiveWorkspace specifies that only clients on the current workspace should
be listed. Valid values are "yes" or "no".

OnlyVisible specifies that only clients on visible workspaces should be listed.
Valid values are "yes" or "no".

ShowIconified specifies that iconified clients will be shown. Valid values are
"yes" or "no".
        '''
        self._assert_arg_type('OnlyActiveWorkspace', OnlyActiveWorkspace, [basestring])
        self._assert_arg_type('OnlyVisible', OnlyVisible, [basestring])
        self._assert_arg_type('ShowIconified', ShowIconified, [basestring])

        arg_str = self._gribble_arg_str([OnlyActiveWorkspace, OnlyVisible, ShowIconified])
        val = self.gribble('CycleClientNext %s' % arg_str)
        return self._from_str('CycleClientNext', val)

    def CycleClientPrev(self, OnlyActiveWorkspace, OnlyVisible, ShowIconified):
        '''
Shows the cycle prompt for clients and advances the selection to the previous
client. If the cycle prompt is already visible, then the selection is advanced
to the previous client.

OnlyActiveWorkspace specifies that only clients on the current workspace should
be listed. Valid values are "yes" or "no".

OnlyVisible specifies that only clients on visible workspaces should be listed.
Valid values are "yes" or "no".

ShowIconified specifies that iconified clients will be shown. Valid values are
"yes" or "no".
        '''
        self._assert_arg_type('OnlyActiveWorkspace', OnlyActiveWorkspace, [basestring])
        self._assert_arg_type('OnlyVisible', OnlyVisible, [basestring])
        self._assert_arg_type('ShowIconified', ShowIconified, [basestring])

        arg_str = self._gribble_arg_str([OnlyActiveWorkspace, OnlyVisible, ShowIconified])
        val = self.gribble('CycleClientPrev %s' % arg_str)
        return self._from_str('CycleClientPrev', val)

    def Dale(self):
        '''
Make sure "audio_play_cmd" is set to a program that can play wav files.
        '''

        arg_str = self._gribble_arg_str([])
        val = self.gribble('Dale %s' % arg_str)
        return self._from_str('Dale', val)

    def Deiconify(self, Client):
        '''
Deiconifies (unminimizes) the window specified by Client. If the window
is already deiconified, this command has no effect.

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Client', Client, [int, basestring])

        arg_str = self._gribble_arg_str([Client])
        val = self.gribble('Deiconify %s' % arg_str)
        return self._from_str('Deiconify', val)

    def False(self):
        '''
Always returns 0.
        '''

        arg_str = self._gribble_arg_str([])
        val = self.gribble('False %s' % arg_str)
        return self._from_str('False', val)

    def Float(self, Client):
        '''
Floats the window specified by Client. If the window is already floating,
this command has no effect.

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Client', Client, [int, basestring])

        arg_str = self._gribble_arg_str([Client])
        val = self.gribble('Float %s' % arg_str)
        return self._from_str('Float', val)

    def Focus(self, Client):
        '''
Focuses the window specified by Client.

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Client', Client, [int, basestring])

        arg_str = self._gribble_arg_str([Client])
        val = self.gribble('Focus %s' % arg_str)
        return self._from_str('Focus', val)

    def FocusRaise(self, Client):
        '''
Focuses and raises the window specified by Client.

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Client', Client, [int, basestring])

        arg_str = self._gribble_arg_str([Client])
        val = self.gribble('FocusRaise %s' % arg_str)
        return self._from_str('FocusRaise', val)

    def FrameBorders(self, Client):
        '''
Set the decorations of the window specified by Client to the "Borders" frame.

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Client', Client, [int, basestring])

        arg_str = self._gribble_arg_str([Client])
        val = self.gribble('FrameBorders %s' % arg_str)
        return self._from_str('FrameBorders', val)

    def FrameFull(self, Client):
        '''
Set the decorations of the window specified by Client to the "Full" frame.

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Client', Client, [int, basestring])

        arg_str = self._gribble_arg_str([Client])
        val = self.gribble('FrameFull %s' % arg_str)
        return self._from_str('FrameFull', val)

    def FrameNada(self, Client):
        '''
Set the decorations of the window specified by Client to the "Nada" frame.

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Client', Client, [int, basestring])

        arg_str = self._gribble_arg_str([Client])
        val = self.gribble('FrameNada %s' % arg_str)
        return self._from_str('FrameNada', val)

    def FrameSlim(self, Client):
        '''
Set the decorations of the window specified by Client to the "Slim" frame.

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Client', Client, [int, basestring])

        arg_str = self._gribble_arg_str([Client])
        val = self.gribble('FrameSlim %s' % arg_str)
        return self._from_str('FrameSlim', val)

    def GetActive(self):
        '''
Returns the id of the currently active window. If there is no active window,
0 is returned.
        '''

        arg_str = self._gribble_arg_str([])
        val = self.gribble('GetActive %s' % arg_str)
        return self._from_str('GetActive', val)

    def GetAllClients(self):
        '''
Returns a list of all client ids separated by new lines. Clients are listed
in the order in which they were managed, starting with the oldest client.
        '''

        arg_str = self._gribble_arg_str([])
        val = self.gribble('GetAllClients %s' % arg_str)
        return self._from_str('GetAllClients', val)

    def GetClientHeight(self, Client):
        '''
Returns the height of the window specified by Client, including
decorations. If the client id is invalid, 0 is returned.

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Client', Client, [int, basestring])

        arg_str = self._gribble_arg_str([Client])
        val = self.gribble('GetClientHeight %s' % arg_str)
        return self._from_str('GetClientHeight', val)

    def GetClientList(self, Workspace):
        '''
Returns a list of client ids separated by new lines on the workspace specified
by Workspace. Clients are listed in their focus orderering, from most recently
focused to least recently focused.

Workspace may be a workspace index (integer) starting at 0, or a workspace
name.
        '''
        self._assert_arg_type('Workspace', Workspace, [int, basestring])

        arg_str = self._gribble_arg_str([Workspace])
        val = self.gribble('GetClientList %s' % arg_str)
        return self._from_str('GetClientList', val)

    def GetClientName(self, Client):
        '''
Returns the name of the window specified by Client active window.

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Client', Client, [int, basestring])

        arg_str = self._gribble_arg_str([Client])
        val = self.gribble('GetClientName %s' % arg_str)
        return self._from_str('GetClientName', val)

    def GetClientStatesList(self, Client):
        '''
Returns a list of states that the client is in. These states are in
correspondence with the possible values of the _NET_WM_STATE property.
The following states may appear in the list: STICKY, MAXIMIZED_VERT,
MAXIMIZED_HORZ, SKIP_TASKBAR, SKIP_PAGER, HIDDEN, FULLSCREEN,
ABOVE, BELOW, DEMANDS_ATTENTION and FOCUSED.

More details can be found here: http://goo.gl/FHdjl

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Client', Client, [int, basestring])

        arg_str = self._gribble_arg_str([Client])
        val = self.gribble('GetClientStatesList %s' % arg_str)
        return self._from_str('GetClientStatesList', val)

    def GetClientType(self, Client):
        '''
Returns the type of the window specified by Client active window. A window
type will either be "desktop", "dock" or "normal".

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Client', Client, [int, basestring])

        arg_str = self._gribble_arg_str([Client])
        val = self.gribble('GetClientType %s' % arg_str)
        return self._from_str('GetClientType', val)

    def GetClientWidth(self, Client):
        '''
Returns the width of the window specified by Client, including
decorations. If the client id is invalid, 0 is returned.

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Client', Client, [int, basestring])

        arg_str = self._gribble_arg_str([Client])
        val = self.gribble('GetClientWidth %s' % arg_str)
        return self._from_str('GetClientWidth', val)

    def GetClientWorkspace(self, Client):
        '''
Returns the workspace of the window specified by Client active window.

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Client', Client, [int, basestring])

        arg_str = self._gribble_arg_str([Client])
        val = self.gribble('GetClientWorkspace %s' % arg_str)
        return self._from_str('GetClientWorkspace', val)

    def GetClientX(self, Client):
        '''
Returns the relative X position of the window specified by Client, where the X
position refers to the left-most region of the window, including
decorations. Note that "relative" in this case refers to the workspace
that the client is on.

Relative positions can be used as arguments to MoveRelative.

If the client id is invalid, or the client is not visible, -9999 is returned.

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Client', Client, [int, basestring])

        arg_str = self._gribble_arg_str([Client])
        val = self.gribble('GetClientX %s' % arg_str)
        return self._from_str('GetClientX', val)

    def GetClientY(self, Client):
        '''
Returns the relative Y position of the window specified by Client, where the Y
position refers to the left-most region of the window, including
decorations. Note that "relative" in this case refers to the workspace
that the client is on.

Relative positions can be used as arguments to MoveRelative.

If the client id is invalid, or the client is not visible, -9999 is returned.

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Client', Client, [int, basestring])

        arg_str = self._gribble_arg_str([Client])
        val = self.gribble('GetClientY %s' % arg_str)
        return self._from_str('GetClientY', val)

    def GetHead(self):
        '''
Returns the index of the current head. Indexing starts at 0. Heads are ordered
by their physical position: left to right and then top to bottom.
        '''

        arg_str = self._gribble_arg_str([])
        val = self.gribble('GetHead %s' % arg_str)
        return self._from_str('GetHead', val)

    def GetHeadHeight(self, Head):
        '''
Gets the workable height of the head indexed at Head. If the head specified
is not visible, then 0 is returned.

Indexing starts at 0. Heads are ordered by their physical position: left to
right and then top to bottom.
        '''
        self._assert_arg_type('Head', Head, [int])

        arg_str = self._gribble_arg_str([Head])
        val = self.gribble('GetHeadHeight %s' % arg_str)
        return self._from_str('GetHeadHeight', val)

    def GetHeadWidth(self, Head):
        '''
Gets the workable width of the head indexed at Head. If the head specified
is not visible, then 0 is returned.

Indexing starts at 0. Heads are ordered by their physical position: left to
right and then top to bottom.
        '''
        self._assert_arg_type('Head', Head, [int])

        arg_str = self._gribble_arg_str([Head])
        val = self.gribble('GetHeadWidth %s' % arg_str)
        return self._from_str('GetHeadWidth', val)

    def GetHeadWorkspace(self, Head):
        '''
Returns the name of the workspace currently visible on the monitor indexed by
Head. Indexing starts at 0. Heads are ordered by their physical position:
left to right and then top to bottom.
        '''
        self._assert_arg_type('Head', Head, [int])

        arg_str = self._gribble_arg_str([Head])
        val = self.gribble('GetHeadWorkspace %s' % arg_str)
        return self._from_str('GetHeadWorkspace', val)

    def GetLayout(self, Workspace):
        '''
Returns the name of the currently active (or "default") layout on the workspace
specified by Workspace. Note that when a workspace is set to a tiling layout,
it is still possible for clients to be floating.

Workspace may be a workspace index (integer) starting at 0, or a workspace
name.
        '''
        self._assert_arg_type('Workspace', Workspace, [int, basestring])

        arg_str = self._gribble_arg_str([Workspace])
        val = self.gribble('GetLayout %s' % arg_str)
        return self._from_str('GetLayout', val)

    def GetNumHeads(self):
        '''
Returns the number of active Heads.
        '''

        arg_str = self._gribble_arg_str([])
        val = self.gribble('GetNumHeads %s' % arg_str)
        return self._from_str('GetNumHeads', val)

    def GetNumHeadsConnected(self):
        '''
Returns the number of Heads connected. This number may be greater
than the number returned by GetNumHeads.
        '''

        arg_str = self._gribble_arg_str([])
        val = self.gribble('GetNumHeadsConnected %s' % arg_str)
        return self._from_str('GetNumHeadsConnected', val)

    def GetWorkspace(self):
        '''
Returns the name of the current workspace.
        '''

        arg_str = self._gribble_arg_str([])
        val = self.gribble('GetWorkspace %s' % arg_str)
        return self._from_str('GetWorkspace', val)

    def GetWorkspaceId(self, Workspace):
        '''
Returns the id (the index) of the workspace specified by Workspace.

Workspace may be a workspace index (integer) starting at 0, or a workspace
name.
        '''
        self._assert_arg_type('Workspace', Workspace, [int, basestring])

        arg_str = self._gribble_arg_str([Workspace])
        val = self.gribble('GetWorkspaceId %s' % arg_str)
        return self._from_str('GetWorkspaceId', val)

    def GetWorkspaceList(self):
        '''
Returns a list of all workspaces, in the order that they were added.

The special "Sticky" workspace is not included.
        '''

        arg_str = self._gribble_arg_str([])
        val = self.gribble('GetWorkspaceList %s' % arg_str)
        return self._from_str('GetWorkspaceList', val)

    def GetWorkspaceNext(self):
        '''
Returns the name of the "next" workspace. The ordering of workspaces is
the order in which they were added. This might cause confusing behavior in
multi-head setups, since multiple workspaces can be viewable at one time.
        '''

        arg_str = self._gribble_arg_str([])
        val = self.gribble('GetWorkspaceNext %s' % arg_str)
        return self._from_str('GetWorkspaceNext', val)

    def GetWorkspacePrefix(self, Prefix):
        '''
Returns the first non-visible workspace starting with Prefix. If the current
workspace starts with Prefix, then the first workspace *after* the current
workspace starting with Prefix will be returned.
        '''
        self._assert_arg_type('Prefix', Prefix, [basestring])

        arg_str = self._gribble_arg_str([Prefix])
        val = self.gribble('GetWorkspacePrefix %s' % arg_str)
        return self._from_str('GetWorkspacePrefix', val)

    def GetWorkspacePrev(self):
        '''
Returns the name of the "previous" workspace. The ordering of workspaces is
the order in which they were added. This might cause confusing behavior in
multi-head setups, since multiple workspaces can be viewable at one time.
        '''

        arg_str = self._gribble_arg_str([])
        val = self.gribble('GetWorkspacePrev %s' % arg_str)
        return self._from_str('GetWorkspacePrev', val)

    def HeadCycle(self):
        '''
Cycles focus to the next head, ordered by index. Heads are ordered
by their physical position: left to right and then top to bottom.
        '''

        arg_str = self._gribble_arg_str([])
        val = self.gribble('HeadCycle %s' % arg_str)
        return self._from_str('HeadCycle', val)

    def HeadFocus(self, Head):
        '''
Focuses the head indexed at Head. Indexing starts at 0. Heads are ordered
by their physical position: left to right and then top to bottom.
        '''
        self._assert_arg_type('Head', Head, [int])

        arg_str = self._gribble_arg_str([Head])
        val = self.gribble('HeadFocus %s' % arg_str)
        return self._from_str('HeadFocus', val)

    def HeadFocusWithClient(self, Head, Client):
        '''
Focuses the head indexed at Head, and move the Client specified by client to
that head. Indexing of heads starts at 0. Heads are ordered by their physical
position: left to right and then top to bottom.

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Head', Head, [int])
        self._assert_arg_type('Client', Client, [int, basestring])

        arg_str = self._gribble_arg_str([Head, Client])
        val = self.gribble('HeadFocusWithClient %s' % arg_str)
        return self._from_str('HeadFocusWithClient', val)

    def HideClientFromPanels(self, Client):
        '''
Sets the appropriate flags so that the window specified by Client is
hidden from panels and pagers.

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Client', Client, [int, basestring])

        arg_str = self._gribble_arg_str([Client])
        val = self.gribble('HideClientFromPanels %s' % arg_str)
        return self._from_str('HideClientFromPanels', val)

    def Iconify(self, Client):
        '''
Iconifies (minimizes) the window specified by Client. If the window
is already iconified, this command has no effect.

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Client', Client, [int, basestring])

        arg_str = self._gribble_arg_str([Client])
        val = self.gribble('Iconify %s' % arg_str)
        return self._from_str('Iconify', val)

    def Input(self, Label):
        '''
Shows a centered prompt window that allows the user to type in text. If the
user presses the Confirm Key (i.e., enter), then the text typed into the
input box will be returned.

Label will be shown next to the input box.

This command may be used as a sub-command to pass user provided arguments to
another command.
        '''
        self._assert_arg_type('Label', Label, [basestring])

        arg_str = self._gribble_arg_str([Label])
        val = self.gribble('Input %s' % arg_str)
        return self._from_str('Input', val)

    def MatchClientClass(self, Client, Class):
        '''
Returns 1 if the "class" part of the WM_CLASS property on the window
specified by Client contains the substring specified by Class, and otherwise
returns 0. The search is done case insensitively.

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Client', Client, [int, basestring])
        self._assert_arg_type('Class', Class, [basestring])

        arg_str = self._gribble_arg_str([Client, Class])
        val = self.gribble('MatchClientClass %s' % arg_str)
        return self._from_str('MatchClientClass', val)

    def MatchClientInstance(self, Client, Instance):
        '''
Returns 1 if the "instance" part of the WM_CLASS property on the window
specified by Client contains the substring specified by Instance, and otherwise
returns 0. The search is done case insensitively.

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Client', Client, [int, basestring])
        self._assert_arg_type('Instance', Instance, [basestring])

        arg_str = self._gribble_arg_str([Client, Instance])
        val = self.gribble('MatchClientInstance %s' % arg_str)
        return self._from_str('MatchClientInstance', val)

    def MatchClientIsTransient(self, Client):
        '''
Returns 1 if the window specified by Client is a transient window, and
otherwise returns 0. A transient window usually corresponds to some kind of
dialog window.

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Client', Client, [int, basestring])

        arg_str = self._gribble_arg_str([Client])
        val = self.gribble('MatchClientIsTransient %s' % arg_str)
        return self._from_str('MatchClientIsTransient', val)

    def MatchClientMapped(self, Client):
        '''
Returns 1 if the window specified by Client is mapped or not.

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Client', Client, [int, basestring])

        arg_str = self._gribble_arg_str([Client])
        val = self.gribble('MatchClientMapped %s' % arg_str)
        return self._from_str('MatchClientMapped', val)

    def MatchClientName(self, Client, Name):
        '''
Returns 1 if the name of the window specified by Client contains the substring
specified by Name, and otherwise returns 0. The search is done case
insensitively.

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Client', Client, [int, basestring])
        self._assert_arg_type('Name', Name, [basestring])

        arg_str = self._gribble_arg_str([Client, Name])
        val = self.gribble('MatchClientName %s' % arg_str)
        return self._from_str('MatchClientName', val)

    def MatchClientType(self, Client, Type):
        '''
Returns 1 if the type of the window specified by Client matches the type
named by Type, and otherwise returns 0.

Valid window types are "Normal", "Dock" or "Desktop".

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Client', Client, [int, basestring])
        self._assert_arg_type('Type', Type, [basestring])

        arg_str = self._gribble_arg_str([Client, Type])
        val = self.gribble('MatchClientType %s' % arg_str)
        return self._from_str('MatchClientType', val)

    def Maximize(self, Client):
        '''
Maximizes the window specified by Client. If the window is already maximized,
this command has no effect.

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Client', Client, [int, basestring])

        arg_str = self._gribble_arg_str([Client])
        val = self.gribble('Maximize %s' % arg_str)
        return self._from_str('Maximize', val)

    def Message(self, Text):
        '''
Shows a centered prompt window with the text specified by Text. The message
will not disappear until it loses focus or when the confirm or cancel key
is pressed.
        '''
        self._assert_arg_type('Text', Text, [basestring])

        arg_str = self._gribble_arg_str([Text])
        val = self.gribble('Message %s' % arg_str)
        return self._from_str('Message', val)

    def MouseMove(self):
        '''
Initiates a drag that allows a window to be moved with the mouse.

This is a special command that can only be assigned in Wingo's mouse
configuration file. Invoking this command in any other way has no effect.
        '''

        arg_str = self._gribble_arg_str([])
        val = self.gribble('MouseMove %s' % arg_str)
        return self._from_str('MouseMove', val)

    def MouseResize(self, Direction):
        '''
Initiates a drag that allows a window to be resized with the mouse.

Direction specifies how the window should be resized, and what the pointer
should look like. For example, if Direction is set to "BottomRight", then only
the width and height of the window can change---but not the x or y position.

Valid values for Direction are: Infer, Top, Bottom, Left, Right, TopLeft,
TopRight, BottomLeft and BottomRight. When "Infer" is used, the direction
is determined based on where the pointer is on the window when the drag is
initiated.

This is a special command that can only be assigned in Wingo's mouse
configuration file. Invoking this command in any other way has no effect.
        '''
        self._assert_arg_type('Direction', Direction, [basestring])

        arg_str = self._gribble_arg_str([Direction])
        val = self.gribble('MouseResize %s' % arg_str)
        return self._from_str('MouseResize', val)

    def Move(self, Client, X, Y):
        '''
Moves the window specified by Client to the x and y position specified by
X and Y. Note that the origin is located in the top left corner.

X and Y may either be pixels (integers) or ratios in the range 0.0 to
1.0 (specifically, (0.0, 1.0]). Ratios are measured with respect to the
window's workspace's geometry.

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Client', Client, [int, basestring])
        self._assert_arg_type('X', X, [float, int])
        self._assert_arg_type('Y', Y, [float, int])

        arg_str = self._gribble_arg_str([Client, X, Y])
        val = self.gribble('Move %s' % arg_str)
        return self._from_str('Move', val)

    def MovePointer(self, X, Y):
        '''
Moves the pointer to the x and y position specified by X and Y. Note the the
origin is located in the top left corner.
        '''
        self._assert_arg_type('X', X, [int])
        self._assert_arg_type('Y', Y, [int])

        arg_str = self._gribble_arg_str([X, Y])
        val = self.gribble('MovePointer %s' % arg_str)
        return self._from_str('MovePointer', val)

    def MovePointerRelative(self, X, Y):
        '''
Moves the pointer to the x and y position specified by X and Y relative to the
current workspace. Note the the origin is located in the top left corner of
the current workspace.

X and Y may either be pixels (integers) or ratios in the range 0.0 to
1.0 (specifically, (0.0, 1.0]). Ratios are measured with respect to the
workspace's geometry.
        '''
        self._assert_arg_type('X', X, [float, int])
        self._assert_arg_type('Y', Y, [float, int])

        arg_str = self._gribble_arg_str([X, Y])
        val = self.gribble('MovePointerRelative %s' % arg_str)
        return self._from_str('MovePointerRelative', val)

    def MoveRelative(self, Client, X, Y):
        '''
Moves the window specified by Client to the x and y position specified by
X and Y, relative to its workspace. Note that the origin is located in the top
left corner of the client's workspace.

X and Y may either be pixels (integers) or ratios in the range 0.0 to
1.0 (specifically, (0.0, 1.0]). Ratios are measured with respect to the
window's workspace's geometry.

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Client', Client, [int, basestring])
        self._assert_arg_type('X', X, [float, int])
        self._assert_arg_type('Y', Y, [float, int])

        arg_str = self._gribble_arg_str([Client, X, Y])
        val = self.gribble('MoveRelative %s' % arg_str)
        return self._from_str('MoveRelative', val)

    def Not(self, Op):
        '''
Returns the negation of Op. When Op is 0, Not returns 1. When Op is 1, Not
returns 0.

If Op is not in {0, 1}, then a warning is logged and nil is returned.
        '''
        self._assert_arg_type('Op', Op, [int])

        arg_str = self._gribble_arg_str([Op])
        val = self.gribble('Not %s' % arg_str)
        return self._from_str('Not', val)

    def Or(self, Op1, Op2):
        '''
Returns the logical OR of Op1 and Op2.

If Op1 or Op2 is not in {0, 1}, then a warning is logged and nil is returned.
        '''
        self._assert_arg_type('Op1', Op1, [int])
        self._assert_arg_type('Op2', Op2, [int])

        arg_str = self._gribble_arg_str([Op1, Op2])
        val = self.gribble('Or %s' % arg_str)
        return self._from_str('Or', val)

    def Quit(self):
        '''
Stops Wingo.
        '''

        arg_str = self._gribble_arg_str([])
        val = self.gribble('Quit %s' % arg_str)
        return self._from_str('Quit', val)

    def Raise(self, Client):
        '''
Raises the window specified by Client to the top of its layer.

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Client', Client, [int, basestring])

        arg_str = self._gribble_arg_str([Client])
        val = self.gribble('Raise %s' % arg_str)
        return self._from_str('Raise', val)

    def RemoveWorkspace(self, Workspace):
        '''
Removes the workspace specified by Workspace. Note that a workspace can *only*
be removed if it is empty (i.e., does not contain any windows).

Workspace may be a workspace index (integer) starting at 0, or a workspace
name.
        '''
        self._assert_arg_type('Workspace', Workspace, [int, basestring])

        arg_str = self._gribble_arg_str([Workspace])
        val = self.gribble('RemoveWorkspace %s' % arg_str)
        return self._from_str('RemoveWorkspace', val)

    def RenameWorkspace(self, Workspace, NewName):
        '''
Renames the workspace specified by Workspace to the name in NewName.

Workspace may be a workspace index (integer) starting at 0, or a workspace
name.
NewName can only be a string.
        '''
        self._assert_arg_type('Workspace', Workspace, [int, basestring])
        self._assert_arg_type('NewName', NewName, [basestring])

        arg_str = self._gribble_arg_str([Workspace, NewName])
        val = self.gribble('RenameWorkspace %s' % arg_str)
        return self._from_str('RenameWorkspace', val)

    def Resize(self, Client, Width, Height):
        '''
Resizes the window specified by Client to some width and height specified by
Width and Height.

Width and Height may either be pixels (integers) or ratios in the range 0.0 to
1.0 (specifically, (0.0, 1.0]). Ratios are measured with respect to the
window's workspace's geometry.

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Client', Client, [int, basestring])
        self._assert_arg_type('Width', Width, [float, int])
        self._assert_arg_type('Height', Height, [float, int])

        arg_str = self._gribble_arg_str([Client, Width, Height])
        val = self.gribble('Resize %s' % arg_str)
        return self._from_str('Resize', val)

    def Restart(self):
        '''
Restarts Wingo in place using exec. This should be used to reload Wingo
after you've made changes to its configuration.
        '''

        arg_str = self._gribble_arg_str([])
        val = self.gribble('Restart %s' % arg_str)
        return self._from_str('Restart', val)

    def Script(self, Command):
        '''
Executes a script in $XDG_CONFIG_HOME/wingo/scripts. The command
may include arguments.
        '''
        self._assert_arg_type('Command', Command, [basestring])

        arg_str = self._gribble_arg_str([Command])
        val = self.gribble('Script %s' % arg_str)
        return self._from_str('Script', val)

    def ScriptConfig(self, ScriptName):
        '''
Returns the path to a script's configuration file.
        '''
        self._assert_arg_type('ScriptName', ScriptName, [basestring])

        arg_str = self._gribble_arg_str([ScriptName])
        val = self.gribble('ScriptConfig %s' % arg_str)
        return self._from_str('ScriptConfig', val)

    def SelectClient(self, TabCompletion, OnlyActiveWorkspace, OnlyVisible, ShowIconified):
        '''
Shows a centered prompt window with a list of clients satisfying the arguments
provided.

OnlyActiveWorkspace specifies that only clients on the current workspace should
be listed. Valid values are "yes" or "no".

OnlyVisible specifies that only clients on visible workspaces should be listed.
Valid values are "yes" or "no".

ShowIconified specifies that iconified clients will be shown. Valid values are
"yes" or "no".

TabCompletetion can be set to either "Prefix", "Any" or "Multiple". When it's
set to "Prefix", the clients can be searched by a prefix matching string. When
it's set to "Any", the clients can be searched by a substring matching string.
When it's set to "Multiple", the clients can be searched by multiple space-
separated substring matching strings.

This command may be used as a sub-command to pass a particular client to
another command.
        '''
        self._assert_arg_type('TabCompletion', TabCompletion, [basestring])
        self._assert_arg_type('OnlyActiveWorkspace', OnlyActiveWorkspace, [basestring])
        self._assert_arg_type('OnlyVisible', OnlyVisible, [basestring])
        self._assert_arg_type('ShowIconified', ShowIconified, [basestring])

        arg_str = self._gribble_arg_str([TabCompletion, OnlyActiveWorkspace, OnlyVisible, ShowIconified])
        val = self.gribble('SelectClient %s' % arg_str)
        return self._from_str('SelectClient', val)

    def SelectWorkspace(self, TabCompletion):
        '''
Shows a centered prompt window with a list of all workspaces.

TabCompletetion can be set to either "Prefix", "Any" or "Multiple". When it's
set to "Prefix", the clients can be searched by a prefix matching string. When
it's set to "Any", the clients can be searched by a substring matching string.
When it's set to "Multiple", the clients can be searched by multiple space-
separated substring matching strings.

This command may be used as a sub-command to pass a particular workspace to
another command.
        '''
        self._assert_arg_type('TabCompletion', TabCompletion, [basestring])

        arg_str = self._gribble_arg_str([TabCompletion])
        val = self.gribble('SelectWorkspace %s' % arg_str)
        return self._from_str('SelectWorkspace', val)

    def SetLayout(self, Workspace, Name):
        '''
Sets the current layout of the workspace specified by Workspace to the layout
named by Name. If a layout with name Name does not exist, this command has
no effect.

Note that this command has no effect if the workspace is not visible.

Workspace may be a workspace index (integer) starting at 0, or a workspace
name.
        '''
        self._assert_arg_type('Workspace', Workspace, [int, basestring])
        self._assert_arg_type('Name', Name, [basestring])

        arg_str = self._gribble_arg_str([Workspace, Name])
        val = self.gribble('SetLayout %s' % arg_str)
        return self._from_str('SetLayout', val)

    def SetOpacity(self, Client, Opacity):
        '''
Sets the opacity of the window specified by Client to the opacity level
specified by Opacity.

This command won't have any effect unless you're running a compositing manager
like compton or cairo-compmgr.

Client may be the window id or a substring that matches a window name.

Opacity should be a float in the range 0.0 to 1.0, inclusive, where 0.0 is
completely transparent and 1.0 is completely opaque.
        '''
        self._assert_arg_type('Client', Client, [int, basestring])
        self._assert_arg_type('Opacity', Opacity, [float])

        arg_str = self._gribble_arg_str([Client, Opacity])
        val = self.gribble('SetOpacity %s' % arg_str)
        return self._from_str('SetOpacity', val)

    def Shell(self, Command):
        '''
Attempts to execute the shell command specified by Command. If an error occurs,
it will be logged to Wingo's stderr.
        '''
        self._assert_arg_type('Command', Command, [basestring])

        arg_str = self._gribble_arg_str([Command])
        val = self.gribble('Shell %s' % arg_str)
        return self._from_str('Shell', val)

    def ShowClientInPanels(self, Client):
        '''
Sets the appropriate flags so that the window specified by Client is
shown on panels and pagers.

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Client', Client, [int, basestring])

        arg_str = self._gribble_arg_str([Client])
        val = self.gribble('ShowClientInPanels %s' % arg_str)
        return self._from_str('ShowClientInPanels', val)

    def TagGet(self, Client, Name):
        '''
Retrieves the tag with name Name for the client specified by Client.

Client may be the window id or a substring that matches a window name.
Or, it may be zero and the property will be retrieved from the root
window.

Tag names may only contain the following characters: [-a-zA-Z0-9_].
        '''
        self._assert_arg_type('Client', Client, [int, basestring])
        self._assert_arg_type('Name', Name, [basestring])

        arg_str = self._gribble_arg_str([Client, Name])
        val = self.gribble('TagGet %s' % arg_str)
        return self._from_str('TagGet', val)

    def TagSet(self, Client, Name, Value):
        '''
Sets the tag with name Name to value Value for the client specified by Client.

Client may be the window id or a substring that matches a window name.
Or, it may be zero and the property will be set on the root window.

Tag names may only contain the following characters: [-a-zA-Z0-9_].
        '''
        self._assert_arg_type('Client', Client, [int, basestring])
        self._assert_arg_type('Name', Name, [basestring])
        self._assert_arg_type('Value', Value, [basestring])

        arg_str = self._gribble_arg_str([Client, Name, Value])
        val = self.gribble('TagSet %s' % arg_str)
        return self._from_str('TagSet', val)

    def ToggleFloating(self, Client):
        '''
Toggles whether the window specified by Client should be forced into the
floating layout. A window forced into the floating layout CANNOT be tiled.

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Client', Client, [int, basestring])

        arg_str = self._gribble_arg_str([Client])
        val = self.gribble('ToggleFloating %s' % arg_str)
        return self._from_str('ToggleFloating', val)

    def ToggleIconify(self, Client):
        '''
Iconifies (minimizes) or deiconifies (unminimizes) the window specified by
Client.

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Client', Client, [int, basestring])

        arg_str = self._gribble_arg_str([Client])
        val = self.gribble('ToggleIconify %s' % arg_str)
        return self._from_str('ToggleIconify', val)

    def ToggleMaximize(self, Client):
        '''
Maximizes or restores the window specified by Client.

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Client', Client, [int, basestring])

        arg_str = self._gribble_arg_str([Client])
        val = self.gribble('ToggleMaximize %s' % arg_str)
        return self._from_str('ToggleMaximize', val)

    def ToggleStackAbove(self, Client):
        '''
Toggles the layer of the window specified by Client from normal to above. When
a window is in the "above" layer, it will always be above other (normal)
clients.

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Client', Client, [int, basestring])

        arg_str = self._gribble_arg_str([Client])
        val = self.gribble('ToggleStackAbove %s' % arg_str)
        return self._from_str('ToggleStackAbove', val)

    def ToggleStackBelow(self, Client):
        '''
Toggles the layer of the window specified by Client from normal to below. When
a window is in the "below" layer, it will always be below other (normal)
clients.

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Client', Client, [int, basestring])

        arg_str = self._gribble_arg_str([Client])
        val = self.gribble('ToggleStackBelow %s' % arg_str)
        return self._from_str('ToggleStackBelow', val)

    def ToggleSticky(self, Client):
        '''
Toggles the sticky status of the window specified by Client. When a window is
sticky, it will always be visible unless iconified. (i.e., it does not belong
to any particular workspace.)

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Client', Client, [int, basestring])

        arg_str = self._gribble_arg_str([Client])
        val = self.gribble('ToggleSticky %s' % arg_str)
        return self._from_str('ToggleSticky', val)

    def True(self):
        '''
Always returns 1.
        '''

        arg_str = self._gribble_arg_str([])
        val = self.gribble('True %s' % arg_str)
        return self._from_str('True', val)

    def Unfloat(self, Client):
        '''
Unfloats the window specified by Client. If the window is not floating,
this command has no effect.

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Client', Client, [int, basestring])

        arg_str = self._gribble_arg_str([Client])
        val = self.gribble('Unfloat %s' % arg_str)
        return self._from_str('Unfloat', val)

    def Unmaximize(self, Client):
        '''
Unmaximizes the window specified by Client. If the window is not maximized,
this command has no effect.

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Client', Client, [int, basestring])

        arg_str = self._gribble_arg_str([Client])
        val = self.gribble('Unmaximize %s' % arg_str)
        return self._from_str('Unmaximize', val)

    def WingoExec(self, Commands):
        '''
Executes a series of Wingo commands specified by Commands. If an error occurs
while executing the command, it will be shown in a popup message.
        '''
        self._assert_arg_type('Commands', Commands, [basestring])

        arg_str = self._gribble_arg_str([Commands])
        val = self.gribble('WingoExec %s' % arg_str)
        return self._from_str('WingoExec', val)

    def WingoHelp(self, CommandName):
        '''
Shows the usage information for a particular command specified by CommandName.
        '''
        self._assert_arg_type('CommandName', CommandName, [basestring])

        arg_str = self._gribble_arg_str([CommandName])
        val = self.gribble('WingoHelp %s' % arg_str)
        return self._from_str('WingoHelp', val)

    def Workspace(self, Workspace):
        '''
Sets the current workspace to the one specified by Workspace.

Workspace may be a workspace index (integer) starting at 0, or a workspace
name.
        '''
        self._assert_arg_type('Workspace', Workspace, [int, basestring])

        arg_str = self._gribble_arg_str([Workspace])
        val = self.gribble('Workspace %s' % arg_str)
        return self._from_str('Workspace', val)

    def WorkspaceGreedy(self, Workspace):
        '''
Sets the current workspace to the one specified by Workspace in a greedy
fashion.

A greedy switch *always* brings the specified workspace to the
currently focused head. (N.B. Greedy is only different when switching between
two visible workspaces.)

Workspace may be a workspace index (integer) starting at 0, or a workspace
name.
        '''
        self._assert_arg_type('Workspace', Workspace, [int, basestring])

        arg_str = self._gribble_arg_str([Workspace])
        val = self.gribble('WorkspaceGreedy %s' % arg_str)
        return self._from_str('WorkspaceGreedy', val)

    def WorkspaceGreedyWithClient(self, Workspace, Client):
        '''
Sets the current workspace to the workspace specified by Workspace in a greedy
fashion, and moves the window specified by Client to that workspace.

A greedy switch *always* brings the specified workspace to the
currently focused head. (N.B. Greedy is only different when switching between
two visible workspaces.)

Workspace may be a workspace index (integer) starting at 0, or a workspace
name.

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Workspace', Workspace, [int, basestring])
        self._assert_arg_type('Client', Client, [int, basestring])

        arg_str = self._gribble_arg_str([Workspace, Client])
        val = self.gribble('WorkspaceGreedyWithClient %s' % arg_str)
        return self._from_str('WorkspaceGreedyWithClient', val)

    def WorkspaceHead(self, Workspace):
        '''
Retrieves the head index of the workspace specified by Workspace. If the
workspace is not visible, then -1 is returned.

Head indexing starts at 0. Heads are ordered by their physical position: left
to right and then top to bottom.

Workspace may be a workspace index (integer) starting at 0, or a workspace
name.
        '''
        self._assert_arg_type('Workspace', Workspace, [int, basestring])

        arg_str = self._gribble_arg_str([Workspace])
        val = self.gribble('WorkspaceHead %s' % arg_str)
        return self._from_str('WorkspaceHead', val)

    def WorkspaceSendClient(self, Workspace, Client):
        '''
Sends the window specified by Client to the workspace specified by Workspace.

Workspace may be a workspace index (integer) starting at 0, or a workspace
name.

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Workspace', Workspace, [int, basestring])
        self._assert_arg_type('Client', Client, [int, basestring])

        arg_str = self._gribble_arg_str([Workspace, Client])
        val = self.gribble('WorkspaceSendClient %s' % arg_str)
        return self._from_str('WorkspaceSendClient', val)

    def WorkspaceToHead(self, Head, Workspace):
        '''
Sets the workspace specified by Workspace to appear on the head specified by
the Head index.

Workspace may be a workspace index (integer) starting at 0, or a workspace
name.

Head indexing starts at 0. Heads are ordered by their physical position: left
to right and then top to bottom.
        '''
        self._assert_arg_type('Head', Head, [int])
        self._assert_arg_type('Workspace', Workspace, [int, basestring])

        arg_str = self._gribble_arg_str([Head, Workspace])
        val = self.gribble('WorkspaceToHead %s' % arg_str)
        return self._from_str('WorkspaceToHead', val)

    def WorkspaceWithClient(self, Workspace, Client):
        '''
Sets the current workspace to the workspace specified by Workspace, and moves
the window specified by Client to that workspace.

Workspace may be a workspace index (integer) starting at 0, or a workspace
name.

Client may be the window id or a substring that matches a window name.
        '''
        self._assert_arg_type('Workspace', Workspace, [int, basestring])
        self._assert_arg_type('Client', Client, [int, basestring])

        arg_str = self._gribble_arg_str([Workspace, Client])
        val = self.gribble('WorkspaceWithClient %s' % arg_str)
        return self._from_str('WorkspaceWithClient', val)

