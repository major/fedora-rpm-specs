Name: restmbmaster
Version: 4
Release: 4%{?dist}
Summary: Rest API gateway to Modbus slaves
License: GPLv2+
URL: https://github.com/jpirko/%{name}/
Source0: https://github.com/jpirko/%{name}/raw/files/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: gcc
BuildRequires: libmodbus-devel
BuildRequires: libmicrohttpd-devel
BuildRequires: systemd

%description
This package contains a tool called %{name} which
is a simple daemon that allows user to access Modbus slaves
over Rest API. The slaves could be either connected over
serial line (Modbus RTU protocol), or over TCP (Modbus TCP protocol).

%prep
%setup -q

%build
%configure --disable-static
%{make_build}

%install
%{make_install}
mkdir -p %{buildroot}%{_unitdir}
install -p systemd/%{name}@.service %{buildroot}%{_unitdir}
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}

%files
%license COPYING
%doc %{name}/example_configs/ example_configs/
%{_unitdir}/%{name}@.service
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*
%{_mandir}/man5/%{name}.conf.5*
%{_sysconfdir}/%{name}

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar 08 2021 Jiri Pirko <jiri@resnulli.us> - 4-1
- Upgrade to version 4

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Sep 05 2020 Jiri Pirko <jiri@resnulli.us> - 3-1
- Upgrade to version 3

* Tue Aug 18 2020 Jiri Pirko <jiri@resnulli.us> - 2-1
- Upgrade to version 2

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 28 2019 Jiri Pirko <jiri@resnulli.us> - 1-1
- Initial build.
