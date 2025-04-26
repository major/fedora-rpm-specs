%global debug_package %{nil}
%global pypi_name msgspec

Name:           python-%{pypi_name}
Summary:        Fast serialization and validation library
Version:        0.19.0
Source:         https://github.com/jcrist/%{pypi_name}/archive/refs/tags/%{version}/msgspec-%{version}.tar.gz
Release:        %autorelease

License:        BSD-3-Clause
URL:            https://jcristharif.com/msgspec/

# Python 3.14: Call __annotate__ on type objects to get annotations
Patch:          https://github.com/jcrist/msgspec/pull/810.patch

BuildRequires:  python3-devel
BuildRequires:  python3dist(wheel)
# Adding the pytest dependency manually, as the `tests` extras group also
# includes mypy, pyright, pre-commit and other unpackaged dependencies
BuildRequires:  python3dist(pytest)
BuildRequires:  gcc
ExcludeArch: s390x i686

%generate_buildrequires
%pyproject_buildrequires

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%global _description %{expand:
A fast serialization and validation library, with builtin support for
JSON, MessagePack, YAML, and TOML.}

%description %_description
%description -n python3-%{pypi_name} %_description

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pyproject_check_import
# tests/test_raw.py::test_raw_copy_doesnt_leak calls Python from subprocess and is confused by msgspec in $PWD
export PYTHONSAFEPATH=1
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
