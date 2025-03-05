Summary: A library for editing typed command lines
Name: compat-readline5
Version: 5.2
Release: %autorelease
License: GPL-2.0-or-later
URL: http://cnswww.cns.cwru.edu/php/chet/readline/rltop.html
Source: ftp://ftp.gnu.org/gnu/readline/readline-%{version}.tar.gz
Patch1: ftp://ftp.gnu.org/gnu/readline/readline-5.2-patches/readline52-001
Patch2: ftp://ftp.gnu.org/gnu/readline/readline-5.2-patches/readline52-002
Patch3: ftp://ftp.gnu.org/gnu/readline/readline-5.2-patches/readline52-003
Patch4: ftp://ftp.gnu.org/gnu/readline/readline-5.2-patches/readline52-004
Patch5: ftp://ftp.gnu.org/gnu/readline/readline-5.2-patches/readline52-005
Patch6: ftp://ftp.gnu.org/gnu/readline/readline-5.2-patches/readline52-006
Patch7: ftp://ftp.gnu.org/gnu/readline/readline-5.2-patches/readline52-007
Patch8: ftp://ftp.gnu.org/gnu/readline/readline-5.2-patches/readline52-008
Patch9: ftp://ftp.gnu.org/gnu/readline/readline-5.2-patches/readline52-009
Patch10: ftp://ftp.gnu.org/gnu/readline/readline-5.2-patches/readline52-010
Patch11: ftp://ftp.gnu.org/gnu/readline/readline-5.2-patches/readline52-011
Patch12: ftp://ftp.gnu.org/gnu/readline/readline-5.2-patches/readline52-013
Patch13: ftp://ftp.gnu.org/gnu/readline/readline-5.2-patches/readline52-014
# fix file permissions, remove RPATH, use CFLAGS
Patch20: readline-5.2-shlib.patch
# fixed in readline-6.0
Patch21: readline-5.2-redisplay-sigint.patch
Patch22: readline-5.2-config.patch
Patch23: compat-readline5-wcwidth.patch
Patch24: compat-readline5-configure-c99.patch
Patch25: readline-5.2-gcc15.patch
BuildRequires: gcc ncurses-devel
BuildRequires: make

%description
The Readline library provides a set of functions that allow users to
edit command lines. Both Emacs and vi editing modes are available. The
Readline library includes additional functions for maintaining a list
of previously-entered command lines for recalling or editing those
lines, and for performing csh-like history expansion on previous
commands.

%package devel
Summary: Files needed to develop programs which use the readline library
Requires: %{name} = %{version}-%{release}
Requires: ncurses-devel

%description devel
The Readline library provides a set of functions that allow users to
edit typed command lines. If you want to develop programs that will
use the readline library, you need to have the readline-devel package
installed. You also need to have the readline package installed.

%package static
Summary: Static libraries for the readline library
Requires: %{name}-devel = %{version}-%{release}

%description static
The readline-static package contains the static version of the readline
library.

%prep
%setup -q -n readline-%{version}
%patch -P1 -p0 -b .001
%patch -P2 -p0 -b .002
%patch -P3 -p0 -b .003
%patch -P4 -p0 -b .004
%patch -P5 -p0 -b .005
%patch -P6 -p0 -b .006
%patch -P7 -p0 -b .007
%patch -P8 -p0 -b .008
%patch -P9 -p0 -b .009
%patch -P10 -p0 -b .010
%patch -P11 -p0 -b .011
%patch -P12 -p0 -b .013
%patch -P13 -p0 -b .014
%patch -P20 -p1 -b .shlib
%patch -P21 -p1 -b .redisplay-sigint
%patch -P22 -p1
%patch -P23 -p1
%patch -P24 -p1
%patch -P25 -p1

%build
export CPPFLAGS="-I%{_includedir}/ncurses"
%configure
%make_build

%install
%make_install

mkdir -p $RPM_BUILD_ROOT{/%{_lib},%{_libdir}/readline5}
mv $RPM_BUILD_ROOT%{_libdir}/libreadline.so.* $RPM_BUILD_ROOT/%{_lib}
mv $RPM_BUILD_ROOT%{_libdir}/lib*.a $RPM_BUILD_ROOT%{_libdir}/readline5

rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.so
ln -sf ../../../%{_lib}/libreadline.so.5 $RPM_BUILD_ROOT%{_libdir}/readline5/libreadline.so
ln -sf ../libhistory.so.5 $RPM_BUILD_ROOT%{_libdir}/readline5/libhistory.so

mkdir $RPM_BUILD_ROOT%{_includedir}/readline5
mv $RPM_BUILD_ROOT%{_includedir}/readline{,5}

rm -rf $RPM_BUILD_ROOT%{_infodir}
rm -rf $RPM_BUILD_ROOT%{_mandir}

%ldconfig_scriptlets

%files
%doc CHANGES COPYING NEWS README USAGE
/%{_lib}/libreadline*.so.*
%{_libdir}/libhistory*.so.*

%files devel
%{_includedir}/readline5
%dir %{_libdir}/readline5
%{_libdir}/readline5/lib*.so

%files static
%{_libdir}/readline5/lib*.a

%changelog
%autochangelog
