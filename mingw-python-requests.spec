%{?mingw_package_header}

%global pkgname requests
%global pypi_name %{pkgname}

Name:          mingw-python-%{pkgname}
Summary:       MinGW Windows Python %{pkgname} library
Version:       2.28.1
Release:       2%{?dist}
BuildArch:     noarch

License:       ASL 2.0
URL:           https://requests.readthedocs.io/
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
Requires:      mingw32-python3-certifi

%description -n mingw32-python3-%{pkgname}
MinGW Windows Python3 %{pkgname}.


%package -n mingw64-python3-%{pkgname}
Summary:       MinGW Windows Python3 %{pkgname}
Requires:      mingw64-python3-certifi

%description -n mingw64-python3-%{pkgname}
MinGW Windows Python3 %{pkgname}.


%prep
%autosetup -p1 -n %{pypi_name}-%{version}

# Strip env shebang in nonexecutable file
sed -i '/#!\/usr\/.*python/d' requests/certs.py


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
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Sandro Mani <manisandro@gmail.com> - 2.28.1-1
- Update to 2.28.1

* Tue Jun 28 2022 Sandro Mani <manisandro@gmail.com> - 2.27.1-5
- Allow charset normalizer >=2 and <3

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 2.27.1-4
- Rebuild for new python dependency generator (take two)

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 2.27.1-3
- Rebuild for new python dependency generator

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.27.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 05 2022 Sandro Mani <manisandro@gmail.com> - 2.27.1-1
- Update to 2.27.1

* Fri Jul 30 2021 Sandro Mani <manisandro@gmail.com> - 2.26.0-1
- Update to 2.26.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.25.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 11 2021 Sandro Mani <manisandro@gmail.com> - 2.25.1-2
- Rebuild (python-3.10)

* Wed Feb 03 2021 Sandro Mani <manisandro@gmail.com> - 2.25.1-1
- Update to 2.25.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.25.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 27 2020 Sandro Mani <manisandro@gmail.com> - 2.25.0-1
- Update to 2.25.0

* Sun Nov 08 2020 Sandro Mani <manisandro@gmail.com> - 2.24.0-3
- Switch to py3_build/py3_install macros

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Sandro Mani <manisandro@gmail.com> - 2.24.0-1
- Update to 2.24.0

* Thu Jun 25 2020 Sandro Mani <manisandro@gmail.com> - 2.23.0-3
- Be more specific in %%files
- Fix license
- Strip env shebang in nonexecutable file

* Tue Jun 02 2020 Sandro Mani <manisandro@gmail.com> - 2.23.0-2
- Rebuild (python-3.9)

* Fri May 22 2020 Sandro Mani <manisandro@gmail.com> - 2.23.0-1
- Update to 2.23.0

* Fri Dec 06 2019 Sandro Mani <manisandro@gmail.com> - 2.22.0-1
- Initial package
