%{?mingw_package_header}

%global pkgname setuptools_scm
%global pypi_name %{pkgname}

Name:          mingw-python-%{pkgname}
Summary:       MinGW Windows Python %{pkgname} library
Version:       6.4.2
Release:       2%{?dist}
BuildArch:     noarch

License:       MIT
URL:           https://github.com/pypa/setuptools_scm/
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
Requires:      mingw32-python3-tomli
Requires:      mingw32-python3-packaging

%description -n mingw32-python3-%{pkgname}
MinGW Windows Python3 %{pkgname} library.


%package -n mingw64-python3-%{pkgname}
Summary:       MinGW Windows Python3 %{pkgname} library
Requires:      mingw64-python3-tomli
Requires:      mingw64-python3-packaging

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
%{mingw32_python3_sitearch}/%{pkgname}/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}-py%{mingw32_python3_version}.egg-info/

%files -n mingw64-python3-%{pkgname}
%license LICENSE
%{mingw64_python3_sitearch}/%{pkgname}/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}-py%{mingw64_python3_version}.egg-info/


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Feb 18 2022 Sandro Mani <manisandro@gmail.com> - 6.4.2-1
- Update to 6.4.2

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 6.3.2-6
- Rebuild for new python dependency generator (take two)

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 6.3.2-5
- Rebuild for new python dependency generator

* Tue Feb 01 2022 Sandro Mani <manisandro@gmail.com> - 6.3.2-4
- Require mingw-python-packaging

* Mon Jan 31 2022 Sandro Mani <manisandro@gmail.com> - 6.3.2-3
- Require mingw-python-tomli

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 21 2021 Sandro Mani <manisandro@gmail.com> - 6.3.2-1
- Update to 6.3.2

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 11 2021 Sandro Mani <manisandro@gmail.com> - 6.0.1-2
- Rebuild (python-3.10)

* Wed Mar 24 2021 Sandro Mani <manisandro@gmail.com> - 6.0.1-1
- Update to 6.0.1

* Tue Feb 02 2021 Sandro Mani <manisandro@gmail.com> - 5.0.1-1
- Update to 5.0.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 08 2020 Sandro Mani <manisandro@gmail.com> - 4.1.2-2
- Switch to py3_build/py3_install macros
* Tue Jun 02 2020 Sandro Mani <manisandro@gmail.com> - 4.1.2-1
- Initial package
