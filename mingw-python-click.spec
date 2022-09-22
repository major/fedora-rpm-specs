%{?mingw_package_header}

%global pkgname click
%global pypi_name %{pkgname}

Name:          mingw-python-%{pkgname}
Summary:       MinGW Windows Python %{pkgname} library
Version:       8.1.3
Release:       1%{?dist}
BuildArch:     noarch

License:       BSD
URL:           https://palletsprojects.com/p/click/
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
%license LICENSE.rst
%{mingw32_python3_sitearch}/%{pkgname}/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}-py%{mingw32_python3_version}.egg-info/


%files -n mingw64-python3-%{pkgname}
%license LICENSE.rst
%{mingw64_python3_sitearch}/%{pkgname}/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}-py%{mingw64_python3_version}.egg-info/


%changelog
* Tue Aug 09 2022 Sandro Mani <manisandro@gmail.com> - 8.1.3-1
- Update to 8.1.3

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Apr 21 2022 Sandro Mani <manisandro@gmail.com> - 8.1.2-1
- Update to 8.1.2

* Mon Feb 28 2022 Sandro Mani <manisandro@gmail.com> - 8.0.4-1
- Update to 8.0.4

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 8.0.3-4
- Rebuild for new python dependency generator (take two)

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 8.0.3-3
- Rebuild for new python dependency generator

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 05 2021 Sandro Mani <manisandro@gmail.com> - 8.0.3-1
- Update to 8.0.3

* Wed Sep 29 2021 Sandro Mani <manisandro@gmail.com> - 8.0.1-3
- Backport proposed patch for unguarded access to None

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 05 2021 Sandro Mani <manisandro@gmail.com> - 8.0.1-1
- Update to 8.0.1

* Fri Jun 11 2021 Sandro Mani <manisandro@gmail.com> - 7.1.2-6
- Rebuild (python-3.10)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 08 2020 Sandro Mani <manisandro@gmail.com> - 7.1.2-4
- Switch to py3_build/py3_install macros

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Sandro Mani <manisandro@gmail.com> - 7.1.2-2
- Rebuild (python-3.9)

* Fri May 22 2020 Sandro Mani <manisandro@gmail.com> - 7.1.2-1
- Update to 7.1.2

* Wed Oct 30 2019 Sandro Mani <manisandro@gmail.com> - 7.0-1
- Update to 7.0
- Switch to python3

* Wed Sep 06 2017 Sandro Mani <manisandro@gmail.com> - 6.7-1
- Initial package
