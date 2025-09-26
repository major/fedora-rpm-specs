%global pypi_name pydepsdev

Name:           python-%{pypi_name}
Version:        0.2.1
Release:        %autorelease
Summary:        Python library for interacting with Open Source Insights API (deps.dev)

License:        Apache-2.0
URL:            https://github.com/eclipseo/pydepsdev
Source:         %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global common_description %{expand:
A Python library for interacting with Open Source Insights API (deps.dev).
Easily fetch package, version, and project data from the API.}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{common_description}

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files %{pypi_name}

%check
%tox

%files -n python3-pydepsdev -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
