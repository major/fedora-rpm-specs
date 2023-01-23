%if 0%{?fedora}
%bcond_without python
%endif

# Use devtoolset 8
%if 0%{?rhel} && 0%{?rhel} == 7
%global dts devtoolset-8-
%endif

Name:    spglib
Summary: C library for finding and handling crystal symmetries
Version: 1.16.1
Release: 7%{?dist}
License: BSD
URL:     https://spglib.github.io/%{name}/
Source0: https://github.com/atztogo/%{name}/archive/%{version}.zip#/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: cmake3, %{?dts}gcc, %{?dts}gcc-c++
%{?el7:BuildRequires: python-srpm-macros}

%description
C library for finding and handling crystal symmetries.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for developing
applications that use spglib.

%if %{with python}
%package -n python%{python3_pkgversion}-%{name}
Summary: Python3 library of %{name}
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools
BuildRequires: python%{python3_pkgversion}-numpy
BuildRequires: python%{python3_pkgversion}-pytest
BuildRequires: python3-pyyaml >= 5.1
Requires: python%{python3_pkgversion}-numpy
%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}}

%description -n python%{python3_pkgversion}-%{name}
This package contains the libraries to 
develop applications with %{name} Python3 bindings.
%endif

%prep
%autosetup -n %{name}-%{version}

%build
mkdir -p build
%if 0%{?el7}
%{?dts:source /opt/rh/devtoolset-8/enable}
%endif
%cmake3 -B build -DCMAKE_INSTALL_INCLUDEDIR:PATH=include/%{name}
%make_build -C build

%if %{with python}
pushd python
%py3_build
popd
%endif

%install
%make_install -C build

# Remove static libraries
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a

%if %{with python}
pushd python
%py3_install
popd
%endif

%check
%if %{with python}
pushd python/test
%pytest -v
popd
%endif

%files
%doc README.md
%license COPYING
%{_libdir}/lib*.so.*

%files devel
%{_libdir}/lib*.so
%{_includedir}/%{name}/

%if %{with python}
%files -n python%{python3_pkgversion}-%{name}
%license COPYING
%{python3_sitearch}/%{name}/
%{python3_sitearch}/%{name}-*.egg-info/
%endif

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.16.1-5
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.16.1-2
- Rebuilt for Python 3.10

* Sat Jan 30 2021 Antonio Trande <sagitter@fedoraproject.org> - 1.16.1-1
- Release 1.16.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Jeff Law <law@redhat.com> - 1.15.1-2
- Use __cmake_in_source_build

* Wed Jun 24 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.15.1-1
- Release 1.15.1
- BuildRequires python3-setuptools explicitly

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.14.1-3
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.14.1-1
- Release 1.14.1
- Use CMake method
- Use devtools-8 on EPEL 7

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.11.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.11.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 20 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.11.1-1
- Update to 1.11.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.10.3-2
- Rebuilt for Python 3.7

* Thu Feb 22 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.10.2-3
- Update to 1.10.3

* Sat Feb 17 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.10.2-3
- Use %%ldconfig_scriptlets

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 14 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.10.2-1
- Update to 1.10.2

* Fri Dec 08 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.10.1-2
- Fix upstream bug #41

* Thu Nov 23 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.10.1-1
- Update to 1.10.1
- Build Python package on epel7

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.9-7.20170325git825e80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.9-6.20170325git825e80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 22 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.9.9-5.20170615git825e80
- Modified for epel builds

* Sun Mar 26 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.9.9-4.20170615git825e80
- Update to git commit #825e80

* Thu Mar 16 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.9.9-3.20170615gitbf4b4c7
- Update to git commit #bf4b4c7

* Mon Mar 13 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.9.9-2
- Fix obsolete m4 macro

* Fri Mar 10 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.9.9-1
- First package
