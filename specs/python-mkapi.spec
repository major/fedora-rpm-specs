%bcond tests 1
%global forgeurl https://github.com/daizutabi/mkapi

Name:           python-mkapi
Version:        3.0.23
Release:        %autorelease
Summary:        Plugin for MkDocs to generate API documentation

# mkapi itself is MIT, but one of the unshipped examples is BSD-2-Clause per
# tests/examples/_styles/LICENSE
SourceLicense:  MIT AND BSD-2-Clause
License:        MIT
URL:            https://daizutabi.github.io/mkapi/
# PyPI tarball is missing test fixtures
Source:         %{forgeurl}/archive/%{version}/mkapi-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
%endif

%global _description %{expand:
MkAPI is a plugin for MkDocs, designed to facilitate the generation of API
documentation for Python projects. MkAPI streamlines the documentation process
by automatically extracting docstrings and organizing them into a structured
format, making it easier for developers to maintain and share their API
documentation.}

%description %_description

%package -n     python3-mkapi
Summary:        %{summary}

%description -n python3-mkapi %_description

%prep
%autosetup -p1 -n mkapi-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l mkapi

%check
%if %{with tests}
# Disable test that hardcodes the source path
%pytest -v --deselect=tests/test_plugin.py::test_mkdocs_config
%else
%pyproject_check_import
%endif

%files -n python3-mkapi -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
