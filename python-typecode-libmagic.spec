%global pypi_name typecode-libmagic
%global pypi_name_with_underscore %(echo "%{pypi_name}" | sed "s/-/_/g")

Name:           python-%{pypi_name}
Version:        21.5.31
Release:        %autorelease
Summary:        ScanCode Toolkit plugin to use pre-installed libmagic library and data file

# Only the code in src/__init__.py is relevant as we do not bundle libmagic
License:        BSD-2-Clause
URL:            https://github.com/nexB/scancode-plugins
# wget https://github.com/nexB/scancode-plugins/archive/v21.5.31/scancode-plugins-21.5.31.tar.gz
# tar xvf scancode-plugins-21.5.31.tar.gz
# pushd scancode-plugins-21.5.31
# find . ! \( -name builtins -o -name typecode_libmagic_system_provided \) -maxdepth 1 -exec rm -rvf {} \;
# mv builtins/typecode_libmagic_system_provided/* ./
# rm -rfv builtins/
# popd
# mv scancode-plugins-21.5.31 typecode-libmagic-21.5.31
# tar czf typecode-libmagic-21.5.31.tar.gz typecode-libmagic-21.5.31
# rm -rfv typecode-libmagic-21.5.31
# rm -rfv scancode-plugins-21.5.31.tar.gz
Source:         %{pypi_name}-%{version}.tar.gz
Patch:          0001-Fix-Linux-distribution-detection.patch
Patch:          0001-Fix-library-location-on-32-bits-arch.patch
Patch:          remove-unused-licenses.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(plugincode)

%global common_description %{expand:
The path to libmagic and its database is determined from well known distro
locations.}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}
Requires:       file-devel

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

%changelog
%autochangelog
