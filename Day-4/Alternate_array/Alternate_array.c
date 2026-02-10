#include<sdio.h>
void alternate_array(int arr[],int n)
{
    int i,temp;
    for(i=0;i<n-1;i+=2)
    {
        temp=arr[i];
        arr[i]=arr[i+1];
        arr[i+1]=temp;
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
    alternate_array(arr,n);
    printf("Alternate array: ");
    for(i=0;i<n;i++)
    {
        printf("%d ",arr[i]);
    }
    return 0;
}
// Time Complexity: O(n)
// Space Complexity: O(1)
