%global commit ffbb2d559af42ddb38f315ce0f5f9f70204e1037
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20250123
%global _hardened_build 1

Name: odhcp6c
Version: 0
Release: 0.27.%{date}git%{shortcommit}%{?dist}
Summary: Embedded DHCPv6 and RA client
# License is GPLv2 except:
# ./src/md5.c: ISC
# ./src/md5.h: ISC
# Automatically converted from old format: GPLv2 and ISC - review is highly recommended.
License: GPL-2.0-only AND ISC
URL: https://git.openwrt.org/?p=project/odhcp6c.git
# Source fetched from git:
# git clone https://git.openwrt.org/project/odhcp6c.git
# cd odhcp6c
# git archive --format=tar.gz --prefix=odhcp6c-%%{commit}/ %%{commit} > ../odhcp6c-%%{commit}.tar.gz
Source0: %{name}-%{commit}.tar.gz
Source1: odhcp6c@.service
# https://github.com/openwrt/odhcp6c/pull/95
Patch: %{name}-0-Use-GNUInstallDirs-macros.patch
BuildRequires: cmake
BuildRequires: gcc
%if 0%{?rhel}
BuildRequires: systemd
%else
BuildRequires: systemd-rpm-macros
%endif

%description
odhcp6c is a minimal DHCPv6 and Router Advertisement client for use in embedded
Linux systems, especially routers. It compiles to only about 35 KB.

%prep
%autosetup -n %{name}-%{commit}

%build
%{cmake}
%{cmake_build}

%install
%{cmake_install}
install -D -p -m 0755 odhcp6c-example-script.sh %{buildroot}%{_sysconfdir}/odhcp6c/odhcp6c-example-script.sh
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/odhcp6c@.service

%files
%doc README
%license COPYING
%{_bindir}/odhcp6c
%dir %{_sysconfdir}/odhcp6c
%{_sysconfdir}/odhcp6c/odhcp6c-example-script.sh
%{_unitdir}/odhcp6c@.service

%changelog
* Wed Feb 05 2025 Juan Orti Alcaine <jortialc@redhat.com> - 0-0.27.20250123gitffbb2d5
- Improve patch to avoid hardcoded sbin dir

* Thu Jan 23 2025 Juan Orti Alcaine <jortialc@redhat.com> - 0-0.26.20250123gitffbb2d5
- Update to commit ffbb2d5
- Patch sbin dir hardcoded in cmake file (RHBZ#2340955)

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.25.20240116gitbcd2836
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 0-0.24.20240116gitbcd2836
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.23.20240116gitbcd2836
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.22.20240116gitbcd2836
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.21.20240116gitbcd2836
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Juan Orti Alcaine <jortialc@redhat.com> - 0-0.20.20240116gitbcd2836
- Update to commit bcd2836

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19.20230116git7d21e8d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18.20230116git7d21e8d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 16 2023 Juan Orti Alcaine <jortialc@redhat.com> - 0-0.17.20230116git7d21e8d
- Update to commit 7d21e8d

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.20220615git39b584b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Juan Orti Alcaine <jortialc@redhat.com> - 0-0.15.20220615git39b584b
- Update to commit 39b584b

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.20210605gite0d9a4b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.20210605gite0d9a4b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 05 2021 Juan Orti Alcaine <jortialc@redhat.com> - 0-0.12.20210605gite0d9a4b
- Update to commit e0d9a4b

* Wed Feb 24 2021 Juan Orti Alcaine <jortialc@redhat.com> - 0-0.11.20210224git53f07e9
- Update to commit 53f07e9

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.20201203gita7b2221
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 03 2020 Juan Orti Alcaine <jortialc@redhat.com> - 0-0.9.20201203gita7b2221
- Update to commit a7b2221

* Tue Aug 04 2020 Juan Orti Alcaine <jortialc@redhat.com> - 0-0.8.20200416gitf575351
- Use cmake_build and cmake_install macros. Fix RHBZ#1865137

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20200416gitf575351
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20200416gitf575351
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Juan Orti Alcaine <jortialc@redhat.com> - 0-0.5.20200416gitf575351
- Install preserving time stamps
- Own /etc/odhcp6c dir

* Tue Apr 21 2020 Juan Orti Alcaine <jortialc@redhat.com> - 0-0.4.20200416gitf575351
- Install in multi-user.target
- Update description

* Sat Apr 18 2020 Juan Orti Alcaine <jortialc@redhat.com> - 0-0.3.20200416gitf575351
- Harden service

* Sat Apr 18 2020 Juan Orti Alcaine <jortialc@redhat.com> - 0-0.2.20200416gitf575351
- Order service unit after network-pre.target
- Fix build in epel

* Thu Apr 16 2020 Juan Orti Alcaine <jortialc@redhat.com> - 0-0.1.20200416gitf575351
- Initial release
