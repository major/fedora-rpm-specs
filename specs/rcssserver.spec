Name:           rcssserver
Version:        19.0.0
Release:        4%{?dist}
Summary:        Robocup 2D Soccer Simulation Server

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://sourceforge.net/projects/sserver/
Source0:        http://downloads.sourceforge.net/sserver/%{name}-%{version}.tar.gz
# Source 1 is created by me.
Source1:        %{name}.desktop

BuildRequires:  gcc-c++ cmake cmake boost-devel zlib-devel
BuildRequires:  desktop-file-utils flex bison git

%description
The RoboCup Soccer Simulator Server (rcssserver) is a research and educational
tool for mutli-agent systems and artificial intelligence. It allows 11
simulated autonomous robotic players to play soccer (football).

This package includes the simulation server. If you want to view the games 
you should install and run a monitor (rcssmonitor or rcssmonitor_classic).

%package        devel
Summary:        Header files and libraries for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       boost-devel

%description    devel
This package contains the header files and libraries
for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package        gui
Summary:        A simple way to run 2D Soccer Simulation on a single machine
Requires:       %{name} = %{version}-%{release}
Requires:       rcssmonitor

%description    gui
This package contains rcsoccersim script as simple way for
running 2D Soccer Simulation on a single machine. It'll also
provide a menu entry for this script.

%prep
%autosetup -S git
sed -i.flagfix "/CMAKE_CXX_FLAGS/d" CMakeLists.txt

%build
%cmake
%cmake_build

%install
%cmake_install

desktop-file-install \
  --dir=%{buildroot}/%{_datadir}/applications %{SOURCE1}

%files
%license COPYING.LESSER
%doc AUTHORS ChangeLog NEWS README.md
%{_bindir}/rcss*
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so

%files gui
%{_bindir}/rcsoccersim
%{_datadir}/applications/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 19.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 19.0.0-3
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 19.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Apr 19 2024 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 19.0.0-1
- Update to latest release: 19.0.0

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 18.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 18.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 18.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 06 2023 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 18.1.3-1
- Update to latest upstream version

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 17.0.1-5
- Rebuilt for Boost 1.81

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 17.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 17.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 17.0.1-2
- Rebuilt for Boost 1.78

* Thu Apr 07 2022 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 17.0.1-1
- Update to latest upstream release: 17.0.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 16.0.0-7
- Rebuilt for Boost 1.76

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 16.0.0-4
- Rebuilt for Boost 1.75

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 16.0.0-2
- Rebuilt for Boost 1.73

* Fri May 08 2020 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 16.0.0-1
- Update to 16.0.0 release

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 15.2.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 15.2.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 15.2.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Jonathan Wakely <jwakely@redhat.com> - 15.2.2-28
- Rebuilt for Boost 1.69

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 15.2.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 15.2.2-26
- Add gcc-c++ build dependency

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 15.2.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 15.2.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 15.2.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 04 2017 Jonathan Wakely <jwakely@redhat.com> - 15.2.2-22
- Rebuilt for Boost 1.64

* Wed Feb 22 2017 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 15.2.2-21
- Remove debug output

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 15.2.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 15.2.2-19
- Rebuilt for Boost 1.63

* Fri Mar 04 2016 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 15.2.2-18
- Fix compile using GCC 6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 15.2.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 15.2.2-16
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 15.2.2-15
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 15.2.2-13
- rebuild for Boost 1.58

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 15.2.2-11
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 15.2.2-10
- Rebuild for boost 1.57.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 03 2014 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 15.2.2-8
- handle AArch64 as 64-bit

* Thu Jun 12 2014 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 15.2.2-7
- Fix build errors with bison 3.0

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 15.2.2-5
- Rebuild for boost 1.55.0

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 15.2.2-4
- rebuild for boost 1.55.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 15.2.2-2
- Rebuild for boost 1.54.0

* Sun Jul 21 2013 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 15.2.2-1
- Update to latest upstream version 15.2.2

* Wed May 22 2013 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 15.2.0-1
- Update to new upstream version: 15.2.0
- Fix rpath issue with the latest version

* Wed May 01 2013 Jon Ciesla <limburgher@gmail.com> - 15.1.0-5
- Drop desktop vendor tag.

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 15.1.0-4
- Rebuild for Boost-1.53.0

* Tue Aug 21 2012 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 15.1.0-3
- Rebuild for Boost 1.50
- Don't use boost filesystem v2

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 04 2012 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 15.1.0-1
- Update to version 15.1.0
- Remove some no-longer-necessary lines (e.g. buildroot tag)
- ax_boost_base.m4 patch no longer necessary

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.0.0-6
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 21 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 15.0.0-4
- Rebuild for Boost 1.48

* Fri Jul 22 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 15.0.0-3
- Rebuild for Boost 1.47

* Fri May 27 2011 Dan Horák <dan[at]danny.cz> - 15.0.0-2
- fix build on non-x86 64-bit architectures

* Thu May 19 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 15.0.0-1
- Updated to 15.0.0 upstream version

* Sun Apr 17 2011 Kalev Lember <kalev@smartlink.ee> - 14.0.3-7
- Rebuilt for boost 1.46.1 soname bump

* Sun Feb 13 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 14.0.3-6
- Use CPPFLAGS instead of CXXFLAGS to avoid overwriting RPM flags

* Thu Feb 10 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 14.0.3-5
- Use the old Boost::FileSystem in Boost 1.46

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 07 2011 Thomas Spura <tomspur@fedoraproject.org> - 14.0.3-3
- rebuild for new boost

* Wed Aug 04 2010 Hedayat Vatankhah <hedayat@fedoraproject.org> - 14.0.3-2
- Rebuild for the new boost

* Fri Jun 04 2010 Hedayat Vatankhah <hedayat@grad.com> 14.0.3-1
- Updated to 14.0.3 with some bug fixes

* Mon Jan 18 2010 Hedayat Vatankhah <hedayat@grad.com> 14.0.2-1
- Updated to 14.0.2 with some bug fixes

* Sun Nov 15 2009 Hedayat Vatankhah <hedayat@grad.com> 14.0.1-1
- Updated to 14.0.1 which fixes a bug in the new catch model

* Mon Nov 02 2009 Hedayat Vatankhah <hedayat@grad.com> 14.0.0-1
- Updated to 14.0.0 which brings some new features including:
  - New Dash and Stamina models
  - Introduce fould model
  - Golden goal option

* Wed Aug 05 2009 Hedayat Vatankhah <hedayat@grad.com> 13.2.2-1
- Updated to 13.2.2 which brings some bug fixes

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 22 2009 Hedayat Vatankhah <hedayat@grad.com> 13.2.0-2
- Rebuild for the new boost libraries

* Tue Apr 07 2009 Hedayat Vatankhah <hedayat@grad.com> 13.2.0-1
- Updated to the latest upstream release

* Sun Mar 01 2009 Hedayat Vatankhah <hedayat@grad.com> 13.1.0-3
- Added a patch for gcc 4.4 compatibility.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 18 2008 Hedayat Vatankhah <hedayat@grad.com> 13.1.0-1
- Bump to 13.1.0 version.

* Wed Dec 17 2008 Benjamin Kosnik  <bkoz@redhat.com> 13.0.2-2
- Rebuild for boost-1.37.0.

* Thu Dec 04 2008 Hedayat Vatankhah <hedayat@grad.com> 13.0.2-1
- Bump to 13.0.2 version.

* Wed Nov 19 2008 Hedayat Vatankhah <hedayat@grad.com> 13.0.1-1
- Bump to 13.0.1 version.

* Wed Nov 5 2008 Hedayat Vatankhah <hedayat@grad.com> 13.0.0-1
- Update the package to the new versoin
- Obsoletes rcssbase as it is included in rcssserver

* Sun Oct 26 2008 Hedayat Vatankhah <hedayat@grad.com> 12.1.4-1
- Updated to the latest version.

* Sat Sep 13 2008 Hedayat Vatankhah <hedayat@grad.com> 12.1.3-2
(Thanks to Mamoru Tasaka)
- Fixed License tag
- Fixed gui sub-package requires to include release number of the main package
- Added defattr to -gui files section
- Modules moved completely to the main package (from -devel)
- Fixed libdir problem in 64bit platforms in rcsoccersim.in 

* Thu Sep 11 2008 Hedayat Vatankhah <hedayat@grad.com> 12.1.3-1
- Updated to the latest version (12.1.3)

* Thu Sep 04 2008 Hedayat Vatankhah <hedayat@grad.com> 12.1.1-1
- Some fixes from rcssbase.spec
- Added gui subpackage

* Fri Jul 11 2008 Hedayat Vatankhah <hedayat@grad.com> 12.1.1-1
- Initial version
