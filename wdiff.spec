%bcond rebuild_mans 1

Name:           wdiff
Version:        1.2.2
Release:        %autorelease
Summary:        Compare files on a word per word basis

# Entire source is GPL-3.0-or-later, except wdiff.texi and the documentation
# built from it, including info, HTML, and PDF documentation, which is Latex2e.
License:        GPL-3.0-or-later AND Latex2e
URL:            https://www.gnu.org/software/wdiff/
Source0:        https://ftp.gnu.org/gnu/wdiff/wdiff-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/wdiff/wdiff-%{version}.tar.gz.sig
Source2:        https://ftp.gnu.org/gnu/gnu-keyring.gpg

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool  

BuildRequires:  gettext-devel
BuildRequires:  ncurses-devel

BuildRequires:  help2man
BuildRequires:  texinfo  
BuildRequires:  texinfo-tex
BuildRequires:  tex(latex)

BuildRequires:  gnupg2

#https://fedorahosted.org/fpc/ticket/174
Provides: bundled(gnulib) = 30.5.2012

%description
The GNU wdiff program is a front end to diff for comparing files on a word per
word basis. A word is anything between whitespace. This is useful for comparing
two texts in which a few words have been changed and for which paragraphs have
been refilled. It works by creating two temporary files, one word per line, and
then executes diff on these files. It collects the diff output and uses it to
produce a nicer display of word differences between the original files.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q

# Fix ISO-8859-1-encoded files
for fn in BACKLOG ChangeLog
do
  iconv --from=ISO-8859-1 --to=UTF-8 "${fn}" > "${fn}.iconv"
  touch -r "${fn}" "${fn}.iconv"
  chmod -v --reference="${fn}" "${fn}.iconv"
  mv -f "${fn}.iconv" "${fn}"
done


%build
autoreconf -fiv
%configure --enable-experimental="mdiff wdiff2 unify" 
%make_build all

%if %{with rebuild_mans}
rm -v man/mdiff.1 man/wdiff.1 man/wdiff2.1 man/unify.1
%make_build -C man mdiff.1 wdiff.1 wdiff2.1 unify.1
%endif

# Make sure we rebuild the info page too.
rm -v doc/wdiff.info
%make_build -C doc info html pdf


%install
%make_install
find '%{buildroot}' -type f -name '*gnulib.mo' -print -delete
rm '%{buildroot}%{_infodir}/dir'
install -d '%{buildroot}%{_pkgdocdir}'
install -t '%{buildroot}%{_pkgdocdir}' -p -m 0644 \
    ABOUT-NLS \
    AUTHORS \
    BACKLOG \
    ChangeLog \
    NEWS \
    README \
    THANKS \
    TODO
cp -rp doc/wdiff.html %{buildroot}%{_pkgdocdir}/html

%find_lang wdiff


%check
%make_build check


%files -f wdiff.lang
%license COPYING

%{_bindir}/mdiff
%{_bindir}/wdiff
%{_bindir}/wdiff2
%{_bindir}/unify

%{_mandir}/man1/mdiff.1*
%{_mandir}/man1/wdiff.1*
%{_mandir}/man1/wdiff2.1*
%{_mandir}/man1/unify.1*

%{_infodir}/wdiff.info.*

%{_pkgdocdir}/


%changelog
%autochangelog
