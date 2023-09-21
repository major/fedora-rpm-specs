%bcond_with tests

%global _description %{expand:
C++ / Python reader for SONATA circuit files. SONATA guide:
https://github.com/AllenInstitute/sonata/blob/master/docs/SONATA_DEVELOPER_GUIDE.md
}

Name:           libsonata
Version:        0.1.23
Release:        %autorelease
Summary:        A Python and C++ interface to the SONATA format

# spdx
# Boost: include/bbp/sonata/{optional,variant}.hpp
# single file header only library: https://github.com/martinmoene/optional-lite
License:        LGPL-3.0-only and BSL-1.0
URL:            https://github.com/BlueBrain/libsonata
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# https://github.com/sanjayankur31/libsonata/tree/fedora-0.1.23
Patch0:         0001-include-catch-cmake.patch
Patch1:         0002-use-cpp-17-filesystem.patch
Patch2:         0003-Remove-pybind-redeclarations.patch
Patch3:         0004-disable-python-ext-build.patch
Patch4:         0005-set-libdir.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  boost-devel
BuildRequires:  cmake(Catch2) < 3
BuildRequires:  fmt-devel
BuildRequires:  json-devel
BuildRequires:  gcc-c++
BuildRequires:  git-core
# 2.3.1-5 has a fix that is necessary to ensure builds on
# s390x, ppc64le, aarch64
# https://github.com/BlueBrain/libsonata/issues/184
BuildRequires:  highfive-devel >= 2.3.1-5
BuildRequires:  hdf5-devel
BuildRequires:  pybind11-devel
BuildRequires:  python3-pybind11

%description %_description

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description devel %_description

%package -n python3-libsonata
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-pytest
BuildRequires:  python3-h5py

%description -n python3-libsonata %_description

%prep
%autosetup -n libsonata-%{version} -S git
rm -rf libsonata.egg-info
rm -rf extlib/{Catch2,Highfive,fmt,nlohmann}

# Comment out to remove /usr/bin/env shebangs
# Can use something similar to correct/remove /usr/bin/python shebangs also
# find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%build
%cmake -DSONATA_PYTHON=ON -DEXTLIB_FROM_SUBMODULES=OFF -DSONATA_VERSION="%{version}" -DSONATA_TESTS=ON -DSONATA_CXX_WARNINGS=OFF -DCMAKE_CXX_STANDARD=17
%cmake_build

# python bits need to be run in the out of source build directory so we need to
# move some files to allow that
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
cp -a README.rst %{__cmake_builddir}
cp -a setup.py %{__cmake_builddir}
cp -a pyproject.toml %{__cmake_builddir}
cp -a COPYING.* %{__cmake_builddir}
cp -a MANIFEST.* %{__cmake_builddir}
mkdir -p %{__cmake_builddir}/python/libsonata/
cp -a python/libsonata/__init__.py %{__cmake_builddir}/python/libsonata
pushd %{__cmake_builddir}
%pyproject_wheel
popd

# regenerate data files and copy to build dir
pushd tests/data
%{python3} generate.py
popd
mkdir -p %{__cmake_builddir}/tests
cp -a tests/data %{__cmake_builddir}/tests

%install
%cmake_install
# remove static lib
rm -rf %{buildroot}/%{_libdir}/libsonata.a
# neither cmake nor pyproject install python module(!?)
install -p -m 0655 -D -t %{buildroot}/%{python3_sitearch}/libsonata/ %{__cmake_builddir}/python/_libsonata*so

export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
pushd %{__cmake_builddir}
%pyproject_install
%pyproject_save_files libsonata
popd


%check
%ctest tests

# There are some messages related to HDF5-DIAG, but upstream's CI also gets them, for example:
# https://github.com/BlueBrain/libsonata/runs/5272240111?check_suite_focus=true
pushd python/tests
export PYTHONPATH=%{buildroot}/%{python3_sitearch}/
%{python3} -m unittest -v
popd

%files
%license COPYING.LESSER
%doc README.rst CHANGELOG.md
%{_libdir}/libsonata.so.0.1
%{_libdir}/libsonata.so.0.1.23

%files devel
%{_includedir}/bbp
%{_datadir}/sonata/
%{_libdir}/libsonata.so

%files -n python3-libsonata -f %{pyproject_files}
%doc README.rst CHANGELOG.md
%{python3_sitearch}/libsonata/_libsonata*so

%changelog
%autochangelog
