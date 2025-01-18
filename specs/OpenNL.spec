%global soname libopennl.so

Name:           OpenNL
Version:        3.2.1
Release:        37%{?dist}
Summary:        A library for solving sparse linear systems

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://alice.loria.fr/index.php/software/4-library/23-opennl.html
Source0:        https://gforge.inria.fr/frs/download.php/27459/OpenNL3.2.zip

# Changes the soname from libnl.so to libopennl.so
Patch0:         OpenNL-3.2.1-library_soname.patch

BuildRequires:  cmake gcc-c++ gcc


%description
OpenNL (Open Numerical Library) is a library for solving sparse linear systems,
especially designed for the Computer Graphics community. The goal for OpenNL is
to be as small as possible, while offering the subset of functionalities
required by this application field. The Makefiles of OpenNL can generate a
single .c + .h file, very easy to integrate in other projects. The distribution
includes an implementation of our Least Squares Conformal Maps parameterization
method.

New version: OpenNL 3.2.1, includes support for CUDA and Fermi architecture
(Concurrent Number Cruncher and Nathan Bell's ELL formats)


OpenNL offers the following set of functionalities:

    Efficient sparse matrix data structure (for non-symmetric and symmetric
matrices)
    Iterative builder for sparse linear system
    Iterative builder for sparse least-squares problems
    Iterative solvers: conjugate gradient, BICGStab, GMRES
    Preconditionners: Jacobi, SSOR
    Iterative solver on the GPU (Concurrent Number Cruncher and Nathan Bell's
ELL)
    Sparse direct solvers: OpenNL can be linked with SuperLU
    Simple demo program with LSCM (Least Squares Conformal Maps)

%package devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the %{name} shared library that one can link against.

%prep
%setup -q -n %{name}%{version}
%patch -P0 -p1

%build
%cmake -DCMAKE_BUILD_TYPE:STRING=Release
%cmake_build


%install
# Install library
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/
install -p -m 0755  %{__cmake_builddir}/binaries/lib/libopennl.so.%{version} \
$RPM_BUILD_ROOT/%{_libdir}/

find  %{__cmake_builddir}/binaries/lib -type l -exec cp -a '{}' \
$RPM_BUILD_ROOT/%{_libdir}/ \;

# Correct encoding
pushd examples
    sed -i 's/\r//' make_test.bat
popd

# Install includes
install -d $RPM_BUILD_ROOT/%{_includedir}/NL/
cp -av src/NL/nl.h $RPM_BUILD_ROOT/%{_includedir}/
find src/NL/ -name "*.h" ! -name "nl.h" -execdir cp -av '{}' $RPM_BUILD_ROOT/%{_includedir}/NL/ \;

%files
%doc doc/*
%{_libdir}/%soname.3.2.1
%{_libdir}/%soname.3

%files devel
%doc examples
%{_libdir}/%soname
%{_includedir}/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 3.2.1-36
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 30 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.2.1-26
- Fix build

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-25
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.2.1-19
- Add gcc/g++ to BR
- Fix typo

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jan 06 2012 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.2.1-6
- spec bump for gcc 4.7 rebuild

* Sat Jul 16 2011 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.2.1-5
- fix doc macro usage

* Fri Jul 15 2011 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.2.1-4
- Modify install section

* Thu Jul 14 2011 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.2.1-3
- add version macros to soname etc.

* Thu Jul 14 2011 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.2.1-2
- add patch to correct libname and versioning (courtesy of Richard Shaw)

* Tue Jul 12 2011 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.2.1-1
- initial rpmbuild

