# Run X11 test
%bcond_without perl_Gtk2_Unique_enables_x11_test

Name:			perl-Gtk2-Unique
Version:		0.07
Release:		7%{?dist}
Summary:		Perl bindings for the C library "libunique" (DEPRECATED)
License:		GPL+ or Artistic
URL:			https://metacpan.org/release/Gtk2-Unique
Source0:		http://cpan.metacpan.org/authors/id/X/XA/XAOC/Gtk2-Unique-%{version}.tar.gz
BuildRequires:		coreutils
BuildRequires:		findutils
BuildRequires:		gcc
BuildRequires:		make
BuildRequires:		perl-devel
BuildRequires:		perl-generators
BuildRequires:		perl-interpreter
BuildRequires:		perl(Cwd)
BuildRequires:		perl(ExtUtils::Depends) >= 0.20
BuildRequires:		perl(ExtUtils::MakeMaker)
BuildRequires:		perl(ExtUtils::PkgConfig) >= 1.03
BuildRequires:		perl(File::Spec)
BuildRequires:		perl(Glib::MakeHelper)
BuildRequires:		perl(Gtk2::CodeGen)
BuildRequires:		perl(strict)
BuildRequires:		perl(warnings)
BuildRequires:		pkgconfig(unique-1.0)
# Run-time:
BuildRequires:		perl(base)
BuildRequires:		perl(DynaLoader)
# Gtk2 1.161 version in Makefile.PL is only a rough guess
BuildRequires:		perl(Gtk2) >= 1.00
# Tests:
BuildRequires:		perl(Data::Dumper)
BuildRequires:		perl(Glib) >= 1.180
%if %{with perl_Gtk2_Unique_enables_x11_test}
BuildRequires:		xorg-x11-server-Xvfb
BuildRequires:		font(:lang=en)
%endif

Requires:		perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
# Gtk2 1.161 version in Makefile.PL is only a rough guess
Requires:		perl(Gtk2) >= 1.00

%{?perl_default_filter}
# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Gtk2\\)$

%description
Gtk2::Unique is a Perl binding for the C library libunique 
which provides a way for writing single instance application. 
If you launch a single instance application twice, the second 
instance will either just quit or will send a message to 
the running instance.

For more information about libunique see: 
http://live.gnome.org/LibUnique.

%package devel
Summary:		Development headers for %{name}
Requires:		%{name} = %{version}-%{release}

%{?perl_default_filter}

%description devel
Development headers for %{name}

%prep
%setup -q -n Gtk2-Unique-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%if %{with perl_Gtk2_Unique_enables_x11_test}
	xvfb-run -a make test
%else
	make test
%endif

%files
%doc Changes README
%{perl_vendorarch}/auto/Gtk2/Unique/
%{perl_vendorarch}/Gtk2*
%exclude %{perl_vendorarch}/Gtk2/Unique/Install/*.h
%{_mandir}/man3/*.3pm*

%files devel
%{perl_vendorarch}/Gtk2/Unique/Install/*.h

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-6
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-1
- 0.07 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-30
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-27
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-24
- Perl 5.28 rebuild

* Wed Apr 11 2018 Petr Pisar <ppisar@redhat.com> - 0.05-23
- Fix a crash when runnig multiple instances (bug #1560182)
- Specify all dependencies
- Perform tests

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-19
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-17
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-14
- Perl 5.22 rebuild

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-13
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Petr Pisar <ppisar@redhat.com> - 0.05-9
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Petr Pisar <ppisar@redhat.com> - 0.05-6
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 09 2011 Iain Arnell <iarnell@gmail.com> 0.05-4
- Rebuild for libpng 1.5
- BuildRequires perl(Test::More)

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.05-3
- Perl mass rebuild

* Sun Jun 19 2011 Liang Suilong <liangsuilong@gmail.com> 0.05-2
- Add a devel subpackage
- Fix spec file errors 

* Sat Jun 04 2011 Liang Suilong <liangsuilong@gmail.com> 0.05-1
- Intial Package for Fedora 15

