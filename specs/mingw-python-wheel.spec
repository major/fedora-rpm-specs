# This package is required by python-build to build wheels.
# To bootstrap, we copy the files to appropriate locations manually and create a minimal dist-info metadata.
# Note that as a pure Python package, the wheel contains no pre-built binary stuff.
%bcond_with     bootstrap

%{?mingw_package_header}

%global pypi_name wheel

Name:          mingw-python-%{pypi_name}
Summary:       MinGW Windows Python %{pypi_name} library
Version:       0.48.0
Release:       2%{?dist}
BuildArch:     noarch

License:       MIT AND (Apache-2.0 OR BSD-2-Clause)
URL:           https://pypi.python.org/pypi/%{pypi_name}
Source0:       %{pypi_source %{pypi_name} %{version}}

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-python3
%if %{without bootstrap}
BuildRequires: mingw32-python3-build
BuildRequires: mingw32-python3-flit-core
%endif

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-python3
%if %{without bootstrap}
BuildRequires: mingw64-python3-build
BuildRequires: mingw64-python3-flit-core
%endif

# Don't scan */bin/wheel for requires, it would generate a Requires: pythonX.Y
%global __requires_exclude_from ^.*/bin/wheel$

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
%if %{with bootstrap}
%global distinfo %{pypi_name}-%{version}+rpmbootstrap.dist-info
mkdir %{distinfo}
cat > %{distinfo}/METADATA << EOF
Metadata-Version: 2.2
Name: %{pypi_name}
Version: 1.0.1
EOF
%else
%global distinfo %{pypi_name}-%{version}.dist-info
%mingw32_py3_build_wheel
%mingw64_py3_build_wheel
%mingw32_py3_build_host_wheel
%mingw64_py3_build_host_wheel
%endif


%install
%if %{with bootstrap}
mkdir -p %{buildroot}%{mingw32_python3_sitearch}
mkdir -p %{buildroot}%{mingw64_python3_sitearch}
cp -a src/wheel %{distinfo} %{buildroot}%{mingw32_python3_sitearch}/
cp -a src/wheel %{distinfo} %{buildroot}%{mingw64_python3_sitearch}/
mkdir -p %{buildroot}%{mingw32_python3_hostsitearch}
mkdir -p %{buildroot}%{mingw64_python3_hostsitearch}
cp -a src/wheel %{distinfo} %{buildroot}%{mingw32_python3_hostsitearch}/
cp -a src/wheel %{distinfo} %{buildroot}%{mingw64_python3_hostsitearch}/
%else
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel
%mingw32_py3_install_host_wheel
%mingw64_py3_install_host_wheel
%endif


%files -n mingw32-python3-%{pypi_name}
%license LICENSE.txt
%if !%{with bootstrap}
%{mingw32_bindir}/wheel
%endif
%{mingw32_python3_sitearch}/%{pypi_name}/
%{mingw32_python3_sitearch}/%{distinfo}
%if !%{with bootstrap}
%{_prefix}/%{mingw32_target}/bin/wheel
%endif
%{mingw32_python3_hostsitearch}/%{pypi_name}/
%{mingw32_python3_hostsitearch}/%{distinfo}

%files -n mingw64-python3-%{pypi_name}
%license LICENSE.txt
%if !%{with bootstrap}
%{mingw64_bindir}/wheel
%endif
%{mingw64_python3_sitearch}/%{pypi_name}/
%{mingw64_python3_sitearch}/%{distinfo}
%if !%{with bootstrap}
%{_prefix}/%{mingw64_target}/bin/wheel
%endif
%{mingw64_python3_hostsitearch}/%{pypi_name}/
%{mingw64_python3_hostsitearch}/%{distinfo}


%changelog
* Tue Sep 22 2026 Sandro Mani <manisandro@gmail.com> - 0.48.0-2
- Rebuild (mingw-python)

* Sun Aug 16 2026 Sandro Mani <manisandro@gmail.com> - 0.48.0-1
- Update to 0.48.0

* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.47.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Sun Apr 26 2026 Sandro Mani <manisandro@gmail.com> - 0.47.0-1
- Update to 0.47.0

* Thu Jan 22 2026 Sandro Mani <manisandro@gmail.com> - 0.46.3-1
- Update to 0.46.3

* Thu Jan 22 2026 Sandro Mani <manisandro@gmail.com> - 0.46.2-1
- Update to 0.46.2

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.46.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.46.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Apr 15 2025 Sandro Mani <manisandro@gmail.com> - 0.46.1-1
- Update to 0.46.1

* Fri Apr 04 2025 Sandro Mani <manisandro@gmail.com> - 0.46.0-1
- Update to 0.46.0

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.45.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Nov 27 2024 Sandro Mani <manisandro@gmail.com> - 0.45.1-1
- Update to 0.45.1

* Sat Nov 09 2024 Sandro Mani <manisandro@gmail.com> - 0.45.0-1
- Update to 0.45.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.43.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Apr 14 2024 Sandro Mani <manisandro@gmail.com> - 0.43.0-1
- Update to 0.43.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.41.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.41.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Oct 12 2023 Sandro Mani <manisandro@gmail.com> - 0.41.2-1
- Update to 0.41.2

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.40.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 28 2023 Sandro Mani <manisandro@gmail.com> - 0.40.0-1
- Update to 0.40.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.38.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 19 2022 Sandro Mani <manisandro@gmail.com> - 0.38.4-1
- Update to 0.38.4

* Wed Oct 19 2022 Sandro Mani <manisandro@gmail.com> - 0.37.1-2
- Fix license
- Add host build
- Filter requires on */bin/wheel

* Tue Sep 27 2022 Sandro Mani <manisandro@gmail.com> - 0.37.1-1
- Initial build
