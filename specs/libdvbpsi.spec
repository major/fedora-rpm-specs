%global commit0 26bdfd4c0dc58f0f4917461cdf31dae24f9e1463
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary:	Library for MPEG TS and DVB PSI tables decoding and generation
Name:		libdvbpsi
Version:	1.3.3
Release:	16%{?dist}
License:	LGPL-2.1-or-later
URL:		http://www.videolan.org/developers/libdvbpsi.html
Source0:        https://code.videolan.org/videolan/libdvbpsi/-/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

BuildRequires:	gcc
BuildRequires:	graphviz doxygen
BuildRequires:	libtool
BuildRequires: make

%package devel
Summary:	Development package for %{name}
Requires:	%{name}%{_isa} = %{version}-%{release}

%package doc
Summary:	Documentation for %{name}


%description
libdvbpsi is a very simple and fully portable library designed for
MPEG TS and DVB PSI table decoding and generation.

%description devel
libdvbpsi is a very simple and fully portable library designed for
MPEG TS and DVB PSI table decoding and generation.
This package contains development files for %{name}

%description doc
Documentation for %{name}.


%prep
%setup -q -n %{name}-%{commit0}
autoreconf -vif


%build
%configure --disable-dependency-tracking --disable-static
%make_build
%make_build doc


%install
%make_install
rm -f %{buildroot}%{_libdir}/lib*.la


%ldconfig_scriptlets


%files
%doc AUTHORS ChangeLog README
%license COPYING
%{_libdir}/%{name}.so.10{,.*}

%files devel
%{_includedir}/dvbpsi/
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/libdvbpsi.pc

%files doc
%doc doc/doxygen/html


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Oct 21 2024 Nicolas Chauvet <kwizart@gmail.com> - 1.3.3-15
- Revert to plain 1.3.3 commit hash

* Thu Oct 10 2024 Nicolas Chauvet <kwizart@gmail.com> - 1.3.3-14
- Update snapshot

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3.3-13
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 22 2019 Nicolas Chauvet <kwizart@gmail.com> - 1.3.3-1
- Update to 1.3.3

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.3.2-1
- Update to 1.3.2

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 16 2017 Nicolas Chauvet <kwizart@gmail.com> - 1.3.1-1
- Update to 1.3.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 26 2016 Nicolas Chauvet <kwizart@gmail.com> - 1.3.0-3
- Add doc sub-package
- clean mixed tab and space
- add %%{?_smp_mflags} for doc

* Thu Sep 15 2016 Nicolas Chauvet <kwizart@gmail.com> - 1.3.0-2
- Spec file clean-up

* Sat Oct 24 2015 Nicolas Chauvet <kwizart@gmail.com> - 1.3.0-1
- Update to 1.3.0

* Sat Oct 24 2015 Nicolas Chauvet <kwizart@gmail.com> - 1.2.0-3
- backport patch - rfbz#3729

* Sun Apr 26 2015 Nicolas Chauvet <kwizart@gmail.com> - 1.2.0-2
- Backport patch to disable Werror - fix f22

* Sat Nov 15 2014 Nicolas Chauvet <kwizart@gmail.com> - 1.2.0-1
- Update to 1.2.0

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Nov 10 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.1.2-1
- Update to 1.1.2

* Sun Apr 28 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.1.0-1
- Update to 1.1.0

* Sun Mar 10 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.0.0-1
- Update to 1.0.0
- Clean-up spec file

* Sun Nov 11 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.0.0-0.2_pre3
- Update to _pre3 as tagged in git

* Thu Oct 18 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.0.0-0.1_pre2
- Update to 1.0.0_pre2

* Wed Jan 25 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 05 2011 Nicolas Chauvet <kwizart@gmail.com> - 0.2.2-1
- Update to 0.2.2

* Tue May 10 2011 Nicolas Chauvet <kwizart@gmail.com> - 0.2.0-1
- Update to 0.2.0
- Switch to LGPLv2+

* Sat Apr 24 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 0.1.7-1
- Update to 0.1.7

* Sat Oct 17 2009 kwizart < kwizart at gmail.com > - 0.1.6-6
- Rebuild

* Sun Apr  5 2009 kwizart < kwizart at gmail.com > - 0.1.6-5
- Rebuild

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.1.6-4
- rebuild for new F11 features

* Mon Aug 04 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 0.1.6-3
- rebuild

* Tue Feb 26 2008 kwizart < kwizart at gmail.com > - 0.1.6-2
- Rebuild for gcc43

* Mon Oct 22 2007 kwizart < kwizart at gmail.com > - 0.1.6-1
- Update to 0.1.6

* Sun Oct 14 2007 kwizart < kwizart at gmail.com > - 0.1.5-3
- Rpmfusion Merge Review

* Mon Mar 13 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> 0.1.5-2
- Drop Epoch completely

* Thu Mar 09 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- switch to new release field

* Tue Feb 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist

* Tue Jul 12 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:0.1.5-0.lvn.1
- 0.1.5.
- Build with dependency tracking disabled.
- Miscellaneous specfile cleanups.

* Mon May 17 2004 Dams <anvil[AT]livna.org> - 0:0.1.3-0.lvn.4
- Added url in Source0

* Sun Sep 28 2003 Dams <anvil[AT]livna.org> 0:0.1.3-0.fdr.3
- Removed comment after scriptlets

* Mon Aug 18 2003 Dams <anvil[AT]livna.org> 0:0.1.3-0.fdr.2
- Moved some doc to devel package

* Sat Aug 16 2003 Dams <anvil[AT]livna.org> 0:0.1.3-0.fdr.1
- Added post/postun scriptlets
- Using RPM_OPT_FLAGS
- Updated to 0.1.3

* Sun Jun 29 2003 Dams <anvil[AT]livna.org> 
- Initial build.
