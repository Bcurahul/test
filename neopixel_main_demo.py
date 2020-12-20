import argparse
from ws2812b_neopixel_luma_led_matrix.neopixel_demo import WS2812_Neopixel
from threading import Thread

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Input effects for ws2812b/neopixel")
    parser.add_argument('effect', type=str, help="Input Effect Type")
    args = parser.parse_args()
    # print(f"Received command line effect argument : {args.effect}")

    try:
        while True:
            neo_pixel =  WS2812_Neopixel()
            thread = Thread(target=neo_pixel.gfx, args=(args.effect,))
            thread.daemon = True
            thread.start()
            thread.join()

    except KeyboardInterrupt:
        pass


