#include "levenshtein.h"
#include <string.h>
#include <stdlib.h>

#define MIN2(a, b) ((a) < (b) ? (a) : (b))
#define MIN3(a, b, c) (MIN2((c), MIN2((a), (b))))

int levenshtein_dist(const char *s, const char *t)
{
    int i=0, j=0;
    int m=strlen(s), n=strlen(t);
    int *d = (int*)malloc((m+1) * (n+1) * sizeof(int));
    if (d == NULL) goto fail;

    for (i=1; i<m+1; ++i)
        d[i*(n+1)] = i;

    for (j=1; j<n+1; ++j)
        d[j] = j;

    for (j=1; j<n+1; ++j) {
        for (i=1; i<m+1; ++i) {
            if (s[i-1] == t[j-1]) {
                d[i*(n+1) + j] = d[(i-1) * (n+1) + (j-1)];
            }
            else {
                d[i*(n+1) + j] = MIN3(d[(i-1) * (n+1) + j] + 1,
                                      d[i * (n+1) + (j-1)] + 1,
                                      d[(i-1) * (n+1) + (j-1)] + 1);
            }
        }
    }

    if(d)
        free(d);

    return d[m * (n+1) + n];

fail:
    return -1;
}
