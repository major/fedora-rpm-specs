Name:           bygfoot
Version:        2.3.5
Release:        6%{?dist}
Summary:        Football management game
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://www.bygfoot.com
Source0:        https://gitlab.com/bygfoot/bygfoot/-/archive/%{version}/bygfoot-%{version}.tar.bz2
Source1:        bygfoot.desktop
Patch0:         bygfoot-c99-1.patch
Patch1:         bygfoot-c99-2.patch

BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  gtk2-devel gettext
BuildRequires:  ninja-build cmake
BuildRequires:  json-c-devel
Requires: bygfoot-data

%description
Bygfoot is a small and simple graphical football (a.k.a. soccer) manager game 
featuring many international leagues and cups. You manage a team from one such 
league: you form the team, buy and sell players, get promoted or relegated and
of course try to be successful.

%package data
Summary: bygfoot country definitions and other game files.
BuildArch:	noarch


%description data
bygfoot country definitions and other game files.

%prep
%autosetup -n %{name}-%{version} -p1

%build
#This package requires -fcommon to build.
%global _legacy_common_support 1

# This package does not ship any object files or static libraries, so we
# don't need -ffat-lto-objects.
%if %{defined _lto_cflags}
%global _lto_cflags %(echo %{_lto_cflags} | sed 's/-ffat-lto-objects//')
%endif

%cmake -G Ninja
%cmake_build

%install
%cmake_install
%find_lang %{name}
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README TODO UPDATE
%license COPYING
%{_bindir}/bygfoot*
%{_datadir}/applications/bygfoot.desktop

%files data
%{_datadir}/bygfoot

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.3.5-5
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Feb 08 2023 Tom Stellard <tom@stellard.net> - 2.3.5-1
- 2.3.5 Release

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 14 2022 Florian Weimer <fweimer@redhat.com> - 2.3.4-3
- Apply upstream patches to improve C99 compatibility

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 3 2022 Tom Stellard <tom@stellard.net> - 2.3.4-1
- 2.3.4 Release

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Sep 04 2020 Tom Stellard <tom@stellard.net> - 2.3.2-22
- Unretire package

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 2.3.2-8
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.3.2-4
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Feb 13 2010 Haïkel Guémar <karlthered@gmail.com> - 2.3.2-2
- Fixed DSO linking issue

* Tue Sep 29 2009 Haïkel Guémar <karlthered@gmail.com> - 2.3.2-1
- Updated to 2.3.2

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.2.0-3
- Autorebuild for GCC 4.3

* Fri Aug 24 2007 Michał Bentkowski <mr.ecik at gmail.com> - 2.2.0-2
- BuildID rebuild
- Fix License tag

* Mon Jun 11 2007 Michał Bentkowski <mr.ecik at gmail.com> - 2.2.0-1
- 2.2.0

* Fri May 18 2007 Michał Bentkowski <mr.ecik at gmail.com> - 2.1.1-1
- 2.1.1

* Thu Oct 12 2006 Michał Bentkowski <mr.ecik at gmail.com> - 2.0.1-1
- Bump release to 2.0.1

* Mon Sep 04 2006 Michał Bentkowski <mr.ecik at gmail.com> - 2.0.0-3
- FC6 rebuild

* Thu Aug 17 2006 Michał Bentkowski <mr.ecik at gmail.com> - 2.0.0-2
- Small fix in %%files section

* Tue Aug 15 2006 Michał Bentkowski <mr.ecik at gmail.com> - 2.0.0-1
- Initial release
