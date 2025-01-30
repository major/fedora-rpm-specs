%global m4ri_tag 36fb553337f4255beb94ed479e23e653d88d8820

Name:           m4ri
Version:        20250128
Release:        %autorelease
Summary:        Linear Algebra over F_2
License:        GPL-2.0-or-later
# The bitbucket is labeled as a mirror of github now, and is trailing commits
URL:            https://github.com/malb/m4ri
Source:         %{url}/archive/%{m4ri_tag}.tar.gz
# Remove an unnecessary direct library dependency from the pkgconfig file,
# and also cflags used to compile m4ri, but not needed by consumers of m4ri.
Patch0:          %{name}-pkgconfig.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  libpng-devel
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool


%description
M4RI is a library for fast arithmetic with dense matrices over F_2.
The name M4RI comes from the first implemented algorithm: The "Method
of the Four Russians" inversion algorithm published by Gregory Bard.
M4RI is used by the Sage mathematics software and the BRiAl library.


%package        devel
# The content of the HTML documentation is GPL-2.0-or-later.  The other licenses
# are for files copied into the documentation by doxygen.
# bc_s.png: GPL-1.0-or-later
# bdwn.png: GPL-1.0-or-later
# closed.png: GPL-1.0-or-later
# doc.png: GPL-1.0-or-later
# doxygen.svg: GPL-1.0-or-later
# dynsections.js: MIT
# folderclosed.png: GPL-1.0-or-later
# folderopen.png: GPL-1.0-or-later
# jquery.js: MIT
# menu.js: MIT
# menudata.js: MIT
# nav_f.png: GPL-1.0-or-later
# nav_g.png: GPL-1.0-or-later
# nav_h.png: GPL-1.0-or-later
# open.png: GPL-1.0-or-later
# splitbar.png: GPL-1.0-or-later
# sync_off.png: GPL-1.0-or-later
# sync_on.png: GPL-1.0-or-later
# tab_a.png: GPL-1.0-or-later
# tab_b.png: GPL-1.0-or-later
# tab_h.png: GPL-1.0-or-later
# tab_s.png: GPL-1.0-or-later
# tabs.css: GPL-1.0-or-later
License:        GPL-2.0-or-later AND GPL-1.0-or-later AND MIT
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       bundled(js-jquery)

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        static
Summary:        Static library files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    static
The %{name}-static package contains the static %{name} library.


%prep
%autosetup -p1 -n m4ri-%{m4ri_tag}

# Fix the version number in the documentation, and generate only HTML
sed -i 's/20140914/%{version}/;/GENERATE_LATEX/s/YES/NO/' m4ri/Doxyfile


%build
autoreconf -fi
%configure --enable-openmp \
%ifarch %{ix86} x86_64
  --enable-sse2

sed -e 's/^\(#define __M4RI_HAVE_SSE2[[:blank:]]*\)0/\11/' \
    -e 's/^\(#define __M4RI_SIMD_CFLAGS[[:blank:]]*\).*/\1" -mmmx -msse -msse2"/' \
    -i m4ri/m4ri_config.h
sed -i 's/^SIMD_CFLAGS =.*/SIMD_CFLAGS = -mmmx -msse -msse2/' Makefile
%else
  --disable-sse2
%endif

# Die, rpath, die!  Also workaround libtool reordering -Wl,--as-needed after
# all the libraries
sed -e "s|\(hardcode_libdir_flag_spec=\)'.*|\1|" \
    -e "s|\(runpath_var=\)LD_RUN_PATH|\1|" \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build

# Build documentation
cd m4ri
doxygen
cd -


%install
%make_install
rm -f %{buildroot}%{_libdir}/lib%{name}.la


%check
make check LD_LIBRARY_PATH=$PWD/.libs


%files
%doc AUTHORS
%license COPYING
%{_libdir}/lib%{name}.so.*


%files devel
%doc doc/html
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%files static
%{_libdir}/lib%{name}.a

%autochangelog
