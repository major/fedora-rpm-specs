Name:           hercstudio
Version:        1.5.0
Release:        24%{?dist}
Summary:        GUI front-end to the Hercules mainframe Emulator

License:        GPLv3+
URL:            http://www.jacobdekel.com/hercstudio/
Source0:        http://www.jacobdekel.com/hercstudio/herculesstudio-%{version}-src.tar.gz
Source1:        %{name}.desktop
# borrowed from Debian
Source2:        HerculesStudio.1
# make build verbose
Patch0:         herculesstudio-1.5.0-verbose-build.patch
# fix float parsing for correct MIPS display
# https://groups.yahoo.com/neo/groups/hercstudio/conversations/topics/137
Patch1:         herculesstudio-1.5.0-float-mips.patch
Patch2:         herculesstudio-1.5.0-appdata.patch

BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  desktop-file-utils
%if 0%{?fedora}
BuildRequires:  libappstream-glib
%endif
BuildRequires: make

Requires:       hercules


%description
GUI front-end to the Hercules mainframe Emulator.


%prep
%setup -q -c
%patch0 -p1 -b .verbose-build
%patch1 -p2
%patch2 -p2

chmod -x HercUtilities/*.{cpp,h}


%build
%{qmake_qt5}
make %{?_smp_mflags}


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1

install -p -m 755 HerculesStudio $RPM_BUILD_ROOT%{_bindir}
install -p -m 644 HercStudio/icons/tray.xpm $RPM_BUILD_ROOT%{_datadir}/pixmaps/hercstudio.xpm
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/man1/

desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}

%if 0%{?fedora}
DESTDIR=$RPM_BUILD_ROOT appstream-util install %{name}.appdata.xml
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/appdata/*.appdata.xml
%endif


%files
%license COPYING
%{_bindir}/HerculesStudio
%{_datadir}/applications/*.desktop
%if 0%{?fedora}
%{_datadir}/appdata/%{name}.appdata.xml
%endif
%{_datadir}/pixmaps/*
%{_mandir}/man1/HerculesStudio.1*


%changelog
* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 01 2017 Dan Horák <dan[at]danny.cz> - 1.5.0-8
- fix MIPS display
- add man page
- install appdata

* Sun Jul 24 2016 Dan Horák <dan[at]danny.cz> - 1.5.0-7
- rebuilt for #1359391

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> 1.5.0-5
- use %%qmake_qt5 macro to ensure proper build flags

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.5.0-3
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 28 2014 Dan Horák <dan[at]danny.cz> - 1.5.0-1
- update to 1.5.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jan 06 2013 Dan Horák <dan[at]danny.cz> - 1.4.0-1
- update to 1.4.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-4
- Rebuilt for c++ ABI breakage

* Sun Jan 15 2012 Dan Horák <dan[at]danny.cz> - 1.3.0-3
- fix unistd.h include

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 14 2011 Dan Horák <dan[at]danny.cz> - 1.3.0-1
- update to 1.3.0

* Fri Apr 29 2011 Dan Horák <dan[at]danny.cz> - 1.2.0-3
- fix build with gcc 4.6

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 19 2010 Dan Horák <dan[at]danny.cz> - 1.2.0-1
- update to 1.2.0

* Sat Jan 16 2010 Dan Horák <dan[at]danny.cz> - 1.1.0-1
- update to 1.1.0

* Mon Jan 11 2010 Dan Horák <dan[at]danny.cz> - 1.0.0-3
- rebuilt with updated source archive

* Tue Nov 24 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.0.0-2
- rebuild for Qt 4.6.0 RC1 in F13 (was built against Beta 1 with unstable ABI)

* Fri Oct 16 2009 Dan Horák <dan[at]danny.cz> - 1.0.0-1
- update to 1.0.0

* Mon Sep  7 2009 Dan Horák <dan[at]danny.cz> - 1.0-0.2.beta
- add patch for panel buttons from upstream

* Mon Sep  7 2009 Dan Horák <dan[at]danny.cz> - 1.0-0.1.beta
- initial Fedora version
