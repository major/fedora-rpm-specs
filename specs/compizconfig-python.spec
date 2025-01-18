%global  basever 0.8.18

Name:           compizconfig-python
Version:        0.8.18
Release:        16%{?dist}
Epoch:          1
Summary:        Python bindings for the Compiz Configuration System
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://gitlab.com/compiz/%{name}
Source0:        %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  libcompizconfig-devel >= %{basever}
BuildRequires:  glib2-devel
BuildRequires:  python3-devel
BuildRequires:  python3-Cython
BuildRequires:  libtool
BuildRequires:  automake
BuildRequires: make

Requires:       compiz >= %{basever}

%description
The Compiz Project brings 3D desktop visual effects that improve
usability of the X Window System and provide increased productivity
though plugins and themes contributed by the community giving a
rich desktop experience.

This package contains bindings to configure Compiz's
plugins and the composite window manager.

%prep
%setup -q -n %{name}-v%{version}

%build
export PYTHON=python3

./autogen.sh
%configure --disable-static

make %{?_smp_mflags} V=1

%install
%{make_install}
find %{buildroot} -type f -name "*.a" -o -name "*.la" | xargs rm -f


%files
%doc COPYING NEWS
%{python3_sitearch}/compizconfig.so
%exclude %{_libdir}/pkgconfig/compizconfig-python.pc


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1:0.8.18-15
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1:0.8.18-13
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1:0.8.18-9
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1:0.8.18-6
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1:0.8.18-3
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov  9 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 1:0.8.18-1
- New version
  Related: rhbz#1891137

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1:0.8.16-5
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1:0.8.16-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr  2 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 1:0.8.16-1
- New version
  Related: rhbz#1656467
- New URL

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1:0.8.14-6
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 1:0.8.14-2
- Rebuild due to bug in RPM (RHBZ #1468476)

* Thu Apr 20 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1:0.8.14-1
- update to 0.8.14 release
- remove ExcludeArch for s390 s390x, libdrm is available there
- switch to python3
- modernize spec file

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.12.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 17 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.12.1-3
- include ppc64 arch

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.8.12.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu May 12 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.12.1-1
- update to 0.8.12.1 release

* Sat Feb 13 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.12-1
- update to 0.8.12 release
- Set minimal Python required version to 2.7.x.
- Use Cython instead of Pyrex.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 06 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.9-1
- update to 0.8.9
- new upstream is at https://github.com/raveit65/compizconfig-python
- remove upstream patches
- use BuildRequires mate-common
- use modern make install macro
- add requires compiz base version

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.8.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 18 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.4-12
- rebuild for f22

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.8.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.8.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.8.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat May 25 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.4-8
- fix build for aarch64
- add requires autoconf, automake and libtool
- add autorefonf command
- fix automake-1.13 build deprecations

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.8.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 15 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.4-6
- build fedora
- remove python_sitelib stuff
- add filter setup
- add basever

* Sat Sep 29 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.8.4-5
- add Epoch tag
- fix source url

* Wed Sep 19 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.8.4-4
- improve spec file

* Tue May 15 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.8.4-3
- build for mate

* Sat Jul 31 2010 Leigh Scott <leigh123linux@googlemail.com> - 0.8.4-3
- rebuild for broken deps

