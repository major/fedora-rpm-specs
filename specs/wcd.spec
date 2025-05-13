Summary:        Wherever Change Directory: chdir for DOS and Unix
Name:           wcd
Version:        6.0.5
Release:        %autorelease

License:        GPL-2.0-or-later
URL:            https://waterlan.home.xs4all.nl/wcd.html
Source:         https://waterlan.home.xs4all.nl/wcd/wcd-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc

# For NLS (translations) in the program
BuildRequires:  gettext
# For rebuilding and translating documentation
BuildRequires:  po4a
BuildRequires:  /usr/bin/pod2html
BuildRequires:  /usr/bin/pod2man
BuildRequires:  /usr/bin/podchecker

BuildRequires:  ncurses-devel
BuildRequires:  libunistring-devel

%global wcd_d1 prefix='%{_prefix}' bindir='%{_bindir}' datadir='%{_datadir}'
%global wcd_d2 docdir='%{_pkgdocdir}' sysconfdir='%{_sysconfdir}'
%global wcd_d3 mandir='%{_mandir}'
%global wcd_dirs %{wcd_d1} %{wcd_d2} %{wcd_d3}
# Paraphrased from doc/UNIX.txt:
#   UCS= Enable Unicode (UTF8) support.
#   UNINORM= Enable Unicode normalization. Requires libunistring. This takes at
#            least partial effect by being defined *to any value*, so do not
#            define it unless we want to enable it (we do).
#   ENABLE_NLS= Enable native language support. That is, use locale files. This
#               option takes effect by being defined *to any value*, so do not
#               define it unless we want to enable it (we do).
#   STATIC= Enable static linking. Make a standalone wcd binary. This option
#           takes effect by being defined *to any value*, so do not define it
#           unless we want to enable it.
#   DEBUG= Add -g to CFLAGS; the distro flags handle this.
#   DEBUGMSG= Makes wcd print verbose messages about accessing the file system.
#   LFS= Large File Support (LFS). This option cannot be effectively disabled
#        due to questionable logic in the Makefile, but that is fine because we
#        certainly want it to be enabled.
#   CURSES= Select curses library. Default is ncurses. There is some magic
#           behind the scenes, so we leave this alone.
#   NCURSES_DEBUG= Link with ncurses debug enabled library.
#   ASCII_TREE= Draw graphical tree with ASCII characters (instead of
#               line-drawing characters). This option takes effect by being
#               defined *to any value*, so do not define it unless we want to
#               enable it.
#   EXT= Set executable extension.
#   HMTLEXT= Set HTML manual file extension.
%global wcd_f1 UCS=1 UNINORM=1 ENABLE_NLS=1
%global wcd_f2 DEBUG=0 DEBUGMSG=0 LFS=1 NCURSES_DEBUG=0
%global wcd_f3 EXT= HTMLEXT=html
%global wcd_flags %{wcd_f1} %{wcd_f2} %{wcd_f3}
%global wcd_opts %{wcd_dirs} %{wcd_flags}

%description
Wcd is a command-line program to change directory fast. It saves time typing at
the keyboard. One needs to type only a part of a directory name and wcd will
jump to it. Wcd has a fast selection method in case of multiple matches and
allows aliasing and banning of directories. Wcd also includes a full screen
interactive directory tree browser with speed search.

Wcd was modeled after Norton Change Directory (NCD). NCD appeared first in The
Norton Utilities, Release 4, for DOS in 1987, published by Peter Norton. NCD
was written by Brad Kingsbury.


%package doc
Summary:        Documentation for wcd

BuildArch:      noarch

%description doc
%{summary}.

Man pages are included with the base package. This package provides the same
documentation in other forms, like plain text and HTML, as well as ancillary
plain-text documentation files, changelogs, and so on.


%prep
%autosetup


%build
%make_build -C src %{wcd_opts}


%install
%make_install install-profile -C src %{wcd_opts}
%find_lang wcd --with-man


# Upstream does not provide any tests


%files -f wcd.lang
%license %{_pkgdocdir}/copying.txt

%{_bindir}/wcd
%{_mandir}/man1/wcd.1*

%config(noreplace) %{_sysconfdir}/profile.d/wcd.sh
%config(noreplace) %{_sysconfdir}/profile.d/wcd.csh


%files doc
%license %{_pkgdocdir}/copying.txt
%doc %{_pkgdocdir}/INSTALL.txt
%doc %{_pkgdocdir}/README.txt
%doc %{_pkgdocdir}/UNIX.txt
%doc %{_pkgdocdir}/faq.txt
%doc %{_pkgdocdir}/problems.txt
%doc %{_pkgdocdir}/todo.txt
%doc %{_pkgdocdir}/wcd.html
%doc %{_pkgdocdir}/wcd.txt
%doc %{_pkgdocdir}/whatsnew.txt
# Localized HTML and plain-text documentation
%doc %dir %{_pkgdocdir}/*/
%doc %{_pkgdocdir}/*/wcd.html
%doc %{_pkgdocdir}/*/wcd.txt


%changelog
%autochangelog
