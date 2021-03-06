# coding: utf-8

"""
    PMT API

    API for the XenonnT PMT database  # noqa: E501

    OpenAPI spec version: 0.1
    Contact: joe.mosbacher@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class PmtAfterpulse(object):
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
        'pmt_no': 'int',
        'run': 'int',
        'start_time': 'int',
        'end_time': 'int',
        'trigger_sigma': 'float',
        'total_ap': 'float',
        'pe': 'float',
        'pe_error': 'float',
        'ar_pos': 'float',
        'hv': 'float',
        'ne_ap': 'float',
        'ne_pos': 'float',
        'xe_pos': 'float',
        'n2_pos': 'float',
        'ch4_ap': 'float',
        'he_ap': 'float',
        'ar_ap': 'float',
        'doublexe_pos': 'float',
        'doublexe_ap': 'float',
        'trigger_mean': 'float',
        'gain': 'float',
        'ch4_pos': 'float',
        'n2_ap': 'float',
        'xe_ap': 'float',
        'pe_pulses': 'float',
        'trigger_number': 'float',
        'id': 'str'
    }

    attribute_map = {
        'pmt_no': 'pmt_no',
        'run': 'run',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'trigger_sigma': 'triggerSigma',
        'total_ap': 'totalAP',
        'pe': 'pe',
        'pe_error': 'peError',
        'ar_pos': 'arPos',
        'hv': 'HV',
        'ne_ap': 'neAP',
        'ne_pos': 'nePos',
        'xe_pos': 'xePos',
        'n2_pos': 'n2Pos',
        'ch4_ap': 'ch4AP',
        'he_ap': 'HeAp',
        'ar_ap': 'arAP',
        'doublexe_pos': 'doublexePos',
        'doublexe_ap': 'doublexeAP',
        'trigger_mean': 'triggerMean',
        'gain': 'Gain',
        'ch4_pos': 'ch4Pos',
        'n2_ap': 'n2AP',
        'xe_ap': 'xeAP',
        'pe_pulses': 'pePulses',
        'trigger_number': 'triggerNumber',
        'id': '_id'
    }

    def __init__(self, pmt_no=None, run=None, start_time=None, end_time=None, trigger_sigma=None, total_ap=None, pe=None, pe_error=None, ar_pos=None, hv=None, ne_ap=None, ne_pos=None, xe_pos=None, n2_pos=None, ch4_ap=None, he_ap=None, ar_ap=None, doublexe_pos=None, doublexe_ap=None, trigger_mean=None, gain=None, ch4_pos=None, n2_ap=None, xe_ap=None, pe_pulses=None, trigger_number=None, id=None):  # noqa: E501
        """PmtAfterpulse - a model defined in Swagger"""  # noqa: E501
        self._pmt_no = None
        self._run = None
        self._start_time = None
        self._end_time = None
        self._trigger_sigma = None
        self._total_ap = None
        self._pe = None
        self._pe_error = None
        self._ar_pos = None
        self._hv = None
        self._ne_ap = None
        self._ne_pos = None
        self._xe_pos = None
        self._n2_pos = None
        self._ch4_ap = None
        self._he_ap = None
        self._ar_ap = None
        self._doublexe_pos = None
        self._doublexe_ap = None
        self._trigger_mean = None
        self._gain = None
        self._ch4_pos = None
        self._n2_ap = None
        self._xe_ap = None
        self._pe_pulses = None
        self._trigger_number = None
        self._id = None
        self.discriminator = None
        if pmt_no is not None:
            self.pmt_no = pmt_no
        if run is not None:
            self.run = run
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if trigger_sigma is not None:
            self.trigger_sigma = trigger_sigma
        if total_ap is not None:
            self.total_ap = total_ap
        if pe is not None:
            self.pe = pe
        if pe_error is not None:
            self.pe_error = pe_error
        if ar_pos is not None:
            self.ar_pos = ar_pos
        if hv is not None:
            self.hv = hv
        if ne_ap is not None:
            self.ne_ap = ne_ap
        if ne_pos is not None:
            self.ne_pos = ne_pos
        if xe_pos is not None:
            self.xe_pos = xe_pos
        if n2_pos is not None:
            self.n2_pos = n2_pos
        if ch4_ap is not None:
            self.ch4_ap = ch4_ap
        if he_ap is not None:
            self.he_ap = he_ap
        if ar_ap is not None:
            self.ar_ap = ar_ap
        if doublexe_pos is not None:
            self.doublexe_pos = doublexe_pos
        if doublexe_ap is not None:
            self.doublexe_ap = doublexe_ap
        if trigger_mean is not None:
            self.trigger_mean = trigger_mean
        if gain is not None:
            self.gain = gain
        if ch4_pos is not None:
            self.ch4_pos = ch4_pos
        if n2_ap is not None:
            self.n2_ap = n2_ap
        if xe_ap is not None:
            self.xe_ap = xe_ap
        if pe_pulses is not None:
            self.pe_pulses = pe_pulses
        if trigger_number is not None:
            self.trigger_number = trigger_number
        if id is not None:
            self.id = id

    @property
    def pmt_no(self):
        """Gets the pmt_no of this PmtAfterpulse.  # noqa: E501


        :return: The pmt_no of this PmtAfterpulse.  # noqa: E501
        :rtype: int
        """
        return self._pmt_no

    @pmt_no.setter
    def pmt_no(self, pmt_no):
        """Sets the pmt_no of this PmtAfterpulse.


        :param pmt_no: The pmt_no of this PmtAfterpulse.  # noqa: E501
        :type: int
        """

        self._pmt_no = pmt_no

    @property
    def run(self):
        """Gets the run of this PmtAfterpulse.  # noqa: E501


        :return: The run of this PmtAfterpulse.  # noqa: E501
        :rtype: int
        """
        return self._run

    @run.setter
    def run(self, run):
        """Sets the run of this PmtAfterpulse.


        :param run: The run of this PmtAfterpulse.  # noqa: E501
        :type: int
        """

        self._run = run

    @property
    def start_time(self):
        """Gets the start_time of this PmtAfterpulse.  # noqa: E501


        :return: The start_time of this PmtAfterpulse.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this PmtAfterpulse.


        :param start_time: The start_time of this PmtAfterpulse.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this PmtAfterpulse.  # noqa: E501


        :return: The end_time of this PmtAfterpulse.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this PmtAfterpulse.


        :param end_time: The end_time of this PmtAfterpulse.  # noqa: E501
        :type: int
        """

        self._end_time = end_time

    @property
    def trigger_sigma(self):
        """Gets the trigger_sigma of this PmtAfterpulse.  # noqa: E501


        :return: The trigger_sigma of this PmtAfterpulse.  # noqa: E501
        :rtype: float
        """
        return self._trigger_sigma

    @trigger_sigma.setter
    def trigger_sigma(self, trigger_sigma):
        """Sets the trigger_sigma of this PmtAfterpulse.


        :param trigger_sigma: The trigger_sigma of this PmtAfterpulse.  # noqa: E501
        :type: float
        """

        self._trigger_sigma = trigger_sigma

    @property
    def total_ap(self):
        """Gets the total_ap of this PmtAfterpulse.  # noqa: E501


        :return: The total_ap of this PmtAfterpulse.  # noqa: E501
        :rtype: float
        """
        return self._total_ap

    @total_ap.setter
    def total_ap(self, total_ap):
        """Sets the total_ap of this PmtAfterpulse.


        :param total_ap: The total_ap of this PmtAfterpulse.  # noqa: E501
        :type: float
        """

        self._total_ap = total_ap

    @property
    def pe(self):
        """Gets the pe of this PmtAfterpulse.  # noqa: E501


        :return: The pe of this PmtAfterpulse.  # noqa: E501
        :rtype: float
        """
        return self._pe

    @pe.setter
    def pe(self, pe):
        """Sets the pe of this PmtAfterpulse.


        :param pe: The pe of this PmtAfterpulse.  # noqa: E501
        :type: float
        """

        self._pe = pe

    @property
    def pe_error(self):
        """Gets the pe_error of this PmtAfterpulse.  # noqa: E501


        :return: The pe_error of this PmtAfterpulse.  # noqa: E501
        :rtype: float
        """
        return self._pe_error

    @pe_error.setter
    def pe_error(self, pe_error):
        """Sets the pe_error of this PmtAfterpulse.


        :param pe_error: The pe_error of this PmtAfterpulse.  # noqa: E501
        :type: float
        """

        self._pe_error = pe_error

    @property
    def ar_pos(self):
        """Gets the ar_pos of this PmtAfterpulse.  # noqa: E501


        :return: The ar_pos of this PmtAfterpulse.  # noqa: E501
        :rtype: float
        """
        return self._ar_pos

    @ar_pos.setter
    def ar_pos(self, ar_pos):
        """Sets the ar_pos of this PmtAfterpulse.


        :param ar_pos: The ar_pos of this PmtAfterpulse.  # noqa: E501
        :type: float
        """

        self._ar_pos = ar_pos

    @property
    def hv(self):
        """Gets the hv of this PmtAfterpulse.  # noqa: E501


        :return: The hv of this PmtAfterpulse.  # noqa: E501
        :rtype: float
        """
        return self._hv

    @hv.setter
    def hv(self, hv):
        """Sets the hv of this PmtAfterpulse.


        :param hv: The hv of this PmtAfterpulse.  # noqa: E501
        :type: float
        """

        self._hv = hv

    @property
    def ne_ap(self):
        """Gets the ne_ap of this PmtAfterpulse.  # noqa: E501


        :return: The ne_ap of this PmtAfterpulse.  # noqa: E501
        :rtype: float
        """
        return self._ne_ap

    @ne_ap.setter
    def ne_ap(self, ne_ap):
        """Sets the ne_ap of this PmtAfterpulse.


        :param ne_ap: The ne_ap of this PmtAfterpulse.  # noqa: E501
        :type: float
        """

        self._ne_ap = ne_ap

    @property
    def ne_pos(self):
        """Gets the ne_pos of this PmtAfterpulse.  # noqa: E501


        :return: The ne_pos of this PmtAfterpulse.  # noqa: E501
        :rtype: float
        """
        return self._ne_pos

    @ne_pos.setter
    def ne_pos(self, ne_pos):
        """Sets the ne_pos of this PmtAfterpulse.


        :param ne_pos: The ne_pos of this PmtAfterpulse.  # noqa: E501
        :type: float
        """

        self._ne_pos = ne_pos

    @property
    def xe_pos(self):
        """Gets the xe_pos of this PmtAfterpulse.  # noqa: E501


        :return: The xe_pos of this PmtAfterpulse.  # noqa: E501
        :rtype: float
        """
        return self._xe_pos

    @xe_pos.setter
    def xe_pos(self, xe_pos):
        """Sets the xe_pos of this PmtAfterpulse.


        :param xe_pos: The xe_pos of this PmtAfterpulse.  # noqa: E501
        :type: float
        """

        self._xe_pos = xe_pos

    @property
    def n2_pos(self):
        """Gets the n2_pos of this PmtAfterpulse.  # noqa: E501


        :return: The n2_pos of this PmtAfterpulse.  # noqa: E501
        :rtype: float
        """
        return self._n2_pos

    @n2_pos.setter
    def n2_pos(self, n2_pos):
        """Sets the n2_pos of this PmtAfterpulse.


        :param n2_pos: The n2_pos of this PmtAfterpulse.  # noqa: E501
        :type: float
        """

        self._n2_pos = n2_pos

    @property
    def ch4_ap(self):
        """Gets the ch4_ap of this PmtAfterpulse.  # noqa: E501


        :return: The ch4_ap of this PmtAfterpulse.  # noqa: E501
        :rtype: float
        """
        return self._ch4_ap

    @ch4_ap.setter
    def ch4_ap(self, ch4_ap):
        """Sets the ch4_ap of this PmtAfterpulse.


        :param ch4_ap: The ch4_ap of this PmtAfterpulse.  # noqa: E501
        :type: float
        """

        self._ch4_ap = ch4_ap

    @property
    def he_ap(self):
        """Gets the he_ap of this PmtAfterpulse.  # noqa: E501


        :return: The he_ap of this PmtAfterpulse.  # noqa: E501
        :rtype: float
        """
        return self._he_ap

    @he_ap.setter
    def he_ap(self, he_ap):
        """Sets the he_ap of this PmtAfterpulse.


        :param he_ap: The he_ap of this PmtAfterpulse.  # noqa: E501
        :type: float
        """

        self._he_ap = he_ap

    @property
    def ar_ap(self):
        """Gets the ar_ap of this PmtAfterpulse.  # noqa: E501


        :return: The ar_ap of this PmtAfterpulse.  # noqa: E501
        :rtype: float
        """
        return self._ar_ap

    @ar_ap.setter
    def ar_ap(self, ar_ap):
        """Sets the ar_ap of this PmtAfterpulse.


        :param ar_ap: The ar_ap of this PmtAfterpulse.  # noqa: E501
        :type: float
        """

        self._ar_ap = ar_ap

    @property
    def doublexe_pos(self):
        """Gets the doublexe_pos of this PmtAfterpulse.  # noqa: E501


        :return: The doublexe_pos of this PmtAfterpulse.  # noqa: E501
        :rtype: float
        """
        return self._doublexe_pos

    @doublexe_pos.setter
    def doublexe_pos(self, doublexe_pos):
        """Sets the doublexe_pos of this PmtAfterpulse.


        :param doublexe_pos: The doublexe_pos of this PmtAfterpulse.  # noqa: E501
        :type: float
        """

        self._doublexe_pos = doublexe_pos

    @property
    def doublexe_ap(self):
        """Gets the doublexe_ap of this PmtAfterpulse.  # noqa: E501


        :return: The doublexe_ap of this PmtAfterpulse.  # noqa: E501
        :rtype: float
        """
        return self._doublexe_ap

    @doublexe_ap.setter
    def doublexe_ap(self, doublexe_ap):
        """Sets the doublexe_ap of this PmtAfterpulse.


        :param doublexe_ap: The doublexe_ap of this PmtAfterpulse.  # noqa: E501
        :type: float
        """

        self._doublexe_ap = doublexe_ap

    @property
    def trigger_mean(self):
        """Gets the trigger_mean of this PmtAfterpulse.  # noqa: E501


        :return: The trigger_mean of this PmtAfterpulse.  # noqa: E501
        :rtype: float
        """
        return self._trigger_mean

    @trigger_mean.setter
    def trigger_mean(self, trigger_mean):
        """Sets the trigger_mean of this PmtAfterpulse.


        :param trigger_mean: The trigger_mean of this PmtAfterpulse.  # noqa: E501
        :type: float
        """

        self._trigger_mean = trigger_mean

    @property
    def gain(self):
        """Gets the gain of this PmtAfterpulse.  # noqa: E501


        :return: The gain of this PmtAfterpulse.  # noqa: E501
        :rtype: float
        """
        return self._gain

    @gain.setter
    def gain(self, gain):
        """Sets the gain of this PmtAfterpulse.


        :param gain: The gain of this PmtAfterpulse.  # noqa: E501
        :type: float
        """

        self._gain = gain

    @property
    def ch4_pos(self):
        """Gets the ch4_pos of this PmtAfterpulse.  # noqa: E501


        :return: The ch4_pos of this PmtAfterpulse.  # noqa: E501
        :rtype: float
        """
        return self._ch4_pos

    @ch4_pos.setter
    def ch4_pos(self, ch4_pos):
        """Sets the ch4_pos of this PmtAfterpulse.


        :param ch4_pos: The ch4_pos of this PmtAfterpulse.  # noqa: E501
        :type: float
        """

        self._ch4_pos = ch4_pos

    @property
    def n2_ap(self):
        """Gets the n2_ap of this PmtAfterpulse.  # noqa: E501


        :return: The n2_ap of this PmtAfterpulse.  # noqa: E501
        :rtype: float
        """
        return self._n2_ap

    @n2_ap.setter
    def n2_ap(self, n2_ap):
        """Sets the n2_ap of this PmtAfterpulse.


        :param n2_ap: The n2_ap of this PmtAfterpulse.  # noqa: E501
        :type: float
        """

        self._n2_ap = n2_ap

    @property
    def xe_ap(self):
        """Gets the xe_ap of this PmtAfterpulse.  # noqa: E501


        :return: The xe_ap of this PmtAfterpulse.  # noqa: E501
        :rtype: float
        """
        return self._xe_ap

    @xe_ap.setter
    def xe_ap(self, xe_ap):
        """Sets the xe_ap of this PmtAfterpulse.


        :param xe_ap: The xe_ap of this PmtAfterpulse.  # noqa: E501
        :type: float
        """

        self._xe_ap = xe_ap

    @property
    def pe_pulses(self):
        """Gets the pe_pulses of this PmtAfterpulse.  # noqa: E501


        :return: The pe_pulses of this PmtAfterpulse.  # noqa: E501
        :rtype: float
        """
        return self._pe_pulses

    @pe_pulses.setter
    def pe_pulses(self, pe_pulses):
        """Sets the pe_pulses of this PmtAfterpulse.


        :param pe_pulses: The pe_pulses of this PmtAfterpulse.  # noqa: E501
        :type: float
        """

        self._pe_pulses = pe_pulses

    @property
    def trigger_number(self):
        """Gets the trigger_number of this PmtAfterpulse.  # noqa: E501


        :return: The trigger_number of this PmtAfterpulse.  # noqa: E501
        :rtype: float
        """
        return self._trigger_number

    @trigger_number.setter
    def trigger_number(self, trigger_number):
        """Sets the trigger_number of this PmtAfterpulse.


        :param trigger_number: The trigger_number of this PmtAfterpulse.  # noqa: E501
        :type: float
        """

        self._trigger_number = trigger_number

    @property
    def id(self):
        """Gets the id of this PmtAfterpulse.  # noqa: E501


        :return: The id of this PmtAfterpulse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PmtAfterpulse.


        :param id: The id of this PmtAfterpulse.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if issubclass(PmtAfterpulse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PmtAfterpulse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
