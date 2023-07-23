%global pypi_name jaraco.collections
# Disable docs build for now
# sphinx deps arn't resolving properly
%bcond_with docs

Name:           python-jaraco-collections
Version:        3.0.0
Release:        15%{?dist}
Summary:        Collection objects similar to those in stdlib by jaraco

License:        MIT
URL:            https://github.com/jaraco/jaraco.collections
Source0:        %{pypi_source}
BuildArch:      noarch
 
BuildRequires:  python3-devel
%generate_buildrequires
%pyproject_buildrequires

%if %{with tests}
# test requirements
BuildRequires:  python3dist(jaraco-text)
BuildRequires:  python3dist(pytest) >= 3.5
BuildRequires:  python3dist(pytest-black-multipy)
BuildRequires:  python3dist(pytest-checkdocs) >= 1.2.3
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-flake8)
BuildRequires:  python3dist(rst-linker) >= 1.9
BuildRequires:  python3dist(six) >= 1.7.0
%endif

%description
%{summary}

%package -n     python3-jaraco-collections
Summary:        %{summary}
 
Requires:       python3-jaraco

# The package name was changed. Obsolete the previous
# name to provide a clean upgrade path.
# Remove in Fedora >= 36
Obsoletes:      python3-jaraco.collections < 3.0.0-3

%description -n python3-jaraco-collections
%{summary}

%package -n python-jaraco-collections-doc
Summary:        jaraco.collections documentation

# The package name was changed. Obsolete the previous
# name to provide a clean upgrade path.
# Remove in Fedora >= 36
Obsoletes:      python-jaraco.collections-doc < 3.0.0-3

%description -n python-jaraco-collections-doc
Documentation for jaraco.collections

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%pyproject_wheel
%if %{with docs}
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%if %{with tests}
%check
%pytest
%endif

%install
%pyproject_install

%files -n python3-jaraco-collections
%license LICENSE
%doc README.rst
# These excludes are provided by python3-jaraco
%pycached %exclude %{python3_sitelib}/jaraco/__init__.py
%pycached %{python3_sitelib}/jaraco/collections.py
%{python3_sitelib}/jaraco.collections-%{version}.dist-info/

%if %{with docs}
%files -n python-jaraco-collections-doc
%doc html
%license LICENSE
%endif

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 3.0.0-14
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 3.0.0-11
- Rebuilt for Python 3.11

* Thu Apr 07 2022 Dan Radez - 3.0.0-10
- Switched to pyproject macros
- disabled docs. Sphinx can't resolve deps properly
- Fixes: rhbz#2069540

* Wed Feb 09 2022 Dan Radez <dradez@redhat.com> - 3.2.1-6
- Don't delete egginfo

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.0.0-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Charalampos Stratakis <cstratak@redhat.com> - 3.0.0-3
- Fix a file conflict with python3-jaraco
- Rename the binary rpms to conform to the packaging guidelines
- Misc packaging fixes

* Fri Jun 19 2020 Matthias Runge <mrunge@redhat.com> - 3.0.0-2
- review feedback: fix license, remove (wrong) conflict

* Fri Mar 13 2020 Matthias Runge <mrunge@redhat.com> - 3.0.0-1
- Initial package.
