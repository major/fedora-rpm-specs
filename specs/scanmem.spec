%global __python %{__python3}

Name:           scanmem
Summary:        Memory scanner
Version:        0.17
Release:        19%{?dist}.1
# Automatically converted from old format: GPLv3+ and LGPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
VCS:            https://github.com/scanmem/scanmem.git
URL:            https://github.com/scanmem/scanmem
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  readline-devel
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# Remove after F29
Obsoletes:      %{name} < 0.17

%description
scanmem is a simple interactive debugging utility, used to locate the address
of a variable in an executing process. This can be used for the analysis or
modification of a hostile process on a compromised machine, reverse
engineering, or as a "pokefinder" to cheat at video games.

%package libs
Summary:        Memory scanner library
# Remove after F29
Obsoletes:      %{name} < 0.17

%description libs
%{summary}.

%package devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
%{summary}.

%package -n gameconqueror
Summary:        CheatEngline-alike interface for scanmem
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       polkit
Requires:       python3-gobject-base
Requires:       gtk3
BuildRequires:  python3-devel
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  %{_bindir}/appstream-util

%description -n gameconqueror
GameConqueror is a GUI front-end for scanmem, providing more features, such as:
* Flexible syntax for searching
* Easier and multiple variable locking
* Better process finder
* Memory browser/editor

%prep
%autosetup
sed -i -e "1s|.*|#!%{__python3}|" gui/GameConqueror.py

%build
./autogen.sh
%configure --enable-gui --disable-static
%make_build

%install
%make_install
# No libtool, please
rm -vf %{buildroot}%{_libdir}/lib%{name}.la
# We install docs ourselves
rm -vrf %{buildroot}%{_datadir}/doc/%{name}/
# No need to do bytecode compilation for us
find %{buildroot}%{_datadir}/gameconqueror/ -type f -name '*.py[co]' -print -delete
%find_lang GameConqueror

%py_byte_compile %{__python3} %{buildroot}%{_datadir}/gameconqueror

%check
make check
desktop-file-validate %{buildroot}%{_datadir}/applications/GameConqueror.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/GameConqueror.appdata.xml

%files
%doc README
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}

%files libs
%license gpl-3.0.txt lgpl-3.0.txt
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so

%files -n gameconqueror -f GameConqueror.lang
%{_datadir}/applications/GameConqueror.desktop
%{_mandir}/man1/gameconqueror.1*
%{_datadir}/gameconqueror/
%{_datadir}/icons/hicolor/*/apps/GameConqueror.png
%{_bindir}/gameconqueror
%{_datadir}/polkit-1/actions/org.freedesktop.gameconqueror.policy
%{_datadir}/appdata/GameConqueror.appdata.xml

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-19.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 0.17-18.1
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-17.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-16.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-15.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-14.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-13.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-12.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-11.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-10.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-9.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-8.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-7.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.17-6.1
- Rebuild for readline 8.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.17-3.1
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.17-1.1
- Remove obsolete scriptlets

* Fri Oct 20 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.17-1
- Update to 0.17

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 08 2017 Igor Gnatenko <ignatenko@rehdat.com> - 0.16.1-1
- Update to 0.16.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.16-2
- Rebuild for readline 7.x

* Tue Dec 20 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.16-1
- Update to 0.16 (RHBZ #1406381)

* Wed Jun 01 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.15.8-1
- Update to 0.15.8 (RHBZ #1341438)

* Wed Apr 27 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.15.7-1
- Update to 0.15.7 (RHBZ #1330792)

* Mon Mar 14 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.15.6-1
- Update to 0.15.6 (RHBZ #1315294)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 29 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.15.4-1
- 0.15.4

* Wed Oct 14 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.15.3-1
- 0.15.3 (RHBZ #1271427)

* Tue Jun 23 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.15.2-1
- 0.15.2 (RHBZ #1235031)
- Use modern RPM macroses

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-7.de2653d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-5.de2653d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 02 2014 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.14-4.de2653d
- Typo fix in files section

* Fri May 02 2014 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.14-3.de2653d
- Update to latest master
- Include appdata

* Sun Dec 08 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.14-2.0bff2a6
- Russian translate
- Fix some crashes (alike RHBZ #1039313)
- spec: some fixes

* Sun Dec 01 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.14-1.3e65b13
- Git fixes + improve pkexec

* Wed Sep  4 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.13-7
- Add patch as downstream for fix shell command crash

* Wed Sep  4 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.13-6
- Update icon fix (in app icons will present)

* Fri Aug 23 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.13-5
- spec: Fix icons path and add scriptlets for gen icon-cache
- spec: some fixes

* Tue Aug 20 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.13-4
- Force removing unversioned doc dir

* Tue Aug 20 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.13-3
- Remove Application category in Desktop-file (deprecated)

* Tue Aug 20 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.13-2
- spec: some fixes

* Tue Aug 20 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.13-1
- Update to 0.13
- Add new sub-package gameconqueror (gui interface for scanmem)
- Drop unneeded tags and sections
- Few fixes in spec

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 27 2007 Jakub Hrozek <jhrozek@redhat.com> 0.07-3
- Rebuild for GCC 4.3

* Thu Dec 27 2007 Jakub Hrozek <jhrozek@redhat.com> 0.07-2
- Refactored spec to match Fedora packaging guidelines

* Tue Jun 05 2007 Dag Wieers <dag@wieers.com> - 0.07-1 - 5269+/dag
- Updated to release 0.07.

* Sun Apr 15 2007 Dag Wieers <dag@wieers.com> - 0.06-1
- Updated to release 0.06.

* Sun Mar 04 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Updated to release 0.05.

* Tue Jan 30 2007 Dag Wieers <dag@wieers.com> - 0.04-1
- Initial package. (using DAR)
