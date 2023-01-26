for (i=0;i<n;i++)
{
    for (j=0;i<n;i++)
    {
        if (j==0 || a[i][j]<mins)
        {
            mins=a[i][j];
            jjmin=j;
        }
    }
    if(i==0 || mins<maxmin)
    {
        mins=a[i][j];
        imaxmin=i;jmaxmin=jjmin
    }
}
cout<<imaxmin<<''<<jmaxmin;
