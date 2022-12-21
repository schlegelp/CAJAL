from .._shared.utils import channel_as_last_axis as channel_as_last_axis, identity as identity, reshape_nd as reshape_nd, slice_at_axis as slice_at_axis
from ..util import dtype as dtype, dtype_limits as dtype_limits
from _typeshed import Incomplete

def convert_colorspace(arr, fromspace, tospace, *, channel_axis: int = ...): ...
def rgba2rgb(rgba, background=..., *, channel_axis: int = ...): ...
def rgb2hsv(rgb, *, channel_axis: int = ...): ...
def hsv2rgb(hsv, *, channel_axis: int = ...): ...

cie_primaries: Incomplete
sb_primaries: Incomplete
xyz_from_rgb: Incomplete
rgb_from_xyz: Incomplete
xyz_from_rgbcie: Incomplete
rgbcie_from_xyz: Incomplete
rgbcie_from_rgb: Incomplete
rgb_from_rgbcie: Incomplete
gray_from_rgb: Incomplete
yuv_from_rgb: Incomplete
rgb_from_yuv: Incomplete
yiq_from_rgb: Incomplete
rgb_from_yiq: Incomplete
ypbpr_from_rgb: Incomplete
rgb_from_ypbpr: Incomplete
ycbcr_from_rgb: Incomplete
rgb_from_ycbcr: Incomplete
ydbdr_from_rgb: Incomplete
rgb_from_ydbdr: Incomplete
lab_ref_white: Incomplete
illuminants: Incomplete

def get_xyz_coords(illuminant, observer, dtype=...): ...

rgb_from_hed: Incomplete
hed_from_rgb: Incomplete
rgb_from_hdx: Incomplete
hdx_from_rgb: Incomplete
rgb_from_fgx: Incomplete
fgx_from_rgb: Incomplete
rgb_from_bex: Incomplete
bex_from_rgb: Incomplete
rgb_from_rbd: Incomplete
rbd_from_rgb: Incomplete
rgb_from_gdx: Incomplete
gdx_from_rgb: Incomplete
rgb_from_hax: Incomplete
hax_from_rgb: Incomplete
rgb_from_bro: Incomplete
bro_from_rgb: Incomplete
rgb_from_bpx: Incomplete
bpx_from_rgb: Incomplete
rgb_from_ahx: Incomplete
ahx_from_rgb: Incomplete
rgb_from_hpx: Incomplete
hpx_from_rgb: Incomplete

def xyz2rgb(xyz, *, channel_axis: int = ...): ...
def rgb2xyz(rgb, *, channel_axis: int = ...): ...
def rgb2rgbcie(rgb, *, channel_axis: int = ...): ...
def rgbcie2rgb(rgbcie, *, channel_axis: int = ...): ...
def rgb2gray(rgb, *, channel_axis: int = ...): ...
def gray2rgba(image, alpha: Incomplete | None = ..., *, channel_axis: int = ...): ...
def gray2rgb(image, *, channel_axis: int = ...): ...
def xyz2lab(xyz, illuminant: str = ..., observer: str = ..., *, channel_axis: int = ...): ...
def lab2xyz(lab, illuminant: str = ..., observer: str = ..., *, channel_axis: int = ...): ...
def rgb2lab(rgb, illuminant: str = ..., observer: str = ..., *, channel_axis: int = ...): ...
def lab2rgb(lab, illuminant: str = ..., observer: str = ..., *, channel_axis: int = ...): ...
def xyz2luv(xyz, illuminant: str = ..., observer: str = ..., *, channel_axis: int = ...): ...
def luv2xyz(luv, illuminant: str = ..., observer: str = ..., *, channel_axis: int = ...): ...
def rgb2luv(rgb, *, channel_axis: int = ...): ...
def luv2rgb(luv, *, channel_axis: int = ...): ...
def rgb2hed(rgb, *, channel_axis: int = ...): ...
def hed2rgb(hed, *, channel_axis: int = ...): ...
def separate_stains(rgb, conv_matrix, *, channel_axis: int = ...): ...
def combine_stains(stains, conv_matrix, *, channel_axis: int = ...): ...
def lab2lch(lab, *, channel_axis: int = ...): ...
def lch2lab(lch, *, channel_axis: int = ...): ...
def rgb2yuv(rgb, *, channel_axis: int = ...): ...
def rgb2yiq(rgb, *, channel_axis: int = ...): ...
def rgb2ypbpr(rgb, *, channel_axis: int = ...): ...
def rgb2ycbcr(rgb, *, channel_axis: int = ...): ...
def rgb2ydbdr(rgb, *, channel_axis: int = ...): ...
def yuv2rgb(yuv, *, channel_axis: int = ...): ...
def yiq2rgb(yiq, *, channel_axis: int = ...): ...
def ypbpr2rgb(ypbpr, *, channel_axis: int = ...): ...
def ycbcr2rgb(ycbcr, *, channel_axis: int = ...): ...
def ydbdr2rgb(ydbdr, *, channel_axis: int = ...): ...
