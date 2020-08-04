"""
回溯算法

核心：
def back_track(roads, selections):
    if condition:
        result.append(selections)
    
    for road in roads:
        if repeat or not satisfy:
            continue
        selections.append(road)
        back_track(roads, selections)
        selections.pop()
"""
from collections import deque
import copy
res = []

def back_track(nums, track_list):
    if len(track_list) == len(nums):
        answer = copy.deepcopy(track_list)
        res.append(answer)
        return
    
    length = len(nums)
    for index in range(length):
        if nums[index] in track_list:
            continue
        track_list.append(nums[index])
        back_track(nums, track_list)
        track_list.pop()


def main():
    nums = [1, 2, 3]
    track = deque()
    back_track(nums, track)
    print(res)

if __name__ == "__main__":
    main()