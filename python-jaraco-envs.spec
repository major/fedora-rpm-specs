%global pypi_name jaraco.envs
%global pkg_name jaraco-envs

# Not all test dependencies are available yet
%bcond_with tests
%bcond_with docs

Name:           python-%{pkg_name}
Version:        2.4.0
Release:        4%{?dist}
Summary:        Classes for orchestrating Python (virtual) environments

License:        MIT
URL:            https://github.com/jaraco/jaraco.envs
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires:  python3-devel


%if %{with tests}
BuildRequires:       python3dist(pytest)
BuildRequires:       python3dist(pytest-cov)
BuildRequires:       python3-path
BuildRequires:       python3dist(pytest-checkdocs)
BuildRequires:       python3dist(pytest-flake8)
BuildRequires:       python3dist(pytest-black-multipy)
%endif # with tests

%generate_buildrequires
%pyproject_buildrequires

%description
Classes for orchestrating Python (virtual) environments.

%package -n     python3-%{pkg_name}
Summary:        %{summary}

Requires:       python3-path
Requires:       python3-jaraco

%description -n python3-%{pkg_name}
Classes for orchestrating Python (virtual) environments.

%if %{with docs}
%package -n python-%{pkg_name}-doc
Summary:        jaraco-envs documentation
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(jaraco-packaging)
BuildRequires:  python3dist(rst-linker)

%description -n python-%{pkg_name}-doc
Documentation for jaraco-envs
%endif # with docs

%prep
%autosetup -n jaraco.envs-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Remove path dependency as to not
# automatically generate requires metadata.
# path does not provide the python3dist namespace
sed -i '/path/d' setup.cfg

%build
%pyproject_wheel
%if %{with docs}
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif # with docs

%install
%pyproject_install
%if %{with tests}
%check
%pytest
%endif # with tests

%files -n python3-%{pkg_name}
%license LICENSE
%doc README.rst
# These excludes are provided by python3-jaraco
%{python3_sitelib}/jaraco/envs*
%{python3_sitelib}/jaraco/__pycache__/envs*
%{python3_sitelib}/jaraco.envs-%{version}.dist-info

%if %{with docs}
%files -n python-%{pkg_name}-doc
%doc html
%license LICENSE
%endif # with docs

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 2.4.0-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Sep 19 2022 Charalampos Stratakis <cstratak@redhat.com> - 2.4.0-1
- Update to 2.4.0
Resolves: rhbz#2080532

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.3.0-2
- Rebuilt for Python 3.11

* Wed Mar 16 2022 Charalampos Stratakis <cstratak@redhat.com> - 2.3.0-1
- Update to 2.3.0
Resolves: rhbz#2059021

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 08 2021 Tomáš Hrnčiar <thrnciar@redhat.com> - 2.2.0-1
- Update to 2.2.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.0-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Charalampos Stratakis <cstratak@redhat.com> - 2.0.0-2
- Packaging fixes

* Tue Jun 02 2020 Charalampos Stratakis <cstratak@redhat.com> - 2.0.0-1
- Initial package.