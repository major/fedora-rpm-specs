Name:       libtbox
Version:    1.7.8

%global forgeurl https://github.com/tboox/tbox

%forgemeta

Release:    %autorelease
Summary:    Portable toolbox library with great cross-platform support

# Library and 3rd-party modules licensing:
# * tbox - Apache-2.0 -- Main tarball;
# * src/tbox/platform/arch/*/context.{S,asm} - BSL-1.0 -- static dependency;
# * src/tbox/hash/adler32.c -- Zlib -- static dependency.
License:    Apache-2.0 AND BSL-1.0 AND Zlib
URL:        https://tboox.org
Source:     %{forgesource}

Patch0:     0001-build-fix-DESTDIR-add-relwithdebinfo.patch

BuildRequires:  bash
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
A feature-packed, embedded friendly toolbox library.
Think of stdlib for embedded systems or Boost for C.
Provides stream, coroutine, regex, container, algorithm and more modules.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains headers and development files for %{name}.

%prep
%forgeautosetup -p1
cat > %{name}.pc << EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: %{name}
Description: %{summary}
Version: %{version}
Libs: -ltbox
EOF

chmod -x *.md

%build
%configure \
  --kind=shared \
  --mode=relwithdebinfo \
  --hash=yes \
  --charset=yes \
  --float=yes \
  --force_utf8=yes
%make_build

%install
%make_install
rm %{buildroot}%{_bindir}/demo

install -Dm644 %{name}.pc %{buildroot}%{_libdir}/pkgconfig/%{name}.pc

%check
%make_build run

%files
%doc README.md README_zh.md CHANGELOG.md
%license LICENSE.md NOTICE.md
%{_libdir}/%{name}.so.1*

%files devel
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/tbox/

%changelog
%autochangelog
