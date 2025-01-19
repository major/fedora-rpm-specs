%global srcname OpenIGTLink
%global _docdir_fmt %{name}

Name:		openigtlink
Version:	2.1
Release:	21%{?dist}
Summary:	Implementation of the OpenIGTLink network communication protocol

# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		http://openigtlink.org
Source0:	https://github.com/openigtlink/OpenIGTLink/archive/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

# RHBZ1509365
Patch2:		openigtlink-install_cmake.patch

# RHBZ1509407
Patch3:		openigtlink-install_headers.patch

BuildRequires:	gcc-c++
BuildRequires:	cmake


%description
OpenIGTLink is a network communication protocol specifically designed and
developed for research on image-guided and computer-assisted interventions. It
provides a standardized mechanism for communications among computers and
devices in operating rooms (OR) for a wide variety of image-guided therapy
(IGT) applications. Examples of such applications include:

- Stereotactic surgical guidance using optical position sensor and medical
  image visualization software
- Intraoperative image guidance using real-time MRI and medical image
  visualization software
- Robot-assisted interventions using robotic devices and surgical planning
  software

OpenIGTLink is a set of messaging formats and rules (protocol) used for data
exchange on a local area network (LAN). The specification of OpenIGTLink and
its reference implementation, the OpenIGTLink Library, are available free of
charge for any purpose including commercial use.


%package devel
Summary:	OpenIGTLink development files
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	cmake%{?_isa}

%description devel
Development files for the OpenIGTLink library.

%prep
%autosetup -n %{srcname}-%{version} -p1
find . -type f -executable -a \( -name '*.h' -o -name '*.cxx' \) -exec chmod a-x {} +


%build
# disable gtest due to upstream bug #122
%cmake \
    -DUSE_GTEST=OFF \
    -D%{srcname}_INSTALL_LIB_DIR=%{_lib} \
    -D%{srcname}_INSTALL_PACKAGE_DIR=%{_lib}/cmake/%{srcname} \
    -D%{srcname}_LEGACY_REMOVE=ON \
%cmake_build


%install
%cmake_install

%check
%global _smp_mflags -j1
%ctest

%files
%license LICENSE.txt
%{_libdir}/lib%{srcname}.so.*

%files devel
%doc README.md
%{_libdir}/lib%{srcname}.so
%{_libdir}/cmake/%{srcname}/
%{_includedir}/igtl/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1-20
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 04 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.1-10
- Make ctest run serially

* Fri Sep 04 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.1-9
- Use cmake macros to fix build

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Nov 19 2017 Dmitry Mikhirev <mikhirev@gmail.com> - 2.1-1
- Upstream release 2.1

* Sun Nov 19 2017 Dmitry Mikhirev <mikhirev@gmail.com> - 2.0-6
- Install igtl_status.h file #1509407
- Fix paths in cmake configuration file #1509365

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sun Mar 12 2017 Dmitry Mikhirev <mikhirev@gmail.com> 2.0-2
- Fix test failure on ppc64 and re-enable build on ppc64 #1427300

* Wed Feb 22 2017 Dmitry Mikhirev <mikhirev@gmail.com> 2.0-1
- Update to 2.0 release
- Fix FTBFS #1424021

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20151015gitccb2438
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20151015gitccb2438
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 28 2015 Dmitry Mikhirev <mikhirev@gmail.com> 0-0.1.20151015gitccb2438
- Initial package
