%{?mingw_package_header}

# Disable debugsource packages
%undefine _debugsource_packages

%global pypi_name numpy

Name:          mingw-%{pypi_name}
Summary:       MinGW Windows Python %{pypi_name} library
Version:       1.26.4
Release:       3%{?dist}

# Everything is BSD except for class SafeEval in numpy/lib/utils.py which is Python
License:       BSD-3-Clause AND Apache-2.0
URL:           http://www.numpy.org/
Source0:       %{pypi_source}

# Don't use MSC specific stuff
# endian.h does not exist on mingw
Patch0:        numpy_mingw.patch
# Drop werror, fails with py3.11
Patch1:        numpy_werror.patch

BuildRequires: gcc-c++

BuildRequires: mingw32-filesystem >= 102
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-dlfcn
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-Cython
BuildRequires: mingw32-python3-setuptools

BuildRequires: mingw64-filesystem >= 102
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-dlfcn
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-Cython
BuildRequires: mingw64-python3-setuptools


%description
%package -n mingw32-python3-%{pypi_name}
Summary:       MinGW Windows Python3 %{pypi_name} library

%description -n mingw32-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name} library.


%package -n mingw64-python3-%{pypi_name}
Summary:       MinGW Windows Python3 %{pypi_name} library

%description -n mingw64-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name} library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%build
%mingw32_py3_build_host
%mingw64_py3_build_host
%mingw32_py3_build
%mingw64_py3_build


%install
%mingw32_py3_install_host
%mingw64_py3_install_host
%mingw32_py3_install
%mingw64_py3_install

# Symlink includedir
mkdir -p %{buildroot}%{mingw32_includedir}
mkdir -p %{buildroot}%{mingw64_includedir}
ln -s %{mingw32_python3_sitearch}/numpy/core/include/numpy/ %{buildroot}%{mingw32_includedir}/numpy
ln -s %{mingw64_python3_sitearch}/numpy/core/include/numpy/ %{buildroot}%{mingw64_includedir}/numpy
mkdir -p %{buildroot}%{_prefix}/%{mingw32_target}/include
mkdir -p %{buildroot}%{_prefix}/%{mingw64_target}/include
ln -s %{mingw32_python3_sitearch}/numpy/core/include/numpy/ %{buildroot}%{_prefix}/%{mingw32_target}/include/numpy
ln -s %{mingw64_python3_sitearch}/numpy/core/include/numpy/ %{buildroot}%{_prefix}/%{mingw64_target}/include/numpy

# Install missing files
for file in _numpyconfig.h __multiarray_api.h __ufunc_api.h; do
cp -a build_mingw32_host/src.linux-*-%{mingw32_python3_version}/numpy/core/include/numpy/${file} %{buildroot}%{mingw32_python3_hostsitearch}/%{pypi_name}/core/include/numpy/${file}
cp -a build_mingw32/src.mingw32-%{mingw32_python3_version}/numpy/core/include/numpy/${file} %{buildroot}%{mingw32_python3_sitearch}/%{pypi_name}/core/include/numpy/${file}
cp -a build_mingw64_host/src.linux-*-%{mingw64_python3_version}/numpy/core/include/numpy/${file} %{buildroot}%{mingw64_python3_hostsitearch}/%{pypi_name}/core/include/numpy/${file}
cp -a build_mingw64/src.mingw64-%{mingw64_python3_version}/numpy/core/include/numpy/${file} %{buildroot}%{mingw64_python3_sitearch}/%{pypi_name}/core/include/numpy/${file}
done


%files -n mingw32-python3-%{pypi_name}
%license LICENSE.txt
%{mingw32_bindir}/f2py
%{mingw32_includedir}/%{pypi_name}
%{mingw32_python3_sitearch}/%{pypi_name}/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}-py%{mingw32_python3_version}.egg-info/
%{_prefix}/%{mingw32_target}/bin/f2py
%dir %{_prefix}/%{mingw32_target}/include/
%{_prefix}/%{mingw32_target}/include/%{pypi_name}
%{mingw32_python3_hostsitearch}/%{pypi_name}/
%{mingw32_python3_hostsitearch}/%{pypi_name}-%{version}-py%{mingw32_python3_version}.egg-info/

%files -n mingw64-python3-%{pypi_name}
%license LICENSE.txt
%{mingw64_bindir}/f2py
%{mingw64_includedir}/%{pypi_name}
%{mingw64_python3_sitearch}/%{pypi_name}/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}-py%{mingw64_python3_version}.egg-info/
%{_prefix}/%{mingw64_target}/bin/f2py
%dir %{_prefix}/%{mingw64_target}/include/
%{_prefix}/%{mingw64_target}/include/%{pypi_name}
%{mingw64_python3_hostsitearch}/%{pypi_name}/
%{mingw64_python3_hostsitearch}/%{pypi_name}-%{version}-py%{mingw64_python3_version}.egg-info/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Sandro Mani <manisandro@gmail.com> - 1.26.4-1
- Update to 1.26.4

* Sat Feb 17 2024 Sandro Mani <manisandro@gmail.com> - 1.26.2-6
- Also install __ufunc_api.h

* Sat Feb 03 2024 Sandro Mani <manisandro@gmail.com> - 1.26.2-5
- Update numpy_mingw.patch: endian.h does not exist on mingw

* Sat Feb 03 2024 Sandro Mani <manisandro@gmail.com> - 1.26.2-4
- Fix missing files

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Dec 27 2023 Sandro Mani <manisandro@gmail.com> - 1.26.2-1
- Update to 1.26.2

* Tue Sep 26 2023 Sandro Mani <manisandro@gmail.com> - 1.26.0-1
- Update to 1.26.0

* Sat Jul 29 2023 Sandro Mani <manisandro@gmail.com> - 1.24.4-1
- Update to 1.24.4

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Apr 24 2023 Sandro Mani <manisandro@gmail.com> - 1.24.3-1
- Update to 1.24.3

* Tue Mar 21 2023 Sandro Mani <manisandro@gmail.com> - 1.24.2-4
- Install missing headers from target build also for host build

* Mon Mar 20 2023 Sandro Mani <manisandro@gmail.com> - 1.24.2-3
- Package headers

* Mon Mar 20 2023 Sandro Mani <manisandro@gmail.com> - 1.24.2-2
- Add host build

* Sun Mar 19 2023 Sandro Mani <manisandro@gmail.com> - 1.24.2-1
- Update to 1.24.2

* Sat Jan 28 2023 Sandro Mani <manisandro@gmail.com> - 1.24.1-1
- Update to 1.24.1

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 05 2022 Sandro Mani <manisandro@gmail.com> - 1.23.5-1
- Update to 1.23.5

* Wed Oct 19 2022 Sandro Mani <manisandro@gmail.com> - 1.23.4-1
- Update to 1.23.4

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.22.0-5
- Rebuild with mingw-gcc-12

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 1.22.0-4
- Rebuild for new python dependency generator (take two)

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 1.22.0-3
- Rebuild for new python dependency generator

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 07 2022 Sandro Mani <manisandro@gmail.com> - 1.22.0-1
- Update to 1.22.0

* Thu Dec 23 2021 Sandro Mani <manisandro@gmail.com> - 1.21.5-1
- Update to 1.21.5

* Sat Aug 07 2021 Sandro Mani <manisandro@gmail.com> - 1.21.1-1
- Update to 1.21.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 11 2021 Sandro Mani <manisandro@gmail.com> - 1.20.1-2
- Rebuild (python-3.10)

* Mon Feb 08 2021 Sandro Mani <manisandro@gmail.com> - 1.20.1-1
- Update to 1.20.1

* Wed Feb 03 2021 Sandro Mani <manisandro@gmail.com> - 1.20.0-1
- Update to 1.20.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 09 2021 Sandro Mani <manisandro@gmail.com> - 1.19.5-1
- Update to 1.19.5

* Wed Nov 04 2020 Sandro Mani <manisandro@gmail.com> - 1.19.4-1
- Update to 1.19.4

* Thu Oct 29 2020 Sandro Mani <manisandro@gmail.com> - 1.19.3-1
- Update to 1.19.3

* Fri Sep 11 2020 Sandro Mani <manisandro@gmail.com> - 1.19.2-1
- Update to 1.19.2

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Sandro Mani <manisandro@gmail.com> - 1.19.1-1
- Update to 1.19.1

* Tue Jun 23 2020 Sandro Mani <manisandro@gmail.com> - 1.19.0-1
- Update to 1.19.0

* Mon Jun 08 2020 Sandro Mani <manisandro@gmail.com> - 1.18.5-1
- Update to 1.18.5

* Sat May 30 2020 Sandro Mani <manisandro@gmail.com> - 1.18.4-2
- Rebuild (python-3.9)

* Mon May 04 2020 Sandro Mani <manisandro@gmail.com> - 1.18.4-1
- Update to 1.18.4

* Tue Apr 21 2020 Sandro Mani <manisandro@gmail.com> - 1.18.3-1
- Update to 1.18.3

* Wed Mar 18 2020 Sandro Mani <manisandro@gmail.com> - 1.18.2-1
- Update to 1.18.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Sandro Mani <manisandro@gmail.com> - 1.18.1-1
- Update to 1.18.1

* Mon Dec 30 2019 Sandro Mani <manisandro@gmail.com> - 1.18.0-1
- Update to 1.18.0

* Tue Nov 12 2019 Sandro Mani <manisandro@gmail.com> - 1.17.4-1
- Update to 1.17.4

* Thu Oct 24 2019 Sandro Mani <manisandro@gmail.com> - 1.17.3-2
- Link devel files to include dir
- Add missing headers

* Fri Oct 18 2019 Sandro Mani <manisandro@gmail.com> - 1.17.3-1
- Update to 1.17.3

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.17.2-2
- Rebuild (Changes/Mingw32GccDwarf2)

* Fri Sep 27 2019 Sandro Mani <manisandro@gmail.com> - 1.17.2-1
- Update to 1.17.2

* Fri Aug 02 2019 Sandro Mani <manisandro@gmail.com> - 1.17.0-1
- Update to 1.17.0
- Drop python2 packages

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 02 2019 Sandro Mani <manisandro@gmail.com> - 1.16.4-1
- Update to 1.16.4

* Wed May 01 2019 Sandro Mani <manisandro@gmail.com> - 1.16.3-2
- Add python3 subpackages

* Tue Apr 23 2019 Sandro Mani <manisandro@gmail.com> - 1.16.3-1
- Update to 1.16.3

* Wed Feb 27 2019 Sandro Mani <manisandro@gmail.com> - 1.16.2-1
- Update to 1.16.2

* Mon Feb 04 2019 Sandro Mani <manisandro@gmail.com> - 1.16.1-1
- Update to 1.16.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Sandro Mani <manisandro@gmail.com> - 1.16.0-1
- Update to 1.16.0

* Thu Aug 30 2018 Sandro Mani <manisandro@gmail.com> - 1.15.1-1
- Update to 1.15.1

* Thu Aug 02 2018 Sandro Mani <manisandro@gmail.com> - 1.15.0-1
- Update to 1.15.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 14 2018 Sandro Mani <manisandro@gmail.com> - 1.14.5-1
- Update to 1.14.5

* Wed May 02 2018 Sandro Mani <manisandro@gmail.com> - 1.14.3-1
- Update to 1.14.3

* Tue Mar 13 2018 Sandro Mani <manisandro@gmail.com> - 1.14.2-1
- Update to 1.14.2

* Thu Feb 22 2018 Sandro Mani <manisandro@gmail.com> - 1.14.1-1
- Update to 1.14.1

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 08 2017 Sandro Mani <manisandro@gmail.com> - 1.13.3-1
- Update to 1.13.3

* Fri Sep 29 2017 Sandro Mani <manisandro@gmail.com> - 1.13.2-1
- Update to 1.13.2

* Sat Sep 09 2017 Sandro Mani <manisandro@gmail.com> - 1.13.1-2
- Rebuild for mingw-filesystem

* Sat Sep 02 2017 Sandro Mani <manisandro@gmail.com> - 1.13.1-1
- Initial package
