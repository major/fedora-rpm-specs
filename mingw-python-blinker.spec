%{?mingw_package_header}

%global pypi_name blinker

Name:          mingw-python-%{pypi_name}
Summary:       MinGW Windows Python %{pypi_name} library
Version:       1.6.2
Release:       1%{?dist}
BuildArch:     noarch

License:       MIT
URL:           https://github.com/pallets-eco/blinker
Source0:       %{pypi_source}

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-build

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-build


%description
MinGW Windows Python %{pypi_name}.


%package -n mingw32-python3-%{pypi_name}
Summary:       MinGW Windows Python3 %{pypi_name}

%description -n mingw32-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name}.


%package -n mingw64-python3-%{pypi_name}
Summary:       MinGW Windows Python3 %{pypi_name}

%description -n mingw64-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name}.


%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%build
%mingw32_py3_build_wheel
%mingw64_py3_build_wheel


%install
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel


%files -n mingw32-python3-%{pypi_name}
%license LICENSE.rst
%{mingw32_python3_sitearch}/%{pypi_name}/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}.dist-info/

%files -n mingw64-python3-%{pypi_name}
%license LICENSE.rst
%{mingw64_python3_sitearch}/%{pypi_name}/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}.dist-info/


%changelog
* Sat Jan 06 2024 Sandro Mani <manisandro@gmail.com> - 1.6.2-1
- Initial package
