import re
import sys
from com.xebialabs.xlrelease.plugin.overthere import RemoteScript

script = RemoteScript(task.pythonScript)
exitCode = script.execute()

output = script.getStdout()
err = script.getStderr()


if exitCode == 0:
    print output
else:
    print "Exit code "
    print exitCode
    print
    print "#### Output:"
    print output

    print "#### Error stream:"
    print err
    print
    print "----"

    if len(re.findall(successRegexp, output)) == 0:
        raise Exception(
            "Failed tests - the regular expression for a successful test suite execution was not found in the output"
        )

    sys.exit(exitCode)
