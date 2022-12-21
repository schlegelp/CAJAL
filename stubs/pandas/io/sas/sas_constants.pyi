from _typeshed import Incomplete
from typing import Final

magic: Final[Incomplete]
align_1_checker_value: Final[bytes]
align_1_offset: Final[int]
align_1_length: Final[int]
align_1_value: Final[int]
u64_byte_checker_value: Final[bytes]
align_2_offset: Final[int]
align_2_length: Final[int]
align_2_value: Final[int]
endianness_offset: Final[int]
endianness_length: Final[int]
platform_offset: Final[int]
platform_length: Final[int]
encoding_offset: Final[int]
encoding_length: Final[int]
dataset_offset: Final[int]
dataset_length: Final[int]
file_type_offset: Final[int]
file_type_length: Final[int]
date_created_offset: Final[int]
date_created_length: Final[int]
date_modified_offset: Final[int]
date_modified_length: Final[int]
header_size_offset: Final[int]
header_size_length: Final[int]
page_size_offset: Final[int]
page_size_length: Final[int]
page_count_offset: Final[int]
page_count_length: Final[int]
sas_release_offset: Final[int]
sas_release_length: Final[int]
sas_server_type_offset: Final[int]
sas_server_type_length: Final[int]
os_version_number_offset: Final[int]
os_version_number_length: Final[int]
os_maker_offset: Final[int]
os_maker_length: Final[int]
os_name_offset: Final[int]
os_name_length: Final[int]
page_bit_offset_x86: Final[int]
page_bit_offset_x64: Final[int]
subheader_pointer_length_x86: Final[int]
subheader_pointer_length_x64: Final[int]
page_type_offset: Final[int]
page_type_length: Final[int]
block_count_offset: Final[int]
block_count_length: Final[int]
subheader_count_offset: Final[int]
subheader_count_length: Final[int]
page_type_mask: Final[int]
page_type_mask2: Final[Incomplete]
page_meta_type: Final[int]
page_data_type: Final[int]
page_mix_type: Final[int]
page_amd_type: Final[int]
page_meta2_type: Final[int]
page_comp_type: Final[int]
page_meta_types: Final[Incomplete]
subheader_pointers_offset: Final[int]
truncated_subheader_id: Final[int]
compressed_subheader_id: Final[int]
compressed_subheader_type: Final[int]
text_block_size_length: Final[int]
row_length_offset_multiplier: Final[int]
row_count_offset_multiplier: Final[int]
col_count_p1_multiplier: Final[int]
col_count_p2_multiplier: Final[int]
row_count_on_mix_page_offset_multiplier: Final[int]
column_name_pointer_length: Final[int]
column_name_text_subheader_offset: Final[int]
column_name_text_subheader_length: Final[int]
column_name_offset_offset: Final[int]
column_name_offset_length: Final[int]
column_name_length_offset: Final[int]
column_name_length_length: Final[int]
column_data_offset_offset: Final[int]
column_data_length_offset: Final[int]
column_data_length_length: Final[int]
column_type_offset: Final[int]
column_type_length: Final[int]
column_format_text_subheader_index_offset: Final[int]
column_format_text_subheader_index_length: Final[int]
column_format_offset_offset: Final[int]
column_format_offset_length: Final[int]
column_format_length_offset: Final[int]
column_format_length_length: Final[int]
column_label_text_subheader_index_offset: Final[int]
column_label_text_subheader_index_length: Final[int]
column_label_offset_offset: Final[int]
column_label_offset_length: Final[int]
column_label_length_offset: Final[int]
column_label_length_length: Final[int]
rle_compression: Final[bytes]
rdc_compression: Final[bytes]
compression_literals: Final[Incomplete]
encoding_names: Final[Incomplete]

class SASIndex:
    row_size_index: Final[int]
    column_size_index: Final[int]
    subheader_counts_index: Final[int]
    column_text_index: Final[int]
    column_name_index: Final[int]
    column_attributes_index: Final[int]
    format_and_label_index: Final[int]
    column_list_index: Final[int]
    data_subheader_index: Final[int]

subheader_signature_to_index: Final[Incomplete]
sas_date_formats: Final[Incomplete]
sas_datetime_formats: Final[Incomplete]
