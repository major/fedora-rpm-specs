Name: systemd-swap
Summary: Creating hybrid swap space from zram swaps, swap files and swap partitions
Version: 3.3.0
Release: 17%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
URL: https://github.com/Nefelim4ag/%{name}
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Not schred swapfc file on ext4
Patch0: %{url}/commit/9f843c41a185b8972470e8ce828cadffea936b59.patch

BuildArch: noarch

BuildRequires: make
%if 0%{?fedora} >= 31
BuildRequires: systemd-rpm-macros
%else
BuildRequires: systemd-units
%endif
%{?systemd_requires}

BuildRequires: help2man

# support for zram
Requires: util-linux
Requires: kmod

# need Linux kernel version 2.6.37.1 or better to use zram
#Requires: kernel >= 2.6.37.1
Requires: kmod(zram.ko)

%description
Manage swap on:
    zswap - Enable/Configure
    zram - Autoconfigurating
    files - (sparse files for saving space, support btrfs)
    block devices - auto find and do swapon
It is configurable in /etc/systemd/swap.conf


%prep
%autosetup -n%{name}-%{version}
# preserve timestamps
sed -i -r 's:install -:\0p -:' Makefile

%build
# nothing

%install
%make_install PREFIX=%{buildroot}
pushd %{buildroot}
install -d .%{_unitdir}
find . -name '*.service' -print -exec mv '{}' .%{_unitdir} \;
install -d .%{_mandir}/man1
help2man -o .%{_mandir}/man1/%{name}.1 .%{_bindir}/%{name}


%post
%systemd_post mkzram.service

%preun
%systemd_preun mkzram.service

%postun
%systemd_postun_with_restart mkzram.service


%files
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/systemd/swap.conf
%{_unitdir}/*.service
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 3.3.0-16
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.3.0-8
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 14 2019 Raphael Groner <projects.rg@smart.ms> - 3.3.0-3
- fix some typos

* Wed Apr 10 2019 Raphael Groner <projects.rg@smart.ms> - 3.3.0-2
- fix hints from package review
- simplify dependencies
- use macros
- note real version in changelog
- generate manpage

* Tue Jul 11 2017 Raphael Groner <projects.rg@smart.ms> - 3.3.0-1
- initial
