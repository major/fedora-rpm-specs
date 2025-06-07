%bcond tests 1
%global forgeurl https://github.com/fralau/mkdocs-test

Name:           python-mkdocs-test
Version:        0.5.3
Release:        %autorelease
Summary:        Test framework for MkDocs projects

License:        MIT
URL:            https://mkdocs-test-plugin.readthedocs.io
# PyPI tarball doesn't include test artifacts
Source:         %{forgeurl}/archive/v%{version}/mkdocs-test-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  mkdocs
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(super-collections)
%endif

%global _description %{expand:
This package provides a framework for testing MkDocs projects.}

%description %_description

%package -n     python3-mkdocs-test
Summary:        %{summary}

%description -n python3-mkdocs-test %_description

%prep
%autosetup -p1 -n mkdocs-test-%{version}

%generate_buildrequires
%if %{with tests}
%pyproject_buildrequires -x test
%else
%pyproject_buildrequires
%endif

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l mkdocs_test

%check
%if %{with tests}
%pytest -v
%else
%pyproject_check_import
%endif

%files -n python3-mkdocs-test -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
