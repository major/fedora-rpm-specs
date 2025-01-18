# Temporarily work around python-scikit-image not rebuilt for numpy 2,
# https://bugzilla.redhat.com/show_bug.cgi?id=2334911
%bcond scikit_image_tests %{undefined fc42}

Name:           python-glymur
Version:        0.13.7
Release:        %autorelease
Summary:        Interface to the OpenJPEG library for working with JPEG 2000 files

# SPDX
License:        MIT
URL:            https://github.com/quintusdias/glymur
# The PyPI sdist lacks documentation.
Source0:        %{url}/archive/v%{version}/glymur-%{version}.tar.gz
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

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if %{undefined fc40} && %{undefined fc41}
ExcludeArch:    %{ix86}
%endif

BuildRequires:  python3-devel
# tests/fixtures.py: each of these enables more tests
%if %{with scikit_image_tests}
BuildRequires:  python3dist(scikit-image)
%endif
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
%autosetup -n glymur-%{version} -p1


%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
install -m 0644 -p -D -t %{buildroot}%{_mandir}/man1 %{SOURCE1} %{SOURCE2}

%pyproject_install
%pyproject_save_files -l glymur


%check
%if %{without scikit_image_tests}
ignore="${ignore-} --ignore=tests/test_tiff2jp2.py"
k="${k-}${k+ and }not (TestJp2k and test_write_using_slicing)"
k="${k-}${k+ and }not (TestSuite and test_openjpeg_library_too_old_for_threaded_tile_writing)"
%endif

%pytest ${ignore-} -k "${k-}" -v


%files -n python3-glymur -f %{pyproject_files}
%doc README.md CHANGES.txt
%{_bindir}/jp2dump
%{_bindir}/tiff2jp2

%{_mandir}/man1/jp2dump.1*
%{_mandir}/man1/tiff2jp2.1*

%changelog
%autochangelog
