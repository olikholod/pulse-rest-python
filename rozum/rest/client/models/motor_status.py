# coding: utf-8

"""
    Robot API

    Robot REST API  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class MotorStatus(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'angle': 'float',
        'rotor_velocity': 'float',
        'rms_current': 'float',
        'voltage': 'float',
        'phase_current': 'float',
        'stator_temperature': 'float',
        'servo_temperature': 'float',
        'velocity_error': 'float',
        'velocity_setpoint': 'float',
        'velocity_output': 'float',
        'velocity_feedback': 'float',
        'position_error': 'float',
        'position_setpoint': 'float',
        'position_output': 'float',
        'position_feedback': 'float'
    }

    attribute_map = {
        'angle': 'angle',
        'rotor_velocity': 'rotorVelocity',
        'rms_current': 'rmsCurrent',
        'voltage': 'voltage',
        'phase_current': 'phaseCurrent',
        'stator_temperature': 'statorTemperature',
        'servo_temperature': 'servoTemperature',
        'velocity_error': 'velocityError',
        'velocity_setpoint': 'velocitySetpoint',
        'velocity_output': 'velocityOutput',
        'velocity_feedback': 'velocityFeedback',
        'position_error': 'positionError',
        'position_setpoint': 'positionSetpoint',
        'position_output': 'positionOutput',
        'position_feedback': 'positionFeedback'
    }

    def __init__(self, angle=None, rotor_velocity=None, rms_current=None, voltage=None, phase_current=None, stator_temperature=None, servo_temperature=None, velocity_error=None, velocity_setpoint=None, velocity_output=None, velocity_feedback=None, position_error=None, position_setpoint=None, position_output=None, position_feedback=None):  # noqa: E501
        """MotorStatus - a model defined in Swagger"""  # noqa: E501

        self._angle = None
        self._rotor_velocity = None
        self._rms_current = None
        self._voltage = None
        self._phase_current = None
        self._stator_temperature = None
        self._servo_temperature = None
        self._velocity_error = None
        self._velocity_setpoint = None
        self._velocity_output = None
        self._velocity_feedback = None
        self._position_error = None
        self._position_setpoint = None
        self._position_output = None
        self._position_feedback = None
        self.discriminator = None

        if angle is not None:
            self.angle = angle
        if rotor_velocity is not None:
            self.rotor_velocity = rotor_velocity
        if rms_current is not None:
            self.rms_current = rms_current
        if voltage is not None:
            self.voltage = voltage
        if phase_current is not None:
            self.phase_current = phase_current
        if stator_temperature is not None:
            self.stator_temperature = stator_temperature
        if servo_temperature is not None:
            self.servo_temperature = servo_temperature
        if velocity_error is not None:
            self.velocity_error = velocity_error
        if velocity_setpoint is not None:
            self.velocity_setpoint = velocity_setpoint
        if velocity_output is not None:
            self.velocity_output = velocity_output
        if velocity_feedback is not None:
            self.velocity_feedback = velocity_feedback
        if position_error is not None:
            self.position_error = position_error
        if position_setpoint is not None:
            self.position_setpoint = position_setpoint
        if position_output is not None:
            self.position_output = position_output
        if position_feedback is not None:
            self.position_feedback = position_feedback

    @property
    def angle(self):
        """Gets the angle of this MotorStatus.  # noqa: E501

        The actual angular position (in degrees) of the servo's output flange  # noqa: E501

        :return: The angle of this MotorStatus.  # noqa: E501
        :rtype: float
        """
        return self._angle

    @angle.setter
    def angle(self, angle):
        """Sets the angle of this MotorStatus.

        The actual angular position (in degrees) of the servo's output flange  # noqa: E501

        :param angle: The angle of this MotorStatus.  # noqa: E501
        :type: float
        """

        self._angle = angle

    @property
    def rotor_velocity(self):
        """Gets the rotor_velocity of this MotorStatus.  # noqa: E501

        The actual rotor velocity (in RPM)  # noqa: E501

        :return: The rotor_velocity of this MotorStatus.  # noqa: E501
        :rtype: float
        """
        return self._rotor_velocity

    @rotor_velocity.setter
    def rotor_velocity(self, rotor_velocity):
        """Sets the rotor_velocity of this MotorStatus.

        The actual rotor velocity (in RPM)  # noqa: E501

        :param rotor_velocity: The rotor_velocity of this MotorStatus.  # noqa: E501
        :type: float
        """

        self._rotor_velocity = rotor_velocity

    @property
    def rms_current(self):
        """Gets the rms_current of this MotorStatus.  # noqa: E501

        The actual input current (in Amperes)  # noqa: E501

        :return: The rms_current of this MotorStatus.  # noqa: E501
        :rtype: float
        """
        return self._rms_current

    @rms_current.setter
    def rms_current(self, rms_current):
        """Sets the rms_current of this MotorStatus.

        The actual input current (in Amperes)  # noqa: E501

        :param rms_current: The rms_current of this MotorStatus.  # noqa: E501
        :type: float
        """

        self._rms_current = rms_current

    @property
    def voltage(self):
        """Gets the voltage of this MotorStatus.  # noqa: E501

        The actual supply voltage (in Volts)  # noqa: E501

        :return: The voltage of this MotorStatus.  # noqa: E501
        :rtype: float
        """
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        """Sets the voltage of this MotorStatus.

        The actual supply voltage (in Volts)  # noqa: E501

        :param voltage: The voltage of this MotorStatus.  # noqa: E501
        :type: float
        """

        self._voltage = voltage

    @property
    def phase_current(self):
        """Gets the phase_current of this MotorStatus.  # noqa: E501

        Current value phase current for this motor  # noqa: E501

        :return: The phase_current of this MotorStatus.  # noqa: E501
        :rtype: float
        """
        return self._phase_current

    @phase_current.setter
    def phase_current(self, phase_current):
        """Sets the phase_current of this MotorStatus.

        Current value phase current for this motor  # noqa: E501

        :param phase_current: The phase_current of this MotorStatus.  # noqa: E501
        :type: float
        """

        self._phase_current = phase_current

    @property
    def stator_temperature(self):
        """Gets the stator_temperature of this MotorStatus.  # noqa: E501

        The actual temperature (in degrees C) as measured on the stator winding  # noqa: E501

        :return: The stator_temperature of this MotorStatus.  # noqa: E501
        :rtype: float
        """
        return self._stator_temperature

    @stator_temperature.setter
    def stator_temperature(self, stator_temperature):
        """Sets the stator_temperature of this MotorStatus.

        The actual temperature (in degrees C) as measured on the stator winding  # noqa: E501

        :param stator_temperature: The stator_temperature of this MotorStatus.  # noqa: E501
        :type: float
        """

        self._stator_temperature = stator_temperature

    @property
    def servo_temperature(self):
        """Gets the servo_temperature of this MotorStatus.  # noqa: E501

        The actual temperature (in degrees C) as measured on the MCU PCB  # noqa: E501

        :return: The servo_temperature of this MotorStatus.  # noqa: E501
        :rtype: float
        """
        return self._servo_temperature

    @servo_temperature.setter
    def servo_temperature(self, servo_temperature):
        """Sets the servo_temperature of this MotorStatus.

        The actual temperature (in degrees C) as measured on the MCU PCB  # noqa: E501

        :param servo_temperature: The servo_temperature of this MotorStatus.  # noqa: E501
        :type: float
        """

        self._servo_temperature = servo_temperature

    @property
    def velocity_error(self):
        """Gets the velocity_error of this MotorStatus.  # noqa: E501

        The difference between the preset and the actual rotor velocities (in RPM)  # noqa: E501

        :return: The velocity_error of this MotorStatus.  # noqa: E501
        :rtype: float
        """
        return self._velocity_error

    @velocity_error.setter
    def velocity_error(self, velocity_error):
        """Sets the velocity_error of this MotorStatus.

        The difference between the preset and the actual rotor velocities (in RPM)  # noqa: E501

        :param velocity_error: The velocity_error of this MotorStatus.  # noqa: E501
        :type: float
        """

        self._velocity_error = velocity_error

    @property
    def velocity_setpoint(self):
        """Gets the velocity_setpoint of this MotorStatus.  # noqa: E501

        The user-preset rotor velocity (in RPM)  # noqa: E501

        :return: The velocity_setpoint of this MotorStatus.  # noqa: E501
        :rtype: float
        """
        return self._velocity_setpoint

    @velocity_setpoint.setter
    def velocity_setpoint(self, velocity_setpoint):
        """Sets the velocity_setpoint of this MotorStatus.

        The user-preset rotor velocity (in RPM)  # noqa: E501

        :param velocity_setpoint: The velocity_setpoint of this MotorStatus.  # noqa: E501
        :type: float
        """

        self._velocity_setpoint = velocity_setpoint

    @property
    def velocity_output(self):
        """Gets the velocity_output of this MotorStatus.  # noqa: E501

        The motor control current (in Amperes) based on the preset velocity  # noqa: E501

        :return: The velocity_output of this MotorStatus.  # noqa: E501
        :rtype: float
        """
        return self._velocity_output

    @velocity_output.setter
    def velocity_output(self, velocity_output):
        """Sets the velocity_output of this MotorStatus.

        The motor control current (in Amperes) based on the preset velocity  # noqa: E501

        :param velocity_output: The velocity_output of this MotorStatus.  # noqa: E501
        :type: float
        """

        self._velocity_output = velocity_output

    @property
    def velocity_feedback(self):
        """Gets the velocity_feedback of this MotorStatus.  # noqa: E501

        The actual rotor velocity (in RPM)  # noqa: E501

        :return: The velocity_feedback of this MotorStatus.  # noqa: E501
        :rtype: float
        """
        return self._velocity_feedback

    @velocity_feedback.setter
    def velocity_feedback(self, velocity_feedback):
        """Sets the velocity_feedback of this MotorStatus.

        The actual rotor velocity (in RPM)  # noqa: E501

        :param velocity_feedback: The velocity_feedback of this MotorStatus.  # noqa: E501
        :type: float
        """

        self._velocity_feedback = velocity_feedback

    @property
    def position_error(self):
        """Gets the position_error of this MotorStatus.  # noqa: E501

        The difference between the preset and the actual positions of the servo flange (in degrees)  # noqa: E501

        :return: The position_error of this MotorStatus.  # noqa: E501
        :rtype: float
        """
        return self._position_error

    @position_error.setter
    def position_error(self, position_error):
        """Sets the position_error of this MotorStatus.

        The difference between the preset and the actual positions of the servo flange (in degrees)  # noqa: E501

        :param position_error: The position_error of this MotorStatus.  # noqa: E501
        :type: float
        """

        self._position_error = position_error

    @property
    def position_setpoint(self):
        """Gets the position_setpoint of this MotorStatus.  # noqa: E501

        The user-preset position of the servo flange in degrees  # noqa: E501

        :return: The position_setpoint of this MotorStatus.  # noqa: E501
        :rtype: float
        """
        return self._position_setpoint

    @position_setpoint.setter
    def position_setpoint(self, position_setpoint):
        """Sets the position_setpoint of this MotorStatus.

        The user-preset position of the servo flange in degrees  # noqa: E501

        :param position_setpoint: The position_setpoint of this MotorStatus.  # noqa: E501
        :type: float
        """

        self._position_setpoint = position_setpoint

    @property
    def position_output(self):
        """Gets the position_output of this MotorStatus.  # noqa: E501

        Rotor velocity (in RPM) based on the position setpoint  # noqa: E501

        :return: The position_output of this MotorStatus.  # noqa: E501
        :rtype: float
        """
        return self._position_output

    @position_output.setter
    def position_output(self, position_output):
        """Sets the position_output of this MotorStatus.

        Rotor velocity (in RPM) based on the position setpoint  # noqa: E501

        :param position_output: The position_output of this MotorStatus.  # noqa: E501
        :type: float
        """

        self._position_output = position_output

    @property
    def position_feedback(self):
        """Gets the position_feedback of this MotorStatus.  # noqa: E501

        The actual position of the servo flange (in degrees) based on the encoder feedback  # noqa: E501

        :return: The position_feedback of this MotorStatus.  # noqa: E501
        :rtype: float
        """
        return self._position_feedback

    @position_feedback.setter
    def position_feedback(self, position_feedback):
        """Sets the position_feedback of this MotorStatus.

        The actual position of the servo flange (in degrees) based on the encoder feedback  # noqa: E501

        :param position_feedback: The position_feedback of this MotorStatus.  # noqa: E501
        :type: float
        """

        self._position_feedback = position_feedback

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MotorStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
