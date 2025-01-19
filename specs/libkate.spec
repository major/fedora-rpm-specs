%if 0%{?fedora} || 0%{?rhel} >= 8
%global _without_python2 1
%endif

Name:           libkate
Version:        0.4.1
Release:        33%{?dist}
Summary:        Libraries to handle the Kate bitstream format

License:        BSD-3-Clause
URL:            https://gitlab.xiph.org/xiph/kate
Source0:        http://libkate.googlecode.com/files/libkate-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
%if 0%{!?_without_python2}
BuildRequires:  python2-devel
%endif
BuildRequires:  libogg-devel
BuildRequires:  liboggz
BuildRequires:  libpng-devel
BuildRequires:  bison
BuildRequires:  flex
%ifarch %{valgrind_arches}
BuildRequires:  valgrind
%endif
BuildRequires:  doxygen
 

%description
This is libkate, the reference implementation of a codec for the Kate bitstream
format.
Kate is a karaoke and text codec meant for encapsulation in an Ogg container.
It can carry text, images, and animate them.

Kate is meant to be used for karaoke alongside audio/video streams (typically
Vorbis and Theora), movie subtitles, song lyrics, and anything that needs text
data at arbitrary time intervals.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libogg-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package utils
Summary:        Encoder/Decoder utilities for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       liboggz

%description utils
The %{name}-utils package contains the katedec/kateenc binaries for %{name}.

%package docs
Summary:        Documentation for %{name}

BuildArch:      noarch

%description docs
The %{name}-docs package contains the docs for %{name}.


%prep
%setup -q

# We regenerate theses files at built step
rm tools/kate_parser.{c,h}
rm tools/kate_lexer.c


%build
%if 0%{!?_without_python2}
export PYTHON=python2
%else
export PYTHON=:
%endif
%configure --disable-static

# Remove rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build


%install
%if 0%{!?_without_python2}
export PYTHON=python2
%else
export PYTHON=:
%endif
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# Fix for header timestramps
touch -r %{buildroot}%{_includedir}/kate/kate_config.h \
 %{buildroot}%{_includedir}/kate/kate.h

%if 0%{?_without_python2}
rm -rf %{buildroot}%{_mandir}/man1/KateDJ.1*
%endif


%check
make check


%files
%exclude %{_docdir}/libkate/html
%doc %{_docdir}/libkate
%{_libdir}/*.so.*

%files devel
%doc examples/
%{_includedir}/kate/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files utils
%if 0%{!?_without_python2}
%{python2_sitelib}/kdj/
%{_bindir}/KateDJ
%{_mandir}/man1/KateDJ.*
%endif
%{_bindir}/katalyzer
%{_bindir}/katedec
%{_bindir}/kateenc
%{_mandir}/man1/katalyzer.*
%{_mandir}/man1/katedec.*
%{_mandir}/man1/kateenc.*

%files docs
%doc %{_docdir}/libkate/html


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 22 2024 Nicolas Chauvet <kwizart@gmail.com> - 0.4.1-32
- Bump

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.4.1-31
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Merlin Mathesius <mmathesi@redhat.com> - 0.4.1-20
- Explicitly disable python when building without python2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 02 2019 Nicolas Chauvet <kwizart@gmail.com> - 0.4.1-17
- Disable python2 for f31+

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 17 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.4.1-15
- Few clean-up

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.4.1-12
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 25 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.4.1-4
- Update valgrind arches

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 12 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.4.1-2
- Update to 0.4.1
- Spec file clean-up
- Set the current valgrind arches
- Use unversioned docdir - rhbz#993818

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.3.8-4
- Rebuild for new libpng

* Tue Mar 08 2011 Dennis Gilmore <dennis@ausil.us> - 0.3.8-3
- no valgrind on sparc or arm arches

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 10 2010 Nicolas Chauvet <kwizart@gmail.com> - 0.3.8-1
- Update to 0.3.8

* Sat Aug 28 2010 Dan Horák <dan[at]danny.cz> - 0.3.7-3
- no valgrind on s390(x)

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Nov 25 2009 Nicolas Chauvet <kwizart@fedoraproject.org> - 0.3.7-1
- Update to 0.3.7

* Fri Oct 16 2009 kwizart < kwizart at gmail.com > - 0.3.6-1
- Update to 0.3.6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul  8 2009 kwizart < kwizart at gmail.com > - 0.3.4-1
- Update to 0.3.4

* Mon Jun 29 2009 kwizart < kwizart at gmail.com > - 0.3.3-2
- Split -docs - Fix #508589

* Mon May 11 2009 kwizart < kwizart at gmail.com > - 0.3.3-1
- Update to 0.3.3

* Fri Apr 10 2009 kwizart < kwizart at gmail.com > - 0.3.1-3
- Use Fedora compliant (using version) _docdir directory.
- Remove shebangs when not needed.
- Bundle examples within -devel
- Use global instead of define

* Sat Apr  4 2009 kwizart < kwizart at gmail.com > - 0.3.1-2
- Prevent conflict with GNU getline() in recent rawhide

* Tue Mar 17 2009 kwizart < kwizart at gmail.com > - 0.3.1-1
- Update to 0.3.1

* Tue Jan 13 2009 kwizart < kwizart at gmail.com > - 0.3.0-1
- Update to 0.3.0
- Add KateDJ and katalyzer in -utils
- Add BR liboggz and -utils Requires liboggz

* Thu Nov 27 2008 kwizart < kwizart at gmail.com > - 0.2.7-1
- Update to 0.2.7

* Mon Oct 20 2008 kwizart < kwizart at gmail.com > - 0.2.5-1
- Update to 0.2.5

* Mon Sep 29 2008 kwizart < kwizart at gmail.com > - 0.2.1-1
- Update to 0.2.1

* Thu Sep 11 2008 kwizart < kwizart at gmail.com > - 0.1.12-1
- Update to 0.1.12

* Thu Sep  4 2008 kwizart < kwizart at gmail.com > - 0.1.11-1
- Update to 0.1.11

* Wed Sep  3 2008 kwizart < kwizart at gmail.com > - 0.1.10-1
- Update to 0.1.10

* Tue Sep  2 2008 kwizart < kwizart at gmail.com > - 0.1.9-1
- Update to 0.1.9

* Fri Aug 29 2008 kwizart < kwizart at gmail.com > - 0.1.8-1
- Update to 0.1.8

* Mon Aug 11 2008 kwizart < kwizart at gmail.com > - 0.1.7-1
- Initial spec file

