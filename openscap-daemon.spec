%global debug_package %{nil}
%if 0%{?fedora} <= 22 || (0%{?rhel} != 0 && 0%{?rhel} <= 7)
%global pypkg python
%global pysitelib %{python_sitelib}
%global __python %{__python}
%global pgobject pygobject2
%else
%global pypkg python3
%global pysitelib %{python3_sitelib}
%global __python %{__python3}
%global pgobject python3-gobject-base
%endif

Name:           openscap-daemon
Version:        0.1.10
Release:        19%{?dist}
Summary:        Manages continuous SCAP scans of your infrastructure

License:        LGPLv2+
URL:            http://open-scap.org
Source0:        https://github.com/OpenSCAP/openscap-daemon/releases/download/%{version}/openscap_daemon-%{version}.tar.gz
Patch0:         no-async.patch
Patch1:         pr149_remove_cElementTree.patch
BuildArch:      noarch

BuildRequires:  systemd-units
BuildRequires:  %{pypkg}-devel
Requires:       %{pypkg}
Requires:       %{pypkg}-dbus
Requires:       %{pgobject}
Requires:       dbus

# for the oscap tool
Requires:       openscap-scanner
# for oscap-ssh, oscap-docker, oscap-vm
Requires:       openscap-utils

%description
OpenSCAP-daemon is a service that performs SCAP scans of bare-metal machines,
virtual machines and containers. These scans can be either one-shot or
continuous according to a schedule. You can interact with the service
using the provided oscapd-cli tool or via the DBus interface.

%prep
%setup -q -n openscap_daemon-%{version}

%patch0 -p1
%patch1 -p1

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT

%files
%doc %{_docdir}/%{name}/README.md
%doc %{_docdir}/%{name}/LICENSE

%dir %{pysitelib}/openscap_daemon
%{pysitelib}/openscap_daemon/*

%{pysitelib}/*egg-info

%{_bindir}/oscapd
%{_mandir}/man8/oscapd.8.gz
%{_bindir}/oscapd-cli
%{_mandir}/man8/oscapd-cli.8.gz
%{_bindir}/oscapd-evaluate
%{_mandir}/man8/oscapd-evaluate.8.gz

%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.oscapd.conf
%{_unitdir}/oscapd.service

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.1.10-18
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.10-15
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.10-12
- Rebuilt for Python 3.9

* Wed May 06 2020 Jan Černý <jcerny@redhat.com> - 0.1.10-11
- Fix import cElementTree module (RHBZ#1817660)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.10-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.10-8
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 06 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.10-5
- Require Python 3 version of the dbus library

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Matěj Týč <matyc@redhat.com> - 0.1.10-3
- Applied patch for Python 3.7 compatibility

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.10-2
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Jan Cerny <jcerny@redhat.com> - 0.1.10-1
- upgrade to the latest upstream release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Jan Cerny <jcerny@redhat.com> - 0.1.9-1
- upgrade to the latest upstream release

* Thu Sep 28 2017 Martin Preisler <mpreisle@redhat.com> - 0.1.8-1
- upgrade to the latest upstream release

* Thu Aug 03 2017 Jan Cerny <jcerny@redhat.com> - 0.1.7-1
- upgrade to the latest upstream release

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1.6-2
- Rebuild for Python 3.6

* Tue Sep 06 2016 Martin Preisler <mpreisle@redhat.com> - 0.1.6-1
- upgrade to the latest upstream release

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Apr 22 2016 Martin Preisler <mpreisle@redhat.com> - 0.1.5-1
- upgrade to the latest upstream release

* Mon Mar 28 2016 Martin Preisler <mpreisle@redhat.com> - 0.1.4-1
- upgrade to the latest upstream release

* Thu Feb 11 2016 Šimon Lukašík <slukasik@redhat.com> - 0.1.3-1
- upgrade to the latest upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Martin Preisler <mpreisle@redhat.com> - 0.1.2-1
- updated to 0.1.2
- dropped dependency on python-requests

* Thu Jan 21 2016 Šimon Lukašík <slukasik@redhat.com> - 0.1.1-4
- Add dependency on python requests

* Wed Jan 20 2016 Šimon Lukašík <slukasik@redhat.com> - 0.1.1-3
- Add dependency on python gobject

* Tue Jan 12 2016 Martin Preisler <mpreisle@redhat.com> - 0.1.1-2
- dropped the atomic requirement, it's an optional dependency

* Mon Jan 11 2016 Martin Preisler <mpreisle@redhat.com> - 0.1.1-1
- updated to 0.1.1

* Tue Dec 01 2015 Šimon Lukašík <slukasik@redhat.com> - 0.1.0-5
- build on all platforms where atomic is available

* Fri Nov 27 2015 Šimon Lukašík <slukasik@redhat.com> - 0.1.0-4
- install openscap-daemon in python3 directories on F23+

* Fri Nov 27 2015 Šimon Lukašík <slukasik@redhat.com> - 0.1.0-3
- openscap-daemon is now exlusively on x86_64

* Fri Nov 20 2015 Martin Preisler <mpreisle@redhat.com> - 0.1.0-2
- require dbus
- fixed license
- added config(noreplace) for org.oscapd.conf

* Mon Oct 26 2015 Martin Preisler <mpreisle@redhat.com> - 0.1.0-1
- initial version
