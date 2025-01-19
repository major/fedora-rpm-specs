%global	repoid		54457

%global	minver_saphire	3.6.5

Name:		mfiler3
Version:	4.4.9
Release:	33%{?dist}
Summary:	Two pane file manager under UNIX console

# SPDX confirmed
License:	MIT
URL:		http://www.geocities.jp/daisuke530221jp/index3.html
Source0:	http://dl.sourceforge.jp/%{name}/%{repoid}/%{name}-%{version}.tgz
Source10:	mfiler3.sh

# Obsoletes but not Provides
Obsoletes:	%{name}-mdnd < 3.0.0

BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	cmigemo-devel
%if 0
BuildRequires:	gc-devel
%endif
# For -Werror=implicit-function-declaration, updated saphire header is needed.
BuildRequires:	saphire-devel >= %{minver_saphire}-29
BuildRequires:	ncurses-devel
BuildRequires:	oniguruma-devel

Requires:	saphire >= %{minver_saphire}

%description
Minnu's Filer3 is a two pane file manager under UNIX console.

%prep
%setup -q

# Don't strip, preserve timestamp
%{__sed} -i.strip -e 's| -s -m| -m|' Makefile.in
%{__sed} -i.stamp -e 's|\([ \t][ \t]*install \)|\1 -p |' Makefile.in

# May have to ask the upstream...
%{__sed} -i.sao -e 's|saphire -c|saphire -rn -c|' Makefile.in

%{__rm} -f *.o

# Prefer less over lv
sed -i.pager \
	-e 's| lv| less|' \
	-e 's|lv |less |' \
	mfiler3.sa

%build
# -D_DEFAULT_SOURCE etc is for wcswidth
%configure \
	CC="gcc %{optflags} -D_XOPEN_SOURCE=700 -D_DEFAULT_SOURCE" \
	--sysconfdir=%{_libdir}/%{name} \
	--bindir=%{_libexecdir}/%{name} \
	--with-migemo \
	--with-system-migemodir=%{_datadir}/cmigemo

# kill parallel make
%{__make} -k \
	docdir=%{_defaultdocdir}/%{name}/

%install
# make install DESTDIR=%%{buildroot}
# Above does not work...
rm -rf ./Trash
%makeinstall \
	sysconfdir=$RPM_BUILD_ROOT%{_libdir}/%{name} \
	bindir=$RPM_BUILD_ROOT%{_libexecdir}/%{name} \
	docdir=$(pwd)/Trash/

# Install wrapper script
%{__mkdir_p} $RPM_BUILD_ROOT%{_bindir}
%{__install} -cpm 0755 %SOURCE10 $RPM_BUILD_ROOT%{_bindir}/%{name}

%files
%defattr(-,root,root,-)
%doc	AUTHORS
%doc	CHANGELOG.txt
%license	LICENSE
%doc	README.en.txt
%doc	USAGE.en.txt
%lang(ja)	%doc	README.ja.txt
%lang(ja)	%doc	USAGE.ja.txt

%{_bindir}/%{name}
%{_libexecdir}/%{name}/
%{_libdir}/%{name}/

%{_mandir}/man1/mfiler3.1*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.9-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.9-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Mar 06 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.4.9-31
- SPDX migration

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.9-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.9-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.9-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.9-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec  6 2022 Florian Weimer <fweimer@redhat.com> - 4.4.9-26
- Build with -D_XOPEN_SOURCE=700 -D_DEFAULT_SOURCE for wcswidth
- Build against newer saphire-devel for string_chomp declaration

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.9-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.9-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.9-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.9-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.9-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.9-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.9-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.9-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 01 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.4.9-17
- Rebuild against oniguruma 6.8.1

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Oct 30 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.4.9-12
- Rebuild for oniguruma 6.1.1

* Mon Jul 18 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.4.9-11
- Rebuild for oniguruma 6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug  7 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.4.9-6
- F-20: adjust for feature: UnversionedDocdirs

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jan 11 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.4.9-2
- Fix saphire Requires

* Tue Jan 10 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.4.9-1
- 4.4.9
- License changed from GPL+ to MIT

* Thu Jan  5 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.4.8-3
- F-17: rebuild against gcc47

* Sun Dec 18 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.4.8-2
- Rebuild against new saphire

* Sun Dec  4 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.4.8-1
- 4.4.8

* Sun Nov 20 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.4.7-1
- 4.4.7

* Thu Nov 17 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.4.6-1
- 4.4.6

* Sun Oct 16 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.4.3-3
- Rebuild against new saphire

* Fri Sep 30 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.4.3-2
- Rebuild against new saphire

* Fri Sep  2 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.4.3-1
- 4.4.3

* Thu Aug 25 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.4.2-1
- 4.4.2

* Sun Aug 21 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.4.1-3
- Rebuild against new saphire

* Sat Aug  6 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.4.1-2
- Rebuild against newer saphire

* Fri Jul 29 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.4.1-1
- 4.4.1

* Tue Jul 19 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.4.0-2
- Rebuild against new saphire

* Sun Jul 11 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.4.0-1
- 4.4.0

* Sun Jun 26 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.3.9-3
- Rebuild against new saphire

* Tue Jun 21 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.3.9-2
- Rebuild against new saphire

* Wed Jun  8 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.3.9-1
- 4.3.9

* Mon Jun  6 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.3.6-3
- Rebuild against new saphire

* Mon May 29 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.3.6-2
- Rebuild

* Thu May 19 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.3.6-1
- 4.3.6

* Mon May 16 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.3.5-2
- Rebuild against new saphire

* Mon May  9 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.3.5-1
- 4.3.5

* Tue May  3 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.3.4-2
- Rebuild against newer saphire

* Sat Apr 29 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.3.4-1
- 4.3.4

* Sat Apr 16 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.2.8-1
- 4.2.8
- enable gc on F-14+

* Thu Apr 14 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.2.7-2
- Fix compilation error with saphire 1.4.0 (and actually fix
  symbol error)
- Prefer less over lv for help pager

* Sun Apr  3 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.2.7-1
- 4.2.7

* Sun Mar 20 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.2.5-1
- 4.2.5

* Sun Mar 13 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.2.4-1
- 4.2.4

* Thu Mar 10 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.2.2-2.respin1
- 4.2.2 respun

* Wed Mar 09 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.2.2-1
- 4.2.2

* Mon Mar  7 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 4.2.1-5
- Rebuild against new saphire

* Thu Feb 24 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 4.2.1-4
- Rebuild against new saphire

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb  3 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 4.2.1-2
- Rebuild against new saphire

* Wed Jan 19 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 4.2.1-1
- 4.2.1

* Tue Jan 18 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 4.2.0-1
- 4.2.0

* Sun Jan  9 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 4.1.8-1
- 4.1.8

* Wed Jan  5 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 4.1.3-1
- 4.1.3

* Wed Dec 29 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 4.1.1-1
- 4.1.1

* Tue Dec 21 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 4.1.0-1
- 4.1.0

* Fri Dec 17 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 4.0.9-1
- 4.0.9-1

* Thu Dec 16 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 4.0.8-1
- 4.0.8

* Thu Dec  9 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 4.0.6-1
- 4.0.6

* Tue Dec  7 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 4.0.5-1
- 4.0.5

* Sat Dec  4 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 4.0.4-1
- 4.0.4

* Tue Aug 24 2010 Adam Tkac <atkac@redhat.com> - 3.0.8-2
- rebuild

* Mon Mar  8 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 3.0.8-1
- 3.0.8

* Sun Mar  7 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 3.0.7-2.respin1
- 3.0.7 respun (patch0 no longer needed)

* Sat Mar  6 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 3.0.7-1
- 3.0.7

* Tue Mar  2 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 3.0.6-1
- 3.0.6

* Thu Feb 25 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 3.0.5-1
- Update to 3.0.5

* Tue Feb 23 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 3.0.4-1
- Update to 3.0.4

* Sat Feb 20 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 3.0.3-1
- Update to 3.0.3

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.1.3-3
- F-12: Mass rebuild

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.1.3-2
- F-11: Mass rebuild

* Sun Nov  9 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.1.3-1
- 2.1.3

* Sun Nov  2 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.1.2-1
- 2.1.2

* Sat Oct 18 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.1.1-1
- 2.1.1

* Wed Oct 15 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.1.0-2
- New tarball

* Wed Oct 15 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.1.0-1
- 2.1.0
- All patches in the previous rpm are applied by the upstream

* Sat Sep 27 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.8a-3
- Better system-wide cmigemo patch

* Sat Sep 27 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.8a-2
- Fix sparc64 build error

* Fri Sep 26 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.8a-1
- 2.0.8a
- More better upgrade compat patch

* Mon Sep 14 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.7-2
- 2.0.7
- Workaround patch to deal with segv after upgrade

* Thu Aug 28 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.6-2
- 2.0.6

* Fri Aug  8 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.5-1
- 2.0.5

* Tue Aug  5 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.2-1
- 2.0.2

* Tue Jul 15 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.0-1
- 2.0.0

* Tue Jul  1 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.1.2-1
- 1.1.2

* Sat Jun 28 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.1.1-1
- 1.1.1

* Mon Jun 23 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.0.2-1
- 1.0.2
- -Werror-implicit-function-declaration is added in the source tarball

* Sun Jun 22 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.0.1-1
- 1.0.1

* Thu Jun 19 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.0.0-1
- 1.0.0
- Add -Werror-implicit-function-declaration

* Tue Jun  3 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.2.1-1
- Initial packaging
- Make mfiler3 parallel installable with mfiler2

