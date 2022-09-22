%{?mingw_package_header}

%global pkgname pyproj

Name:           mingw-python-%{pkgname}
Summary:        MinGW Python %{pkgname} library
Version:        3.4.0
Release:        1%{?dist}
BuildArch:      noarch

License:        MIT
Url:            https://github.com/jswhit/%{pkgname}
Source0:        %{pypi_source %pkgname}


BuildRequires:  mingw32-filesystem >= 102
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-proj
BuildRequires:  mingw32-python3
BuildRequires:  mingw32-python3-setuptools
BuildRequires:  mingw32-python3-Cython

BuildRequires:  mingw64-filesystem >= 102
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-proj
BuildRequires:  mingw64-python3
BuildRequires:  mingw64-python3-setuptools
BuildRequires:  mingw64-python3-Cython


%description
MinGW Python %{pkgname} library.


%package -n mingw32-python3-%{pkgname}
Summary:       MinGW Python 3 %{pkgname} library

%description -n mingw32-python3-%{pkgname}
MinGW Python 3 %{pkgname} library.


%package -n mingw64-python3-%{pkgname}
Summary:       MinGW Python 3 %{pkgname} library

%description -n mingw64-python3-%{pkgname}
MinGW Python 3 %{pkgname} library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}


%build
(
export PROJ_DIR=%{mingw32_prefix}
export PROJ_INCDIR=%{mingw32_includedir}
export PROJ_LIBDIR=%{mingw32_libdir}
export PROJ_VERSION=`mingw32-pkg-config --modversion proj`
%{mingw32_py3_build}
)
(
export PROJ_DIR=%{mingw64_prefix}
export PROJ_INCDIR=%{mingw64_includedir}
export PROJ_LIBDIR=%{mingw64_libdir}
export PROJ_VERSION=`mingw64-pkg-config --modversion proj`
%{mingw64_py3_build}
)


%install
(
export PROJ_DIR=%{mingw32_prefix}
export PROJ_INCDIR=%{mingw32_includedir}
export PROJ_LIBDIR=%{mingw32_libdir}
export PROJ_VERSION=`mingw32-pkg-config --modversion proj`
%{mingw32_py3_install}
)
(
export PROJ_DIR=%{mingw64_prefix}
export PROJ_INCDIR=%{mingw64_includedir}
export PROJ_LIBDIR=%{mingw64_libdir}
export PROJ_VERSION=`mingw64-pkg-config --modversion proj`
%{mingw64_py3_install}
)


%files -n mingw32-python3-%{pkgname}
%license LICENSE
%{mingw32_bindir}/pyproj
%{mingw32_python3_sitearch}/%{pkgname}/
%{mingw32_python3_sitearch}/%{pkgname}-%{version}*-py%{mingw32_python3_version}.egg-info/

%files -n mingw64-python3-%{pkgname}
%license LICENSE
%{mingw64_bindir}/pyproj
%{mingw64_python3_sitearch}/%{pkgname}/
%{mingw64_python3_sitearch}/%{pkgname}-%{version}*-py%{mingw64_python3_version}.egg-info/


%changelog
* Tue Sep 13 2022 Sandro Mani <manisandro@gmail.com> - 3.4.0-1
- Update to 3.4.0

* Sun Sep 04 2022 Sandro Mani <manisandro@gmail.com> - 3.3.1-3
- Rebuild (proj)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 03 2022 Sandro Mani <manisandro@gmail.com> - 3.3.1-1
- Update to 3.3.1

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 3.3.0-4
- Rebuild with mingw-gcc-12

* Wed Mar 09 2022 Sandro Mani <manisandro@gmail.com> - 3.3.0-3
- Rebuild for proj-9.0.0

* Sat Feb 19 2022 Sandro Mani <manisandro@gmail.com> - 3.3.0-2
- Fix spec filename
- Fix URL

* Fri Feb 11 2022 Sandro Mani <manisandro@gmail.com> - 3.3.0-1
- Initial package
