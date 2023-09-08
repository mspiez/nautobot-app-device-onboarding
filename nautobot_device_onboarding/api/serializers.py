"""Model serializers for the nautobot_device_onboarding REST API."""
# pylint: disable=duplicate-code

from rest_framework import serializers

from nautobot.core.api.serializers import ValidatedModelSerializer
from nautobot.dcim.models import Location, Platform
from nautobot.extras.models import Role

from nautobot_device_onboarding.models import OnboardingTask
from nautobot_device_onboarding.utils.credentials import Credentials, onboarding_credentials_serializer
from nautobot_device_onboarding.worker import enqueue_onboarding_task



class OnboardingTaskSerializer(ValidatedModelSerializer):
    # """Serializer for the OnboardingTask model."""

    class Meta:  # noqa: D106 "Missing docstring in public nested class"
        model = OnboardingTask

        fields = "__all__"

        read_only_fields = ["id", "created_device", "status", "failed_reason", "message"]

    # def create(self, validated_data):
    #     """Create an OnboardingTask and enqueue it for processing."""
    #     # Fields are string-type so default to empty (instead of None)
    #     username = validated_data.pop("username", "")
    #     password = validated_data.pop("password", "")
    #     secret = validated_data.pop("secret", "")

    #     credentials = Credentials(
    #         username=username,
    #         password=password,
    #         secret=secret,
    #     )

    #     onboarding_task = OnboardingTask.objects.create(**validated_data)

    #     enqueue_onboarding_task(onboarding_task.id, credentials)

    #     return onboarding_task
