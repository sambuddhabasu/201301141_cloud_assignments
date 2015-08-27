#include <iostream>
#include <fstream>
using namespace std;
int main() {
	string registers[4] = {"eax", "ebx", "ecx", "edx"};
	string new_registers[4] = {"rax", "rbx", "rcx", "rdx"};
	int i, res;
	string::iterator iter;
	ifstream infile("32_bit.asm");
	ofstream outfile("64_bit.asm");
	for(string line; getline(infile, line);) {
		for(i=0; i<4; i++) {
			res = line.find(registers[i]);
			if(res!=-1) {
				line.replace(res, 3, new_registers[i]);
			}
		}
		outfile<<line<<endl;
	}
	return 0;
}
