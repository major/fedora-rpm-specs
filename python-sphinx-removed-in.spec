%global pypi_name sphinx-removed-in

Name:           python-%{pypi_name}
Version:        0.2.1
Release:        15%{?dist}
Summary:        versionremoved and removed-in directives for Sphinx
License:        BSD
URL:            https://github.com/MrSenko/sphinx-removed-in
Source:         %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

# Drop the dependency on deprecated sphinx-testing
# From https://github.com/MrSenko/sphinx-removed-in/pull/9
Patch:          %{url}/commit/52457154d7.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  python3-pytest

%description
This is a Sphinx extension which recognizes the versionremoved and removed-in
directives.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This is a Sphinx extension which recognizes the versionremoved and removed-in
directives.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install
# https://github.com/MrSenko/sphinx-removed-in/pull/10
rm -rf %{buildroot}%{python3_sitelib}/tests

%check
%pytest

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/sphinx_removed_in/
%{python3_sitelib}/sphinx_removed_in-%{version}-py%{python3_version}.egg-info/

%changelog
* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.2.1-13
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.2.1-10
- Rebuilt for Python 3.11

* Thu Feb 17 2022 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-9
- Drop the dependency on deprecated sphinx-testing

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Python Maint <python-maint@redhat.com> - 0.2.1-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Ken Dreyer <kdreyer@redhat.com> - 0.2.1-1
- Update to 0.2.1

* Fri Nov 08 2019 Ken Dreyer <kdreyer@redhat.com> 0.2.0-1
- Update to 0.2.0 (rhbz#1697060)
- Drop upstreamed patch

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.3-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.3-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 12 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.3-1
- Initial package
