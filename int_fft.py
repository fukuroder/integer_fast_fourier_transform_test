# coding: utf-8
import cmath

def int_fft(aa):
    def int_lift(a,w):
        (c, s) = (w.real, w.imag)
        if(-1.0e-10 < s < 1.0e-10):
            pass
        elif(c >= 0.0):
            a[0] += int(a[1]*(c-1)/s)
            a[1] += int(a[0]*s)
            a[0] += int(a[1]*(c-1)/s)
        else:
            a[0] += int(a[1]*(c+1)/s)
            a[1] += int(a[0]*(-s))
            a[0] += int(a[1]*(c+1)/s)
            a *= -1
        return a

    n = len(aa)
    if(n > 1):
        ww = (cmath.exp(-2j*cmath.pi*k/n) for k in range(n/2))
        aa1 = int_fft( [(a1+a2)       for a1,a2 in zip(aa,aa[n/2:])] )
        aa2 = int_fft( [int_lift(a1-a2,w) for a1,a2,w in zip(aa,aa[n/2:], ww)] )
        return reduce(lambda xx,x: xx+[x[0],x[1]],zip(aa1,aa2),[])
    else:
        return aa

def int_ifft(aa):
    def int_ilift(a,w):
        (c, s) = (w.real, w.imag)
        if( -1.0e-10 < s < 1.0e-10 ):
            pass
        elif( c >= 0.0):   
            a[0] -= int(a[1]*(c-1)/s)
            a[1] -= int(a[0]*s)
            a[0] -= int(a[1]*(c-1)/s)
        else:
            a *= -1
            a[0] -= int(a[1]*(c+1)/s)
            a[1] -= int(a[0]*(-s))
            a[0] -= int(a[1]*(c+1)/s)
        return a
        
    n = len(aa)
    if(n > 1):
        ww = (cmath.exp(-2j*cmath.pi*k/n) for k in range(n/2))
        aa1 = int_ifft( aa[0::2] )
        aa2 = [int_ilift(a2, w) for a2,w in zip(int_ifft( aa[1::2] ), ww)]
        return [(a1+a2)/2 for a1,a2 in zip(aa1,aa2)] + \
               [(a1-a2)/2 for a1,a2 in zip(aa1,aa2)] 
    else:
        return aa

if __name__ == '__main__':
    import numpy
    input = numpy.random.randint(10000, size=(16,2))
    input2 = [numpy.array(complex(a[0],a[1])) for a in input]
    
    # input
    print "[input]"
    print input
    
    # fft
    int_fft_result = int_fft(input)
    np_fft_result = [ numpy.array([a.real, a.imag]) for a in numpy.fft.fft(input2) ]
    
    print "[int fft]"
    print numpy.array(int_fft_result)
    
    print "[numpy fft]"
    print numpy.array(np_fft_result)
    
    print "[fft error]"
    print numpy.abs(numpy.array(int_fft_result) - numpy.array(np_fft_result))

    # ifft
    int_ifft_result = int_ifft(int_fft_result)
    
    print "[ifft]"
    print numpy.array(int_ifft_result)
    
    print "[ifft error]"
    print numpy.abs(numpy.array(int_ifft_result) - input)
