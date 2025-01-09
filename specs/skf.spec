%if 0%{?fedora} < 19
%global	rubyabi	1.9.1
%endif

#%%define usescm 1
%undefine	usescm

%global	repoid		78199

%global	mainver	2.10.16
%global	prever	2.10.10
#%%define	betaver	-rc1
%undefine	betaver
%define	betarel	%(echo %betaver | sed -e 's|-|_|' | sed -e 's|^_||')

%global	baserelease	10

%undefine        _changelog_trimtime

Name:		skf
Version:	%{mainver}
Release:	%{?betaver:0.}%{baserelease}%{?betaver:.%betarel}%{?dist}
Summary:	Utility binary files in Simple Kanji Filter

License:	LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-UCD
URL:		http://osdn.jp/projects/skf
Source0:	https://ftp.iij.ad.jp/pub/osdn.jp/skf/%{repoid}/skf_%{mainver}%{?betaver}.tar.xz
Source1:	skf-basic-test.sh
Source2:	create-skf-tarball-from-scm.sh
# https://osdn.net/projects/skf/ticket/39882
Source11:	https://ymu.dl.osdn.jp/ticket/g/s/sk/skf/39882/5733/pythontest
# rubyext: remove unneeded ptr -> VALUE conversion
# ref: https://bugzilla.redhat.com/show_bug.cgi?id=2256789
Patch0:	skf-2.10.16-rubyext-ptr-conversion.patch
# rubyext: type check for argument (ref: bug 2256789)
Patch1:	skf-2.10.16-rubyext-ptr-typecheck.patch

# common BR
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	gettext
# For iconv for Japanese locale
BuildRequires:	glibc-all-langpacks
# BR for extenstions
BuildRequires:	swig
BuildRequires:	ruby-devel
BuildRequires:	rubygems-devel
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl(ExtUtils::Embed)
BuildRequires:	python3-devel
%if 0%{?usescm} >= 1
BuildRequires:	autoconf
%endif
# Patch0 needs autoconf anyway
BuildRequires:	autoconf

Requires:	%{name}-common = %{version}-%{release}
Obsoletes:	python2-skf < %{prever}.99
Obsoletes:	skf-python < %{prever}.99


%package	common
Summary:	Common files for Simple Kanji Filter - i18n kanji converter

%package	ruby
Summary:	Ruby extension module for %{name}
Requires:	%{name}-common = %{version}-%{release}
%if 0%{?fedora} >= 19
Requires:	ruby(release)
%else
Requires:	ruby(abi) = %{rubyabi}
%endif
Provides:	ruby(skf) = %{version}-%{release}

%package	-n python3-skf
Summary:	Python3 extension module for %{name}
Requires:	%{name}-common = %{version}-%{release}

%package	perl
Summary:	Perl extension module for %{name}
Requires:	%{name}-common = %{version}-%{release}

%description
This package contains utility binary files in skf.

%description	common
skf is an i18n-capable kanji filter. skf is designed for
reading documents in various languages and codes using kanji
or unicode capable display devices. Like other kanji filters,
skf provides basic Japanese kanji code conversion features, 
include to/from JIS, EUC, Shift-JIS, UCS2, KEIS83 and UTF-7/8,
but also support various international codesets include Korian
and Chinese standard codesets.

Unlike nkf, skf does not provide additional fancy features
like broken jis recovery, but it has support for ISO-8859's,
European domestic sets, JIS X-0212/X-0213 code conversion, 
IBM gaiji support and can add other code supports easily.

This package contains files commonly used by other skf related
packages.

%description	ruby
This package contains Ruby extension module for skf.

%description	-n python3-skf
This package contains Python3 extension module for skf.

%description	perl
This package contains Perl extension module for skf.

%prep
%setup -q -c -T -a 0
ln -sf %{name}-* main

cp -p %SOURCE1 .

pushd main

%patch -P0 -p1 -b .rubyptr
%patch -P1 -p1 -b .rubycheck

%if 0%{?usescm} >= 1
autoconf

mkdir -p doc || :
touch doc/empty

find . -type d -name CVS | sort -r | xargs rm -rf
%endif

## Fixing build error
# Fix pythonext build error on F-14+
sed -i -e '/python_version=.*substr/s|)-2|)-3|' configure

# Fix for ruby 3
sed -i.ruby3 skf_convert.h \
	-e 's@^#if defined.SKF_RUBY3.*$@#if 0@'
sed -i configure.ac configure \
	-e '\@^[ \t][ \t]*ruby_19_preferred="yes"@i ruby_21_preferred="yes";@' \
	-e '\@^RUBY=.*false@d' \
	%{nil}

## configure option, etc
# change optflags, don't strip
# believe upstream
#sed -i.flags -e 's|-Wno-format-security||' configure

## directory change
# change the directory where tables are to be installed
sed -i.table -e "s|^lskfdir=.*$|lskfdir='%{_libdir}/%{name}'|" configure

## documents
# EUC-JP related
sed -i.eucjp -e '/JOMANDIR/d' Makefile.in
popd # from main

# Okay, duplicate main directory
for ext in \
	python3 \
	ruby perl
do
	mkdir -p $ext
	cp -pr main/* $ext
done

# change optflags
# add -fno-strict-aliasing
%global	optflags_old	%optflags
%global	optflags	%optflags_old -fno-strict-aliasing

%build
# Parallel make all unsafe

OPTS=""
OPTS="$OPTS --enable-debug"
OPTS="$OPTS --disable-strip"

OPTS="$OPTS --with-ruby_sitearch_dir=%{ruby_vendorarchdir}"
PYTHON3OPTS="$OPTS --enable-python3 --with-python_sitearch_dir=%{python3_sitearch}"

# Workaround for ruby 3
export RUBY=ruby

# A. main
pushd main
%configure $OPTS
make -j1
popd

# B. extensions
for ext in \
	ruby perl \
	%{nil}
do
	pushd $ext

    if [ $ext == ruby ] ; then
        export CFLAGS="%optflags $(pkg-config --cflags ruby)"
    fi

	%configure $OPTS
	unset CFLAGS
	make -j1 ${ext}ext

	# Check if tables generated in each extension are
	# the same as in main
	shopt -s nullglob
	pushd table
	for f in *stb
	do
		cmp --quiet $f ../../main/table/$f || exit 1
	done
	popd
	shopt -u nullglob

	popd
done

# python3
pushd python3
export PYTHON=python3
%configure $OPTS $PYTHON3OPTS
unset CFLAGS
# The following is pythonext, not python3ext
make -j1 pythonext
unset PYTHON
popd

# tweak find-debuginfo.sh
%global	debuginfo_subdir	%{name}-%{version}-%{release}.%{?_arch}
%global	__debug_install_post_old	%__debug_install_post
%global	__debug_install_post		\
	\
	%__debug_install_post_old \
	pushd %{buildroot}%{_prefix}/src/debug/%{debuginfo_subdir} \
	for ext in \\\
		python3 \\\
		ruby python perl \
	do \
		test -d $ext || continue \
		cd $ext \
		for file in * \
		do \
			if test -f ../main/$file \
			then \
				status=$(cmp --quiet $file ../main/$file && echo $? || echo $?) \
				if test $status = 0 ; then \
					ln -sf ../main/$file $file \
				fi \
			fi \
		done \
		cd .. \
	done \
	for ext in \\\
		ruby perl \
	do \
		cd $ext \
		for file in *_table_defs.h \
		do \
			status=$(cmp --quiet $file ../python/$file && echo $? || echo $?) \
			if test $status = 0 ; then \
				ln -sf ../python/$file $file \
			fi \
		done \
		cd .. \
	done \
	popd \
	%{nil}

%install
rm -rf %{buildroot}

OPTS=""
OPTS="${OPTS} DESTDIR=%{buildroot}"
OPTS="${OPTS} INSTALL='install -p'"
OPTS="${OPTS} INSTALL_DATA='install -p -m 0644'"

OPTS="$OPTS JMANDIR=%{_mandir}/ja/man1"

# A. main
eval make -C main ${OPTS} install locale_install

# Kill documents, will install with %%doc
rm -rf %{buildroot}%{_defaultdocdir}

# B. extentions
for ext in ruby \
	%{nil}
do
	eval make -C $ext ${OPTS} ${ext}ext_install
done
## python3
( eval make -C python3 ${OPTS} pythonext_install )

## perl
pushd perl
mkdir -p %{buildroot}%{perl_vendorarch}/auto/skf
install -cpm 0644 skf.pm %{buildroot}%{perl_vendorarch}
install -cpm 0755 skf.so %{buildroot}%{perl_vendorarch}/auto/skf/skf.so
popd

## Cleanup

%find_lang %{name}

%check
# Setting environ
export PATH=%{buildroot}%{_bindir}:$PATH

export PERL5LIB=%{buildroot}%{perl_vendorarch}
export python3PATH=%{buildroot}%{python3_sitearch}
export RUBYLIB=%{buildroot}%{ruby_vendorarchdir}

export CHECK_PYTHON2=no

# SOURCE1
sh %{SOURCE1}
(
  export PYTHONPATH=${python3PATH}
  python3 %{SOURCE11}
)

%files
%defattr(-,root,root,-)
%{_bindir}/skf

%{_mandir}/man1/skf.1*
%lang(ja)	%{_mandir}/ja/man1/skf.1*

%files	common	-f %{name}.lang
%defattr(-,root,root,-)
%lang(ja)	%doc	main/debian/changelog
%doc	main/README.txt
%license	main/copyright
%if 0%{?usescm} < 1
%lang(ja)	%doc	main/doc/
%endif

%{_libdir}/%{name}/

%files	ruby
%defattr(-,root,root,-)
%{ruby_vendorarchdir}/skf.so

%files	-n python3-skf
%defattr(-,root,root,-)
%{python3_sitearch}/_skf.so
%{python3_sitearch}/skf.py*
%{python3_sitearch}/__pycache__/skf.*

%files	perl
%defattr(-,root,root,-)
%{perl_vendorarch}/skf.pm
%{perl_vendorarch}/auto/skf/

%changelog
* Wed Jan 08 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.16-10
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.4

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 12 2024 Jitka Plesnikova <jplesnik@redhat.com> - 2.10.16-8
- Perl 5.40 rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.10.16-7
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan  5 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.16-5
- rubyext: type check for argument (ref: bug 2256789)

* Fri Jan  5 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.16-4
- rubyext: remove unneeded ptr -> VALUE conversion (ref: bug 2256789)

* Wed Jan 03 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.16-3
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.3

* Sat Jul 22 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 2.10.16-1.2
- Perl 5.38 rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.10.16-1.1
- Rebuilt for Python 3.12

* Fri Jan 27 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.16-1
- 2.10.16

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.15-2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.15-2.1
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.2

* Mon Jan  2 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.15-2
- Proposal patch for supporting PEP623 in python3.12

* Thu Nov 17 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.15-1
- 2.10.15

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.14-4.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.10.14-4.5
- Rebuilt for Python 3.11

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.10.14-4.4
- Perl 5.36 rebuild

* Thu Jan 27 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.14-4.3
- F-36: rebuild against ruby31

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.14-4.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.14-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 21 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.14-4
- BR: glibc-all-langpacks for iconv for Japanese locale

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.10.14-3.3
- Rebuilt for Python 3.10

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.10.14-3.2
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.14-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan  7 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.14-3
- F-34: build for ruby 3.0
- Some fix to support ruby 3.0

* Mon Dec 21 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.14-2
- Enable python3 binding

* Fri Dec  4 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.14-1
- 2.10.14

* Mon Aug  3 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.12-2
- Remove no longer used macros

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.12-1.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.10.12-1.3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.12-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.12-1.1
- F-32: rebuild against ruby27

* Wed Jan  1 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.12-1
- 2.10.12

* Tue Nov  5 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.11-1
- 2.10.11
- F-32: drop python2 support

* Tue Jul 30 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.10-1
- 2.10.10

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.9-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.10.9-1.1
- Perl 5.30 rebuild

* Tue Apr  9 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.9-1
- 2.10.9

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.8.2-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.8.2-1.1
- F-30: rebuild against ruby26

* Mon Dec 31 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.8.2-1
- 2.10.8.2

* Fri Sep  7 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.7.1-1
- 2.10.7.1 (ruby binding bugfix release)

* Thu Sep  6 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.7-1
- 2.10.7 (not built actually)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.5-1.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.10.5-1.3
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.5-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 03 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.5-1.1
- F-28: rebuild for ruby25

* Sun Dec 31 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.5-1
- 2.10.5

* Wed Nov 22 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.4-1
- 2.10.4

* Fri Oct 13 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.2-1
- 2.10.2

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.10.1-3.5
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.10.1-3.4
- Python 2 binary package renamed to python2-skf
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-3.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.10.1-3.1
- Perl 5.26 rebuild

* Mon Mar 13 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.1-3
- Modify %%__debug_install_post treaking wrt rpm parallel debuginfo change

* Mon Mar 13 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.1-2
- 2.10.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10-1
- 2.10

* Wed Jan 11 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10-0.1.rc1.1
- F-26: rebuild for ruby24

* Thu Jan  5 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10-0.1.rc1
- 2.10-rc1

* Fri Jul 29 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.00.6-1
- 2.00.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.00.4-1.2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.00.4-1.1
- Perl 5.24 rebuild

* Wed Feb 10 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.00.4-1
- 2.00.4

* Tue Feb  2 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.00.3-1
- 2.00.3

* Thu Jan 14 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.00.2-2
- F-24: rebuild against ruby23

* Sun Dec 06 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.00.2-1
- 2.00.2

* Tue Jun 23 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.00.1-1
- 2.00.1

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.00-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.00-1.1
- Perl 5.22 rebuild

* Fri May 29 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.00-1
- 2.00

* Sun May  3 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.00-0.5.b2a_2
- 2.00b2a-2

* Sat May  2 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.00-0.4.b2a_1
- 2.00b2a-1

* Fri Jan 16 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.00-0.3.b1_0
- F-22: Rebuild for ruby 2.2

* Tue Jan 13 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.00-0.2.b1_0
- 2.00b1-0

* Sun Jan  4 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.00-0.1.b0_0
- 2.00b0-0

* Sun Nov 23 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.99.10-1
- 1.99.10

* Wed Sep 10 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.99.9-1
- 1.99.9

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.99.8-1.4
- Perl 5.20 rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.99.8-1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.99.8-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 29 2014 Vít Ondruch <vondruch@redhat.com> - 1.99.8-1.1
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Tue Feb  4 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.99.8-1
- 1.99.8

* Mon Dec 30 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.99.7-1
- 1.99.7

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 1.99.6-1.1
- Perl 5.18 rebuild

* Sat Jul 27 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.99.6-1
- 1.99.6

* Fri Jul 26 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.99.5-1
- 1.99.5

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.99.4-1.1
- Perl 5.18 rebuild

* Tue Apr 23 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.99.4-1
- 1.99.4

* Fri Apr 12 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.99.3-1
- 1.99.3

* Wed Mar 27 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.99.2-0.1.cvs20130327T1317
- Try CVS source for ruby 2.0 support

* Sun Mar 17 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.99.1-2
- F-19: rebuild for ruby 2.0.0

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.99.1-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 15 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.99.1-1
- 1.99.1

* Mon Jan 14 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.99.0-3
- Check if tables generated in each extension are the same as in main
- Detect and strip same files in debuginfo rpm more

* Thu Jan 10 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.99.0-2
- Workaround for gcc48 build failure (dyn_table_gen segfault)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.99.0-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 1.99.0-1.1
- Perl 5.16 rebuild

* Mon Apr  2 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.99.0-1
- 1.99.0

* Thu Jan  5 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.99-0.2.alg
- F-17: rebuild against gcc47

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.99-0.1.a1g.1
- Perl mass rebuild

* Thu Mar 24 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.99-0.1.a1g
- Try 1.99 a1g

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.97.4-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  9 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.97.4-1
- 1.97.4

* Thu Nov  4 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.97.3-1
- 1.97.3

* Thu Aug 12 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.97.2-1
- 1.97.2
- The method to build python3 binding is now written in the spec file,
  however for now not activate it

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.97.1-2.2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jun 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.97.1-2.1
- Mass rebuild with perl-5.12.0

* Thu Apr  1 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.97.1-2
- 1.97.1

* Thu Mar 25 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.97.0-0.2.a
- Remove useless sed line
- Move man pages to "main" package

* Sat Mar 20 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.97.0-0.1.a
- 1.97.0a
- Initial packaging
