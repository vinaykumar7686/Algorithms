/*
Aim: First Come First Serve CPU Scheduling
*/

#include <stdio.h>
int main()
{
	printf("Enter the number of processes : ");
	int n;
	scanf("%d",&n);
	int pid[10],at[10],bt[10],ct[10],tat[10],wt[10];
	int i=0,j=0;
	for(i=0;i<n;i++)
	{
		pid[i]=i+1;
		printf("Enter the 'Arrival Time' and 'Burst Time' of Process no. : %d\n",(i+1));
		scanf("%d",&at[i]);
		scanf("%d",&bt[i]);
	}
	//arranging the processes in ascending order of arrival time
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
	/*printing arranged processes
	for (int i=0;i<n;i++)
	{
		printf("Arrival time of process : %d is ",(i+1));
		printf("%d\n",at[i]);
		printf("Burst time of process number : %d is ",(i+1));
		printf("%d\n",bt[i]);
	}*/
	
	//computing completion time, tat, wt and average tat,wt
	float avgtat=0.0f,avgwt=0.0f;
	ct[0]=at[0]+bt[0];
	tat[0]=ct[0]-at[0];
	avgtat=tat[0];
	wt[0]=tat[0]-bt[0];
	avgwt=wt[0];
	for( i=1;i<n;i++)
	{
		ct[i]=ct[i-1]+bt[i];
		
		tat[i]=ct[i]-at[i];
		avgtat+=tat[i];
		
		wt[i]=tat[i]-bt[i];
		avgwt+=wt[i];
	}
	avgtat/=n;
	avgwt/=n;
	
	//computing throughput
	double tput=(double)n/(ct[n-1]-at[0]);
	
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
	//printing calculated data
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

