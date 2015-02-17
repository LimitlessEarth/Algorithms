#include<stdio.h>

main(){
  double a[200];
  a[0] = 0;
  a[1] = 1;
  int i;
  for ( i=2; i<201; i++) {
    a[i] = a[i-1] + a[i-2];
    //printf("%d\n", i );
    //printf("%f\n", a[i]);
  }

  printf("%f\n", a[200]);
  return;
}
