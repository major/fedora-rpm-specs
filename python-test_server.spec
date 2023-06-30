%bcond_without doc

%global modname test_server

Name:           python-%{modname}
Version:        0.0.31
Release:        19%{?dist}
Summary:        Server to test HTTP clients, written in Python

License:        MIT
URL:            https://github.com/lorien/%{modname}
Source0:        %{url}/archive/v%{version}.tar.gz#/%{modname}-%{version}.tar.gz
# improve Python 3 compatibility
Patch0:         %{url}/commit/3df9b437630789d0515ce8a9999cf97bf3b30536.patch
# https://github.com/Anorov/PySocks/issues/117
Patch10:        %{modname}-deprecated-params.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-bottle
BuildRequires:  python3-webtest

%if %{with doc}
BuildRequires:  python3-sphinx
%endif

# Tests:
BuildRequires:  python3-pytest

%?python_enable_dependency_generator

%description
%{summary}.

%package -n     python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}

%description -n python3-%{modname}
%{summary}.

%package        doc
Summary:        Documentation files for %{modname}

%description    doc
%{summary}.


%prep
%autosetup -p1 -n%{modname}-%{version}

%build
%py3_build

%if %{with doc}
# avoid WARNING: autodoc: failed to import module
echo "import sys; import os; sys.path.insert(0, os.path.abspath('..'))" >>docs/conf.py
# FIXME several other warnings from sphinx
# FIXME drop binary suffix in case python3 gets the default runtime
sphinx-build-3 -d docs/doctrees docs docs/html
rm -fv docs/html/.build*
%endif

%install
%py3_install

%check
%{__python3} -m pytest -v


%files -n python3-%{modname}
%license LICENSE
%doc README.rst CHANGELOG.md
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}-py%{python3_version}.egg-info/

%if %{with doc}
%files doc
%license LICENSE
%doc docs/html
%endif


%changelog
* Wed Jun 28 2023 Python Maint <python-maint@redhat.com> - 0.0.31-19
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.31-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.31-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Python Maint <python-maint@redhat.com> - 0.0.31-16
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.31-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 25 2021 Raphael Groner <raphgro@fedoraproject.org> - 0.0.31-14
- improve Python 3 compatibility, rhbz#1926091 

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.31-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.0.31-12
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.31-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.31-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.31-9
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.31-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.31-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.31-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.31-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.31-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 01 2018 Raphael Groner <projects.rg@smart.ms> - 0.0.31-3
- support old API for pysocks

* Sat Oct 06 2018 Raphael Groner <projects.rg@smart.ms> - 0.0.31-2
- replace python3 version macro with concrete value, currently no plan for epel7
- use binary suffix for sphinx due to weird error with mock

* Wed Oct 03 2018 Raphael Groner <projects.rg@smart.ms> - 0.0.31-1
- prepare for review
- add optional generation of documentation into subpackage
- don't use pypi tarball due to missing docs subfolder
- skip epel7 for now due to missing runtime e.g. bottle and webtest

* Fri Aug 17 2018 Miro Hrončok <mhroncok@redhat.com> - 0.0.31-0
- Initial package
