%{?mingw_package_header}

%global pkgname affine
%global pypi_name %{pkgname}

Name:          mingw-python-%{pkgname}
Summary:       MinGW Windows Python %{pkgname}
Version:       2.3.1
Release:       2%{?dist}
BuildArch:     noarch

License:       BSD
URL:           https://github.com/sgillies/affine
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
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Apr 20 2022 Sandro Mani <manisandro@gmail.com> - 2.3.1-1
- Update to 2.3.1

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 2.3.0-9
- Rebuild for new python dependency generator (take two)

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 2.3.0-8
- Rebuild for new python dependency generator

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 11 2021 Sandro Mani <manisandro@gmail.com> - 2.3.0-5
- Rebuild (python-3.10)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 08 2020 Sandro Mani <manisandro@gmail.com> - 2.3.0-3
- Switch to py3_build/py3_install macros

* Tue Jun 02 2020 Sandro Mani <manisandro@gmail.com> - 2.3.0-2
- Rebuild (python-3.9)

* Mon Dec 16 2019 Sandro Mani <manisandro@gmail.com> - 2.3.0-1
- Initial package
