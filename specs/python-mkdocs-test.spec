%bcond tests 1

%global forgeurl https://github.com/fralau/mkdocs-test
Version:        0.6.0
%forgemeta

Name:           python-mkdocs-test
Release:        %autorelease
Summary:        Test framework for MkDocs projects

License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}

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
%forgeautosetup -p1

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
# Exclude/remove the 'test' package installed in site-packages
rm -rf %{buildroot}%{python3_sitelib}/test


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
