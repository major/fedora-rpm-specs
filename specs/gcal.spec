%global gcalmantag 4

Name:		gcal
Version:	4.1
Release:	%autorelease
Summary:	GNU Gregorian calendar program

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		https://www.gnu.org/software/gcal/
Source0:	https://ftp.gnu.org/gnu/gcal/%{name}-%{version}.tar.xz
# The man pages are not shipped in tarball but reside in the git repository
# at https://git.savannah.gnu.org/git/gcal.git
# To fetch the man pages from a clone of that repository, do:
# $ gcalmantag=4  # n.b. there is no 4.1 tag
# $ git archive --format=tar v${gcalmantag} -- doc/en/man | \
#     xz > gcal-man-v${gcalmantag}.tar.xz
Source1:	gcal-man-v%{gcalmantag}.tar.xz
Patch:		gcal-glibc-no-libio.patch
Patch:		gcal-configure-c99.patch
Patch:		gcal-4.1-oob-write.patch
Patch:		gcal-configure-tget.patch
BuildRequires:	gcc
BuildRequires:	gettext-devel
BuildRequires:	ncurses-devel
BuildRequires:	libunistring-devel
BuildRequires:	make
BuildRequires:	autoconf automake

# Gnulib is granted exception of "no bundled libraries" packaging guideline:
# https://fedoraproject.org/wiki/Packaging:No_Bundled_Libraries#Packages_granted_exceptions
Provides: bundled(gnulib)

%description
Gcal is a program for calculating and printing calendars.  Gcal
displays hybrid and proleptic Julian and Gregorian calendar sheets.
It also displays holiday lists for many countries around the globe.

%prep
%autosetup -p1
tar xf %{SOURCE1}


%build
autoreconf -ifv
export LIBS=-lunistring
%if 0%{?fedora} > 41 || 0%{?rhel} > 10
# Initialization of 'void (*)(void)' from incompatible pointer type
export CFLAGS="$CFLAGS -std=gnu17"
%endif
%configure --enable-unicode
%make_build


%check
make check


%install
%make_install
install -dm 755 %{buildroot}%{_mandir}/man1
install -pm 644 doc/en/man/*.1 %{buildroot}%{_mandir}/man1
rm -f %{buildroot}%{_datadir}/%{name}/Makefile.in
rm -f %{buildroot}%{_infodir}/dir
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS BUGS LIMITATIONS NEWS README THANKS
%{_bindir}/gcal
%{_bindir}/gcal2txt
%{_bindir}/tcal
%{_bindir}/txt2gcal
%{_datadir}/gcal/
%{_infodir}/*.info*
%{_mandir}/man1/*.1*

%changelog
%autochangelog
