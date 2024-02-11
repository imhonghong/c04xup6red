//IEEE754 floating point to deciaml
#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main(){

	cout<<"transfer IEEE754 fp to decimal"<<endl;
	
	while(1){
		cout<<"SE-------F---------------------0"<<endl;
		string A;
		cin>>A;
		
		if(A=="00000000000000000000000000000000")
			cout<<"decimal: 0"<<endl<<endl;
			else{
			//convert string to array
			int Arr[32];
			for(int i=0; i<32 ; i++){
				Arr[i]=(A.at(i)-48);
				if(Arr[i]>1||Arr[i]<0){
					cout<<"invalid input"<<endl;
					return 0;
				}
			}
			
			//compute exponential 
			int E=-127;
			for(int e=0 ; e<8 ; e++){
				if(Arr[8-e])
					E=E+pow(2,e);
			}
			
			//compute fraction
			double DEC=1.0;
			for(int f=0 ; f<23 ; f++){
				if(Arr[31-f])
					DEC=DEC+pow(2,f-23);
			}
			//print E,F to check
			cout<<"expo=2^("<<E<<") , fraction= "<<DEC<<endl;
			
			//consider sign bit
			if(Arr[0])
				DEC=-DEC*pow(2,E);
			else
				DEC=DEC*pow(2,E);
			
			//print ans
			cout<<"decimal: "<<DEC<<endl<<endl;
			}
	}
	return 0;
}
