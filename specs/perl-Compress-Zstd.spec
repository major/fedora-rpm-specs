Name:           perl-Compress-Zstd
Version:        0.20
Release:        2%{?dist}
Summary:        Perl interface to Zstandard compressor and decompressor
# lib/Compress/Zstd.pm:                     BSD-2-Clause
# lib/Compress/Zstd/CompressionContext.pm:  BSD-2-Clause
# lib/Compress/Zstd/Compressor.pm:          BSD-2-Clause
# lib/Compress/Zstd/Decompressor.pm:        BSD-2-Clause
# lib/Compress/Zstd/DecompressionContext.pm:        BSD-2-Clause
# lib/Compress/Zstd/DecompressionDictionary.pm:     BSD-2-Clause
# lib/Compress/Zstd/CompressionDictionary.pm:       BSD-2-Clause
# LICENSE:      BSD-2-Clause text
# README.md:    BSD-2-Clause
## Unbunlded
# ext/zstd/COPYING:         GPL-2.0 text
# ext/zstd/LICENSE:         BSD-2-Clause text
# ext/zstd/Makefile:        BSD-2-Clause OR GPL-2.0-only
# ext/zstd/README.md:       BSD-2-Clause OR GPL-2.0-only
# ext/zstd/build/cmake/CMakeLists.txt:              BSD-2-Clause OR GPL-2.0-only
# ext/zstd/build/cmake/contrib/CMakeLists.txt:      BSD-2-Clause OR GPL-2.0-only
# ext/zstd/build/cmake/contrib/gen_html/CMakeLists.txt: BSD-2-Clause OR GPL-2.0-only
# ext/zstd/build/cmake/contrib/pzstd/CMakeLists.txt:    BSD-2-Clause OR GPL-2.0-only
# ext/zstd/build/cmake/lib/CMakeLists.txt:          BSD-2-Clause OR GPL-2.0-only
# ext/zstd/build/cmake/programs/CMakeLists.txt:     BSD-2-Clause OR GPL-2.0-only
# ext/zstd/build/cmake/tests/CMakeLists.txt:        BSD-2-Clause
# ext/zstd/build/meson/GetZstdLibraryVersion.py:    BSD-2-Clause OR GPL-2.0-only
# ext/zstd/build/meson/InstallSymlink.py:           BSD-2-Clause OR GPL-2.0-only
# ext/zstd/build/meson/contrib/gen_html/meson.build:    BSD-2-Clause OR GPL-2.0-only
# ext/zstd/build/meson/contrib/meson.build:         BSD-2-Clause OR GPL-2.0-only
# ext/zstd/build/meson/contrib/pzstd/meson.build:   BSD-2-Clause OR GPL-2.0-only
# ext/zstd/build/meson/lib/meson.build:             BSD-2-Clause OR GPL-2.0-only
# ext/zstd/build/meson/meson.build:                 BSD-2-Clause OR GPL-2.0-only
# ext/zstd/build/meson/meson_options.txt:           BSD-2-Clause OR GPL-2.0-only
# ext/zstd/build/meson/programs/meson.build:        BSD-2-Clause OR GPL-2.0-only
# ext/zstd/build/meson/tests/meson.build:           BSD-2-Clause OR GPL-2.0-only
# ext/zstd/build/meson/tests/valgrindTest.py:       BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/adaptive-compression/adapt.c:            BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/adaptive-compression/datagencli.c:       BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/gen_html/Makefile:               BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/largeNbDicts/Makefile:           BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/largeNbDicts/largeNbDicts.c:     BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/linux-kernel/0001-lib-Add-xxhash-module.patch:           BSD-2-Clause
# ext/zstd/contrib/linux-kernel/0003-btrfs-Add-zstd-support.patch:          GPL-2.0-only
# ext/zstd/contrib/linux-kernel/0004-squashfs-Add-zstd-support.patch:       GPL-2.0-or-later
# ext/zstd/contrib/linux-kernel/0005-crypto-Add-zstd-support.patch:         GPL-2.0-only
# ext/zstd/contrib/linux-kernel/0006-squashfs-tools-Add-zstd-support.patch: GPL-2.0-or-later
# ext/zstd/contrib/linux-kernel/COPYING:                    GPL-2.0 text
# ext/zstd/contrib/linux-kernel/fs/btrfs/zstd.c:            GPL-2.0-only
# ext/zstd/contrib/linux-kernel/fs/squashfs/zstd_wrapper.c: GPL-2.0-or-later
# ext/zstd/contrib/linux-kernel/include/linux/xxhash.h:     BSD-2-Clause
# ext/zstd/contrib/linux-kernel/include/linux/zstd.h:       BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/linux-kernel/lib/xxhash.c:               BSD-2-Clause
# ext/zstd/contrib/linux-kernel/lib/zstd/bitstream.h:       BSD-2-Clause
# ext/zstd/contrib/linux-kernel/lib/zstd/compress.c:        BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/linux-kernel/lib/zstd/decompress.c:      BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/linux-kernel/lib/zstd/entropy_common.c:  BSD-2-Clause
# ext/zstd/contrib/linux-kernel/lib/zstd/error_private.h:   BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/linux-kernel/lib/zstd/fse.h:             BSD-2-Clause
# ext/zstd/contrib/linux-kernel/lib/zstd/fse_compress.c:    BSD-2-Clause
# ext/zstd/contrib/linux-kernel/lib/zstd/fse_decompress.c:  BSD-2-Clause
# ext/zstd/contrib/linux-kernel/lib/zstd/huf.h:             BSD-2-Clause
# ext/zstd/contrib/linux-kernel/lib/zstd/huf_compress.c:    BSD-2-Clause
# ext/zstd/contrib/linux-kernel/lib/zstd/huf_decompress.c:  BSD-2-Clause
# ext/zstd/contrib/linux-kernel/lib/zstd/mem.h:             BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/linux-kernel/lib/zstd/zstd_common.c:     BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/linux-kernel/lib/zstd/zstd_internal.h:   BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/linux-kernel/lib/zstd/zstd_opt.h:        BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/linux-kernel/test/DecompressCrash.c:     BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/linux-kernel/test/RoundTripCrash.c:      BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/linux-kernel/xxhash_test.c:              BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/linux-kernel/zstd_compress_test.c:       BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/linux-kernel/zstd_decompress_test.c:     BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/pzstd/ErrorHolder.h:                     BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/pzstd/Logging.h:                         BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/pzstd/Makefile:                          BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/pzstd/Options.cpp:                       BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/pzstd/Options.h:                         BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/pzstd/Pzstd.cpp:                         BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/pzstd/Pzstd.h:                           BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/pzstd/SkippableFrame.cpp:                BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/pzstd/SkippableFrame.h:                  BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/pzstd/main.cpp:                          BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/pzstd/test/OptionsTest.cpp:              BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/pzstd/test/PzstdTest.cpp:                BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/pzstd/test/RoundTrip.h:                  BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/pzstd/test/RoundTripTest.cpp:            BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/pzstd/utils/Buffer.h:                    BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/pzstd/utils/FileSystem.h:                BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/pzstd/utils/Likely.h:                    BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/pzstd/utils/Range.h:                     BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/pzstd/utils/ResourcePool.h:              BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/pzstd/utils/ScopeGuard.h:                BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/pzstd/utils/ThreadPool.h:                BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/pzstd/utils/WorkQueue.h:                 BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/pzstd/utils/test/BufferTest.cpp:         BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/pzstd/utils/test/RangeTest.cpp:          BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/pzstd/utils/test/ResourcePoolTest.cpp:   BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/pzstd/utils/test/ScopeGuardTest.cpp:     BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/pzstd/utils/test/ThreadPoolTest.cpp:     BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/pzstd/utils/test/WorkQueueTest.cpp:      BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/seekable_format/examples/Makefile:       BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/seekable_format/examples/parallel_compression.c:         BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/seekable_format/examples/parallel_processing.c:          BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/seekable_format/examples/seekable_compression.c:         BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/seekable_format/examples/seekable_decompression.c:       BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/seekable_format/examples/seekable_decompression_mem.c:   BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/seekable_format/zstd_seekable_compression_format.md:     LPD-document
# ext/zstd/contrib/seekable_format/zstdseek_compress.c:     BSD-2-Clause OR GPL-2.0-only
# ext/zstd/contrib/seekable_format/zstdseek_decompress.c:   BSD-2-Clause OR GPL-2.0-only
# ext/zstd/doc/educational_decoder/harness.c:               BSD-2-Clause OR GPL-2.0-only
# ext/zstd/doc/educational_decoder/zstd_decompress.c:       BSD-2-Clause OR GPL-2.0-only
# ext/zstd/doc/educational_decoder/zstd_decompress.h:       BSD-2-Clause OR GPL-2.0-only
# ext/zstd/doc/zstd_compression_format.md:  LPD-document
# ext/zstd/examples/Makefile:               BSD-2-Clause OR GPL-2.0-only
# ext/zstd/examples/common.h:               BSD-2-Clause OR GPL-2.0-only
# ext/zstd/examples/dictionary_compression.c:       BSD-2-Clause OR GPL-2.0-only
# ext/zstd/examples/dictionary_decompression.c:     BSD-2-Clause OR GPL-2.0-only
# ext/zstd/examples/multiple_simple_compression.c:  BSD-2-Clause OR GPL-2.0-only
# ext/zstd/examples/multiple_streaming_compression.c:       BSD-2-Clause OR GPL-2.0-only
# ext/zstd/examples/simple_compression.c:           BSD-2-Clause OR GPL-2.0-only
# ext/zstd/examples/simple_decompression.c:         BSD-2-Clause OR GPL-2.0-only
# ext/zstd/examples/streaming_decompression.c:      BSD-2-Clause OR GPL-2.0-only
# ext/zstd/examples/streaming_memory_usage.c:       BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/Makefile:                    BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/common/bitstream.h:          BSD-2-Clause
# ext/zstd/lib/common/compiler.h:           BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/common/cpu.h:                BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/common/debug.c:              BSD-2-Clause
# ext/zstd/lib/common/debug.h:              BSD-2-Clause
# ext/zstd/lib/common/entropy_common.c:     BSD-2-Clause
# ext/zstd/lib/common/error_private.c:      BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/common/error_private.h:      BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/common/fse.h:                BSD-2-Clause
# ext/zstd/lib/common/fse_decompress.c:     BSD-2-Clause
# ext/zstd/lib/common/huf.h:                BSD-2-Clause
# ext/zstd/lib/common/mem.h:                BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/common/pool.c:               BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/common/pool.h:               BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/common/threading.c:          BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/common/threading.h:          BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/common/xxhash.h:             BSD-2-Clause
# ext/zstd/lib/common/zstd_common.c:        BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/common/zstd_errors.h:        BSD-2-Clause
# ext/zstd/lib/common/zstd_errors.h:        BSD-2-Clause
# ext/zstd/lib/common/zstd_internal.h:      BSD-2-Clause
# ext/zstd/lib/compress/fse_compress.c:     BSD-2-Clause
# ext/zstd/lib/compress/hist.h:             BSD-2-Clause
# ext/zstd/lib/compress/huf_compress.c:     BSD-2-Clause
# ext/zstd/lib/compress/zstd_compress.c:    BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/compress/zstd_compress_internal.h:           BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/compress/zstd_compress_literals.c:           BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/compress/zstd_compress_literals.h:           BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/compress/zstd_compress_sequences.c:          BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/compress/zstd_compress_sequences.h:          BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/compress/zstd_double_fast.c: BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/compress/zstd_double_fast.h: BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/compress/zstd_fast.c:        BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/compress/zstd_fast.h:        BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/compress/zstd_lazy.c:        BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/compress/zstd_lazy.h:        BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/compress/zstd_ldm.c:         BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/compress/zstd_ldm.h:         BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/compress/zstd_opt.h:         BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/compress/zstdmt_compress.c:  BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/compress/zstdmt_compress.h:  BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/compress/zstdmt_compress.h:  BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/decompress/huf_decompress.c: BSD-2-Clause
# ext/zstd/lib/decompress/zstd_ddict.c:     BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/decompress/zstd_ddict.h:     BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/decompress/zstd_decompress.c:                BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/decompress/zstd_decompress.c:                BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/decompress/zstd_decompress_block:            BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/decompress/zstd_decompress_internal.h:       BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/deprecated/zbuff.h:          BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/deprecated/zbuff_common.c:           BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/deprecated/zbuff_decompress.c:       BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/dictBuilder/cover.c:         BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/dictBuilder/divsufsort.c:    MIT
# ext/zstd/lib/dictBuilder/divsufsort.h:    MIT
# ext/zstd/lib/dictBuilder/zdict.c:         BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/dictBuilder/zdict.h:         BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/dll/example/Makefile:        BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/legacy/zstd_legacy.h:        BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/legacy/zstd_v01.c:   BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/legacy/zstd_v01.h:   BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/legacy/zstd_v02.c:   BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/legacy/zstd_v02.h:   BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/legacy/zstd_v03.c:   BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/legacy/zstd_v03.h:   BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/legacy/zstd_v04.c:   BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/legacy/zstd_v04.h:   BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/legacy/zstd_v05.c:   BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/legacy/zstd_v05.h:   BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/legacy/zstd_v06.c:   BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/legacy/zstd_v06.h:   BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/legacy/zstd_v07.c:   BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/legacy/zstd_v07.h:   BSD-2-Clause OR GPL-2.0-only
# ext/zstd/lib/libzstd.pc.in:       BSD-2-Clause
# ext/zstd/lib/zstd.h:              BSD-2-Clause OR GPL-2.0-only
# ext/zstd/programs/Makefile:       BSD-2-Clause OR GPL-2.0-only
# ext/zstd/programs/benchfn.c:      BSD-2-Clause OR GPL-2.0-only
# ext/zstd/programs/benchfn.h:      BSD-2-Clause OR GPL-2.0-only
# ext/zstd/programs/benchzstd.c:    BSD-2-Clause OR GPL-2.0-only
# ext/zstd/programs/benchzstd.h:    BSD-2-Clause OR GPL-2.0-only
# ext/zstd/programs/datagen.c:      BSD-2-Clause OR GPL-2.0-only
# ext/zstd/programs/datagen.h:      BSD-2-Clause OR GPL-2.0-only
# ext/zstd/programs/dibio.c:        BSD-2-Clause OR GPL-2.0-only
# ext/zstd/programs/dibio.h:        BSD-2-Clause OR GPL-2.0-only
# ext/zstd/programs/fileio.c:       BSD-2-Clause OR GPL-2.0-only
# ext/zstd/programs/fileio.h:       BSD-2-Clause OR GPL-2.0-only
# ext/zstd/programs/platform.h:     BSD-2-Clause OR GPL-2.0-only
# ext/zstd/programs/timefn.h:       BSD-2-Clause OR GPL-2.0-only
# ext/zstd/programs/util.h:         BSD-2-Clause OR GPL-2.0-only
# ext/zstd/programs/zstdcli.c:      BSD-2-Clause OR GPL-2.0-only
# ext/zstd/programs/zstdgrep:       BSD-2-Clause
# ext/zstd/tests/Makefile:          BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/bigdict.c:         BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/checkTag.c:        BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/datagencli.c:              BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/decodecorpus.c:            BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/fullbench.c:               BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/fuzz/Makefile:             BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/fuzz/block_decompress.c:   BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/fuzz/block_round_trip.c:   BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/fuzz/dictionary_decompress.c:  BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/fuzz/dictionary_round_trip.c:  BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/fuzz/fuzz.h:               BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/fuzz/fuzz.py:              BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/fuzz/fuzz_helpers.h:       BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/fuzz/regression_driver.c:  BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/fuzz/simple_compress.c:    BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/fuzz/simple_decompress.c:  BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/fuzz/simple_round_trip.c:  BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/fuzz/stream_decompress.c:  BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/fuzz/stream_round_trip.c:  BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/fuzz/zstd_frame_info.c:    BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/fuzz/zstd_helpers.c:       BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/fuzz/zstd_helpers.h:       BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/fuzzer.c:          BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/gzip/Makefile:             BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/gzip/gzip-env:             GPL-3.0-or-later
# ext/zstd/tests/gzip/helin-segv.sh:        GPL-3.0-or-later
# ext/zstd/tests/gzip/help-version.sh:      GPL-3.0-or-later
# ext/zstd/tests/gzip/hufts.sh:             GPL-3.0-or-later
# ext/zstd/tests/gzip/init.sh:              GPL-3.0-or-later
# ext/zstd/tests/gzip/keep.sh:              GPL-3.0-or-later
# ext/zstd/tests/gzip/list.sh:              GPL-3.0-or-later
# ext/zstd/tests/gzip/memcpy-abuse.sh:      GPL-3.0-or-later    
# ext/zstd/tests/gzip/mixed.sh:             GPL-3.0-or-later
# ext/zstd/tests/gzip/null-suffix-clobber.sh:   GPL-3.0-or-later
# ext/zstd/tests/gzip/stdin.sh:             GPL-3.0-or-later
# ext/zstd/tests/gzip/test-driver.sh:       GPL-2.0-or-later WITH Autoconf-exception-generic
# ext/zstd/tests/gzip/trailing-nul.sh:      GPL-3.0-or-later
# ext/zstd/tests/gzip/unpack-invalid.sh:    GPL-3.0-or-later
# ext/zstd/tests/gzip/z-suffix.sh:          GPL-3.0-or-later
# ext/zstd/tests/gzip/zdiff.sh:             GPL-3.0-or-later
# ext/zstd/tests/gzip/zgrep-context.sh:     GPL-3.0-or-later
# ext/zstd/tests/gzip/zgrep-f.sh:           GPL-3.0-or-later
# ext/zstd/tests/gzip/zgrep-signal.sh:      GPL-3.0-or-later
# ext/zstd/tests/gzip/znew-k.sh:            GPL-3.0-or-later
# ext/zstd/tests/invalidDictionaries.c:     BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/legacy.c:          BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/longmatch.c:       BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/paramgrill.c:      BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/poolTests.c:       BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/rateLimiter.py:            BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/regression/Makefile:       BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/regression/config.c:       BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/regression/config.h:       BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/regression/data.c:         BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/regression/data.h:         BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/regression/levels.h:       BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/regression/method.c:       BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/regression/method.h:       BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/regression/result.c:       BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/regression/result.h:       BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/regression/test.c: BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/roundTripCrash.c:  BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/seqgen.c:          BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/seqgen.h:          BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/symbols.c:         BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/test-zstd-speed.py:        BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/test-zstd-versions.py:     BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/zbufftest.c:       BSD-2-Clause OR GPL-2.0-only
# ext/zstd/tests/zstreamtest.c:     BSD-2-Clause OR GPL-2.0-only
# ext/zstd/zlibWrapper/examples/example.c:  Zlib
# ext/zstd/zlibWrapper/examples/example_original.c: Zlib
# ext/zstd/zlibWrapper/examples/fitblk.c:           LicenseRef-Fedora-Public-Domain
# ext/zstd/zlibWrapper/examples/fitblk_original.c:  LicenseRef-Fedora-Public-Domain
# ext/zstd/zlibWrapper/examples/minigzip.c:     Zlib
# ext/zstd/zlibWrapper/examples/zwrapbench.c:   BSD-2-Clause OR GPL-2.0-only
# ext/zstd/zlibWrapper/gzcompatibility.h:   BSD-2-Clause OR GPL-2.0-only
# ext/zstd/zlibWrapper/gzclose.c:           Zlib
# ext/zstd/zlibWrapper/gzguts.h:            Zlib
# ext/zstd/zlibWrapper/gzlib.c:             Zlib
# ext/zstd/zlibWrapper/gzread.c:            Zlib
# ext/zstd/zlibWrapper/gzwrite.c:           Zlib
# ext/zstd/zlibWrapper/zstd_zlibwrapper.c   BSD-2-Clause OR GPL-2.0-only
# ext/zstd/zlibWrapper/zstd_zlibwrapper.h:  BSD-2-Clause OR GPL-2.0-only
# ppport.h:     GPL-1.0-or-later OR Artistic-1.0-Perl
License:        BSD-2-Clause AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
SourceLicense:  %{license} AND (BSD-2-Clause OR GPL-2.0-only) AND BSD-2-Clause AND GPL-3.0-or-later AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-2.0-or-later WITH Autoconf-exception-generic AND LPD-document AND MIT AND Zlib AND LicenseRef-Fedora-Public-Domain
URL:            https://metacpan.org/dist/Compress-Zstd
Source0:        https://www.cpan.org/authors/id/J/JI/JIRO/Compress-Zstd-%{version}.tar.gz
# Build against a system libzstd, not suitable for upstream as it replaces
# a special-casing for building from git tree.
Patch0:         Compress-Zstd-0.20-Build-against-system-libzstd.patch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Config)
BuildRequires:  perl(Devel::PPPort)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::ParseXS)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  libzstd-devel >= 1.4.0
# Run-time:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Test::More) >= 0.98
# pkgconf for /usr/bin/pkg-config
BuildRequires:  pkgconf
BuildRequires:  pkgconfig(libzstd)

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::More\\)$

%description
The Compress::Zstd module provides a Perl interface to the Zstd compressor and
decompressor.

%package tests
Summary:        Tests for %{name}
License:        BSD-2-Clause
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.98
Requires:       pkgconf
Requires:       pkgconfig(libzstd)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n Compress-Zstd-%{version}
# Remove bundled code
rm -r ext ppport.h
unset RELEASE_TESTING
perl -i -ne 'print $_ unless m{\A(ext/|ppport\.h)}' MANIFEST
# Correct modes
chmod a-x eg/*

%build
perl Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%files
%license LICENSE
%doc Changes eg README.md
%dir %{perl_vendorarch}/auto/Compress
%{perl_vendorarch}/auto/Compress/Zstd
%dir %{perl_vendorarch}/Compress
%{perl_vendorarch}/Compress/Zstd
%{perl_vendorarch}/Compress/Zstd.pm
%{_mandir}/man3/Compress::Zstd.*
%{_mandir}/man3/Compress::Zstd::*

%files tests
%{_libexecdir}/%{name}

%changelog
* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Mon May 04 2026 Petr Pisar <ppisar@redhat.com> 0.20-1
- 0.20 version packaged
