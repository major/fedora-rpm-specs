# Enabling this requires an additional source, a 2.4 GB archive of test data
# files, which we consider too large to include in the source RPMs purely for
# the purpose of running the tests. We keep the “machinery” for running the
# tests in the spec file in case we want to download the archive and try the
# tests locally. If you use this build conditional, note that because it
# conditionalizes a source, it must be set when building both the source RPM
# and the binary RPM; “fedpkg mockbuild --with test_data” alone will not
# suffice. It’s easiest to just temporarily modify the spec file.
%bcond test_data 0

# This package is usable both as a library and as a command-line tool. Upstream
# seems to consider the command-line tool to be the primary interface, so we
# use application naming guidelines.
Name:           spec2nii
Version:        0.8.6
Release:        %autorelease
Summary:        Multi-format in vivo MR spectroscopy conversion to NIFTI

# The entire source is BSD-3-Clause.
#
# Per spec2nii/GE/VESPA_LICENSE, “elements of ge_pfile.py, ge_read_pfile.py and
# ge_hdr_fields.py are taken from or adapted from the VESPA project” under a
# license which is also BSD-3-Clause. From LICENSE:
#
#   This software includes third party open source software components from the
#   VESPA project. These software components have their own license. Please see
#   ./spec2nii/GE/VESPA_LICENSE.
#
# Per LICENSE, other code is adapted from nmrglue, also under a BSD-3-Clause
# license:
#   This software includes third party open source software from the nmrglue
#   project. These software components have their own license which is
#   reproduced here and in the relevant source code files
#   (spec2nii/fileiobase.py and spec2nii/varian.py).
License:        BSD-3-Clause
URL:            https://github.com/wtclarke/spec2nii
# The PyPI sdist contains some, but not all, of the files in tests/ that we
# need to run the tests. We use the GitHub archive instead.
Source0:        %{url}/archive/%{version}/spec2nii-%{version}.tar.gz
%if %{with test_data}
# Get the test data commit hash by looking at:
# https://github.com/wtclarke/spec2nii/tree/%%{version}/tests
%global test_data_url https://git.fmrib.ox.ac.uk/wclarke/spec2nii_test_data
%global test_data_commit 1594c2625a53a877670f9dd0492c0e1b6f3471d5
%global test_data_dir spec2nii_test_data-%{test_data_commit}
Source1:        %{test_data_url}/-/archive/%{test_data_commit}/%{test_data_dir}.tar.bz2
%endif

# Man pages hand-written for Fedora in groff_man(7) format based on --help
Source100:      spec2nii.1
Source101:      spec2nii-auto.1
Source102:      spec2nii-twix.1
Source103:      spec2nii-dicom.1
Source104:      spec2nii-rda.1
Source105:      spec2nii-uih.1
Source106:      spec2nii-philips.1
Source107:      spec2nii-philips_dl.1
Source108:      spec2nii-philips_dcm.1
Source109:      spec2nii-ge.1
Source110:      spec2nii-text.1
Source111:      spec2nii-jmrui.1
Source112:      spec2nii-raw.1
Source113:      spec2nii-bruker.1
Source114:      spec2nii-varian.1
Source115:      spec2nii-anon.1
Source116:      spec2nii-dump.1
Source117:      spec2nii-extract.1
Source118:      spec2nii-insert.1

# The package is arched because a dependency is removed on s390x only. It does
# not contain any compiled code.
%global debug_package %{nil}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
# (Also, python-pandas is ExcludeArch: %%{ix86}.)
ExcludeArch:    %{ix86}

# Per spec2nii/GE/VESPA_LICENSE, “elements of ge_pfile.py, ge_read_pfile.py and
# ge_hdr_fields.py are taken from or adapted from the VESPA project.”
# Similarly, per LICENSE, “This software includes third party open source
# software from the nmrglue project.” We assess that neither case of selective
# copying and adaptation rises to the level of a bundled dependency.

BuildSystem:            pyproject
BuildOption(install):   -l spec2nii
%ifarch s390x
# Skip import-checking modules that need pymapvbvd.
BuildOption(check):     -e spec2nii.Siemens.dicomfunctions
%endif

BuildRequires:  %{py3_dist pytest}
# Required for orientation tests – but those tests fail.
# BuildRequires:  %%{py3_dist fsleyes}

%py_provides python3-spec2nii

%description
A program for multi-format conversion of in vivo MRS to the NIfTI-MRS format
(https://github.com/wexeee/mrs_nifti_standard).

This program was inspired by the imaging DICOM to NIfTI converter dcm2niix,
developed by Chris Rorden. All MRS(I) orientations are tested with images
converted using dcm2niix.


%prep -a
%if %{with test_data}
%setup -q -T -D -a 1 -c -n %{name}-%{version}
rmdir tests/spec2nii_test_data
mv %{test_data_dir} tests/spec2nii_test_data
%endif

%ifarch s390x
# PyMapVBVD assumes the platform is little-endian
# https://bugzilla.redhat.com/show_bug.cgi?id=2225518
# Most of the functionality in this package is still available without it, so
# we can remove the dependency and still get a generally usable package.
sed -r -i 's/^([[:blank:]]*)?(-[[:blank:]]+)?(pyMapVBVD)\b/\1# \2\3/' \
    requirements.yml
%endif


%install -a
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
    '%{SOURCE100}' '%{SOURCE101}' '%{SOURCE102}' '%{SOURCE103}' \
    '%{SOURCE104}' '%{SOURCE105}' '%{SOURCE106}' '%{SOURCE107}' \
    '%{SOURCE108}' '%{SOURCE109}' '%{SOURCE110}' '%{SOURCE111}' \
    '%{SOURCE112}' '%{SOURCE113}' '%{SOURCE114}' '%{SOURCE115}' \
    '%{SOURCE116}' '%{SOURCE117}' '%{SOURCE118}'


%check -a
%if %{with test_data}
# Only a few tests can be executed without the test data archive, and those
# that pass without it generally do so tautologically – e.g. they run a test
# for all files matching a glob, and succeed on zero files.

# Since pv_version is in brukerapi.schemas.REQUIRED_PROPERTIES["2dseq"], the
# following failures would seem to suggest that the test data files are not
# compliant with the current schema. This does not seem worth investigating,
# but help is welcome.
#
# E           subprocess.CalledProcessError: Command '['spec2nii', 'bruker',
#             '-f', 'fid', '-m', 'FID', '-d', '-o',
#             PosixPath('/tmp/pytest-of-mockbuild/pytest-0/test_fid0'), '-j',
#             '/[…]/spec2nii_test_data/bruker/20201208_105201_lego_rod_1_3']'
#             returned non-zero exit status 1.
# […] from brukerapi:
# AttributeError: 'Dataset' object has no attribute 'pv_version'
k="${k-}${k+ and }not test_fid"
# E           subprocess.CalledProcessError: Command '['spec2nii', 'bruker',
#             '-f', '2dseq', '-m', '2DSEQ', '-d', '-o',
#             PosixPath('/tmp/pytest-of-mockbuild/pytest-0/test_2dseq0'), '-j',
#             '/[…]/spec2nii_test_data/bruker/20201208_105201_lego_rod_1_3']'
#             returned non-zero exit status 1.
# […] from brukerapi:
# AttributeError: 'Dataset' object has no attribute 'pv_version'
k="${k-}${k+ and }not test_2dseq"

# Orientation tests fail with an error from fsleyes, e.g.:
# E           subprocess.CalledProcessError: Command '['fsleyes', 'render',
#             '-of',
#             PosixPath('/tmp/pytest-of-mockbuild/pytest-0/test_svs_orientation0/svs_0.png'),
#             '-vl', '98', '158', '149', '-xc', '0', '0', '-yc', '0', '0',
#             '-zc', '0', '0', '-hc',
#             PosixPath('/[…]/tests/spec2nii_test_data/ge/from_dicom/T1.nii.gz'),
#             '-dr', '-211', '7400',
#             PosixPath('/tmp/pytest-of-mockbuild/pytest-0/test_svs_orientation0/svs.nii.gz'),
#             '-ot', 'complex', '-a', '50', '-cm', 'blue']' returned non-zero
#             exit status 1.
# For whatever it is worth, upstream CI doesn’t run orientation tests either.
# Note that we have also omitted the BuildRequires on fsleyes.
k="${k-}${k+ and }not orientation"

%pytest -k "${k-}" tests -v
%endif


%files -f %{pyproject_files}
%{_bindir}/spec2nii
%{_mandir}/man1/spec2nii.1*
%{_mandir}/man1/spec2nii-*.1*


%changelog
%autochangelog
