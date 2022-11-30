Name:           libpoly
Version:        0.1.11
Release:        4%{?dist}
Summary:        C library for manipulating polynomials

License:        LGPL-3.0-or-later
URL:            https://sri-csl.github.io/libpoly/
Source0:        https://github.com/SRI-CSL/libpoly/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3dist(sympy)

%description
LibPoly is a C library for manipulating polynomials.  The target
applications are symbolic reasoning engines, such as SMT solvers, that
need to reason about polynomial constraints.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package     -n python3-%{name}
Summary:        Python 3 interface to %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python3-%{name}
This package contains a python 3 interface to %{name}.

%prep
%autosetup

# Install in the right place
if [ "%{_lib}" != "lib" ]; then
  sed -i 's/\(DESTINATION \)lib/\1%{_lib}/' src/CMakeLists.txt
fi

# Clean up hidden files before they get installed
find . -name .gitignore -delete

%build
%cmake %{_cmake_skip_rpath} \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DLIBPOLY_BUILD_STATIC:BOOL=OFF \
  -DLIBPOLY_BUILD_STATIC_PIC:BOOL=OFF
%cmake_build

%install
%cmake_install

# Install the python interface by hand
mkdir -p %{buildroot}%{python3_sitearch}
cp -p %{_vpath_builddir}/python/polypy.so %{buildroot}%{python3_sitearch}

%check
export LD_LIBRARY_PATH=$PWD/%{_vpath_builddir}/src
%ctest

%files
%license LICENCE
%doc README.md
%{_libdir}/libpoly.so.0*
%{_libdir}/libpolyxx.so.0*

%files devel
%{_includedir}/poly/
%{_libdir}/libpoly.so
%{_libdir}/libpolyxx.so

%files -n python3-%{name}
%{python3_sitearch}/polypy.so

%changelog
* Mon Nov 28 2022 Jerry James <loganjerry@gmail.com> - 0.1.11-4
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Python Maint <python-maint@redhat.com> - 0.1.11-3
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 25 2021 Jerry James <loganjerry@gmail.com> - 0.1.11-1
- Version 0.1.11
- Enable tests for 32-bit platforms

* Mon Jul 26 2021 Jerry James <loganjerry@gmail.com> - 0.1.10-1
- Version 0.1.10

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.9-2
- Rebuilt for Python 3.10

* Tue Apr 13 2021 Jerry James <loganjerry@gmail.com> - 0.1.9-1
- Version 0.1.9

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.8-2
- Rebuilt for Python 3.9

* Thu Mar 26 2020 Jerry James <loganjerry@gmail.com> - 0.1.8-1
- Version 0.1.8
- Add sympy BR for the tests
- Add the python3 interface
- Bring back the check script for 64-bit platforms; 32-bit platforms cannot
  run all tests due to the limited size of a C integer

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 30 2018 Jerry James <loganjerry@gmail.com> - 0.1.7-1
- New upstream version
- Drop python2-only interface; we'll bring it back when it is ported to python3
- Drop python-only check script

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul  3 2018 Jerry James <loganjerry@gmail.com> - 0.1.5-1
- New upstream version

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan  1 2018 Jerry James <loganjerry@gmail.com> - 0.1.4-1
- Initial RPM
