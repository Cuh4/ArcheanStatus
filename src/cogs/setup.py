# // ---------------------------------------------------------------------
# // ------- Setup
# // ---------------------------------------------------------------------

"""
A cog containing commands relating to status setup.
Repo: https://github.com/cuhHub/ArcheanStatus

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
import discord
from discord.ext import commands
from bot import Bot

from libs import embeds

# ---- // Main
class Setup(commands.Cog):
    def __init__(self, bot: Bot):
        self.Bot = bot

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def setup(self, context: commands.Context, channel: discord.TextChannel):
        """
        Sets the status channel for the server.
        """

        await context.send(embed = embeds.Success(""))