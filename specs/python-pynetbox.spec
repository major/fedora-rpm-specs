%global pypi_name pynetbox

Name:           python-%{pypi_name}
Version:        7.6.1
Release:        %autorelease
Summary:        Python API client library for Netbox

License:        Apache-2.0
URL:            https://github.com/netbox-community/pynetbox
Source:         %{pypi_source}

BuildArch:      noarch

%global _description \
%{summary}.

%description %{_description}

%package     -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%description -n python3-%{pypi_name} %{_description}

%prep
%autosetup -n %{pypi_name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest -vv tests/test_*.py tests/unit

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGELOG.md

%changelog
%autochangelog
