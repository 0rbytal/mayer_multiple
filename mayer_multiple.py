#!/bin/python
import datetime
import time
import requests
import re
from lxml import html
import tweepy		# pip install tweepy

all_cryptos = ['bitcoin', 'ethereum', 'ripple', 'bitcoin-cash', 'litecoin', 'neo', 'cardano', 'stellar', 'eos', 
'monero', 'dash', 'iota', 'nem', 'tron', 'ethereum-classic', 'tether', 'vechain', 'nano', 'lisk', 'omisego', 
'bitcoin-gold', 'qtum', 'zcash', 'icon', 'binance-coin', 'digixdao', 'steem', 'populous', 'bytecoin-bcn', 'waves', 
'verge', 'stratis', 'rchain', 'maker', 'status', 'dogecoin', 'siacoin', 'bitshares', 'decred', 'aeternity', 
'waltonchain', 'augur', 'komodo', '0x', 'bytom', 'veritaseum', 'electroneum', 'ark', 'cryptonex', 'kucoin-shares', 
'zilliqa', 'ardor', 'syscoin', 'dragonchain', 'basic-attention-token', 'gas', 'hshare', 'golem', 'digibyte', 'pivx', 
'ethos', 'aion', 'monacoin', 'qash', 'factom', 'loopring', 'nebulas', 'funfair', 'byteball', 'revain', 'particl', 
'dentacoin', 'aelf', 'reddcoin', 'zcoin', 'salt', 'gxchain', 'kyber-network', 'chainlink', 'polymath-network', 'kin', 
'nxt', 'dent', 'iostoken', 'smartcash', 'bancor', 'power-ledger', 'nexus', 'emercoin', 'iconomi', 'neblio', 
'singularitynet', 'sirin-labs-token', 'enigma-project', 'request-network', 'tenx', 'bitcore', 'maidsafecoin', 
'pillar', 'cindicator', 'genesis-vision', 'blocknet', 'storj', 'gnosis-gno', 'vertcoin', 'bitcoindark', 'gamecredits', 
'quantstamp', 'achain', 'enjin-coin', 'raiden-network-token', 'santiment', 'rlc', 'paypie', 'ignis', 'pura', 'civic', 
'theta-token', 'minexcoin', 'substratum', 'aragon', 'xpa', 'wax', 'monaco', 'zencash', 'ubiq', 'skycoin', 'nav-coin', 
'metal', 'decentraland', 'salus', 'dynamic-trading-rights', 'nuls', 'credits', 'digitalnote', 'poet', 'blockv', 'asch', 
'arcblock', 'experience-points', 'storm', 'high-performance-blockchain', 'sophiatx', 'adx-net', 'spacechain', 'fusion', 
'time-new-bank', 'ethlend', 'bridgecoin', 'telcoin', 'envion', 'oyster', 'ion', 'edgeless', 'c20', 'poa-network', 
'medibloc', 'simple-token', 'bluzelle', 'agoras-tokens', 'medishares', 'sonm', 'peercoin', 'dew', 'bitbay', 
'quantum-resistant-ledger', 'vibe', 'ambrosus', 'burst', 'red-pulse', 'melon', 'bibox-token', 'eidoo', 'wings', 
'streamr-datacoin', 'spankchain', 'ripio-credit-network', 'iot-chain', 'wagerr', 'cloakcoin', 'library-credits', 
'singulardtv', 'bread', 'origintrail', 'mobilego', 'feathercoin', 'ink', 'utrust', 'deepbrain-chain', 'ins-ecosystem', 
'html-coin', 'jibrel-network', 'universa', 'wabi', 'atmchain', 'viacoin', 'einsteinium', 'rise', 'gulden', 'naga', 
'smartmesh', 'taas', 'metaverse', 'wepower', 'decision-token', 'delphy', 'appcoins', 'cobinhood', 'xtrabytes', 
'cybermiles', 'data', 'etherparty', 'gifto', 'counterparty', 'synereo', 'aeon', 'cpchain', 'modum', 'refereum', 
'bottos', 'district0x', 'groestlcoin', 'zclassic', 'mobius', 'lunyr', 'trinity-network-credit', 'cofound-it', 
'kickico', 'blockmason', 'indahash', 'unikoin-gold', 'adtoken', 'airswap', 'decent', 'centra', 'presearch', 
'crown', 'blox', 'swarm-fund', 'tierion', 'ucash', 'hive-project', 'datum', 'dimecoin', 'humaniq', 'tokencard', 
'viberate', 'unobtanium', 'bitcny', 'shift', 'medicalchain', 'sibcoin', 'ecc', 'mooncoin', 'zeepin', 'crypterium', 
'pepe-cash', 'qlink', 'namecoin', 'triggers', 'spectre-dividend', 'flash', 'numeraire', 'everex', 'whitecoin', 
'nimiq', 'ormeus-coin', 'safe-exchange-coin', 'blockport', 'steem-dollars', 'iocoin', 'soarcoin', 'vericoin', 
'colossuscoinxt', 'potcoin', 'mercury', 'deeponion', 'voxels', 'diamond', 'blackcoin', 'lykke', 'bean-cash', 
'internet-node-token', 'paragon', 'leocoin', 'suncontract', 'faircoin', 'monetha', 'dadi', 'zap', 'bloom', 'stk', 
'lamden', 'coss', 'cappasity', 'odyssey', 'swissborg', 'grid', 'aeron', 'linkeye', 'newyorkcoin', 'yoyow', 
'hi-mutual-society', 'matchpool', 'mothership', 'trust', 'uquid-coin', 'blackmoon', 'elastic', 'expanse', 
'zeusshield', 'domraider', 'dai', 'mintcoin', 'posw-coin', 'trade-token', 'nolimitcoin', 'swftcoin', 'target-coin', 
'qunqun', 'maecenas', 'zoin', 'selfkey', 'qbao', 'gridcoin', 'aurora-dao', 'pascal-coin', 'blocktix', 'peerplays', 
'energo', 'moeda-loyalty-points', 'game', 'alqo', 'encrypgen', 'carvertical', 'insurepal', 'omni', 'radium', 
'latoken', 'hempcoin', 'bitconnect', 'all-sports', 'agrello', 'firstblood', 'waves-community-token', 'covesting', 
'propy', 'true-chain', 'electra', 'solarcoin', 'primecoin', 'monetaryunit', 'icos', 'e-dinar-coin', 'rivetz', 
'canyacoin', 'restart-energy-mwat', 'divi', 'florincoin', 'oax', 'earthcoin', 'boolberry', 'bitsend', 'bitusd', 
'bitdegree', 'investfeed', 'energycoin', 'bodhi', 'databits', 'swarm-city', 'neumark', 'okcash', 'phore', 'prizm', 
'bitclave', 'olympus-labs', 'b2bx', 'shield', 'spectrecoin', 'rubycoin', 'auroracoin', 'payfair', 'everus', 'myriad', 
'hubii-network', 'mybit-token', 'remme', 'incent', 'golos', 'clams', 'rialto', 'chronobank', 'etheroll', 'musicoin', 
'stox', 'fidentiax', 'lomocoin', 'axpire', 'bitdice', 'neoscoin', 'toacoin', 'fedoracoin', 'pluton', 
'open-trading-network', 'ixledger', 'quantum', 'alis', 'hacken', 'exchange-union', 'universal-currency', 'xaurum', 
'airtoken', 'patientory', 'prochain', 'nvo', 'pandacoin', 'nexium', 'snovio', 'espers', 'transfercoin', 'nubits', 
'e-coin', 'gambit', 'decentbet', 'syndicate', 'bismuth', 'measurable-date-token', 'hackspace-capital', 'blue', 
'luxcoin', 'dynamic', 'neutron', 'mysterium', 'blockcat', 'foldingcoin', 'oraclechain', 'hydro-protocol', 'tiesdb', 
'gobyte', 'atbcoin', 'lockchain', 'primas', 'internet-of-poeple', 'hedge', 'the-champcoin', 'sportyco', 'dubaicoin', 
'ethorse', 'greencoin', 'coinfi', 'polybius', 'solaris', 'cargox', 'rebellious', 'circuits-of-value', 'bounty0x', 
'voise', 'polis', 'oneroot-network', 'spectre-utility', 'curecoin', 'zeitcoin', 'kilocoin', 'pinkcoin', 'get-protocol', 
'chips', 'novacoin', 'oxycoin', 'sphere', 'ink-protocol', 'leverj', 'linda', 'change', 'aventus', 'worldcore', 
'pareto-network', 'bitcrystals', 'echolink', 'vcash', 'kore', 'profile-utilility-token', 'b3coin', 'dcorp', 
'clearpoll', 'coinmeet', 'stealthcoin', 'elixir', 'hellogold', 'ebitcoin', 'biocoin', 'bezop', 'sequence', 
'heat-leadger', 'atmos', 'pirl', 'playkey', 'aidcoin', 'bitcoinz', 'farad', 'karma', 'obits', 'dopecoin', 
'uniform-fiscal-object', 'devery', 'block-array', 'flixxo', 'bitmark', 'breakout-stake', 'locicoin', 'cvcoin', 'vezt', 
'sureremit', 'hyperstake', 'artbyte', 'sether', 'starbase', 'memetic', 'qwark', 'smartlands', 'trueflip', 'apx', 
'elite', 'aichain', 'astro', 'gatcoin', 'autonio', 'denarius', 'vtorrent', 'synergy', 'pesetacoin', 'europecoin', 
'travelflex', 'iungo', 'eroscoin', 'russiacoin', 'global-currency-reserve', 'bela', 'exclusivecoin', 'hush', 'lampix', 
'bitcoin-plus', 'tokenbox', 'veriumreserve', 'encryptotel', 'herocoin', 'sumokoin', 'adbank', 'bitcloud', 'internxt', 
'vsync', 'putincoin', 'goldcoin', 'zrcoin', 'dotcoin', 'opus', 'publica', 'masternodecoin', 'monkey-project', 'aigang', 
'breakout', 'flik', 'zilla', 'creditbit', 'mcap', 'starta', 'sharechain', 'riecoin', 'primalbase-token', 'viuly', 
'digipulse', 'draftcoin', 'asiacoin', '2give', 'hawala.today', 'goldmint', 'global-jobcoin', 'huntercoin', 'upfiring', 
'cannabiscoin', 'exrnchain', 'altcoin', 'bonpay', 'luckchain', 'sprouts', 'audiocoin', 'karbo', 'tokes', 'vslice', 
'terracoin', 'teslacoin', 'tracto', 'dnotes', 'blitzcash', 'life', 'sociall', 'nushares', 'trezarcoin', 'wild-crypto', 
'social-send', 'adshares', 'bitswift', 'ergo', 'monoeci', 'obsidian', 'mywish', 'evergreencoin', 'gcn-coin', 'rex', 
'hollywoodcoin', 'trustplus', 'buzzcoin', 'atlant', 'yocoin', 'quark', 'bitwhite', 'giga-watt-token', 'zero', 
'creativecoin', 'spreadcoin', 'zephyr', 'verify', 'bluecoin', 'bitzeny', 'lendconnect', 'flypme', 'privatix', 
'indorse-token', 'real', 'chaincoin', 'startcoin', 'e-gulden', 'coinlancer', 'magi', 'martexcoin', 'starcredits', 
'bulwark', 'ellaism', 'sexcoin', 'xgox', 'jesus-coin', 'carboncoin', 'magnet', 'parkbyte', 'rupee', 
'speed-mining-service', 'litedoge', 'straks', 'sagacoin', 'hexx', 'student-coin', 'ethereum-movie-venture', 'micromoney', 
'oceanlab', 'regalcoin', 'innova', 'chronologic', 'linx', 'unity-ingot', 'interstellar-holdings', 'unbreakablecoin', 
'crypto-bullion', 'procurrency', 'ignition', 'intensecoin', 'qvolta', 'maza', 'force', 'ongsocial', 
'growers-international', 'inflationcoin', 'ganjacoin', 'embers', 'bitdeal', 'thegcccoin', 'equitrader', 'campuscoin', 
'condensate', 'eboost', 'fundyourselfnow', 'footy-cash', 'accelerator-network', 'leafcoin', 'pluscoin', 'adzcoin', 
'pure', 'digitalprice', 'eltcoin', 'cryptoping', 'unitus', 'pylon-network', 'renos', 'project-decorum', 'piplcoin', 
'vivo', 'op-coin', 'skincoin', 'photon', 'commodity-ad-network', 'ethersportz', 'smileycoin', 'i0coin', 'noblecoin', 
'unify', 'bytecent', 'magiccoin', "miners-reward-token", 'britcoin', 'fastcoin', '42-coin', 'cream', 'emphy', 
'biblepay', 'worldcoin', 'moin', 'arcticcoin', 'canada-ecoin', 'kolion', 'ethbits', 'crowdcoin', 'woodcoin', 'bata', 
'fujicoin', 'legends-room', 'bitpark-coin', 'bitair', 'bitradio', 'dinastycoin', 'zennies', 'machinecoin', 'platinumbar', 
'arbitragect', 'petrodollar', 'tigereum', 'leviarcoin', 'equal', 'zetacoin', 'fucktoken', 'centurion', 'roulettetoken', 
'soma', 'blakestar', 'guncoin', 'suretly', 'bitcoin-scrypt', 'quebecoin', 'netcoin', 'cryptocarbon', 'popularcoin', 
'kubera-coin', 'copico', 'wandx', 'abjcoin', 'deutsche-emark', 'intelligent-trading-tech', 'sugar-exchange', 
'hodlcoin', 'megacoin', 'poly-ai', 'skeincoin', 'cartaxi-token', 'elcoin', 'argentum', 'ethereum-cash', 'aerium', 
'ace', 'dfscoin', 'firstcoin', 'authorship', 'aquariuscoin', 'bittokens', 'bitgem', 'jetcoin', 'digitalcoin', 
'lanacoin', 'happycoin', 'cryptojacks', 'manna', 'titcoin', 'rupaya', 'blazecoin', 'wavesgo', 'tittiecoin', 
'minereum', 'trumpcoin', 'cryptonite', 'elementrem', 'mojocoin', 'ethereum-gold', 'triangles', 'rimbit', 'whalecoin', 
'netko', 'ebitcoincash', 'digital-developers-fund', 'visio', 'erc20', 'phoenixcoin', 'capricoin', 'iethereum', 
'supercoin', 'octanox', 'billionaire-token', 'royal-kingdom-coin', 'bitcoin-red', 'galactrum', 'steneum-coin', 
'litecoin-plus', 'pakcoin', 'bankcoin', 'swagbucks', 'goldblocks', 'hicoin', 'digicube', 'bitbtc', 'garlicoin', 
'phantomx', 'tokyo', 'pioneer-coin', 'tagcoin', 'postcoin', 'golfcoin', 'desire', 'adcoin', 'coin2-1', 'daxxcoin', 
'bolivarcoin', 'x-coin', 'mao-zedong', 'coinonatx', '808coin', 'confido', 'ammo-reloaded', 'kayicoin', 'newbium', 
'macron', 'influxcoin', 'funcoin', 'redcoin', 'helleniccoin', 'berncash', 'advanced-internet-blocks', 'ratecoin', 
'crystal-clear', 'homeblockcoin', 'chancoin', 'c-bit', 'octocoin', 'ethereum-dark', 'bitgold', 'atomic-coin', 
'briacoin', 'nevacoin', 'global-tour-coin', 'philosopher-stones', 'onix', 'spacecoin', 'icobid', 'stronghands', 
'bigup', 'ecocoin', 'qbic', 'pascal-lite', 'globalcoin', 'bitcoal', 'nekonium', 'leacoin', 'sooncoin', 'sixeleven', 
'votecoin', 'dix-asset', 'catcoin', 'yenten', 'dalecoin', 'prime-xi', 'bipcoin', 'fincoin', 'reecoin', 'eurocoin', 
'acoin', 'veltor', 'ronpaulcoin', 'trident-group', 'allsafe', 'speedcash', 'litebitcoin', 'eot-token', 'cachecoin', 
'impact', 'biteur', 'tajcoin', 'quazarcoin', 'artex-coin', 'theresa-may-coin', 'cannation', 'eryllium', 'neuro', 
'peepcoin', 'comet', 'zlancer', 'coinonat', 'sono', 'amsterdamcoin', 'spots', 'master-swiscoin', 'cthulhu-offerings', 
'kronecoin', 'womencoin', 'vaperscoin', 'litecoin-ultra', 'solarflarecoin', 'save-and-gain', 'torcoin', 'rawcoin', 
'veros', 'playercoin', 'crevacoin', 'ulatech', 'prcoin', 'vault-coin', 'harmonycoin', 'digital-money-bits', 'tao', 
'russian-mining-coin', 'bitqy', 'ecobit', 'credo', 'dao-casino', 'bunnycoin', 'virtacoin', 'xenon', 'blockpool', 
'cryptopay', 'dovu', 'mercury-protocol', 'eventchain', 'sense', 'bowhead', 'prospectors-gold', 'ixcoin', 'goodomy', 
'triaconta', 'yashcoin', 'bitboost', 'darcrus', 'incakoin', 'anoncoin', 'rustbits', 'version', 'fimkrypto', 'kekcoin', 
'orbitcoin', 'aurumcoin', 'neverdie', 'inpay', 'universe', 'fluttercoin', 'ico-openledger', 'insanecoin', 'etheriya', 
'qubitcoin', 'shadowcash', 'maxcoin', 'metalcoin', 'shorty', 'fantomcoin', 'piggycoin', 'scorecoin', 
'ultimate-secure-cash', 'ethbet', 'hitcoin', 'deuscoin', 'trollcoin', 'kobocoin', 'bitbar', 'cryptoforecast', 
'hobonickels', 'sovereign-hero', 'monster-byte', 'unicoin', 'datacoin', 'grimcoin', 'gaia', 'bit20', 'aricoin', 
'iticoin', 'eternity', 'smartcoin', 'motocoin', 'fuelcoin', 'bitstar', 'colossuscoin-v2', 'securecoin', 'nyancoin', 
'ultracoin', 'paycoin', 'btctalkcoin', 'halcyon', 'opal', 'valorbit', 'link-platform', 'bitcurrency', 'sterlingcoin', 
'joulecoin', 'purevidz', 'goldreserve', 'gapcoin', 'tigercoin', 'glasscoin', 'tattoocoin', 'signatum', 'blakecoin', 
'px', 'flycoin', 'droxne', 'sacoin', 'kurrent', 'chronos', 'blockpay', 'cypher', 'icoin', 'truckcoin', 'bitsilver', 
'coin', 'chesscoin', 'prototanium', 'tekcoin', 'kushcoin', 'mineum', '8bit', 'wayguide', 'marscoin', 'litebar', 
'bitcoin-fast', 'ambercoin', 'satoshimadness', 'cryptoinsight', 'zozocoin', 'cannacoin', 'bitz', 'cashcoin', 
'dashcoin', 'irishcoin', 'fujinto', 'revolvercoin', 'swing', 'roofs', 'evil-coin', 'globaltoken', 'virta-unique-coin', 
'xios', 'rubies', 'virtacoinplus', 'sproutsextreme', 'virtualcoin', 'gameunits', 'senderon', 'freicoin', 'peerguess', 
'dollarcoin', 'bumbacoin', 'honey', 'firecoin', 'sativacoin', 'joincoin', 'beatcoin', 'boostcoin', 'parallelcoin', 
'polcoin', 'independent-money-system', 'quatloo', 'globalboost-y', 'shadow-token', 'emerald-crypto', 'ccore', 'darsek', 
'mincoin', 'evotion', 'zurcoin', 'bitcoin-planet', 'jin-coin', 'paycon', 'yacoin', 'islacoin', 'mustangcoin', '300-token', 
'money', 'brother', 'franko', 'enigma', 'bitcoin-21', 'secretcoin', 'luna-coin', 'flaxscript', 'fuzzballs', 'gpu-coin', 
'madcoin', 'network-token', 'eaglecoin', 'hempcoin', 'allion', 'crypto', 'asiadigicoin', 'soilcoin', 'elacoin', 
'postoken', 'bolenum', 'guccionecoin', 'antibitcoin', 'creatio', 'goldpieces', 'compucoin', 'benjirolls', 'ripto-bux', 
'marijuanacoin', 'remicoin', 'idice', 'bnrtxcoin', 'starcash-network', 'bitasean', 'digital-rupees', 
'gold-pressed-latinum', 'metal-music-coin', 'shilling', 'bitquark', 'debitcoin', 'warp', 'californium', 'litecred', 
'billarycoin', 'songcoin', 'uro', 'bitcedi', 'cabbage', 'jewels', 'vectorai', 'printerium', 'sojourn', 'arbit', 
'cryptoescudo', 'dappster', 'slevin', 'mindcoin', 'wild-beast-block', 'ride-my-car', 'useless-ethereum-token', 
'zayedcoin', 'vip-tokens', 'g3n', 'blackstar', 'dreamcoin', 'milocoin', 'ponzicoin', 'unrealcoin', 'zetamicron', 'ego', 
'pulse', 'javascript-token', 'kingn-coin', 'orlycoin', 'iconic', 'coexistcoin', 'impulsecoin', 'braincoin', 'jobscoin', 
'posex', 'exchangen', 'zonecoin', 'steps', 'bowscoin', 'letitride', 'cryptoworldx-token', 'anarchistsprime', 
'healthywormcoin', 'bioscrypto', 'plncoin', 'piecoin', 'tagrcoin', 'geertcoin', 'crtcoin', 'destiny', 'boat', 'rsgpcoin', 
'osmiumcoin', 'credence-coin', 'gbcgoldcoin', 'xonecoin', 'high-voltage', 'bitvolt', 'agrolifecoin', 'dollar-online', 
'sydpak', 'antilitecoin', 'ibank', 'argus', 'coimatic-3.0', 'biobar', 'tychocoin', 'elysium', 'coupecoin', 'p7coin', 
'socialcoin', 'futurxe', 'concoin', 'project-x', 'coimatic-2', 'selfiecoin', 'nodecoin', 'magnum', 'geysercoin', 
'levoplus', 'caliphcoin', 'ccminer', 'tristar-coin', 'digital-credits', 'pizzacoin', 'abncoin', 'dibcoin', 
'ebittree-coin', 'atmcoin', 'ontology', 'huobi-token', 'nucleus-vision', 'oceanchain', 'educare', 'elastos', 
'electronic-pk-token', 'nework', 'ruff', 'bitcoin-diamond', 'ai-doctor', 'pundi-x', 'lightning-bitcoin', 'waykichain', 
'matryx', 'genaro-network', 'chatcoin', 'true-usd', 'paccoin', 'halalchain', 'aware', 'cube', 'clubcoin', 'eztoken', 
'education-ecosystem', 'hyper-pay', 'pressone', 'iht-real-estate-protocol', 'animation-vision-cash', 'electrifyasia', 
'selfsell', 'topchain', 'rock', 'lightchain', 'ofcoin', 'bankex', 'molecular-future', 'acute-angle-cloud', 'fortuna', 
'yee', 'fargocoin', 'ug-token', 'super-bitcoin', 'united-bitcoin', 'w3coin', 'show', 'kzcash', 'bitcoinx', 'spherepay', 
'matrix-ai-network', 'boscoin', 'mktcoin', 'fairgame', 'sharex', 'scryinfo', 'tez', 'realchain', 'cfun', 'read', 'moac', 
'iquant', 'tokenclub', 'babb', 'republic-protocol', 'gems-', 'thekey', 'investdigital', 'valuechain', 
'content-and-ad-network', 'lympo', 'litecoin-cash', 'qube', 'bigone-token', 'bee-token', 'kcash', 'tomochain', 
'filecoin', 'mergecoin', 'strikebitclub', 'comsa-xem', 'comsa-eth', 'atn', 'tidex-token', 'weth', 'jet8', 'bitsoar', 
'ugchain', 'infinity-economics', 'starchain', 'interplanetary-broadcast-coin', 'mixin', 'experty', 'titanium-blockchain', 
'gladius-token', 'animecoin', 'numus', 'aidos-kuneen', 'sphre-air', 'unlimitedip', 'jingtum-tech', 'reftoken', 
'techshares', 'datx', 'ea-coin', 'timescoin', 'coinpoker', 'neurotoken', 'maverick-chain', 'insights-network', 
'etherecash', 'zengold', 'dmarket', 'blockcdn', 'startercoin', 'cashaa', 'graft', 'alphacat', 'segwit2x', 'candy', 
'shekel', 'ipchain', 'msd', 'infchain', 'bt2-cst', 'entcash', 'datawallet', 'geocoin', 'golos-gold', 'dether', 
'acchain', 'magnetcoin', 'jiyo', 'gamechain', 'wincoin', 'hoqu', 'infinitecoin', 'copytrack', 'dimcoin', 'donationcoin', 
'topaz-coin', 'supernet', 'swaptoken', 'lepen', 'swisscoin', 'corion', 'superior-coin', 'uttoken', 'escroco', 
'pabyosi-coin-special', 'harvest-mastenode-coin', 'cryptopiafeeshares', 'davorcoin', 'wa-space', 'tokugawa', 'neo-gold', 
'encryptotel-eth', 'html5coin', 'bitcoin-atom', 'cloud', 'casinocoin', 'vpncoin', 'maggie', 'idex-membership', 
'crave', 'sparks', 'bitcoin-god', 'plexcoin', 'storjcoin-x', 'cyder', 'avatarcoin', 'gold-reward-token', 'high-gain', 
'president-johnson', 'first-bitcoin-capital', 'macro', 'musiconomi', 'grandcoin', 'alphabit', 'drp-utility', 
'internet-of-things', 'ox-fina', 'invisiblecoin', 'bitserial', 'ethereum-lite', 'dynamiccoin', 'wi-coin', 'btcmoon', 
'namocoin', 'rublebit', 'edrcoin', 'ur', 'blazercoin', 'terranova', 'indicoin', 'muse', 'cashme', 'flappycoin', 
'president-trump', 'fapcoin', 'zilbercoin', 'sjwcoin', 'shacoin', 'todaycoin', 'sharkcoin', 'royalties', 'rabbitcoin', 
'protean', 't-coin', 'birds', 'francs', 'numuscash', 'sisa', 'first-bitcoin', 'slothcoin', 'safecoin', 'sakuracoin', 
'hyper', 'wink', 'vulcano', 'xtd-coin', 'fireflycoin', 'universalroyalcoin', 'omicron', 'fazzcoin', 'nitro', 
'akuya-coin', 'cycling-coin', 'bitfid', 'moneycoin', 'gay-money', 'pokecoin', 'happy-creator-coin', 'ugain', 'topcoin', 
'landcoin', 'levocoin', 'goldmaxcoin', 'pirate-blocks', 'aces', 'zsecoin', 'bastonet', 'royalcoin', 'darklisk', 'minex', 
'dashs', 'india-coin', 'safe-trade-coin', 'wowcoin', 'sand-coin', 'batcoin', 'tellurion', 'primulon', 'thecreed', 
'alpacoin', 'yescoin', 'trickycoin', 'snakeeyes', 'anryze', 'avoncoin', 'egold', 'bestchain', 'wearesatoshi', 
'lazaruscoin', 'the-vegan-initiative', 'mobilecash', 'stex', 'turbocoin', 'natcoin', 'sportscoin', 'fonziecoin', 
'coffeecoin', 'hodl-bucks', 'dutch-coin', 'marxcoin', 'mmxvi', 'moneta', 'halloween-coin', 'psilocybin', 'opescoin', 
'betacoin', 'futcoin', 'antimatter', 'operand', 'shellcoin', 'cubits', 'deltacredits', 'granite', 'pinkdog', 'teamup', 
'netbit', 'voyacoin', 'digital-bullion-gold', 'bubble', 'runners', 'bitbase', 'linkedcoin', 'regacoin', 
'tattoocoin-limited', 'quotient', 'karmacoin', 'rcoin', 'sigmacoin', 'axiom', 'dubstep', 'bitok', 'eggcoin', 
'teslacoilcoin', 'bitalphacoin', 'smoke', 'uncoin', 'gameleaguecoin', 'cybercoin', 'paypeer', 'qora', 'klondikecoin', 
'xaucoin', 'x2', 'richcoin', 'prismchain', 'international-diamond', 'frankywillcoin', 'lathaan', 'kashhcoin', 'rhfcoin', 
'cheapcoin', 'huncoin', 'aseancoin', 'compcoin', 'lltoken', 'ocow', 'farstcoin', 'monero-gold'] 
# All the cryptocurrencies listed on coinmarketcap.com as of 11 March 2018

#functions
def get_coins():
	page = requests.get('https://coinmarketcap.com/all/views/all/')	# List all cryptocurrencies from coinmarketcap.com
    tree = html.fromstring(page.content)
	all_coins = tree.xpath('//a[@class="currency-name-container"]/text()')
	lower_case_list = map(str.lower, all_coins)		# makes all coins lower-case
	corrected_coin_list = [s.replace(' ','-') for s in lower_case_list]	# replaces all spaces with hyphens
	return corrected_coin_list
	
def visit(url):
	visited.add(url)
	extracted_body = requests.get(url).text
	matches = re.findall(http_re, extracted_body)
	for match in matches:
		if match not in visited :
		visit(match)

def build_url(coin):	# This function builds the URLs based on the coin being queried
	prefix = "https://coinmarketcap.com/currencies/"
	startdate = (datetime.datetime.now() - datetime.timedelta(days=200)).date().strftime('%Y%m%d')
	suffix = "/historical-data/?start=" + startdate + "&end=" + datetime.datetime.today().strftime('%Y%m%d')
	new_url = prefix + coin + suffix
	return new_url

def get_current_price(coin):	# This function grabs the current price of the coin being queried
	page = requests.get(build_url(coin))
	tree = html.fromstring(page.content)
	current_price = tree.xpath('//span[@class="text-large2"]/text()')
	return float(current_price[0])

def pull_prices(coin):		# This function retrieves the last 200 days of prices from the coin's page
	page = requests.get('build_url(coin)')
	tree = html.fromstring(page.content)
	all_prices = tree.xpath('//td[@data-format-fiat]/text()')
	return all_prices

def mayer_multiple(coin):	# This function calculates the Mayer Multiple for the coin
	closing_prices = pull_prices(coin)[3::4] # filtering the closing prices from the entire list
	moving_avg = sum([float(i) for i in closing_prices])/len(closing_prices)
	m_multiple = get_current_price(coin) / moving_avg
	return round(m_multiple, 2)
	
def get_api(cfg):
	auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
 	auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
	return tweepy.API(auth)

def tweet_msg(coin, current_price, m_multiple):	# This function tweets a message based on the Mayer Multiple
	if m_mupltiple < 0.9:
		message = "BUY alert: " + coin + " has a current price of $" + current_price + " and a current mayer multiple of " + str(m_multiple)
		tweet(message)
	elif m_multiple > 2.4:
		message = "SELL alert: " + coin + " has a current price of $" + current_price + " and a current mayer multiple of " + str(m_multiple)
		tweet(message)
	else:
		return

def main():
	while True:
		undervalued = []
		overvalued = []
		for crypto in all_cryptos:
			current_coin = str(crypto)
			if len(pull_prices(current_coin)) < 800:
				time.sleep(.5)
			else:
				current_price = str(get_current_price(current_coin))
				m_multiple = mayer_multiple(current_coin)

				if m_multiple < 0.9:
					tweet_msg(current_coin, current_price, m_multiple)
					if current_coin not in undervalued:
						undervalued.append(current_coin)
				elif m_multiple > 2.5:
					tweet_msg(current_coin, current_price, m_multiple)
					if current_coin not in overvalued:
						overvalued.append(current_coin)
				else:
					time.sleep(.5)
			time.sleep(.1)
		print "Currently UNDERvalued [i.e., BUY!]:"
		print undervalued
		print "\nCurrently OVERvalued [i.e., SELL!]:"
		print overvalued
		time.sleep(300)

if __name__ == "__main__":
  main()
