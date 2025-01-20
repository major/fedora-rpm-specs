%global pypi_name types-mock
%global pypi_version 5.1.0.20240425

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        2%{?dist}
Summary:        Typing stubs for mock

License:        Apache-2.0
URL:            https://github.com/python/typeshed
Source0:        %{pypi_source}
Source1:        https://raw.githubusercontent.com/python/typeshed/main/LICENSE
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%global _description %{expand:
This is a PEP 561 type stub package for the mock package. It can be used by
type-checking tools like mypy, pyright, pytype, PyCharm, etc. to check code
that uses mock.}

%description %{_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{_description}


%prep
%autosetup -n %{pypi_name}-%{pypi_version}
rm -rf %{pypi_name}.egg-info
cp %{SOURCE1} LICENSE

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l mock-stubs

%files -n python3-%{pypi_name}
%{python3_sitelib}/mock-stubs
%{python3_sitelib}/types_mock-%{version}.dist-info

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0.20240425-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 14 2024 Paul Pfeister <code@pfeister.dev> - 5.1.0.20240425-1
- Initial package.