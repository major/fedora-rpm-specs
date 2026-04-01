Name:           pspp
Version:        2.1.1
Release:        %autorelease
Summary:        A program for statistical analysis of sampled data
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/pspp/
VCS:            git://git.savannah.gnu.org/pspp.git
Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz.sig
# https://cgit.git.savannah.gnu.org/cgit/pspp.git/plain/Smake?h=58e4c1b576fe9293c053924446e6c89efd34c53a
Source2:        pspp-Smake
Source3:        C2D1AB061656AAC54B5E975485199DE8C6648E90.gpg
# Follow up to CVE-2022-39831
Patch:		pspp-0001-Don-t-install-man-page-for-non-existent-app.patch
# Will be proposed upstream
Patch:		pspp-0002-Revert-update-gnulib-version-to-latest-from-stable-2.patch
Patch:		pspp-0003-MATRIX-Use-int64_t-instead-of-long-for-sequence-rang.patch
Patch:		pspp-0004-Revert-MATRIX-Skip-test-for-too-large-matrices-on-32.patch
Patch:		pspp-0005-Revert-tests-skip-test-MATRIX-very-large-matrices-on.patch
Patch:		pspp-0006-Reapply-update-gnulib-version-to-latest-from-stable-.patch
Patch:          pspp-0007-pspp-convert-Fix-integer-overflow-in-password-length.patch
Patch:          pspp-0008-pspp-convert-Fix-uninitialized-pointer-use-in-parse_.patch
Patch:          pspp-0009-zip-reader-Fix-heap-buffer-overflow-in-inflate_read-.patch
# FIXME: pspp-0010 fixes a real missing-braces bug in spvxml_parse_attributes()
# (CVE-2025-47816) where 'return' was unconditionally executed after checking
# only the first attribute, effectively short-circuiting all subsequent checks.
# The fix is correct, but it exposes a latent issue in the bundled tutorial
# .spv files shipped with pspp-2.1.1: under full attribute validation, some of
# those files fail parsing mid-render, causing 'error while writing to output
# stream' from Cairo and missing doc/pspp-figures/tutorial*.png at install time.
# The .spv files need to be regenerated upstream with the fix in place.
#Patch:          pspp-0010-spvxml-helpers-Fix-missing-brace-bug-causing-OOB-rea.patch
Patch:          pspp-0011-variable-Fix-assertion-failure-in-var_set_leave_quie.patch
Patch:          pspp-0012-encrypted-file-Fix-heap-buffer-over-read-in-fill_buf.patch
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
BuildRequires:  texlive-tex
BuildRequires:  texlive-wasy
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
make -f Smake GNULIB=/usr/share/gnulib/lib GNULIB_TOOL=/usr/bin/gnulib-tool

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
make check


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
