# (C) Datadog, Inc. 2018
# All rights reserved
# Licensed under Simplified BSD License (see LICENSE)
import pytest

from stackstate_checks.kafka_consumer import KafkaCheck
from .common import is_supported

pytestmark = pytest.mark.skipif(
    not is_supported('kafka'), reason='kafka consumer offsets not supported in current environment'
)


BROKER_METRICS = ['kafka.broker_offset']

CONSUMER_METRICS = ['kafka.consumer_offset', 'kafka.consumer_lag']


@pytest.mark.usefixtures('sts_environment')
def test_check_kafka(aggregator, kafka_instance):
    """
    Testing Kafka_consumer check.
    """
    kafka_consumer_check = KafkaCheck('kafka_consumer', {}, [kafka_instance])
    kafka_consumer_check.check(kafka_instance)

    assert_check_kafka(aggregator, kafka_instance)


@pytest.mark.e2e
def test_e2e(aggregator, kafka_instance):
    #aggregator = dd_agent_check(kafka_instance)

    assert_check_kafka(aggregator, kafka_instance)


def assert_check_kafka(aggregator, kafka_instance):
    for name, consumer_group in kafka_instance['consumer_groups'].items():
        for topic, partitions in consumer_group.items():
            for partition in partitions:
                tags = ["topic:{}".format(topic), "partition:{}".format(partition)] + ['optional:tag1']
                for mname in BROKER_METRICS:
                    aggregator.assert_metric(mname, tags=tags, at_least=1)
                for mname in CONSUMER_METRICS:
                    aggregator.assert_metric(mname, tags=tags + ["consumer_group:{}".format(name)], at_least=1)

    aggregator.assert_all_metrics_covered()
