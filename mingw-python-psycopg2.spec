%{?mingw_package_header}

%global pypi_name psycopg2

Name:          mingw-python-%{pypi_name}
Summary:       MinGW Windows Python %{pypi_name} library
Version:       2.9.3
Release:       3%{?dist}
BuildArch:     noarch


# The exceptions allow linking to OpenSSL and PostgreSQL's libpq
# LGPLv3+ with exceptions: most files
# BSD: psycopg/adapter*.{h,c} and psycopg/microprotocol*.{h,c}
License:       (LGPLv3+ with exceptions) and BSD
URL:           https://www.psycopg.org/
Source0:       %{pypi_source}

# MinGW build fixes
Patch0:        psycopg2_mingw.patch

BuildRequires: gcc

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw32-postgresql
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-build

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc
BuildRequires: mingw64-postgresql
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


%{?mingw_debug_package}


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
%{mingw32_python3_sitearch}/%{pypi_name}/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}.dist-info/

%files -n mingw64-python3-%{pypi_name}
%license LICENSE
%{mingw64_python3_sitearch}/%{pypi_name}/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}.dist-info/


%changelog
* Tue Oct 11 2022 Sandro Mani <manisandro@gmail.com> - 2.9.3-3
- Switch to python3-build

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri May 20 2022 Sandro Mani <manisandro@gmail.com> - 2.9.3-1
- Update to 2.9.3

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 2.9.1-5
- Rebuild with mingw-gcc-12

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 2.9.1-4
- Rebuild for new python dependency generator (take two)

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 2.9.1-3
- Rebuild for new python dependency generator

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 04 2021 Sandro Mani <manisandro@gmail.com> - 2.9.1-1
- Update to 2.9.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 11 2021 Sandro Mani <manisandro@gmail.com> - 2.8.6-4
- Rebuild (python-3.10)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 09 2020 Sandro Mani <manisandro@gmail.com> - 2.8.6-2
- Fix License and URL, use pypi_source

* Mon Nov 09 2020 Sandro Mani <manisandro@gmail.com> - 2.8.6-1
- Update to 2.8.6

* Sun May 31 2020 Sandro Mani <manisandro@gmail.com> - 2.8.5-2
- Rebuild (python-3.9)

* Thu May 21 2020 Sandro Mani <manisandro@gmail.com> - 2.8.5-1
- Initial package
