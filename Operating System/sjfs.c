#include <stdio.h>
int main()
{
	int n,x,t=0,maxct=0,i=0,j=0;
	printf("Enter the number of processes  :  ");
	scanf("%d",&n);
	int pid[n],at[n],bt[n],ct[n],tat[n],wt[n],mark[n],done[n];
	float avgtat=0,avgwt=0,tput=0;
	
	printf("\tENTER THE DETAILS OF PROCESSES\n");
	for( i=0;i<n;i++)
	{
		printf("Enter Process ID , Arival Time and Burst Time  of process no.: %d \n",i+1);
		scanf("%d",&pid[i]);
		scanf("%d",&at[i]);
		scanf("%d",&bt[i]);
		ct[i]=0;
		tat[i]=0;
		wt[i]=0;
		mark[i]=0;
		done[i]=0;
	}
	//arranging the processes in order of incrasing at
	for( i=0;i<n;i++)
	{
		for( j=0;j<n-i-1;j++)
		{
			if(at[j]>at[j+1])
			{
				int temp=at[j];
				at[j]=at[j+1];
				at[j+1]=temp;
				
				temp=bt[j];
				bt[j]=bt[j+1];
				bt[j+1]=temp;
				
				temp=pid[j];
				pid[j]=pid[j+1];
				pid[j+1]=temp;
			}
		}
	}
	
	//Calculation
	int c=0;
	for( i=0;c!=n;i++)
	{
		t=0;//found
		//unmarking all previous marks
		for( j=0;j<n;j++)
		{
			mark[j]=0;
		}

		//marking the processes with at less than or equal to clock
		for( j=0;j<n;j++)
		{
			if((at[j]<=i)&&(done[j]==0))
			{
				t++;
				mark[j]=1;
			}
		}
		
		if(t>0)	//inner conditions will run iff any process whose at is less than clk is found
		{					
			//finding the process with shortest burst time amongst the checked ones 
			
			int sbt=9999;
			int k=0;
			for( j=n-1;j>=0;j--)
			{
				if((bt[j]<=sbt)&&(mark[j]==1))
				{
					k=j;
					sbt=bt[j];
				}
			}
			
			done[k]=1;		
		
			//calculating compile time of the marked process
			ct[k]=i+bt[k];
			i+=bt[k]-1;
			c++;   
			
			//calculating other details
			tat[k]=ct[k]-at[k];
			wt[k]=tat[k]-bt[k];
			avgtat+=tat[k];
			avgwt+=wt[k];
			
			//finding max CT
			if(maxct<ct[k])
				maxct=ct[k];
		}		
	}
	avgtat=(float)avgtat/n;
	avgwt=(float)avgwt/n;
	tput=(float)n/(maxct-at[0]);
	
	//arranging the processess in order of pid
	for( i=0;i<n;i++)
	{
		for( j=0;j<n-i-1;j++)
		{
			if(pid[j]>pid[j+1])
			{
				int temp=at[j];
				at[j]=at[j+1];
				at[j+1]=temp;
				
				temp=bt[j];
				bt[j]=bt[j+1];
				bt[j+1]=temp;
				
				temp=pid[j];
				pid[j]=pid[j+1];
				pid[j+1]=temp;
				
				temp=ct[j];
				ct[j]=ct[j+1];
				ct[j+1]=temp;
				
				temp=wt[j];
				wt[j]=wt[j+1];
				wt[j+1]=temp;
				
				temp=tat[j];
				tat[j]=tat[j+1];
				tat[j+1]=temp;
			}
		}
	}
	
	//printing the processed details
	printf("\n\n");
	printf("\tCalculated Data after (SJFS) Shortest Job First Scheduling ");
	printf("\n\n");
	printf("PID.\t\t A.T.\t\t B.T.\t\t C.T.\t\t T.A.T\t\t W.T.\n");
	for( i=0;i<n;i++)
	{
		printf("%d\t\t %d\t\t %d\t\t %d\t\t %d\t\t %d\n",pid[i],at[i],bt[i],ct[i],tat[i],wt[i]);
	}
	printf("\n\n");
	printf("Average Turn Around Time : %.2f\n",avgtat);
	printf("Average Waiting Time : %.2f\n",avgwt);
	printf("Through Put : %.2f",tput);
}
