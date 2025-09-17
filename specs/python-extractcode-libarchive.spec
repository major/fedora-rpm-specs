%global pypi_name extractcode-libarchive-system-provided
%global pypi_name_with_underscore %(echo "%{pypi_name}" | sed "s/-/_/g")
%global wheel_name extractcode-libarchive
%global wheel_name_with_underscore %(echo "%{wheel_name}" | sed "s/-/_/g")

Name:           python-%{wheel_name}
Version:        33.0.0
Release:        %autorelease
Summary:        ScanCode Toolkit plugin to use pre-installed libarchive library

# LICENSE.txt is only if we bundle
License:        Apache-2.0
URL:            https://github.com/aboutcode-org/scancode-plugins
Source:         %{pypi_source %{pypi_name_with_underscore}}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(plugincode)

%global common_description %{expand:
The path of libarchive.so is either determined by distro data or explicitily
taken from EXTRACTCODE_LIBARCHIVE_PATH environment variable.}

%description %{common_description}

%package -n python3-%{wheel_name}
Summary:        %{summary}
Requires:       libarchive

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
%doc README.rst

%changelog
%autochangelog
