%{?mingw_package_header}

%global pkgname shapely
%global pypi_name Shapely

Name:          mingw-python-%{pkgname}
Summary:       MinGW Windows Python %{pkgname}
Version:       1.8.4
Release:       1%{?dist}
BuildArch:     noarch

License:       BSD
URL:           https://github.com/Toblerity/Shapely
Source0:       %{pypi_source}

# Fix loading geos library
Patch0:        shapely_geos.patch

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-setuptools
BuildRequires: mingw32-gcc

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-setuptools
BuildRequires: mingw64-gcc


%description
MinGW Windows Python %{pkgname}.


%package -n mingw32-python3-%{pkgname}
Summary:       MinGW Windows Python3 %{pkgname}
# See Patch0
Requires:      mingw32(libgeos_c-1.dll)

%description -n mingw32-python3-%{pkgname}
MinGW Windows Python3 %{pkgname}.


%package -n mingw64-python3-%{pkgname}
Summary:       MinGW Windows Python3 %{pkgname}
# See Patch0
Requires:      mingw64(libgeos_c-1.dll)

%description -n mingw64-python3-%{pkgname}
MinGW Windows Python3 %{pkgname}.


%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%build
export NO_GEOS_CONFIG=1
%{mingw32_py3_build}
%{mingw64_py3_build}


%install
export NO_GEOS_CONFIG=1
%{mingw32_py3_install}
%{mingw64_py3_install}


%files -n mingw32-python3-%{pkgname}
%license LICENSE.txt
%{mingw32_python3_sitearch}/%{pkgname}/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}-py%{mingw32_python3_version}.egg-info/

%files -n mingw64-python3-%{pkgname}
%license LICENSE.txt
%{mingw64_python3_sitearch}/%{pkgname}/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}-py%{mingw64_python3_version}.egg-info/


%changelog
* Tue Aug 30 2022 Sandro Mani <manisandro@gmail.com> - 1.8.4-1
- Update to 1.8.4

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Sandro Mani <manisandro@gmail.com> - 1.8.2-1
- Update to 1.8.2

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.8.1-2
- Rebuild with mingw-gcc-12

* Fri Feb 18 2022 Sandro Mani <manisandro@gmail.com> - 1.8.1-1
- Update to 1.8.1

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 1.8.0-4
- Rebuild for new python dependency generator (take two)

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 1.8.0-3
- Rebuild for new python dependency generator

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 26 2021 Sandro Mani <manisandro@gmail.com> - 1.8.0-1
- Update to 1.8.0

* Thu Oct 21 2021 Sandro Mani <manisandro@gmail.com> - 1.7.1-6
- Rebuild (geos)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 11 2021 Sandro Mani <manisandro@gmail.com> - 1.7.1-4
- Rebuild (python-3.10)

* Sat Feb 13 2021 Sandro Mani <manisandro@gmail.com> - 1.7.1-3
- Rebuild (geos)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 05 2020 Sandro Mani <manisandro@gmail.com> - 1.7.1-1
- Update to 1.7.1

* Tue Jun 02 2020 Sandro Mani <manisandro@gmail.com> - 1.7a2-2
- Rebuild (python-3.9)

* Mon Dec 16 2019 Sandro Mani <manisandro@gmail.com> - 1.7a2-1
- Initial package
