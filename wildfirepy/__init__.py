from wildfirepy import net
from wildfirepy import coordinates
from wildfirepy import io

__all__ = ['net', 'coordinates', 'io']

from pkg_resources import get_distribution, DistributionNotFound
try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    pass  # package is not installed
