%{?mingw_package_header}

%global pkgname urllib3
%global pypi_name %{pkgname}

Name:          mingw-python-%{pkgname}
Summary:       MinGW Windows Python %{pkgname}
Version:       1.26.12
Release:       1%{?dist}
BuildArch:     noarch

License:       MIT
URL:           https://urllib3.readthedocs.io/en/latest/
Source0:       %{pypi_source}

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-setuptools

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-setuptools


%description
MinGW Windows Python %{pkgname}.


%package -n mingw32-python3-%{pkgname}
Summary:       MinGW Windows Python3 %{pkgname}

%description -n mingw32-python3-%{pkgname}
MinGW Windows Python3 %{pkgname}.


%package -n mingw64-python3-%{pkgname}
Summary:       MinGW Windows Python3 %{pkgname}

%description -n mingw64-python3-%{pkgname}
MinGW Windows Python3 %{pkgname}.


%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%build
%{mingw32_py3_build}
%{mingw64_py3_build}


%install
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
* Fri Sep 23 2022 Sandro Mani <manisandro@gmail.com> - 1.26.12-1
- Update to 1.26.12

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Sandro Mani <manisandro@gmail.com> - 1.26.9-1
- Update to 1.26.9

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 1.26.8-4
- Rebuild for new python dependency generator (take two)

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 1.26.8-3
- Rebuild for new python dependency generator

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 09 2022 Sandro Mani <manisandro@gmail.com> - 1.26.8-1
- Update to 1.26.8

* Tue Sep 28 2021 Sandro Mani <manisandro@gmail.com> - 1.26.7-1
- Update to 1.26.7

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 12 2021 Sandro Mani <manisandro@gmail.com> - 1.26.6-1
- Update to 1.26.6

* Fri Jun 11 2021 Sandro Mani <manisandro@gmail.com> - 1.26.5-2
- Rebuild (python-3.10)

* Wed May 26 2021 Sandro Mani <manisandro@gmail.com> - 1.26.5-1
- Update to 1.26.5

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 05 2020 Sandro Mani <manisandro@gmail.com> - 1.25.10-1
- Update to 1.25.10

* Tue Jun 02 2020 Sandro Mani <manisandro@gmail.com> - 1.25.7-2
- Rebuild (python-3.9)

* Mon Dec 16 2019 Sandro Mani <manisandro@gmail.com> - 1.25.7-1
- Initial package
