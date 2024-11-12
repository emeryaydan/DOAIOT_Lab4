import hal.hal_input_switch as switch
import hal.hal_led as led
import time

def blink_led(frequency, duration=None):
    period = 1 / frequency
    half_period = period / 2
    start_time = time.time()
    blink_count = 0

    print(f"Blinking LED at {frequency} Hz")
    while True:
        led.set_output(0, 1)  # Turn LED on
        print(f"LED ON - Blink {blink_count + 1}")
        time.sleep(half_period)
        led.set_output(0, 0)  # Turn LED off
        print(f"LED OFF - Blink {blink_count + 1}")
        time.sleep(half_period)
        blink_count += 1

        if duration and (time.time() - start_time) >= duration:
            print(f"Blink duration {duration}s reached. Stopping.")
            break

def main():
    print("Initializing switch and LED...")
    switch.init()
    led.init()
    print("Initialization complete.")

    print("PiLedTest running. Press Ctrl+C to exit.")

    try:
        while True:
            switch_state = switch.read_slide_switch()
            print(f"Current switch state: {switch_state}")

            if switch_state == 1:  # Switch in left position
                print("Switch in left position. Blinking at 5 Hz.")
                blink_led(5, 10)
                led.set_output(0, 0)  # Turn LED off after 5 seconds
                print("Waiting for 1 second before checking switch again...")
                time.sleep(1)  # Wait for 1 second before checking switch again
            else:  # Switch in right position
                print("Switch in right position. Blinking at 10 Hz for 5 seconds.")
                blink_led(10, 5)
                print("5 seconds elapsed. Turning LED off.")
                led.set_output(0, 0)  # Turn LED off after 5 seconds
                print("Waiting for 1 second before checking switch again...")
                time.sleep(1)  # Wait for 1 second before checking switch again

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        led.set_output(0, 0)  # Ensure LED is off when exiting
        print("LED turned off.")
        print("Cleanup complete. Exiting program.")

if __name__ == "__main__":
    print("Starting PiLedTest...")
    main()