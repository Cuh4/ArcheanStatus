# // ---------------------------------------------------------------------
# // ------- Archean Status
# // ---------------------------------------------------------------------

"""
A Discord bot for displaying the status of an Archean server.
Repo: https://github.com/Cuh4/ArcheanStatus

---

Copyright (C) 2024 Cuh4

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# ---- // Imports
from libs.archean import (
    Archean
)

import libs.env as env
from libs.db import Database 

from bot import Bot

# ---- // Main
# Create database
database = Database(env.GetDatabasePath(), {
    "status_message_id" : None
})

# Create bot
bot = Bot(database, Archean())

# Run bot
bot.run(env.GetBotToken())