# coding: utf-8
import cmath
from itertools import chain

def fft_lift(aa):
    def lift(x,w):
        (c, s) = (w.real, w.imag)
        a = [x.real, x.imag]
        if(-1.0e-10 < s < 1.0e-10):
            pass
        elif(c >= 0.0):
            a[0] += a[1]*(c-1)/s
            a[1] += a[0]*s
            a[0] += a[1]*(c-1)/s
        else:
            a[0] += a[1]*(c+1)/s
            a[1] += a[0]*(-s)
            a[0] += a[1]*(c+1)/s
            a[0] *= -1
            a[1] *= -1
        return complex(a[0], a[1])

    n = len(aa)
    if(n > 1):
        ww = (cmath.exp(-2j*cmath.pi*k/n) for k in range(n//2))
        aa1 = fft_lift( [(a1+a2)       for a1,a2 in zip(aa,aa[n//2:])] )
        aa2 = fft_lift( [lift(a1-a2,w) for a1,a2,w in zip(aa,aa[n//2:], ww)] )
        return list(chain.from_iterable(zip(aa1,aa2)))
    else:
        return aa

def ifft_lift(aa):
    def ilift(x,w):
        (c, s) = (w.real, w.imag)
        a = [x.real, x.imag]
        if( -1.0e-10 < s < 1.0e-10 ):
            pass
        elif( c >= 0.0):   
            a[0] -= a[1]*(c-1)/s
            a[1] -= a[0]*s
            a[0] -= a[1]*(c-1)/s
        else:
            a[0] *= -1
            a[1] *= -1
            a[0] -= a[1]*(c+1)/s
            a[1] -= a[0]*(-s)
            a[0] -= a[1]*(c+1)/s
        return complex(a[0], a[1])
        
    n = len(aa)
    if(n > 1):
        ww = (cmath.exp(-2j*cmath.pi*k/n) for k in range(n//2))
        aa1 = ifft_lift( aa[0::2] )
        aa2 = [ilift(a2, w) for a2,w in zip(ifft_lift( aa[1::2] ), ww)]
        return [(a1+a2)/2 for a1,a2 in zip(aa1,aa2)] + \
               [(a1-a2)/2 for a1,a2 in zip(aa1,aa2)] 
    else:
        return aa

if __name__ == '__main__':
    import numpy
    input = numpy.random.randint(10000, size=(16,2))
    input2 = [numpy.array(complex(a[0],a[1])) for a in input]
    
    # input
    print("[input]")
    print(numpy.array(input2))
    
    # fft
    fft_result = fft_lift(input2)
    np_fft_result = numpy.fft.fft(input2)
    
    print("[fft]")
    print(numpy.array(fft_result))
    
    print("[numpy fft]")
    print(np_fft_result)
    
    print("[fft error]")
    print(numpy.abs(numpy.array(fft_result) - np_fft_result))

    # ifft
    ifft_result = ifft_lift(fft_result)
    
    print("[ifft]")
    print(numpy.array(ifft_result))
    
    print("[ifft error]")
    print(numpy.abs(numpy.array(ifft_result) - input2))
