Name: sqm-scripts
Version: 1.6.0
Release: 5%{?dist}
Summary: Traffic shaper scripts for Smart Queue Management
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL: https://www.bufferbloat.net/projects/cerowrt/wiki/Smart_Queue_Management/
Source0: https://github.com/tohojo/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# Workaround for network-manager bug: https://github.com/tohojo/sqm-scripts/pull/129
Patch0: %{name}-1.4.0-run_service_after_network.patch
BuildArch: noarch
BuildRequires: make
%if 0%{?rhel}
BuildRequires: systemd
%else
BuildRequires: systemd-rpm-macros
%endif

%description
"Smart Queue Management", or "SQM" is shorthand for an integrated network
system that performs better per-packet/per flow network scheduling, active
queue length management (AQM), traffic shaping/rate limiting, and QoS
(prioritization).

%prep
%autosetup -p1

%build
%{make_build}

%install
%{make_install} UNIT_DIR=%{?buildroot}%{_unitdir}

%files
%doc README.md
%dir %{_sysconfdir}/sqm
%{_sysconfdir}/sqm/default.conf
%config(noreplace) %{_sysconfdir}/sqm/sqm.conf
%{_bindir}/sqm
%{_prefix}/lib/sqm
%{_unitdir}/sqm@.service
%{_tmpfilesdir}/sqm.conf

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.6.0-4
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 24 2023 Toke Høiland-Jørgensen <toke@redhat.com> - 1.6.0-1
- Bump to upstream 1.6.0 (RHBZ#2233870)

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Sep 24 2022 Juan Orti Alcaine <jortialc@redhat.com> - 1.5.2-1
- Version 1.5.2 (RHBZ#2121140)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 18 2021 Toke Høiland-Jørgensen <toke@redhat.com> - 1.5.1-1
- Bump to upstream 1.5.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 08 2021 Toke Høiland-Jørgensen <toke@redhat.com> - 1.5.0-1
- Bump to upstream 1.5.0
- Set UNIT_DIR on 'make install'

* Tue Dec 08 2020 Juan Orti Alcaine <jortialc@redhat.com> - 1.4.0-3
- Start service after network-online.target

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 23 2020 Juan Orti Alcaine <jortialc@redhat.com> - 1.4.0-1
- Initial release
