# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the License);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an AS IS BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
""" Core component """

from typing import Any, Dict, List, Tuple

from score.dimensions.dimension import Dimension


class FieldSelection(Dimension):
  """ Quantifies whether the correct fields were mapped (versus ignored) """
  def __init__(self, *, translations=Dict[str, List[Tuple[str, Any]]]):
    super().__init__(translations=translations)

    solution_fields = set(
        map(lambda item: item[1].raw_field_name, translations['solution']))
    proposed_fields = set(
        map(lambda item: item[1].raw_field_name, translations['proposed']))

    correct_fields = proposed_fields.intersection(solution_fields)
    incorrect_fields = proposed_fields.difference(solution_fields)

    self.correct_reporting = len(correct_fields)
    self.correct_ceiling_reporting = len(set(translations['solution']))
    self.incorrect_reporting = len(incorrect_fields)
