%global srcname exabgp

Name:           python-exabgp
Version:        4.0.10
Release:        14%{?dist}
Summary:        The BGP swiss army knife of networking (Library)

License:        BSD
URL:            https://github.com/Exa-Networks/exabgp
Source0:        https://github.com/Exa-Networks/%{srcname}/archive/%{version}.tar.gz

BuildArch:      noarch

%description
ExaBGP python module


%package -n python3-%{srcname}
Summary:        The BGP swiss army knife of networking
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-six
Conflicts:      python2-%{srcname} < 4.0.10
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
The BGP swiss army knife of networking

%package -n exabgp
Summary:        The BGP swiss army knife of networking
BuildRequires:  systemd-units
Requires:       systemd
Requires:       python3-%{srcname} = %{version}-%{release}

%description -n exabgp
The BGP swiss army knife of networking (exabgp systemd unit)

%prep
%autosetup -n %{srcname}-%{version}
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" etc/exabgp/run/*

%build
%py3_build

%install
%py3_install

# XXX: setup.py installs binaries in /usr/bin but systemd unit expects it to be in /usr/sbin
mkdir -p %{buildroot}%{_sbindir}
mv %{buildroot}%{_bindir}/%{srcname} %{buildroot}%{_sbindir}/

# Install health check
install -p -D -m 0755 bin/healthcheck %{buildroot}%{_sbindir}
mv %{buildroot}%{_sbindir}/healthcheck %{buildroot}/%{_sbindir}/%{srcname}-healthcheck

# Install exabgpcli
install -p -D -m 0755 bin/exabgpcli %{buildroot}%{_bindir}

# Configure required directories for the exabgp service
mkdir -p %{buildroot}/%{_sysconfdir}/exabgp
mkdir -p %{buildroot}/%{_libdir}/exabgp
# Install exabgp systemd unit
mkdir -p %{buildroot}/%{_unitdir}
install -p -D -m 0644 etc/systemd/%{srcname}.service %{buildroot}/%{_unitdir}/%{srcname}.service

# Install man pages
mkdir -p %{buildroot}/%{_mandir}/man1
install doc/man/exabgp.1 %{buildroot}/%{_mandir}/man1
mkdir -p %{buildroot}/%{_mandir}/man5
install doc/man/exabgp.conf.5 %{buildroot}/%{_mandir}/man5

%post -n exabgp
%systemd_post %{srcname}.service

%preun -n exabgp
%systemd_preun %{srcname}.service

%postun -n exabgp
%systemd_postun_with_restart %{srcname}.service


%files -n python3-%{srcname}
%doc CHANGELOG README.md
%license COPYRIGHT
%{python3_sitelib}/*

# Let's split out exabgp service here
%files -n exabgp
%attr(755, root, root) %{_sbindir}/%{srcname}-healthcheck
%attr(755, root, root) %{_sbindir}/%{srcname}
%attr(755, root, root) %{_bindir}/exabgpcli
%{_unitdir}/%{srcname}.service
%dir %{_libdir}/%{srcname}
%dir %{_datadir}/%{srcname}
%dir %{_datadir}/%{srcname}/processes
%dir %{_sysconfdir}/%{srcname}
%attr(744, root, root) %{_datadir}/%{srcname}/processes/*
%{_mandir}/man1/*
%{_mandir}/man5/*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.0.10-13
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.0.10-10
- Rebuilt for Python 3.10

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.0.10-9
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0.10-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.10-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 28 2018 Miro Hrončok <mhroncok@redhat.com> - 4.0.10-1
- Update to 4.0.10, Python 3 only

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.0.5-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Luke Hinds <lhinds@redhat.com> - 4.0.5
- 4.0.5 release

* Tue Jan 16 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.0.1-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 10 2017 Luke Hinds <lhinds@redhat.com> - 4.0.1-2
- Fixed dependency issues
* Fri Jul 07 2017 Luke Hinds <lhinds@redhat.com> - 4.0.1
- 4.0.1 release, and python 3 support
* Fri May 19 2017 Luke Hinds <lhinds@redhat.com> - 4.0.0
- Initial release
