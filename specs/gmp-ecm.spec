Name:           gmp-ecm
Version:        7.0.7
Release:        %autorelease
Summary:        Elliptic Curve Method for Integer Factorization
License:        GPL-3.0-or-later
URL:            https://gitlab.inria.fr/zimmerma/ecm
Source0:        %{url}/-/archive/git-%{version}/ecm-git-%{version}.tar.bz2

BuildRequires:  docbook-style-xsl
BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  gsl-devel
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  m4
BuildRequires:  make

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
Programs and libraries employing elliptic curve method for factoring
integers (with GMP for arbitrary precision integers).

%package        libs
Summary:        Elliptic Curve Method library
License:        LGPL-3.0-or-later

%description    libs
The %{name} elliptic curve method library.

%package        devel
Summary:        Files useful for %{name} development
License:        LGPL-3.0-or-later
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}

%description    devel
The libraries and header files for using %{name} for development.

%prep
%autosetup -n ecm-git-%{version}

fixtimestamp() {
  touch -r $1.orig $1
  rm -f $1.orig
}

# Fix non-UTF-8 encodings
for badfile in AUTHORS ; do
  iconv -f iso-8859-1 -t utf-8 -o $badfile.UTF-8 $badfile 
  touch -r $badfile $badfile.UTF-8
  mv $badfile.UTF-8 $badfile
done

# Fix the FSF's address
for badfile in `grep -FRl 'Fifth Floor' .`; do
  sed -e 's/Fifth Floor/Suite 500/' -e 's/02111-1307/02110-1335/' \
      -i.orig $badfile
  fixtimestamp $badfile
done

# Generate the configure script
autoreconf -fi .


%build
# Build an SSE2-enabled version for 32-bit x86, and a non-SSE2 version for all
# other arches, including x86_64; the assembly code containing SSE2
# instructions is 32-bit only.
%configure --disable-static --enable-shared --enable-openmp \
  --disable-gmp-cflags \
%ifarch %{ix86}
  --enable-sse2 \
%else
  --disable-sse2 \
%endif
  CFLAGS='%{build_cflags} -Wa,--noexecstack' \
  LDFLAGS='%{build_ldflags} -Wl,-z,noexecstack -lgmp -lgomp'

# Eliminate hardcoded rpaths; workaround libtool reordering -Wl,--as-needed
# after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC=.g..|& -Wl,--as-needed|' \
    -i libtool

%make_build


%install
%make_install INSTALL="install -p"
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
pushd $RPM_BUILD_ROOT%{_bindir}
  mv ecm %{name}
popd
pushd $RPM_BUILD_ROOT%{_mandir}/man1
  for file in ecm.1*; do
    mv $file ${file/ecm/%{name}}
  done
popd


%check
export LD_LIBRARY_PATH=$PWD/.libs
make check


%files
%doc README
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%files libs
%doc AUTHORS ChangeLog NEWS TODO
%license COPYING.LIB
%{_libdir}/libecm.so.1
%{_libdir}/libecm.so.1.*

%files devel
%doc README.lib
%{_includedir}/ecm.h
%{_libdir}/libecm.so

%changelog
%autochangelog
