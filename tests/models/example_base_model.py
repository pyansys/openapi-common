import pprint
from ansys.openapi.common import ModelBase


class ExampleBaseModel(ModelBase):
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

    swagger_types = {"model_type": "str"}

    attribute_map = {"model_type": "modelType"}

    discriminator_value_class_map = {"examplemodel": "ExampleModel"}

    def __init__(self, model_type=None):  # noqa: E501
        """Model - a model defined in Swagger"""  # noqa: E501
        self.discriminator = "modelType"
        self._model_type = model_type

    @property
    def model_type(self):
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        if model_type is None:
            raise ValueError(
                "Invalid value for `model_type`, must not be `None`"
            )  # noqa: E501

        self._model_type = model_type

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr in self.swagger_types.keys():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
