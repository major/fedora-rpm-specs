%{?mingw_package_header}

%global pkgname ephem
%global pypi_name %{pkgname}

Name:          mingw-python-%{pkgname}
Summary:       MinGW Windows Python %{pkgname}
Version:       4.1.3
Release:       3%{?dist}
BuildArch:     noarch

License:       MIT
URL:           http://rhodesmill.org/pyephem/
Source0:       %{pypi_source}

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-setuptools

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc
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


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%build
%{mingw32_py3_build}
%{mingw64_py3_build}


%install
%{mingw32_py3_install}
%{mingw64_py3_install}

# Drop installed tests and doc
rm -rf %{buildroot}%{mingw32_python3_sitearch}/ephem/tests/
rm -rf %{buildroot}%{mingw64_python3_sitearch}/ephem/tests/
rm -rf %{buildroot}%{mingw32_python3_sitearch}/ephem/doc/
rm -rf %{buildroot}%{mingw64_python3_sitearch}/ephem/doc/


%files -n mingw32-python3-%{pkgname}
%license LICENSE
%{mingw32_python3_sitearch}/%{pypi_name}/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}*-py%{mingw32_python3_version}.egg-info

%files -n mingw64-python3-%{pkgname}
%license LICENSE
%{mingw64_python3_sitearch}/%{pypi_name}/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}*-py%{mingw64_python3_version}.egg-info


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 4.1.3-2
- Rebuild with mingw-gcc-12

* Sat Mar 05 2022 Sandro Mani <manisandro@gmail.com> - 4.1.3-1
- Update to 4.1.3

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 4.0.0.2-8
- Rebuild for new python dependency generator (take two)

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 4.0.0.2-7
- Rebuild for new python dependency generator

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sandro Mani <manisandro@gmail.com> - 4.0.0.2-5
- Add debug package

* Mon Aug 02 2021 Sandro Mani <manisandro@gmail.com> - 4.0.0.2-4
- Also drop doc installed below python site-packages dir

* Mon Aug 02 2021 Sandro Mani <manisandro@gmail.com> - 4.0.0.2-3
- Don't install tests

* Mon Aug 02 2021 Sandro Mani <manisandro@gmail.com> - 4.0.0.2-2
- Fix pkgname pyephem -> ephem

* Sat Jul 31 2021 Sandro Mani <manisandro@gmail.com> - 4.0.0.2-1
- Initial package
