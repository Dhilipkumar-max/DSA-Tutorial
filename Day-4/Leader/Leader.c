#include<stdio.h>
void leader(int arr[],int n)
{
    int i,j,flag;
    printf("Leaders in the array: ");
    for(i=0;i<n;i++)
    {
        flag=0;
        for(j=i+1;j<n;j++)
        {
            if(arr[i]<arr[j])
            {
                flag=1;
                break;
            }
        }
        if(flag==0)
        {
            printf("%d ",arr[i]);
        }
    }
}
int main()
{
    int n,i;
    printf("Enter the size of the array: ");
    scanf("%d",&n);
    int arr[n];
    printf("Enter the elements of the array: ");
    for(i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    leader(arr,n);
    return 0;
}
// Time Complexity: O(n^2)
// Space Complexity: O(1)