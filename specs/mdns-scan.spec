Summary:        Scan for mDNS/DNS-SD services published on the local network
Name:           mdns-scan
Version:        0.5
Release:        12%{?dist}
License:        GPL-2.0-or-later
URL:            https://github.com/alteholz/mdns-scan/
Source0:        https://github.com/alteholz/mdns-scan/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         mdns-scan-0.5-typo.patch
BuildRequires:  make
BuildRequires:  gcc

%description
mdns-scan is a tool for scanning for mDNS/DNS-SD services published on
the local network. It works by issuing a mDNS PTR query to the special
RR _services._dns-sd._udp.local for retrieving a list of all currently
registered services on the local link.

%prep
%setup -q
%patch -P0 -p1 -b .typo

%build
%make_build CFLAGS="$RPM_OPT_FLAGS $RPM_LD_FLAGS"

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
%make_install
install -D -p -m 0644 %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%files
%license LICENSE
%doc README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 01 2020 Robert Scheck <robert@fedoraproject.org> 0.5-1
- Upgrade to 0.5 (#1830539)
- Initial spec file for Fedora and Red Hat Enterprise Linux
