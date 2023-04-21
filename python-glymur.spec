Name:           python-glymur
Version:        0.12.2
Release:        %autorelease
Summary:        Interface to the OpenJPEG library for working with JPEG 2000 files

# SPDX
License:        MIT
URL:            https://pypi.org/project/Glymur/
# The PyPI sdist lacks documentation.
Source0:        https://github.com/quintusdias/glymur/archive/v%{version}/%{name}-%{version}.tar.gz
# Man pages hand-written for Fedora in groff_man(7) format based on --help
# output:
Source1:        jp2dump.1
Source2:        tiff2jp2.1

# Since the package has had endian-dependent test failures in the past, we give
# up “noarch” in the base package in order to run tests on all supported
# architectures.  We can still make all the built RPMs noarch.  Since the
# package does not in fact contain any compiled code, there is no corresponding
# debuginfo package.
%global debug_package %{nil}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
# tests/fixtures.py: each of these enables more tests
BuildRequires:  python3dist(scikit-image)
BuildRequires:  python3dist(gdal)

# Provide shared libraries opened via ctypes; see glymur/config.py
BuildRequires:  openjpeg2
BuildRequires:  libtiff

%global _description %{expand:
Glymur contains a Python interface to the OpenJPEG
library which allows one to read and write JPEG 2000 files.}

%description %_description

%package -n python3-glymur
Requires:       openjpeg2
Summary:        %{summary}

BuildArch:      noarch

# Provide shared libraries opened via ctypes; see glymur/config.py
Requires:       openjpeg2
Requires:       libtiff

# glymur/jp2box.py: provides optional functionality
Recommends:     python3dist(gdal)

%description -n python3-glymur %_description


%prep
%autosetup -n glymur-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
install -m 0644 -p -D -t %{buildroot}%{_mandir}/man1 %{SOURCE1} %{SOURCE2}

%pyproject_install
%pyproject_save_files glymur


%check
%ifarch s390x
# New s390x test failures on Fedora in 0.12.2
# https://github.com/quintusdias/glymur/issues/604
#
# See also:
#
# glymur autopkgtests regressed on s390x
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1032291
#
# Note that it has been…
#
#   “verified that the tests from 0.12.1 pass with either the 0.12.1 or 0.12.2
#   code, and the tests from 0.12.2 fail with either the 0.12.1 or 0.12.2 code”
#
# That is, new tests revealed existing problems, and there is no evidence that
# there are regressions.
k="${k-}${k+ and }not (TestSuite and test_rgb_tiled_bigtiff)"
k="${k-}${k+ and }not (TestSuite and test_ycbcr_jpeg_single_tile)"
k="${k-}${k+ and }not (TestSuite and test_ycbcr_jpeg_tiff)"
k="${k-}${k+ and }not (TestSuite and test_ycbcr_jpeg_unevenly_tiled)"
%endif
%pytest -v -k "${k-}"


%files -n python3-glymur -f %{pyproject_files}
%doc README.md CHANGES.txt
%license LICENSE.txt
%{_bindir}/jp2dump
%{_bindir}/tiff2jp2

%{_mandir}/man1/jp2dump.1*
%{_mandir}/man1/tiff2jp2.1*

%changelog
%autochangelog
