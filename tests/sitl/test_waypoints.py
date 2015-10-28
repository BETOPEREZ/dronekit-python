import time
import math
from dronekit import connect, VehicleMode, LocationGlobal, Command
from dronekit.tools import with_sitl
from nose.tools import assert_not_equals

@with_sitl
def test_parameter(connpath):
    # Connect to the Vehicle
    vehicle = connect(connpath, await_params=True)

    cmds = vehicle.commands
    cmds.download()
    cmds.wait_valid()
    cmds.clear()
    vehicle.flush()

    print 'hi'

    # home
    cmds.download()
    cmds.wait_valid()

    for command in [
        Command(0, 0, 0, 0, 16, 1, 1, 0.0, 0.0, 0.0, 0.0, -35.3605, 149.172363, 747.0),
        Command(0, 0, 0, 3, 22, 0, 1, 0.0, 0.0, 0.0, 0.0, -35.359831, 149.166334, 100.0),
        Command(0, 0, 0, 3, 16, 0, 1, 0.0, 0.0, 0.0, 0.0, -35.363489, 149.167213, 100.0),
        Command(0, 0, 0, 3, 16, 0, 1, 0.0, 0.0, 0.0, 0.0, -35.355491, 149.169595, 100.0),
        Command(0, 0, 0, 3, 16, 0, 1, 0.0, 0.0, 0.0, 0.0, -35.355071, 149.175839, 100.0),
        Command(0, 0, 0, 3, 113, 0, 1, 0.0, 0.0, 0.0, 0.0, -35.362666, 149.178715, 22222.0),
        Command(0, 0, 0, 3, 115, 0, 1, 2.0, 22.0, 1.0, 3.0, 0.0, 0.0, 0.0),
        Command(0, 0, 0, 3, 16, 0, 1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
    ]:
        cmds.add(command)
    vehicle.flush()

    cmds.download()
    cmds.wait_valid()
    for cmd in cmds[1:]:  #skip first item as it is home waypoint.
        print(cmd)

    print(len(cmds))
