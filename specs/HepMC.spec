Name:		HepMC
Version:	2.06.11
Release:	15%{?dist}
Summary:	C++ Event Record for Monte Carlo Generators

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://hepmc.web.cern.ch/hepmc/
Source0:	http://hepmc.web.cern.ch/hepmc/releases/%{name}-%{version}.tar.gz

BuildRequires:	gcc-c++
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	make

%description
The HepMC package is an object oriented event record written in C++
for High Energy Physics Monte Carlo Generators. Many extensions from
HEPEVT, the Fortran HEP standard, are supported: the number of entries
is unlimited, spin density matrices can be stored with each vertex,
flow patterns (such as color) can be stored and traced, integers
representing random number generator states can be stored, and an
arbitrary number of event weights can be included. Particles and
vertices are kept separate in a graph structure, physically similar to
a physics event. The added information supports the modularization of
event generators. The package has been kept as simple as possible with
minimal internal/external dependencies. Event information is accessed
by means of iterators supplied with the package.

%package devel
Summary:	C++ Event Record for Monte Carlo Generators - development files
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides development files of HepMC.

%package doc
Summary:	C++ Event Record for Monte Carlo Generators - documentation
BuildArch:	noarch

%description doc
This package provides HepMC manuals and examples.

%prep
%setup -q

%build
autoreconf -i
%configure --with-momentum=GEV --with-length=MM --disable-static
%make_build

%install
%make_install

rm %{buildroot}%{_libdir}/libHepMC.la
rm %{buildroot}%{_libdir}/libHepMCfio.la

rm %{buildroot}%{_datadir}/%{name}/examples/pythia8/config.sh
rm %{buildroot}%{_datadir}/%{name}/examples/pythia8/config.csh
rm %{buildroot}%{_datadir}/%{name}/examples/pythia8/README

mkdir -p %{buildroot}%{_pkgdocdir}
mv %{buildroot}%{_datadir}/%{name}/examples %{buildroot}%{_pkgdocdir}
mv %{buildroot}%{_datadir}/%{name}/doc/HepMC2_reference_manual.pdf \
   %{buildroot}%{_pkgdocdir}/%{name}-reference-manual.pdf
mv %{buildroot}%{_datadir}/%{name}/doc/HepMC2_user_manual.pdf \
   %{buildroot}%{_pkgdocdir}/%{name}-user-manual.pdf
install -p -m 644 AUTHORS %{buildroot}%{_pkgdocdir}
install -p -m 644 ChangeLog %{buildroot}%{_pkgdocdir}
install -p -m 644 README %{buildroot}%{_pkgdocdir}

%check
%make_build check

%ldconfig_scriptlets

%files
%{_libdir}/libHepMC.so.*
%{_libdir}/libHepMCfio.so.*
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/AUTHORS
%doc %{_pkgdocdir}/ChangeLog
%doc %{_pkgdocdir}/README
%license COPYING

%files devel
%{_libdir}/libHepMC.so
%{_libdir}/libHepMCfio.so
%{_includedir}/%{name}

%files doc
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/examples
%doc %{_pkgdocdir}/*.pdf
%license COPYING

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.06.11-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.06.11-14
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.06.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.06.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.06.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.06.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.06.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.06.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.06.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Apr 06 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.06.11-6
- Use rpm make build macros

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.06.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.06.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.06.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.06.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 10 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.06.11-1
- Update to version 2.06.11
- Drop patches - all fixed in the new version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.06.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jul 28 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.06.10-1
- Update to version 2.06.10
- Drop patches - all fixed in the new version
- Drop the -ffp-contract=off hack
- Remove redundant m_outstream->setf(std::ios::fixed)
- Fix GenEventCopmpare
- Adjust expected test output for changes in the code

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.06.09-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.06.09-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 08 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.06.09-22
- Fix a segmentation fault (continue vs. break)

* Mon Jul 16 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.06.09-21
- Add BuildRequires on gcc-c++
- Packaging updates
  - Remove Group and BuildRoot tags
  - Don't clear the buildroot in the install section
  - Remove the clean section
  - Install license in licensedir (where applicable)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.06.09-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.06.09-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.06.09-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.06.09-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.06.09-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Oct 07 2016 Dan Horák <dan[at]danny.cz> - 2.06.09-15
- disable FMA on s390(x)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.06.09-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 17 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 2.06.09-13
- disable FMA on both aarch64 and ppc64(le) to pass all tests

* Thu Sep 03 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 2.06.09-12
- disable -fexpensive-optimizations for aarch64 to get it build

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.06.09-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.06.09-10
- Rebuilt for GCC 5 C++11 ABI change

* Fri Mar 06 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.06.09-9
- Increase epsilon - for i686 Fedora 22+ tests

* Fri Mar 06 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.06.09-8
- Do not trigger hexfloat output with gcc 5

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.06.09-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.06.09-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 08 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.06.09-5
- Use _pkgdocdir

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.06.09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 05 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.06.09-3
- Make doc package independent

* Wed May 22 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.06.09-2
- Add isa to dependencies

* Fri Nov 16 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.06.09-1
- Initial build
