%{?mingw_package_header}

%global pypi_name pytz

Name:          mingw-python-%{pypi_name}
Summary:       MinGW Windows Python %{pypi_name} library
Version:       2023.3
Release:       1%{?dist}
BuildArch:     noarch

License:       MIT
URL:           https://github.com/stub42/pytz
Source0:       %{pypi_source}

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-build

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-build


%description
MinGW Windows Python %{pypi_name} library.


%package -n mingw32-python3-%{pypi_name}
Summary:       MinGW Windows Python3 %{pypi_name} library

%description -n mingw32-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name} library.


%package -n mingw64-python3-%{pypi_name}
Summary:       MinGW Windows Python3 %{pypi_name} library

%description -n mingw64-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name} library.


%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%build
%mingw32_py3_build_wheel
%mingw64_py3_build_wheel


%install
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel


%files -n mingw32-python3-%{pypi_name}
%license LICENSE.txt
%{mingw32_python3_sitearch}/%{pypi_name}/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}.dist-info/

%files -n mingw64-python3-%{pypi_name}
%license LICENSE.txt
%{mingw64_python3_sitearch}/%{pypi_name}/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}.dist-info/


%changelog
* Fri Mar 31 2023 Sandro Mani <manisandro@gmail.com> - 2023.3-1
- Update to 2023.3

* Tue Mar 28 2023 Sandro Mani <manisandro@gmail.com> - 2023.2-1
- Update to 2023.2

* Fri Jan 20 2023 Sandro Mani <manisandro@gmail.com> - 2022.7.1-1
- Update to 2022.7.1

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 19 2022 Sandro Mani <manisandro@gmail.com> - 2022.7-1
- Update to 2022.7

* Tue Nov 01 2022 Sandro Mani <manisandro@gmail.com> - 2022.6-1
- Update to 2022.6

* Thu Oct 13 2022 Sandro Mani <manisandro@gmail.com> - 2022.2.1-2
- Switch to python3-build

* Tue Aug 16 2022 Sandro Mani <manisandro@gmail.com> - 2022.1-3
- Update to 2022.2.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2022.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Mar 23 2022 Sandro Mani <manisandro@gmail.com> - 2022.1-1
- Update to 2022.1

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 2021.3-4
- Rebuild for new python dependency generator (take two)

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 2021.3-3
- Rebuild for new python dependency generator

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 19 2021 Sandro Mani <manisandro@gmail.com> - 2021.3-1
- Update to 2021.3

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 11 2021 Sandro Mani <manisandro@gmail.com> - 2020.4-3
- Rebuild (python-3.10)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 05 2020 Sandro Mani <manisandro@gmail.com> - 2020.4-1
- Update to 2020.4

* Tue Jun 02 2020 Sandro Mani <manisandro@gmail.com> - 2020.1-2
- Rebuild (python-3.9)

* Fri May 22 2020 Sandro Mani <manisandro@gmail.com> - 2020.1-1
- Initial package
