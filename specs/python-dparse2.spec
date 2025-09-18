%global pypi_name dparse2

Name:           python-%{pypi_name}
Version:        0.7.0
Release:        %autorelease
Summary:        Parser for Python dependency files

License:        MIT
URL:            https://github.com/nexB/dparse2
Source:         %url/archive/%{version}/%{pypi_name}-%{version}.tar.gz
# https://github.com/aboutcode-org/dparse2/pull/7
Patch:          0001-Depends-on-tomllib-instead-of-deprecated-toml.patch
# Update project references
# https://github.com/aboutcode-org/dparse2/commit/9b6bd1c223ca5a874c6dcf96cad8fe4c47b0bf2a
Patch:          0001-Update_link_references_of_ownership_from_nexB_to_aboutcode-org.patch

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
