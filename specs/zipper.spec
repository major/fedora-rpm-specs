Name:           zipper
Summary:        C++ wrapper around minizip compression library
Version:        1.0.3
Release:        10%{?dist}
URL:            https://github.com/sebastiandev/zipper

## Source archive from github obtained by
## git clone -b v1.0.3 --depth 1 --single-branch --progress --recursive https://github.com/sebastiandev/zipper.git
## rm -rf zipper/.git*
## tar -czvf  zipper-1.0.3.tar.gz zipper
Source0:        https://github.com/sebastiandev/zipper/archive/zipper/%{name}-%{version}.tar.gz

#Patch0:         zipper-unbundle_minizip.patch
Patch1:         zipper-gcc14.patch

# zlib and GPL+ (no version) licenses come from minizip/ source code
License:        MIT AND ZLIB AND GPL-1.0-or-later

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(zlib)
#BuildRequires:  minizip-compat-devel
Provides: bundled(minizip) = 1.1

%description
Zipper brings the power and simplicity of minizip to a more
object oriented/c++ user friendly library.
It was born out of the necessity of a compression library that would be
reliable, simple and flexible. 
By flexibility I mean supporting all kinds of inputs and outputs,
but specifically been able to compress into memory instead of been
restricted to file compression only, and using data from memory instead
of just files as well.

Features:
- Create zip in memory
- Allow files, vector and generic streams as input to zip
- File mappings for replacing strategies
  (overwrite if exists or use alternative name from mapping)
- Password protected zip
- Multi platform

%package devel
Summary: Development files of %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides header files, shared and static library files of %{name}.

%package static
Summary: Static library of %{name}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}

%description static
This package provides static library file of %{name}.

%prep
%autosetup -n %{name} -p1

%build
%cmake -Wno-cpp -Wno-dev \
 -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} -DBUILD_SHARED_VERSION:BOOL=ON -DBUILD_STATIC_VERSION:BOOL=ON \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE -DCMAKE_COLOR_MAKEFILE:BOOL=ON \
 -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES -DCMAKE_SKIP_RPATH:BOOL=YES \
 -DINSTALL_PKGCONFIG_DIR:PATH=%{_libdir}/pkgconfig \
 -DZLIB_INCLUDE_DIR:PATH=%{_includedir} -DZLIB_LIBRARY_RELEASE:FILEPATH=%{_libdir}/libz.so
%cmake_build

%install
%cmake_install

rm -f %{buildroot}%{_bindir}/Zipper-test

%check
%ctest

%files
%doc README.md VERSION.txt
%license LICENSE.md
%{_libdir}/*.so.1
%{_libdir}/*.so.1.0.2

%files devel
%{_libdir}/*.so
%{_includedir}/zipper/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/*.cmake

%files static
%{_libdir}/libZipper.a
%{_libdir}/libZipper-static.a

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Mar 17 2024 Antonio Trande <sagitter@fedoraproject.org> - 1.0.3-8
- Patched for GCC-14

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 14 2021 Antonio Trande <sagitter@fedoraproject.org> - 1.0.3-1
- Release 1.0.3

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 09 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.0.1-1
- Release 1.0.1

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-7.20170831giteee877a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-6.20170831giteee877a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-5.20170831giteee877a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-4.20170831giteee877a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 03 2018 Antonio Trande <sagitter@fedoraproject.org> - 0.9.1-3.20170831giteee877a
- Rebuild for batched updates

* Sun Apr 29 2018 Antonio Trande <sagitter@fedoraproject.org> - 0.9.1-2.20170831giteee877a
- Specify bundled code's license and version

* Thu Apr 19 2018 Antonio Trande <sagitter@fedoraproject.org> - 0.9.1-1.20170831giteee877a
- First package
