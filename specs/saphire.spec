%global	repoid		54458
%undefine	_docdir_fmt


Name:		saphire
Version:	3.6.5
Release:	35%{?dist}
Summary:	Yet another shell

# SPDX confirmed
License:	MIT
URL:		http://ab25cq.wiki.fc2.com/
Source0:	http://dl.sourceforge.jp/sash/%{repoid}/saphire-%{version}.tgz
Patch0:	saphire-3.6.5-gcc10-fno-common.patch
Patch1:	saphire-3.6.5-c99-port.patch
Patch2:	saphire-string_chomp-public.patch
Patch3:	saphire-3.6.5-c23.patch

BuildRequires:	make
BuildRequires:  gcc
BuildRequires:	cmigemo-devel
BuildRequires:	gc-devel
BuildRequires:	ncurses-devel
BuildRequires:	oniguruma-devel
#BuildRequires:	pcre-devel
BuildRequires:	readline-devel

%description
Yet another shell

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
# Patches
%patch -P0 -p1 -b .gcc10
%patch -P1 -p1 -b .c99
%patch -P2 -p1 -b .string_chomp
%patch -P3 -p1 -b .c23

# Don't strip binary
sed -i.strip -e 's|\$(INSTALL) -s|\$(INSTALL) |' Makefile.in
# cp -> ln for library
sed -i.ln -e '/libsaphire.so/s|cp |ln -s -f |' Makefile.in
# Add current directory to library search path
sed -i.libpath -e '/^LIBS[2]*=/s|^\(.*\)$|\1 -L.|' Makefile.in
# Don't do lib-install for all
sed -i.all -e '/^all:/s|lib-install||' Makefile.in
# Keep timestamp
sed -i.stamp \
	-e 's| -m 755| -p -m 0755|g' \
	-e 's| -m 644| -p -m 0644|g' \
	Makefile.in
# Umm...
sed -i.soname \
	-e '/[ \t]/s|\( -o libsaphire.so.2.0.0 \)| -Wl,-soname,libsaphire.so.2 \1|' \
	Makefile.in

# FIX CRLF
for file in \
	CHANGELOG.txt \
	README*.txt \
	USAGE.*.txt
do
	sed -i.dos -e 's|\r||' $file
	touch -r $file{.dos,}
	rm $file.dos
done

# Some encodings or so fixes
pushd headers/saphire
for f in *.h
do
	touch -r $f $f.stamp
	iconv -f EUC-JP -t UTF-8 $f > $f.utf8 && mv -f $f.utf8 $f || rm -f $f.utf8
	iconv -f SHIFT-JIS -t UTF-8 $f > $f.utf8 && mv -f $f.utf8 $f || rm -f $f.utf8
	sed -i -e 's|\r||' $f
	touch -r $f.stamp $f
	rm -f $f.stamp
done
popd

# Prefer less over lv
sed -i.pager \
	-e 's| lv| less|' \
	-e 's|lv |less |' \
	saphire.sa

%build
# Move maybe-arch-dependent file out of %%sysconfdir
# --docdir is needed
%configure \
	--with-migemo \
	--with-system-migemodir=%{_datadir}/cmigemo \
	--sysconfdir=%{_libdir}/ \
	--docdir=%{_defaultdocdir}/%{name}-%{version}

# configure overrides $CFLAGS
# Kill parallel make
# Umm... override docdir also here
make -j1 \
	CC="gcc %{optflags}" \
	docdir=%{_defaultdocdir}/%{name}-%{version} \
	-k

# Samples
rm -rf install_samples/
mkdir -p install_samples/samples
cp -p samples/*sa install_samples/samples

pushd install_samples/samples
chmod 0644 *.sa
sed -i \
	-e '\@^#!/usr.*@d' \
	-e '\@^#!/home.*@d' \
	*.sa
popd

%install
make install \
	DESTDIR=%{buildroot} \
	includedir=%{_includedir}/%{name} \
	docdir=%{_defaultdocdir}/%{name}-%{version}
	

%ldconfig_scriptlets

%files
%doc	AUTHORS
%license	LICENSE
%doc	README.en.txt
%doc	USAGE.en.txt
%doc	install_samples/samples
%lang(ja)	%doc	CHANGELOG.txt
%lang(ja)	%doc	README.ja.txt
#%%lang(ja)	%doc	TODO.ja.txt
%lang(ja)	%doc	USAGE.ja.txt

%{_bindir}/%{name}
%{_bindir}/saphiresh
%{_libdir}/lib%{name}.so.2*
%dir %{_libdir}/%{name}/
%{_libdir}/%{name}/%{name}.sa*
%{_libdir}/%{name}/completion.sa*
%{_libdir}/%{name}/shelp.sa*

%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/saphiresh.1*

%files	devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/lib%{name}.so

%changelog
* Thu Jan 16 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.6.5-35
- Port to C23

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.5-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Mar 06 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.6.5-33
- SPDX migration

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.5-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.5-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.5-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec  6 2022 Florian Weimer <fweimer@redhat.com> - 3.6.5-29
- Declare string_chomp in the installed header file (#2151172)

* Sun Dec  4 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.6.5-28
- Port to C99, -Werror=implicit-function-declaration -Werror=implicit-int

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.6.5-21
- Patch to compile with gcc10 -fno-common

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.6.5-19
- Rebuild for readline 8.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 01 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.6.5-16
- Rebuild against oniguruma 6.8.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 3.6.5-11
- Rebuild for readline 7.x

* Sun Oct 30 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.6.5-10
- Rebuild for oniguruma 6.1.1

* Mon Jul 18 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.6.5-9
- Rebuild for oniguruma 6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug  6 2013 Mamoru TASAKA <mtasaka@fedoraproject.org>
- Fix build error

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 10 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.6.5-1
- 3.6.5
- License changed from GPL+ to MIT

* Thu Jan  5 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.6.4-2
- F-17: rebuild against gcc47

* Sun Dec 18 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.6.4-1
- 3.6.4

* Sun Dec  4 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.6.3-1
- 3.6.3

* Sun Nov 20 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.6.2-1
- 3.6.2

* Thu Nov 17 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.6.1-1
- 3.6.1

* Sun Oct 16 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.5.5-1
- 3.5.5

* Fri Sep 30 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.5.3-1
- 3.5.3

* Fri Sep  9 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.5.1-1
- 3.5.1

* Fri Sep  2 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.5.0-1
- 3.5.0

* Thu Aug 25 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.4.9-1
- 3.4.9

* Sat Aug 20 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.4.7-1
- 3.4.7 

* Sat Aug 20 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.4.5-1
- 3.4.5

* Sat Aug  6 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.4.2-1
- 3.4.2

* Sat Jul 30 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.3.5-1
- 3.3.5

* Tue Jul 26 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.3.3-1
- 3.3.3

* Tue Jul 19 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.3.2-1
- 3.3.2

* Thu Jul 14 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.3.1-1
- 3.3.1

* Mon Jul 11 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.3.0-1
- 3.3.0

* Sun Jul  3 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.2.3-1
- 3.2.3

* Fri Jul  1 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.2.2-1
- 3.2.2

* Sun Jun 26 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.2.1-1
- 3.2.1

* Tue Jun 21 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.2.0-1
- 3.2.0

* Sun Jun 12 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.1.5-1
- 3.1.5

* Wed Jun  8 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.1.4-1
- 3.1.4

* Mon Jun  6 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.1.3-1
- 3.1.3

* Fri Jun  3 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.1.2-1
- 3.1.2

* Sun May 29 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.1.1-1
- 3.1.1

* Sun May 22 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.1.0-1
- 3.1.0

* Thu May 19 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.0.9-1
- 3.0.9

* Mon May 16 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.0.8-1
- 3.0.8

* Mon May  9 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.0.7-1
- 3.0.7

* Tue May  3 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.0.5-1
- 3.0.5

* Sat Apr 29 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.0.3-1
- 3.0.3

* Fri Apr 22 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.0.2-1
- 2.0.2

* Sat Apr 16 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.4.2-1
- 1.4.2
- Use gc for F-14+

* Wed Apr 13 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.4.0-1
- 1.4.0
- Prefer less over lv for help pager

* Sat Apr  9 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.3.8-1
- 1.3.8

* Sun Apr  3 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.3.7-1
- 1.3.7

* Sun Mar 20 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.3.5-1
- 1.3.5

* Sun Mar 13 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.3.2-1
- 1.3.2

* Wed Mar 09 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.3.1-1
- 1.3.1

* Mon Mar 07 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.3.0-1
- 1.3.0

* Thu Feb 24 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.2.8-1
- 1.2.8

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 31 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.6-1
- 1.2.6

* Thu Jan 27 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.5-1
- 1.2.5

* Wed Jan 19 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.4-1
- 1.2.4

* Tue Jan 18 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.3-1
- 1.2.3

* Fri Jan 14 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.1-1
- 1.2.1

* Sun Jan  9 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.0-1
- 1.2.0

* Wed Jan  5 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.1.7-1
- 1.1.7

* Sun Jan  2 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.1.4-1
- 1.1.4

* Sat Jan  1 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.1.2-1
- 1.1.2

* Wed Dec 29 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.1.0-2.respin1
- 1.1.0 respun

* Wed Dec 29 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.1.0-1
- 1.1.0

* Wed Dec 21 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.0.8-1
- 1.0.8

* Tue Dec 21 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.0.7-1
- 1.0.7

* Fri Dec 17 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.0.6-1
- 1.0.6

* Thu Dec 16 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.0.5-1
- 1.0.5

* Thu Dec  9 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.0.2-1
- 1.0.2

* Tue Dec  7 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.0.1-1
- 1.0.1

* Sat Dec  4 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.0.0-1
- 1.0.0

* Fri Nov 10 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.9.5-1
- Initial packaging
