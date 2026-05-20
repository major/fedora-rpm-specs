Name:           python-uncalled-for
Version:        0.3.2
Release:        %autorelease
Summary:        Async dependency injection for Python functions

License:        MIT
URL:            https://github.com/chrisguidry/uncalled-for
Source:         %{pypi_source uncalled_for}

# Remove some unrecognized arguments for pytest (coverage, xdist, etc...)
Patch:          remove-pytest-unrecognized-arguments.diff

BuildArch:      noarch

# Test dependencies
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio

%global _description %{expand:
Async dependency injection for Python functions.

Declare what your function needs as parameter defaults. They show up resolved
when the function runs. No ceremony, no container, no configuration.}

%description %_description

%package -n     python3-uncalled-for
Summary:        %{summary}

%description -n python3-uncalled-for %_description


%prep
%autosetup -p1 -n uncalled_for-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l uncalled_for


%check
%pyproject_check_import
%pytest


%files -n python3-uncalled-for -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
