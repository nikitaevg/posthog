from django.db import models


class AlertCheck(models.Model):
    class CheckResult(models.TextChoices):
        NormalValue = "NORMAL_VALUE"
        Anomaly = "ANOMALY"
        Error = "ERROR"

    alert: models.ForeignKey = models.ForeignKey("posthog.Alert", on_delete=models.CASCADE)
    checked_at: models.DateTimeField = models.DateTimeField(auto_now_add=True, blank=True)
    calculated_value: models.FloatField = models.FloatField(null=True)
    anomaly_condition: models.JSONField = models.JSONField(default=dict)
    check_result: models.CharField = models.CharField(max_length=20, choices=CheckResult.choices)
    error_message: models.TextField = models.TextField(null=True)
