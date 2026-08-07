%global pypi_name pyone

Name:           python-%{pypi_name}
Version:        6.0.2
Release:        %autorelease
Summary:        Python Bindings for OpenNebula XML-RPC API

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            http://opennebula.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Source1:        https://github.com/OpenNebula/addon-pyone/blob/master/LICENSE
BuildArch:      noarch

BuildRequires:  python3-aenum
BuildRequires:  python3-devel
BuildRequires:  python3-dicttoxml
BuildRequires:  python3-lxml
BuildRequires:  python3-requests
BuildRequires:  python3-six
BuildRequires:  python3-tblib
BuildRequires:  python3-xmltodict

%description
OpenNebula Python Bindings Description --PyOne is an implementation of Open
Nebula XML-RPC bindings in Python.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
OpenNebula Python Bindings Description --PyOne is an implementation of Open
Nebula XML-RPC bindings in Python. It has been integrated into upstream
OpenNebula release cycles from here <

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove shebangs from non-executable Python library files
find pyone -name '*.py' -exec sed -i -e '/^#!\//d' {} +

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
install -pm 0644 %{SOURCE1} LICENSE
%pyproject_install
%pyproject_save_files pyone

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
