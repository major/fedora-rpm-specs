%global pypi_name   pymaven-patch
%global forgeurl    https://github.com/nexB/pymaven
Version:            0.3.0
%global tag         0.3.0

%forgemeta

Name:           python-%{pypi_name}
Release:        %autorelease
Summary:        Library for working with Maven repositories via Python

License:        Apache-2.0
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(py)
BuildRequires:  python3dist(pytest)

%global common_description %{expand:
Pymaven is a Python library for interfacing with the Maven build system. There
are two major interfaces:

 - pymaven.client provides a basic Maven repository client
 - pymaven.pom provides a Pom object that can provide progromatic access to a
 maven pom file}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{common_description}

%prep
%forgeautosetup -p1

# Remove version limit from lxml
sed -i "s/lxml.*/lxml/" requirements.txt

%generate_buildrequires
# Fix issue about "versioning for this project requires either an sdist tarball,
# or access to an upstream git repository. It's also possible that there is a
# mismatch between the package name in setup.cfg and the argument given 
# to pbr.version.VersionInfo."
export PBR_VERSION=%{version}
%pyproject_buildrequires 

%build
# Fix issue about "versioning for this project requires either an sdist tarball,
# or access to an upstream git repository. It's also possible that there is a
# mismatch between the package name in setup.cfg and the argument given 
# to pbr.version.VersionInfo."
export PBR_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pymaven

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc CHANGELOG.rst README.rst

%changelog
%autochangelog
