%global pypi_name sphinx-notfound-page
%global srcname sphinx_notfound_page
%global importname notfound
%global project_owner readthedocs
%global github_name sphinx-notfound-page
%global desc Create a custom 404 page with absolute URLs hardcoded

%if 0%{?fedora} > 30 || 0%{?rhel} > 7
%bcond_with python2
%else
%bcond_without python2
%endif

Name:           python-%{pypi_name}
Version:        0.7.1
Release:        7%{?dist}
Summary:        Create a custom 404 page with absolute URLs hardcoded

License:        MIT
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://github.com/%{project_owner}/%{github_name}/archive/%{version}.tar.gz

# Ensure compatibility with Sphinx 6+ - proposed upstream
# https://github.com/readthedocs/sphinx-notfound-page/pull/218/
Patch:          dont_test_for_jquery_presence_with_sphinx_6.patch

BuildArch:      noarch

%description
%desc

%if %{with python2}
%package -n python2-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-sphinx
BuildRequires:  python2-pytest
Requires:       python2-setuptools
Requires:       python2-sphinx
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
%desc
%endif

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python3-pytest
Requires:       python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-sphinx
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
%desc


%prep
%autosetup -n %{pypi_name}-%{version} -p1

%build
%if %{with python2}
%py2_build
%endif
%py3_build


%install
%if %{with python2}
%py2_install
%endif

%py3_install

%check
%if %{with python2}
PYTHONPATH="$(pwd)" py.test-%{python2_version} -v .
%endif
PYTHONPATH="$(pwd)" py.test-%{python3_version} -v .

%if %{with python2}
%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst CHANGELOG.rst docs
%{python2_sitelib}/%{srcname}-%{version}*-py%{python2_version}.egg-info/
%{python2_sitelib}/%{importname}/
%endif

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst CHANGELOG.rst docs
%{python3_sitelib}/%{srcname}-%{version}*-py%{python3_version}.egg-info/
%{python3_sitelib}/%{importname}/

%changelog
* Fri Apr 14 2023 Karolina Surma <ksurma@redhat.com> - 0.7.1-7
- Ensure compatibility with Sphinx 6+
Resolves: rhbz#2180484

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.7.1-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Karolina Surma <ksurma@redhat.com> - 0.7.1-1
- Update to new upstream version 0.7.1

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.6-5
- Rebuilt for Python 3.10

* Mon Mar  8 2021 Tim Landscheidt <tim@tim-landscheidt.de> - 0.6-4
- Remove obsolete requirements for %%post/%%postun scriptlets

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Charalampos Stratakis <cstratak@redhat.com> - 0.6-2
- Fix compatibility with Sphinx 3.4

* Tue Jan 12 2021 Charalampos Stratakis <cstratak@redhat.com> - 0.6-1
- Update to version 0.6

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4-8
- Rebuilt for Python 3.9

* Tue Apr 21 2020 Charalampos Stratakis <cstratak@redhat.com> - 0.4-7
- Fix test failures with Sphinx 3 (rhbz#1823521)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 13 2019 Kevin Fenzi <kevin@scrye.com> - 0.4-2
- Use bcond for python2 support.

* Wed Jul 03 2019 Kevin Fenzi <kevin@scrye.com> - 0.4-1
- Initial version for Fedora.
