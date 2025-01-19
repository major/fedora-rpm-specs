Name:           perl-Gnome2
Version:        1.048
Release:        16%{?dist}
Summary:        Perl interface to the 2.x series of the GNOME libraries (deprecated)
# Gnome2.pm:    LGPL-2.1-or-later
# gnome2perl.h: LGPL-2.1-or-later
# LICENSE:      LGPL-2.1 text
# xs/Gnome2.xs: LGPL-2.1-or-later
# xs/GnomeAbout.xs: LGPL-2.1-or-later
# xs/GnomeApp.xs:   LGPL-2.1-or-later
# xs/GnomeAppBar.xs:    LGPL-2.1-or-later
# xs/GnomeAppHelper.xs: LGPL-2.1-or-later
# xs/BonoboDock.xs:     LGPL-2.1-or-later
# xs/BonoboDockItem.xs: LGPL-2.1-or-later
# xs/GnomeClient.xs:    LGPL-2.1-or-later
# xs/GnomeColorPicker.xs:   LGPL-2.1-or-later
# xs/GnomeConfig.xs:    LGPL-2.1-or-later
# xs/GnomeDateEdit.xs:  LGPL-2.1-or-later
# xs/GnomeDruid.xs:     LGPL-2.1-or-later
# xs/GnomeDruidPage.xs: LGPL-2.1-or-later
# xs/GnomeDruidPageEdge.xs: LGPL-2.1-or-later
# xs/GnomeDruidPageStandard.xs: LGPL-2.1-or-later
# xs/GnomeEntry.xs: LGPL-2.1-or-later
# xs/GnomeFileEntry.xs: LGPL-2.1-or-later
# xs/GnomeFontPicker.xs:    LGPL-2.1-or-later
# xs/GnomeGConf.xs: LGPL-2.1-or-later
# xs/GnomeHelp.xs:  LGPL-2.1-or-later
# xs/GnomeHRef.xs:  LGPL-2.1-or-later
# xs/GnomeIconEntry.xs: LGPL-2.1-or-later
# xs/GnomeIconList.xs:  LGPL-2.1-or-later
# xs/GnomeIconLookup.xs:    LGPL-2.1-or-later
# xs/GnomeIconSelection.xs: LGPL-2.1-or-later
# xs/GnomeIconTextItem.xs:  LGPL-2.1-or-later
# xs/GnomeIconTheme.xs: LGPL-2.1-or-later
# xs/GnomeInit.xs:  LGPL-2.1-or-later
# xs/GnomeI18N.xs:  LGPL-2.1-or-later
# xs/GnomeModuleInfo.xs:    LGPL-2.1-or-later
# xs/GnomePasswordDialog.xs:    LGPL-2.1-or-later
# xs/GnomePixmapEntry.xs:   LGPL-2.1-or-later
# xs/GnomePopupMenu.xs:     LGPL-2.1-or-later
# xs/GnomeProgram.xs:       LGPL-2.1-or-later
# xs/GnomeScore.xs: LGPL-2.1-or-later
# xs/GnomeScores.xs:    LGPL-2.1-or-later
# xs/GnomeSound.xs: LGPL-2.1-or-later
# xs/GnomeThumbnail.xs: LGPL-2.1-or-later
# xs/GnomeUIDefs.xs:    LGPL-2.1-or-later
# xs/GnomeURL.xs:   LGPL-2.1-or-later
# xs/GnomeUtil.xs:  LGPL-2.1-or-later
# xs/GnomeWindowIcon.xs:    LGPL-2.1-or-later
# xs/GnomeWindow.xs:    LGPL-2.1-or-later
## Not in any binary package
# Makefile.PL:  LGPL-2.1-or-later
License:        LGPL-2.1-or-later
URL:            https://metacpan.org/release/Gnome2
Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAOC/Gnome2-%{version}.tar.gz
# Adapt to Perl 5.40.0, bug #2292164, CPAN RT#153977
Patch0:         Gnome2-1.048-Adapt-to-perl-5.40.0.patch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libgnomeui-devel
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::Depends) >= 0.20
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::PkgConfig) >= 1.03
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Glib::GenPod)
BuildRequires:  perl(Glib::MakeHelper)
# Gnome2::Canvas is maybe run-time hard checked at build-time
BuildRequires:  perl(Gnome2::Canvas) >= 1.00
# Gnome2::VFS is maybe run-time hard checked at build-time
BuildRequires:  perl(Gnome2::VFS) >= 1.00
# Gtk2 is maybe run-time hard checked at build-time
BuildRequires:  perl(Gtk2) >= 1.00
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(DynaLoader)
# Tests:
BuildRequires:  perl(constant)
# Data::Dumper not used
BuildRequires:  perl(Glib) >= 1.04
BuildRequires:  perl(Test::More)
Requires:       perl(Gnome2::Canvas) >= 1.00
Requires:       perl(Gnome2::VFS) >= 1.00
Requires:       perl(Gtk2) >= 1.00

%{?perl_default_filter}

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Gnome2::Canvas|Gnome2::VFS|Glib|Gtk2)\\)$

%description
The Gnome2 module allows a Perl developer to use the GNOME libraries.  Find out
more about GNOME+ at <https://www.gnome.org/>.

This package is deprecated. Users are advised to uninstall it.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Glib) >= 1.04

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n Gnome2-%{version}
chmod a+x t/*.t t/GnomeClient t/GnomeHelp t/GnomeScore t/GnomeSound t/GnomeURL

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc AUTHORS ChangeLog.pre-git examples maps NEWS README TODO
%{perl_vendorarch}/auto/Gnome2
%{perl_vendorarch}/Gnome2
%{perl_vendorarch}/Gnome2.pm
%{_mandir}/man3/Gnome2.*
%{_mandir}/man3/Gnome2::*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.048-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.048-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jun 13 2024 Petr Pisar <ppisar@redhat.com> - 1.048-14
- Adapt to Perl 5.40.0 (bug #2292164)
- Covert a license tag to SPDX
- Package the tests

* Tue Jun 11 2024 Jitka Plesnikova <jplesnik@redhat.com> - 1.048-13
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.048-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.048-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.048-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.048-9
- Perl 5.38 rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.048-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.048-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.048-6
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.048-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.048-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.048-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.048-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 06 2021 Petr Pisar <ppisar@redhat.com> - 1.048-1
- 1.048 bump
- License tag corrected to "LGPLv2+"

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.047-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.047-10
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.047-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.047-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.047-7
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.047-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.047-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.047-4
- Perl 5.28 rebuild

* Tue Mar 06 2018 Petr Pisar <ppisar@redhat.com> - 1.047-3
- Build-require gcc

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.047-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 09 2017 Petr Pisar <ppisar@redhat.com> - 1.047-1
- 1.047 bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.046-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.046-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.046-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.046-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.046-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.046-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 23 2015 Petr Pisar <ppisar@redhat.com> - 1.046-1
- 1.046 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.045-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.045-5
- Perl 5.22 rebuild

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.045-4
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.045-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.045-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Dec 10 2013 Petr Pisar <ppisar@redhat.com> - 1.045-1
- 1.045 bump

* Mon Oct 21 2013 Petr Pisar <ppisar@redhat.com> - 1.044-1
- 1.044 bump

* Wed Oct 02 2013 Petr Pisar <ppisar@redhat.com> - 1.043-1
- 1.043 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.042-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Petr Pisar <ppisar@redhat.com> - 1.042-15
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.042-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.042-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Petr Pisar <ppisar@redhat.com> - 1.042-12
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.042-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 09 2011 Iain Arnell <iarnell@gmail.com> 1.042-10
- Rebuild for libpng 1.5
- BuildRequires perl(Test::More)

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.042-9
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.042-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.042-7
- 661697 rebuild for fixing problems with vendorach/lib

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.042-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.042-5
- rebuild against perl 5.10.1

* Thu Jul 30 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.042-4
- Fix mass rebuild breakdown: Add BR: perl(Glib::MakeHelper).

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.042-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.042-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 19 2009 Allisson Azevedo <allisson@gmail.com> 1.042-1
- Initial rpm release.
