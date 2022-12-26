Name:           python-exabgp
Version:        4.2.21
Release:        1%{?dist}
Summary:        The BGP swiss army knife of networking (Library)

License:        BSD-3-Clause
URL:            https://github.com/Exa-Networks/exabgp
Source0:        https://github.com/Exa-Networks/exabgp/archive/%{name}-%{version}.tar.gz
Source1:        exabgp.sysusers.exabgp.conf
Source2:        exabgp.tmpfiles.exabgp.conf
Source3:        exabgp.systemd.exabgp.service
Source4:        exabgp.systemd.exabgp@.service

BuildArch:      noarch

%description
ExaBGP python module

%package -n python3-exabgp
Summary:        The BGP swiss army knife of networking
BuildRequires:  python3-devel
Requires:       python3 >= 3.7
Obsoletes:      python2-exabgp <= %{version}
%{?python_provide:%python_provide python3-exabgp}

%description -n python3-exabgp
The BGP swiss army knife of networking

%package -n exabgp
Summary:        The BGP swiss army knife of networking
BuildRequires:  systemd-rpm-macros
Requires:       systemd
Requires:       python3-exabgp = %{version}-%{release}

%description -n exabgp
The BGP swiss army knife of networking (exabgp systemd unit)

%prep
%autosetup -p1 -n exabgp-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files exabgp

# project installs binaries in /usr/bin but systemd unit expects it to be in /usr/sbin
mkdir -p %{buildroot}%{_sbindir}
mv %{buildroot}%{_bindir}/exabgp %{buildroot}%{_sbindir}/

# Install health check with non-generic name
install -p -m 0755 bin/healthcheck %{buildroot}%{_sbindir}/exabgp-healthcheck

# Install exabgpcli
install -p -m 0755 bin/exabgpcli %{buildroot}%{_bindir}/

# Configure required directories for the exabgp service
mkdir -p %{buildroot}/%{_sysconfdir}/exabgp

# Install exabgp systemd unit files
mkdir -p %{buildroot}/%{_unitdir}
install -p -m 0644 %{SOURCE3} %{buildroot}/%{_unitdir}/exabgp.service
install -p -m 0644 %{SOURCE4} %{buildroot}/%{_unitdir}/exabgp@.service

# Install man pages
mkdir -p %{buildroot}/%{_mandir}/man1
install -p -m 0644 doc/man/exabgp.1 %{buildroot}/%{_mandir}/man1/
mkdir -p %{buildroot}/%{_mandir}/man5
install -p -m 0644 doc/man/exabgp.conf.5 %{buildroot}/%{_mandir}/man5/

# Install sysusers.d files
mkdir -p %{buildroot}%{_sysusersdir}
install -p -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/exabgp.conf

# Install tmpfiles.d files
mkdir -p %{buildroot}%{_tmpfilesdir}
install -p -m 0644 %{SOURCE2} %{buildroot}%{_tmpfilesdir}/exabgp.conf

# Remove examples
rm -rf %{buildroot}%{_usr}/etc

%check
%tox

%pre -n exabgp
%sysusers_create_package exabgp %{SOURCE1}

%post -n exabgp
%systemd_post exabgp.service
# Default env
[ -f %{_sysconfdir}/exabgp/exabgp.env ] || %{_sbindir}/exabgp --full-ini > %{_sysconfdir}/exabgp/exabgp.env

%preun -n exabgp
%systemd_preun exabgp.service

%postun -n exabgp
%systemd_postun_with_restart exabgp.service

%files -n python3-exabgp -f %{pyproject_files}
%doc README.md
%license LICENCE.txt

%files -n exabgp
%{_bindir}/exabgp-healthcheck
%{_bindir}/exabgpcli
%{_bindir}/exabgp-cli
%{_sbindir}/exabgp
%{_sbindir}/exabgp-healthcheck
%dir %attr(750,root,exabgp) %{_sysconfdir}/exabgp
%{_unitdir}/exabgp.service
%{_unitdir}/exabgp@.service
%{_mandir}/man1/exabgp.1{,.*}
%{_mandir}/man5/exabgp.conf.5{,.*}
%{_sysusersdir}/exabgp.conf
%{_tmpfilesdir}/exabgp.conf

%changelog
* Sat Dec 24 2022 Gary Buhrmaster <gary.buhrmaster@gmail.com> - 4.2.21-1
- Update to upstream 4.2.21 (resolves rhbz#1721067)
- Update license to SPDX format
- spec file tidy/modernization
  - derive from current upstream
  - use modern python build macros
  - de-glob some files to follow current packaging guidelines

* Sat Dec 24 2022 Gary Buhrmaster <gary.buhrmaster@gmail.com> - 4.0.10-15
- Rebuild after PR#5 for pathfix.py location changes (resolves: rhbz#2155194)

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
