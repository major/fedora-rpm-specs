Name:           nsntrace
Version:        4
Release:        6%{?dist}
Summary:        Perform network trace of a program by using network namespaces

License:        GPLv2+
URL:            https://github.com/nsntrace/nsntrace
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  libpcap-devel
BuildRequires:  pkgconfig(libnl-route-3.0)
BuildRequires:  /usr/sbin/iptables
BuildRequires:  libxslt
BuildRequires:  docbook-style-xsl

Requires:  /usr/sbin/iptables

%description
The nsntrace program uses Linux network namespaces to perform network traces
of a single application. The traces are saved as pcap files. And can later be
analyzed by for instance Wireshark.

%prep
%autosetup

%build
./autogen.sh
%configure
%make_build

%install
%make_install

# As tests requires sudo, spec doesn't contain check section

%files
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 15 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 4-2
- Adding note for check based on BZ1914638 review

* Sun Jan 10 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 4-1
- Version update

* Fri Jul 22 2016 jonas <jonas@threetimestwo.org> - 2-1
- Initial SPEC for package

