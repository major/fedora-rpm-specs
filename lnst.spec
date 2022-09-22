# The package contains python code in /usr/share that is not executed on
# the machine where it is installed. Instead, it is distributed to its
# slaves to be executed there. To exclude these modules from the automatic
# byte compilation, we turn off the global byte-compile script here and
# compile the rest of the code manually.
%global _python_bytecompile_extra 0

Name:       lnst
Version:    15
Release:    14%{?dist}
Summary:    Common code for lnst-ctl and lnst-slave
Requires:   python3, python3-pyroute2, bzip2, tar

License:    GPLv2+
URL:        http://lnst-project.org
Source0:    http://lnst-project.org/files/%{name}-%{version}.tar.gz
Patch:      fix-python-shebangs.patch

BuildRequires:    python3-devel, systemd-units
BuildArch:        noarch


%package ctl
Summary:    Linux Network Stack Test Controller
Requires:   %{name} = %{version}-%{release}, python3-lxml, python3-requests, procps-ng


%package slave
Summary:           Linux Network Stack Test Slave Daemon
Requires:          %{name} = %{version}-%{release}, bridge-utils, gcc, make, iproute, ethtool, python3-dbus, python3-ethtool
Requires(post):    systemd
Requires(post):    policycoreutils-python-utils
Requires(preun):   systemd
Requires(postun):  systemd
Requires(postun):  policycoreutils-python-utils

%package recipes
Summary:           Linux Network Stack Test recipes

%description
Linux Network Stack Test is a tool useful for developing and performing
automated network tests. LNST focuses on maximum portability of the
so-called recipes (descriptions of test cases and scenarios).

This package contains the code that is common for both LNST controller
and LNST slave.

%description ctl
LNST controller is able to communicate with networks of LNST slave
daemons and execute tests on them.

%description slave
LNST slave is a daemon that waits for instructions from LNST controller.
It is able to react to a variety of commands from the controller and act
as a test node for executing network tests.

%description recipes
This package installs test recipes that are maintained by the LNST project.
These can be used by the LNST controller.


%prep
%setup -q -n %{name}-%{version}


%build
%{__python3} setup.py build


%install
%{__python3} setup.py install --root=%{buildroot}
install -D -m 0644 dist/%{name}-slave.service %{buildroot}/%{_unitdir}/%{name}-slave.service

# Manually compile files in python sitelib that need bytecompilation
%py_byte_compile %{__python3} %{buildroot}%{python3_sitelib}

%post slave
semanage fcontext -a -t bin_t -f f %{_bindir}/%{name}-slave
restorecon -R %{_bindir}/%{name}-slave
%systemd_post lnst-slave.service

%preun slave
%systemd_preun lnst-slave.service

%postun slave
semanage fcontext -d -t bin_t -f f %{_bindir}/%{name}-slave
%systemd_postun_with_restart lnst-slave.service

%files
%doc README.md COPYING
%dir %{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}/__pycache__/*
%{python3_sitelib}/%{name}/__init__.*
%{python3_sitelib}/%{name}/Common/
%{python3_sitelib}/%{name}-%{version}-*.egg-info

%files ctl
%{python3_sitelib}/%{name}/Controller/
%{python3_sitelib}/%{name}/RecipeCommon/
%{_bindir}/%{name}-ctl
%{_bindir}/%{name}-pool-wizard
%{_mandir}/man1/%{name}-ctl.1.*
%{_mandir}/man1/%{name}-pool-wizard.1.*
%{_sysconfdir}/bash_completion.d/%{name}-ctl.bash
%{_sysconfdir}/bash_completion.d/%{name}-pool-wizard.bash
%config(noreplace) %{_sysconfdir}/%{name}-ctl.conf
%{_datadir}/%{name}/
%exclude %{_datadir}/%{name}/recipes/

%files slave
%{python3_sitelib}/%{name}/Slave/
%{_bindir}/%{name}-slave
%{_mandir}/man1/%{name}-slave.1.*
%{_sysconfdir}/bash_completion.d/%{name}-slave.bash
%config(noreplace) %{_sysconfdir}/%{name}-slave.conf
%{_unitdir}/%{name}-slave.service

%files recipes
%{_datadir}/%{name}/recipes/


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 15-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 15-13
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 15-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 15-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 15-10
- Rebuilt for Python 3.10

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 15-9
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 15-6
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 15-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 26 2019 Ondrej Lichtner <olichtne@redhat.com> - 15-3
- Update to 15.1 sources which includes a python3 port for one more script

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 15-2
- Rebuilt for Python 3.8

* Thu Aug 15 2019 Ondrej Lichtner <olichtne@redhat.com> - 15-1
- Updating to stable release 15
- Python3 port of the XML Recipe supporting LNST

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Jan Tluka <jtluka@redhat.com> - 13.6
- Update to satisfy Fedora29 Python requirements
- Use python2 macros python2_sitelib and __python2
- Use proper macros for manual bytecompiling

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 13-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 21 2017 Jan Tluka <jtluka@redhat.com> - 13-1
- Updating to stable release 13
- Most likely the final release supporting XML recipes

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Oct 07 2016 Ondrej Lichtner <olichtne@redhat.com> - 12-1
- Updating to stable release 12
- This is going to be one of the final releases supporting XML recipes

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 19 2016 Ondrej Lichtner <olichtne@redhat.com> - 11-2
- added missing dbus-python dependency for lnst-slave

* Thu Feb 18 2016 Ondrej Lichtner <olichtne@redhat.com> - 11-1
- Updating to stable release 11

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 30 2015 Ondrej Lichtner <olichtne@redhat.com> - 10-1
- Updating to stable release 10
- fixed selinux label for binaries
- added wizard

* Thu Oct 15 2015 Ondrej Lichtner <olichtne@redhat.com> - 9-1
- Updating to stable release 9
- Fixed dependencies of lnst-slave

* Mon Jul 27 2015 Jan Tluka <jtluka@redhat.com> - 8-4
- Updated dep on policycoreutils-python-utils for Fedora 23 and newer 

* Fri Jul 24 2015 Tomas Radej <tradej@redhat.com> - 8-3
- Updated dep on policycoreutils-python-utils

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 27 2015 Jiri Pirko <jpirko@redhat.com> - 8-1
- Updating to stable release 8
- Fixed subpackages dependencies

* Wed Mar 11 2015 Jiri Pirko <jpirko@redhat.com> - 7-1
- Updating to stable release 7

* Fri Dec 05 2014 Jiri Pirko <jpirko@redhat.com> - 6-1
- Updating to stable release 6

* Mon Jul 28 2014 Jiri Pirko <jpirko@redhat.com> - 5-1
- Updating to stable release 5

* Thu Jul 03 2014 Jiri Pirko <jpirko@redhat.com> - 4-1
- Updating to stable release 4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 18 2014 Jiri Pirko <jpirko@redhat.com> - 3-1
- Updating to stable release 3

* Sat Jan 25 2014 Jiri Pirko <jpirko@redhat.com> - 2-1
- Updating to stable release 2

* Thu Oct 10 2013 Radek Pazdera <rpazdera@redhat.com> - 1-2
- Fixing accidentally removed dist tag

* Thu Oct 10 2013 Radek Pazdera <rpazdera@redhat.com> - 1-1
- Updating to stable release 1
- Added new dependencies (python2-pyroute, python-lxml, bzip2)
- Fixed bogus date warnings in changelog

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.7.20130717git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Radek Pazdera <rpazdera@redhat.com> - 0.1-0.6.20130717git
- Update to commit 269de0a

* Wed Feb 06 2013 Radek Pazdera <rpazdera@redhat.com> - 0.1-0.5.20130206git
- Update to commit f901a34

* Tue Jan 15 2013 Radek Pazdera <rpazdera@redhat.com> - 0.1-0.4.20121204git
- removed -common subpackage, its content was moved to the base package
- fixed release number to meet the conventions for pre-release packages
- fixed inaccurate license

* Thu Jan 10 2013 Radek Pazdera <rpazdera@redhat.com> - 0.1-0.3.20121204git
- removed dependency on python3-devel for python bytecompile macros
- use py_copmp and py_ocomp macros from macros.python instead

* Thu Jan 03 2013 Radek Pazdera <rpazdera@redhat.com> - 0.1-0.2.20121204git
- Added a comment explaining disabling global byte-compile
- Removed superfluous dependency on python runtime
- Fixed a problem with unowned directories
- Man pages are now included by a wild-card
- Added proper systemd service handling

* Tue Dec 04 2012 Radek Pazdera <rpazdera@redhat.com> - 0.1-0.1.20121204git
- Initial package
