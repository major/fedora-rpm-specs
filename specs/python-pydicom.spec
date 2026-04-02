%global _description %{expand:
pydicom is a pure python package for working with DICOM files. It was made for
inspecting and modifying DICOM data in an easy "pythonic" way. The
modifications can be written again to a new file.

pydicom is not a DICOM server, and is not primarily about viewing images. It is
designed to let you manipulate data elements in DICOM files with python code.

Limitations -- the main limitation of the current version is that compressed
pixel data (e.g. JPEG) cannot be altered in an intelligent way as it can for
uncompressed pixels. Files can always be read and saved, but compressed pixel
data cannot easily be modified.

Documentation is available at https://pydicom.github.io/pydicom}

Name:           python-pydicom
Version:        3.0.2
Release:        %autorelease
Summary:        Read, modify and write DICOM files with python code

# There are generated data (private dict) in special format from GDCM (see License file)
License:        MIT and BSD-3-Clause
URL:            https://github.com/darcymason/pydicom
Source0:        %{url}/archive/v%{version}/pydicom-%{version}.tar.gz

# Man pages hand-written for Fedora in groff_man(7) format based on --help
Source10:       pydicom.1
Source11:       pydicom-codify.1
Source12:       pydicom-help.1
Source13:       pydicom-show.1

# Patch for fixes to non-compressed imaging + RLE (pydicom + numpy)
# https://github.com/pydicom/pydicom/issues/2147#issuecomment-2421048992
Patch:          pydicom-3.0.1-endian-numpy.patch
# Patch for compressed imaging with (pydicom + numpy + pillow)
# https://github.com/pydicom/pydicom/issues/2147#issuecomment-2423736084
Patch:          pydicom-3.0.1-endian-pillow.patch

# Fix for python 3.14
Patch:          https://github.com/pydicom/pydicom/pull/2173/commits/016abf0fa18a6f578a55d9816084f901a9809367.patch

# The package contains no compiled code, and the binary RPMs are noarch, but
# the base package is arched because there are arch-dependent test failures and
# we need to test on all architectures.
%global debug_package %{nil}
# This is a leaf package *on i686* because everything that requires it
# (directly or indirectly) is noarch, and noarch packages are no longer built
# on i686.
# repoquery --repo=rawhide{,-source} --whatrequires python3-pydicom --recursive
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
# (Also, there are a handful of failing tests we would have to skip.)
ExcludeArch:    %{ix86}

%description %_description

%package -n python3-pydicom
Summary:        %{summary}

BuildArch:      noarch

BuildRequires:  python3-devel

# For weak dependencies (also useful in tests)
BuildRequires:  python3-gdcm
BuildRequires:  python3-numpy
BuildRequires:  python3-pillow

# Extra dependencies for tests only:
BuildRequires:  python3-pydicom-data
BuildRequires:  python3-pytest
BuildRequires:  python3-pyfakefs

Recommends:     python3-gdcm
Recommends:     python3-numpy
Recommends:     python3-pillow

%description -n python3-pydicom %_description

%prep
%autosetup -n pydicom-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pydicom
install -t '%{buildroot}%{_mandir}/man1' -p -m 0644 -D \
    '%{SOURCE10}' '%{SOURCE11}' '%{SOURCE12}' '%{SOURCE13}'

%check
%pyproject_check_import

# Requires network access, since this explicitly tests downloading the test
# data files (which we have provided via a BuildRequires on
# python3-pydicom-data).
k="${k-}${k+ and }not test_fetch_data_files"

# TODO: What is wrong?
# >       assert [0.92012787, 0.91510725, 0.9160201, 0.92104053] == [
#             round(x, 8) for x in arr[:4, 0]
#         ]
# E       AssertionError
k="${k-}${k+ and }not (TestAsArray and test_reference_expl[parametric_map_float.dcm])"
k="${k-}${k+ and }not (TestAsArray and test_reference_expl_binary[parametric_map_float.dcm])"
k="${k-}${k+ and }not (TestIterArray and test_reference_expl[parametric_map_float.dcm])"
k="${k-}${k+ and }not (TestIterArray and test_reference_expl_binary[parametric_map_float.dcm])"

# Some error message texts have changed very slightly.
#
# E       AssertionError: Regex pattern did not match.
# E        Regex: "Unable to decompress as the plugins for the 'JPEG 2000 Image
#          Compression \\(Lossless Only\\)' decoder are all missing
#          dependencies:"
# E        Input: "Unable to decompress 'JPEG 2000 Image Compression (Lossless
#          Only)' pixel data because the specified plugin is missing
#          dependencies:\n\tpylibjpeg - requires pylibjpeg>=2.0 and
#          pylibjpeg-openjpeg>=2.0"
k="${k-}${k+ and }not (TestDecompress and test_no_decoders_raises)"
# E       AssertionError: Regex pattern did not match.
# E        Regex: "Error deepcopying the buffered element \\(7FE0,0010\\)
#          'Pixel Data': cannot (.*) '_io.BufferedReader' object"
# E        Input: "Error deepcopying the buffered element (7FE0,0010) 'Pixel
#          Data': cannot pickle 'BufferedReader' instances"
k="${k-}${k+ and }not (TestDatasetWithBufferedData and test_deepcopy_bufferedreader_raises)"

%ifarch s390x
# A number of tests fail on big-endian hosts (s390x)
# https://github.com/pydicom/pydicom/issues/2147
k="${k-}${k+ and }not (TestDecoding and test_bits_allocated_mismatch)"
k="${k-}${k+ and }not (TestDecoding and test_j2k[693_J2KI.dcm])"
k="${k-}${k+ and }not (TestDecoding and test_j2k[JPEG2000.dcm])"
k="${k-}${k+ and }not (TestDecoding and test_j2k[MR2_J2KI.dcm])"
k="${k-}${k+ and }not (TestDecoding and test_j2k[RG1_J2KI.dcm])"
k="${k-}${k+ and }not (TestDecoding and test_j2k[RG3_J2KI.dcm])"
k="${k-}${k+ and }not (TestDecoding and test_j2k_lossless[693_J2KR.dcm])"
k="${k-}${k+ and }not (TestDecoding and test_j2k_lossless[J2K_pixelrep_mismatch.dcm])"
k="${k-}${k+ and }not (TestDecoding and test_j2k_lossless[MR2_J2KR.dcm])"
k="${k-}${k+ and }not (TestDecoding and test_j2k_lossless[MR_small_jp2klossless.dcm])"
k="${k-}${k+ and }not (TestDecoding and test_j2k_lossless[RG1_J2KR.dcm])"
k="${k-}${k+ and }not (TestDecoding and test_j2k_lossless[RG3_J2KR.dcm])"
k="${k-}${k+ and }not (TestDecoding and test_j2k_lossless[emri_small_jpeg_2k_lossless.dcm])"
k="${k-}${k+ and }not (TestDecoding and test_jls_lossless[JLSL_16_15_1_1F.dcm])"
k="${k-}${k+ and }not (TestDecoding and test_jls_lossless[MR_small_jpeg_ls_lossless.dcm])"
k="${k-}${k+ and }not (TestDecoding and test_jls_lossless[emri_small_jpeg_ls_lossless.dcm])"
k="${k-}${k+ and }not (TestDecoding and test_jls_lossy[JPEGLSNearLossless_16.dcm])"
k="${k-}${k+ and }not (TestDecoding and test_jpg_lossless_sv1[JPEG-LL.dcm])"
k="${k-}${k+ and }not (TestRLELossless and test_cycle_i16_1s_1f)"
k="${k-}${k+ and }not (TestRLELossless and test_cycle_u16_3s_1f)"
k="${k-}${k+ and }not (TestRLELossless and test_cycle_u32_1s_1f)"
k="${k-}${k+ and }not (TestRLELossless and test_cycle_u32_3s_1f)"
k="${k-}${k+ and }not (TestRLELossless and test_cycle_u8_1s_1f)"
k="${k-}${k+ and }not (TestRLELossless and test_cycle_u8_3s_1f)"
k="${k-}${k+ and }not (Test_JPEG_LS_Lossless_transfer_syntax and test_read_emri_with_gdcm)"
k="${k-}${k+ and }not (Test_JPEG_LS_Lossless_transfer_syntax and test_read_mr_with_gdcm)"
k="${k-}${k+ and }not (TestsWithGDCM and test_JPEG2000PixelArray[File])"
k="${k-}${k+ and }not (TestsWithGDCM and test_JPEG2000PixelArray[InMemory])"
k="${k-}${k+ and }not (TestsWithGDCM and test_JPEG_LS_PixelArray[File])"
k="${k-}${k+ and }not (TestsWithGDCM and test_JPEG_LS_PixelArray[InMemory])"
k="${k-}${k+ and }not (TestsWithGDCM and test_JPEGlosslessPixelArray[File])"
k="${k-}${k+ and }not (TestsWithGDCM and test_JPEGlosslessPixelArray[InMemory])"
k="${k-}${k+ and }not (TestsWithGDCM and test_JPEGlossyPixelArray[File])"
k="${k-}${k+ and }not (TestsWithGDCM and test_JPEGlossyPixelArray[InMemory])"
k="${k-}${k+ and }not (TestsWithGDCM and test_decompress_using_gdcm[File])"
k="${k-}${k+ and }not (TestsWithGDCM and test_decompress_using_gdcm[InMemory])"
k="${k-}${k+ and }not (TestsWithGDCM and test_emri_JPEG2000PixelArray[File])"
k="${k-}${k+ and }not (TestsWithGDCM and test_emri_JPEG2000PixelArray[InMemory])"
k="${k-}${k+ and }not (TestsWithGDCM and test_emri_JPEG_LS_PixelArray_with_gdcm[File])"
k="${k-}${k+ and }not (TestsWithGDCM and test_emri_JPEG_LS_PixelArray_with_gdcm[InMemory])"
k="${k-}${k+ and }not (TestsWithGDCM and test_pixel_rep_mismatch[File])"
k="${k-}${k+ and }not (TestsWithGDCM and test_pixel_rep_mismatch[InMemory])"
%endif

%{pytest} -k "${k-}" -rs -vv

%files -n python3-pydicom -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/pydicom
%{_mandir}/man1/pydicom.1*
%{_mandir}/man1/pydicom-*.1*

%changelog
%autochangelog
