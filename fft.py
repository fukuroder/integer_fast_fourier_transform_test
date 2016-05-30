# coding: utf-8
import cmath

def fft(aa):
    n = len(aa)
    if(n > 1):
        ww = (cmath.exp(-2j*cmath.pi*k/n) for k in range(n/2))
        aa1 = fft( [(a1+a2)   for a1,a2 in zip(aa,aa[n/2:])] )
        aa2 = fft( [(a1-a2)*w for a1,a2,w in zip(aa,aa[n/2:], ww)] )
        return reduce(lambda xx,x: xx+[x[0],x[1]],zip(aa1,aa2),[])
    else:
        return aa

def ifft(aa):
    n = len(aa)
    if(n > 1):
        ww = (cmath.exp(-2j*cmath.pi*k/n) for k in range(n/2))
        aa1 = ifft( aa[0::2] )
        aa2 = [a2/w for a2,w in zip(ifft( aa[1::2] ), ww)]
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
    print numpy.array(input2)
    
    # fft
    fft_result = fft(input2)
    np_fft_result = numpy.fft.fft(input2)
    
    print "[fft]"
    print numpy.array(fft_result)
    
    print "[numpy fft]"
    print np_fft_result
    
    print "[fft error]"
    print numpy.abs(numpy.array(fft_result) - np_fft_result)

    # ifft
    ifft_result = ifft(fft_result)
    
    print "[ifft]"
    print numpy.array(ifft_result)
    
    print "[ifft error]"
    print numpy.abs(numpy.array(ifft_result) - input2)
