%{?mingw_package_header}

%global pkg_name charset-normalizer
%global pypi_name charset_normalizer

Name:          mingw-python-%{pkg_name}
Summary:       MinGW Windows Python %{pypi_name} library
Version:       3.4.1
Release:       1%{?dist}
BuildArch:     noarch

License:       MIT
URL:           https://github.com/ousret/charset_normalizer
Source0:       %{pypi_source}
Patch0:        charset_normalizer-deps.patch

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-build

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-build


%description
MinGW Windows Python %{pypi_name} library.


%package -n mingw32-python3-%{pkg_name}
Summary:       MinGW Windows Python3 %{pypi_name} library

%description -n mingw32-python3-%{pkg_name}
MinGW Windows Python3 %{pypi_name} library.


%package -n mingw64-python3-%{pkg_name}
Summary:       MinGW Windows Python3 %{pypi_name} library

%description -n mingw64-python3-%{pkg_name}
MinGW Windows Python3 %{pypi_name} library.


%prep
%autosetup -p1 -n %{pypi_name}-%{version}



%build
%mingw32_py3_build_wheel
%mingw64_py3_build_wheel


%install
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel


%files -n mingw32-python3-%{pkg_name}
%license LICENSE
%{mingw32_bindir}/normalizer
%{mingw32_python3_sitearch}/charset_normalizer/
%{mingw32_python3_sitearch}/charset_normalizer-%{version}.dist-info/

%files -n mingw64-python3-%{pkg_name}
%license LICENSE
%{mingw64_bindir}/normalizer
%{mingw64_python3_sitearch}/charset_normalizer/
%{mingw64_python3_sitearch}/charset_normalizer-%{version}.dist-info/


%changelog
* Tue Jan 07 2025 Sandro Mani <manisandro@gmail.com> - 3.4.1-1
- Update to 3.4.1

* Wed Oct 23 2024 Sandro Mani <manisandro@gmail.com> - 3.4.0-1
- Update to 3.4.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Nov 03 2023 Sandro Mani <manisandro@gmail.com> - 3.3.2-1
- Update to 3.3.2

* Sat Oct 28 2023 Sandro Mani <manisandro@gmail.com> - 3.3.1-1
- Update to 3.3.1

* Sat Oct 07 2023 Sandro Mani <manisandro@gmail.com> - 3.3.0-1
- Update to 3.3.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 18 2023 Sandro Mani <manisandro@gmail.com> - 3.2.0-1
- Update to 3.2.0

* Wed Mar 08 2023 Sandro Mani <manisandro@gmail.com> - 3.1.0-1
- Update to 3.1.0

* Wed Feb 15 2023 Sandro Mani <manisandro@gmail.com> - 3.0.1-1
- Update to 3.0.1

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 11 2022 Sandro Mani <manisandro@gmail.com> - 2.1.0-3
- Switch to python3-build

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 Sandro Mani <manisandro@gmail.com> - 2.1.0-1
- Update to 2.1.0

* Mon Feb 21 2022 Sandro Mani <manisandro@gmail.com> - 2.0.12-1
- Update to 2.0.12

* Fri Feb 11 2022 Sandro Mani <manisandro@gmail.com> - 2.0.11-1
- Initial package
