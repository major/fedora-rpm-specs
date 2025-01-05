Name:           libmamba
Version:        1.5.12
Release:        1%{?dist}
Summary:        C++ API for mamba depsolving library

License:        BSD-3-Clause
URL:            https://github.com/mamba-org/mamba
Source0:        https://github.com/mamba-org/mamba/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
# Force the install to be arch dependent
Source1:        setup.py
# Upstream fix for csh file
Patch0:         libmamba-csh.patch
# https://github.com/mamba-org/mamba/pull/3016
Patch1:         libmamba-deps.patch
# Use Fedora versions of yaml-cpp and zstd
Patch2:         libmamba-fedora.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  bzip2-devel
BuildRequires:  fmt-devel
BuildRequires:  gtest-devel
BuildRequires:  json-devel
BuildRequires:  libarchive-devel
BuildRequires:  libcurl-devel
# Need CONDA_ADD_USE_ONLY_TAR_BZ2
BuildRequires:  libsolv-devel
BuildRequires:  openssl-devel
BuildRequires:  reproc-devel
BuildRequires:  cmake(simdjson)
BuildRequires:  spdlog-devel
BuildRequires:  cmake(tl-expected)
BuildRequires:  yaml-cpp-devel
# This is not yet provided by Fedora package
# https://src.fedoraproject.org/rpms/zstd/pull-request/7
#BuildRequires:  cmake(zstd)
BuildRequires:  libzstd-devel

%description
libmamba is a reimplementation of the conda package manager in C++.

* parallel downloading of repository data and package files using multi-
  threading
* libsolv for much faster dependency solving, a state of the art library used
  in the RPM package manager of Red Hat, Fedora and OpenSUSE
* core parts of mamba are implemented in C++ for maximum efficiency


%package        devel
Summary:        Development files for %{name}
License:        MIT
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake-filesystem
Requires:       pkgconfig
Requires:       fmt-devel%{?_isa}
Requires:       json-devel%{?_isa}
Requires:       libsolv-devel%{?_isa}
Requires:       reproc-devel%{?_isa}
Requires:       spdlog-devel%{?_isa}
Requires:       cmake(tl-expected)
Requires:       yaml-cpp-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package -n     micromamba
Summary:        Tiny version of the mamba package manager
BuildRequires:  cli11-devel
BuildRequires:  pybind11-devel
# Generate a simple man page until https://github.com/mamba-org/mamba/issues/3032 is addressed
BuildRequires:  help2man
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n micromamba
micromamba is a tiny version of the mamba package manager. It is a C++
executable with a separate command line interface. It does not need a base
environment and does not come with a default version of Python.


%package -n     python3-libmambapy
Summary:        Python bindings for libmamba
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python3-libmambapy
Python bindings for libmamba.


%prep
%autosetup -p1 -n mamba-libmamba-%{version}
cp -p %SOURCE1 libmambapy/setup.py
sed -i '/LIBRARY DESTINATION/s,\${CMAKE_CURRENT_SOURCE_DIR},${Python_STDARCH}/site-packages,' libmambapy/CMakeLists.txt


%build
%cmake \
   -DCMAKE_BUILD_TYPE=RelWithDebInfo \
   -DBUILD_LIBMAMBA=ON \
   -DBUILD_LIBMAMBAPY=ON \
   -DBUILD_MICROMAMBA=ON \
   -DBUILD_EXE=ON \
   -DBUILD_SHARED=ON \
   -DBUILD_STATIC=OFF \
   -DENABLE_TESTS=ON
%cmake_build
cd libmambapy
%pyproject_wheel
cd -
help2man %{_vpath_builddir}/micromamba/micromamba > %{_vpath_builddir}/micromamba/micromamba.1


%install
%cmake_install
cd libmambapy
%pyproject_install
%pyproject_save_files libmambapy
cd -

# Install init scripts
mkdir -p %{buildroot}/etc/profile.d
for shell in csh sh 
do
  sed -e 's,\$MAMBA_EXE,%{_bindir}/micromamba,' < libmamba/data/micromamba.$shell > %{buildroot}/etc/profile.d/micromamba.$shell
done
mkdir -p %{buildroot}%{_datadir}/fish/vendor_conf.d
sed -e 's,\$MAMBA_EXE,%{_bindir}/micromamba,' < libmamba/data/mamba.fish > %{buildroot}%{_datadir}/fish/vendor_conf.d/micromamba.fish

# man page
mkdir -p %{buildroot}%{_mandir}/man1
cp -p %{_vpath_builddir}/micromamba/micromamba.1 %{buildroot}%{_mandir}/man1/


%check
%ctest


%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_libdir}/libmamba.so.2
%{_libdir}/libmamba.so.2.*

%files devel
%{_includedir}/mamba/
%{_libdir}/libmamba.so
%{_libdir}/cmake/%{name}/

%files -n micromamba
# TODO - better ownership of vendor_conf.d
%dir %{_datadir}/fish/vendor_conf.d
%{_datadir}/fish/vendor_conf.d/micromamba.fish
/etc/profile.d/micromamba.sh
/etc/profile.d/micromamba.csh
%{_bindir}/micromamba
%{_mandir}/man1/micromamba.1*

%files -n python3-libmambapy -f %{pyproject_files}
%doc CHANGELOG.md README.md
%{python3_sitearch}/libmambapy/bindings.*


%changelog
* Fri Jan 03 2025 Orion Poplawski <orion@nwra.com> - 1.5.12-1
- Update to 1.5.12

* Sat Nov 30 2024 Orion Poplawski <orion@nwra.com> - 1.5.11-1
- Update to 1.5.11

* Tue Nov 26 2024 František Zatloukal <fzatlouk@redhat.com> - 1.5.10-3
- Rebuilt for spdlog 1.15.0

* Thu Oct 24 2024 Orion Poplawski <orion@nwra.com> - 1.5.10-2
- Drop yaml-cpp patch

* Fri Oct 18 2024 Orion Poplawski <orion@nwra.com> - 1.5.10-1
- Update to 1.5.10

* Fri Aug 02 2024 Orion Poplawski <orion@nwra.com> - 1.5.8-2
- Add patch for fmt 11 support (FTBFS bz#2300904)

* Tue Jul 30 2024 Orion Poplawski <orion@nwra.com> - 1.5.8-1
- Update to 1.5.8

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.5.6-3
- Rebuilt for Python 3.13

* Tue May 21 2024 František Zatloukal <fzatlouk@redhat.com> - 1.5.6-2
- Rebuilt for spdlog 1.14.1

* Fri Feb 23 2024 Orion Poplawski <orion@nwra.com> - 1.5.6-1
- Update to 1.5.6

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 04 2023 Orion Poplawski <orion@nwra.com> - 1.5.3-2
- Generate man page with help2man

* Thu Nov 30 2023 Orion Poplawski <orion@nwra.com> - 1.5.3-1
- Initial package
