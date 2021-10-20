from workplace import workplace # <- - - - - - - Workplace Function

# dont touch this stuff 

taskNum = 0 # <- - - - - Task Number
numtasks = 4 # <- - - - - Number of tasks, also edit files
variables = {}
perfect = True

for i in range(numtasks):
  # Argument formatting
  testCase = open(("tC/tC" + str(i) + ".in"), "r").read().splitlines()

  print("-------------------<test-case-" + str(i) + ">-------------------")
  variables["t{0}t".format(i)] = open(("tCA/tCA" + str(i) + ".out"), "r").read()

  variables["t{0}a".format(i)] = workplace(testCase)

  if variables["t{0}t".format(i)] == variables["t{0}a".format(i)]:
    print("              ##< TESTCASE SOLVED >##\n\n\n")
  else:
    print("                    you failed\n\n\n")
    perfect = False

if perfect == True:
  print("Congratulations! You successfully completed PY3_task_" + str(taskNum))
