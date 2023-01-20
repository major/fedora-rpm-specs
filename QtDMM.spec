Name: QtDMM
Version: 0.8.12
Release: 26%{?dist}
Summary: A digital multimeter readout software
License: GPLv2+

URL: http://www.mtoussaint.de/qtdmm.html
Source: http://www.mtoussaint.de/qtdmm-%{version}.tgz
Patch1: qtdmm-0.8.12-desktop.patch
Patch2: qtdmm-0.8.12-xpm-warnings.patch
Patch3: qtdmm-0.8.12-warnings.patch

Requires: electronics-menu
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires: qt3-devel, desktop-file-utils

%description
QtDMM is a DMM readout software including a configurable recorder.
The recorder features manual start, scheduled start (at a given time),
triggered automatic start when given thresholds are reached, and the
ability to display more than one value from the multimeter.
It was written for Metex (and compatible like VOLTCRAFT) multimeter
which use an 14 byte protocol. Later several more protocols have been added.
For more information on the currently supported DMM's have a look at
the preset table.

%prep
%setup -q

%patch1 -p1 -b .desktop
%patch2 -p1 -b .xpm-warnings
%patch3 -p1 -b .warnings

chmod a-x src/*.cpp src/*.h

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
install -p -d $RPM_BUILD_ROOT%{_bindir}
install -p -d $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -p -d $RPM_BUILD_ROOT%{_datadir}/applications
install -p -d $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m 755 bin/qtdmm $RPM_BUILD_ROOT%{_bindir}
install -p -m 644 qtdmm.png $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -p -m 644 qtdmm.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
desktop-file-install \
	--vendor="" \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	--add-category "Engineering;Electronics;" \
	--delete-original \
	QtDMM.desktop

%files
%doc README AUTHORS CHANGELOG COPYING
%{_bindir}/qtdmm
%{_datadir}/applications/QtDMM.desktop
%{_datadir}/pixmaps/qtdmm.png
%{_mandir}/man1/%{name}.1.gz

%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.12-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.12-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.12-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.12-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.12-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.12-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.12-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.12-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.12-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.12-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.12-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.12-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.12-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.8.12-10
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.12-4
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jun  6 2009 Andrew Zabolotny <zap@homelink.ru> 0.8.12-1
- updated to latest version
- Fedora packaging guidelines

* Thu Nov 23 2006 Radek Liboska <liboska@uochb.cas.cz>
- 0.8.8

* Sat Sep 23 2006 Radek Liboska <liboska@uochb.cas.cz>
- License added, install bug (strip) corrected

* Wed Dec 28 2005 Radek Liboska <liboska@uochb.cas.cz>
- 0.8.7

* Wed Aug 17 2005 Radek Liboska <liboska@uochb.cas.cz>
- 0.8.6

* Mon Jun 28 2005 Radek Liboska <liboska@uochb.cas.cz>
- 0.8.5

* Mon May  2 2005 Radek Liboska <liboska@uochb.cas.cz>
- 0.8.4

* Fri Apr 29 2005 Radek Liboska <liboska@uochb.cas.cz>
- 0.8.3

* Fri Oct 18 2002 Radek Liboska <liboska@uochb.cas.cz>
- 0.8.1

* Tue May  7 2002 Radek Liboska <liboska@uochb.cas.cz>
- ports ttyS4-ttyS7 added

* Wed Mar  6 2002 Radek Liboska <liboska@uochb.cas.cz>
- 0.7

* Tue Nov 27 2001 Radek Liboska <liboska@uochb.cas.cz>
- 0.6 

* Tue Sep  4 2001 Radek Liboska <liboska@uochb.cas.cz>
- 0.5 Second RPM release
- 0.4 Initial RPM release
