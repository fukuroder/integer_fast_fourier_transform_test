# coding: utf-8

# input
s0 = 3
s1 = 6
print "[input]"
print "s0_0 =", s0
print "s0_1 =", s1

# decompose
s1 -= s0
s0 += s1/2.0
print "[decompose]"
print "s1_0 =", s0
print "d1_0 =", s1

# reconstruct
s0 -= s1/2.0
s1 += s0
print "[reconstruct]"
print "s0_0 =", s0
print "s0_1 =", s1
