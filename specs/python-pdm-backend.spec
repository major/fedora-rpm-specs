Name:           python-pdm-backend
Version:        2.4.5
Release:        %autorelease
Summary:        The build backend used by PDM that supports latest packaging standards
# SPDX
License:        MIT
URL:            https://github.com/pdm-project/pdm-backend
Source:         %{pypi_source pdm_backend}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-editables
BuildRequires:  python3-packaging
BuildRequires:  python3-tomli-w
BuildRequires:  python3-pyproject-metadata
# Test-only deps
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  mercurial
BuildRequires:  python3-editables
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools


%global _description %{expand:
The build backend used by PDM that supports latest packaging standards.}


%description %_description

%package -n     python3-pdm-backend
Summary:        %{summary}
Requires:       python3-editables
Requires:       python3-packaging
Requires:       python3-tomli-w
Requires:       python3-pyproject-metadata

%description -n python3-pdm-backend %_description


%prep
%autosetup -p1 -n pdm_backend-%{version}
# Remove bundled dependencies
rm -rv src/pdm/backend/_vendor
find ./ -name "*.py" | xargs \
  sed -i "s/from pdm\.backend\._vendor\./from /;s/from pdm\.backend\._vendor //"


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pdm


%check
git config --global user.name "John Doe"
git config --global user.email "john@doe.com"
%pytest


%files -n python3-pdm-backend -f %{pyproject_files}
%license LICENSE
%doc README.md


%changelog
%autochangelog
