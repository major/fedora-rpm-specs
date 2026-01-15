Name:           python-pathspec
Version:        1.0.3
Release:        %autorelease
Summary:        Utility library for gitignore style pattern matching of file paths

License:        MPL-2.0
URL:            https://github.com/cpburnz/python-path-specification
Source:         %{pypi_source pathspec}

BuildArch:      noarch
BuildRequires:  python3-devel

# Tests require pytest which requires python-iniconfig, which in turn
# requires python-hatchling, requiring python-pathspec
# Conditionalize to make new Python bootstrap possible
%bcond tests 1

%if %{with tests}
BuildRequires:  python3-pytest
%endif

%description
Path Specification (pathspec) is a utility library for pattern matching of file
paths. So far this only includes Git's wildmatch pattern matching which itself
is derived from Rsync's wildmatch. Git uses wildmatch for its gitignore files.


%package -n     python3-pathspec
Summary:        %{summary}

%description -n python3-pathspec
Path Specification (pathspec) is a utility library for pattern matching of file
paths. So far this only includes Git's wildmatch pattern matching which itself
is derived from Rsync's wildmatch. Git uses wildmatch for its gitignore files.


%prep
%autosetup -n pathspec-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pathspec


%check
%pyproject_check_import
%if %{with tests}
%pytest
%endif


%files -n python3-pathspec -f %{pyproject_files}
%doc README.rst
%license LICENSE


%changelog
%autochangelog
