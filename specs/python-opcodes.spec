%global pypi_name opcodes
%global pypi_version 0.3.13
# No tags
%global commit0 0e37e4f718d0ad2524b9a7c8147bdb78ff09cdd1
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        %autorelease
Summary:        Database of Processor Instructions/Opcodes

License:        BSD-2-Clause
URL:            https://github.com/Maratyszcza/Opcodes
Source0:        %{url}/archive/%{commit0}/%{pypi_name}-%{shortcommit0}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3-pkg-resources

%description
Opcodes Project The goal of this project is to document instruction sets in a
format convenient for tools development.

%package -n     python3-%{pypi_name}
Summary:        Database of Processor Instructions/Opcodes

Requires:       python3dist(setuptools)
Requires:       python3-pkg-resources
%description -n python3-%{pypi_name}
Opcodes Project The goal of this project is to document instruction sets in a
format convenient for tools development.

%prep
%autosetup -n Opcodes-%{commit0}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pyproject_check_import
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license license.rst
%doc readme.rst

%changelog
%autochangelog

