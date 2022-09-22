%{?mingw_package_header}

%global pkgname charset-normalizer
%global pypi_name %{pkgname}


Name:          mingw-python-%{pkgname}
Summary:       MinGW Windows Python %{pkgname} library
Version:       2.1.0
Release:       2%{?dist}
BuildArch:     noarch

License:       MIT
URL:           https://github.com/ousret/charset_normalizer
Source0:       %{pypi_source}

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-setuptools

BuildRequires: mingw64-filesystem >= 95
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
%{mingw32_bindir}/normalizer
%{mingw32_python3_sitearch}/charset_normalizer/
%{mingw32_python3_sitearch}/charset_normalizer-%{version}-py%{mingw32_python3_version}.egg-info/

%files -n mingw64-python3-%{pkgname}
%license LICENSE
%{mingw64_bindir}/normalizer
%{mingw64_python3_sitearch}/charset_normalizer/
%{mingw64_python3_sitearch}/charset_normalizer-%{version}-py%{mingw64_python3_version}.egg-info/


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 Sandro Mani <manisandro@gmail.com> - 2.1.0-1
- Update to 2.1.0

* Mon Feb 21 2022 Sandro Mani <manisandro@gmail.com> - 2.0.12-1
- Update to 2.0.12

* Fri Feb 11 2022 Sandro Mani <manisandro@gmail.com> - 2.0.11-1
- Initial package
