import random
from PoEApiTools import PoeApiTools as pat
from discord.ext.commands import Bot

BOT_PREFIX = ("?", "!")
TOKEN = "XXXXXXX"

client = Bot(command_prefix=BOT_PREFIX)


@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


@client.command(name='check',
                description="""Works like this:
                
                                    !check "Currency Name" League
                                    
                               It is necessary to include the quotes.
                               Aliases for the command are '!pricecheck' '!price' '!equiv' !convert' '!CHECK' '!Check'
                            """,
                brief="---returns chaos equivalent of the currency you provide",
                aliases=['equiv', 'convert', 'CHECK', 'Check'])
async def check(currency, league):
    response = pat.PoeNinjaGetChaosEquiv(currencyTypeName=currency, league=league)

    await client.say("1 {0} is equal to ".format(currency) + str(response) + " chaos orbs.")


@client.command(name='compare',
                description="""Works like this:
                
                                    !check "Currency1" NumberOfCurrency1 "Currency2" League
                                    
                               It is necessary to include the quotes.
                            """,
                brief="---compares two currencies")
async def check(currency1, numCurrency1, currency2, league):
    print(currency1 + ", " + numCurrency1 + ", " + currency2 + ", " + league)
    response = pat.PoeNinjaGetCurrencyComparison(currencyTypeNameA=currency1, numCurrencyA=float(numCurrency1),
                                                 currencyTypeNameB=currency2, league=league)

    await client.say("{0} {1} is equal to ".format(numCurrency1, currency1)
                     + str('%.2f' % response) + " {0} in {1}".format(currency2, league))


@client.command(name='price',
                description="""Works like this:

                                    !price "item name" "Item Type" [c|ex] League
                                                    
                               Valid item types are:

                                    Unique Armor, Unique Weapon, Unique Flask, Map, Unique Map, Unique Accessory,
                                    Unique Jewel, Prophecy, Divination Card        

                               It is necessary to include the quotes and spell the item and type correctly.
                            """,
                brief='Prices unique items, cards and maps',
                aliases=['pricecheck'])
async def price(item, category, priceType, league):
    response = pat.PoeNinjaGetSingleItemPrice(itemName=item, itemValueType=priceType,
                                              itemCategory=category, league=league)

    await client.say("{0} is worth ".format(item)
                     + str('%.2f' % response) + " {0} in {1}".format(priceType, league))

client.run(TOKEN)
