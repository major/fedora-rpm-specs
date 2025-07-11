%global pkgname spdx-license-list
%global srcname spdx_license_list

Name:           python-%{pkgname}
Version:        3.27.0
Release:        %autorelease
Summary:        SPDX License List as a Python dictionary
License:        MIT
URL:            https://pypi.org/project/spdx-license-list/
Source:         %{pypi_source %{srcname}}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Provides the SPDX License List as a Python dictionary.}

%description %_description

%package -n python3-%{pkgname}
Summary:        %{summary}

%description -n python3-%{pkgname} %_description


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -L %{srcname}


%check
%pyproject_check_import


%files -n python3-%{pkgname} -f %{pyproject_files}
%license LICENSE
%doc README.md


%changelog
%autochangelog
