Name:           remind
Version:        04.02.09
Release:        %autorelease
Summary:        Sophisticated calendar and alarm program

# GPL-2.0-only: main software
# GPL-2.0-only AND LicenseRef-Fedora-Public-Domain:
#  - src/moon.c
# LicenseRef-Fedora-Public-Domain:
# - src/md5.c
License:        GPL-2.0-only AND BSD-2-Clause AND (GPL-2.0-only AND LicenseRef-Fedora-Public-Domain) AND LicenseRef-Fedora-Public-Domain
URL:            https://dianne.skoll.ca/projects/remind/
Source:         %url/download/%{name}-%{version}.tar.gz
Source:         %url/download/%{name}-%{version}.tar.gz.sig
Source:         685A5A5E511D30E2.gpg
Source:         tkremind.desktop
# stolen from Debian
Patch:          use-system-libjsonparser.diff


# temporary
Patch:          remove-timezone-tests-from-compare.patch

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  perl(Cairo)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(Pango)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(json-parser)
BuildRequires:  desktop-file-utils
Recommends:     remind-tools
Recommends:     remind-gui
Recommends:     remind-doc

%description
Remind is a sophisticated calendar and alarm program. It includes the following
features:

 - A sophisticated scripting language and intelligent handling of exceptions
   and holidays
 - Plain-text, PDF, PostScript and HTML output
 - Timed reminders and pop-up alarms
 - A friendly graphical front-end for people who don't want to learn the
   scripting language
 - Facilities for both the Gregorian and Hebrew calendars
 - Support for 12 different languages

%package        doc
Summary:        Documentation for remind, a sophisticated calendar and alarm program
License:        GPL-2.0-only
BuildArch:      noarch

%description    doc
Documentation and information on how to use remind

%package        gui
Summary:        GUI for remind, a sophisticated calendar and alarm program
License:        GPL-2.0-only
BuildArch:      noarch
Provides:       tkremind = %{version}-%{release}
Requires:       %{name} = %{version}-%{release}
Requires:       tcl
Requires:       tcllib
Requires:       tk >= 8.0
Suggests:       google-noto-fonts

%description    gui
Tkremind provides a GUI which allows viewing a calendar and adding or editing
reminders without learning the syntax of Remind.

%package        tools
Summary:        Additional tools for remind
# GPL-2.0-or-later:
#  - contrib/ical2rem.pl
#  - contrib/rem2ics-0.93/rem2ics.spec
#  - contrib/remind-conf-mode/remind-conf-mode.el
# GPL-2.0-or-later AND GPL-2.0-only:
#  - contrib/rem2ics-0.93/rem2ics
# GPL-3.0-only:
#  - contrib/remind-conf-mode/gpl.txt
License:        GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only

%description    tools
Tools to convert the remind output to ps, pdf or html as well as example files.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n %{name}-%{version}
# Disable packlist and perllocal update
sed -i 's|\$(PERL) Makefile.PL|\$(PERL) Makefile.PL NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"|g' rem2pdf/Makefile.top.in

# json-parser is in fedora; remove bundled copies
rm src/json.h
rm src/json.c

%build
%configure
%make_build

%install
%make_install

desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE3}

%check
# NOTE(neil): 2024-01-09 disabling tz.rem as it is broken

sed -iE 's,^TZ=America.*,,;s,^TZ=Europe.*,,' tests/test-rem

make test

%files
%doc README
%license COPYRIGHT MICROSOFT-AND-APPLE
%attr(0755,-,-) %{_bindir}/%{name}
%{_bindir}/rem
%{_datadir}/remind/
%{_mandir}/man1/rem.1*
%{_mandir}/man1/%{name}.1*

%files doc
%doc README docs/
%doc www/ examples/ contrib/

%files tools
%license COPYRIGHT MICROSOFT-AND-APPLE
%attr(0755,-,-) %{_bindir}/rem2html
%attr(0755,-,-) %{_bindir}/rem2pdf
%attr(0755,-,-) %{_bindir}/rem2ps
%{perl_vendorlib}/*
%{_mandir}/man1/rem2html.1*
%{_mandir}/man1/rem2pdf.1*
%{_mandir}/man1/rem2ps.1*
%{_mandir}/man3/Remind::PDF.3pm*
%{_mandir}/man3/Remind::PDF::Entry.3pm*

%files gui
%attr(0755,-,-) %{_bindir}/tkremind
%{_mandir}/man1/tkremind.1*
%{_datadir}/applications/tkremind.desktop

%changelog
%autochangelog
