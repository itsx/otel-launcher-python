# Copyright Lightstep Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from logging import getLogger

from opentelemetry.exporter.otlp.metrics_exporter import OTLPMetricsExporter

_logger = getLogger(__name__)


class LightstepOTLPMetricsExporter(OTLPMetricsExporter):
    def export(self, *args, **kwargs):
        try:
            super().export(*args, **kwargs)
        except Exception as error:
            _logger.exception(
                "Unable to export metrics to satellite: %s", error
            )
            raise