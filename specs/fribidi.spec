Summary: Library implementing the Unicode Bidirectional Algorithm
Name: fribidi
Version: 1.0.17
Release: %autorelease
URL: https://github.com/fribidi/fribidi/
Source: https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
License: LGPL-2.1-or-later AND Unicode-DFS-2016
BuildRequires: gcc
%if 0%{?rhel} && 0%{?rhel} <= 8
BuildRequires: automake autoconf libtool
%else
BuildRequires: meson
%endif
BuildRequires: make
Patch0: fribidi-drop-bundled-gnulib.patch

%description
A library to handle bidirectional scripts (for example Hebrew, Arabic),
so that the display is done in the proper way; while the text data itself
is always written in logical order.

%package devel
Summary: Libraries and include files for FriBidi
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Include files and libraries needed for developing applications which use
FriBidi.

%prep
%autosetup -p1
%if 0%{?rhel} && 0%{?rhel} <= 8
autoreconf -i
%endif
# Clean up older file in archive
(cd lib;
 rm arabic-shaping.tab.i bidi-type.tab.i brackets*.tab.i joining-type.tab.i mirroring.tab.i fribidi-unicode-version.h
)

%build
%if 0%{?rhel} && 0%{?rhel} <= 8
%if 0%{?el5}
# FORTIFY_SOURCE=2 breaks EL-5 build
export CFLAGS=`echo $RPM_OPT_FLAGS | sed -e 's|FORTIFY_SOURCE=2|FORTIFY_SOURCE=1|'`
%ifarch ppc ppc64 x86_64
export CFLAGS="$CFLAGS -DPAGE_SIZE=4096"
%endif
%else
# outside of EL-5, only ppc* needs modification
%ifarch ppc ppc64
export CFLAGS="$RPM_OPT_FLAGS -DPAGE_SIZE=4096"
%endif
%endif
%configure --disable-static --disable-docs
make %{?_smp_mflags} V=1
%else
%meson -Ddocs=false
%meson_build
%endif

%check
%if 0%{?rhel} && 0%{?rhel} <= 8
make check
%else
%meson_test
%endif

%install
%if 0%{?rhel} && 0%{?rhel} <= 8
make DESTDIR=$RPM_BUILD_ROOT install INSTALL="install -p"
%else
%meson_install
%endif
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_scriptlets

%files
%doc README AUTHORS ChangeLog THANKS NEWS TODO
%license COPYING
%{_bindir}/fribidi
%{_libdir}/libfribidi.so.0*
%{_mandir}/man1/fribidi.1*

%files devel
%{_includedir}/fribidi
%{_libdir}/libfribidi.so
%{_libdir}/pkgconfig/*.pc
#%%{_mandir}/man3/*.gz

%changelog
%autochangelog
