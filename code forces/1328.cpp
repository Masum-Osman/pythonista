#include<bits/stdc++.h>
    
int main()
{
    int T;
    scanf("%d", &T);

    for (int i = 0; i < T; i++)
    {
        int a, b;
        scanf("%d %d", &a, &b);

        if(a % b == 0)
        {
            printf("%d\n", 0);
        }
        else
        {
            int ans = b - (a % b);
            printf("%d\n", ans);
        }
    }
}