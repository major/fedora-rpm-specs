Name:           pspp
Version:        2.0.1
Release:        %autorelease
Summary:        A program for statistical analysis of sampled data
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/pspp/
VCS:            git://git.savannah.gnu.org/pspp.git
Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz.sig
Source2:        pspp-Smake
Source3:        C2D1AB061656AAC54B5E975485199DE8C6648E90.gpg
# Follow up to CVE-2022-39831
Patch1:		pspp-0001-Don-t-install-man-page-for-non-existent-app.patch
# FIXME retest on F-40+
Patch2:		pspp-0002-FIXME-disable-tests-failing-on-F-40.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cairo-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  gnulib-devel
BuildRequires:  gnupg2
BuildRequires:  gsl-devel >= 1.11-2
BuildRequires:  gtk3-devel
BuildRequires:  gtksourceview4-devel
BuildRequires:  libpq-devel
BuildRequires:  librsvg2-tools
BuildRequires:  libtool
BuildRequires:  libxml2
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  pango-devel
BuildRequires:  perl(Config::Perl::V)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Diff)
BuildRequires:  perl-devel
BuildRequires:  plotutils-devel
BuildRequires:  python3
BuildRequires:  readline-devel
BuildRequires:  spread-sheet-widget-devel
BuildRequires:  texinfo
# FIXME not sure what's going on there. It passes TeX-tests perfectly fine on my machine.
#BuildRequires:  texlive-tex
#BuildRequires:  texlive-wasy
Requires:	hicolor-icon-theme


%description
PSPP is a program for statistical analysis of sampled data. It
interprets commands in the SPSS language and produces tabular
output in ASCII, PostScript, or HTML format.

PSPP development is ongoing. It already supports a large subset
of SPSS's transformation language. Its statistical procedure
support is currently limited, but growing.


%prep
%{gpgverify} --keyring='%{SOURCE3}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
# Remove bundled Gnulib and prepare to import system-wide one
rm -rf gl/
rm -f aclocal.m4
install -D -p -m 0644 %{SOURCE2} Smake


%build
# Import and build system-wide Gnulib
make -f Smake GNULIB=%{_datadir}/gnulib/lib GNULIB_TOOL=%{_bindir}/gnulib-tool

autoreconf -ifv
%configure CFLAGS="${CFLAGS:-%optflags} -fgnu89-inline" \
    --disable-static --disable-rpath
%make_build


%install
%make_install
# Install docs
mkdir -p %{buildroot}%{_pkgdocdir}
cp -p AUTHORS NEWS ONEWS README THANKS %{buildroot}%{_pkgdocdir}
# don't own /usr/share/info/dir
rm %{buildroot}%{_infodir}/dir

# don't lala
find %{buildroot}%{_libdir}/ \
   -name \*.la -delete

# desktop file
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnu.pspp.desktop

# localization
%find_lang %{name}

# clean up some stuff
rm -f %{buildroot}%{_datadir}/icons/hicolor/icon-theme.cache


%check
echo $LC_NUMERIC
LC_NUMERIC=C make check


%files -f %{name}.lang
%license COPYING
%{_bindir}/pspp
%{_bindir}/pspp-convert
%{_bindir}/pspp-output
%{_bindir}/psppire
%{_datadir}/applications/org.gnu.%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/org.gnu.%{name}.png
%{_datadir}/icons/hicolor/*/mimetypes/*.png
%{_datadir}/icons/hicolor/scalable/apps/org.gnu.%{name}.svg
%{_datadir}/metainfo/org.gnu.%{name}.metainfo.xml
%{_datadir}/mime/packages/org.gnu.%{name}.xml
%{_datadir}/pspp/
%{_infodir}/pspp*
%{_infodir}/screenshots/*-ad.png.gz
%{_libdir}/%{name}/
%{_mandir}/man1/pspp-convert.1.*
%{_mandir}/man1/pspp-output.1.*
%{_mandir}/man1/pspp.1.*
%{_mandir}/man1/psppire.1.*
%{_pkgdocdir}/


%changelog
%autochangelog
