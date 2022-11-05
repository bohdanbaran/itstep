import  inspect
import  requests

print(inspect.getmodule(requests.get))
print(inspect.getmodule(list))