Name:           chemical-mime-data
Version:        0.1.94
Release:        39%{?dist}
Summary:        Support for chemical/* MIME types

License:        LGPL-2.1-or-later
URL:            https://github.com/dleidert/chemical-mime
# The SF page has been removed
# Source0:        http://downloads.sourceforge.net/chemical-mime/%%{name}-%%{version}.tar.bz2
# The latest release is in the lookaside cache
Source0:        %{name}-%{version}.tar.bz2
Patch0:         chemical-mime-data-0.1.94-turbomole.patch

BuildArch:      noarch
BuildRequires:  gcc
BuildRequires:  ImageMagick
BuildRequires:  intltool
BuildRequires:  libxml2
BuildRequires:  libxslt
BuildRequires:  perl(XML::Parser)
BuildRequires:  shared-mime-info
BuildRequires: make
Requires:       pkgconfig
Requires:       shared-mime-info
Requires:       hicolor-icon-theme

%description
A collection of data files which tries to give support for various chemical
MIME types (chemical/*) on Linux/UNIX desktops. Chemical MIME's have been
proposed in 1995, though it seems they have never been registered with IANA.


%prep
%autosetup -p1
iconv -f iso8859-1 -t utf-8 ChangeLog > ChangeLog.conv && mv -f ChangeLog.conv ChangeLog
sed -i -e '/^libdir/d' chemical-mime-data.pc.in


%build
%configure --disable-update-database \
           --without-gnome-mime \
           --without-pixmaps \
           --without-kde-mime
%make_build


%install
%make_install
cp -pR $RPM_BUILD_ROOT%{_docdir}/%{name} __docs
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}
%find_lang %{name}


%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog HACKING NEWS README THANKS TODO
%doc __docs/*
%{_datadir}/icons/hicolor/*/mimetypes/gnome-mime-chemical.png
%{_datadir}/icons/hicolor/scalable/mimetypes/gnome-mime-chemical.svgz
%{_datadir}/mime/packages/chemical-mime-data.xml
%{_datadir}/pkgconfig/chemical-mime-data.pc


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.94-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.94-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.94-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.94-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Dec 29 2023 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.1.94-35
- Switch to SPDX license identifier
- Remove defunct URLs 

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.94-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.94-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.94-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.94-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.94-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.94-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.94-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.94-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 04 2019 Julian Sikorski <belegdol@fedoraproject.org> - 0.1.94-26
- Disable chemical/x-turbomole-vibrational as it is causing issues (RH #1779397)
- Modernise the .spec file
- Update the URL

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.94-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.94-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.94-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.94-22
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.94-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.94-20
- Remove obsolete scriptlets

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.94-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.94-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.94-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.94-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 09 2014 Rex Dieter <rdieter@fedoraproject.org> 0.1.94-15
- update mime scriptlets

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.94-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.94-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.94-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Julian Sikorski <belegdol@fedoraproject.org> - 0.1.94-11
- Switched from librsvg2 to ImageMagick since rsvg binary is no more

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.94-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 07 2012 Julian Sikorski <belegdol@fedoraproject.org> - 0.1.94-9
- Rebuilt for gcc-4.7
- Dropped obsolete Group, Buildroot, %%clean and %%defattr
- Updated icon cache scriptlets to the latest spec

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.94-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 10 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.1.94-7
- Enabled some turbomole mimetypes (RH #501177)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.94-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Mar 04 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.1.94-5
- Dropped the KDE MIME .desktop files

* Mon Feb 23 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.1.94-4
- Convert the ChangeLog to utf-8

* Sun Aug 26 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.1.94-3
- Adjusted License tag as per latest guidelines

* Mon Feb 12 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.1.94-2
- Whoops. Added intltool and gettext to BuildRequires

* Sun Feb 11 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.1.94-1
- Updated to 0.1.94

* Mon Jan 29 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.1.93-4
- Install *.pc to %%{_datadir}/pkgconfig, change to noarch (#225095).

* Mon Dec 04 2006 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.1.93-3
- Removed INSTALL from %%doc

* Sun Dec 03 2006 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.1.93-2
- Fixed ownership
- Fixed .pc file location

* Sun Dec 03 2006 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.1.93-1
- Initial RPM release
