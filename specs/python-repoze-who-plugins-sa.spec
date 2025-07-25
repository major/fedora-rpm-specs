Name:           python-repoze-who-plugins-sa
Version:        1.0.1
Release:        49.20160106gite1a36c5%{?dist}
Summary:        repoze.who SQLAlchemy plugin

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://code.gustavonarea.net/repoze.who.plugins.sa
# Git snapshot to get python3 support.  Generate this way:
# git clone https://github.com/repoze/repoze.who-sqlalchemy.git
# cd repoze.who-sqlalchemy
# patch -p1 < ../repoze-who-plugins-sa-sdist.patch
# python3 setup.py sdist
# tarball will be in the dist/ subdirectory
Source0: repoze.who.plugins.sa-%{version}.tar.gz
#Source0:        https://pypi.python.org/packages/source/r/repoze.who.plugins.sa/repoze.who.plugins.sa-%%{version}.tar.gz
# This patch is to be applied when generating the tarball.  It includes the
# test directoriy so we can run the test suite
# https://github.com/repoze/repoze.who-sqlalchemy/pull/6
#Patch100: repoze-who-plugins-sa-sdist.patch
Patch101: repoze-who-plugins-sa-requires.patch
BuildArch:      noarch

BuildRequires: python3-devel
BuildRequires: python3-repoze-who
BuildRequires: python3-sqlalchemy
BuildRequires: python3-coverage
BuildRequires: python3-pytest

%global _description\
This plugin provides one repoze.who authenticator which works with SQLAlchemy\
or Elixir-based models.\


%description %_description

%package -n python3-repoze-who-plugins-sa
Summary: repoze.who SQLAlchemy plugin

%description -n python3-repoze-who-plugins-sa
This plugin provides one repoze.who authenticator which works with SQLAlchemy
based models on python3


%prep
%setup -q -n repoze.who.plugins.sa-%{version}
%patch -P 101 -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files repoze


%check
%pyproject_check_import
# Tests not ported to Python3.
%if 0
%pytest
%endif


%files -n python3-repoze-who-plugins-sa -f %{pyproject_files}
%doc README.txt
%{python3_sitelib}/repoze.who.plugins.sa-%{version}-py%{python3_version}-nspkg.pth
%exclude %{python3_sitelib}/tests


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-49.20160106gite1a36c5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jul 14 2025 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.0.1-48.20160106gite1a36c5
- Migrate from py_build/py_install to pyproject macros (bz#2378162)

* Sat Jun 07 2025 Python Maint <python-maint@redhat.com> - 1.0.1-47.20160106gite1a36c5
- Rebuilt for Python 3.14

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-46.20160106gite1a36c5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.1-45.20160106gite1a36c5
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-44.20160106gite1a36c5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 16 2024 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.0.1-43.20160106gite1a36c5
- Rebuild for python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-42.20160106gite1a36c5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-41.20160106gite1a36c5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-40.20160106gite1a36c5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 1.0.1-39.20160106gite1a36c5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-38.20160106gite1a36c5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 18 2023 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.0.1-37.20160106gite1a36c5
- Do not use glob on python sitelib

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-36.20160106gite1a36c5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.0.1-35.20160106gite1a36c5
- Rebuilt for Python 3.11

* Thu Apr 21 2022 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.0.1-34.20160106gite1a36c5
- Switch from deprecated nose to pytest

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-33.20160106gite1a36c5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-32.20160106gite1a36c5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.1-31.20160106gite1a36c5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-30.20160106gite1a36c5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-29.20160106gite1a36c5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-28.20160106gite1a36c5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-27.20160106gite1a36c5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-26.20160106gite1a36c5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-25.20160106gite1a36c5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-24.20160106gite1a36c5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 13 2019 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.0.1-23.20160106gite1a36c5
- Changed dependency on repoze.who 2.1b1 to 2.1.
  Beta versions are not relevant.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-22.20160106gite1a36c5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 31 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-21.20160106gite1a36c5
- Subpackage python2-repoze-who-plugins-sa has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-20.20160106gite1a36c5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-19.20160106gite1a36c5
- Rebuilt for Python 3.7

* Wed Feb 14 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.1-18.20160106gite1a36c5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-17.20160106gite1a36c5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.1-16.20160106gite1a36c5
- Python 2 binary package renamed to python2-repoze-who-plugins-sa
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-15.20160106gite1a36c5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Tom Callaway <spot@fedoraproject.org> - 1.0.1-14.20160106gite1a36c5
- disable tests, not ported to Python 3 properly

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-13.20160106gite1a36c5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-12.20160106gite1a36c5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-11.20160106gite1a36c5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10.20160106gite1a36c5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan  7 2016 Toshio Kuratomi <toshio@fedoraproject.org> - 1.0.1-9.20160106gite1a36c5
- Really build the python3 subpackage

* Wed Jan  6 2016 Toshio Kuratomi <toshio@fedoraproject.org> - 1.0.1-8.20160106gite1a36c5
- Update to a git snapshot
- Build python3 subppackage

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Dec 06 2013 Pierre-Yves Chibon <pingou@pingoured>fr - 1.0.1-5
- Change BR from python-setuptools-devel to python-setuptools
  See https://fedoraproject.org/wiki/Changes/Remove_Python-setuptools-devel

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 06 2012 Luke Macken <lmacken@redhat.com> - 1.0.1-1
- 1.0.1 update
- Remove BR on python-elixir, which was orphaned

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 16 2011 Luke Macken <lmacken@redhat.com> - 1.0-1
- Update to 1.0 final (#701602)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.7.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.0-0.6.rc2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed May 05 2010 Luke Macken <lmacken@redhat.com> - 1.0-0.4.rc2
- Update to 1.0 rc2
- Enable the test suite during %%check

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.4.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 20 2009 Luke Macken <lmacken@redhat.com> - 1.0-0.3.rc1
- Remove the test suite, since it conflicts with other packages (#512759)

* Thu May 21 2009 Luke Macken <lmacken@redhat.com> - 1.0-0.2.rc1
- Update to 1.0rc1
- Add python-elixir, python-sqlalchemy, python-coverage, python-nose,
  and python-repoze-who to the BuildRequires
- Remove the setuptools patch

* Tue Jan 06 2009 Luke Macken <lmacken@redhat.com> - 1.0-0.1.b2.r2909
- Initial package for Fedora
