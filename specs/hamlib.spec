%if 0%{?fedora} || 0%{?rhel} >= 8
%global tclver 8.6
%global pyver 3
%global swigver swig
%else
%global tclver 8.5
%global pyver 2
%global swigver swig3
%endif

%global githash 028d750249ab00c8c362598c838b15e8aa6a2951
%global shorthash %(c=%{githash}; echo ${c:0:10})

Name:           hamlib
Version:        4.6
Release:        1%{?dist}
Summary:        Run-time library to control radio transceivers and receivers

License:        GPL-2.0-or-later and LGPL-2.0-or-later
URL:            http://www.hamlib.org
%if "%{githash}" == "0"
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
%else
Source0:        https://github.com/Hamlib/Hamlib/archive/%{githash}/%{name}-%{shorthash}.tar.gz
%endif

Patch0:         hamlib-4.0-perl_install.patch
# -lpython is not needed, https://github.com/Hamlib/Hamlib/issues/253
Patch1:         hamlib-4.0-drop-libpython.patch

ExcludeArch:    i686

BuildRequires:  automake autoconf libtool
BuildRequires:  make
BuildRequires:  gcc gcc-c++ %{?swigver}
BuildRequires:  gd-devel
BuildRequires:  doxygen
BuildRequires:  source-highlight
BuildRequires:  boost-devel
BuildRequires:  libtool-ltdl-devel
BuildRequires:  libusb1-devel
BuildRequires:  libxml2-devel
BuildRequires:  pkgconfig
BuildRequires:  python%{pyver}-devel
BuildRequires:  tcl-devel
#for perl
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)

# Filter provides from private libraries.
%{?perl_default_filter}


%description
Hamlib provides a standardized programming interface that applications
can use to send the appropriate commands to a radio.

Also included in the package is a simple radio control program 'rigctl',
which lets one control a radio transceiver or receiver, either from
command line interface or in a text-oriented interactive interface.

%package devel
Summary:        Development library to control radio transceivers and receivers
Requires:       hamlib%{?_isa} = %{version}-%{release}
Requires:       tcl-hamlib%{?_isa} = %{version}-%{release}

%description devel
Hamlib radio control library C development headers and libraries
for building C applications with Hamlib.

%package doc
Summary:        Documentation for the hamlib radio control library
BuildArch:      noarch

%description doc
This package provides the developers documentation for the hamlib radio
control library API.

%package c++
Summary:        Hamlib radio control library C++ binding
Requires:       hamlib%{?_isa} = %{version}-%{release}

%description c++
Hamlib radio control library C++ language binding.

%package c++-devel
Summary:        Hamlib radio control library C++ binding development headers and libraries
Requires:       hamlib-devel%{?_isa} = %{version}-%{release}
Requires:       hamlib-c++%{?_isa} = %{version}-%{release}

%description c++-devel
Hamlib radio control library C++ binding development headers and libraries
for building C++ applications with Hamlib.


%package -n perl-%{name}
Summary:        Hamlib radio control library Perl binding
Requires:       hamlib%{?_isa} = %{version}-%{release}
Obsoletes:      hamlib-perl < 3.0
Provides:       hamlib-perl = %{version}-%{release}

%description -n perl-%{name}
Hamlib PERL Language bindings to allow radio control from PERL scripts.


%package -n python%{pyver}-%{name}
%{?python_provide:%python_provide python2-%{name}}
Summary:        Hamlib radio control library Python binding
Requires:       hamlib%{?_isa} = %{version}-%{release}, python%{pyver}

%description -n python%{pyver}-%{name}
Hamlib Python Language bindings to allow radio control from Python scripts.

%package -n tcl-%{name}
Summary:        Hamlib radio control library TCL binding
Requires:       hamlib%{?_isa} = %{version}-%{release}
Provides:       hamlib-tcl = %{version}-%{release}
  
%description -n tcl-%{name}
Hamlib TCL Language bindings to allow radio control from TCL scripts.


%prep
%if "%{githash}" == "0"
%autosetup -p1
%else
%autosetup -p1 -n Hamlib-%{githash}
%endif

%build
%if 0%{?fedora} || 0%{?rhel} >= 8
export PYTHON=%{__python3}
%else
export PYTHON=%{__python2}
%endif

# Only run if we're working with a git checkout
#if 0%{?githash}
autoreconf -fi
#endif

%configure \
        --disable-static \
        --with-tcl=/usr/%{_lib} \
        --with-tcl-binding \
        --with-perl-binding \
        --with-python-binding \

%make_build

# Build Documentation
make -C doc doc


%install
%make_install

# Install documentation
mkdir -p %{buildroot}%{_docdir}/%{name}/html/search
for f in `find doc/html/ -type f -maxdepth 1`
        do install -D -m 0644 $f %{buildroot}%{_docdir}/%{name}/`echo $f | cut -d '/' -f2`
done
for f in `find doc/html/search -type f -maxdepth 1`
        do install -D -m 0644 $f %{buildroot}%{_docdir}/%{name}/html/`echo $f | cut -d '/' -f3`
 done

# Move installed docs to include them in subpackage via %%doc magic
rm -rf __tmp_doc ; mkdir __tmp_doc
mv %{buildroot}%{_docdir}/%{name}/* __tmp_doc


# Fix permissions
find %{buildroot} -type f -name Hamlib.so -exec chmod 0755 {} ';'

# Remove unneeded files
find %{buildroot} -name \*.la -exec rm -f {} ';'
find %{buildroot} -type f -name pkgIndex.tcl -exec rm -f {} ';'
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name Hamlib.bs -exec rm -f {} ';'
find %{buildroot} -type f -name perltest.pl -exec rm -f {} ';'


%check
make V=1 check

%ldconfig_scriptlets

%ldconfig_scriptlets c++

%ldconfig_scriptlets -n tcl-hamlib


%files
%license COPYING
%doc AUTHORS ChangeLog PLAN README THANKS
%{_bindir}/*
%{_libdir}/libhamlib.so.*
%{_mandir}/man?/*

%files devel
%doc README.developer
%{_libdir}/libhamlib.so
%{_libdir}/tcl%{tclver}/Hamlib/hamlibtcl.so
%{_datadir}/aclocal/hamlib.m4
%dir %{_includedir}/hamlib
%{_includedir}/hamlib/ampclass.h
%{_includedir}/hamlib/amplifier.h
%{_includedir}/hamlib/amplist.h
#{_includedir}/hamlib/config.h
%{_includedir}/hamlib/multicast.h
%{_includedir}/hamlib/rig.h
%{_includedir}/hamlib/riglist.h
%{_includedir}/hamlib/rig_dll.h
%{_includedir}/hamlib/rotator.h
%{_includedir}/hamlib/rotlist.h
%{_libdir}/pkgconfig/hamlib.pc

%files doc
%doc __tmp_doc/*

%files c++
%{_libdir}/libhamlib++.so.*

%files c++-devel
%{_libdir}/libhamlib++.so
%{_includedir}/hamlib/rigclass.h
%{_includedir}/hamlib/rotclass.h

%files -n perl-hamlib
%{perl_vendorarch}/*

%files -n python%{pyver}-%{name}
%if 0%{?fedora} || 0%{?rhel} >= 8
%{python3_sitearch}/*.py*
%{python3_sitearch}/_Hamlib.so
%{python3_sitearch}/__pycache__/Hamlib.*
%else
%{python2_sitearch}/*.py*
%{python2_sitearch}/_Hamlib.so
%endif

%files -n tcl-hamlib
%{_libdir}/tcl%{tclver}/
%exclude %{_libdir}/tcl%{tclver}/Hamlib/hamlibtcl.so


%changelog
* Wed Dec 25 2024 Richard Shaw <hobbes1069@gmail.com> - 4.6-1
- Update to 4.6.

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 12 2024 Jitka Plesnikova <jplesnik@redhat.com> - 4.5.5-8
- Perl 5.40 rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 4.5.5-7
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 4.5.5-3
- Perl 5.38 rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 4.5.5-2
- Rebuilt for Python 3.12

* Mon May 29 2023 Richard Shaw <hobbes1069@gmail.com> - 4.5.5-1
- Update to 4.5.5.

* Sun Jan 22 2023 Richard Shaw <hobbes1069@gmail.com> - 4.5.4-1
- Update to 4.5.4.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jan 01 2023 Richard Shaw <hobbes1069@gmail.com> - 4.5.3-1
- Update to 4.5.3.

* Sun Dec 25 2022 Richard Shaw <hobbes1069@gmail.com> - 4.5.2-1
- Update to 4.5.2.

* Mon Nov 07 2022 Richard Shaw <hobbes1069@gmail.com> - 4.5-1
- Update to 4.5.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.4-4
- Rebuilt for Python 3.11

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 4.4-3
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 22 2021 Richard Shaw <hobbes1069@gmail.com> - 4.4-1
- Update to 4.4.

* Mon Oct 11 2021 Richard Shaw <hobbes1069@gmail.com> - 4.3.1-1
- Update to 4.3.1.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.2-2
- Rebuilt for Python 3.10

* Sun May 30 2021 Richard Shaw <hobbes1069@gmail.com> - 4.2-1
- Update to 4.2.

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 4.1-2
- Perl 5.34 rebuild

* Mon Feb 01 2021 Richard Shaw <hobbes1069@gmail.com> - 4.1-1
- Update to 4.1.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 25 2020 Richard Shaw <hobbes1069@gmail.com> - 4.0-2
- Add additional modes known to flrig but not hamlib.

* Fri Dec 25 2020 Richard Shaw <hobbes1069@gmail.com> - 4.0-1
- Update to 4.0 final.

* Thu Nov 26 2020 Richard Shaw <hobbes1069@gmail.com> - 4.0-0.13.20201126gitd8be93350f
- Update to latest git checkout to fix Kenwood retries issue.

* Thu Nov 12 2020 Richard Shaw <hobbes1069@gmail.com> - 4.0-0.12.20201111gitc7de6e8b19
- Update to latest Hamlib 4.0 branch.

* Mon Sep 28 2020 Richard Shaw <hobbes1069@gmail.com> - 4.0-0.11.20200928gitc9cfd40e91
- Update to latest git checkout, c9cfd40e91a225184f8e9423cd93015c94a57385.

* Sat Sep 12 2020 Richard Shaw <hobbes1069@gmail.com> - 4.0-0.10.20200912gitd47987db85
- Update to latest git checkout.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-0.9.20200615git779cd69287
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 4.0-0.8.20200615git779cd69287
- Perl 5.32 rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 4.0-0.7.20200615git779cd69287
- Perl 5.32 rebuild

* Mon Jun 15 2020 Richard Shaw <hobbes1069@gmail.com> - 4.0-0.6.20200615git779cd69287
- Update to master.

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0-0.5.20200409git6269bc4dec
- Rebuilt for Python 3.9

* Tue May 19 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.0-0.4.20200409git6269bc4dec
- Do not link with -lpython

* Thu Apr 09 2020 Richard Shaw <hobbes1069@gmail.com> - 4.0-0.3.20200409git6269bc4dec
- Update to 4.0.20200409git6269bc4dec.

* Tue Mar 31 2020 Richard Shaw <hobbes1069@gmail.com> - 4.0-0.1
- Update to git checkout as wsjtx requires it and hamlib has not released
  in quite some time.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3-7
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.3-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 04 2018 Richard Shaw <hobbes1069@gmail.com> - 3.3-3
- Correct __pycache__ reference in %%files.

* Wed Oct 03 2018 Richard Shaw <hobbes1069@gmail.com> - 3.3-2
- Replace python 2 module with python 3.

* Thu Aug 30 2018 Richard Shaw <hobbes1069@gmail.com> - 3.3-1
- Update to 3.3.

* Fri Jul 20 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 3.2-5
- Fixed FTBFS by adding gcc-c++ requirement
  Resolves: rhbz#1604307

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.2-3
- Perl 5.28 rebuild

* Tue Jun 19 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 3.2-2
- Dropped info scriptlets, it's now handled automatically by trigger

* Tue Apr 03 2018 Richard Shaw <hobbes1069@gmail.com> - 3.2-1
- Update to 3.2.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 08 2017 Richard Shaw <hobbes1069@gmail.com> - 3.1-10
- Fix ambiguous Python 2 dependency declarations
  https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Fri Sep  1 2017 Richard Shaw <hobbes1069@gmail.com> - 3.1-9
- Update upstream URL for package, fixes RHBZ#1487568.
- Patch pkgconfig file to correct lib dir, fixes RHBZ#1487575.

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.1-8
- Python 2 binary package renamed to python2-hamlib
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 3.1-5
- Rebuilt for Boost 1.64

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.1-4
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 3.1-2
- Rebuilt for Boost 1.63

* Sun Jan  1 2017 Richard Shaw <hobbes1069@gmail.com> - 3.1-1
- Update to latest upstream release.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3.0.1-4
- Perl 5.24 rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 3.0.1-2
- Rebuilt for Boost 1.60

* Thu Jan  7 2016 Richard Shaw <hobbes1069@gmail.com> - 3.0.1-1
- Update to latest upstream release.

* Thu Sep 24 2015 Richard Shaw <hobbes1069@gmail.com> - 3.0-3
- Fix devel package dependency on tcl-hamlib.
- Fix devel package requires.
- Make provides version and release specific.

* Tue Sep 22 2015 Jitka Plesnikova <jplesnik@redhat.com> - 3.0-2
- Rebuild against new swig (BZ#1192849)

* Sat Sep 19 2015 Richard Shaw <hobbes1069@gmail.com> - 3.0-1
- Update to latest upstream release.

* Wed Sep  2 2015 Richard Shaw <hobbes1069@gmail.com> - 3.0-0.1.rc1
- Update to latest upstream release candidate.
- Rename binding package names to be compliant with the package naming
  guidelines.
- Clean up spec cruft.

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.2.15.3-20
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.15.3-19
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159
 
* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.2.15.3-18
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.15.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.2.15.3-16
- Perl 5.22 rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.2.15.3-15
- Rebuilt for GCC 5 C++11 ABI change

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 1.2.15.3-14
- Rebuild for boost 1.57.0

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.2.15.3-13
- Perl 5.20 rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.15.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul  1 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 1.2.15.3-11
- Moved arch python module to sitearch dir, resolved multilib conflict
  Resolves: rhbz#1030768

* Tue Jun 24 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 1.2.15.3-10
- Switched to recent dependency filtering system,
  it should resolve most of the multilib conflicts

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.15.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 1.2.15.3-8
- Rebuild for boost 1.55.0

* Tue May 20 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 1.2.15.3-7
- Rebuilt for tcl/tk8.6

* Sat Dec 14 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 1.2.15.3-6
- Fix duplicate documentation (#1001257)
- License included only in base package, subpackages that depend on
  base package don't need to include it again
- Build noarch HTML -doc subpackage
- Include %%_libdir/hamlib directory
- Drop obsolete spec buildroot definition/removal and %%clean
- Add %%?_isa to explicit package deps
- Remove %%defattr

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.15.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 1.2.15.3-4
- Rebuild for boost 1.54.0

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.2.15.3-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.15.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 06 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 1.2.15.3-1
- New version
  Resolves: rhbz#846438

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 14 2012 Lucian Langa <cooly@gnome.eu.org> - 1.2.15.1-1
- remove gnuradio dependency as we do not require it
- drop temporary patch
- new upstream release

* Sun Feb 05 2012 Lucian Langa <cooly@gnome.eu.org> - 1.2.15-1
- add temporary patch to fix usrmove issues
- drop patch 1 - no longer building with usrp
- drop patch 2 - fixed upstream
- new upstream release

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 29 2011 Randall "Randy" Berry <dp67@fedoraproject.org> - 1.2.14-4
- Rebuild to fix broken deps libusrp

* Wed Dec 07 2011 Randall "Randy" Berry <dp67@fedoraproject.org> - 1.2.14-3
- Rebuild to fix broken deps libusrp

* Wed Dec 07 2011 Randall "Randy" Berry <dp67@fedoraproject.org> - 1.2.14-2
- Rebuild to fix broken deps libusrp
- Apply --without-usrp

* Sun Jul 31 2011 Lucian Langa <cooly@gnome.eu.org> - 1.2.14-1
- new upstream release

* Mon Jul 04 2011 Lucian Langa <cooly@gnome.eu.org> - 1.2.13.1-2
- add patch to fix building with latest gnuradio

* Thu Jun 16 2011 Lucian Langa <cooly@gnome.eu.org> - 1.2.13.1-1
- new upstream release

* Sun Apr 24 2011 Lucian Langa <cooly@gnome.eu.org> - 1.2.13-1
- setup filter provides for libdir/hamlib
- update bindings patch
- new upstream release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 2 2011 Randall "Randy" Berry N3LRX <dp67@fedoraproject.org> - 1.2.12-3
- Rebuild to fix broken deps libxml2

* Fri Nov 05 2010 Lucian Langa <cooly@gnome.eu.org> - 1.2.12-2
- update bindings patch
- rebuild against newer libxml2

* Mon Sep 6 2010 Randall "Randy" Berry <dp67@fedoraproject.org> - 1.2.12-1
- New upstream release
- Apply patches to new source
- Removed patch1 applied upstream (usrp.patch)
- Upstream-release-monitoring bz 630702
- Upstream changes:
- New models: PCR-2500, RX331, TRP 8255 S R
- New rotator backends: DF9GR's ERC
- Fixes and features: Paragon, TS-690S, FT-920, FT-990, FT-2000,
- Elektor SDR-USB, IC-7000, IC-7700, AR-8200, AR-8600

* Mon Aug 2 2010 Randall "Randy" Berry <dp67@fedoraproject.org> - 1.2.11-5
- Rebuild

* Mon Aug 2 2010 Randall "Randy" Berry <dp67@fedoraproject.org> - 1.2.11-4
- Build against Python 2.7
- Fix broken dep python2.7

* Sat Jul 31 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.2.11-3
- Rebuild for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1.2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Jul 01 2010 Lucian Langa <cooly@gnome.eu.org> - 1.2.11-1
- update bindings patch
- drop patch2 - fixed upstream
- new upstream release

* Sun May 09 2010 Lucian Langa <cooly@gnome.eu.org> - 1.2.10-4
- description cleanup
- add patch2 - fix double-free in cleanup in dummy module (#587701)

* Sun Nov 08 2009 Lucian Langa <cooly@gnome.eu.org> - 1.2.10-3
- various cleanups
- disable rpath
- rebuild using system libltdl

* Sat Nov 07 2009 Lucian Langa <cooly@gnome.eu.org> - 1.2.10-2
- build with usrp backend

* Sat Nov 07 2009 Lucian Langa <cooly@gnome.eu.org> - 1.2.10-1
- new upstream release

* Sun Aug 23 2009 Lucian Langa <cooly@gnome.eu.org> - 1.2.9-1
- new install rule for docs for new doxygen
- misc cleanups
- patch0 update
- new upstream release

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 01 2009 Sindre Pedersen Bjørdal <sindrepb@fedoraproject.org> - 1.2.8-3
- Add hackish fix for python binding issue

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 15 2008 Sindre Pedersen Bjørdal <sindrepb@fedoraproject.org> - 1.2.8-1
- New upstream release

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.2.7-3
- Rebuild for Python 2.6

* Tue Aug 26 2008 Steve Conklin <fedora@conklinhouse.com> - 1.2.7-2
- New patch to fix hamlib-perl

* Fri Feb 15 2008 Steve Conklin <sconklin@redhat.com> - 1.2.7-1
- New upstream released

* Thu Feb 14 2008 Steve Conklin <sconklin@redhat.com> - 1.2.6.2-7
- Rebuild against new gcc4.3

* Thu Jan 03 2008 Alex Lancaster <alexlan[AT]fedoraproject.org> - 1.2.6.2-6
- Rebuild against new Tcl 8.5

* Sun Dec 09 2007 Sindre Pedersen Bjørdal - 1.2.6.2-5
- use sitearch not sitelib for perl package
- Make sure it builds on all arches

* Sat Dec 08 2007 Sindre Pedersen Bjørdal - 1.2.6.2-3
- Clean up BuildRequires
- Remove obsolete swig patch

* Sat Dec 08 2007 Sindre Pedersen Bjørdal - 1.2.6.2-2
- Spec file cleanups
- Use make install instead of depriciated %%makeinstall
- Replace make trickery with patched upstream makefiles
- enable perl bindings
- Patch bindings makefile to install perl to vendor, not site
- Merge swig patch with bindings patch
- enable tcl bindings
- Create doc subpackage, solves #341481
- Remove 2nd bindings patch, not needed as we don't rely on make trickery for bindings anymore
- Add patch to install python bindings in proper python dirs
- Clean up %%files list
- Depend on version-release, not just version

* Tue Sep 25 2007 Denis Leroy <denis@poolshark.org> - 1.2.6.2-1
- Update to new upstream 1.2.6.2
- Added rigsmtr binary

* Mon Sep  3 2007 Denis Leroy <denis@poolshark.org> - 1.2.5-6
- Rebuild, License tag update
- Added net-tools BR

* Wed May  9 2007 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 1.2.5-5
- Move HTML devel documentation to the proper subpackage (#228364)

* Thu Dec 14 2006 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.2.5-4
- Rebuild for new Python

* Sat Sep 30 2006 Dennis Gilmore <dennis@ausil.us> 1.2.5-3
- fix Requires for hamlib-devel  its pkgconfig not pkg-config

* Sat Sep 30 2006 Dennis Gilmore <dennis@ausil.us> 1.2.5-2
- Fix BuildRequires added libxml2-devel, tcl-devel
- libusb-devel, pkgconfig  pkgconfig is required for fc5  as 
- libusb-devel doesnt require it there  but it wont hurt other 
- releases

* Sat Jul 29 2006 Robert 'Bob' Jensen <bob@bobjensen.com> 1.2.5-1
- Upstream update
- Spec file cleanups

* Sun Feb 19 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.2.4-3
- Fix bindings problems
- Remove static libs
- Remove .la files

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Wed Apr  6 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.2.4-1
- Upstream update
- Spec file cleanups

* Wed Mar 23 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.2.3-9
- Python binding cleanup
- soname/ldconfig cleanup
- Added %%{_includedir}/hamlib to -devel
- Removed %%{_libdir}/hamlib-*.a and hamlib-*.la
- %%doc cleanups

* Wed Mar 23 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.2.3-8
- Added -q to %%setup
- Fixed Python binding build and Requires

* Mon Mar 21 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.2.3-7
- Removed spurious period and spelling mistake in Summary

* Sat Mar 19 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.2.3-6
- %%

* Thu Mar 17 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.2.3-5
- Removed spurious Requires(...)

* Thu Mar 17 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.2.3-4
- Fixed %%post and %%postun along with Requires(...)

* Wed Mar 16 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.2.3-3
- Spell-corrected %%description

* Wed Mar 16 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.2.3-2
- Removed/fixed explicit Requires

* Tue Mar 15 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.2.3-1
- Bump release to 1
- Fixed BuildRoot

* Thu Feb 10 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0:1.2.3-0.iva.1
- Fixed error with automake in -devel (#26)

* Mon Jan 31 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0:1.2.3-0.iva.0
- Upstream update

* Sun Jan  9 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0:1.2.2-0.iva.1
- Fixed %%files %%defattr

* Sun Jan  9 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0:1.2.2-0.iva.0
- Ported to FC3
- Upgraded to 1.2.2

* Sun Apr 18 2004 David L Norris <dave@webaugur.com>
- Enable disabled script bindings.
- Touch up descriptions.

* Tue Jan 20 2004 Tomi Manninen
- Fix for 1.1.5pre2
- Better use of rpm macros
- Disable all bindings

* Wed Oct 08 2003 Joop Stakenborg
- Fix 'make rpm' again by disabling c++ bindings.
- rotclass.h and rigclass.h go into the devel package for now (FIXME)

* Wed Jan 15 2003 Joop Stakenborg
- Fix the spec file for 1.1.4CVS
- 'make rpm' should work now

* Mon Jun 17 2002 Stephane Fillod
- Added rotator support
- Added RPC daemon, hamlib.m4
- Upstream version 1.1.3

* Wed Jul 18 2001 Stephane Fillod
- Made initial "working" SPEC file

