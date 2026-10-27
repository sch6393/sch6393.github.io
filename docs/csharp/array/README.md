# Array

## Difference
```c#
// Sample
int[] iarr1 = { 2, 4, 6, 8, 10 };
int[] iarr2 = { 3, 6, 9 };

// iarr1 기준
var vExcept = iarr1.Except(iarr2);
foreach (var vtmp in vExcept)
{
    Console.Write(vtmp);
}
```

!!! abstract "2, 4, 8, 10"

## Intersection
```c#
// Sample
int[] iarr1 = { 2, 4, 6, 8, 10 };
int[] iarr2 = { 3, 6, 9 };

var vIntersection = iarr1.Intersect(iarr2);
foreach (var vtmp in vIntersection)
{
    Console.Write(vtmp);
}
```
!!! abstract "6"

### Union
```c#
// Sample
int[] iarr1 = { 2, 4, 6, 8, 10 };
int[] iarr2 = { 3, 6, 9 };

var vUnion = iarr1.Union(iarr2).OrderBy(n => n).Reverse();
foreach (var vtmp in vUnion)
{
    Console.Write(vtmp);
}
```

!!! abstract "10, 9, 8, 6, 4, 3, 2"
