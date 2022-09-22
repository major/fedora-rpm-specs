%{?mingw_package_header}

%global pkgname psycopg2
%global pypi_name %{pkgname}

Name:          mingw-python-%{pkgname}
Summary:       MinGW Windows Python %{pkgname} library
Version:       2.9.3
Release:       2%{?dist}
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
BuildRequires: mingw32-python3-setuptools

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc
BuildRequires: mingw64-postgresql
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-setuptools


%description
MinGW Windows Python %{pkgname} library.


%package -n mingw32-python3-%{pkgname}
Summary:       MinGW Windows Python3 %{pkgname} library

%description -n mingw32-python3-%{pkgname}
MinGW Windows Python3 %{pkgname} library.


%package -n mingw64-python3-%{pkgname}
Summary:       MinGW Windows Python3 %{pkgname} library

%description -n mingw64-python3-%{pkgname}
MinGW Windows Python3 %{pkgname} library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%build
%{mingw32_py3_build}
%{mingw64_py3_build}


%install
%{mingw32_py3_install}
%{mingw64_py3_install}


%files -n mingw32-python3-%{pkgname}
%license LICENSE
%{mingw32_python3_sitearch}/%{pkgname}/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}-py%{mingw32_python3_version}.egg-info/


%files -n mingw64-python3-%{pkgname}
%license LICENSE
%{mingw64_python3_sitearch}/%{pkgname}/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}-py%{mingw64_python3_version}.egg-info/


%changelog
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
