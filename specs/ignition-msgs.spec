%undefine __cmake_in_source_build
%global abiver 1

Name:		ignition-msgs
Version:	1.0.0
Release:	23%{?dist}
Summary:	Common messages for the ignition framework

# Bundled gtest and python helper scripts are licensed BSD, but not included in installation
# Installed files are Apache 2
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:	Apache-2.0
URL:		http://www.ignitionrobotics.org
Source0:	http://gazebosim.org/distributions/ign-msgs/releases/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:  ignition-cmake-devel
BuildRequires:	ignition-math-devel >= 4
BuildRequires:	protobuf-devel

%description
A standard set of message definitions, used by Ignition Transport, and
other applications.  Contains pre-compiled protobuf definitions of messages
for re-use by other libraries and applications.

%package devel
Summary: Development libraries and headers for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: ignition-math-devel
Requires: protobuf-devel

%description devel
%{summary}

%package doc
Summary: Development documentation for ignition-msgs
BuildArch: noarch

%description doc
Automatically generated API documentation for the ignition-msgs library

%prep
%autosetup

%build
export CXXFLAGS="%{optflags} -Wl,--as-needed"
%cmake \
%ifnarch x86_64
  -DSSE2_FOUND=FALSE \
%endif
  -DSSE3_FOUND=FALSE \
  -DSSSE3_FOUND=FALSE \
  -DSSE4_1_FOUND=FALSE \
  -DSSE4_2_FOUND=FALSE \
  -DCMAKE_C_FLAGS_ALL="%{optflags}" \
  -DCMAKE_CXX_FLAGS_ALL="%{optflags}" \
  -DCMAKE_BUILD_TYPE=Release


%cmake_build
%cmake_build --target doc

%install
%cmake_install
rm -fr %{buildroot}%{_prefix}/lib/ruby

%check
%ctest

%files
%license COPYING LICENSE
%doc AUTHORS NEWS README.md
%{_libdir}/*.so.%{version}
%{_libdir}/*.so.%{abiver}
%{_datadir}/ignition

%files devel
%{_libdir}/*.so
%{_includedir}/ignition
%{_libdir}/cmake/%{name}%{abiver}
%{_libdir}/pkgconfig/*.pc

%files doc
%license COPYING LICENSE
%doc %{_vpath_builddir}/doxygen/html

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.0-22
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 06 2021 Adrian Reber <adrian@lisas.de> - 1.0.0-14
- Rebuilt for protobuf 3.19.0

* Mon Oct 25 2021 Adrian Reber <adrian@lisas.de> - 1.0.0-13
- Rebuilt for protobuf 3.18.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 14:23:51 CET 2021 Adrian Reber <adrian@lisas.de> - 1.0.0-10
- Rebuilt for protobuf 3.14

* Thu Sep 24 2020 Adrian Reber <adrian@lisas.de> - 1.0.0-9
- Rebuilt for protobuf 3.13

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 14 2020 Adrian Reber <adrian@lisas.de> - 1.0.0-6
- Rebuilt for protobuf 3.12

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Orion Poplawski <orion@nwra.com> - 1.0.0-4
- Rebuild for protobuf 3.11

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 23 2018 Rich Mattes <richmattes@gmail.com> - 1.0.0-1
- Update to 1.0.0

* Thu Nov 22 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.0-12
- Rebuild for protobuf 3.6

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 30 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.7.0-9
- Rebuild for protobuf 3.5

* Mon Nov 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.0-8
- Rebuild for protobuf 3.4

* Mon Aug 07 2017 Björn Esser <besser82@fedoraproject.org> - 0.7.0-7
- Rebuilt for AutoReq cmake-filesystem

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Orion Poplawski <orion@cora.nwra.com> - 0.7.0-4
- Rebuild for protobuf 3.3.1

* Tue Mar 28 2017 Rich Mattes <richmattes@gmail.com> - 0.7.0-3
- Add --as-needed link flags

* Sun Mar 05 2017 Rich Mattes <richmattes@gmail.com> - 0.7.0-2
- Create a separate -doc subpackage for documentation

* Sun Mar 05 2017 Rich Mattes <richmattes@gmail.com> - 0.7.0-1
- Update to release 0.7.0

* Mon Jan 09 2017 Rich Mattes <richmattes@gmail.com> - 0.6.1-1
- Initial package
