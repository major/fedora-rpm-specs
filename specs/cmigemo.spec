%define		mainver	1.3
%define		tarballver	20110227
%define		minorver	date%{tarballver}
%define		prerelease	1

%define		baserelease	19


%define		uprel		%(echo %{?minorver} | %{__sed} -e 's|^--*||' | %{__sed} -e 's|-|_|g' )
%define		rel		%{?prerelease:0.}%{baserelease}%{?minorver:.%uprel}

%define		skkdicdir	%{_datadir}/skk
%define		skkcoding	EUC-JP


Name:		cmigemo
Version:	%{mainver}
Release:	%{rel}%{?dist}
Summary:	C interface of Ruby/Migemo Japanese incremental search tool

# doc/LICENSE_MIT.txt	MIT
# SKK-JISYO.L (from skkdic)	GPL-2.0-or-later
# SPDX confirmed
License:	MIT AND GPL-2.0-or-later
URL:		http://www.kaoriya.net/software/cmigemo
#Source0:	http://www.kaoriya.net/dist/var/%{name}-%{mainver}%{?minorver}.tar.bz2
Source0:	http://cmigemo.googlecode.com/files/cmigemo-default-src-%{tarballver}.zip
Patch0:		cmigemo-20110227-ignore-random-string.patch
Patch1:		cmigemo-1.3c-MIT-dont-escape.patch
Patch2:		cmigemo-20110227-compile.patch
Patch3:		cmigemo-20110227-keep-regex-with-brackets.patch

BuildRequires:  gcc
BuildRequires:  skkdic
BuildRequires:  /usr/bin/perl
BuildRequires:  make

%description
C/Migemo is a C interface of Ruby/Migemo, a Japanese incremental search tool
by Romaji.

%package	devel
Summary:	Development files for cmigemo

Requires:	%{name}%{?isa} = %{version}-%{release}

%description	devel
This package  contains libraries and header files for
developing applications that use cmigemo.

%prep
%setup -q -c -T %{name}-%{version} -a 0
cd cmigemo-default-src/
%patch -P0 -p1 -b .random
%patch -P1 -p1 -b .escape
%patch -P2 -p1 -b .build
%patch -P3 -p1 -b .regex

# Change default command for configure
%{__sed} -i.command \
	-e 's|curl|true|' \
	-e 's|nkf|true|' \
	-e 's|install\"|install -p"|' \
	configure

# use iconv instead of nkf
%{__sed} -i.nkf \
	-e 's|^\(FILTER_CP932[ \t][ \t]*=\).*|\1 iconv -f %{skkcoding} -t SJIS|' \
	-e 's|^\(FILTER_EUCJP[ \t][ \t]*=\).*|\1 iconv -f SJIS -t EUC-JP|' \
	compile/config.mk.in

# make cmigemo original data dir
%{__sed} -i.dir \
	-e 's|/share/migemo|/share/cmigemo|' \
	compile/config.mk.in config.mk

# ( don't create unnecessary backup file for document...)
%{__sed} -i \
	-e 's|/usr/local/share/migemo|%{_datadir}/cmigemo|' \
	doc/README_j.txt tools/migemo.vim

# remove unneeded rpath
%{__sed} -i.rpath \
	-e 's|^\(LDFLAGS_MIGEMO[ \t][ \t]*=\).*|\1 |' \
	compile/Make_gcc.mak

# 64 bits libdir
%{__sed} -i.bits \
	-e 's|\$(prefix)/lib|$(prefix)/%{_lib}|' \
	config.mk compile/config.mk.in compile/config_default.mk

# Also install zen2han
%{__sed} -i.han \
	-e 's|^\(.*\)\(han2zen\)\(.*\)$|\1\2\3\n\1zen2han\3|' \
	compile/unix.mak

%{__chmod} 0644 tools/*

%build
cd cmigemo-default-src/
%{__chmod} u+x configure
%configure

# parallel make unsafe
%{__make} gcc CC="gcc $RPM_OPT_FLAGS"

# This is under GPL-2.0-or-later
%{__cat} %{skkdicdir}/SKK-JISYO.L | gzip > dict/SKK-JISYO.L.gz
%{__make} gcc-dict
( cd dict ; %{__make} utf-8 )

%install
pushd cmigemo-default-src/

%{__make} gcc-install prefix=$RPM_BUILD_ROOT%{_prefix}

# remove unneeded document
%{__rm} -rf $RPM_BUILD_ROOT%{_prefix}/doc/

popd

# make documentation directory
%{__rm} -rf doc_install
%{__rm} -rf licenses
%{__rm} -rf tools

pushd cmigemo-default-src/
cp -a tools ..

%{__rm} -rf doc_install
%{__mkdir} doc_install
%{__mkdir} licenses
cd doc
for f in *txt ; do \
	iconv -f SJIS -t UTF-8 $f > ../doc_install/$f && \
		touch -r $f ../doc_install/$f || \
		%{__cp} -p $f ../doc_install/$f
done
cp -p LICENSE_MIT.txt ../licenses/
cd ..

mv doc_install ..
mv licenses ..
popd

%ldconfig_scriptlets

%files
%defattr(-,root,root,-)
%license licenses/*
%doc doc_install/*
%doc tools/

%{_bindir}/%{name}
%{_libdir}/libmigemo.so.1{,.*}

%{_datadir}/cmigemo/

%files	devel
%defattr(-,root,root,-)
%{_includedir}/migemo.h
%{_libdir}/libmigemo.so

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.19.date20110227
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.18.date20110227
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.17.date20110227
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.16.date20110227
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan  7 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3-0.15.date20110227
- SPDX migration

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.14.date20110227.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.13.date20110227.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.13.date20110227.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.13.date20110227.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.13.date20110227.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.13.date20110227.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.13.date20110227.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.13.date20110227.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.13.date20110227.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.13.date20110227.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3-0.13.date20110227
- Add gcc as BR

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.12.date20110227.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.12.date20110227.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.12.date20110227.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.12.date20110227.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 15 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3-0.12.date20110227
- Add perl as BR

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.11.date20110227.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.11.date20110227.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-0.11.date20110227.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-0.11.date20110227.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-0.11.date20110227.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Nov 14 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3-0.11.date20110227
- Rebuild for updated skkdic

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-0.10.date20110227.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-0.10.date20110227.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan  4 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3-0.10.date20110227
- Rebuild for updated skkdic

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-0.9.date20110227.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jan  8 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.3-0.9.date20110227
- F-17: rebuild against gcc47

* Sun Oct 16 2011 Mamoru Tasaka <mtasaka@fedoraproject.org>
- Rebuild for updated skkdic (for F-16)

* Wed Mar  9 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.3-0.8.date20110227
- Moved to googlecode, 20110227 is released

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-0.7.c_MIT.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Sep 29 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- F-12: Rebuild for updated skkdic (for F12Beta)

* Wed Aug  5 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- F-12: Rebuild for updated skkdic (for F12Alpha)

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- F-12: Mass rebuild

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- F-11: Mass rebuild

* Tue Jan 20 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3-0.7.c_MIT
- Also install zen2han (JD 6 comment 976)

* Sat Feb  9 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Rebuild against gcc43

* Wed Aug 22 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3-0.6.c_MIT.dist.1
- Mass rebuild (buildID or binutils issue)

* Wed Jul 11 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3-0.6.c_MIT
- Re-enable Migemo autocompletion

* Sun May 26 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3-0.5.c_MIT
- Don't make special character escaped.

* Sat May 26 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3-0.4.c_MIT
- Suppress completent for too random string.

* Sun May 20 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3-0.3.c_MIT
- Don't create unnecessary document backup

* Sun May 20 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3-0.2.c_MIT
- 64 bits fix

* Sat May 19 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3-0.1.c_MIT
- Initial packaging.
