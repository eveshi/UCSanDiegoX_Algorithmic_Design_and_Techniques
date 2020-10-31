# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

# def siftdown(curr, data, p):
#     min_index = curr
#     left = curr*2 + 1
#     right = curr*2 + 2
#     if (left<len(data)) and (data[left] < data[min_index]):
#         min_index = left
#     if (right<len(data)) and (data[right] < data[min_index]):
#         min_index = right

#     # print("===>", data, min_index)
#     if min_index != curr:
#         data[curr], data[min_index] = data[min_index], data[curr]
#         p[curr], p[min_index] = p[min_index], p[curr]
#         curr = min_index
#         # print("===> curr", curr, data)
#         return siftdown(curr, data, p)
#     else:
#         return data, p

def compareWorker(worker1, min_worker, next_free_time, pos):
    if next_free_time[worker1] != next_free_time[min_worker]:
        return next_free_time[worker1] < next_free_time[min_worker]
    else:
        return pos[worker1] < pos[min_worker]

def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    pos = [x for x in range(n_workers)]
    for job in jobs:
        print(pos)
        result.append(AssignedJob(pos[0], next_free_time[0]))
        next_free_time[0] += job
        curr = 0
        # next_free_time, pos = siftdown(0, next_free_time, pos)
        while curr < len(next_free_time):
            min_index = curr
            left = curr*2 + 1
            right = curr*2 + 2
            if (left<len(next_free_time)) and compareWorker(left, min_index, next_free_time, pos):
                min_index = left
            if (right<len(next_free_time)) and compareWorker(right, min_index, next_free_time, pos):
                min_index = right

            # print("===>", next_free_time, min_index)
            if min_index != curr:
                next_free_time[curr], next_free_time[min_index] = next_free_time[min_index], next_free_time[curr]
                pos[curr], pos[min_index] = pos[min_index], pos[curr]
                curr = min_index
            else:
                break

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
