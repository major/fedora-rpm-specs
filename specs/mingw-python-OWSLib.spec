%{?mingw_package_header}

%global mod_name owslib
%global pypi_name OWSLib

Name:          mingw-python-%{pypi_name}
Summary:       MinGW Windows Python %{pypi_name} library
Version:       0.32.0
Release:       2%{?dist}
BuildArch:     noarch

License:       BSD-3-Clause
URL:           https://geopython.github.io/OWSLib
Source0:       %{pypi_source}

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-build

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-build


%description
MinGW Windows Python %{pypi_name} library.


%package -n mingw32-python3-%{mod_name}
Summary:       MinGW Windows Python3 %{pypi_name} library
Obsoletes:     mingw32-python3-%{pypi_name} < 0.27.2-2
Provides:      mingw32-python3-%{pypi_name} = %{version}-%{release}

%description -n mingw32-python3-%{mod_name}
MinGW Windows Python3 %{pypi_name} library.


%package -n mingw64-python3-%{mod_name}
Summary:       MinGW Windows Python3 %{pypi_name} library
Obsoletes:     mingw64-python3-%{pypi_name} < 0.27.2-2
Provides:      mingw64-python3-%{pypi_name} = %{version}-%{release}

%description -n mingw64-python3-%{mod_name}
MinGW Windows Python3 %{pypi_name} library.


%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%build
%mingw32_py3_build_wheel
%mingw64_py3_build_wheel


%install
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel


%files -n mingw32-python3-%{mod_name}
%license LICENSE
%{mingw32_python3_sitearch}/%{mod_name}/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}.dist-info/

%files -n mingw64-python3-%{mod_name}
%license LICENSE
%{mingw64_python3_sitearch}/%{mod_name}/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}.dist-info/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Nov 15 2024 Sandro Mani <manisandro@gmail.com> - 0.32.0-1
- Update to 0.32.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jul 07 2024 Sandro Mani <manisandro@gmail.com> - 0.31.0-1
- Update to 0.31.0

* Fri Mar 22 2024 Sandro Mani <manisandro@gmail.com> - 0.30.0-1
- Update to 0.30.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 07 2023 Sandro Mani <manisandro@gmail.com> - 0.29.3-1
- Update to 0.29.3

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May 22 2023 Sandro Mani <manisandro@gmail.com> - 0.29.2-1
- Update to 0.29.2

* Sat Apr 15 2023 Sandro Mani <manisandro@gmail.com> - 0.29.1-1
- Update to 0.29.1

* Mon Apr 10 2023 Sandro Mani <manisandro@gmail.com> - 0.29.0-1
- Update to 0.29.0

* Tue Feb 28 2023 Sandro Mani <manisandro@gmail.com> - 0.28.1-1
- Update to 0.28.1

* Tue Feb 21 2023 Sandro Mani <manisandro@gmail.com> - 0.28.0-1
- Update to 0.28.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 11 2022 Sandro Mani <manisandro@gmail.com>
- Switch to python3-build

* Tue Aug 30 2022 Sandro Mani <manisandro@gmail.com> - 0.27.2-1
- Update to 0.27.2

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Sandro Mani <manisandro@gmail.com> - 0.26.0-2
- Relax pyproj requires to fix broken dependencies

* Mon Jun 13 2022 Sandro Mani <manisandro@gmail.com> - 0.26.0-1
- Update to 0.26.0

* Tue Feb 15 2022 Sandro Mani <manisandro@gmail.com> - 0.25.0-6
- Drop OWSLib_pyproj.patch

* Tue Feb 15 2022 Sandro Mani <manisandro@gmail.com> - 0.25.0-5
- Temporarily patch out pyproj requires which is not yet packaged

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 0.25.0-4
- Rebuild for new python dependency generator (take two)

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 0.25.0-3
- Rebuild for new python dependency generator

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 27 2021 Sandro Mani <manisandro@gmail.com> - 0.25.0-1
- Update to 0.25.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 11 2021 Sandro Mani <manisandro@gmail.com> - 0.21.0-3
- Rebuild (python-3.10)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 10 2020 Sandro Mani <manisandro@gmail.com> - 0.21.0-1
- Update to 0.21.0

* Thu Nov 05 2020 Sandro Mani <manisandro@gmail.com> - 0.20.0-1
- Update to 0.20.0

* Tue Jun 02 2020 Sandro Mani <manisandro@gmail.com> - 0.18.0-2
- Rebuild (python-3.9)

* Sun Nov 03 2019 Sandro Mani <manisandro@gmail.com> - 0.18.0-1
- Initial package
