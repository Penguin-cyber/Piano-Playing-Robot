import time
import serial


class servo:
    """
    Servo class. Requires id and pyserial port on initialization.

    All packets are in big endian form for SCS series servos.
    """

    def __init__(self, id, bus):
        self.id = id
        self.bus = bus

    """
    Information/Query-related functions
    """

    def read_reply(self):
        time.sleep(0.005)

        response = self.bus.read_all()
        if response:
            print(f"Servo {self.id} Reply Packet: ",
                  [hex(b) for b in response])
        else:
            print(f"No Reply From Servo {self.id}")

    def ping(self):
        """
        Query the working status
        """

        checksum = (~((self.id+0X02+0X01) & 0XFF) & 0XFF).to_bytes()

        packet = bytearray([0XFF, 0XFF, self.id, 0X02, 0X01]) + checksum

        self.bus.write(packet)

        self.read_reply()

    def read_pos(self):
        """
        Query the position of the servo
        """

        checksum = (~((self.id+0X04+0X02+0X38+0X02) & 0XFF) & 0XFF).to_bytes()

        packet = bytearray(
            [0XFF, 0XFF, self.id, 0X04, 0X02, 0X38, 0X02]) + checksum

        self.bus.write(packet)

        time.sleep(0.005)
        response = self.bus.read_all()
        pos = (response[5] << 8) | response[6]

        return pos

    """
    Mode-related functions
    """

    def query_mode(self):
        """
        For continuous mode, min and max angle have to be 0. Otherwise, it is closed loop.

        Returns 0 for closed-loop (positional) and 1 for open-loop (continuous).
        """

        # query min & max
        checksum = (~((self.id+0X04+0X02+0X09+0X02) & 0XFF) & 0XFF).to_bytes()
        packet = bytearray(
            [0XFF, 0XFF, self.id, 0X04, 0X02, 0X09, 0X02]) + checksum

        self.bus.write(packet)

        time.sleep(0.005)

        response = self.bus.read_all()
        min_ang = (response[5] << 8) | response[6]

        checksum = (~((self.id+0X04+0X02+0X011+0X02) & 0XFF) & 0XFF).to_bytes()
        packet = bytearray(
            [0XFF, 0XFF, self.id, 0X04, 0X02, 0X11, 0X02]) + checksum

        self.bus.write(packet)

        time.sleep(0.005)

        response = self.bus.read_all()
        max_ang = (response[5] << 8) | response[6]

        print(min_ang, max_ang)
        return min_ang + max_ang == 0

    def pos_mode(self):
        """
        Sets the mode of the servo to positional (closed-loop). State = 0.
        """

        min_ang = (20).to_bytes(2, byteorder='big')
        check_sum = (
            ~((self.id+0X05+0X03+0X09+sum(min_ang)) & 0XFF) & 0XFF).to_bytes()
        packet = bytearray(
            [0XFF, 0XFF, self.id, 0X05, 0X03, 0X09]) + min_ang + check_sum

        self.bus.write(packet)

        self.read_reply()

        max_ang = (1003).to_bytes(2, byteorder='big')
        check_sum = (
            ~((self.id+0X05+0X03+0X11+sum(max_ang)) & 0XFF) & 0XFF).to_bytes()
        packet = bytearray(
            [0XFF, 0XFF, self.id, 0X05, 0X03, 0X11]) + max_ang + check_sum

        self.bus.write(packet)

        self.read_reply()

    def cont_mode(self):
        """
        Sets the mode of the servo to continuous (open-loop). State = 1.
        """

        time.sleep(0.005)
        min_ang = (0).to_bytes(2, byteorder='big')
        check_sum = (
            ~((self.id+0X05+0X03+0X09+sum(min_ang)) & 0XFF) & 0XFF).to_bytes()
        packet = bytearray(
            [0XFF, 0XFF, self.id, 0X05, 0X03, 0X09]) + min_ang + check_sum

        self.bus.write(packet)

        self.read_reply()

        max_ang = (0).to_bytes(2, byteorder='big')
        check_sum = (
            ~((self.id+0X05+0X03+0X11+sum(max_ang)) & 0XFF) & 0XFF).to_bytes()
        packet = bytearray(
            [0XFF, 0XFF, self.id, 0X05, 0X03, 0X11]) + max_ang + check_sum

        self.bus.write(packet)

        self.read_reply()

    def swap_mode(self):
        # if we are in open loop
        if (self.query_mode()):
            time.sleep(0.005)
            min_ang = (20).to_bytes(2, byteorder='big')
            check_sum = (
                ~((self.id+0X05+0X03+0X09+sum(min_ang)) & 0XFF) & 0XFF).to_bytes()
            packet = bytearray(
                [0XFF, 0XFF, self.id, 0X05, 0X03, 0X09]) + min_ang + check_sum

            self.bus.write(packet)

            self.read_reply()

            max_ang = (1003).to_bytes(2, byteorder='big')
            check_sum = (
                ~((self.id+0X05+0X03+0X11+sum(max_ang)) & 0XFF) & 0XFF).to_bytes()
            packet = bytearray(
                [0XFF, 0XFF, self.id, 0X05, 0X03, 0X11]) + max_ang + check_sum

            self.bus.write(packet)

            self.read_reply()
        else:
            time.sleep(0.005)
            min_ang = (0).to_bytes(2, byteorder='big')
            check_sum = (
                ~((self.id+0X05+0X03+0X09+sum(min_ang)) & 0XFF) & 0XFF).to_bytes()
            packet = bytearray(
                [0XFF, 0XFF, self.id, 0X05, 0X03, 0X09]) + min_ang + check_sum

            self.bus.write(packet)

            self.read_reply()

            max_ang = (0).to_bytes(2, byteorder='big')
            check_sum = (
                ~((self.id+0X05+0X03+0X11+sum(max_ang)) & 0XFF) & 0XFF).to_bytes()
            packet = bytearray(
                [0XFF, 0XFF, self.id, 0X05, 0X03, 0X11]) + max_ang + check_sum

            self.bus.write(packet)

            self.read_reply()

    """
    Movement-related functions
    """

    def move_to(self, p, t, s):
        """
        Move to a position. (position, time, speed)

        If time = 0, then speed dictates the rate of rotation. If speed = 0, then time dictates the rate of rotation.
        """

        # convert to hex - big endian
        hp = p.to_bytes(2, byteorder='big')
        ht = t.to_bytes(2, byteorder='big')
        hs = s.to_bytes(2, byteorder='big')

        check_sum = (
            ~((self.id+0X09+0X03+0X2A+sum(hp)+sum(ht)+sum(hs)) & 0XFF) & 0XFF).to_bytes()

        packet = bytearray([0XFF, 0XFF,
                            self.id, 0X09, 0X03,
                            0X2A]) + hp + ht + hs + check_sum
        self.bus.write(packet)

        print(packet)

        self.read_reply()

    def cont_move(self, t):
        """
        Continually moves with a torque of t. Positive t for counter-clockwise; negative t for clockwise.

        For movement to occur, torque has to exceed 70.
        """

        # bit 10 needs to be 1 for clockwise rotation
        if t < 0:
            t = -t
            t = (1 << 10) | t

        ht = t.to_bytes(2, byteorder='big')

        check_sum = (
            ~((self.id+0X05+0X03+0X2C+sum(ht)) & 0XFF) & 0XFF).to_bytes()

        packet = bytearray([0XFF, 0XFF,
                            self.id, 0X05, 0X03,
                            0X2C]) + ht + check_sum

        self.bus.write(packet)

        print(packet)

        self.read_reply()

    def cont_stop(self):
        """
        Stops the continuous rotation of the servo.
        """

        self.cont_move(0)


if __name__ == '__main__':
    ser = serial.Serial('COM3', 1000000)

    s1 = servo(1, ser)
    s2 = servo(2, ser)
    s3 = servo(3, ser)
    s4 = servo(4, ser)
    s5 = servo(5, ser)
    s6 = servo(6, ser)
    s7 = servo(7, ser)
    s8 = servo(8, ser)
    s9 = servo(9, ser)
    s10 = servo(10, ser)
    s11 = servo(11, ser)
    s12 = servo(12, ser)
    time.sleep(1)
    s12.cont_mode()

    s12.cont_move(1000)
    time.sleep(1)
    s12.cont_stop()
    s12.cont_move(100)
    time.sleep(2)
    s12.cont_stop()
    s12.cont_move(-1000)
    time.sleep(0.75)
    s12.cont_stop()
