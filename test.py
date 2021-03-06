from StyleRubric import StyleRubric
from json import dumps

s = StyleRubric()
# testnames = ['break_bad.cpp', 'operator_spacing_good.cpp', 'operator_spacing_bad.cpp',
#              'continue_good.cpp', 'continue_bad.cpp', 'goto_good.cpp', 'goto_bad.cpp',
#              'while_true_bad.cpp', 'while_true_good.cpp', 'bool_comp.cpp', 'class_main.cpp',
#              'compile_error.cpp']
testnames = ['prohibited_libs.cpp', 'ternary.cpp', 'line_length.cpp']
for filename in testnames:
    filename = 'test/' + filename
    s.gradeFile(filename)

# for filename, errors in s._fileErrors.iteritems():
#     print 'Grading {}...'.format(filename)
#     if len(errors) == 0:
#         print 'No errors found :D'
#     else:
#         for e in errors:
#             print '{0}:{1}:{2} {3}'.format(filename, e.lineNum, e.colNum, e.message)
#     print
print dumps(s.generateReport(), indent=4, separators=(',', ': '))