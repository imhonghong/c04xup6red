//decimal to IEEE754 floating point number
#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main(){
	
	while(1){
		double A;
		cin>>A;
		int S=0;
		if(A<0){
			A=-A;
			S=1;
		}
		
		double B;
		int expo;
		
		//find exponential part
		for(expo=127 ; expo>-127 ; expo--){
			if((A-pow(2,expo))<0){
				B=A;
			}
			else{
				B=A-pow(2,expo);
				break;
			}
		}
		
		//turn expo to E in 8bit
		int Eb=expo+127;
		int E[8];
		for(int e=7 ; e>=0 ; e--){
			if((Eb-pow(2,e))<0){
				E[e]=0;
			}
			else{
				Eb=Eb-pow(2,e);
				E[e]=1;
			}
		}
		
		//find fraction
		int F[23];
		for(int f=22; f>=0 ; f--){
			expo--;
			if((B-pow(2,expo))<0){
				F[f]=0;
			}
			else{
				F[f]=1;
				B=B-pow(2,expo);
			}
		}
		
		//print output
		cout<<"input="<<A<<endl;//test
		cout<<"SE-------F----------------------"<<endl;
		cout<<S;
		for(int i=7 ; i>=0 ; i--){//test
			cout<<E[i];
		}
		for(int i=22 ; i>=0 ; i--){//test
			cout<<F[i];
		}
		cout<<endl<<endl;
		
	}
	return 0;
}
