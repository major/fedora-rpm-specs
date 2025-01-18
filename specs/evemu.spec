%if 0%{?rhel} && 0%{?rhel} < 8
%bcond_without legacy_python
%endif

#global gitdate 20150818
#global gitversion eba96a4

Name:           evemu
Version:        2.7.0
Release:        32%{?gitdate:.%{gitdate}git%{gitversion}}%{?dist}
Summary:        Event Device Query and Emulation Program

License:        GPL-3.0-only AND LGPL-3.0-only AND GPL-3.0-or-later
URL:            http://www.freedesktop.org/wiki/Evemu

%if 0%{?gitdate}
Source0:        %{name}-%{gitdate}.tar.bz2
Source1:        make-git-snapshot.sh
Source2:        commitid
%else
Source0:        http://www.freedesktop.org/software/%{name}/%{name}-%{version}.tar.xz
%endif

BuildRequires:  automake libtool gcc gcc-c++ make
%if %{with legacy_python}
BuildRequires:  python2-devel
%else
BuildRequires:  python3-devel
%endif
BuildRequires:  xmlto asciidoc
BuildRequires:  libevdev-devel >= 1.3
Requires:       libevdev >= 0.5
Requires:       %{name}-libs = %{version}-%{release}

%description
%{name} is a simple utility to capture the event stream from input devices
and replay that stream on a virtual input device.

%package libs
Summary:        Event Device Query and Emulation Program Library
License:        LGPL-3.0-or-later
Conflicts:      evemu < 2.7.0-8

%description libs
%{name} base library, used by the evemu tools.

%package devel
Summary:        Event Device Query and Emulation Program Development Package
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description devel
%{name} development files.

%prep
%setup -q -n %{name}-%{?gitdate:%{gitdate}}%{!?gitdate:%{version}}

%build
autoreconf -v --install --force || exit 1
%if %{with legacy_python}
export PYTHON=python2
%else
export PYTHON=python3
%endif
%configure --disable-static --disable-silent-rules
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# We intentionally don't ship *.la files
rm -f %{buildroot}%{_libdir}/*.la

%ldconfig_scriptlets

%files
%license COPYING
%{_bindir}/evemu-describe
%{_bindir}/evemu-device
%{_bindir}/evemu-play
%{_bindir}/evemu-event
%{_bindir}/evemu-record
%{_mandir}/man1/evemu-*

%files libs
%{_libdir}/libevemu.so.*

%files devel
%{_includedir}/evemu.h
%{_libdir}/libevemu.so
%{_libdir}/pkgconfig/evemu.pc
%if %{with legacy_python}
%{python2_sitelib}/evemu
%else
%{python3_sitelib}/evemu
%endif

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Miroslav Suchý <msuchy@redhat.com> - 2.7.0-30
- convert license to SPDX

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.7.0-29
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Sep 08 2023 Peter Hutterer <peter.hutterer@redhat.com> - 2.7.0-26
- SPDX migration

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 2.7.0-24
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.7.0-21
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.7.0-18
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 01 2020 Peter Hutterer <peter.hutterer@redhat.com> 2.7.0-16
- Add make to BuildRequires

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.7.0-14
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.7.0-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.7.0-11
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 16 2018 Peter Hutterer <peter.hutterer@redhat.com> 2.7.0-8
- Split the lib into its own subpackage, it's LGPLv3+
- remove utouch-evemu Obsoletes line, it's been over 5 years

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.7.0-6
- Rebuilt for Python 3.7

* Fri Mar 30 2018 Carl George <carl@george.computer> - 2.7.0-5
- Build with python3 on Fedora
- Fix license handling
- Use %%ldconfig_scriptlets macro

* Thu Mar 08 2018 Peter Hutterer <peter.hutterer@redhat.com> 2.7.0-4
- Add BuildRequires for gcc-c++, needed for a test build

* Mon Feb 19 2018 Peter Hutterer <peter.hutterer@redhat.com> 2.7.0-3
- Add BuildRequires for gcc

* Tue Feb 06 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.7.0-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Mon Sep 25 2017 Benjamin Tissoires <benjamin.tissoires@redhat.com> 2.7.0-1
- Evemu 2.7.0

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 03 2017 Peter Hutterer <peter.hutterer@redhat.com> 2.6.0-1
- evemu 2.6.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep 16 2016 Benjamin Tissoires <benjamin.tissoires@redhat.com> 2.5.0-1
- Evemu v2.5.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Apr 04 2016 Benjamin Tissoires <benjamin.tissoires@redhat.com> 2.4.0-1
- Evemu v2.4.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 14 2015 Benjamin Tissoires <benjamin.tissoires@redhat.com> 2.3.1-1
- Evemu v2.3.1

* Tue Aug 18 2015 Benjamin Tissoires <benjamin.tissoires@redhat.com> 2.2.0-2.20150818giteba96a4
- git snapshot to fix rhbz #1251015

* Tue Aug 04 2015 Benjamin Tissoires <benjamin.tissoires@redhat.com> 2.2.0-1
- Evemu v2.2.0

* Wed Jul 22 2015 Benjamin Tissoires <benjamin.tissoires@redhat.com> 2.1.0-4.20150722git79b29f0
- Update to current git master: add dmi info and EV_SW and EV_LED states

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Benjamin Tissoires <benjamin.tissoires@redhat.com> 2.1.0-2
- Apply 2 upstream patches: handle holes in the input node list,
  add uname to the header comment

* Wed Nov 12 2014 Peter Hutterer <peter.hutterer@redhat.com> 2.1.0-1
- Update to version 2.1.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 19 2014 Benjamin Tissoires <benjamin.tissoires@redhat.com> 2.0.0-1
- Update to version 2.0.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.99.0-4.20140324gitaf60032
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 23 2014 Peter Hutterer <peter.hutterer@redhat.com> - 1.99.0-3.20140324gitaf60032
- Update to current git, stray debugging output lead to invalid traces

* Mon Feb 10 2014 Peter Hutterer <peter.hutterer@redhat.com> - 1.99.0-2.20131213gitb8f3f57
- Rebuild for libevdev soname bump

* Fri Dec 13 2013 Benjamin Tissoires <benjamin.tissoires@redhat.com> 1.99.0-1.20131213gitb8f3f57
- Update to current git, before 2.0 is released
- fixes #1037056 (evemu FTBFS if "-Werror=format-security" flag is used)
- use libevdev backend (libevdev >= 0.5 is required)

* Thu Nov 21 2013 Benjamin Tissoires <benjamin.tissoires@redhat.com> 1.2.0-0
- Update to version 1.2.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-5.20130724git304eb65f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Benjamin Tissoires <benjamin.tissoires@redhat.com> 1.1.0-4.20130724git304eb65f
- Update to current git, record the resolution and bump the file format to 1.2

* Wed Jul 10 2013 Peter Hutterer <peter.hutterer@redhat.com> - 1.1.0-3.20130708gitf2eb0f2cd
- disable silent rules

* Mon Jul 08 2013 Peter Hutterer <peter.hutterer@redhat.com> - 1.1.0-2.20130708gitf2eb0f2cd
- Update to current git, avoids printing unused bits

* Thu May 23 2013 Peter Hutterer <peter.hutterer@redhat.com>
- Drop unused patch

* Fri May 03 2013 Benjamin Tissoires <benjamin.tissoires@redhat.com> 1.1.0-1
- Update to version 1.1.0, hosted now on freedesktop

* Thu Jan 31 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.0.10-3
- fclose output only once

* Tue Jan 08 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.0.10-2
- Test for device grab in evemu-record

* Fri Jul 06 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.0.10-1
- Update to version 1.0.10, rename. upstream changed name to "evemu" with
  this version

* Thu Feb 09 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.0.8-2
- autoreconf --force to stop weird libtool build errors

* Tue Feb 07 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.0.8-1
- Initial package
