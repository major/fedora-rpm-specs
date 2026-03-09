Name:           perl-Curses
Version:        1.46
Release:        %autorelease
Summary:        Perl bindings for ncurses

# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Curses
Source0:        https://cpan.metacpan.org/authors/id/G/GI/GIRAFFED/Curses-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  sed

%description
Perl bindings for ncurses, bringing terminal-independent character
handling capabilities to Perl.


%prep
%autosetup -p1 -n Curses-%{version}
test -f hints/c-linux.ncursesw.h || cp hints/c-linux.ncurses.h hints/c-linux.ncursesw.h
sed -i -e 's|/usr/local/bin/perl|%{__perl}|' demo*
sed -i -e 's|/usr//bin/perl|%{__perl}|' demo*

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" \
   PANELS MENUS FORMS
make %{?_smp_mflags}

# A note about the following alarming output...
#
#  WARNING: Your Curses form.h file appears to be in the default
#  system search path, which will not work for us because of
#  the conflicting Perl form.h file.  This means your 'make' will
#  probably fail unless you fix this, as described in the INSTALL
#  file.
#
#... can be ignored because /usr/include/form.h is a symlink to
#/usr/include/ncurses/form.h, which the Makefile.PL finds and
#uses quite happily.


%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

#Remove exec perm for file aimed to be bundled as %%doc
chmod -x demo*

%check
make test



%files
%doc Copying Artistic README demo*
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Curses.pm
%{_mandir}/man3/*.3*


%changelog
%autochangelog
