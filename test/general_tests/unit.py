import re

from deepthought.correction.units.c import CUnit

class Unit(CUnit):
	def run(self):
		self.ucopy(["solution.awk"], cd=True)
		if not self.execute("awk -F, -f solution.awk avocado.csv > user && diff user system", required_files=["solution.awk"], trace_output=True, trace_cmd=True, maxtime=30):
			self.comment("KO (Output Differs)")
			self.ko()
			return

		with open("test_output", "r") as fp:
			test_output = fp.read()

		if test_output == "[OK]\n":
			self.comment("OK")
			self.set_grade(100)
			self.ok()
		else:
			self.comment("KO")
			self.ko()
