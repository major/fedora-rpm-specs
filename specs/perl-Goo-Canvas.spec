Name:           perl-Goo-Canvas
Version:        0.06
Release:        58%{?dist}
Summary:        Perl interface to the GooCanvas
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Goo-Canvas
Source0:        https://cpan.metacpan.org/authors/id/Y/YE/YEWENBIN/Goo-Canvas-%{version}.tar.gz
Source1:        Changes.20090614
Patch0:         perltetris_pl-undefined.diff
Patch1:         perl-Goo-Canvas-c99.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  goocanvas-devel
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Cairo) >= 1.00
BuildRequires:  perl(ExtUtils::Depends) >= 0.2
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::PkgConfig) >= 1.0
BuildRequires:  perl(Glib) >= 1.103
BuildRequires:  perl(Glib::MakeHelper)
BuildRequires:  perl(Gtk2) >= 1.100
BuildRequires:  perl(Test::More)

%{?perl_default_filter:
%filter_from_requires /perl(Tetris/d
%filter_from_requires /perl(Mine/d
%?perl_default_filter
}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Tetris|Mine

%description
GTK+ does't has an buildin canvas widget. GooCanvas is wonderful. It is easy to use
and has powerful and extensible way to create items in canvas. Just try it.
For more documents, please read GooCanvas Manual and the demo programs provided
in the source distribution in both perl-Goo::Canvas and GooCanvas.

%prep
%setup -q -n Goo-Canvas-%{version}
pushd bin
%patch -P0 -p0 -b .warning
popd
%patch -P1 -p1
cp -f %{SOURCE1} Changes

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags} NOECHO=

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT%{_bindir}/perltetris.pl $RPM_BUILD_ROOT%{_bindir}/perlfangkuai.pl
mv $RPM_BUILD_ROOT%{_mandir}/man1/perltetris.pl.1 $RPM_BUILD_ROOT%{_mandir}/man1/perlfangkuai.pl.1
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes goocanvas.typemap maps README
%{_bindir}/*
%{_mandir}/man3/*.3*
%{perl_vendorarch}/Goo/
%{_mandir}/man1/*.1.gz
%{perl_vendorarch}/auto/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug  6 2024 Miroslav Suchý <msuchy@redhat.com> - 0.06-57
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 11 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-55
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-51
- Perl 5.38 rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 13 2023 Martin Gansser <martinkg@fedoraproject.org> - 0.06-49
- Rebuilt it due shutter required it for rawhide

* Fri Dec  9 2022 Florian Weimer <fweimer@redhat.com> - 0.06-48
- Add goocanvas private function declarations for C99 compatibility

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-46
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-43
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-40
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-37
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-34
- Perl 5.28 rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.06-33
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-29
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-27
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-24
- Perl 5.22 rebuild

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-23
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Petr Pisar <ppisar@redhat.com> - 0.06-19
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Petr Pisar <ppisar@redhat.com> - 0.06-16
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 10 2011 Iain Arnell <iarnell@gmail.com> 0.06-14
- Rebuild for libpng 1.5
- BuildRequires perl(Test::More)

* Mon Jun 25 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.06-13
- add new filter

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.06-12
- Perl mass rebuild

* Sat Feb 19 2011 Iain Arnell <iarnell@gmail.com> 0.06-11
- add filtering for provides/requires

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 17 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.06-9
- 661697 rebuild for fixing problems with vendorach/lib

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.06-8
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.06-7
- rebuild against perl 5.10.1

* Sun Jul 28 2009 Liang Suilong <liangsuilong@gmail.com> 0.06-6
- Add BR: perl(Glib::MakeHelper)
- Remove BR: perl-Glib-devel

* Sun Jul 28 2009 Liang Suilong <liangsuilong@gmail.com> 0.06-5
- Change BuildRequires from perl(Glib::MakeHelper) to perl(Glib)
- Add BR: perl-Glib-devel

* Sun Jul 27 2009 Liang Suilong <liangsuilong@gmail.com> 0.06-4
- Change BuildRequires from perl(Glib) to perl(Glib::MakeHelper)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 15 2009 Liang Suilong <liangsuilong@gmail.com> 0.06-2
- Correct directory ownership
- Correct the typo in %%description 

* Thu Jun 11 2009 Liang Suilong <liangsuilong@gmail.com> 0.06-1
- Upstream to perl-Goo-Canvas-0.06-1
- Update Changes

* Thu Jun 11 2009 Liang Suilong <liangsuilong@gmail.com> 0.05-6
- Rename perltertris.pl.1 as perlfangkuang.pl.1
- Update Changes

* Wed May 27 2009 Liang Suilong <liangsuilong@gmail.com> 0.05-5
- Rename perltertris.pl as perlfangkuang.pl and update README and Changes

* Sun Apr 21 2009 Liang Suilong <liangsuilong@gmail.com> 0.05-4
- Modify BuildRequires and correct the %%files.

* Sun Apr 05 2009 Liang Suilong <liangsuilong@gmail.com> 0.05-3
- Specfile autogenerated by cpanspec 1.77.

* Fri Mar 13 2009 Suilong Liang <liangsuilong@gmail.com> -0.05-2
-  Fix the bug that the package could not be built on x86_64

* Sun Jan 18 2009 Suilong Liang <liangsuilong@gmail.com> -0.05-1
- Initial package for Fedora 10.
