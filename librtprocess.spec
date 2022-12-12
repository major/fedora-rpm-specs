Name:           librtprocess
Version:        0.12.0
Release:        6%{?dist}
Summary:        RawTherapee's processing algorithms

# The entire source is GPL-3.0-or-later, except:
# - BSL-1.0: src/include/helpersse2.h
#            src/include/sleef.h
#            src/include/sleefsseavx.h
License:        GPL-3.0-or-later AND BSL-1.0
URL:            https://github.com/CarVac/librtprocess
Source0:        %{url}/archive/%{version}/librtprocess-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make

%description
This is a project that aims to make some of RawTherapee's highly optimized
raw processing routines readily available for other FOSS photo editing
software.
The goal is to move certain source files from RawTherapee into this library.
Thus, any changes to the source can be done here and will be used by the
projects which use librtprocess.


%package devel
Summary:        Libraries, includes, etc. used to develop an application with librtprocess
License:        GPLv3
Requires:       %{name}%{_isa} = %{version}-%{release}

%description devel
These are the files needed to develop an application using librtprocess.


%prep
%autosetup


%build
%cmake
%cmake_build


%install
%cmake_install


%files
%license LICENSE.txt
%doc README.md
%{_libdir}/*.so.0
%{_libdir}/*.so.0.0.1

%files devel
%{_includedir}/rtprocess
%{_libdir}/*.so
%{_libdir}/pkgconfig/rtprocess.pc
%{_libdir}/cmake/rtprocess/


%changelog
* Thu Dec 08 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 0.12.0-6
- Update License to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Mar 16 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 0.12.0-4
- Update to tagged 0.12.0 release with assorted minor fixes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Mar 07 2021 Mattia Verga <mattia.verga@protonmail.com> - 0.12.0-1
- Initial import
