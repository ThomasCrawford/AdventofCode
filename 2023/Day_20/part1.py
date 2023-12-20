from queue import Queue

num_iterations =1000
filename = "input.txt"

class Module:
	pulse_queue = Queue()
	low_count = 0
	high_count = 0

	def __init__(self):
		self.name = ""
		self.connections = set()
		self.output_pulse = 'low'

	def add_connection(self, other_module):
		self.connections.add(other_module)
		# Conjunction Modules need to know what connect to them
		if isinstance(other_module, ConjunctionModule):
			other_module.add_input_connection(self)

	def add_name(self, name):
		self.name = name

	def send_pulse(self, pulse):
		for module in self.connections:
			Module.pulse_queue.put((module, pulse, self))
			# print(f"{self.name} wants to send a {pulse} pulse to {module.name}")

	@staticmethod
	def process_pulses():
		while not Module.pulse_queue.empty():			
			recipient, pulse, source = Module.pulse_queue.get()
			recipient.receive_pulse(pulse, source)
			if pulse == "low":
				Module.low_count +=1
			elif pulse == "high":
				Module.high_count += 1
			# print(f"{source.name} sent a {pulse} pulse to {recipient.name}")

class BroadcastModule(Module):
	def __init__(self):
		super().__init__()
		self.connections = set()
		self.output_pulse = 'low'


class FlipFlopModule(Module):
	def __init__(self):
		super().__init__()
		self.state = 'off'

	def receive_pulse(self, pulse, source):
		if pulse == 'low':
			self.state = 'on' if self.state == 'off' else 'off'
			self.send_pulse('high' if self.state == 'on' else 'low')


class ConjunctionModule(Module):
	def __init__(self):
		super().__init__()
		self.input_memory = {} #Now a dictionary

	def receive_pulse(self, pulse,source):
		self.input_memory[source.name] = pulse
		if all(memory == 'high' for memory in self.input_memory.values()):
			self.send_pulse('low')
		else:
			self.send_pulse('high')

	def add_input_connection(self, source_module):
		self.input_memory[source_module.name] = 'low'

class EndModule(Module): # only needs to be able to be sent a pulse
	def __init__(self):
		super().__init__()

	def receive_pulse(self, pulse,source):
		pass


# parse
module_registry = {}
connections_data = []
with open(filename) as file:
	for line in file:
		name, targets = line.split(" -> ")
		match name[0]:
			case "b":
				new_module = BroadcastModule()
			case "%":
				new_module = FlipFlopModule()
			case "&":
				new_module = ConjunctionModule()
		module_registry[name[1:]] = new_module
		new_module.name = name[1:]

		for target in targets.strip().split(","):
			target = target.strip()
			connections_data.append([name[1:],target])

for name, target in connections_data:
	if target not in module_registry:
		new_module = EndModule()
		EndModule.name = target
		module_registry[target] = new_module
	module_registry[name].add_connection(module_registry[target])


# Press start
for i in range(num_iterations):
	print(f"\nRound {i}:")
	module_registry["roadcaster"].send_pulse('low')
	Module.process_pulses()

print(Module.low_count+num_iterations,Module.high_count)
print((Module.low_count+num_iterations)*Module.high_count)





