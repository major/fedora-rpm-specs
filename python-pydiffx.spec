Name:           python-pydiffx
Version:        1.1
Release:        1%{?dist}
Summary:        Python implementation of the DiffX specification
License:        MIT
URL:            https://diffx.org/pydiffx/
Source:         %{pypi_source pydiffx}

BuildArch:      noarch

BuildRequires:  python3-devel

# https://github.com/beanbaginc/diffx/pull/2
Patch:          add_requirements.patch

%global _description %{expand:
DiffX is a proposed specification for a structured version of Unified
Diffsthat contains metadata, standardized parsing, multi-commit diffs, and
binary diffs, in a format compatible with existing diff parsers.

This module is a reference implementation designed to make it easy to read
and write DiffX files in any Python application.}

%description %_description


%package -n python3-pydiffx
Summary:        %{summary}


%description -n python3-pydiffx %_description


%prep
%autosetup -n pydiffx-%{version}


%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files pydiffx


%check
%pytest


%files -n python3-pydiffx -f %{pyproject_files}
%doc README.rst
%license LICENSE


%changelog
* Tue Nov 22 2022 Jonathan Wright <jonathan@almalinux.org> - 1.1-1
- Initial package build

