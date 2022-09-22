%global _hardened_build 1

Name:           ubridge
Version:        0.9.18
Release:        7%{?dist}
Summary:        Bridge for UDP tunnels, Ethernet, TAP and VMnet interfaces

License:        GPLv3+
URL:            https://github.com/GNS3/ubridge
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz


# Not needed, RPM will auto-generate deps
#Requires: iniparser
BuildRequires: libnl3-devel
BuildRequires: libpcap-devel
BuildRequires: gcc
BuildRequires: make
BuildRequires: iniparser-devel
# So rpm can set caps
BuildRequires: libcap
BuildRequires: git-core

# LXC netlink code seems to be from older lxc codebase
# lxc-devel/lxc-lib do not provide it either
Provides: bundled(lxc-libs)


%description
uBridge is a simple application to create user-land bridges between various
technologies. Currently bridging between UDP tunnels, Ethernet and TAP
interfaces is supported. Packet capture is also supported.

%prep
%autosetup -S git


%build
make %{?_smp_mflags} SYSTEM_INIPARSER=1 CFLAGS="-DLINUX_RAW $RPM_OPT_FLAGS -lnl-3"

%install
mkdir -p %{buildroot}%{_bindir}
install -p -m4755 %{name} %{buildroot}%{_bindir}



%files
%license LICENSE
%doc README.rst
%attr(0755,root,root) %caps(cap_net_admin,cap_net_raw=ep) %{_bindir}/%{name}


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 10 2021 Alexey Kurov <nucleo@fedoraproject.org> - 0.9.18-4
- Add -lnl-3 in CFLAGS, BuildRequires: libnl3-devel (Bug 1923474)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 30 2020 Nicolas Chauvet <kwizart@gmail.com> - 0.9.18-1
- Update to 0.9.18

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 21 2019 Athmane Madjoudj <athmane@fedoraproject.org> - 0.9.14-5
- Enable raw support

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun May 06 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 0.9.14-2
- Fix capabilities (rhbz #1575005)

* Sun Mar 18 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 0.9.14-1
- Update to 0.9.14
- Remove upstreamed patches

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 29 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 0.9.12-2
- Use hardened build flags
- Unbundle libs

* Sun Jul 30 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 0.9.12-1
- Initial spec

