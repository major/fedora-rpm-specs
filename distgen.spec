%global pybin %{?fedora:%{__python3}}%{!?fedora:%{__python2}}
%global pylib %{?fedora:%{python3_sitelib}}%{!?fedora:%{python2_sitelib}}
%global pypkg %{?fedora:python3}%{!?fedora:python}
%global meh_pypkg %{?fedora:%{pypkg}-}

%if 0%{?rhel} >= 8
%global pybin %__python3
%global pylib %python3_sitelib
%global pypkg python3
%global meh_pypkg python3-
%endif


Name:       distgen
Summary:    Templating system/generator for distributions
Version:    1.14
Release:    2%{?dist}
License:    GPL-2.0-or-later AND Apache-2.0
URL:        https://github.com/devexp-db/distgen
BuildArch:  noarch

Requires: %{pypkg}-jinja2
Requires: %{pypkg}-distro
Requires: %{meh_pypkg}PyYAML
Requires: %{pypkg}-six

BuildRequires: make
BuildRequires: %{pypkg}-devel
BuildRequires: %{pypkg}-distro
BuildRequires: %{pypkg}-jinja2
BuildRequires: %{meh_pypkg}pytest
%if 0%{?rhel} && 0%{?rhel} < 8
BuildRequires: %{pypkg}-mock
BuildRequires: %{pypkg}-pytest-catchlog
%endif
BuildRequires: %{meh_pypkg}PyYAML
BuildRequires: %{pypkg}-setuptools
BuildRequires: %{pypkg}-six

Source0: https://pypi.org/packages/source/d/%name/%name-%version.tar.gz

%description
Based on given template specification (configuration for template), template
file and preexisting distribution metadata generate output file.


%prep
%autosetup -p1


%build
%{pybin} setup.py build


%install
%{pybin} setup.py install --root=%{buildroot}
mkdir -p %{buildroot}%{_datadir}/distgen
mv %{buildroot}%{pylib}/distgen/{distconf,templates} %{buildroot}%{_datadir}/distgen


%check
make PYTHON=%{pybin} check


%files
%license LICENSE
%doc AUTHORS NEWS
%doc docs/
%{_bindir}/dg
%{pylib}/distgen
%{pylib}/%{name}-*.egg-info
%{_datadir}/%{name}
%{_mandir}/man1/*


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 06 2022 Zuzana Miklankova <zmiklank@redhat.com> - 1.14-1
- new upstream release, https://github.com/devexp-db/distgen/releases/tag/v1.14

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.13-2
- Rebuilt for Python 3.11

* Thu Jun 09 2022 Zuzana Miklankova <zmiklank@redhat.com> - 1.13-1
- new upstream release, https://github.com/devexp-db/distgen/releases/tag/v1.13

* Thu Apr 14 2022 Zuzana Miklankova <zmiklank@redhat.com> - 1.12-1
- new upstream release, https://github.com/devexp-db/distgen/releases/tag/v1.12

* Thu Mar 24 2022 Zuzana Miklankova <zmiklank@redhat.com> - 1.11-1
- new upstream release, https://github.com/devexp-db/distgen/releases/tag/v1.11

* Thu Jan 27 2022 Pavel Raiskup <praiskup@redhat.com> - 1.10-1
- fix FTBFS on EPEL9, new release, https://github.com/devexp-db/distgen/releases/tag/v1.10

* Wed Jan 26 2022 Pavel Raiskup <praiskup@redhat.com> - 1.9-1
- new upstream release, https://github.com/devexp-db/distgen/releases/tag/v1.9

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 08 2021 Pavel Raiskup <praiskup@redhat.com> - 1.8-1
- fix ftbfs in Fedora (rhbz#1968796)

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.7-2
- Rebuilt for Python 3.10

* Sat Feb 20 2021 Pavel Raiskup <praiskup@redhat.com> - 1.7-1
- new upstream release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 24 2020 Honza Horak <hhorak@redhat.com> - 1.6-1
- Provide F32 branched configs
  Provide CentOS 8 config

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5-2
- Rebuilt for Python 3.9

* Wed Apr 01 2020 Pavel Raiskup <praiskup@redhat.com> - 1.5-1
- provide F32 branched configs

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 24 2019 Pavel Raiskup <praiskup@redhat.com> - 1.4-1
- new upstream release (f31 configs)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3-4
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 02 2019 Pavel Raiskup <praiskup@redhat.com> - 1.3-2
- fix ftbfs on rawhide (rhbz#1705262)

* Thu Mar 21 2019 Pavel Raiskup <praiskup@redhat.com> - 1.3-1
- new upstream release, per release notes:
  https://github.com/devexp-db/distgen/releases/tag/v1.3

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 14 2018 Pavel Raiskup <praiskup@redhat.com> - 1.2-1
- latest upstream release

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1-2
- Rebuilt for Python 3.7

* Thu Apr 19 2018 Pavel Raiskup <praiskup@redhat.com> - 1.1-1
- sync with upstream spec file

* Wed Apr 18 2018 Slavek Kabrda <bkabrda@redhat.com> - 1.1-1
- update to 1.1
- update source url to conform with new PyPI urls format

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 27 2017 Slavek Kabrda <bkabrda@redhat.com> - 0.20-1
- update to 0.20

* Thu Nov 02 2017 Slavek Kabrda <bkabrda@redhat.com> - 0.19-1
- update to 0.19

* Mon Oct 30 2017 Slavek Kabrda <bkabrda@redhat.com> - 0.18-1
- update to 0.18

* Tue Oct 17 2017 Slavek Kabrda <bkabrda@redhat.com> - 0.17-1
- update to 0.17

* Mon Sep 18 2017 Slavek Kabrda <bkabrda@redhat.com> - 0.16-1
- update to 0.16

* Wed Sep 13 2017 Slavek Kabrda <bkabrda@redhat.com> - 0.15-1
- update to 0.15

* Wed Sep 06 2017 Slavek Kabrda <bkabrda@redhat.com> - 0.14-1
- update to 0.14

* Fri Aug 18 2017 Pavel Raiskup <praiskup@redhat.com> - 0.13.dev1-1
- fix build on RHEL7

* Fri Aug 18 2017 Slavek Kabrda <bkabrda@redhat.com> - 0.12.dev1-1
- new release scheme

* Tue Aug 15 2017 Pavel Raiskup <praiskup@redhat.com> - 0.11~dev-1
- multiple --spec options

* Mon Aug 14 2017 Pavel Raiskup <praiskup@redhat.com> - 0.10~dev-1
- rebase

* Thu May 19 2016 Pavel Raiskup <praiskup@redhat.com> - 0.9~dev-1
- rebase

* Sat Feb 06 2016 Pavel Raiskup <praiskup@redhat.com> - 0.8~dev-1
- rebase

* Wed Jan 27 2016 Pavel Raiskup <praiskup@redhat.com> - 0.7~dev-1
- rebase

* Fri Nov 20 2015 Pavel Raiskup <praiskup@redhat.com> - 0.6~dev-1
- rebase

* Mon Oct 26 2015 Pavel Raiskup <praiskup@redhat.com> - 0.5~dev-1
- rebase

* Thu Sep 10 2015 Pavel Raiskup <praiskup@redhat.com> - 0.4~dev-1.git33125
- rebase

* Tue Sep 01 2015 Pavel Raiskup <praiskup@redhat.com> - 0.3~dev-1.git76d41
- rebase

* Wed May 20 2015 Pavel Raiskup <praiskup@redhat.com> - 0.2~dev-1.git32635
- new release, enable testsuite

* Mon May 11 2015 Pavel Raiskup <praiskup@redhat.com> - 0.1~dev-4.gitf6fc9
- fixes to allow build of PostgreSQL Docker image correctly

* Mon May 11 2015 Pavel Raiskup <praiskup@redhat.com> - 0.1~dev-3.git97392
- bump version (better example)

* Sun May 10 2015 Pavel Raiskup <praiskup@redhat.com> - 0.1~dev-2.gitdefcd
- Add 'dg' option parser

* Sun May 10 2015 Pavel Raiskup <praiskup@redhat.com> - 0.1~dev-1.git64bbe
- Initial packaging
