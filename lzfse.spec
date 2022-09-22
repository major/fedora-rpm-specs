Name:           lzfse
Version:        1.0
Release:        %autorelease
Summary:        LZFSE compression library and command line tool

License:        BSD
URL:            https://github.com/lzfse/lzfse
Source:         %{url}/archive/%{name}-%{version}/%{name}-%{name}-%{version}.tar.gz
# cmake: version the shared library
Patch:          %{url}/pull/60.patch

BuildRequires:  cmake
BuildRequires:  gcc

# LZFSE isn't supported on big-endian architectures
# https://github.com/lzfse/lzfse/issues/23
ExcludeArch:    s390x

%description
LZFSE is a Lempel-Ziv style data compression algorithm using Finite State
Entropy coding. It targets similar compression rates at higher compression
and decompression speed compared to deflate using zlib.

This package is a reference C implementation of the LZFSE compressor introduced
in the Compression library with OS X 10.11 and iOS 9.

%package        libs
Summary:        Shared libraries for %{name}

%description    libs
This package contains shared libraries for %{name}.

%package        devel
Summary:        Development headers and libraries for %{name}
Requires:       %{name}-libs%{_isa} = %{version}-%{release}

%description    devel
This package contains development headers and libraries for %{name}.

%prep
%autosetup -n %{name}-%{name}-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%doc README.md
%{_bindir}/%{name}

%files libs
%license LICENSE
%{_libdir}/lib%{name}.so.1*

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so

%changelog
%autochangelog
