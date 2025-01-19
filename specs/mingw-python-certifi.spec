%{?mingw_package_header}

%global pypi_name certifi

Name:          mingw-python-%{pypi_name}
Summary:       MinGW Windows Python %{pypi_name} library
Version:       2024.8.30
Release:       2%{?dist}
BuildArch:     noarch

License:       MPL-2.0
URL:           https://certifi.io/en/latest/
Source0:       %{pypi_source}

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-build

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-build


%description
MinGW Windows Python %{pypi_name}.


%package -n mingw32-python3-%{pypi_name}
Summary:       MinGW Windows Python3 %{pypi_name}

%description -n mingw32-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name}.


%package -n mingw64-python3-%{pypi_name}
Summary:       MinGW Windows Python3 %{pypi_name}

%description -n mingw64-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name}.


%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%build
%mingw32_py3_build_wheel
%mingw64_py3_build_wheel


%install
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel


%files -n mingw32-python3-%{pypi_name}
%license LICENSE
%{mingw32_python3_sitearch}/%{pypi_name}/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}.dist-info/

%files -n mingw64-python3-%{pypi_name}
%license LICENSE
%{mingw64_python3_sitearch}/%{pypi_name}/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}.dist-info/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2024.8.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 30 2024 Sandro Mani <manisandro@gmail.com> - 2024.8.30-1
- Update to 2024.8.30

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2024.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jul 07 2024 Sandro Mani <manisandro@gmail.com> - 2024.7.4-1
- Update to 2024.7.4

* Sat Jun 08 2024 Sandro Mani <manisandro@gmail.com> - 2024.6.2-1
- Update to 2024.6.2

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.7.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.7.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Aug 04 2023 Sandro Mani <manisandro@gmail.com> - 2023.7.22-1
- Update to 2023.7.22

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2023.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 18 2023 Sandro Mani <manisandro@gmail.com> - 2023.5.7-1
- Update to 2023.5.7

* Tue Jul 18 2023 Sandro Mani <manisandro@gmail.com> - 2023.05.07-1
- Update to 2023.05.07

* Tue Mar 21 2023 Sandro Mani <manisandro@gmail.com> - 2022.12.7-1
- Update to 2022.12.7

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.9.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 16 2022 Sandro Mani <manisandro@gmail.com> - 2022.9.24-1
- Update to 2022.9.24

* Mon Oct 10 2022 Sandro Mani <manisandro@gmail.com> - 2021.10.8-3
- Switch to python3-build

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021.10.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Feb 14 2022 Sandro Mani <manisandro@gmail.com> - 2021.10.8-1
- Update to 2021.10.8

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 2020.12.5-7
- Rebuild for new python dependency generator (take two)

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 2020.12.5-6
- Rebuild for new python dependency generator

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020.12.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.12.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 11 2021 Sandro Mani <manisandro@gmail.com> - 2020.12.5-3
- Rebuild (python-3.10)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.12.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 15 2021 Sandro Mani <manisandro@gmail.coM> - 2020.12.5-1
- Update to 2020.12.5

* Wed Nov 11 2020 Sandro Mani <manisandro@gmail.com> - 2020.11.08-1
- Update to 2020.11.08

* Sun Nov 08 2020 Sandro Mani <manisandro@gmail.com> - 2020.06.20-2
- Switch to py3_build/py3_install macros

* Sat Aug 15 2020 Sandro Mani <manisandro@gmail.com> - 2020.06.20-1
- Update to 2020.06.20

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2020.04.05.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 31 2020 Sandro Mani <manisandro@gmail.com> - 2020.04.05.1-2
- Rebuild (python-3.9)

* Fri May 22 2020 Sandro Mani <manisandro@gmail.com> - 2020.04.05.1-1
- Update to 2020.04.05.1

* Mon Dec 16 2019 Sandro Mani <manisandro@gmail.com> - 2019.11.28-1
- Initial package
