%global pypi_name columnize

Name:           pycolumnize
Version:        0.3.11
Release:        %autorelease
Summary:        Python module to align in columns a simple list

License:        MIT
URL:            https://github.com/rocky/pycolumnize
Source:         %pypi_source
BuildArch:      noarch

%description
A Python module to format a simple (i.e. not nested) list into aligned columns.
A string with embedded newline characters is returned.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%description -n python3-%{pypi_name}
A Python module to format a simple (i.e. not nested) list into aligned columns.
A string with embedded newline characters is returned.

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import
%pytest -v

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc ChangeLog README.rst SECURITY.md THANKS

%changelog
%autochangelog
