%global cpan_version 1.9.02

Name:       perl-App-Asciio 
Version:    1.90.02
Release:    4%{?dist}
# see lib/App/Asciio.pm
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:    Asciio back-end libraries 
Source:     https://cpan.metacpan.org/authors/id/N/NK/NKH/App-Asciio-%{cpan_version}.tar.gz 
Url:        https://metacpan.org/release/App-Asciio
BuildArch:  noarch

# non-perl
BuildRequires: make
BuildRequires: desktop-file-utils

BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl(Algorithm::Diff)
BuildRequires: perl(Clone)
BuildRequires: perl(Compress::Bzip2)
BuildRequires: perl(Cwd)
BuildRequires: perl(Data::Compare)
BuildRequires: perl(Data::TreeDumper)
BuildRequires: perl(Data::TreeDumper::Renderer::GTK)
BuildRequires: perl(Directory::Scratch)
BuildRequires: perl(Directory::Scratch::Structured)
BuildRequires: perl(Eval::Context)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Copy)
BuildRequires: perl(File::Slurp)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Glib)
BuildRequires: perl(Gtk2)
BuildRequires: perl(Gtk2::Gdk::Keysyms)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(List::Util)
BuildRequires: perl(MIME::Base64)
BuildRequires: perl(Module::Util)
BuildRequires: perl(Readonly)
BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Block)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::NoWarnings)
BuildRequires: perl(Test::Strict)
BuildRequires: perl(Test::Warn)
BuildRequires: perl(version) >= 0.5

# keep rpmlint happy 
Requires:      perl(lib)

# this package has a rather basic way of mixing-in functionalities that leads
# rpm to believe that it doesn't actually provide these
Provides: perl(App::Asciio::Actions)     = %{version}
Provides: perl(App::Asciio::Ascii)       = %{version}
Provides: perl(App::Asciio::Connections) = %{version}
Provides: perl(App::Asciio::Dialogs)     = %{version}
Provides: perl(App::Asciio::Elements)    = %{version}
Provides: perl(App::Asciio::GTK::Asciio::Dialogs)   = %{version}
Provides: perl(App::Asciio::GTK::Asciio::Menues)    = %{version}
Provides: perl(App::Asciio::GTK::Asciio::stripes::editable_arrow2)  = %{version}
Provides: perl(App::Asciio::GTK::Asciio::stripes::editable_box2)    = %{version}
Provides: perl(App::Asciio::GTK::Asciio::stripes::wirl_arrow)       = %{version}
Provides: perl(App::Asciio::Io)          = %{version}
Provides: perl(App::Asciio::Menues)      = %{version}
Provides: perl(App::Asciio::Options)     = %{version}
Provides: perl(App::Asciio::Setup)       = %{version}
Provides: perl(App::Asciio::Undo)        = %{version}

%{?perl_default_filter}

# Filter under-specified provides
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\((App::Asciio|App::Asciio::GTK::Asciio)\\)$

%description
This gtk2-perl application allows you to draw ASCII diagrams in a modern
(but simple) graphical application. The ASCII graphs can be saved as ASCII
or in a format that allows you to modify them later.

This package contains the back-end libraries needed to implement asciio.  For
the actual application itself, please install the 'asciio' package.

%package -n asciio
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:    Draw ascii art quickly and easily!
Requires:   %{name} = %{version}-%{release}

%description -n asciio
This application allows you to draw ASCII diagrams in a modern (but simple)
graphical application. The ASCII graphs can be saved as ASCII or in a format
that allows you to modify them later.

Think: Visio for ASCII :-)

%prep
%setup -q -n App-Asciio-%{cpan_version}

# generate our menu entry
cat << \EOF > asciio.desktop
[Desktop Entry] 
Name=Asciio
GenericName=Ascii diagrams editor
Comment=Ascii diagrams editor
Exec=%{_bindir}/asciio
#Icon= no icon currently
Terminal=false
Type=Application
Categories=Graphics;
Version=0.9.4
EOF

# fix perms
find . -type f -exec chmod -c -x {} +

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'

%{_fixperms} %{buildroot}/*

# desktop file
desktop-file-install --dir=%{buildroot}%{_datadir}/applications asciio.desktop

%check
# passes outside of rpm, but fails in rpmbuild F-10+ (no $DISPLAY)
#make test

%files
%doc README.md documentation/ 
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%files -n asciio
%doc README.md
%{_bindir}/*
%{_datadir}/applications/*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.90.02-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Aug 05 2024 Miroslav Suchý <msuchy@redhat.com> - 1.90.02-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.90.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun May 26 2024 Emmanuel Seyman <emmanuel@seyman.fr> - 1.90.02-1
- Update to 1.9.02

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.51.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.51.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.51.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.51.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.51.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.51.3-21
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.51.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.51.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.51.3-18
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.51.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.51.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.51.3-15
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.51.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.51.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.51.3-12
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.51.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.51.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.51.3-9
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.51.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.51.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.51.3-6
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.51.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.51.3-4
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.51.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 15 2015 Petr Pisar <ppisar@redhat.com> - 1.51.3-2
- Fix dependency filter

* Sun Jul 12 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 1.51.3-1
- Update to 1.51.3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02.71-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 15 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.02.71-19
- Perl 5.22 rebuild

* Thu Sep 04 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.02.71-18
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02.71-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 06 2013 Petr Pisar <ppisar@redhat.com> - 1.02.71-16
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02.71-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02.71-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02.71-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 24 2012 Petr Pisar <ppisar@redhat.com> - 1.02.71-12
- Perl 5.16 rebuild

* Sun Mar 11 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr - 1.02.71-11
- Add perl default filter
- Clean up spec file

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02.71-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.02.71-9
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02.71-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.02.71-7
- 661697 rebuild for fixing problems with vendorach/lib

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.02.71-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.02.71-5
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02.71-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02.71-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 06 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.02.71-2
- update per RHBZ#483676, comment #3

* Mon Jan 19 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.02.71-1
- update to 1.02.71

* Sat Nov 29 2008 Chris Weyl <cweyl@alumni.drew.edu> 1.01-2
- update for submission
- break out into asciio subpackage

* Sun Oct 05 2008 Chris Weyl <cweyl@alumni.drew.edu> 1.01-1
- initial RPM packaging
- generated with cpan2dist (CPANPLUS::Dist::RPM version 0.0.1)

