%{?mingw_package_header}

%global pypi_name ephem

Name:          mingw-python-%{pypi_name}
Summary:       MinGW Windows Python %{pypi_name}
Version:       4.1.6
Release:       2%{?dist}
BuildArch:     noarch

License:       MIT
URL:           http://rhodesmill.org/pyephem/
Source0:       %{pypi_source}

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-dlfcn
BuildRequires: mingw32-gcc
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-build

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-dlfcn
BuildRequires: mingw64-gcc
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


%{?mingw_debug_package}


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
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 08 2024 Sandro Mani <manisandro@gmail.com> - 4.1.6-1
- Update to 4.1.6

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Oct 12 2023 Sandro Mani <manisandro@gmail.com> - 4.1.5-1
- Update to 4.1.5

* Mon Sep 04 2023 Sandro Mani <manisandro@gmail.com> - 4.1.4-1
- Update to 4.1.4

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 11 2022 Sandro Mani <manisandro@gmail.com> - 4.1.3-4
- Switch to python3-build

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
- Fix pypi_name pyephem -> ephem

* Sat Jul 31 2021 Sandro Mani <manisandro@gmail.com> - 4.0.0.2-1
- Initial package
