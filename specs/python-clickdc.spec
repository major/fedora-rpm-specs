Summary:        Manage click arguments using python dataclass
Name:           python-clickdc
Version:        0.1.1
Release:        %autorelease
License:        MIT
URL:            https://github.com/Kamilcuk/clickdc
Source:         %{pypi_source clickdc}
Patch:          python-clickdc-0.1.1-reqs.patch
Patch:          python-clickdc-0.1.1-click-832.patch
BuildArch:      noarch
BuildRequires:  python3-devel
%global _description %{expand:
This is a package to define click command line options from a python
dataclass.

You can define a python dataclass from dataclasses with fields that
have proper types when assigned by click parsing library. Then each
field is initialized with a option, argument, command or group from
clickdc library.}

%description %_description

%package     -n python3-clickdc
Summary:        %{summary}
%description -n python3-clickdc %_description

%pyproject_extras_subpkg -n python3-clickdc test

%prep
%autosetup -p1 -n clickdc-%{version}

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l clickdc

%check
%pyproject_check_import
%pytest

%files -n python3-clickdc -f %{pyproject_files}

%changelog
%autochangelog
