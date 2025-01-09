%global		rubyabi		1.9.1
%define		qdbm_ver	1.8.75

# Workaround for ruby side bug (bug 226381 c11)
%{!?ruby_arch:	%define ruby_arch	%(ruby -rrbconfig -e "puts RbConfig::CONFIG['archdir']")}

%define set_javaver() \
%if 	0%{?fedora}%{?rhel} == %1 \
BuildRequires:	java-%2-openjdk-devel \
%if	%1 >= 42 \
BuildRequires:	javapackages-local-openjdk%2 \
%endif \
%endif \
%{nil}

Name:		hyperestraier
Version:	1.4.13
Release:	66%{?dist}
Summary:	A full-text search system

# Overall	LGPL-2.1-or-later
# javapure/*.java	BSD-3-Clause
# md5.c	Zlib
# rubypure/estcall.rb	BSD-3-Clause
# SPDX confimed
License:	LGPL-2.1-or-later AND BSD-3-Clause
URL:		http://hyperestraier.sourceforge.net/
Source0:	http://hyperestraier.sourceforge.net/%{name}-%{version}.tar.gz
# Taken from Debian:
# http://packages.debian.org/testing/ruby/libestraier-ruby1.9.1
Patch0:		huperestraier-1.4.13-ruby-19-compat.patch
# Make javanative/configure c99 compat manually
# instead of rerunning autoupdate -> autoconf
Patch1:		hyperestraier-1.4.13-javanative-configure-c99-compat.patch
# rubynative: fix function prototype passed to rb_rescue
Patch2:		hyperestraier-1.4.13-rubyext-functype.patch

BuildRequires:	gcc
BuildRequires:	bzip2-devel zlib-devel
BuildRequires:	lzo-devel >= 2.02
BuildRequires:	qdbm-devel >= %{qdbm_ver}
BuildRequires:	rubygem(rdoc)
BuildRequires:	ruby-devel
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl(ExtUtils::MakeMaker)
# java related macros
%ifarch %java_arches
%set_javaver	43	21
%set_javaver	42	21
%set_javaver	41	21
%set_javaver	40	21
%set_javaver	39	17
BuildRequires:	javapackages-tools
%endif
BuildRequires:	make

%description
Hyper Estraier is a full-text search system. You can search 
lots of documents for some documents including specified words. 
If you run a web site, it is useful as your own search engine 
for pages in your site. Also, it is useful as search utilities 
of mail boxes and file servers.

%package devel
Summary:	Libraries and Header files for Hyper Estraier
Requires:	%{name} = %{version}-%{release}
Requires:	qdbm-devel >= %{qdbm_ver}
Requires:	pkgconfig

%description devel
This is the development package that provides header files and libraries
for Hyper Estraier.

%package java
Summary:	Hyper Estraier library for Java
Requires:	%{name} = %{version}-%{release}

%description java
This package contains a Java interface for Hyper Estraier

%package perl
Summary:	Hyper Estraier library for Perl
Requires:	%{name} = %{version}-%{release}

%description perl
This package contains a Perl interface for Hyper Estraier

%package -n ruby-hyperestraier
Summary:	Hyper Estraier Library for Ruby
Requires:	%{name} = %{version}-%{release}
Requires:	ruby(release)
Provides:	ruby(hyperestraier) = %{version}-%{release}

%description -n ruby-hyperestraier
This package contains a Ruby interface for Hyper Estraier.


%prep
%setup -q

%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
## 0. First:
## - remove rpath
## - fix pkgconfig file to hide header files
## - fix Makefile to keep timestamps
%{__sed} -i.rpath -e '/^LDENV/d' `find . -name Makefile.in`
%{__sed} -i.misc \
	 -e '/^Libs/s|@[A-Z][A-Z]*@||g' \
	 -e '/Cflags/s|^\(.*\)|\1 -I\${includedir}/%{name}|' \
	 %{name}.pc.in

%{__sed} -i.path \
	-e '/^cflags/s|^\(.*\)\"$|\1 -I%{_datadir}/qdbm -I%{_datadir}/%{name}\"|' \
	estconfig.in

%{__sed} -i.stamp \
	 -e 's|cp \(-R*f \)|cp -p \1| ' \
	 -e 's|^CP =.*$|CP = cp -p|' \
	`find . -name Makefile.in -or -name \*[mM]akefile`

## 1. For main
%{__sed} -i.flags \
	-e '/^CFLAGS/s|^\(.*\)$|\1 %{optflags}|' Makefile.in
%configure \
	--enable-devel \
	--enable-zlib \
	--enable-bzip \
	--enable-lzo

%{__make} %{?_smp_mflags}

## 2. For java
%ifarch %java_arches
pushd javanative/
%{__sed} -i.flags -e '/^MYCFLAGS/s|-O2.*|%{optflags}\"|' configure
export JAVA_HOME=%{java_home}
%configure
# Failed with -j8 on Matt's mass build
%{__make} -j1 JAR=%{jar} JAVAC=%{javac}
popd
%endif

## 3. For perl:
pushd perlnative
%configure
%{__make} %{?_smp_mflags} \
	CC="gcc %optflags $(pkg-config --cflags qdbm)" \
	OPTIMIZE="" \
	LDDLFLAGS="-shared"
popd

##4. For ruby
pushd rubynative

# Workaround for ruby side bug (bug 226381 c11)
%{__cp} -p %{ruby_arch}/rbconfig.rb .
%{__sed} -i.static -e 's|-static||g' rbconfig.rb
export RUBYLIB=$(pwd)

%{__sed} -i.path -e 's|-O3.*|\`pkg-config --cflags qdbm\`\"|' src/extconf.rb

# Fix placement for Ruby 1.9.
%{__sed} -i.vendor \
	-e 's|myrblibdir=.*|myrblibdir=%{ruby_vendorarchdir}|' configure

%configure
%{__make} %{?_smp_mflags}
popd

%install
%{__rm} -rf $RPM_BUILD_ROOT

## 1. For main
%{__make} install DESTDIR=$RPM_BUILD_ROOT

# clean up
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/lib*.a
%{__rm} -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/doc/
%{__rm} -f $RPM_BUILD_ROOT%{_datadir}/%{name}/[A-Z]*

# hide header files to name specific directory
pushd $RPM_BUILD_ROOT%{_includedir}
mkdir %{name}
for f in *.h ; do
	for g in *.h ; do
		eval sed -i -e \'s\|include \<$g\>\|include \"$g\"\|\' $f
	done
done
%{__mv} *.h %{name}/
popd

%ifarch %java_arches
## 2. For java
pushd javanative/
%{__make} DESTDIR=$RPM_BUILD_ROOT install JAR=%{jar}
popd
%{__mkdir_p} $RPM_BUILD_ROOT%{_jnidir}
%{__mv} -f $RPM_BUILD_ROOT%{_libdir}/*.jar \
	$RPM_BUILD_ROOT%{_jnidir}
%endif

## 3. For perl
pushd perlnative
%{__make} install DESTDIR=$RPM_BUILD_ROOT INSTALLDIRS=vendor
popd
# clean up
%{__rm} $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod
find $RPM_BUILD_ROOT%{perl_vendorarch} \
	-name \*.bs -or -name .packlist | \
	xargs rm -f
find $RPM_BUILD_ROOT%{perl_vendorarch} \
	-name \*.so | \
	xargs chmod 0755

## 4. For ruby
pushd rubynative/
%{__make} DESTDIR=$RPM_BUILD_ROOT install \
	ruby_headers=


popd

%ldconfig_scriptlets

%files
%defattr(-,root,root,-)
%license COPYING
%doc ChangeLog
%doc THANKS
%doc example/
%doc doc/*guide-en.html doc/*.png doc/*.css
%lang(ja) %doc doc/*guide-ja.html

%{_libdir}/libestraier.so.*
%{_bindir}/est*
%exclude %{_bindir}/estconfig
%exclude %{_bindir}/*.pl
%exclude %{_bindir}/*.rb
%{_libexecdir}/*.cgi
%{_datadir}/%{name}/

%{_mandir}/man1/*.1*

%files devel
%defattr(-,root,root,-)

%{_bindir}/estconfig
%{_includedir}/%{name}/
%{_libdir}/libestraier.so
%{_libdir}/pkgconfig/*.pc

%{_mandir}/man3/est*.3*

%ifarch %java_arches
%files java
%defattr(-,root,root,-)
%doc doc/javanativeapi/*
%doc javanative/overview.html
%doc javanative/example/

%{_jnidir}/*.jar
%{_libdir}/libj*.so*
%endif

%files perl
%defattr(-,root,root,-)
%doc doc/perlnativeapi/index.html
%doc perlnative/example/

%{_bindir}/*.pl
%{perl_vendorarch}/*.p*
%{perl_vendorarch}/auto/*/
%{_mandir}/man3/*.3pm*

%files -n ruby-hyperestraier
%defattr(-,root,root,-)
%doc doc/rubynativeapi/*
%doc rubynative/example/

%{_bindir}/*.rb
%{ruby_vendorarchdir}/*.so


%changelog
* Wed Jan 08 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.13-66
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.4

* Fri Oct 25 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.13-65
- Reable mvn dependency generation again

* Sun Sep 29 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.13-64
- Use explicit java version for BR
- Add more BR stuff for F42
- Kill mvn dependency generator which is difficult to understand

* Sat Aug 31 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.13-63
- Explicitly specify openjdk version on F-39

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.13-62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Jitka Plesnikova <jplesnik@redhat.com> - 1.4.13-61
- Perl 5.40 rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.13-60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.13-59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.13-58
- rubynative: fix function prototype passed to rb_rescue

* Wed Jan 03 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.13-57
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.3

* Sat Dec 30 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.13-56
- SPDX migration

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.13-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.4.13-54
- Perl 5.38 rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.13-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.13-52
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.2

* Sat Nov 26 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.13-51
- Patch for javanative module for c99 conformant: -Werror=implicit-int

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.13-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jul  9 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.13-49
- Adopt %%java_arches https://fedoraproject.org/wiki/Changes/Drop_i686_JDKs

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.4.13-48
- Perl 5.36 rebuild

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.4.13-47
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 27 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.13-46
- F-36: rebuild against ruby31

* Sun Jul 25 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.13-45
- Rebuild for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.4.13-44
- Perl 5.34 rebuild

* Sat Jan 30 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.13-43
- F-34: mass rebuild

* Thu Jan 07 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.13-42
- F-34: rebuild against ruby 3.0

* Fri Aug 07 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.13-41
- F-33: mass rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.4.13-40
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.4.13-39
- Perl 5.32 rebuild

* Sun Feb 02 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.13-38
- F-32: mass rebuild

* Sat Jan 18 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.13-37
- F-32: rebuild against ruby27

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.4.13-36
- Perl 5.30 rebuild

* Tue Feb 05 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.13-35
- rebuild for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.13-34
- F-30: rebuild against ruby26

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.4.13-33
- Perl 5.28 rebuild

* Mon May 28 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.13-32
- F-29: BR javapackages-tools for java rpm macros

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1.4.13-31
- Rebuilt for switch to libxcrypt

* Wed Jan 03 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.13-30
- F-28: rebuild for ruby25

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.4.13-29
- Perl 5.26 rebuild

* Wed Feb 15 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.13-28
- F-26: mass rebuild

* Wed Jan 11 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.13-27
- F-26: rebuild for ruby24

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.4.13-26
- Perl 5.24 rebuild

* Fri Feb  5 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.13-25
- F-24 massbuild

* Wed Jan 13 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.13-24
- F-24: rebuild against ruby23

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.4.13-23
- Perl 5.22 rebuild

* Fri Jan 16 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.13-22
- F-22: rebuild for https://fedoraproject.org/wiki/Changes/Ruby_2.2

* Wed Sep 10 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.13-21
- Enable java build again, using openjdk

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.4.13-20
- Perl 5.20 rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.13-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 12 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.13-18
- F-21: disable java due to gcc-java vanishment

* Thu Apr 24 2014 Vít Ondruch <vondruch@redhat.com> - 1.4.13-17
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Wed Aug  7 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.13-16
- F-20: mass rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 1.4.13-15
- Perl 5.18 rebuild

* Sun Mar 17 2013 Mamour TASAKA <mtasaka@fedoraproject.org> - 1.4.13-4
- F-19: rebuild for ruby 2.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.13-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Aug  6 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.4.13-12
- F-18: Mass rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.4.13-11
- Perl 5.16 rebuild

* Thu Mar 01 2012 Vít Ondruch <vondruch@redhat.com> - 1.4.13-10
- Rebuilt for Ruby 1.9.3.

* Thu Jan  5 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.4.13-9
- F-17: rebuild against gcc47

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.4.13-8
- Perl mass rebuild

* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.4.13-7
- Mass rebuild with perl-5.12.0

* Wed Dec 23 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.13-6
- F-13: rebuild for new perl

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.13-5
- F-12: Mass rebuild

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.13-4
- F-11: Mass rebuild

* Fri Aug 29 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.13-3
- Use -j1 under javanative (-j8 failed)

* Sat Mar 15 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.13-2
- Rebuild against new perl (F-9)

* Sat Feb  9 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Rebuild against gcc43 (F-9)

* Sun Dec 30 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.13-1
- 1.4.13

* Thu Nov 29 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.12-1
- 1.4.12

* Sat Nov 17 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.11-1
- 1.4.11

* Wed Aug 22 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.10-2.dist.2
- Mass rebuild (buildID or binutils issue)

* Fri Aug  3 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.10-2.dist.1
- License update

* Thu Jun 16 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.10-2
- Fix java directory

* Thu Mar 22 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.10-1
- 1.4.10
- Ruby subpackage description change according to Guildlines

* Thu Mar  8 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.9-3
- Add perl-devel for BR

* Fri Feb 23 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.9-2.dist.1
- Drop lzo support on FC-5

* Fri Feb 23 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.9-2
- Remove duplicate files and fix the dependency for main package.

* Thu Feb 22 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.9-1
- Initial packaging for Fedora.
