# The memory management scheme does not work with PIE
%undefine _hardened_build

%global giturl  https://github.com/polyml/polyml

Name:           polyml
Version:        5.9.2
Release:        %autorelease
Summary:        Poly/ML compiler and runtime system

License:        LGPL-2.1-or-later
URL:            https://www.polyml.org/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{name}-%{version}.tar.gz

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  libffi-devel
BuildRequires:  make

Requires:       gcc-c++
Requires:       polyml-libs%{?_isa} = %{version}-%{release}

%description
Poly/ML is a full implementation of Standard ML available as open-source.
This release supports the ML97 version of the language and the Standard Basis
Library.

%package doc
Summary:        Poly/ML documentation
BuildArch:      noarch

%description doc
Documentation for Poly/ML.

%package libs
Summary:        Poly/ML runtime libraries

%description libs
Runtime libraries for Poly/ML.

%prep
%autosetup -p1

%conf
# Fix end of line encoding
sed -i 's/\r//' documentation/main.css

%build
# Some hand-coded assembler is included.  While it does contain an explicit
# section marker stating that the stack section does not need the executable
# bit, for some reason that marker does not always take effect, causing the
# executable to be marked as needing an executable stack on some arches.  This
# is bad news for people running SELinux.  The execstack flag is not really
# needed, so we go through the contortions below to keep it off.
%configure --enable-shared --disable-static \
%ifarch %{x86_64} %{arm64}
  --enable-compact32bit \
%endif
  CPPFLAGS="-D_GNU_SOURCE" \
  CFLAGS="%{build_cflags} -fno-strict-aliasing -Wa,--noexecstack" \
  CXXFLAGS="%{build_cxxflags} -fno-strict-aliasing -Wa,--noexecstack" \
  CCASFLAGS="-Wa,--noexecstack" \
  LDFLAGS="%{build_ldflags} -Wl,-z,noexecstack"

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build

# Change polyc:
# - avoid adding an rpath
# - don't link to extra libraries unnecessarily
# - build with extension_cflags instead of build_cflags
extflags=$(sed 's/[[:space:]]*$//' <<< '%{extension_cflags}')
sed -e 's/-Wl,-rpath,\${LIBDIR} //'\
    -e 's/-lffi //;s/-lgmp //' \
    -e "s/^\(CFLAGS=\).*/\1\"-O2 -pipe -fno-strict-aliasing $extflags\"/" \
    -i polyc

%install
%make_install

%check
make check

%files
%{_bindir}/poly
%{_bindir}/polyc
%{_bindir}/polyimport
%{_libdir}/libpolymain.a
%{_libdir}/libpolyml.so
%{_libdir}/polyml/
%{_libdir}/pkgconfig/polyml.pc
%{_mandir}/man1/poly.1*
%{_mandir}/man1/polyc.1*
%{_mandir}/man1/polyimport.1*

%files doc
%doc documentation/*
%license COPYING

%files libs
%license COPYING
%{_libdir}/libpolyml.so.16{,.*}

%changelog
%autochangelog
