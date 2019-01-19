import zmq

def main():
    try:
        context = zmq.Context(1)
        frontend = context.socket(zmq.PULL)
        frontend.bind("tcp://*:6001")

        backend = context.socket(zmq.PUSH)
        backend.bind("tcp://*:6002")

        zmq.device(zmq.STREAMER, frontend, backend)
    except Exception as e:
        print(e)
        print("Closing zmq device")
    finally:
        pass
        frontend.close()
        backend.close()
        context.term()

if __name__ == "__main__":
    main()
