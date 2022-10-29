%global pypi_name PyMunin3

%global _description %{expand:
Python module for developing Munin Multigraph Plugins

Regular Munin Plugins employ one plugin, one graph logic and require the
execution of a script for data retrieval for each graph. Multigraph
plugins permit retrieval of data for multiple graphs in one execution
run (one plugin, many graphs), reducing the processing time and delay
for the fetch cycle significantly.}

Name:           python-%{pypi_name}
Version:        3.0.2
Release:        %{autorelease}
Summary:        Python module for developing Munin Multigraph Plugins
BuildArch:      noarch

License:        GPL-3.0-only
URL:            https://pypi.org/pypi/%{pypi_name}
Source0:        %{pypi_source %{pypi_name}}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description -n python3-%{pypi_name} %_description


%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pymunin


%check
# Package does not provide any tests
%pyproject_check_import


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
