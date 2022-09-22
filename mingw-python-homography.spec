%{?mingw_package_header}

%global pkgname homography

Name:          mingw-python-%{pkgname}
Summary:       MinGW Windows Python %{pkgname} library
Version:       0.1.7
Release:       7%{?dist}
BuildArch:     noarch

License:       GPLv3
URL:           https://github.com/satellogic/%{pkgname}
Source0:       https://github.com/satellogic/%{pkgname}/archive/v%{version}/%{pkgname}-%{version}.tar.gz

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
%autosetup -p1 -n %{pkgname}-%{version}


%build
%{mingw32_py3_build}
%{mingw64_py3_build}


%install
%{mingw32_py3_install}
%{mingw64_py3_install}


%files -n mingw32-python3-%{pkgname}
%license LICENSE
%{mingw32_python3_sitearch}/%{pkgname}.py
%{mingw32_python3_sitearch}/__pycache__/%{pkgname}*
%{mingw32_python3_sitearch}/%{pkgname}-%{version}-py%{mingw32_python3_version}.egg-info/

%files -n mingw64-python3-%{pkgname}
%license LICENSE
%{mingw64_python3_sitearch}/%{pkgname}.py
%{mingw64_python3_sitearch}/__pycache__/%{pkgname}*
%{mingw64_python3_sitearch}/%{pkgname}-%{version}-py%{mingw32_python3_version}.egg-info/


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 0.1.7-6
- Rebuild for new python dependency generator (take two)

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 0.1.7-5
- Rebuild for new python dependency generator

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 11 2021 Sandro Mani <manisandro@gmail.com> - 0.1.7-2
- Rebuild (python-3.10)

* Thu Jan 28 2021 Sandro Mani <manisandro@gmail.com> - 0.1.7-1
- Update to 0.1.7

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 09 2020 Sandro Mani <manisandro@gmail.com> - 0.1.6-1
- Update to 0.1.6

* Tue Jun 02 2020 Sandro Mani <manisandro@gmail.com> - 0.1.5-2
- Rebuild (python-3.9)

* Wed Oct 30 2019 Sandro Mani <manisandro@gmail.com> - 0.1.5-1
- Initial package
