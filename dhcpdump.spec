Name:           dhcpdump
Version:        1.8
Release:        5%{?dist}
Summary:        Parse DHCP packets

License:        BSD-2-Clause
URL:            http://www.mavetju.org/unix/general.php
Source0:        http://www.mavetju.org/download/%{name}-%{version}.tar.gz
Patch0: dhcpdump.c.patch
Patch1: dhcpdump-build.patch
Patch2: dhcpdump-bugfix_ethertype.patch
Patch3: dhcpdump-bugfix_flags.patch
Patch4: dhcpdump-bugfix_opt82.patch
Patch5: dhcpdump-bugfix_strcounts.patch
Patch6: dhcpdump-warnings.patch
Patch7: dhcpdump-spelling.patch


BuildRequires:  gcc
BuildRequires:  libpcap-devel
BuildRequires:  make
BuildRequires:  perl-podlators

%description
A utility to analyze sniffed DHCP packets.

%prep
%autosetup -p1


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
