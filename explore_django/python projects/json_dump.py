import json

d={
    'course_name':'python',
    'fees':1500,
}
f=json.dumps(d)         # dictionary converted to json

print(type(f))
print(f)