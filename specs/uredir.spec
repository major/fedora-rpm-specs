Name:           uredir
Version:        3.3
Release:        10%{?dist}
Summary:        UDP port redirector

License:        ISC
URL:            https://github.com/troglobit/uredir
Source0:        https://github.com/troglobit/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext
BuildRequires:  libuev-devel
BuildRequires:  make

%description
uredir is a small Linux daemon to redirect UDP connections. 
It can be used to forward connections on small and embedded 
systems that do not have (or want to use) iptables or nftables.

%prep
%autosetup

%build
./autogen.sh
%configure
%make_build

%check
make check

%install
%make_install

# remove docs from buildroot
rm -rf %{buildroot}%{_docdir}/%{name}

%files
%license LICENSE
%doc README.md AUTHORS design.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 04 2021 Alessio <alessio@fedoraproject.org> - 3.3-3
- Rebuilt for libuev so version change

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Apr 07 2021 Alessio <alessio@fedoraproject.org> - 3.3-1
- Initial RPM version
