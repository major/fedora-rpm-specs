Name:           gpscorrelate
Version:        2.0
Release:        6%{?dist}
Summary:        A GPS photo correlation / geotagging tool

License:        GPLv2+
URL:            https://dfandrich.github.com/gpscorrelate/
Source0:        https://github.com/dfandrich/gpscorrelate/releases/download/%{version}/gpscorrelate-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  exiv2-devel libxml2-devel gtk3-devel
# For the .desktop file
BuildRequires:  desktop-file-utils
# For the manpage
BuildRequires:  libxslt docbook-style-xsl
BuildRequires: make
# For: %{_datadir}/icons/hicolor/scalable/apps/gpscorrelate-gui.svg
Requires: hicolor-icon-theme


%description
Gpscorrelate adds coordinates to the exif data of jpeg pictures based on a gpx
track file. The correlation is done by comparing the timestamp of the images
with the timestamp of the gps coordinates.


%prep
%setup -q


%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" OFLAGS="$RPM_OPT_FLAGS" docdir="%{_pkgdocdir}"


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT bindir=%{_bindir} mandir=%{_mandir} docdir="%{_pkgdocdir}"
make install-desktop-file DESTDIR=$RPM_BUILD_ROOT datadir=%{_datadir} 


%files
%doc %{_pkgdocdir}
%{_bindir}/%{name}
%{_bindir}/%{name}-gui
%{_datadir}/applications/gpscorrelate.desktop
%{_datadir}/icons/hicolor/scalable/apps/gpscorrelate-gui.svg
%{_mandir}/man1/gpscorrelate.1*


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Till Maas <opensource@till.name> - 2.0-1
- Update to new upstream with new release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Rex Dieter <rdieter@fedoraproject.org> - 1.6.1-26
- rebuild (exiv2)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.6.1-23
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 02 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.6.1-20
- rebuild (exiv2)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 24 2015 Rex Dieter <rdieter@fedoraproject.org> - 1.6.1-17
- rebuild (exiv2)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.6.1-15
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Dec 03 2013 Rex Dieter <rdieter@fedoraproject.org> - 1.6.1-12
- rebuild (exiv2)

* Tue Aug 06 2013 Till Maas <opensource@till.name> - 1.6.1-11
- Use %%{_pkgdocdir}

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 02 2012 Rex Dieter <rdieter@fedoraproject.org> - 1.6.1-7
- rebuild (exiv2)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 14 2011 Rex Dieter <rdieter@fedoraproject.org> - 1.6.1-5
- rebuild (exiv2)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 02 2011 Rex Dieter <rdieter@fedoraproject.org> - 1.6.1-3
- rebuild (exiv2)

* Mon May 31 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.6.1-2 
- rebuild (exiv2)

* Thu Feb 18 2010 Till Maas <opensource@till.name> - 1.6.1-1
- Update to new release, only change: our patches are included 
- use %%global instead of %%define
- remove upstreamed patches and icon

* Wed Feb 10 2010 Till Maas <opensource@till.name> - 1.6.0-6
- Fix DSOLinkChange breakage using g++ to link instead of adding -lstdc++.
  Thanks Ralf Corsepius for spotting this:
  http://lists.fedoraproject.org/pipermail/devel/2010-February/130631.html

* Wed Feb 10 2010 Till Maas <opensource@till.name> - 1.6.0-5
- Fix build failure due to https://fedoraproject.org/wiki/UnderstandingDSOLinkChange

* Mon Jan 04 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.6.0-4 
- rebuild (exiv2)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Apr 18 2009 Till Maas <opensource@till.name> - 1.6.0-2
- Move icon installation into Makefile to get upstreamable patch

* Sun Apr 12 2009 Till Maas <opensource@till.name> - 1.6.0-1
- Update to new upstream release
- Add svg icon using public domain cliparts by najsbajs and Anonymous from
  Open Clip Art Library

* Sun Feb 15 2009 Till Maas <opensource@till.name> - 1.5.8-2
- add RELEASES to %%doc

* Sat Nov 01 2008 Till Maas <opensource@till.name> - 1.5.8-1
- Update to new upstream version
- Remove upstreamed patches

* Thu Oct 30 2008 Till Maas <opensource@till.name> - 1.5.7-2
- add extended manpage based on manpage from debian
- fix help text (--no-write is useful with --verbose, not --show)

* Thu Oct 30 2008 Till Maas <opensource@till.name> - 1.5.7-1
- Update to new version, remove upstreamed patch
- add patch to remove some compiler warnings
- add patch to include desktop file install in makefile

* Wed Aug 13 2008 Till Maas <opensource@till.name> - 1.5.6-2
- add missing desktop file

* Sat Aug 02 2008 Till Maas <opensource@till.name> - 1.5.6-1
- initial version for Fedora
