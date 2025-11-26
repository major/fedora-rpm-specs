%bcond tests 1

Name:           python-mkdocs-gen-files
Version:        0.6.0
Release:        %autorelease
Summary:        MkDocs plugin to generate documentation pages during the build

License:        MIT
URL:            https://oprypin.github.io/mkdocs-gen-files
Source:         %{pypi_source mkdocs_gen_files}

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-golden)
%endif

%global _description %{expand:
This package provides a plugin for MkDocs to programmatically generate
documentation pages during the build.}

%description %_description

%package -n     python3-mkdocs-gen-files
Summary:        %{summary}

%description -n python3-mkdocs-gen-files %_description

%prep
%autosetup -p1 -n mkdocs_gen_files-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l mkdocs_gen_files

%check
%if %{with tests}
%pytest
%else
%pyproject_check_import
%endif

%files -n python3-mkdocs-gen-files -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
