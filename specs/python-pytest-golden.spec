Name:           python-pytest-golden
Version:        0.2.2
Release:        %autorelease
Summary:        Plugin for pytest that offloads expected outputs to data files

License:        MIT
URL:            https://github.com/oprypin/pytest-golden
# PyPI tarball doesn't include tests
Source:         %{url}/archive/v%{version}/pytest-golden-%{version}.tar.gz
# Drop Python 3.6
Patch:          %{url}/commit/e42d7a786083f957ae7cfa09548c94e8abfa2944.patch
# Migrate to Hatch build and mypy type checker
Patch:          %{url}/commit/70df82de02b88781d5d23b1e1f170f7ecb5e42bf.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
This package provides a plugin for pytest that offloads expected outputs to
data files.}

%description %_description

%package -n     python3-pytest-golden
Summary:        %{summary}

%description -n python3-pytest-golden %_description

%prep
%autosetup -p1 -n pytest-golden-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L pytest_golden

%check
%pytest -v

%files -n python3-pytest-golden -f %{pyproject_files}
%license LICENSE.md
%doc README.md

%changelog
%autochangelog
