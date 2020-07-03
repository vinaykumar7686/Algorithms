#include<stdio.h>
int main()
{
	int nb,nr,pf=0,mp=0,flag,mstatus=0, i=0, j=0, k=0;
	printf("Enter total number of page frames in memory : ");
	scanf("%d",&nb);
	printf("\nEnter total number of page references : ");
	scanf("%d",&nr);
	int mm[nb],pr[nr],mark[nb];
	printf("\nEnter page references\n");
	for(i=0;i<nr;i++)
	{
		printf("   Reference %d : ",(i+1));
		scanf("%d",&pr[i]);
	}
	for( i=0;i<nb;i++)
	{
		mm[i]=-99;
		mark[i]=-99;
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
			//unmarking all marks
			for( j=0;j<nb;j++)
			{
				mark[j]=-99;
			}
			/*printf("i = %d\n",i);*/
			
			//if memory is empty
			if(mstatus<nb)
			{
				mstatus++;
				mm[mp++]=pr[i];
				pf++;
			}
			//if memory is full and replacement is needed
			else if(mstatus>=nb)
			{
				int count=0;
				for( j=i-1;j>=0;j--)
				{
					for( k=0;k<nb;k++)
					{
						if(count<nb-1)
						{
							if((mm[k]==pr[j]))
							{
								mark[k]=1;
								count++;
							}
						}
					}
				}
				for( j=0;j<nb;j++)
				{
					if(mark[j]==-99)
					{
						mm[j]=pr[i];
						pf++;
						break;
					}
				}
			}
		}
		/*
		printf("Memory: ");
		for(int p=0;p<nb;p++)
		{
			printf("%d\t",mm[p]);
		}
		printf("\n");*/
	}
	printf("\n\n\tNo. of page faults occoured while applying Least Recently Used(LRU) Page Replacement Algorithm : %d",pf);
}
