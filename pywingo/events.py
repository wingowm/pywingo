from collections import namedtuple


def _new_Noop(j):
    assert j['EventName'] == 'Noop'
    return Noop()
Noop = namedtuple('Noop', [])


def _new_Restarting(j):
    assert j['EventName'] == 'Restarting'
    return Restarting()
Restarting = namedtuple('Restarting', [])


def _new_Subscribed(j):
    assert j['EventName'] == 'Subscribed'
    return Subscribed()
Subscribed = namedtuple('Subscribed', [])


def _new_ChangedWorkspace(j):
    assert j['EventName'] == 'ChangedWorkspace'
    return ChangedWorkspace()
ChangedWorkspace = namedtuple('ChangedWorkspace', [])


def _new_ChangedVisibleWorkspace(j):
    assert j['EventName'] == 'ChangedVisibleWorkspace'
    return ChangedVisibleWorkspace()
ChangedVisibleWorkspace = namedtuple('ChangedVisibleWorkspace', [])


def _new_ChangedWorkspaceNames(j):
    assert j['EventName'] == 'ChangedWorkspaceNames'
    return ChangedWorkspaceNames()
ChangedWorkspaceNames = namedtuple('ChangedWorkspaceNames', [])


def _new_AddedWorkspace(j):
    assert j['EventName'] == 'AddedWorkspace'
    return AddedWorkspace(j['Name'])
AddedWorkspace = namedtuple('AddedWorkspace', ['Name'])


def _new_RemovedWorkspace(j):
    assert j['EventName'] == 'RemovedWorkspace'
    return RemovedWorkspace(j['Name'])
RemovedWorkspace = namedtuple('RemovedWorkspace', ['Name'])


def _new_FocusedClient(j):
    assert j['EventName'] == 'FocusedClient'
    return FocusedClient(j['Id'])
FocusedClient = namedtuple('FocusedClient', ['Id'])


def _new_UnfocusedClient(j):
    assert j['EventName'] == 'UnfocusedClient'
    return UnfocusedClient(j['Id'])
UnfocusedClient = namedtuple('UnfocusedClient', ['Id'])


def _new_MappedClient(j):
    assert j['EventName'] == 'MappedClient'
    return MappedClient(j['Id'])
MappedClient = namedtuple('MappedClient', ['Id'])


def _new_UnmappedClient(j):
    assert j['EventName'] == 'UnmappedClient'
    return UnmappedClient(j['Id'])
UnmappedClient = namedtuple('UnmappedClient', ['Id'])


def _new_ManagedClient(j):
    assert j['EventName'] == 'ManagedClient'
    return ManagedClient(j['Id'])
ManagedClient = namedtuple('ManagedClient', ['Id'])


def _new_UnmanagedClient(j):
    assert j['EventName'] == 'UnmanagedClient'
    return UnmanagedClient(j['Id'], j['Name'], j['Workspace'], j['Class'], j['Instance'])
UnmanagedClient = namedtuple('UnmanagedClient', ['Id', 'Name', 'Workspace', 'Class', 'Instance'])


def _new_ChangedClientName(j):
    assert j['EventName'] == 'ChangedClientName'
    return ChangedClientName(j['Id'])
ChangedClientName = namedtuple('ChangedClientName', ['Id'])


def _new_ChangedActiveClient(j):
    assert j['EventName'] == 'ChangedActiveClient'
    return ChangedActiveClient(j['Id'])
ChangedActiveClient = namedtuple('ChangedActiveClient', ['Id'])


def _new_ChangedLayout(j):
    assert j['EventName'] == 'ChangedLayout'
    return ChangedLayout(j['Workspace'])
ChangedLayout = namedtuple('ChangedLayout', ['Workspace'])


