# coding: utf-8

# input
s0_0 = 3
s0_1 = 6
print "[input]"
print "s0_0 =", s0_0
print "s0_1 =", s0_1

# decompose
s1_0 = (s0_0 + s0_1)/2.0
d1_0 = s0_1 - s0_0
print "[decompose]"
print "s1_0 =", s1_0
print "d1_0 =", d1_0

# reconstruct
s0_0 = s1_0 - d1_0/2.0
s0_1 = s1_0 + d1_0/2.0
print "[reconstruct]"
print "s0_0 =", s0_0
print "s0_1 =", s0_1
