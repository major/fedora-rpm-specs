Summary:        Filter IPv4 and IPv6 addresses matching CIDR patterns
Name:           grepcidr
Version:        2.0
Release:        10%{?dist}
License:        GPL-2.0-or-later
URL:            https://www.pc-tools.net/unix/grepcidr/
Source0:        https://www.pc-tools.net/files/unix/%{name}-%{version}.tar.gz
Source1:        https://www.pc-tools.net/files/unix/%{name}-%{version}.tar.gz.sha512
BuildRequires:  make
# Unfortunately we cannot build the grepcidr man page in Fedora because
# we do not have docbook-to-man, just docbook2man and db2x_docbook2man.
BuildRequires:  gcc

%description
The grepcidr utility can be used to filter a list of IP addresses against
one or more Classless Inter-Domain Routing (CIDR) specifications. As with
grep, there are options to invert matching and load patterns from a file.
It is capable of efficiently processing large numbers of IPs and networks.

%prep
%setup -q
sed -e 's/install /$(INSTALL) /' -i Makefile

%build
%make_build CFLAGS="$RPM_OPT_FLAGS $RPM_LD_FLAGS"

%install
%make_install BINDIR="%{_bindir}" MANDIR="%{_mandir}"

%files
%license COPYING
%doc ChangeLog README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0-9
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 14 2021 Robert Scheck <robert@fedoraproject.org> 2.0-1
- Upgrade to 2.0 (#2013866)
- Initial spec file for Fedora and Red Hat Enterprise Linux
