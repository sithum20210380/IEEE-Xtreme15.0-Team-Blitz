try:
    T = int(input())
    for k in range(T):
        N = int(input())
        alice_score = 0
        bob_score = 0
        alice_die = 1
        bob_die = 2
        d1_6 = 0
        d2_6 = 0
        count_d_1 = 1
        count_d_2 = 2
        d1_tot = 0
        d2_tot = 0
        for cnt in range (N):
            ansc, bnsc = input().split(' ')
            ansc= int(ansc)
            bnsc =int(bnsc)

            if 1<=ansc<=6:
                alice_score = alice_score + ansc
            if 1<=bnsc<=6:
                bob_score = bob_score + bnsc

            if count_d_1 == 1:
                d1_tot = d1_tot + ansc
                if ansc == 6:
                    d1_6 = d1_6+1
            else:
                d1_tot = d1_tot + bnsc
                if bnsc == 6:
                    d1_6 = d1_6+1

            if count_d_2 == 2:
                d2_tot = d2_tot + bnsc
                if bnsc == 6:
                    d2_6 = d2_6 +1
            else:
                d2_tot = d2_tot + ansc
                if ansc == 6:
                    d2_6 = d2_6 +1

            if bob_score != alice_score:
                if bob_die == 2:
                    bob_die = 1
                    alice_die = 2
                    count_d_1 = 2
                    count_d_2 = 1
                else:
                    bob_die = 2
                    alice_die = 1
                    count_d_1 = 1
                    count_d_2 = 2

        if d1_tot < d2_tot and d1_6 < d2_6:
            print("2")
        elif d2_tot < d1_tot and d2_6 < d1_6:
            print("1")
        elif d2_tot < d1_tot:
            print("1")
        elif d1_tot > d2_tot:
            print("2")
        elif d1_6 < d2_6:
            print("2")
        elif d2_6 < d1_6:
            print("1")
        else:
            print("2")
except:
    print()