# Copyright (C) 2023 Maxwell G <maxwell@gtmx.me>
# Copyright (C) Fedora Project Authors
# SPDX-License-Identifier: MIT
# License text: https://spdx.org/licenses/MIT

%bcond tests 1
%global forgeurl https://github.com/madpah/requirements-parser

Name:           python-requirements-parser
Version:        0.5.0
%forgemeta
Release:        1%{?dist}
Summary:        A small Python module for parsing Pip requirement files

License:        Apache-2.0
URL:            https://requirements-parser.readthedocs.org/
# The sdist is missing tests
Source:         %{forgesource}
# Part of https://github.com/madpah/requirements-parser/pull/87 submitted
# upstream
Patch:          pyproject.toml-limit-documentation-to-the-sdist.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  tomcli+tomlkit
%if %{with tests}
BuildRequires:  %{py3_dist pytest}
%endif

%global _description %{expand:
This package provides a small Python module for parsing Pip requirements files.}

%description %{_description}


%package -n     python3-requirements-parser
Summary:        %{summary}

%description -n python3-requirements-parser %{_description}


%prep
%autosetup -p1 %{forgesetupargs}
# types-setuptools is not needed at runtime,
# but setuptools itself for pkg_resources is
tomcli-set pyproject.toml del tool.poetry.dependencies.types-setuptools
tomcli-set pyproject.toml str tool.poetry.dependencies.setuptools "*"


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files requirements


%check
%pytest


%files -n python3-requirements-parser -f %{pyproject_files}
%license AUTHORS.rst LICENSE
%doc README.md


%changelog
* Tue Aug 15 2023 Maxwell G <maxwell@gtmx.me> - 0.5.0-1
- Initial import. Closes rhbz#2232042.
