Name:           python-glymur
Version:        0.14.4
%global srcversion %(echo '%{version}' | sed -r 's/\\.(post)/\\1/')
Release:        %autorelease
Summary:        Interface to the OpenJPEG library for working with JPEG 2000 files

# SPDX
License:        MIT
URL:            https://github.com/quintusdias/glymur
# The PyPI sdist lacks documentation.
Source0:        %{url}/archive/v%{srcversion}/glymur-%{srcversion}.tar.gz
# Man pages hand-written for Fedora in groff_man(7) format based on --help
# output:
Source1:        jp2dump.1
Source2:        jpeg2jp2.1
Source3:        tiff2jp2.1

BuildSystem:            pyproject
BuildOption(install):   -l glymur

# Since the package has had endian-dependent test failures in the past, we give
# up “noarch” in the base package in order to run tests on all supported
# architectures.  We can still make all the built RPMs noarch.  Since the
# package does not in fact contain any compiled code, there is no corresponding
# debuginfo package.
%global debug_package %{nil}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

# Test dependencies are now only listed in CI configurations, e.g.
# ci/travis-313.yaml, so we must enumerate them manually.
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-xdist}
BuildRequires:  %{py3_dist scikit-image}

# tests/fixtures.py: each of these enables more tests
# (We also have a weak dependency on gdal.)
BuildRequires:  %{py3_dist gdal}

# Provide shared libraries opened via ctypes; see glymur/config.py
BuildRequires:  openjpeg2
BuildRequires:  libtiff

%if %{defined fc42}
# Workaround for setuptools<77.0.3; see
# https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#license-and-license-files.
%global no_pep_639_backend 1

BuildRequires:  tomcli
%endif

%global _description %{expand:
Glymur contains a Python interface to the OpenJPEG
library which allows one to read and write JPEG 2000 files.}

%description %_description

%package -n python3-glymur
Summary:        %{summary}

BuildArch:      noarch

# Provide shared libraries opened via ctypes; see glymur/config.py
Requires:       openjpeg2
Requires:       libtiff

# glymur/jp2box.py: provides optional functionality
Recommends:     %{py3_dist gdal}

%description -n python3-glymur %_description


%prep -a
%if 0%{?no_pep_639_backend}
tomcli set pyproject.toml del project.license
%endif


%install -a
install -m 0644 -p -D -t '%{buildroot}%{_mandir}/man1' \
    '%{SOURCE1}' '%{SOURCE2}' '%{SOURCE3}'


%check -a
%pytest -n auto -rs -v


%files -n python3-glymur -f %{pyproject_files}
%doc README.md CHANGES.txt
%{_bindir}/jp2dump
%{_bindir}/jpeg2jp2
%{_bindir}/tiff2jp2

%{_mandir}/man1/jp2dump.1*
%{_mandir}/man1/jpeg2jp2.1*
%{_mandir}/man1/tiff2jp2.1*

%changelog
%autochangelog
