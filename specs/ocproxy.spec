%global commit0 c98f06d942970cdf35dd66ab46840f7d6d567b60
%global date0   20190728
%global scommit %(c=%{commit0}; echo ${c:0:7} )

Name:           ocproxy
Version:        1.60
Release:        14.%{date0}git%{scommit}%{?dist}
Summary:        OpenConnect Proxy

# BSD for both ocproxy and bundled lwip
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/cernekee/%{name}
Source0:        %{url}/archive/%{commit0}.tar.gz#/%{name}-%{scommit}.tar.gz
# PR#11 rebased:
# use latest lwip sources, fix gcc warnings
# drop useless files copied accidently from lwip project
Patch0:         %{name}-1.60-with-lwip-2.1.2.patch

BuildRequires:  automake make gcc
BuildRequires:  libevent-devel

Provides:       bundled(lwip) = 2.1.2
Requires:       openconnect

%description
OCProxy is a user-level SOCKS and port forwarding proxy for OpenConnect based
on lwIP. When using ocproxy, OpenConnect only handles network activity that 
the user specifically asks to proxy, so the VPN interface no longer "hijacks" 
all network traffic on the host.

%prep
%autosetup -p1 -n%{name}-%{commit0}
./autogen.sh


%build
%configure --enable-vpnns
%make_build


%install
%make_install


%files
%license LICENSE
%doc %{_docdir}/%{name}/
%{_bindir}/%{name}
%{_bindir}/vpnns
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/vpnns.1*



%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-14.20190728gitc98f06d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 2 2024 Miroslav Suchý <msuchy@redhat.com> - 1.60-13.20190728gitc98f06d
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-12.20190728gitc98f06d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-11.20190728gitc98f06d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-10.20190728gitc98f06d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-9.20190728gitc98f06d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-8.20190728gitc98f06d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-7.20190728gitc98f06d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-6.20190728gitc98f06d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-5.20190728gitc98f06d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-4.20190728gitc98f06d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-3.20190728gitc98f06d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-2.20190728gitc98f06d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Raphael Groner <projects.rg@smart.ms> - 1.60-1.20190728gitc98f06d
- initial
- use latest lwip sources, pull request #11
