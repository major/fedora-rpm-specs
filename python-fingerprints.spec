%global pypi_name fingerprints

Name:           python-%{pypi_name}
Version:        1.2.3
Release:        %autorelease
Summary:        Compare the names of companies and people by applying strong normalization

License:        MIT
URL:            https://github.com/alephdata/fingerprints
Source:         %url/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pyicu)

%global common_description %{expand:
This library helps with the generation of fingerprints for entity data. A
fingerprint in this context is understood as a simplified entity identifier,
derived from it's name or address and used for cross-referencing of entity
across different datasets.}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}
Recommends:     python3dist(pyicu)

%description -n python3-%{pypi_name} %{common_description}

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
