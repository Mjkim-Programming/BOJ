#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAX 1000005
#define PI 3.14159265358979323846

typedef struct { double r, i; } Complex;

Complex c_add(Complex a, Complex b){ return (Complex){a.r+b.r, a.i+b.i}; }
Complex c_sub(Complex a, Complex b){ return (Complex){a.r-b.r, a.i-b.i}; }
Complex c_mul(Complex a, Complex b){ return (Complex){a.r*b.r - a.i*b.i, a.r*b.i + a.i*b.r}; }

void fft(Complex *a, int n, int invert){
    for(int i=1,j=0;i<n;i++){
        int bit = n>>1;
        for(; j>=bit; bit>>=1) j-=bit;
        j+=bit;
        if(i<j){
            Complex tmp = a[i]; a[i]=a[j]; a[j]=tmp;
        }
    }

    for(int len=2; len<=n; len<<=1){
        double ang = 2*PI/len * (invert?-1:1);
        Complex wlen = {cos(ang), sin(ang)};
        for(int i=0;i<n;i+=len){
            Complex w = {1,0};
            for(int j=0;j<len/2;j++){
                Complex u=a[i+j], v=c_mul(a[i+j+len/2], w);
                a[i+j] = c_add(u, v);
                a[i+j+len/2] = c_sub(u, v);
                w = c_mul(w, wlen);
            }
        }
    }

    if(invert){
        for(int i=0;i<n;i++){ a[i].r/=n; a[i].i/=n; }
    }
}

int main(){
    char s1[MAX], s2[MAX];
    scanf("%s %s", s1, s2);

    int len1=strlen(s1), len2=strlen(s2);
    int n=1;
    while(n < len1+len2) n <<=1;

    Complex *a = calloc(n, sizeof(Complex));
    Complex *b = calloc(n, sizeof(Complex));

    for(int i=0;i<len1;i++) a[i].r = s1[len1-1-i]-'0';
    for(int i=0;i<len2;i++) b[i].r = s2[len2-1-i]-'0';

    fft(a,n,0); fft(b,n,0);
    for(int i=0;i<n;i++) a[i] = c_mul(a[i], b[i]);
    fft(a,n,1);

    int *res = calloc(n, sizeof(int));
    for(int i=0;i<n;i++) res[i] = (int)(a[i].r + 0.5);

    for(int i=0;i<n;i++){
        if(res[i]>=10){
            if(i+1<n) res[i+1] += res[i]/10;
            res[i] %= 10;
        }
    }

    int start = n-1;
    while(start>0 && res[start]==0) start--;
    for(int i=start;i>=0;i--) printf("%d", res[i]);
    printf("\n");

    free(a); free(b); free(res);
    return 0;
}
