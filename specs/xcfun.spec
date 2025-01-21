%global soname 2

Name:    xcfun
Version: 2.1.1
Release: 16%{?dist}
Summary: A library of approximate exchange-correlation functionals
License: MPL-2.0
URL:     https://xcfun.readthedocs.io
Source0: https://github.com/dftlibs/xcfun/archive/v%{version}/%{name}-%{version}.tar.gz

# Patch out potential array overflow
Patch0:  https://github.com/dftlibs/xcfun/pull/154.patch
# Fix build on 32-bit architectures
Patch1:  https://github.com/dftlibs/xcfun/pull/155.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gcc-gfortran
BuildRequires: make
BuildRequires: python3-devel
BuildRequires: pybind11-devel

# For tests
BuildRequires: python3-numpy
BuildRequires: python3-pytest

%description
XCFun is a library of approximate exchange-correlation functionals,
used in the Density Functional Theory description of electronic
structure. Because XCFun is based on automatic differentiation the
library can provide arbitrary order derivatives of all supported
functionals. Only the exchange-correlation energy expression needs to
be implemented, which is a huge gain in productivity (and also
efficiency). For this reason the library is very well suited for high
order time dependent DFT or for the development of new functionals.

%package devel
Summary:  Development headers and libraries for XCFun
Requires: %{name}%{?_isa} = %{version}-%{release}
# For dir ownership
Requires: cmake

%description devel
XCFun is a library of approximate exchange-correlation functionals,
used in the Density Functional Theory description of electronic
structure. Because XCFun is based on automatic differentiation the
library can provide arbitrary order derivatives of all supported
functionals. Only the exchange-correlation energy expression needs to
be implemented, which is a huge gain in productivity (and also
efficiency). For this reason the library is very well suited for high
order time dependent DFT or for the development of new functionals.

This package contains the development headers and libraries necessary
to compile code against XCFun.

%package -n python3-xcfun
Summary:  Python bindings for XCFun

%description -n python3-xcfun
XCFun is a library of approximate exchange-correlation functionals,
used in the Density Functional Theory description of electronic
structure. Because XCFun is based on automatic differentiation the
library can provide arbitrary order derivatives of all supported
functionals. Only the exchange-correlation energy expression needs to
be implemented, which is a huge gain in productivity (and also
efficiency). For this reason the library is very well suited for high
order time dependent DFT or for the development of new functionals.

This package contains the Python bindings for XCFun.

%prep
%setup -q
%patch -P0 -p1 -b .overflow
%patch -P1 -p1 -b .32bit

%build
%cmake -B %{_host} -DCMAKE_BUILD_TYPE=RelWithDebInfo -DLIB=%{_lib} -DXCFUN_PYTHON_INTERFACE=ON -DPYMOD_INSTALL_LIBDIR=../../%{python3_sitearch}
%make_build -C %{_host}

%install
%make_install -C %{_host}
# Fix test permissions
chmod u=rwX,og=rX -R %{buildroot}%{python3_sitearch}/xcfun/tests

%check
cd %{_host}
ctest --output-on-failure

%files
%license LICENSE.md
%doc CHANGELOG.md README.md
%{_libdir}/libxcfun.so.%{soname}*

%files devel
%{_datadir}/cmake/XCFun/
%{_includedir}/XCFun/
%{_libdir}/libxcfun.so

%files -n python3-xcfun
%{python3_sitearch}/xcfun

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jun 20 2024 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.1.1-14
- Modernize patch syntax.

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 2.1.1-13
- Rebuilt for Python 3.13

* Sat Apr 13 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1.1-12
- convert license to SPDX

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.1.1-9
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.1.1-6
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 08 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.1.1-5
- Patches to fix 32-bit builds and potential array overflow.

* Fri Jul 30 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.1.1-4
- Disable 32-bit architectures which are not supported by xcfun.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.1.1-2
- Review fixes

* Mon May 17 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.1.1-1
- First release
