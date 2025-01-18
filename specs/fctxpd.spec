
%global commit          c4dba7f21f8549b3cdd844b05613bb7ca1135619
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global snapshotdate    20210326

Name:   fctxpd
Version:        0.2
Release:        14.%{snapshotdate}git%{shortcommit}%{?dist}
Summary:        Fibrechannel transport daemon

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/brocade/bsn-fc-txptd/
Source:         %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  gcc
BuildRequires:  device-mapper-devel
BuildRequires:  systemd-devel
BuildRequires:  libudev-devel
BuildRequires:  udev
BuildRequires: device-mapper-multipath
BuildRequires: systemd
BuildRequires: device-mapper-multipath-devel
BuildRequires: make
Requires:       device-mapper >= 1.2.78


%description
The purpose of this daemon is to add FC network intelligence in host and
host intelligence in FC network. This daemon would inter-operate with
Brocade FC fabric in order to improve the response time of the MPIO failover.
In future, it can also collect the congestion related details and perform
workload analysis, and provide QOS at application level by inter-operating with
application performance profiling software.

%prep
%autosetup -n bsn-fc-txptd-%{commit}

%post
%systemd_post fctxpd.service

%preun
%systemd_preun fctxpd.service

%postun
%systemd_postun_with_restart fctxpd.service

%build
%make_build


%install
%make_install

%files
%doc README
%{_sbindir}/fctxpd
%{_unitdir}/fctxpd.service
%license LICENSES/GPL-2.0

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-14.20210326gitc4dba7f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2-13.20210326gitc4dba7f
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-12.20210326gitc4dba7f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-11.20210326gitc4dba7f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-10.20210326gitc4dba7f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-9.20210326gitc4dba7f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-8.20210326gitc4dba7f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-7.20210326gitc4dba7f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-6.20210326gitc4dba7f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-5.20210326gitc4dba7f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Mar 26 2021  Muneendra <muneendra.kumar@broadcom.com> 0.2-4.20210326gitc4dba7f
- Added support to add change rport port_state to marginal on fpin-li

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2-3.20200827gitccbaf3a
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-2.20200827gitccbaf3a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 27 2020  Muneendra <muneendra.kumar@broadcom.com> 0.2-1.20200827gitccbaf3a
- Added additioanl FPIN checks
- Updated the README

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-3.20190813gitc195e67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-2.20190813gitc195e67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

*Mon Aug 12 2019  Muneendra <muneendra.kumar@broadcom.com> 0.1-1.20190813gitc195e67
-No functional changes,just Licenses
-Spec file:Created LICENSES dir with the text of all used license
-Added the license header in the corresponding source files

*Fri Jul 26 2019  Muneendra <muneendra.kumar@broadcom.com> 0.1-1
-Initial package for fedora
