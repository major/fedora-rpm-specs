# Without this, some documentation files end up in /usr/share/doc/python3-caja.
# They should all go in /usr/share/doc/python-caja.
%global _docdir_fmt %{name}

%global _description\
Python bindings for Caja

%define shortver        %(cut -d. -f1,2 <<< '%{version}')

Name:          python-caja
Version:       1.26.0
Release:       14%{?dist}
Epoch:         1
Summary:       Python bindings for Caja

# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:           http://mate-desktop.org
Source0:       http://pub.mate-desktop.org/releases/%{shortver}/%{name}-%{version}.tar.xz
Patch1:        python-caja-1.26-python313.patch

BuildRequires: python3-devel
BuildRequires: caja-devel
BuildRequires: pkgconfig(pygobject-3.0)
BuildRequires: make
BuildRequires: mate-common


%description
%_description

%package -n python3-caja
Summary:        %summary
%{?python_provide:%python_provide python3-caja}

%description -n python3-caja
%_description

%package devel
Summary:        Python bindings for Caja
Requires:       python3-caja%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
%_description


%prep
%autosetup -p1

%build
export PYTHON=python3

%configure \
     --disable-static

make %{?_smp_mflags}


%install
%{make_install}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/caja-python/extensions
find $RPM_BUILD_ROOT -name '*.la' -delete

# We use %%doc instead
rm $RPM_BUILD_ROOT%{_docdir}/python-caja/README

%find_lang %{name} --with-gnome --all-name


%files -n python3-caja -f %{name}.lang
%license COPYING
%doc README AUTHORS NEWS
%{_libdir}/caja/extensions-2.0/libcaja-python.so
%{_datadir}/caja/extensions/libcaja-python.caja-extension
%dir %{_datadir}/caja-python
%dir %{_datadir}/caja-python/extensions
%{_docdir}/python-caja/examples/

%files devel
%{_libdir}/pkgconfig/caja-python.pc


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.26.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep  4 2024 Miroslav Suchý <msuchy@redhat.com> - 1:1.26.0-13
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.26.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Python Maint <python-maint@redhat.com> - 1:1.26.0-11
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.26.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.26.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Nov  2 2023 Patrick Monnerat <patrick@monnerat.net> 1:1.26.0-8
- Patch "python313" for Python 3.13 compatibility.
  https://bugzilla.redhat.com/show_bug.cgi?id=2247264

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.26.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 1:1.26.0-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.26.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.26.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1:1.26.0-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Aug 07 2021 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.0-1
- update to 1.26.0 release

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.24.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1:1.24.0-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.24.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 19 2020 Patrick Monnerat <patrick@monnerat.net> 1:1.24.0-4
- Run autogen.sh to refresh automake macros.
  https://bugzilla.redhat.com/show_bug.cgi?id=1899132

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1:1.24.0-2
- Rebuilt for Python 3.9

* Tue Feb 11 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.24.0-1
- update to 1.24.0

* Mon Feb 03 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.23.1-1
- update to 1.23.1

* Wed Jan 29 2020 Patrick Monnerat <patrick@monnerat.net> 1.23.0-4
- Use commons even with gcc 10.
  https://bugzilla.redhat.com/show_bug.cgi?id=1795940

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1:1.23.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.23.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 2019 Patrick Monnerat <patrick@monnerat.net> 1.23.0-1
- New upstream release.

* Mon Mar 04 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.22.0-1
- update to 1.22.0

* Fri Feb 01 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1:1.20.2-2
- add upstream python2/3 support improvements from master branch

* Wed Dec 26 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1:1.20.2-1
- update to 1.20.2 release

* Thu Aug 16 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1:1.20.1-3
- Switch to Python 3
- Move COPYING to /usr/share/licenses
- drop obsolete rpm scriptlets

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1:1.20.1-1
- update to 1.20.1 release

* Sun Feb 11 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1:1.20.0-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sun Feb 11 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.20.0-1
- update to 1.20.0 release
- switch to using autosetup

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.19.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Oct 13 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1.19.0-1
- update to 1.19.0 release

* Thu Aug 10 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1:1.18.1-4
- Python 2 binary package renamed to python2-caja
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.18.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Mon Jul 31 2017 Florian Weimer <fweimer@redhat.com> - 1:1.18.1-2
- Rebuild with binutils fix for ppc64le (#1475636)

* Wed Jul 26 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1.18.1-1
- update to 1.18.1

* Tue Mar 14 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1.18.0-1
- update to 1.18.0 release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 06 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.17.0-1
- test 1.17.0 release

* Thu Sep 22 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.16.0-1
- update to 1.16.0 release

* Mon Jun 13 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.15.0-1
- update to 1.15.0 release

* Thu Apr 07 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.14.0-1
- update to 1.14.0

* Sun Feb 07 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.13.0-1
- update to 1.13.0 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 06 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.12.0-1
- update to 1.12.0 release

* Sat Sep 12 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:1.10.0-1
- update to 1.10.0 release
- remove patches
- remove conditions for caja

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Apr 05 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:1.4.0-6
- use and own %%{_libdir}/caja/extensions-2.0/python
- fix rhbz (#1082693)

* Sun Mar 16 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:1.4.0-5
- create and own /usr/lib/caja/extensions-2.0/python/ directory

* Wed Dec 18 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:1.4.0-4
- rebuild for caja rename in f21
- add python2 stacks

* Mon Sep 23 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:1.4.0-3
- own directories

* Fri Sep 06 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:1.4.0-2
- initial build for fedora
- use modern make install macro
- add epoch tag to obsolete python-caja from external repo
- add upstream patches to fix incorrect-FSF-address
- add upstream patch for automake-1.13
- add LGPLv2+ to license information

* Thu May 30 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.4.0-1
- build for f19
- add python-caja_removal_of_mate-python_usage.patch

* Tue Apr 10 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.2.0-1
- rename package to python-caja

* Wed Mar 14 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.2.0-1
- update to 1.2.0 version

* Mon Feb 13 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - caja-python-1.1.0-2
- rebuild for enable builds for .i686

* Sat Jan 21 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.1.0-1
- update to version 1.1.0

* Wed Jan 04 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 2011.12.01-1
- caja-python.spec based on nautilus-python-1.0-1.fc16 spec
