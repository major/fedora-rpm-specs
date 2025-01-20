Name:		renrot
Version:	1.2.0
Release:	27%{?dist}
Summary:	A program to rename and rotate files according to EXIF tags

License:	Artistic-2.0
URL:		http://puszcza.gnu.org.ua/projects/renrot/
Source0:	ftp://download.gnu.org.ua/pub/release/renrot/%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires: make
BuildRequires:	perl-interpreter
BuildRequires:	perl-generators
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Image::ExifTool) >= 5.72
BuildRequires:	perl(Getopt::Long) >= 2.34
Requires:	/usr/bin/jpegtran
%if 0%{?fedora}
Recommends:	perl(Image::Magick)
%endif

%{?perl_default_filter}

%description
Renrot renames files according the DateTimeOriginal and FileModifyDate
EXIF tags, if they exist. Otherwise, the name will be set according to
the current timestamp. Additionally, it rotates files and their
thumbnails, accordingly Orientation EXIF tag.

The script can also put commentary into the Commentary and UserComment
tags.

Personal details can be specified via XMP tags defined in a
configuration file.


%prep
%autosetup


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make_build


%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} $RPM_BUILD_ROOT/*

# Fix shbang
sed -i 's|#!/usr/bin/env perl|#!/usr/bin/perl|' $RPM_BUILD_ROOT%{_bindir}/renrot

# install sample configuration files
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install -m644 etc/colors.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install -m644 etc/copyright.tag $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install -m644 etc/renrot.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install -m644 etc/tags.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}


%check
make test


%files
%doc AUTHORS README ChangeLog NEWS TODO
%lang(ru) %doc README.russian
%{perl_vendorlib}/*
%{_bindir}/renrot
%{_mandir}/man1/*.1*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/colors.conf
%config(noreplace) %{_sysconfdir}/%{name}/copyright.tag
%config(noreplace) %{_sysconfdir}/%{name}/renrot.conf
%config(noreplace) %{_sysconfdir}/%{name}/tags.conf


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Apr 21 2024 Charles R. Anderson <cra@alum.wpi.edu> - 1.2.0-25
- Fix SPDX license string

* Sat Apr 20 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.0-24
- convert license to SPDX

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.2.0-18
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.2.0-15
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.2.0-12
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.2.0-9
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.2.0-6
- Perl 5.28 rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.0-5
- Escape macros in %%changelog

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.2.0-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan  2 2017 Charles R. Anderson <cra@wpi.edu> - 1.2.0-1
- Update to 1.2.0
- Modernize spec file
- Remove ancient config file conversion trigger
- Use standard path to perl interpreter
- Recommends: perl(Image::Magick) on Fedora

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.1-3.13
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3.12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.1-3.10
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.1-3.9
- Perl 5.20 rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 1.1-3.6
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 1.1-3.3
- Perl 5.16 rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Petr Sabata <contyk@redhat.com> - 1.1-3
- Perl mass rebuild
- Dropping now obsolete Buildroot and defattr
- Commenting Requires(hint) out since fedpkg refuses to work with it

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 01 2010 Adam Tkac <atkac redhat com> - 1.1-2
- Require /usr/bin/jpegtran instead of libjpeg; compatible with both
  libjpeg and libjpeg-turbo

* Wed Jun 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.1-1.4
- Mass rebuild with perl-5.12.0

* Wed Jun 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.1-1.3
- Mass rebuild with perl-5.12.0

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Oct 07 2008 Andy Shevchenko <andy@smile.org.ua> - 1.1-1
- update to 1.1

* Mon Oct 06 2008 Andy Shevchenko <andy@smile.org.ua> - 1.1-0.3.rc3
- update to 1.1rc3
- change License to Artistic 2.0 accordingly to mainstream
- update URLs
- require (optional) Image::Magick

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.25-4.1
Rebuild for new perl

* Tue Sep 04 2007 Andy Shevchenko <andy@smile.org.ua> 0.25-3.1
- Fix License tag
- Add BuildRequires: perl(ExtUtils::MakeMaker)

* Fri Oct 06 2006 Andy Shevchenko <andy@smile.org.ua> 0.25-2
- update to 0.25
- fix tarball

* Sun Sep 03 2006 Andy Shevchenko <andriy@asplinux.com.ua> 0.24-1
- update to 0.24

* Tue Aug 22 2006 Andy Shevchenko <andy@smile.org.ua>
- add colors.conf

* Sat Aug 19 2006 Andy Shevchenko <andriy@asplinux.com.ua> 0.23-1
- update to 0.23

* Tue Jul 18 2006 Andy Shevchenko <andriy@asplinux.com.ua> 0.22-1.0
- update to 0.22

* Thu Jul 06 2006 Andy Shevchenko <andriy@asplinux.com.ua> 0.21.1-2
- rebuild

* Thu Jul 06 2006 Andy Shevchenko <andriy@asplinux.com.ua> 0.21.1-1
- update to 0.21.1

* Mon Jun 12 2006 Andy Shevchenko <andriy@asplinux.com.ua> 0.21-1
- update to 0.21

* Wed Jun 07 2006 Andy Shevchenko <andriy@asplinux.com.ua>
- relocate configuration to %%_sysconfdir/%%name

* Sat Jun 03 2006 Andy Shevchenko <andriy@asplinux.com.ua> 0.20-2
- remove BR: perl
- fix renrot permissions

* Thu Jun 01 2006 Andy Shevchenko <andriy@asplinux.com.ua> 0.20-1
- update to 0.20

* Mon May 22 2006 Andy Shevchenko <andriy@asplinux.com.ua> 0.19.3-1
- update to 0.19.3

* Fri May 19 2006 Andy Shevchenko <andriy@asplinux.com.ua> 0.19.2-1
- update to 0.19.2

* Mon May 15 2006 Andy Shevchenko <andriy@asplinux.com.ua> 0.19-1
- update to 0.19

* Mon May 15 2006 Andy Shevchenko <andriy@asplinux.com.ua>
- install rc-file

* Mon May 01 2006 Andy Shevchenko <andriy@asplinux.com.ua> 0.16.1-1
- update to 0.16.1

* Tue Apr 18 2006 Andy Shevchenko <andriy@asplinux.com.ua>
- initial package
