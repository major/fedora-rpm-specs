Name:		gprolog
Version:	1.5.0
Release:	%autorelease
Summary:	GNU Prolog is a free Prolog compiler

License:	LGPL-3.0-or-later OR GPL-2.0-or-later
URL:		http://www.gprolog.org
Source:		http://www.gprolog.org/gprolog-%{version}.tar.gz
Patch0:		gprolog.make-print-submake-output.patch
# Link binaries with Fedora ldflags
Patch1:		gprolog.link-with-fedora-flags.patch

BuildRequires:	gcc-c++
BuildRequires:	gdb-headless
BuildRequires:	make

ExclusiveArch:	x86_64 %{ix86} ppc alpha aarch64

Obsoletes:	gprolog-examples < 1.4.0
Provides:	gprolog-examples = %{version}-%{release}

%description 
GNU Prolog is a native Prolog compiler with constraint solving over
finite domains (FD) developed by Daniel Diaz
(http://loco.inria.fr/~diaz).

GNU Prolog is a very efficient native compiler producing (small)
stand-alone executables. GNU-Prolog also offers a classical
top-level+debugger.

GNU Prolog conforms to the ISO standard for Prolog but also includes a
lot of extensions (global variables, DCG, sockets, OS interface,...).

GNU Prolog also includes a powerful constraint solver over finite
domains with many predefined constraints+heuristics.


%package docs
Summary:	Documentation for GNU Prolog
Requires:	%{name} = %{version}-%{release}

%description docs
Documentation for GNU Prolog.

%prep
%autosetup -p1

# For build reproducibility reasons, we do not want to insert today's date
# into header files, but rather the date of the gprolog release.
verdate=$(date +"%b %d %Y" -r VERSION)
veryear=$(date +%Y -r VERSION)
sed -i s/'`pl_date`'/"\"$verdate\""/';'s/'`pl_year`'/"$veryear"/ src/configure

%build
# This package fails to build with LTO due to use of global register variables.
# See https://gcc.gnu.org/bugzilla/show_bug.cgi?id=68384 for an explanation.
# Disable LTO
%define _lto_cflags %{nil}

cd src

# BZ #1799464
%define _legacy_common_support 1

# See http://lists.gnu.org/archive/html/bug-prolog/2016-08/msg00006.html
# for the discussion on adding '--disable-regs'
%configure \
      --with-install-dir=$RPM_BUILD_ROOT%{_libdir}/gprolog-%{version} \
      --without-links-dir --without-examples-dir \
      --with-doc-dir=dist-doc \
      --with-c-flags="$RPM_OPT_FLAGS" \
%ifarch %{ix86}
      --disable-regs
%endif

# Remove package notes flag from LDFLAGS
# See https://bugzilla.redhat.com/show_bug.cgi?id=2051341
sed -i 's/ -Wl,-dT.*\.ld//' EnginePl/gp_config.h

# _smp_flags seems to make trouble
make

%check
cd src
#
export PATH=$RPM_BUILD_ROOT%{_bindir}:$PATH
#
make check

%install
cd src
(
    make install
    mkdir $RPM_BUILD_ROOT%{_bindir}
    cd $RPM_BUILD_ROOT%{_libdir}/gprolog-%{version}/bin
    for i in *; do
	ln -s ../%{_lib}/gprolog-%{version}/bin/$i $RPM_BUILD_ROOT%{_bindir}/$i
    done
)
rm -f dist-doc/*.{chm,dvi,ps}
rm -f dist-doc/compil-scheme.pdf
rm -f dist-doc/debug-box.pdf

for file in ChangeLog COPYING NEWS README VERSION
do
    rm -f $RPM_BUILD_ROOT%{_libdir}/gprolog-%{version}/$file
done

%files
%doc README COPYING ChangeLog NEWS PROBLEMS VERSION
%{_bindir}/*
%{_libdir}/gprolog-%{version}

%files docs
%doc src/dist-doc/*

%changelog
%autochangelog
