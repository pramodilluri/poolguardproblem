#!/usr/bin/python3


import sys
from bitarray import bitarray

# 0 : t0 - t1, 1 : t1 - t2, so on...
guard_avail_t = 1000000000 * bitarray('0')
redundant_avail_t = 1000000000 * bitarray('0')



def prepare_data(lines):

    for line in lines:
        t_slot = line.strip().split(' ')
        start = int(t_slot[0])
        end = int(t_slot[1])
   
        #print ("start %d end %d" %(start, end))
        # Mark availability
        for i in range(start, end):
            if not guard_avail_t[i]:
                #print ("guard not found available so far in %d slot, setting this slot" %i)
                guard_avail_t[i] = 1
            else:
                #print("guard already available in %d slot, so marking this slot redundant" %i)
                redundant_avail_t[i] = 1


def func(lines):
    min_impact = sys.maxsize
    min_imp_guard_id = 0
    guard_id = 0

    for line in lines:
        t_slot = line.strip().split(' ')
        start = int(t_slot[0])
        end = int(t_slot[1])
        impact = 0 
        # check for impact if removed
        for i in range(start, end):
            if not redundant_avail_t[i]:
                impact += 1

        if impact < min_impact:
            min_impact = impact
            min_imp_guard_id = guard_id

        guard_id += 1

    print ("\nLifeguard number %d could be removed with less impact on coverage" %(min_imp_guard_id+1))

    # remove min impact guard id time coverage
    t_slot = lines[min_imp_guard_id].strip().split(' ')
    start = int(t_slot[0])
    end = int(t_slot[1])

    for i in range(start, end):
        if not redundant_avail_t[i]:
            guard_avail_t[i] = 0

    # calculate time coverage after firing min impactful lifeguard
    return guard_avail_t.count(1)


def main():
    # main driver function 
    with open(sys.argv[1], 'r') as my_file:
        lines = my_file.readlines()

    guard_count = lines[0]
    lines.pop(0)

    # process realtime input and prepare compute easy data
    prepare_data(lines)

    # identify the guard with least impact on time coverage on firing.
    result = func(lines)
    print ("Maximum time coverage after removing one lifeguard : %d\n" % result)


if __name__ == "__main__":
    main()
