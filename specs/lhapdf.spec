Name:		lhapdf
Version:	6.5.5
Release:	1%{?dist}
Summary:	Les Houches Accord PDF Interface

License:	GPL-3.0-only
URL:		https://lhapdf.hepforge.org/
Source0:	https://www.hepforge.org/archive/lhapdf/LHAPDF-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	yaml-cpp-devel
BuildRequires:	python%{python3_pkgversion}-Cython
BuildRequires:	python%{python3_pkgversion}-devel
BuildRequires:	doxygen

#		Obsolete LHAPDF5 packages not provided by LHAPDF6
Obsoletes:	octave-lhapdf < 6
Obsoletes:	lhapdf-pdfsets-minimal < 6

%description
LHAPDF is a general purpose C++ interpolator, used for evaluating PDFs
from discretized data files. Previous versions of LHAPDF were written
in Fortran 77/90 and are documented at http://lhapdf.hepforge.org/lhapdf5/.

LHAPDF6 vastly reduces the memory overhead of the Fortran LHAPDF (from
gigabytes to megabytes!), entirely removes restrictions on numbers of
concurrent PDFs, allows access to single PDF members without needing
to load whole sets, and separates a new standardized PDF data format
from the code library so that new PDF sets may be created and released
easier and faster. The C++ LHAPDF6 also permits arbitrary parton
contents via the standard PDG ID code scheme, is computationally more
efficient (particularly if only one or two flavors are required at
each phase space point, as in PDF reweighting), and uses a flexible
metadata system which fixes many fundamental metadata and concurrency
bugs in LHAPDF5.

Compatibility routines are provided as standard for existing C++ and
Fortran codes using the LHAPDF5 and PDFLIB legacy interfaces, so you
can keep using your existing codes. But the new interface is much more
powerful and pleasant to work with, so we think you'll want to switch
once you've used it!

LHAPDF6 is documented in more detail in http://arxiv.org/abs/1412.7420

%package devel
Summary:	Les Houches Accord PDF Interface - development files
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides development files of LHAPDF, including C++ bindings.

%package -n python%{python3_pkgversion}-%{name}
Summary:	Les Houches Accord PDF Interface - Python 3 module
%py_provides	python%{python3_pkgversion}-%{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description -n python%{python3_pkgversion}-%{name}
This package provides Python 3 bindings for LHAPDF.
This package also provides a script called "lhapdf" which can be used
to query the catalog of PDF sets and to install and update them from
the command line. It accepts commands "list", "update", "install" and
"upgrade". Please run "lhapdf help" for full usage instructions.

%package doc
Summary:	Les Houches Accord PDF Interface - documentation
BuildArch:	noarch

%description doc
This package provides API documentation and examples for LHAPDF.

%prep
%setup -q -n LHAPDF-%{version}

# Remove cython generated file
rm wrappers/python/lhapdf.cpp

# Remove bundled yaml-cpp
rm -rf src/yamlcpp/

# Fix shebangs
sed 's!/usr/bin/env python!%{__python3}!' -i bin/lhapdf examples/*.py
sed 's!/usr/bin/env bash!/bin/bash!' -i bin/lhapdf-config.in

%build
%configure \
	--disable-static \
	--with-yaml-cpp \
	--enable-librelease \
	--docdir=%{_pkgdocdir} \
	PYTHON=%{__python3}
%make_build

# Build doxygen documentation
%make_build doxy

%install
%make_install

mkdir %{buildroot}%{python3_sitearch}/%{name}-%{version}.dist-info
cat << EOF > %{buildroot}%{python3_sitearch}/%{name}-%{version}.dist-info/METADATA
Name: %{name}
Version: %{version}
EOF

rm %{buildroot}%{_libdir}/libLHAPDF.la
find %{buildroot}%{_pkgdocdir}/examples -type f -a '!' -name '*.*' -delete

%check
%make_build check

%files
%{_libdir}/libLHAPDF-%{version}.so
%{_datadir}/LHAPDF
%doc AUTHORS ChangeLog
%license COPYING

%files devel
%{_bindir}/%{name}-config
%{_includedir}/LHAPDF
%{_libdir}/libLHAPDF.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n python%{python3_pkgversion}-%{name}
%{_bindir}/%{name}
%{python3_sitearch}/%{name}-%{version}.dist-info
%{python3_sitearch}/%{name}

%files doc
%doc %{_pkgdocdir}/doxygen
%doc %{_pkgdocdir}/examples
%license COPYING

%changelog
* Wed Jan 01 2025 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.5.5-1
- Update to version 6.5.5
- Drop soname patch, use new configure option --enable-librelease instead
- Unbundle yaml-cpp, using new configure option --with-yaml-cpp
- EPEL 7 EOL specfile cleanup

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 6.5.4-7
- Rebuilt for Python 3.13

* Mon Jun 03 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.5.4-6
- Eliminate use of obsolete patchN syntax

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 6.5.4-2
- Rebuilt for Python 3.12

* Mon Mar 13 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.5.4-1
- Update to version 6.5.4

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 6.4.0-3
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Dec 19 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.4.0-1
- Update to version 6.4.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 6.3.0-3
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 23 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.3.0-1
- Update to version 6.3.0
- Drop patch lhapdf-cython-configure.patch (previously backported)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 6.2.1-10
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 6.2.1-8
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 07 2019 Troy Dawson <tdawson@redhat.com> - 6.2.1-6
- Rebuilt to change main python from 3.4 to 3.6

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 10 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.2.1-5
- Drop Python 2 bindings for Fedora 29+
- Make Cython checking script usable with Python3 (backport)
- Add Python 3.6 package for EPEL 7

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 6.2.1-4
- Rebuild with fixed binutils

* Sun Jul 29 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.2.1-3
- Move lhapdf script to python3 package for Fedora 29+

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 04 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.2.1-1
- Update to version 6.2.1
- Change license tag from GPLv2+ to GPLv3+
- Add Python 3 bindings
- Drop packages not provided by LHAPDF6: octave-lhapdf, lhapdf-pdfsets-minimal

* Wed Feb 07 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.9.1-23
- Compile with -std=legacy when using gfortran >= 8

* Thu Aug 10 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.9.1-22
- Rename python package
- EPEL 5 End-Of-Life specfile clean-up
  - Remove Group and BuildRoot tags
  - Don't clear the buildroot in the install section
  - Remove the clean section
  - Remove octave packaging macro definitions

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.9.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Wed Feb 08 2017 Kalev Lember <klember@redhat.com> - 5.9.1-18
- Rebuilt for libgfortran soname bump

* Wed Dec 07 2016 Orion Poplawski <orion@cora.nwra.com> - 5.9.1-17
- Rebuild for octave 4.2

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.9.1-16
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 17 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.9.1-15
- Disable octave support for EPEL 6 ppc64 - octave no longer available

* Mon Feb 08 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.9.1-14
- Disable tests on arm

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 06 2015 Orion Poplawski <orion@cora.nwra.com> - 5.9.1-12
- Rebuild for octave 4.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.9.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 5.9.1-10
- Rebuilt for GCC 5 C++11 ABI change

* Sat Mar 07 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.9.1-9
- Fix lhacontrol common block in example

* Sun Oct 12 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.9.1-8
- Re-enable octave for EPEL 7

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jun 03 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.9.1-5
- Disable octave for EPEL 7 - not yet available

* Tue Jan 07 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.9.1-4
- Add "pkg load lhapdf" to octave example
- Fixes for EPEL 5

* Sat Dec 28 2013 Kevin Fenzi <kevin@scrye.com> - 5.9.1-3
- Rebuild to fix broken deps

* Thu Nov 21 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.9.1-2
- Remove bundled swig generated sources

* Tue Oct 29 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.9.1-1
- Update to version 5.9.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.8.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 18 2013 Dan Horák <dan[at]danny.cz> - 5.8.9-4
- don't run check on s390 - OOM when loading the library in Octave

* Wed Jun 05 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.8.9-3
- Make doc package independent

* Wed May 22 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.8.9-2
- Reduce libtool overlinking
- Add isa to dependencies

* Sat May 18 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.8.9-1
- Update to version 5.8.9

* Wed Nov 14 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.8.8-1
- Initial build
