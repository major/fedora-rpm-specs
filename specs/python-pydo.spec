%global srcname pydo

Name: python-%{srcname}
Summary: PyDo - DigitalOcean python library
Version: 0.24.0
Release: 3%{?dist}

License: ASL 2.0

Url: https://github.com/digitalocean/%{srcname}
Source:         %{url}/archive/v%{version}/pydo-%{version}.tar.gz

BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3dist(poetry-core)
# Test dependencies
BuildRequires:  python3dist(aioresponses)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(responses)

%global _description %{expand:
Official DigitalOcean Python Client based on the DO OpenAPIv3 specification.}
%description %_description

%package -n python3-pydo
Summary: %{summary}
%description -n python3-pydo %_description


%prep
%autosetup -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
%pyproject_check_import
%pytest -rA --tb=short tests/mocked/.


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%license LICENSE


%changelog
* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild


* Wed Jul 30 2025 Alex Manson <dev@neurowinter.com>
- Inital release of 0.13.0
