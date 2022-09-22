%{?mingw_package_header}

%global pkgname OWSLib
%global pypi_name %{pkgname}

Name:          mingw-python-%{pkgname}
Summary:       MinGW Windows Python %{pkgname} library
Version:       0.27.2
Release:       1%{?dist}
BuildArch:     noarch

License:       BSD
URL:           https://geopython.github.io/OWSLib
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

find . -name '*.py' | xargs sed -i '1s|^#!python|#!/usr/bin/python3|'


%build
%{mingw32_py3_build}
%{mingw64_py3_build}


%install
%{mingw32_py3_install}
%{mingw64_py3_install}


%files -n mingw32-python3-%{pkgname}
%license LICENSE
%{mingw32_python3_sitearch}/owslib/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}-py%{mingw32_python3_version}.egg-info/

%files -n mingw64-python3-%{pkgname}
%license LICENSE
%{mingw64_python3_sitearch}/owslib/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}-py%{mingw64_python3_version}.egg-info/


%changelog
* Tue Aug 30 2022 Sandro Mani <manisandro@gmail.com> - 0.27.2-1
- Update to 0.27.2

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Sandro Mani <manisandro@gmail.com> - 0.26.0-2
- Relax pyproj requires to fix broken dependencies

* Mon Jun 13 2022 Sandro Mani <manisandro@gmail.com> - 0.26.0-1
- Update to 0.26.0

* Tue Feb 15 2022 Sandro Mani <manisandro@gmail.com> - 0.25.0-6
- Drop OWSLib_pyproj.patch

* Tue Feb 15 2022 Sandro Mani <manisandro@gmail.com> - 0.25.0-5
- Temporarily patch out pyproj requires which is not yet packaged

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 0.25.0-4
- Rebuild for new python dependency generator (take two)

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 0.25.0-3
- Rebuild for new python dependency generator

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 27 2021 Sandro Mani <manisandro@gmail.com> - 0.25.0-1
- Update to 0.25.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 11 2021 Sandro Mani <manisandro@gmail.com> - 0.21.0-3
- Rebuild (python-3.10)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 10 2020 Sandro Mani <manisandro@gmail.com> - 0.21.0-1
- Update to 0.21.0

* Thu Nov 05 2020 Sandro Mani <manisandro@gmail.com> - 0.20.0-1
- Update to 0.20.0

* Tue Jun 02 2020 Sandro Mani <manisandro@gmail.com> - 0.18.0-2
- Rebuild (python-3.9)

* Sun Nov 03 2019 Sandro Mani <manisandro@gmail.com> - 0.18.0-1
- Initial package
