%global pypi_name acres

Name:           python-%{pypi_name}
Version:        0.4.1
Release:        %{autorelease}
Summary:        Access resources on your terms

%global forgeurl https://github.com/nipreps/acres
%global tag %{version}
%forgemeta

License:        Apache-2.0
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
This module aims to provide a simple way to access package resources
that will fit most use cases.}

%description %_description


%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%prep
%forgeautosetup -p1


%generate_buildrequires
# Allow PDM backend to determine version
export PDM_BUILD_SCM_VERSION="%{version}"
%pyproject_buildrequires


%build
# Allow PDM backend to determine version
export PDM_BUILD_SCM_VERSION="%{version}"
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -L %{pypi_name}


%check
%pytest
# Run import test in addition
%pyproject_check_import


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc CHANGELOG.md README.md
%license LICENSE


%changelog
%autochangelog
