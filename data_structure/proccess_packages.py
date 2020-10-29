from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process(self, request):
        # write your code here
        while len(self.finish_time) > 0 and request.arrived_at >= self.finish_time[0]:
            self.finish_time.pop(0)

        print(self.finish_time)
        print(self.size)

        if len(self.finish_time) < self.size:
            print("==>", self.finish_time)
            if len(self.finish_time) == 0:
                self.finish_time.append(request.arrived_at + request.time_to_process)
                print(request.arrived_at)
                return Response(False, request.arrived_at)
            else:
                start_time = request.arrived_at
                if self.finish_time[-1] > request.arrived_at:
                    start_time = self.finish_time[-1]
                    self.finish_time.append(self.finish_time[-1]+request.time_to_process)
                    return Response(False, start_time)
                elif self.finish_time[-1] == request.arrived_at:
                    start_time = self.finish_time[-1] + 1
                    self.finish_time.append(start_time + request.time_to_process)
                    return Response(False, start_time)

        return Response(True, -1)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    print("=>", responses)
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()