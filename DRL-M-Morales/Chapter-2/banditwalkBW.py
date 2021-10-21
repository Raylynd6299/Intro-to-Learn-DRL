'''
--Actions--
0 left
1 right

--------------
| H | S | G  |
--------------
G final state
S Initial state

'''

P= {
    0: {   #State- Example state 0
        0: [(1.0,0,0.0, True)], #Action (Action 0) : Possible transitions for that (State, Action)
        1: [(1.0,0,0.0, True)]  #[probabilit of that transition, next state, reward, flag thath indicated if the next state is terminal]
    },
    1: {
        0: [(1.0,0,0.0, True)],
        1: [(1.0,2,1.0, True)]
    },
    2: {
        0: [(1.0,2,0.0, True)],
        1: [(1.0,2,0.0, True)]
    }
}

'''
Another way:
import gym, gym_walk
P= gym.make('BanditWalk-v0).env.P
'''