%global oname targetcli-fb

Name:           targetcli
License:        Apache-2.0
Summary:        An administration shell for storage targets
Version:        3.0.1
Release:        2%{?dist}
URL:            https://github.com/open-iscsi/%{oname}
Source:         %{url}/archive/v%{version}/%{oname}-%{version}.tar.gz
# Proposed upstream
## From: https://github.com/open-iscsi/targetcli-fb/pull/176
BuildArch:      noarch
BuildRequires:  python3-devel, systemd-rpm-macros
Requires:       target-restore


%description
An administration shell for configuring iSCSI, FCoE, and other
SCSI targets, using the TCM/LIO kernel target subsystem. FCoE
users will also need to install and use fcoe-utils.


%prep
%setup -q -n %{oname}-%{version}

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l 'targetcli*'
mkdir -p %{buildroot}%{_sysconfdir}/target/backup
mkdir -p %{buildroot}%{_mandir}/man8/
install -m 644 targetcli*.8 %{buildroot}%{_mandir}/man8/
mkdir -p %{buildroot}%{_unitdir}/
install -m 644 systemd/* %{buildroot}%{_unitdir}/

%check
%pyproject_check_import

%files -f %{pyproject_files}
%doc README.md
%license COPYING
%{_bindir}/targetcli
%{_bindir}/targetclid
%{_mandir}/man8/targetcli*.8*
%{_unitdir}/*
%dir %{_sysconfdir}/target
%dir %{_sysconfdir}/target/backup

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jul 01 2025 Yaakov Selkowitz <yselkowi@redhat.com> - 3.0.1-1
- Update to 3.0.1

* Mon Jun 02 2025 Python Maint <python-maint@redhat.com> - 2.1.58-5
- Rebuilt for Python 3.14

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.58-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.58-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.1.58-2
- Rebuilt for Python 3.13

* Mon Feb 12 2024 Maurizio Lombardi <mlombard@redhat.com> - 2.1.58-1
- migrated to SPDX license
- Update to version v2.1.58

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.57-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild


* Thu Oct 26 2023 Maurizio Lombardi <mlombard@redhat.com> - 2.1.57-1
- Update to version v2.1.57

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.56-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.1.56-2
- Rebuilt for Python 3.12


* Tue Jun 06 2023 Maurizio Lombardi <mlombard@redhat.com> - 2.1.56-1
- Rebase to version 2.1.56

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.54-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.54-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.1.54-5
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.54-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.54-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.1.54-2
- Rebuilt for Python 3.10

* Mon May 17 2021 Maurizio Lombardi <mlombard@redhat.com> - 2.1.54-1
- Update to version 2.1.54

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.53-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.53-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Matt Coleman <matt@datto.com> - 2.1.53-1
- New upstream version
- Add the upstream project's targetclid systemd unit files
- Add proposed upstream patch:
  + Do not install systemd files in setup.py
  + https://github.com/open-iscsi/targetcli-fb/pull/176

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.fb49-9
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.fb49-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Neal Gompa <ngompa13@gmail.com> - 2.1.fb49-7
- Use correct Python macros to build the package
- Fix file list and install COPYING as license file
- Don't compress manpages in build phase, as rpm auto-compresses manpages

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.fb49-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.fb49-5
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.fb49-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 15 2019 Alan Pevec <apevec AT redhat.com> - 2.1.fb49-3
- Reduce dep to python3-gobject-base rhbz#1688808

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.fb49-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 10 2018 Andy Grover <agrover@redhat.com> - 2.1.fb49-1
- New upstream version
- Fix URL so spectool -g works
- Remove patch 0001-signed-char.patch

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.fb48-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.fb48-5
- Rebuilt for Python 3.7

* Tue May 8 2018 Andy Grover <agrover@redhat.com> - 2.1.fb48-4
- Add patch 0001-signed-char.patch

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.fb48-3
- Escape macros in %%changelog

* Wed Jan 31 2018 Andy Grover <agrover@redhat.com> - 2.1.fb48-2
- Add dep on python3-gobject

* Fri Jan 26 2018 Andy Grover <agrover@redhat.com> - 2.1.fb48-1
- New upstream version

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.fb46-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 1 2017 Andy Grover <agrover@redhat.com> - 2.1.fb46-1
- New upstream version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.fb43-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.1.fb43-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.fb43-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Apr 7 2016 Andy Grover <agrover@redhat.com> - 2.1.fb43-1
- New upstream version

* Tue Feb 23 2016 Andy Grover <agrover@redhat.com> - 2.1.fb42-3
- Fix #1294337 by adding dep on correct Py3 dbus pkg

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.fb42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 1 2015 Andy Grover <agrover@redhat.com> - 2.1.fb42-1
- New upstream version

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.fb41-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Aug 31 2015 Andy Grover <agrover@redhat.com> - 2.1.fb41-3
- Fix Requires to python3-six from python-six

* Fri Aug 28 2015 Andy Grover <agrover@redhat.com> - 2.1.fb41-2
- Add Requires on target-restore

* Tue Jun 23 2015 Andy Grover <agrover@redhat.com> - 2.1.fb41-1
- New upstream version
- Use python-six instead of 2to3

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.fb40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 20 2015 Andy Grover <agrover@redhat.com> - 2.1.fb40-1
- New upstream version

* Tue Jan 13 2015 Andy Grover <agrover@redhat.com> - 2.1.fb39-1
- New upstream version

* Tue Dec 2 2014 Andy Grover <agrover@redhat.com> - 2.1.fb38-1
- New upstream version

* Thu Nov 13 2014 Andy Grover <agrover@redhat.com> - 2.1.fb37-2
- Convert to using Python 3 interpreter and libs

* Wed Sep 24 2014 Andy Grover <agrover@redhat.com> - 2.1.fb37-1
- New upstream version

* Thu Aug 28 2014 Andy Grover <agrover@redhat.com> - 2.1.fb36-1
- New upstream version

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.fb35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 14 2014 Andy Grover <agrover@redhat.com> - 2.1.fb35-1
- New upstream version

* Mon Feb 24 2014 Andy Grover <agrover@redhat.com> - 2.1.fb34-1
- New upstream version

* Wed Dec 4 2013 Andy Grover <agrover@redhat.com> - 2.1.fb33-1
- New upstream version

* Fri Nov 1 2013 Andy Grover <agrover@redhat.com> - 2.1.fb31-1
- New upstream version
- Move service handling to python-rtslib
- Remove old packaging bits: clean, buildroot, defattr

* Thu Sep 12 2013 Andy Grover <agrover@redhat.com> - 2.1.fb30-1
- New upstream version

* Tue Sep 10 2013 Andy Grover <agrover@redhat.com> - 2.1.fb29-1
- New upstream release
- Remove no-longer-needed BuildRequires

* Mon Aug 5 2013 Andy Grover <agrover@redhat.com> - 2.1.fb28-1
- New upstream release

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.fb27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Andy Grover <agrover@redhat.com> - 2.1.fb27-1
- New upstream release
- License now Apache 2.0
- Remove patch modules-not-loaded.patch

* Tue Jun 18 2013 Andy Grover <agrover@redhat.com> - 2.1.fb26-2
- Add patch
  * modules-not-loaded.patch

* Fri Jun 7 2013 Andy Grover <agrover@redhat.com> - 2.1.fb26-1
- New upstream release

* Thu May 9 2013 Andy Grover <agrover@redhat.com> - 2.1.fb25-1
- New upstream release

* Thu May 2 2013 Andy Grover <agrover@redhat.com> - 2.1.fb24-1
- New upstream release
- Update source URL

* Fri Apr 12 2013 Andy Grover <agrover@redhat.com> - 2.1.fb23-1
- New upstream release

* Wed Apr 10 2013 Andy Grover <agrover@redhat.com> - 2.1.fb22-1
- New upstream release

* Mon Mar 4 2013 Andy Grover <agrover@redhat.com> - 2.0.fb21-1
- New upstream release

* Tue Feb 26 2013 Andy Grover <agrover@redhat.com> - 2.0.fb20-1
- New upstream release

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0rc1.fb19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 7 2013 Andy Grover <agrover@redhat.com> - 2.0rc1.fb19-1
- New upstream release

* Thu Jan 3 2013 Andy Grover <agrover@redhat.com> - 2.0rc1.fb18-2
- Add python-ethtool BuildRequires

* Thu Dec 20 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb18-1
- New upstream release
- Add python-ethtool requires
- Update Source0 to use Github tar-from-tag instead of Downloads

* Thu Dec 13 2012 Lukáš Nykrýn <lnykryn@redhat.com> - 2.0rc1.fb17-2
- Scriptlets replaced with new systemd macros (#850335)

* Mon Nov 12 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb17-1
- New upstream release

* Tue Aug 7 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb16-1
- New upstream release
- Update rtslib version dependency

* Tue Jul 31 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb15-1
- New upstream release

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0rc1.fb14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 28 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb14-2
- Fix %%files to claim /etc/target, not claim sitelib

* Thu Jun 28 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb14-1
- New upstream release

* Tue Jun 12 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb13-1
- New upstream release

* Wed May 30 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb12-1
- Update Source URL to proper tarball
- New upstream release

* Mon Apr 9 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb11-1
- New upstream release

* Wed Feb 29 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb10-1
- New upstream release

* Tue Feb 21 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb9-1
- New upstream release

* Thu Feb 16 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb8-1
- New upstream release

* Wed Feb 8 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb7-1
- New upstream release

* Fri Feb 3 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb6-1
- New upstream release

* Tue Jan 24 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb5-2
- Update After= in service file to wait for localfs and network
- Improve description in service file

* Tue Jan 24 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb5-1
- New upstream release

* Fri Jan 13 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb4-1
- New upstream release

* Tue Dec 13 2011 Andy Grover <agrover@redhat.com> - 2.0rc1.fb3-2
- Fix service file to mount configfs before starting targetcli

* Tue Dec 13 2011 Andy Grover <agrover@redhat.com> - 2.0rc1.fb3-1
- New upstream release
- Fixup service file for new start/stop targetcli commands

* Tue Dec 6 2011 Andy Grover <agrover@redhat.com> - 2.0rc1.fb2-1
- New upstream source and release
- Remove patches:
  * targetcli-git-version.patch
  * 0001-Remove-ads-from-cli-welcome-msg.-Mention-help-is-ava.patch
  * 0002-bundle-lio-utils.patch
  * 0003-Hack.-dump-scripts-aren-t-in-PATH-anymore-so-call-th.patch
  * 0004-ignore-errors-from-failure-to-set-device-attributes.patch
  * 0005-fix-spec_root-path.patch
  * 0006-add-docs.patch
  * 0007-all-start.patch

* Mon Nov 21 2011 Andy Grover <agrover@redhat.com> - 1.99.2.gitb03ec79-4
- Update doc patch to include iscsi tutorial

* Wed Nov 2 2011 Andy Grover <agrover@redhat.com> - 1.99.2.gitb03ec79-3
- Add buildrequires for systemd-units
- use _unitdir
- remove preun, modify post

* Wed Nov 2 2011 Andy Grover <agrover@redhat.com> - 1.99.2.gitb03ec79-2
- Add patch
  * 0007-all-start.patch
- Replace sysv init with systemd init

* Fri Oct 7 2011 Andy Grover <agrover@redhat.com> - 1.99.2.gitb03ec79-1
- Initial Fedora packaging
