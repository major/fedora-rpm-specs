# https://src.fedoraproject.org/rpms/redhat-rpm-config/blob/master/f/buildflags.md#legacy-fcommon
%define _legacy_common_support 1

Name:		newsx
Version:	1.6
Release:	46%{?dist}
# public domain:
# dbz/dbz-v3.c
# dbz/dbz-v6.c
# dbz/endian.c
# src/hash.c
# src/mkcrc.c
# src/mkcrc.rc
#
# dbz/md5.{c,h} are RSA Message-Digest licensed - ignoring per https://gitlab.com/fedora/legal/fedora-license-data/-/issues/440
# lib/setenv.c is BSD-4-Clause-UC but not compiled into binary
License:	GPL-2.0-or-later AND Zeeff
Summary:	NNTP news exchange utility
Summary(pl):	Narzędzie do wymiany newsów po NNTP
Source0:	ftp://ftp.tin.org/pub/news/utils/newsx/%{name}-%{version}.tar.gz
# Source0-md5:	ad9c76c53d5c7d21d86bec805fe8cd34
Patch0:		%{name}-make.patch
Patch1:		%{name}-stack.patch
Patch2:		%{name}-quotes.patch
# port to automake 1.12+
Patch3:		%{name}-automake.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:	inn-devel
BuildRequires:	automake
BuildRequires:	autoconf
Requires:	inn

%description
Newsx is an NNTP client that will connect to a remote NNTP server and
post outgoing news articles batched by the news system (e.g. INN), as
well as fetch incoming articles.

%description -l pl
Newsx jest klientem NNTP który łączy się ze zdalnym serwerem i wysyła
wychodzące artykuły zgromadzone przez system newsów (np. INN) oraz
pobiera przychodzące artykuły.

%prep
%setup -q
%patch 0 -p1
%patch 1 -p1 -b .stack
%patch 2 -p1 -b .quotes
%patch 3 -p1 -b .am-1.12

%build
autoreconf -f -i
%configure \
	--with-inhosts=/var/spool/news/inhosts \
	--with-newsconfig=/usr/lib/news/lib/innshellvars \
	--with-newslib=%{_libdir}/news/lib \

%make_build

%install
%make_install

# avoid conflict with leafnode
pushd $RPM_BUILD_ROOT
mv .%{_bindir}/newsq .%{_bindir}/newsx-newsq
mv .%{_mandir}/man1/newsq.1 .%{_mandir}/man1/newsx-newsq.1
popd

%files
%doc AUTHORS ChangeLog FAQ NEWS README TODO
%license COPYING
%attr(755,root,root) %{_bindir}/*
%attr(770,root,news) %dir /var/spool/news/inhosts
%{_mandir}/man[158]/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 16 2023 Dominik Mierzejewski <dominik@greysector.net> - 1.6-41
- rebuild for INN 2.7.1
- modernize spec
- use SPDX license identifiers

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 17 2022 Dominik Mierzejewski <dominik@greysector.net> - 1.6-39
- rebuild for INN 2.7.0 (fixes rhbz#2142188)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 21 2020 Dominik Mierzejewski <rpm@greysector.net> 1.6-33
- work around gcc10 build issue

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 05 2017 Kalev Lember <klember@redhat.com> - 1.6-25
- Rebuilt for libinn soname bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 22 2015 Jochen Schmitt <Jochen herr-schmitt de> - 1.6-22
- Rebuilt for new INN release

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 25 2013 Dominik Mierzejewski <rpm@greysector.net> 1.6-18
- port to current automake (fixes FTBFS bug #914215)
- work around perl bug 927170

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Sep 14 2009 Dominik Mierzejewski <rpm@greysector.net> 1.6-13
- changed source URL to tin.org

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 29 2008 Dominik Mierzejewski <rpm@greysector.net> 1.6-10
- recognize single quotes (fixes bug #455806, patch by Enrico Scholz)

* Sat Jul 12 2008 Dominik Mierzejewski <rpm@greysector.net> 1.6-9
- fixed stack buffer overflow in getarticle.c (#454483)
- rebuilt against INN shared libraries (#454897)
- fixed build on rawhide

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.6-8
- Autorebuild for GCC 4.3

* Mon Aug 27 2007 Dominik Mierzejewski <rpm@greysector.net> 1.6-7
- rebuild for BuildID
- update license tag

* Sat Oct 14 2006 Dominik Mierzejewski <rpm@greysector.net> 1.6-6
- rename newsq to avoid conflict with leafnode
- simplify autotools invocation

* Sun Oct 01 2006 Dominik Mierzejewski <rpm@greysector.net> 1.6-5
- fix build on devel

* Fri Jul 27 2006 Dominik Mierzejewski <rpm@greysector.net> 1.6-3
- remove unnecessary Provides: tag

* Sun Apr 02 2006 Dominik Mierzejewski <rpm@greysector.net> 1.6-2
- fix BuildReqs

* Sat Jan 07 2006 Dominik Mierzejewski <rpm@greysector.net> 1.6-1
- FE compliance

* Sun Sep 25 2005 Dominik Mierzejewski <rpm@greysector.net>
- rebuilt for Fedora based on PLD specfile
