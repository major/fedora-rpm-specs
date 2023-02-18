%global year 2020
%global month 07

%global __provides_exclude_from ^.*libperl6_ops_moar\\.so.*$

Name:           rakudo
Version:        0.%{year}.%{month}
Release:        6%{?dist}
Summary:        Perl 6 compiler implementation that runs on MoarVM
License:        Artistic 2.0
URL:            http://rakudo.org/

Source0:        https://github.com/rakudo/rakudo/releases/download/%{year}.%{month}/rakudo-%{year}.%{month}.tar.gz
# sources for desktop files are added here
Source1:        ftp://ftp.uni-siegen.de/pub/desk/rakudo.desk.tar.gz
Source2:        macros.perl6

#Patch0:         M_LIBPATH_to_NQP_LIBPATH.patch

# general BuildRequires
BuildRequires:  perl-interpreter, make, perl-podlators, coreutils

# general perl-package BuildRequires
BuildRequires:  perl(base), perl(Cwd), perl(Exporter), perl(File::Copy)
BuildRequires:  perl(File::Spec), perl(Getopt::Long), perl(lib), perl(strict)
BuildRequires:  perl(Text::ParseWords), perl(warnings) perl(Digest::SHA)
BuildRequires:  perl(Data::Dumper), perl(IPC::Cmd)

# gcc
BuildRequires:  gcc

# general perl-test-package BuildRequires
BuildRequires:  perl(FindBin), perl(List::Util) 

BuildRequires:  perl(ExtUtils::Command)
BuildRequires:  perl(Test::Harness)


# BuildRequires for MoarVM
BuildRequires:  nqp >= 0.0.%{year}.%{month}
Requires:       nqp >= 0.0.%{year}.%{month}
BuildRequires:  moarvm-devel >= 0.%{year}.%{month}
%if 0%{?fedora}
BuildRequires:  libatomic_ops-devel
# Needed for the header files, (#include <uv.h> - libuv-devel)
BuildRequires:  libuv-devel
BuildRequires:  libtommath-devel
%endif
BuildRequires:  libffi-devel


# Needed for desktop-file-install usage
BuildRequires:  desktop-file-utils


%description
Rakudo Perl 6, or just Rakudo, is an implementation of the
Perl 6 language specification. More information about Perl 6 is available
from <http://perl6.org/>. This package provides a Perl 6 compiler built for
MoarVM virtual machine.


%prep
%setup -q -n rakudo-%{year}.%{month}


%build
%{__perl} Configure.pl --prefix=%{_prefix} --backends=moar
CFLAGS="$RPM_OPT_FLAGS" %{make_build} VERBOSE_BUILD=1


%install
export QA_SKIP_BUILD_ROOT=1
CFLAGS="$RPM_OPT_FLAGS" %make_install VERBOSE_BUILD=1

# Generating man-pages
%{__perl} -MExtUtils::Command -e mkpath $RPM_BUILD_ROOT%{_mandir}/man1
pod2man --section=1 --name=perl6 docs/running.pod | %{__gzip} -c > $RPM_BUILD_ROOT%{_mandir}/man1/perl6.1.gz
pod2man --section=1 --name=perl6-m docs/running.pod | %{__gzip} -c > $RPM_BUILD_ROOT%{_mandir}/man1/perl6-m.1.gz


# install desktop files for the URLs: docs.perl6.org and perl6intro.com
%define DESK_TARGET $RPM_BUILD_ROOT%{_datadir}/applications/
%{__mkdir} -p %{DESK_TARGET}
%{__tar} xzf %{SOURCE1}

desktop-file-install --delete-original --dir=%{DESK_TARGET} \
  perl6_doc_link.desktop intro_link.desktop usr_bin_perl6.desktop \
  2015-perl6-course-pdf.desktop intro_pdf.desktop

install icon/browser_world.png -D $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/browser_world.png
install icon/pdf_doc.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/

# install script for installing perl6 modules
sed -i -e '1 s&#!.*\(perl6\)&#!/usr/bin/rakudo&' tools/install-dist.p6
install tools/install-dist.p6 -D $RPM_BUILD_ROOT%{_datadir}/perl6/bin/mod_inst.pl

# remove zero-length files
rm -f $RPM_BUILD_ROOT/%{_libdir}/perl6/precomp/.lock
rm -f $RPM_BUILD_ROOT/%{_libdir}/perl6/repo.lock

rm -f $RPM_BUILD_ROOT/%{_bindir}/perl6*
rm -f $RPM_BUILD_ROOT/%{_bindir}/raku
rm -f $RPM_BUILD_ROOT/%{_bindir}/raku-debug

ln -s %{_bindir}/rakudo $RPM_BUILD_ROOT/%{_bindir}/perl6
ln -s %{_bindir}/rakudo-m $RPM_BUILD_ROOT/%{_bindir}/perl6-m
ln -s %{_bindir}/rakudo $RPM_BUILD_ROOT/%{_bindir}/raku
ln -s %{_bindir}/rakudo-debug $RPM_BUILD_ROOT/%{_bindir}/raku-debug

#
# perl6 RPM macros
#
mkdir -p ${RPM_BUILD_ROOT}%{_rpmconfigdir}/macros.d
install -p -m 644 %{SOURCE2} ${RPM_BUILD_ROOT}%{_rpmconfigdir}/macros.d/
sed -i -e 's/HARDCODED_VERSION/%{version}/' \
       -e 's#HC_LIBDIR#%{_datadir}#g' \
   ${RPM_BUILD_ROOT}%{_rpmconfigdir}/macros.d/macros.perl6


%check
%{?!_without_tests:
rm -f t/04-nativecall/06-struct.t
rm -f t/08-performance/99-misc.t
%ifarch ppc64le
#  rm -f t/08-performance/99-misc.t
  rm -f t/04-nativecall/01-argless.t
%endif
%ifarch s390x
  rm -f t/04-nativecall/21-callback-other-thread.t t/09-moar/Line_Break__LineBreak.t t/09-moar/General_Category__extracted-DerivedGeneralCategory.t
  rm -f t/04-nativecall/01-argless.t
%endif
%{__make} test
}


%files
%doc README.md CREDITS docs/module_management.md docs/ChangeLog
%doc from_rakudo-star/cheatsheet.txt from_rakudo-star/perl6intro.pdf
%doc from_rakudo-star/2015-spw-perl6-course.pdf
%license LICENSE

%{_bindir}/perl6
%{_bindir}/perl6-m
%{_bindir}/raku
%{_bindir}/raku-debug
%{_bindir}/rakudo*
%{_mandir}/man1/perl6.1.gz
%{_mandir}/man1/perl6-m.1.gz

# macro file
%{_rpmconfigdir}/macros.d/macros.perl6

# desktop files
%{_datadir}/applications/*.desktop

# icon files
%{_datadir}/icons/hicolor/16x16/apps/*.png

%{_datadir}/perl6


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2020.07-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 24 2022 Petr Pisar <ppisar@redhat.com> - 0.2020.07-5
- Rebuild with disabled package-notes in moarvm (bug #2070099)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2020.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2020.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2020.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 12 2020 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2020.07-1 
- update to 2020.07

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2020.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 25 2020 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2020.02-1 
- update to 2020.02

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2019.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 11 2019 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2019.11-3
- add perl6-m as link to rakudo-m

* Mon Dec 02 2019 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2019.11-2
- move the mod_inst.pl script and content to the datadir

* Sat Nov 30 2019 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2019.11-1
- update to 2019.11

* Sat Jul 13 2019 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2019.03-3
- add patch M_LIBPATH_to_NQP_LIBPATH.patch

* Sun May 19 2019 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2019.03-2
- remove the test t/04-nativecall/06-struct.t to make the build more stable
- change the source URL

* Tue Mar 19 2019 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2019.03-1
- update to 2019.03
- add 'export QA_SKIP_BUILD_ROOT=1'

* Sun Nov 11 2018 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2018.10-2
- remove the test t/08-performance/99-misc.t to make the build more stable

* Mon Oct 29 2018 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2018.10-1
- update to 2018.10
- follow the change in source from tools/install-dist.pl to tools/install-dist.p6

* Mon Apr 30 2018 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2018.04.1-1
- update to 2018.04.1
- follow the change of the source URL from upstream

* Wed Apr 25 2018 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2018.04-2
- all tests work now

* Wed Apr 25 2018 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2018.04-1
- rakudo builds again on all primary architectures
- add BuildRequires perl(Digest::SHA)
- update to 2018.04

* Mon Aug 28 2017  Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2017.08-2
- rebuild to install to _libdir again

* Tue Aug 22 2017  Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2017.08-1
- exclude architectures s390x ppc64
- update to 2017.08

* Mon Jun 19 2017  Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2017.06-2
- rebuild with changed macros.perl6 source file

* Sun Jun 18 2017  Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2017.06-1
- install file tools/install-dist.pl
- update to 2017.06

* Wed Jun 07 2017  Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2017.04.2-4
- add a rpm macro file for Perl 6

* Wed May 24 2017  Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2017.04.2-3
- build with new desktop file sources

* Mon May 08 2017  Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2017.04.2-2
- rebuild with changed moarvm build and new nqp rebuild

* Wed Mar 15 2017 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2017.04.2-1
- update to 2017.04.2
- build with patch to add libdir option

* Wed Mar 15 2017 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2017.02-1
- update to 2017.02
- initial epel7 branch upload

* Thu Mar 09 2017 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2017.01-5
- fix the rakudo-star version that is provided
- group tag removed
- remove zero-length files
- preventing to provides libperl6_ops_moar.so from non-standard path

* Tue Mar 07 2017 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2017.01-4
- install to _libdir/nqp instead of /usr/share/nqp/lib

* Wed Mar 01 2017 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2017.01-3
- install to _libdir/perl6 instead of /usr/share/perl6 

* Thu Feb 23 2017 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2017.01-2
- summary tab, description and operator in obsoletes tag is changed
- dependency on readline-devel is removed
- _prefix marcro is used
- docs/ChangeLog is packaged as documentation
- general build-requires are added

* Tue Feb 21 2017 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2017.01-1
- initial spec file for the new review
