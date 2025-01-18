# first two digits of version
%global release_version %%(echo %{version} | awk -F. '{print $1"."$2}')

Name:           gnome-nettool
Version:        3.8.1
Release:        32%{?dist}
Summary:        Network information tool for GNOME

# Automatically converted from old format: GPLv2+ and GFDL - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-GFDL
URL:            https://gitlab.gnome.org/GNOME/gnome-nettool
Source0:        https://download.gnome.org/sources/gnome-nettool/%{release_version}/gnome-nettool-%{version}.tar.xz

# Backported from upstream
# https://gitlab.gnome.org/GNOME/gnome-nettool/merge_requests/2
Patch0:         fix-scalable-icon.patch

BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  libgtop2-devel
BuildRequires: make

Requires:       bind-utils
Requires:       coreutils
Requires:       iputils
Requires:       net-tools
Requires:       nmap
Requires:       traceroute
Requires:       whois

%description
GNOME Nettool is a front-end to various networking command-line
tools, like ping, netstat, ifconfig, whois, traceroute, finger.


%prep
%autosetup -p1


%build
%configure --disable-compile-warnings
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

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
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
BugReportURL: https://bugzilla.gnome.org/show_bug.cgi?id=736831
SentUpstream: 2014-09-17
-->
<application>
  <id type="desktop">gnome-nettool.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Perform advanced networking analysis</summary>
  <description>
    <p>
      Network Tools is a utility to perform advanced networking analysis
      operations.
      It features a range of networking tools that are typically done on
      the command line, but allows you to perform them with a graphical
      interface.
      With Network Tools, you can perform the following: ping, netstat,
      traceroute, port scans, lookup, finger and whois.
    </p>
  </description>
  <url type="homepage">http://projects.gnome.org/gnome-network/</url>
  <screenshots>
    <screenshot type="default">https://projects.gnome.org/gnome-network/screenshots/info_info.jpg</screenshot>
    <screenshot>https://projects.gnome.org/gnome-network/screenshots/info_netstat.jpg</screenshot>
    <screenshot>https://projects.gnome.org/gnome-network/screenshots/info_lookup.jpg</screenshot>
  </screenshots>
</application>
EOF

%find_lang gnome-nettool --with-gnome


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/gnome-nettool.desktop



%files -f gnome-nettool.lang
%doc AUTHORS COPYING NEWS README
%{_bindir}/gnome-nettool
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/gnome-nettool.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-nettool.gschema.xml
%{_datadir}/gnome-nettool/
%{_datadir}/icons/hicolor/*/apps/gnome-nettool.png
%{_datadir}/icons/hicolor/scalable/apps/gnome-nettool.svg


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 3.8.1-31
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-21
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 20 2020 Kalev Lember <klember@redhat.com> - 3.8.1-19
- Backport a patch to fix scalable icon (#1829838)
- Update upstream URLs (#1836677)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.8.1-13
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Kalev Lember <klember@redhat.com> - 3.8.1-10
- Rebuilt for libgtop2 soname bump

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 3.8.1-6
- Add an AppData file for the software center

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 01 2014 Kalev Lember <kalevlember@gmail.com> - 3.8.1-3
- Rebuilt for libgtop2 soname bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 02 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.1-1
- Update to 3.8.1

* Thu May 02 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 20 2012 Kalev Lember <kalevlember@gmail.com> - 3.2.0-3
- Depend on package names instead of executables

* Wed Apr 18 2012 Kalev Lember <kalevlember@gmail.com> - 3.2.0-2
- Use %%global instead of %%define (#812674)

* Fri Apr 13 2012 Kalev Lember <kalevlember@gmail.com> - 3.2.0-1
- Update to 3.2.0, spec file clean up for re-review (#812674)

* Fri Feb 11 2011 Matthias Clasen <mclasen@redhat.com> 2.91.5-4
- Rebuild gainst newer gtk

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.91.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.5-2
- Rebuild against newer gtk

* Tue Jan 11 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.5-1
- Update to 2.91.5

* Sun Jan  9 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.2-2
- Rebuild against newer gtk3

* Fri Nov 12 2010 Matthias Clasen <mclasen@redhat.com> - 2.91.2-1
- Update to 2.91.2

* Thu Aug 30 2010 Matthias Clasen <mclasen@redhat.com> - 2.32.0-1
- Update to 2.32.0

* Thu Aug 19 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.6-1
- Update to 2.31.6

* Fri Dec  4 2009 Matthias Clasen <mclasen@redhat.com> - 2.28.0-1
- Update to 2.28.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 17 2009 Matthias Clasen <mclasen@redhat.com> - 2.26.0-1
- Update to 2.26.0

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 17 2008 Matthias Clasen <mclasen@redhat.com> - 2.25.3-2
- Update to 2.25.3

* Sun Nov 23 2008 Matthias Clasen <mclasen@redhat.com> - 2.22.1-3
- Tweak description

* Tue Sep 23 2008 Matthias Clasen <mclasen@redhat.com> - 2.22.1-2
- Update to 2.22.1

* Thu May 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.22.0-2
- fix license tag

* Tue Mar 11 2008 Matthias Clasen <mclasen@redhat.com> - 2.22.0-1
- Update to 2.22.0

* Mon Feb 18 2008 Christopher Aillon <caillon@redhat.com> - 2.20.0-3
- Rebuild to celebrate my birthday (and GCC 4.3)

* Thu Oct 11 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0-2
- Rebuild

* Tue Sep 18 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0-1
- Update to 2.20.0

* Fri Aug 24 2007 Adam Jackson <ajax@redhat.com> - 2.19.90-2
- Rebuild for build ID

* Mon Aug 13 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.90-1
- Update to 2.19.90

* Tue Mar 13 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.0-1
- Update to 2.18.0

* Wed Dec 19 2006 Matthias Clasen <mclasen@redhat.com> - 2.17.4-1
- Update to 2.17.4

* Tue Sep  5 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.0-1.fc6
- Update to 2.16.0

* Mon Aug 21 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.92-1.fc6
- Update to 2.15.92

* Sat Aug 12 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.91-1.fc6
- Update to 2.15.91

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.15.0-1.1
- rebuild

* Fri Jun  9 2006 Matthias Clasen <mclasen@redhat.com> 2.15.0-1
- Update to 2.15.0

* Fri Jun  9 2006 Matthias Clasen <mclasen@redhat.com> 2.13.90-4
- Add missing BuildRequires

* Tue Jun  6 2006 Matthias Clasen <mclasen@redhat.com> 2.13.90-3
- Add BuildRequires for perl-XML-Parser

* Wed Mar 01 2006 Karsten Hopp <karsten@redhat.de> 2.13.90-2
- BuildRequires: desktop-file-utils for desktop-file-install

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.13.90-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.13.90-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Jan 30 2006 Matthias Clasen <mclasen@redhat.com>
- Update to 2.13.90

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Mar 17 2005 Ray Strode <rstrode@redhat.com> - 1.2.0-1
- Update to upstream version 1.2.0

* Wed Mar  2 2005 Mark McLoughlin <markmc@redhat.com> 0.99.3-3
- Rebuild with gcc4

* Tue Sep 21 2004 Mark McLoughlin <markmc@redhat.com> 0.99.3-2
- Move to the System Tools menu from the Internet menu - bug #131619

* Tue Aug 31 2004 Mark McLoughlin <markmc@redhat.com> 0.99.3-1
- Update to 0.99.3

* Fri Aug 27 2004 Mark McLoughlin <markmc@redhat.com> 0.99.2-1
- Initial build
