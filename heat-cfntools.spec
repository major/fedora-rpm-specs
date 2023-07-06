Name: heat-cfntools
Version: 1.4.2
Release: 22%{?dist}
Summary: Tools required to be installed on Heat provisioned cloud instances
License: ASL 2.0
URL: https://launchpad.net/heat-cfntools/
Source0: https://pypi.python.org/packages/source/h/heat-cfntools/%{name}-%{version}.tar.gz

# All patches to current git master (d23083a8e93311def2fc78fe7ece2a76fe59287b)
# Fixes issues with requirements, code style, Python 3.6+ compat,
# updates links to openstack.org not launchpad.net
# patches 8 and 16 manually rediffed for differences between 1.4.2
# tarball and git tag
Patch0001: 0001-Changed-logger-init-and-added-verbose-arg-handling.patch
Patch0002: 0002-Replace-deprecated-LOG.warn-with-LOG.warning.patch
Patch0003: 0003-Fix-typo.patch
Patch0004: 0004-Drop-unused-directory-in-tox.patch
Patch0005: 0005-Replace-MagicMock-with-Mock.patch
Patch0006: 0006-Show-team-and-repo-badges-on-README.patch
Patch0007: 0007-Remove-white-space-between-print.patch
Patch0008: 0008-Add-OpenStack-doc-support-for-heat-cfntools.patch
Patch0009: 0009-Remove-discover-from-test-requirements.patch
Patch0010: 0010-Update-links-in-README.patch
Patch0011: 0011-Python3-Don-t-use-cmp-function.patch
Patch0012: 0012-Fix-pep8-errors-with-later-versions-of-hacking.patch
Patch0013: 0013-Move-Zuul-config-into-repo.patch
Patch0014: 0014-Modernise-requirements.patch
Patch0015: 0015-Add-tox-python3-overrides.patch
Patch0016: 0016-Switch-to-use-stestr-for-unit-test.patch
Patch0017: 0017-fix-bug-link-in-readme.patch
Patch0018: 0018-add-python-3.6-unit-test-job.patch
Patch0019: 0019-Migrate-the-link-of-bug-report-button-to-storyboard.patch
Patch0020: 0020-Use-template-for-lower-constraints.patch
Patch0021: 0021-Update-the-bugs-link-to-storyboard.patch

BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-testrepository
BuildRequires: python3-boto
BuildRequires: python3-mock
BuildRequires: python3-pytest
BuildRequires: python3-pbr >= 0.5.20
BuildRequires: python3-six

# imported by cfn_helper
Requires: python3-boto
Requires: python3-psutil
Requires: python3-six >= 1.9.0

# external commands
Requires: bzip2
Requires: coreutils
Requires: curl
Requires: gzip
Requires: python3-setuptools
Requires: shadow-utils
Requires: tar

%description
Tools required to be installed on Heat provisioned cloud instances

%prep
%autosetup -p1 -S git

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install -O1 --skip-build --root=%{buildroot}
mkdir -p %{buildroot}/%{_sharedstatedir}/%{name}

%check
%pytest

%files
%doc README.rst CONTRIBUTING.rst AUTHORS ChangeLog
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{_bindir}/cfn-*
%{python3_sitelib}/heat_cfntools*
%dir %{_sharedstatedir}/%{name}

%changelog
* Tue Jul 04 2023 Python Maint <python-maint@redhat.com> - 1.4.2-22
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 1.4.2-19
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.4.2-16
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.2-13
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.2-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.2-10
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 14 2019 Adam Williamson <awilliam@redhat.com> - 1.4.2-8
- Backport all patches to current git master (#1674322 etc.)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.2-5
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Miro Hrončok <mhroncok@redhat.com> - 1.4.2-1
- Rebuild for Python 3.6
- Updated

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 10 2015 Ryan S Brown <ryansb@redhat.com> - 1.3.0-6
- Rebuilt for dependency re-resolution

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Jul 13 2015 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-4
- Build with Python 3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 15 2015 Haïkel Guémar <hguemar@fedoraproject.org> - 1.3.0-2
- Enforce python-six >= 1.9.0 (RHBZ #1231908)

* Fri May 29 2015 Haïkel Guémar <hguemar@fedoraproject.org> - 1.3.0-1
- Upstream 1.3.0
- Cleanup spec file

* Thu Nov 06 2014 Colin Walters <walters@redhat.com> - 1.2.8-2
- Remove yum dependency, as it will not typically be installed on Atomic hosts

* Thu Aug 28 2014 Jeff Peeler <jpeeler@redhat.com> 1.2.8-1
- rebase to 1.2.8
- remove wget dependency as it's no longer required
- remove rubygems dependency as it's too big for non-ruby users

* Tue Aug 19 2014 Jeff Peeler <jpeeler@redhat.com> 1.2.7-4
- fix dependencies to include external commands (rhbz#1130964)

* Sat Jul 12 2014 Tom Callaway <spot@fedoraproject.org> 1.2.7-2
- fix license handling

* Tue Jun 24 2014 Jeff Peeler <jpeeler@redhat.com> 1.2.7
- rebase to 1.2.7

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Nov 11 2013 Jeff Peeler <jpeeler@redhat.com> 1.2.6-2
- add /var/lib/heat-cfntools directory (rhbz #1028664)

* Tue Oct 22 2013 Jeff Peeler <jpeeler@redhat.com> 1.2.6-1
- rebase to 1.2.6
- added new doc files
- bump boto version requirement
- add python-pbr buildrequire
- fixed previous changelog date

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Jeff Peeler <jpeeler@redhat.com> 1.2.3-1
- rebased to 1.2.3

* Fri Mar 22 2013 Jeff Peeler <jpeeler@redhat.com> 1.2.1-1
- Version bump to match upstream
- Added cfn-create-aws-symlinks
- Updated URL, Source
- Added psutil requires
- Changed install location from /opt to /bin

* Mon Dec 24 2012 Steve Baker <sbaker@redhat.com> 1.0-1
- initial fork of heat-jeos
