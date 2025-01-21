%undefine __cmake_in_source_build

Summary:        Taglib support for other formats 
Name:           taglib-extras
Version:        1.0.1
Release:        33%{?dist}

# all LGPLv2, except for rmff/ which is GPLv2+/LGPLv2+
# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            http://websvn.kde.org/trunk/kdesupport/taglib-extras/
Source0:	http://www.kollide.net/~jefferai/taglib-extras-%{version}.tar.gz

# taglib-extras-config: drop multilib-conflicting mention of libdir, since
# it's already in default linker search path
Patch1: taglib-extras-0.1-multilib-1.patch

## upstreamable patches
Patch50: taglib-extras-1.0.1-taglib_ver.patch

## upstream patches
Patch100: taglib-extras-1.0.1-version.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires: cmake3 >= 2.6.0
BuildRequires: pkgconfig
BuildRequires: taglib-devel >= 1.6

%description
Taglib-extras delivers support for reading and editing the meta-data of 
audio formats not supported by taglib, including: asf, mp4v2, rmff, wav.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: taglib-devel
%description devel
%{summary}.


%prep
%setup -q 

%patch -P1 -p1 -b .multilib
%patch -P50 -p1 -b .taglib_ver
%patch -P100 -p1 -b .version


%build
%{cmake3}
%cmake3_build


%install
%cmake3_install


%ldconfig_scriptlets

%files
%license COPYING.LGPL
%{_libdir}/libtag-extras.so.1*

%files devel
%{_bindir}/taglib-extras-config
%{_includedir}/taglib-extras/
%{_libdir}/libtag-extras.so
%{_libdir}/pkgconfig/taglib-extras.pc


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.1-32
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 08 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.0.1-18
- use %%make_build %%ldconfig_scriptlets
- drop hard-coded Requires: taglib

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 14 2016 Rex Dieter <rdieter@fedoraproject.org> 1.0.1-13
- cleanup, use %%license, FTBFS against taglib-1.10+ (#1308174)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.1-10
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 19 2014 Rex Dieter <rdieter@fedoraproject.org> 1.0.1-8
- .spec cleanup

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Sep 21 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.0.1-1
- taglib-extras-1.0.1

* Thu Sep 17 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.0.0-2
- drop (deprecated/no-op) kde integration

* Thu Sep 17 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.0.0-1
- taglib-extras-1.0.0 (API/ABI bump)

* Wed Sep 09 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.1.7-1
- taglib-extras-0.1.7

* Mon Aug 03 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.1.6-1
- taglib-extras-0.1.6

* Fri Jul 24 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.1.5-1
- taglib-extras-0.1.5

* Fri Jun 12 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.1.4-1
- taglib-extras-0.1.4

* Sat May 02 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.1.3-1
- taglib-extras-0.1.3

* Thu Apr 07 2009 Eelko Berkenpies <fedora@berkenpies.nl> - 0.1.2-1
- taglib-extras-0.1.2

* Thu Mar 26 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.1.1-2
- enable KDE integration, -DWITH_KDE

* Tue Mar 24 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.1.1-1
- taglib-extras-0.1.1

* Tue Mar 24 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.1-4
- refetch tarball

* Mon Mar 23 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.1-3
- -devel: Requires: taglib-devel
- Source0: full URL

* Mon Mar 23 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.1-2
- fixup for review

* Fri Mar 20 2009 Eelko Berkenpies <fedora@berkenpies.nl> - 0.1-1
- initial package
