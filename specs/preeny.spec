Name:             preeny
URL:              https://github.com/zardus/preeny
Version:          0.1
Release:          24%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:          LicenseRef-Callaway-BSD
BuildRequires:    coreutils
BuildRequires:    make
BuildRequires:    gcc
BuildRequires:    libini_config-devel
Summary:          Some helpful preload libraries for pwning stuff
Source0:          https://github.com/zardus/preeny/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# https://github.com/zardus/preeny/commit/bc048654b9c4c417a3ff8c27e986edee3e07ebef
Patch:            preeny-0.1-warning-fix.patch
# https://github.com/zardus/preeny/pull/89
Patch:            preeny-0.1-libini_config-api-convert.patch

%description
Preeny helps you pwn noobs by making it easier to interact with services
locally. It disables fork(), rand(), and alarm() and, if you want, can convert
a server application to a console one using clever/hackish tricks, and can
even patch binaries.

%prep
%autosetup -p1

%build
%{set_build_flags}
%{make_build}

%install
cd src
# workaround for RHEL-7, "install -pDt" doesn't seem to work
mkdir -p %{buildroot}%{_libdir}/%{name}
install -pt %{buildroot}%{_libdir}/%{name} *.so

%files
%license LICENSE
%doc README.md
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.so

%changelog
* Thu Mar 05 2026 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1-24
- Switched to new libini_config API
- Minor spec cleanup

* Wed Jan 21 2026 Kevin Fenzi <kevin@scrye.com> - 0.1-23
- Rebuild due to buildsystem issue

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1-19
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 14 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1-3
- Added workaround for RHEL-7

* Tue Aug  8 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1-2
- Various fixes according to review

* Mon Aug  7 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1-1
- Initial version
