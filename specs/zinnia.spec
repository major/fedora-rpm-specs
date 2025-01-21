Name:		zinnia
Version:	0.06
Release:	72%{?dist}
Summary:	Online handwriting recognition system with machine learning

License:	BSD-3-Clause
URL:		http://zinnia.sourceforge.net/
Source0:	http://downloads.sourceforge.net/zinnia/%{name}-%{version}.tar.gz
Source1:	http://zinnia.svn.sourceforge.net/viewvc/zinnia/zinnia/tomoe2s.pl
Source2:	Makefile.tomoe
Patch0:		zinnia-0.05-bindings.patch
Patch1:		zinnia-0.06-fixes-ppc-float.patch
Patch2:		always-store-data-in-little-endian-format.patch
Patch3:		zinnia-fixes-gcc6-compile.patch
Patch4:		zinnia-fixes-python-setuptools.patch
BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	libdb-devel, python3-devel
BuildRequires:	swig
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	tomoe
BuildRequires:	autoconf
BuildRequires:	gnome-common
BuildRequires:	python3-setuptools

%description
Zinnia provides a simple, customizable, and portable dynamic OCR
system for hand-written input, based on Support Vector Machines.

Zinnia simply receives user pen strokes as coordinate data and outputs
the best matching characters sorted by SVM confidence. To maintain
portability, it has no rendering functionality. In addition to
recognition, Zinnia provides a training module capable of creating
highly efficient handwriting recognition models.

This package contains the shared libraries.

%package        devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package 	utils
Summary:	Utils for the zinnia library
Requires:	%{name} = %{version}-%{release}

%description	utils
The %{name}-utils package provides utilities for zinnia library that 
use %{name}.

%package 	doc
Summary:	Documents for the zinnia library
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	doc
The %{name}-doc package provide documents for zinnia library that 
use %{name}.

%package  	perl
Summary:	Perl bindings for %name
Requires:	%{name} = %{version}-%{release}


%description 	perl
This package contains perl bindings for %{name}.

%package 	-n python3-zinnia
%{?python_provide:%python_provide python3-zinnia}
Summary:	Python bindings for %{name}
Requires:	%{name} = %{version}-%{release}

%description 	-n python3-zinnia
This package contains python bindings for %{name}.

%package	tomoe-ja
Summary:        Japanese tomoe model file for %{name}
Requires:       %{name} = %{version}-%{release}
Provides:       zinnia-tomoe = %{version}-%{release}
Obsoletes:      zinnia-tomoe < 0.06-19

%description	tomoe-ja
This package contains Japanese tomoe model files for %{name}.

%package	tomoe-zh_CN
Summary:        Simplified Chinese tomoe model file for %{name}
Requires:       %{name} = %{version}-%{release}
Provides:       zinnia-tomoe = %{version}-%{release}
Obsoletes:      zinnia-tomoe < 0.06-19

%description	tomoe-zh_CN
This package contains Simplified Chinese tomoe model files for %{name}.

%prep
%setup -q -n %{name}-%{version}
%patch -P0 -p1 -b .bindings
%patch -P1 -p1 -b .ppc
%patch -P2 -p1 -R -b .little-endian
%patch -P3 -p1 -b .gcc6
%patch -P4 -p1 -b .python

find . -type f -name "*.pyc" -exec rm -f {} ';'
cp %{SOURCE1} .
cp %{SOURCE2} .
pushd doc
iconv -f latin1 -t utf8 zinnia.css > zinnia.css.bak 
mv -f zinnia.css.bak zinnia.css
popd

# re-generate zinnia.py and zinnia_wrap.cxx for python 3.x
pushd swig
make python
popd

%build
gnome-autogen.sh
%configure --disable-static --disable-rpath
make CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" %{?_smp_mflags}
make -f Makefile.tomoe build

pushd perl
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}
popd

pushd python
python3 setup.py build
popd

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
make -f Makefile.tomoe install DESTDIR=$RPM_BUILD_ROOT

pushd perl
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
popd

pushd python
python3 setup.py install --root $RPM_BUILD_ROOT

#the following line fixes RHBZ#2048104
rm -rf $RPM_BUILD_ROOT%{python3_sitearch}/zinnia_python-0.0.0-py%{python3_version}.egg-info
pushd

#remove something unnecessary
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.bs" -size 0c -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'

#change the privilege of some files
chmod 0755 $RPM_BUILD_ROOT%{perl_vendorarch}/auto/%{name}/%{name}.so



%ldconfig_scriptlets


%files
%doc README COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/lib%{name}.so

%{_libdir}/pkgconfig/%{name}.pc

%files utils
%{_bindir}/zinnia
%{_bindir}/zinnia_convert
%{_bindir}/zinnia_learn

%files doc
%doc doc/*

%files	perl
%{perl_vendorarch}/auto/%{name}/
%{perl_vendorarch}/%{name}.pm

%files	-n python3-zinnia
%{python3_sitearch}/_%{name}.*.so
%{python3_sitearch}/%{name}*
%{python3_sitearch}/__pycache__/*

%files tomoe-ja
%dir %{_datadir}/zinnia/model/tomoe/
%{_datadir}/zinnia/model/tomoe/handwriting-ja.model

%files tomoe-zh_CN
%dir %{_datadir}/zinnia/model/tomoe/
%{_datadir}/zinnia/model/tomoe/handwriting-zh_CN.model

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-72
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Oct 30 2024 Peng Wu <pwu@redhat.com> - 0.06-71
- Fix build
- Resolves: RHBZ#2319752

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-70
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 12 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-69
- Perl 5.40 rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.06-68
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-66
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-65
- Perl 5.38 rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.06-64
- Rebuilt for Python 3.12

* Sat May  6 2023 Peng Wu <pwu@redhat.com> - 0.06-63
- Migrate to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 24 2022 Peng Wu <pwu@redhat.com> - 0.06-61
- Add BuildRequires python3-setuptools

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.06-59
- Rebuilt for Python 3.11

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-58
- Perl 5.36 rebuild

* Fri Feb 11 2022 Peng Wu <pwu@redhat.com> - 0.06-57
- Fix RHBZ#2048104

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.06-54
- Rebuilt for Python 3.10

* Fri Jun  4 2021 Peng Wu <pwu@redhat.com> - 0.06-53
- Disable rpath

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-52
- Perl 5.34 rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-49
- Perl 5.32 rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.06-48
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.06-46
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.06-45
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-43
- Perl 5.30 rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 10 2018 Peng Wu <pwu@redhat.com> - 0.06-41
- Switch from python2 to python3

* Tue Jul 24 2018 Peng Wu <pwu@redhat.com> - 0.06-40
- Use python2

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-38
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.06-36
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.06-35
- Python 2 binary package renamed to python2-zinnia
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-32
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-30
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-29
- Perl 5.24 rebuild

* Wed Feb 17 2016 Peng Wu <pwu@redhat.com> - 0.06-28
- Fixes compile with gcc 6.0

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-25
- Perl 5.22 rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.06-24
- Rebuilt for GCC 5 C++11 ABI change

* Thu Dec 11 2014 Peng Wu <pwu@redhat.com> - 0.06-23
- Fixes split issues

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-22
- Perl 5.20 rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 29 2014 Peng Wu <pwu@redhat.com> - 0.06-20
- Split zinnia-tomoe sub-package for ibus-handwrite

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.06-17
- Perl 5.18 rebuild

* Tue Mar 26 2013 Peng Wu <pwu@redhat.com> - 0.06-16
- Fixes aarch64 build

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.06-13
- Perl 5.16 rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-12
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.06-10
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 26 2010  Peng Wu <pwu@redhat.com> - 0.06-8
- Remove noarch from zinnia-tomoe sub-package for Fedora 12 ppc build.

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.06-7
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Jul 16 2010  Peng Wu <pwu@redhat.com> - 0.06-6
- revert patch always-store-data-in-little-endian-format.patch for ppc build.

* Tue Jun 08 2010 Liang Suilong <liangsuilong@gmail.com> - 0.06-5
- Force to use default compiling macro 

* Fri Jun 04 2010  Peng Wu <pwu@redhat.com> - 0.06-4
- Add a patch(zinnia-0.06-fixes-ppc-float.patch),
  to fixes ppc/ppc64 zinnia tomoe model generating error.

* Wed Jun 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.06-3
- Mass rebuild with perl-5.12.0

* Thu May 20 2010  Peng Wu <pwu@redhat.com> - 0.06-2
- Auto generate zinnia tomoe model files,
  and includes all model files in zinnia-tomoe noarch sub-package.

* Thu May 20 2010  Peng Wu <pwu@redhat.com> - 0.06-1
- Update to version 0.06.

* Wed Mar 10 2010 Liang Suilong <liangsuilong@gmail.com> - 0.05-4
- Fix the bugs of SPEC file

* Fri Mar 04 2010 Liang Suilong <liangsuilong@gmail.com> - 0.05-3
- Fix something wrong of spec file

* Wed Mar 02 2010 Liang Suilong <liangsuilong@gmail.com> - 0.05-2
- Rename Subpackage for perl and python

* Tue Feb 02 2010 Liang Suilong <liangsuilong@gmail.com> - 0.05-1
- Initial Package
