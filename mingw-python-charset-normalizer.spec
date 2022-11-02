%{?mingw_package_header}

%global pypi_name charset-normalizer

Name:          mingw-python-%{pypi_name}
Summary:       MinGW Windows Python %{pypi_name} library
Version:       2.1.0
Release:       3%{?dist}
BuildArch:     noarch

License:       MIT
URL:           https://github.com/ousret/charset_normalizer
Source0:       %{pypi_source}

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-build

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-build


%description
MinGW Windows Python %{pypi_name} library.


%package -n mingw32-python3-%{pypi_name}
Summary:       MinGW Windows Python3 %{pypi_name} library

%description -n mingw32-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name} library.


%package -n mingw64-python3-%{pypi_name}
Summary:       MinGW Windows Python3 %{pypi_name} library

%description -n mingw64-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name} library.


%prep
%autosetup -p1 -n %{pypi_name}-%{version}



%build
%mingw32_py3_build_wheel
%mingw64_py3_build_wheel


%install
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel


%files -n mingw32-python3-%{pypi_name}
%license LICENSE
%{mingw32_bindir}/normalizer
%{mingw32_python3_sitearch}/charset_normalizer/
%{mingw32_python3_sitearch}/charset_normalizer-%{version}.dist-info/

%files -n mingw64-python3-%{pypi_name}
%license LICENSE
%{mingw64_bindir}/normalizer
%{mingw64_python3_sitearch}/charset_normalizer/
%{mingw64_python3_sitearch}/charset_normalizer-%{version}.dist-info/


%changelog
* Tue Oct 11 2022 Sandro Mani <manisandro@gmail.com> - 2.1.0-3
- Switch to python3-build

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 Sandro Mani <manisandro@gmail.com> - 2.1.0-1
- Update to 2.1.0

* Mon Feb 21 2022 Sandro Mani <manisandro@gmail.com> - 2.0.12-1
- Update to 2.0.12

* Fri Feb 11 2022 Sandro Mani <manisandro@gmail.com> - 2.0.11-1
- Initial package
