%global pypi_name pyhaversion
%global pkg_name haversion

Name:           python-%{pkg_name}
Version:        24.6.1
Release:        %autorelease
Summary:        Python module to get the version number of Home Assistant

License:        MIT
URL:            https://github.com/ludeeus/pyhaversion
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
A Python module to get the version number of Home Assistant.

%package -n     python3-%{pkg_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-aresponses

%description -n python3-%{pkg_name}
A Python module to get the version number of Home Assistant.

%prep
%autosetup -n %{pypi_name}-%{version}
sed -i -e 's/"0"/"%{version}"/g' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest -v tests -k "not test_stable_version and not test_etag" 

%files -n python3-%{pkg_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
