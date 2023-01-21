%{?mingw_package_header}

%global mod_name pygments
%global pypi_name Pygments

Name:          mingw-python-%{mod_name}
Summary:       MinGW Windows Python %{pypi_name} library
Version:       2.13.0
Release:       2%{?dist}
BuildArch:     noarch

License:       BSD
URL:           https://pygments.org/
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

%description -n mingw32-python3-%{mod_name}
MinGW Windows Python3 %{pypi_name} library.


%package -n mingw64-python3-%{mod_name}
Summary:       MinGW Windows Python3 %{pypi_name} library

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
%{mingw32_bindir}/pygmentize
%{mingw32_python3_sitearch}/%{mod_name}/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}.dist-info/

%files -n mingw64-python3-%{mod_name}
%license LICENSE
%{mingw64_bindir}/pygmentize
%{mingw64_python3_sitearch}/%{mod_name}/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}.dist-info/


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 01 2022 Sandro Mani <manisandro@gmail.com> - 2.13.0-1
- Update to 2.13.0

* Wed Oct 12 2022 Sandro Mani <manisandro@gmail.com> - 2.12.0-3
- Switch to python3-build

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri May 20 2022 Sandro Mani <manisandro@gmail.com> - 2.12.0-1
- Update to 2.12.0

* Tue Feb 15 2022 Sandro Mani <manisandro@gmail.com> - 2.11.5-1
- Update to 2.11.5

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 2.10.0-4
- Rebuild for new python dependency generator (take two)

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 2.10.0-3
- Rebuild for new python dependency generator

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 24 2021 Sandro Mani <manisandro@gmail.com> - 2.10.0-1
- Update to 2.10.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 05 2021 Sandro Mani <manisandro@gmail.com> - 2.9.0-1
- Update to 2.9.0

* Fri Jun 11 2021 Sandro Mani <manisandro@gmail.com> - 2.8.1-2
- Rebuild (python-3.10)

* Sun Mar 14 2021 Sandro Mani <manisandro@gmail.com> - 2.8.1-1
- Update to 2.8.1

* Thu Feb 04 2021 Sandro Mani <manisandro@gmail.com> - 2.7.4-1
- Update to 2.7.4

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 27 2020 Sandro Mani <manisandro@gmail.com> - 2.7.2-1
- Update to 2.7.2

* Thu Nov 05 2020 Sandro Mani <manisandro@gmail.com> - 2.7.1-1
- Update to 2.7.1

* Tue Jun 02 2020 Sandro Mani <manisandro@gmail.com> - 2.6.1-2
- Rebuild (python-3.9)

* Fri May 22 2020 Sandro Mani <manisandro@gmail.com> - 2.6.1-1
- Initial package
