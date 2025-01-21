%global           upstream_version 4.0

Summary:          The card game Skat
Name:             xskat
# Upstream License requires to alter the version number
# for re-distribution
Version:          %{upstream_version}.0
Release:          36%{?dist}
# https://fedoraproject.org/wiki/Licensing/XSkat_License
License:          XSkat
Source0:          http://www.xskat.de/xskat-%{upstream_version}.tar.gz
Source1:          xskat.desktop
Patch0:           xskat-c99.patch
URL:              http://www.xskat.de/xskat.html
# xskat requires an 10x20 font
Requires:         xorg-x11-fonts-misc
BuildRequires: make
BuildRequires:  gcc
BuildRequires:    imake
BuildRequires:    libX11-devel
BuildRequires:    desktop-file-utils
BuildRequires:    ImageMagick


%description
XSkat lets you play the card game Skat as defined by the official Skat Order.

Features:
    * Single- and multiplayer mode
    * Playing over LAN or IRC
    * Game lists and logs
    * Three types of scoring
    * English or German text
    * German or French suited cards
    * Selectable computer playing strength
    * Pre-definable card distributions
    * Variations: Ramsch, Bock, Kontra & Re, ... 

%prep
%autosetup -p1 -n %{name}-%{upstream_version}

# fix encoding
iconv -f iso8859-1 -t utf-8 CHANGES-de > CHANGES-de.conv && \
touch -r CHANGES-de CHANGES-de.conv && \
mv -f CHANGES-de.conv CHANGES-de

iconv -f iso8859-1 -t utf-8 README-de > README-de.conv && \
touch -r README-de README-de.conv && \
mv -f README-de.conv README-de

iconv -f iso8859-1 -t utf-8 README.IRC-de > README.IRC-de.conv && \
touch -r README.IRC-de README.IRC-de.conv && \
mv -f README.IRC-de.conv README.IRC-de

%build
%configure
make CDEBUGFLAGS="%{optflags}"

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT MANDIR=%{_mandir}/man6 MANSUFFIX=6 install install.man
install -d $RPM_BUILD_ROOT%{_mandir}/de/man6
mv $RPM_BUILD_ROOT%{_mandir}/man6/xskat-de.6 $RPM_BUILD_ROOT%{_mandir}/de/man6/xskat.6
chmod 644 $RPM_BUILD_ROOT%{_mandir}/man6/xskat.6*
chmod 644 $RPM_BUILD_ROOT%{_mandir}/de/man6/xskat.6*

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
convert icon.xbm $RPM_BUILD_ROOT%{_datadir}/pixmaps/xskat.xpm
touch -r icon.xbm $RPM_BUILD_ROOT%{_datadir}/pixmaps/xskat.xpm

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ravi Srinivasan <ravishankar.srinivasan@gmail.com> -->
<!--
EmailAddress: m@il.xskat.de
SentUpstream: 2014-09-25
-->
<application>
  <id type="desktop">xskat.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>A trick taking card game popular in Germany</summary>
  <description>
    <p>
      XSkat is a trick taking card game that is popular in Germany.
      It has single and multiplayer (IRC, LAN) options.
    </p>
  </description>
  <url type="homepage">http://www.xskat.de/xskat.html</url>
</application>
EOF

%files
%doc README* CHANGES*
%{_bindir}/xskat
%{_mandir}/man6/xskat.6.gz
%lang(de) %{_mandir}/de/man6/xskat.6.gz
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/*
%{_datadir}/pixmaps/%{name}.xpm


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 20 2022 Florian Weimer <fweimer@redhat.com> - 4.0.0-30
- Port to C99 (#2155178)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 4.0.0-20
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 4.0.0-13
- Add an AppData file for the software center

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Aug 01 2010 Christian Krause <chkr@fedoraproject.org> - 4.0.0-5
- Change "Categories" in xskat.desktop to "Game;CardGame;"
  (BZ 619223)

* Thu Nov 12 2009 Christian Krause <chkr@fedoraproject.org> - 4.0.0-4
- Add %%{?dist} to Release tag

* Fri Nov 06 2009 Christian Krause <chkr@fedoraproject.org> - 4.0.0-3
- Don't own /usr/share/applications
- Fix permissions of man pages
- Use %%global instead of %%define

* Thu Nov 05 2009 Christian Krause <chkr@fedoraproject.org> - 4.0.0-2
- Require xorg-x11-fonts-misc package since xskat explicitly requires
  an 10x20 font

* Tue Nov 03 2009 Christian Krause <chkr@fedoraproject.org> - 4.0.0-1
- Initial version

