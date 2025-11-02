%bcond tests 1

Name:           python-mkdocs-autorefs
Version:        1.4.3
Release:        %autorelease
Summary:        Automatically link across pages in MkDocs.

License:        ISC
URL:            https://mkdocstrings.github.io/autorefs
Source:         %{pypi_source mkdocs_autorefs}
# Fix test_reference_implicit_with_code_inlinehilite_python
Patch:          https://github.com/mkdocstrings/autorefs/pull/60.patch
# setuptools is too old for the new PEP 639 SPDX license expression
# see https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#license-and-license-files
Patch100:       mkdocs_autorefs-revert-license-fields.diff

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  mkdocs-material
BuildRequires:  python3dist(pymdown-extensions)
BuildRequires:  python3dist(pytest)
%endif

%global _description %{expand:
This package provides a plugin to automatically link across pages in MkDocs.}

%description %_description

%package -n     python3-mkdocs-autorefs
Summary:        %{summary}

%description -n python3-mkdocs-autorefs %_description

%prep
%autosetup -N -n mkdocs_autorefs-%{version}
%autopatch -p1 -M99

%if (0%{?fedora} && 0%{?fedora} < 43) || (0%{?rhel} && 0%{?rhel} < 11)
# for older setuptools
%autopatch -p1 -m100 -M199
%endif

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L mkdocs_autorefs

%check
%if %{with tests}
# requires griffe which is unpackaged
rm tests/test_api.py
%pytest -v --deselect=tests/test_references.py::test_reference_implicit_with_code_inlinehilite_python
%else
%pyproject_check_import
%endif

%files -n python3-mkdocs-autorefs -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGELOG.md

%changelog
%autochangelog
