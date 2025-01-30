%global m4rie_tag 75a2a862c15932cd86a42b670cd6edc5a004f1d3

Name:           m4rie
Version:        20250128
Release:        %autorelease
Summary:        Linear Algebra over F_2^e
License:        GPL-2.0-or-later
# The bitbucket is labeled as a mirror of github now, and is trailing commits
URL:            https://github.com/malb/m4rie
Source:         %{url}/archive/%{m4rie_tag}.tar.gz
# Remove unnecessary direct library dependencies from the pkgconfig file,
# and also cflags used to compile m4rie, but not needed by consumers of m4rie.
Patch:          %{name}-pkgconfig.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  make
BuildRequires:  pkgconfig(m4ri)
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool


%description
M4RIE is a library for fast arithmetic with dense matrices over F_2^e.
It is an add-on to the M4RI library, which implements fast arithmetic
with dense matrices over F_2.  M4RIE is used by the Sage mathematics
software.

%package        devel
# The content of the HTML documentation is GPL-2.0-or-later.  The other licenses
# are for files copied into the documentation by doxygen.
# bc_s.png: GPL-1.0-or-later
# bdwn.png: GPL-1.0-or-later
# closed.png: GPL-1.0-or-later
# doc.png: GPL-1.0-or-later
# doxygen.css: GPL-1.0-or-later
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
Requires:       m4ri-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        static
Summary:        Static library files for %{name}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    static
The %{name}-static package contains the static %{name} library.

%prep
%autosetup -p1 -n m4rie-%{m4rie_tag}

%build
autoreconf -fi
%configure

%make_build
cd m4rie
doxygen
cd -

%install
%make_install
rm -f %{buildroot}%{_libdir}/lib%{name}.la

%check
make check

%files
%license COPYING
%{_libdir}/lib%{name}.so.*

%files devel
%doc doc/html
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files static
%{_libdir}/lib%{name}.a

%autochangelog
