/* file name dshm.c
 */

#include <stdio.h>

int main() {
  FILE *fp = fopen("dsm_data.csv","w");
  if (fp == NULL){ 
    printf("Error opening file\n");
    return 1;
  }
  float x, v, a, E, m, k, T, b, dt,t=0;
  printf("Enter intial position\n");
  scanf("%f", &x);

  printf("Enter intial velocity\n");
  scanf("%f", &v);

  printf("Enter damping constant\n");
  scanf("%f", &b);

  printf("Enter simulation time\n");
  scanf("%f", &T);

  printf("Enter length of time step\n");
  scanf("%f",&dt);

  printf("Enter mass of block\n");
  scanf("%f",&m);

  printf("Enter spring constant\n");
  scanf("%f",&k);

if (dt <= 0 || T <= 0 || m <= 0 || k <= 0) {
    printf("Invalid parameters\n");
    return 1;
}

  int steps = (int)(T/dt);
  a = -(k/m)*x-(b/m)*v;

  fprintf(fp, "t,x,v,a,E,b,k,m\n");
  for (int i =0;i<=steps;i++) {
    E = 0.5*m*v*v+0.5*k*x*x;
    fprintf(fp, "%f,%f,%f,%f,%f,%f,%f,%f\n",t,x,v,a,E,b,k,m);
    v = v + a*dt;
    x = x + v*dt;
    t = t+dt;
    a = -(k/m)*x-(b/m)*v;
  }
  fclose(fp);
  return 0;
}

