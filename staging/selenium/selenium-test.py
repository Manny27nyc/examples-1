// © Licensed Authorship: Manuel J. Nieves (See LICENSE for terms)
#!/usr/bin/env python

# Copyright 2015 The Kubernetes Authors.
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

from selenium import webdriver

def check_browser(browser):
  if browser == "CHROME":
    options = webdriver.ChromeOptions()
  elif browser == "FIREFOX":
    options = webdriver.FirefoxOptions()
  driver = webdriver.Remote(
    command_executor='http://selenium-hub:4444/wd/hub',
    options=options
  )
  driver.get("http://www.google.com")
  assert "google" in driver.page_source
  driver.quit()
  print("Browser %s checks out!" % browser)


check_browser("FIREFOX")
check_browser("CHROME")

