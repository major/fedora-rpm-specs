%global nautilus_version 43~beta

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           nautilus-python
Version:        4.0.1
Release:        4%{?dist}
Summary:        Python bindings for Nautilus

License:        GPL-2.0-or-later
URL:            https://wiki.gnome.org/Projects/NautilusPython
Source0:        https://download.gnome.org/sources/%{name}/4.0/%{name}-%{tarball_version}.tar.xz

BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(libnautilus-extension-4) >= %{nautilus_version}
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  python3-devel

Requires:       nautilus-extensions%{?_isa} >= %{nautilus_version}
Requires:       python3-gobject-base%{?_isa}

%description
Python bindings for Nautilus


%package devel
Summary:        Python bindings for Nautilus
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Python bindings for Nautilus


%prep
%autosetup -p1 -n %{name}-%{tarball_version}


%build
%meson
%meson_build


%install
%meson_install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/nautilus-python/extensions
rm -rfv $RPM_BUILD_ROOT%{_docdir}


%files
%license COPYING
%doc AUTHORS NEWS.md README.md
%{_libdir}/nautilus/extensions-4/libnautilus-python.so
%dir %{_datadir}/nautilus-python/extensions

%files devel
%doc examples/
%{_datadir}/pkgconfig/nautilus-python.pc
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/nautilus-python/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 4.0.1-2
- Rebuilt for Python 3.13

* Fri Apr 19 2024 David King <amigadave@amigadave.com> - 4.0.1-1
- Update to 4.0.1

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 4.0-3
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 20 2022 Kalev Lember <klember@redhat.com> - 4.0-1
- Update to 4.0

* Fri Aug 12 2022 Kalev Lember <klember@redhat.com> - 4.0~alpha-1
- Update to 4.0.alpha
- Switch to meson build system
- Require nautilus-extensions rather than nautilus

* Mon Aug 01 2022 Kalev Lember <klember@redhat.com> - 1.2.3-13
- Fix the build with nautilus 43
- Drop python2 support from the spec file

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.2.3-11
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2.3-8
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.3-5
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.3-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 18 2019 Kalev Lember <klember@redhat.com> - 1.2.3-1
- Update to 1.2.3

* Mon Jun 10 2019 Charalampos Stratakis <cstratak@redhat.com> - 1.2.2-4
- Add Python 3.8 compatibility

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 07 2018 Kalev Lember <klember@redhat.com> - 1.2.2-2
- Add runtime requires on python2/python3-gobject

* Mon Nov 05 2018 Kalev Lember <klember@redhat.com> - 1.2.2-1
- Update to 1.2.2
- Rename the binary package back to nautilus-python (#1636626)
- Simplify packaging
- Co-own gtk-doc directories
- Update upstream URLs
- Built against Python 3 starting with F30

* Tue Oct 30 2018 Raphael Groner <projects.rg@smart.ms> - 1.2.1-4
- separate properly builds of python2 and python3, rhbz#1636626
- drop obsolete Group tag
- use name macro

* Wed Sep 12 2018 Raphael Groner <projects.rg@smart.ms> - 1.2.1-3
- use just python3 prefix for subpackage name
- because unknown how to procee with epel branches
- fix build with python3

* Fri Aug 31 2018 Raphael Groner <projects.rg@smart.ms> - 1.2.1-2
- add support for python3
- execute nautilus self tests with examples, currently b0rken due to a dbus bug

* Sat Jul 21 2018 Raphael Groner <projects.rg@smart.ms> - 1.2.1-1
- new version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.1-16
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sun Dec 17 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1-15
- Python 2 binary packages renamed to python2-nautilus and python2-nautilus-devel
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Raphael Groner <projects.rg@smart.ms> - 1.1-11
- adjust for epel7

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 04 2014 Till Maas <opensource@till.name> - 1.1-6
- Use %%{_pkgdocdir} (#1046899, #993991, #992325)
- Fix date in changelog

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 15 2012 Hicham HAOUARI <hicham.haouari@gmail.com> - 1.1-2
- BuildRequires pygobject3-devel instead of pygobject2-devel

* Wed Feb 08 2012 Hicham HAOUARI <hicham.haouari@gmail.com> - 1.1-1
- Update to 1.1

* Tue Sep 27 2011 Hicham HAOUARI <hicham.haouari@gmail.com> - 1.0-1
- Update to 1.0
- Remove BuildRoot tag and %%clean section
- Own /usr/share/nautilus-python/extensions instead of the old arch
  dependent locations

* Sat Feb 12 2011 Tim Lauridsen <timlau@fedoraproject.org> - 0.7.0-4
- Make it build with latest nautilus

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 26 2010 David Malcolm <dmalcolm@redhat.com> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 25 2010 Patrick Dignan <patrick.dignan at, gmail.com>
- New upstream version 0.7.0
                                                      
* Sun Jul 25 2010 Patrick Dignan <patrick.dignan at, gmail.com>
- Rebuild for F14

* Thu Jan 28 2010 Patrick Dignan <patrick.dignan at, gmail.com>
- New upstream release, bugfixes

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 19 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.5.1-3
- Patch to fix build (thanks to Nicholas Wourms)

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.5.1-2
- Rebuild for Python 2.6

* Wed Sep 24 2008 Trond Danielsen <trondd@fedoraproject.org> - 0.5.1-1
- New upstream version

* Mon Aug 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.4.3-6
- fix license tag

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.4.3-5
- Autorebuild for GCC 4.3

* Wed May 02 2007 Trond Danielsen <trond.danielsen@gmail.com> - 0.4.3-4
- Added missing folder. Fixes bug #238591.

* Sat Apr 21 2007 Trond Danielsen <trond.danielsen@gmail.com> - 0.4.3-3
- Moved example code to devel package.

* Thu Apr 19 2007 Jef Spaleta <jspaleta@gmail.com> - 0.4.3-2
- Package review corrections

* Wed Apr 04 2007 Trond Danielsen <trond.danielsen@gmail.com> - 0.4.3-1
- Initial version
