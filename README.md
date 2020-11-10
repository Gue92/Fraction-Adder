# Fraction Adder
Program for the mathematical addition of two simple fractions.

## Application
- The function "add-frac" is used for the calculation. (Without exclamation marks).
- The function input of the two fractions is used as follows: add-frac( counter 1, nominator 1, counter 2, nominator 2 )
- The result will be displayed as text with numbers and special characters.
- The function is mainly executed with if & else conditions.

## Function Workflow
- 1.) The function sequence starts with a check for zero divisions.
- 2.) The fractions are expanded to the common denominator and added together.
- 3.) A check is made to see if the new counter is zero and if it is, it will be returned (the function stops).
- 4.) To simplify the fractions, the common divisor of numerator and denominator is searched.
- 5.) The numerator and denominator are divided by the common divisor.
- 6.) In the last step the function checks if the numerator and the denominator are equal or if the denominator is 1 before outputting the result.

### Further user information
- The code is one of my first projects, so variables and comments are written in German.
- The last extension and revision of the function was carried out subsequently, already dispensing with cumbersome variables.
- The language used does not influence input or output.
- The programme only calculates the addition product of two simple fractions.


### License declaration
Copyright 2020 Guenther Kaffenda

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
