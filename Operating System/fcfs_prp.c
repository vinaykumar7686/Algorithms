#include<stdio.h>
int main()
{
	int nb,nr,pf=0,mp=0,flag,mstatus=0,i=0,j=0;
	printf("Enter total number of page frames in memory : ");
	scanf("%d",&nb);
	printf("\nEnter total number of page references : ");
	scanf("%d",&nr);
	int mm[nb],pr[nr];
	printf("\nEnter page references\n");
	for( i=0;i<nr;i++)
	{
		printf("   Reference %d : ",(i+1));
		scanf("%d",&pr[i]);
	}
	for( i=0;i<nb;i++)
	{
		mm[i]=-99;
	}
	//Calculation
	for( i=0;i<nr;i++)
	{
		flag=0;
		for( j=0;j<nb;j++)
		{
			if(mm[j]==pr[i])
			{
				flag=1;
			}
		}
		if(flag==0)
		{
			mp=(mp+1)%nb;
			mm[mp]=pr[i];
			pf++;
		}
	}
	printf("\n\n\tNo. of page faults occoured while applying First Come First Serve (FCFS) Page Replacement Algorithm : %d",pf);
}
