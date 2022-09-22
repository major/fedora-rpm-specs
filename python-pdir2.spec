# what it's called on pypi
%global srcname pdir2
# what it's imported as
%global libname pdir
# name of egg info directory
%global eggname pdir2
# package name fragment
%global pkgname pdir2

%global common_description %{expand:
An improved version of dir() with better output.  Attributes are grouped by
types/functionalities, with beautiful colors.  Supports ipython, ptpython,
bpython, and Jupyter Notebook.}

%if (%{defined fedora} && 0%{?fedora} < 30) || (%{defined rhel} && 0%{?rhel} < 8)
%bcond_without  python2
%bcond_without  python2_tests
%endif

%bcond_without  python3
%if %{defined fedora}
# missing python36-pandas in EPEL
%bcond_without  python3_tests
%endif

# Upstream tag doesn't match the version
%global tag 0.3.1


Name:           python-%{pkgname}
Version:        0.3.1.post2
Release:        16%{?dist}
Summary:        Pretty dir() printing with joy
License:        MIT
URL:            https://github.com/laike9m/pdir2
# PyPI tarball doesn't have tests
Source0:        %{url}/archive/v%{tag}/%{srcname}-%{version}.tar.gz
# https://github.com/laike9m/pdir2/issues/31
Patch0:         remove-environment-markers.patch
# Patch to add support for pytest 4 and 5.  This is fixed upstream in the
# master branch in a way that drops support for pytest 2 (the version in EL7).
# This patch is similar to the upstream fixes but retains pytest 2
# compatibility.
# https://github.com/laike9m/pdir2/commit/787195841c86980562c81fc81df65d4096a73f09#diff-e2b79530c0a804d26dfec15c6f85f757
# https://github.com/laike9m/pdir2/commit/a85a7e2fc0b60b865039d8b75c5268be5ada99c3#diff-c3d931c13b4769887b493d82966b7771
# https://github.com/laike9m/pdir2/commit/ad9fe01639bc927fc0d721469254e6fbe78fea6a
Patch1:         pdir2-0001-pytest-compat.patch
# Patch to fix Python 3.9 compatibility.  Backported from the upstream master
# branch.
# https://github.com/laike9m/pdir2/commit/5d44803dca3c24eba44aac373a8e06ebacea59a5
Patch2:         pdir2-0002-fix-deprecated-imports-from-collections.patch
Patch3:         pdir2-0003-add-py311-getstate.patch
BuildArch:      noarch


%description %{common_description}


%if %{with python2}
%package -n python2-%{pkgname}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%if %{with python2_tests}
BuildRequires:  python2-pytest >= 2.4
BuildRequires:  python2-pandas
BuildRequires:  python2-enum34
%endif
Requires:       python2-enum34
%{?python_provide:%python_provide python2-%{pkgname}}


%description -n python2-%{pkgname} %{common_description}
%endif


%if %{with python3}
%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%if %{with python3_tests}
BuildRequires:  python%{python3_pkgversion}-pytest >= 2.4
BuildRequires:  python%{python3_pkgversion}-pandas
%endif
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkgname}}


%description -n python%{python3_pkgversion}-%{pkgname} %{common_description}
%endif


%prep
%autosetup -n %{srcname}-%{tag} -p 1


%build
%{?with_python2:%py2_build}
%{?with_python3:%py3_build}


%install
%{?with_python2:%py2_install}
%{?with_python3:%py3_install}


%check
%{?with_python2_tests:PYTHONPATH=%{buildroot}%{python2_sitelib} py.test-%{python2_version} --verbose}
%{?with_python3_tests:PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} --verbose}


%if %{with python2}
%files -n python2-%{pkgname}
%license LICENSE
%doc README.md HISTORY.md
%{python2_sitelib}/%{libname}
%{python2_sitelib}/%{eggname}-%{version}-py%{python2_version}.egg-info
%endif


%if %{with python3}
%files -n python%{python3_pkgversion}-%{pkgname}
%license LICENSE
%doc README.md HISTORY.md
%{python3_sitelib}/%{libname}
%{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info
%endif


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1.post2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Simon de Vlieger <cmdr@supakeen.com> - 0.3.1.post2-15
- Add patch for Python 3.11 __getstate__

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.3.1.post2-14
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1.post2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1.post2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.1.post2-11
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1.post2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1.post2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.1.post2-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1.post2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Carl George <carl@george.computer> - 0.3.1.post2-6
- Add patch2 for Python 3.9 compatiblity rhbz#1794276

* Thu Jan 02 2020 Carl George <carl@george.computer> - 0.3.1.post2-5
- Update patch1 to add support for pytest 5

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.1.post2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.1.post2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1.post2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 03 2019 Carl George <carl@george.computer> - 0.3.1.post2-1
- Latest upstream
- Drop python3_other subpackage
- Disable python2 subpackage on EL8
- Run python2 tests on EL7
- Add patch for pytest 4 compatibility rhbz#1706163

* Fri Mar 08 2019 Troy Dawson <tdawson@redhat.com> - 0.3.0-6
- Rebuilt to change main python from 3.4 to 3.6

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 21 2018 Carl George <carl@george.computer> - 0.3.0-5
- Disable python2 subpackage on F30+
- Enable python36 subpackage on EPEL7

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Carl George <carl@george.computer> - 0.3.0-3
- Add patch1 to mark test_pdir_class as an expected fail
- Share doc and license dir between subpackages
- Update URL

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-2
- Rebuilt for Python 3.7

* Wed Feb 28 2018 Carl George <carl@george.computer> - 0.3.0-1
- Latest upstream

* Tue Feb 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.2.2-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Oct 20 2017 Carl George <carl@george.computer> - 0.2.2-1
- Latest upstream
- Remove environment markers from setup.py to allow using older setuptools
- EPEL compatibility

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 05 2017 Carl George <carl@george.computer> - 0.2.1-1
- Latest upstream
- Remove patch100 and patch101

* Thu Jun 29 2017 Carl George <carl@george.computer> - 0.2.0-1
- Initial package
