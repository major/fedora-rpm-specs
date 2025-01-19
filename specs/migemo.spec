%define		migemover	0.40

%define		emacsver	21.4
%define		xemacsver	21.4
%define		e_sitedir	%{_datadir}/emacs/site-lisp
%define		xe_sitedir	%{_datadir}/xemacs/site-lisp
%define		rubyabi		1.9.1

Name:		migemo
Version:	%{migemover}
Release:	45%{?dist}
Summary:	Japanese incremental search tool

# migemo-dict	GPL-2.0-or-later
# migemo.el.in	GPL-2.0-or-later
# Otherwise	GPL-2.0-only
# SPDX confirmed
License:	GPL-2.0-only AND GPL-2.0-or-later
URL:		http://0xcc.net/migemo/
Source0:	http://0xcc.net/migemo/%{name}-%{version}.tar.gz
# patch taken and modified from http://d.hatena.ne.jp/yshl/20090814/1250197679
Patch0:		migemo-ruby-1.9.patch
# See bug 830559
Patch1:		migemo-0.40-bz830559.patch

BuildArch:	noarch

BuildRequires:  make
BuildRequires:  glibc-langpack-ja
Requires:	ruby(release)
BuildRequires:	ruby(release)
BuildRequires:	ruby
BuildRequires:	ruby-devel

BuildRequires:	ruby(romkan)
BuildRequires:	ruby(bsearch)
BuildRequires:	emacs >= %{emacsver}
%if 0%{?fedora} < 36
BuildRequires:	xemacs >= %{xemacsver}
%endif
Requires:	ruby(romkan)
Requires:	ruby(bsearch)

%if 0%{?fedora} >= 36
Obsoletes:	%{name}-xemacs < 0.40-36
%endif

%description
Ruby/Migemo is a tool for Japanese incremental search.

%package	emacs
Summary:	Emacs front-end of Migemo
Requires:	%{name} = %{version}-%{release}
Requires:	emacs(bin) >= %{emacsver}
Requires:	apel

%description	emacs
%{summary}.

%if 0%{?fedora} < 36
%package	xemacs
Summary:	XEmacs front-end of Migemo
Requires:	%{name} = %{version}-%{release}
Requires:	xemacs(bin) >= %{emacsver}
Requires:	apel

%description	xemacs
%{summary}.
%endif

%prep
%setup -q
%patch -P0 -p1
sed -i '18d' migemo-convert.rb # patching is failing probably because of the special chars, so do this by sed
%patch -P1 -p1

%build
%configure \
	--with-rubydir=%{ruby_vendorlibdir}
%{__make} %{?_smp_mflags} migemo.elc

%install
%{__rm} -rf $RPM_BUILD_ROOT
export LANG=ja_JP.eucJP
%{__make} INSTALL="%{__install} -c -p" DESTDIR=$RPM_BUILD_ROOT install

%if 0%{?fedora} < 36
# For xemacs
%{__rm} -f migemo.elc
%configure \
	--with-rubydir=%{ruby_sitelib} \
	--with-emacs=xemacs \
	--with-lispdir=%{xe_sitedir}
%{__make} INSTALL="%{__install} -c -p" DESTDIR=%{buildroot} install-lispLISP
%endif

%check
export LANG=ja_JP.eucJP
cd tests
for f in *.sh ; do \
	sh ./$f || :
done

%files
%defattr(-,root,root,-)
%doc AUTHORS
%doc ChangeLog
%license COPYING
%doc README

%{_bindir}/migemo*
%{_datadir}/migemo/
%{ruby_vendorlibdir}/migemo*

%files	emacs
%defattr(-,root,root,-)
%{e_sitedir}/migemo.el*

%if 0%{?fedora} < 36
%files	xemacs
%defattr(-,root,root,-)
%{xe_sitedir}/migemo.el*
%endif

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan  7 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.40-41
- SPDX migration

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov  9 2021 Jerry James <loganjerry@gmail.com> - 0.40-36
- Drop support for XEmacs in F36 and later

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 05 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.40-29
- Add BR:glibc-langpack-ja
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Nov  7 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.40-22
- Limit emacs / xemacs Requires to emacs(bin) or so (bug 1154495)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 20 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.40-19
- F-19: rebuild for ruby 2.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.40-16
- Fix crash on migemo-dict.rb with actual use (bug 830559)

* Fri Mar 02 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.40-15
- Rebuilt and patched for Ruby 1.9.3.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Feb 25 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.40-13
- Change %%SUMMARY to %%summary so that the macro is expanded

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.40-11
- F-12: Mass rebuild

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.40-10
- Explicitly add the leading path for scripts under current path
  for bash 4.0 change

* Fri Aug  3 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.40-9.dist.1
- License update

* Thu Apr 26 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.40-9
- Specify Ruby abi

* Thu Apr 12 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.40-8
- Rewrite

* Sun Apr 08 2007 Minokichi Sato <m-sato@rc.kyushu-u.ac.jp>
- First build for Fedora Core 6

* Thu Feb 22 2007 NAKAYA Toshiharu <nakaya@momonga-linux.org>
- (0.40-7m)
- add dependencies on apel

* Tue Jun 28 2005 Toru Hoshina <t@momonga-linux.org>
- (0.40-6m)
- /usr/lib/ruby

* Fri Feb 18 2005 Dai OKUYAMA <dai@ouchi.nahi.to>
- (0.40-5m)
- enable x86_64.
- xemacs elisps destination is moved from %%{_libdir} to %%{_datadir}.

* Thu Nov 25 2004 Shigeyuki Yamashita <shige@momonga-linux.org>
- (0.40-4m)
- rebuild against emacs-21.3.50 (nen no tame...)

* Tue Mar 23 2004 Toru Hoshina <t@momonga-linux.org>
- (0.40-3m)
- revised spec for enabling rpm 4.2.

* Tue Aug  5 2003 Kazuhiko <kazuhiko@fdiary.net>
- (0.40-2m)
- rebuild against ruby-1.8

* Fri May 30 2003 Shigeyuki Yamashita <shige@cty-net.ne.jp>
- (0.40-1m)
- update 0.40

* Sat Sep  1 2001 Kazuhiko <kazuhiko@kondara.org>
- (0.32-2k)
- Obsoletes: jrsearch-emacs
- divide into migemo, migemo-emacs, and migemo-xemacs packages
