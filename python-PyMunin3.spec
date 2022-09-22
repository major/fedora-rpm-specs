# Package does not provide any tests
%bcond_with tests

%global _description %{expand:
Python module for developing Munin Multigraph Plugins

Regular Munin Plugins employ one plugin, one graph logic and require the
execution of a script for data retrieval for each graph. Multigraph
plugins permit retrieval of data for multiple graphs in one execution
run (one plugin, many graphs), reducing the processing time and delay
for the fetch cycle significantly.}

# Package does not provide debug info
%global debug_package %{nil}

Name:           python-PyMunin3
Version:        3.0.1
Release:        %{autorelease}
Summary:        Python module for developing Munin Multigraph Plugins

License:        GPL-3.0-only
URL:            https://pypi.org/pypi/PyMunin3
Source0:        %{pypi_source PyMunin3}

%description %_description

%package -n python3-PyMunin3
Summary:        %{summary}
BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3-pytest
%endif

BuildArch:      noarch

%description -n python3-PyMunin3 %_description


%prep
%autosetup -n PyMunin3-%{version}

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pymunin


%check
%if %{with tests}
%{pytest}
%else
%pyproject_check_import
%endif


%files -n python3-PyMunin3 -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
