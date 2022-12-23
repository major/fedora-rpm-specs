%bcond_without tests
%bcond_with docs

%global pypi_name earthpy

%global _description %{expand:
EarthPy makes it easier to plot and manipulate spatial data in Python.}

Name:           python-%{pypi_name}
Version:        0.9.4
Release:        5%{?dist}
Summary:        A package built to support working with spatial data

License:        BSD
URL:            https://github.com/earthlab/earthpy
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

#For tests
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov

#For documentation
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(sphinx-gallery)

#Main dependencies
BuildRequires:  python3dist(geopandas)
BuildRequires:  python3dist(matplotlib)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(rasterio)
BuildRequires:  python3dist(scikit-image)
BuildRequires:  python3dist(requests)

%description -n python3-%{pypi_name} %_description

%if %{with docs}
%package doc
Summary:        %{summary}

%description doc
Documentation for %{name}.
%endif

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

#Some documents are downloaded from the internet during the build.
%if %{with docs}
# Generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs/ html
# Remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%py3_install

%check
%if %{with tests}
# Disable network tests
%pytest -k 'not test_io'
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md paper.md examples/ CHANGELOG.rst
%doc CODE_OF_CONDUCT.rst CONTRIBUTING.rst CONTRIBUTORS.rst
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pypi_name}

%if %{with docs}
%files -n python-%{pypi_name}-doc
%license LICENSE
%doc html/
%endif

%changelog
* Mon Dec 19 2022 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.9.4-5
- Drop support for i686

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 Python Maint <python-maint@redhat.com> - 0.9.4-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 7 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.9.4-1
- Update to the latest upstream's release

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9.2-3
- Rebuilt for Python 3.10

* Fri May 21 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.9.2-2
- Install additional docs

* Sat May 15 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.9.2-1
- Initial package
