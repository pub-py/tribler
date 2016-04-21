from distutils.core import setup
from Tribler.Core.version import version_id

setup(
    name='libtribler',
    version=str(version_id),
    author='Tribler',
    packages=[
        'Tribler',
        'Tribler.Category',
        'Tribler.Core',
        'Tribler.Core.APIImplementation',
        'Tribler.Core.CacheDB',
        'Tribler.Core.DecentralizedTracking',
        'Tribler.Core.DecentralizedTracking.pymdht',
        'Tribler.Core.DecentralizedTracking.pymdht.core',
        'Tribler.Core.DecentralizedTracking.pymdht.plugins',
        'Tribler.Core.DecentralizedTracking.pymdht.profiler',
        'Tribler.Core.DecentralizedTracking.pymdht.profiler.parsers',
        'Tribler.Core.DecentralizedTracking.pymdht.ui',
        'Tribler.Core.DecentralizedTracking.pymdht.ut2mdht',
        'Tribler.Core.Libtorrent',
        'Tribler.Core.Modules',
        'Tribler.Core.Modules.channel',
        'Tribler.Core.Modules.restapi',
        'Tribler.Core.TFTP',
        'Tribler.Core.TorrentChecker',
        'Tribler.Core.Upgrade',
        'Tribler.Core.Utilities',
        'Tribler.Core.Video',
        'Tribler.Main',
        'Tribler.Main.Dialogs',
        'Tribler.Main.Emercoin',
        'Tribler.Main.Utility',
        'Tribler.Main.vwxGUI',
        'Tribler.Main.webUI',
        'Tribler.Utilities',
        'Tribler.community',
        'Tribler.community.allchannel',
        'Tribler.community.bartercast4',
        'Tribler.community.channel',
        'Tribler.community.demers',
        'Tribler.community.multichain',
        'Tribler.community.search',
        'Tribler.community.template',
        'Tribler.community.tunnel',
        'Tribler.community.tunnel.Socks5',
        'Tribler.community.tunnel.crypto',
        'Tribler.dispersy',
        'Tribler.dispersy.discovery',
        'Tribler.dispersy.libnacl.libnacl',
        'Tribler.dispersy.tool',
        'Tribler.dispersy.tracker',
    ],

    url='https://github.com/Tribler/tribler',
    license='LICENSE.txt',
    description='AT3 package for Python for Android',
    package_data={
        'Tribler': [
            'schema_sdb_v28.sql',
            'anon_test.torrent'],
        'Tribler.Category': [
            'filter_terms.filter',
            'category.conf'],
        'Tribler.Core.DecentralizedTracking.pymdht.core': [
            'bootstrap_stable',
            'bootstrap_unstable'],
    },
    long_description='This is the core tribler functionality package which is used for the android app.',
)
