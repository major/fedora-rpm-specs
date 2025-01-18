Name:           dhcpdump
Version:        1.9
Release:        5%{?dist}
Summary:        Parse DHCP packets

License:        BSD-2-Clause
URL:            https://github.com/bbonev/%{name}
Source0:        https://github.com/bbonev/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/bbonev/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2:        https://raw.githubusercontent.com/bbonev/%{name}/v%{version}/debian/upstream/signing-key.asc


BuildRequires:  gcc
BuildRequires:  libpcap-devel
BuildRequires:  make
BuildRequires:  perl-podlators
BuildRequires:  gnupg2

%description
A utility to analyze sniffed DHCP packets.

%global _hardened_build 1

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup


%build
%make_build

%install
install -D -p -m 755 -t %{buildroot}%{_bindir} %{name}
install -D -p -m 644 -t %{buildroot}%{_mandir}/man8/ %{name}.8

%files
%license LICENSE
%doc CHANGES CONTACT
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 10 2023 Boian Bonev <bbonev@ipacct.com> - 1.9-1
- Change upstream to a maintained fork

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Feb 23 2023 Boian Bonev <bbonev@ipacct.com> - 1.8-5
- Import multiple fixes from Debian

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Dec 11 2022 Florian Weimer <fweimer@redhat.com> - 1.8-3
- Port to C99 (#2152420)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 13 2022 Jonathan Wright <jonathan@almalinux.org> - 1.8-1
- Initial version of the package
