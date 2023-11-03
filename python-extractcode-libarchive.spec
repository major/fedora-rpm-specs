%global pypi_name extractcode-libarchive
%global pypi_name_with_underscore %(echo "%{pypi_name}" | sed "s/-/_/g")

Name:           python-%{pypi_name}
Version:        21.5.31
Release:        %autorelease
Summary:        ScanCode Toolkit plugin to use pre-installed libarchive library

# LICENSE.txt is only if we bundle
License:        Apache-2.0
URL:            https://github.com/nexB/scancode-plugins
# wget https://github.com/nexB/scancode-plugins/archive/v21.5.31/scancode-plugins-21.5.31.tar.gz
# tar xvf scancode-plugins-21.5.31.tar.gz
# pushd scancode-plugins-21.5.31
# find . ! \( -name builtins -o -name extractcode_libarchive_system_provided \) -maxdepth 1 -exec rm -rvf {} \;
# mv builtins/extractcode_libarchive_system_provided/* ./
# rm -rfv builtins/
# popd
# mv scancode-plugins-21.5.31 extractcode-libarchive-21.5.31
# tar czf extractcode-libarchive-21.5.31.tar.gz extractcode-libarchive-21.5.31
# rm -rfv extractcode-libarchive-21.5.31
# rm -rfv scancode-plugins-21.5.31.tar.gz
Source:         %{pypi_name}-%{version}.tar.gz
Patch:          0001-Fix-Linux-distribution-detection.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(plugincode)

%global common_description %{expand:
The path of libarchive.so is either determined by distro data or explicitily
taken from EXTRACTCODE_LIBARCHIVE_PATH environment variable.}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}
Requires:       libarchive-devel

%description -n python3-%{pypi_name} %{common_description}


%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name_with_underscore}

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
