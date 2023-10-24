%global pypi_name dparse2

Name:           python-%{pypi_name}
Version:        0.7.0
Release:        %autorelease
Summary:        Parser for Python dependency files

License:        MIT
URL:            https://github.com/nexB/dparse2
Source:         %url/archive/%{version}/%{pypi_name}-%{version}.tar.gz
Patch:          0001-Depends-on-tomllib-instead-of-deprecated-toml.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global common_description %{expand:
A parser for Python dependency files.}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}

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
%doc CONTRIBUTING.rst README.rst

%changelog
%autochangelog
