%global pypi_name presets
%global pypi_version 0.1.3

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        4%{?dist}
Summary:        A python module to manipulate default parameters of a module's functions

License:        ISC
URL:            http://github.com/bmcfee/presets
Source0:        https://github.com/bmcfee/presets/archive/%{version}/presets-%{version}.tar.gz
# https://github.com/bmcfee/presets/pull/16
Patch0:         importlib.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)

%description
A python module to manipulate default parameters of a module's functions

%package -n     python3-%{pypi_name}
Summary:        %{summary}

Requires:       python3dist(numpydoc)
Requires:       python3dist(six)
%description -n python3-%{pypi_name}
A python module to manipulate default parameters of a module's functions


%prep
%autosetup -n %{pypi_name}-%{pypi_version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name} -l
sed -e '1d' -i %{buildroot}%{python3_sitelib}/presets/__init__.py
sed -e '1d' -i %{buildroot}%{python3_sitelib}/presets/version.py

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Oct 31 2024 Gwyn Ciesla <gwync@protonmail.com> - 0.1.3-3
- Additional fixes`

* Wed Oct 30 2024 Gwyn Ciesla <gwync@protonmail.com> - 0.1.3-2
- Review fixes

* Wed Dec 21 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.1.3-1
- Initial package.
