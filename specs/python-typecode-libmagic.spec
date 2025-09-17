%global pypi_name typecode-libmagic-system-provided
%global pypi_name_with_underscore %(echo "%{pypi_name}" | sed "s/-/_/g")
%global wheel_name typecode-libmagic
%global wheel_name_with_underscore %(echo "%{wheel_name}" | sed "s/-/_/g")

Name:           python-%{wheel_name}
Version:        33.0.0
Release:        %autorelease
Summary:        ScanCode Toolkit plugin to use pre-installed libmagic library and data file

# Only the code in src/__init__.py is relevant as we do not bundle libmagic
License:        BSD-2-Clause
URL:            https://github.com/aboutcode-org/scancode-plugins
Source:         %{pypi_source %{pypi_name_with_underscore}}
Patch:          remove-unused-licenses.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(plugincode)

%global common_description %{expand:
The path to libmagic and its database is determined from well known distro
locations.}

%description %{common_description}

%package -n python3-%{wheel_name}
Summary:        %{summary}
Requires:       file-libs

%description -n python3-%{wheel_name} %{common_description}


%prep
%autosetup -p1 -n %{pypi_name_with_underscore}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{wheel_name_with_underscore}

%check
%pyproject_check_import

%files -n python3-%{wheel_name} -f %{pyproject_files}

%changelog
%autochangelog
