%global pypi_name jaraco.text
%global pkg_name jaraco-text

# there's an issue with sphinx dep resolution
# turining off docs build for now
%bcond_with docs
# Not all test dependencies are available yet
%bcond_with tests

Name:           python-%{pkg_name}
Version:        3.12.0
Release:        1%{?dist}
Summary:        Module for text manipulation

License:        MIT
URL:            https://github.com/jaraco/jaraco.text
Source0:        %{pypi_source}
BuildArch:      noarch
 
BuildRequires:  python3-devel
%generate_buildrequires
%pyproject_buildrequires

%if %{with tests}
BuildRequires: python3dist(pytest)
BuildRequires: python3dist(pytest-checkdocs)
BuildRequires: python3dist(pytest-flake8)
BuildRequires: python3dist(pytest-black-multipy)
BuildRequires: python3dist(pytest-cov)
# with tests
%endif

%description
%{summary}

%package -n     python3-%{pkg_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pkg_name}}

%description -n python3-%{pkg_name}
%{summary}

%package -n python-%{pkg_name}-doc
Summary:        jaraco.text documentation
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(rst-linker) >= 1.9
BuildRequires:  python3dist(jaraco-packaging)

%description -n python-%{pkg_name}-doc
Documentation for jaraco.text

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%pyproject_wheel

%if %{with docs}
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
# with docs
%endif

%install
%pyproject_install
install jaraco/text/Lorem\ ipsum.txt \
    %{buildroot}%{python3_sitelib}/jaraco/text/

%if 0%{?with_tests}
%check
%pytest
# with tests
%endif

%files -n python3-%{pkg_name}
%license LICENSE
%doc README.rst
# These excludes are provided by python3-jaraco
%{python3_sitelib}/jaraco/text/
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info

%if %{with docs}
%files -n python-%{pkg_name}-doc
%doc html
%license LICENSE
# with docs
%endif

%changelog
* Wed Nov 29 2023 Dan Radez <dradez@redhat.com> - 3.12.0-1
- update to upstream 3.12 rhbz#2251804

* Wed Aug 16 2023 Dan Radez <dradez@redhat.com> - 3.11.1-1
- update to upstream 3.11 rhbz#2232234

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 3.2.0-12
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 3.2.0-9
- Rebuilt for Python 3.11

* Wed May 04 2022 Tomáš Hrnčiar <thrnciar@redhat.com> - 3.2.0-8
- Backport patch to fix DeprecationWarning

* Thu Apr 07 2022 Dan Radez - 3.2.0-7
- Switched to pyproject macros
- disabled docs. Sphinx can't resolve deps properly
- Fixes: rhbz#2069541

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.2.0-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Mar 13 2020 Matthias Runge <mrunge@redhat.com> - 3.2.0-1
- Initial package.
