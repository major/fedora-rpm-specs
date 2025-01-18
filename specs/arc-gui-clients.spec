Name:		arc-gui-clients
Version:	0.4.6
Release:	36%{?dist}
Summary:	ARC Graphical Clients

License:	Apache-2.0
URL:		http://sourceforge.net/projects/arc-gui-clients/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}-Source.tar.gz
#		Fixes for ARC version 4
Patch0:		%{name}-arc4.patch
#		Fixes for ARC version 5.1
Patch1:		%{name}-arc5.patch
#		Fix some compiler warnings
Patch2:		%{name}-warnings.patch
#		Fix a crash
Patch3:		%{name}-no-job-list-crash-fix.patch
#		Fixes for ARC version 6
Patch4:		%{name}-arc6.patch
#		Qt5 port
Patch5:		%{name}-qt5.patch

BuildRequires:	cmake
BuildRequires:	make
BuildRequires:	qt5-qtbase-devel
BuildRequires:	qt5-qtwebkit-devel
BuildRequires:	glibmm24-devel
BuildRequires:	nss-devel
BuildRequires:	nordugrid-arc-devel
BuildRequires:	desktop-file-utils

%description
Provides graphical clients to the NorduGrid ARC middleware.

%prep
%setup -q -n %{name}-%{version}-Source
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1

%build
%cmake
%make_build -C %{_vpath_builddir}

%install
%make_install -C %{_vpath_builddir}

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p %{buildroot}%{_datadir}/appdata
cat > %{buildroot}%{_datadir}/appdata/arcstat-ui.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<component type="desktop">
  <metadata_license>CC0-1.0</metadata_license>
  <id>arcstat-ui.desktop</id>
  <metadata>
    <value key="X-Merge-With-Parent">arcstorage-ui.desktop</value>
  </metadata>
</component>
EOF

desktop-file-validate %{buildroot}%{_datadir}/applications/arccert-ui.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/arcproxy-ui.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/arcstat-ui.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/arcstorage-ui.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/arcsub-ui.desktop

%files
%{_bindir}/arccert-ui
%{_bindir}/arcproxy-ui
%{_bindir}/arcstat-ui
%{_bindir}/arcstorage-ui
%{_bindir}/arcsub-ui
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/arccert-ui.desktop
%{_datadir}/applications/arcproxy-ui.desktop
%{_datadir}/applications/arcstat-ui.desktop
%{_datadir}/applications/arcstorage-ui.desktop
%{_datadir}/applications/arcsub-ui.desktop
%doc AUTHORS README
%license LICENSE

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 03 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.4.6-34
- Update License tags (SPDX)
- Eliminate use of obsolete patchN syntax

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 0.4.6-27
- Rebuilt with OpenSSL 3.0.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.4.6-23
- Adapt to new cmake rpm macro

* Fri Apr 10 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.4.6-22
- Change BR qt5-devel to qt5-qtbase-devel

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 12 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.4.6-19
- Port to Qt 5 (avoid using qt4-webkit)
- Adapt to ARC 6.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.4.6-17
- Add source directory to cmake command

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 25 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.4.6-15
- Fix a crash

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 11 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.4.6-13
- Fix EPEL 7 compilation
- Fix some compiler warnings

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jun 24 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.4.6-9
- Adapt to ARC 5.1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.4.6-6
- Rebuilt for GCC 5 C++11 ABI change

* Tue Mar 31 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.4.6-5
- Implement new license packaging guidelines

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.4.6-4
- Add an AppData file for the software center

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Nov 28 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.4.6-1
- Release 0.4.6

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 25 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.4.3-2
- Add missing BR qt4-webkit-devel

* Thu Apr 18 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.4.3-1
- Release 0.4.3

* Fri Nov 02 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.3.1-3
- Drop unnecessary scriptlets

* Fri Oct 19 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.3.1-2
- Drop obsolete buildroot removal and group tag

* Tue Sep 18 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.3.1-1
- Update to 0.3.1

* Wed Aug 22 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.3.0-1
- Update to 0.3.0

* Wed Jul 04 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.2.3-1
- Initial build
