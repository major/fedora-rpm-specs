%global git_commit 364732e348679893686ae46e8747cb17b0656d86
%global git_date 20220222

%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}

Name:          vmmlib
Version:       1.8.0
Release:       0.8.%{git_suffix}%{?dist}
Summary:       A vector and matrix math library implemented using C++ templates
# Automatically converted from old format: BSD - review is highly recommended.
License:       LicenseRef-Callaway-BSD
#URL:           http://vmmlib.sourceforge.net/
URL:           http://github.com/VMML/vmmlib/
#Source0:       http://github.com/VMML/vmmlib/archive/release-%%{version}.tar.gz#/%%{name}-release-%%{version}.tar.gz
Source0:       %{url}/archive/%{git_commit}/%{name}-%{version}-%{git_suffix}.tar.gz
BuildArch:     noarch
BuildRequires: gcc-c++
BuildRequires: doxygen
BuildRequires: cmake
BuildRequires: boost-devel
# https://github.com/VMML/vmmlib/pull/101
Patch0:        vmmlib-1.8.0-gcc-13-fix.patch

%description
vmmlib is a vector and matrix math library implemented using C++ templates.
Its basic functionality includes a vector and a matrix class, with additional
functionality for the often-used 3d and 4d vectors and 3x3 and 4x4 matrices.
More advanced functionality include solvers, frustum computations and frustum
culling classes, and spatial data structures.

%package devel
Summary:       A vector and matrix math library implemented using C++ templates
Requires:      pkgconfig, cmake

%description devel
vmmlib is a vector and matrix math library implemented using C++ templates.
Its basic functionality includes a vector and a matrix class, with additional
functionality for the often-used 3d and 4d vectors and 3x3 and 4x4 matrices.
More advanced functionality include solvers, frustum computations and frustum
culling classes, and spatial data structures.

%prep
%autosetup -p1 -n %{name}-%{git_commit}

%build
%cmake
%cmake_build

%install
%cmake_install
rm -r %{buildroot}%{_datadir}/vmmlib/tests/*
rmdir %{buildroot}%{_datadir}/vmmlib/tests
mkdir -p %{buildroot}%{_includedir}
cp -a vmmlib %{buildroot}%{_includedir}

%check
%ctest

%files devel
%license LICENSE.txt
%doc doc/RELNOTES.md CHANGES README.md AUTHORS ACKNOWLEDGEMENTS
%{_includedir}/vmmlib
%{_datadir}/vmmlib/CMake/*.cmake

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-0.8.20220222git364732e3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.8.0-0.7.20220222git364732e3
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-0.6.20220222git364732e3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-0.5.20220222git364732e3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-0.4.20220222git364732e3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-0.3.20220222git364732e3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-0.2.20220222git364732e3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb 22 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 1.8.0-0.1.20220222git364732e3
- New version
  Resolves: rhbz#2047102

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-18.20140319git925a709b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-17.20140319git925a709b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 13 2021 Björn Esser <besser82@fedoraproject.org> - 1.6.2-16.20140319git925a709b
- Properly set BLA_VENDOR to FlexiBLAS for cmake >= 3.19

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-15.20140319git925a709b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 27 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.6.2-14.20140319git925a709b
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-13.20140319git925a709b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-12.20140319git925a709b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-11.20140319git925a709b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-10.20140319git925a709b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-9.20140319git925a709b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-8.20140319git925a709b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-7.20140319git925a709b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-6.20140319git925a709b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun  8 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 1.6.2-5.20140319git925a709b
- Fixed build requirements to require gcc-c++
  Resolves: rhbz#1230504

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-4.20140319git925a709b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-3.20140319git925a709b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-2.20140319git925a709b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 19 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 1.6.2-1.20140319git925a709b
- New version

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.6.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.5.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.4.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.3.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 20 2011 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0-0.2.rc1
- Added dist tag to spec

* Tue Dec 20 2011 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0-0.1.rc1
- New version

* Tue Dec 13 2011 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.4.20111214svn558
- New svn snapshot that fixes cp3_tensor test

* Tue Dec 13 2011 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.3.20111214svn556
- New svn snapshot that fixes several problems in unit test

* Tue Dec 13 2011 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.2.20111122svn540
- Fixed unit test on 64 bit

* Tue Nov 22 2011 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.1.20111122svn540
- Initial release
