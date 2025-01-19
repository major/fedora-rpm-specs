Name:           liboping
Version:        1.10.0
Release:        32%{?dist}
Summary:        A C library to generate ICMP echo requests

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://noping.cc/
Source0:        https://noping.cc/files/%{name}-%{version}.tar.bz2
# Disable -Werror to avoid https://github.com/octo/liboping/issues/38
Patch0:         liboping-1.10.0-no-werror.patch
# Fix build with ncurses-6.3 https://github.com/octo/liboping/pull/61
# Note: slightly tweaked, since we don't have
#       https://github.com/octo/liboping/commit/47130cb9c2cdc900acf1daca1d028c87eccd2004
Patch1:         liboping-1.10.0-ncurses-6.3.patch

BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  ncurses-devel
BuildRequires:  make


%description
Liboping is a C library to generate ICMP echo requests, better known as
"ping packets". It is intended for use in network monitoring applications
or applications that would otherwise need to fork ping(1) frequently.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains files needed to develop and build software against
liboping, a %{summary}.

%prep
%autosetup -p1

%build
%configure --disable-static
# The application uses a local copy of libtool, we need to remove rpath with the
# following two lines (see https://fedoraproject.org/wiki/Packaging/Guidelines#Beware_of_Rpath)
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make -C src %{?_smp_mflags}
make -C bindings %{?_smp_mflags} perl/Makefile
cd bindings/perl
%{__perl} Makefile.PL INSTALLDIRS=vendor TOP_BUILDDIR=..
%make_build

%install
make -C src install DESTDIR=%{buildroot}
cd bindings/perl
make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
LD_LIBRARY_PATH=../../src/.libs make -C bindings/perl test

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog README
%license COPYING
%{_bindir}/oping
%{_bindir}/noping
%{_libdir}/liboping.so.*
%{_mandir}/man8/oping.8*
%{_mandir}/man3/Net::Oping.3pm*
%{perl_vendorarch}/*
%exclude %{_libdir}/liboping.la

%files devel
%{_includedir}/oping.h
%{_libdir}/liboping.so
%{_libdir}/pkgconfig/liboping.pc
%{_mandir}/man3/liboping.3*
%{_mandir}/man3/ping_construct.3*
%{_mandir}/man3/ping_get_error.3*
%{_mandir}/man3/ping_host_add.3*
%{_mandir}/man3/ping_iterator_get.3*
%{_mandir}/man3/ping_iterator_get_context.3*
%{_mandir}/man3/ping_iterator_get_info.3*
%{_mandir}/man3/ping_send.3*
%{_mandir}/man3/ping_setopt.3*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.10.0-31
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Jitka Plesnikova <jplesnik@redhat.com> - 1.10.0-29
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.10.0-25
- Perl 5.38 rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.10.0-22
- Perl 5.36 rebuild

* Tue May 03 2022 Frantisek Sumsal <frantisek@sumsal.cz> - 1.10.0-21
- Fix build with ncurses-6.3 (BZ#2080201)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Sep 25 2021 Frantisek Sumsal <frantisek@sumsal.cz> - 1.10.0-19
- FTBFS fix - drop redundant RPATH (BZ#1969505)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.10.0-17
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-15
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.10.0-13
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.10.0-10
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Adam Williamson <awilliam@redhat.com> - 1.10.0-8
- Disable -Werror to fix build (see upstream #38)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.10.0-6
- Perl 5.28 rebuild

* Mon Jun 18 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.10.0-6
- Update links

* Thu Mar 15 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.10.0-5
- Update BR

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 15 2017 Fabian Affolter <mail@fabian-affolter.ch> - 1.10.0-1
- Update to latest upstream version 1.10.0 (rhbz#1450029)

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.9.0-3
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 14 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.9.0-1
- Update to latest upstream version 1.9.0 (rhbz#1350992)

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.8.0-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.8.0-2
- Perl 5.22 rebuild

* Fri Nov 21 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.8.0-1
- Update to latest upstream version 1.8.0 (rhbz#1166357)

* Fri Sep 26 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.7.0-1
- Update to latest upstream version 1.7.0 (rhbz#1146892)

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.2-5
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 24 2013 Lubomir Rintel <lkundrak@v3.sk> - 1.6.2-2
- Bulk sad and useless attempt at consistent SPEC file formatting

* Sat Aug 10 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.2-1
- Update to latest upstream version 1.6.2

* Sat Aug 10 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.0-1
- Update to latest upstream version 1.6.0
- Spec file updated

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.5.1-8
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.5.1-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 15 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.5.1-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Dec 04 2010 Lubomir Rintel <lkundrak@v3.sk> - 1.5.1-1
- Bump to later version

* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.3.4-2
- Mass rebuild with perl-5.12.0

* Tue Mar 09 2010 Lubomir Rintel <lkundrak@v3.sk> - 1.3.4-1
- Initial packaging
