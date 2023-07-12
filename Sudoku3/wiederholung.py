import time

start_second = time.time()
print("start_second" , start_second)


time.sleep(3)



now_second = time.time()

game_play_time = now_second - start_second

print("start second " , start_second)

print("game_play time in seconds " , game_play_time)