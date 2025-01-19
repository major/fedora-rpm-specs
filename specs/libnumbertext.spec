Name:      libnumbertext
Version:   1.0.11
Release:   8%{?dist}
Summary:   Number to number name and money text conversion library

#The entire source code is dual license LGPLv3+ or BSD, except for
#the data files hr.sor, sr.sor and sh.sor which are dual license
#CC-BY-SA or LGPLv3+
License:   ( LGPL-3.0-or-later OR BSD-3-Clause ) AND ( LGPL-3.0-or-later OR CC-BY-SA-3.0 )
URL:       https://github.com/Numbertext/libnumbertext
Source:    https://github.com/Numbertext/libnumbertext/releases/download/%{version}/libnumbertext-%{version}.tar.xz

BuildRequires: autoconf, automake, libtool, gcc-c++
BuildRequires: make

%description
Language-neutral NUMBERTEXT and MONEYTEXT functions for LibreOffice Calc

%package devel
Requires: libnumbertext = %{version}-%{release}
Summary: Files for developing with libnumbertext

%description devel
Includes and definitions for developing with libnumbertext

%prep
%autosetup -p1

%build
autoreconf -v --install --force
%configure --disable-silent-rules --disable-static --disable-werror --with-pic
%make_build

%check
make check

%install
rm -rf $RPM_BUILD_ROOT
%make_install
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog NEWS THANKS
%license COPYING
%{_bindir}/spellout
%{_libdir}/*.so.*
%{_datadir}/libnumbertext

%files devel
%{_includedir}/libnumbertext
%{_libdir}/pkgconfig/libnumbertext.pc
%{_libdir}/*.so

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Feb 23 2023 Caolán McNamara <caolanm@redhat.com> - 1.0.11-3
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 13 2023 Caolán McNamara <caolanm@redhat.com> - 1.0.11-1
- latest version

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Apr 04 2022 Caolán McNamara <caolanm@redhat.com> - 1.0.10-1
- latest version

* Mon Apr 04 2022 Caolán McNamara <caolanm@redhat.com> - 1.0.9-1
- latest version

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 08 2020 Caolán McNamara <caolanm@redhat.com> - 1.0.6-1
- latest version

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Tom Stellard <tstellar@redhat.com> - 1.0.5-5
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 16 2018 Caolán McNamara <caolanm@redhat.com> - 1.0.5-1
- latest version

* Thu Aug 16 2018 Caolán McNamara <caolanm@redhat.com> - 1.0.3-1
- latest version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Caolán McNamara <caolanm@redhat.com> - 1.0.2-3
- fix changelog order
- remove clean section
- set COPYING as license
- use LT_INIT

* Mon Jun 11 2018 Caolán McNamara <caolanm@redhat.com> - 1.0.2-2
- clarify extra license option of the sh/sr/hr data files

* Mon Jun 11 2018 Caolán McNamara <caolanm@redhat.com> - 1.0.2-1
- initial version
