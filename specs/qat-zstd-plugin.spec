# SPDX-License-Identifier: MIT

Name:		qat-zstd-plugin
Version:	1.0.0
Release:	%autorelease
Summary:	Intel QuickAssist Technology ZSTD Plugin

License:	BSD-3-Clause
URL:		https://github.com/intel/QAT-ZSTD-Plugin
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Patch0:		test.patch

BuildRequires:	automake
BuildRequires:	gcc
BuildRequires:	libzstd-devel
BuildRequires:	qatlib-devel
BuildRequires:	numactl-devel

# Upstream only supports x86_64
ExclusiveArch:	x86_64

%description
Intel QuickAssist Technology ZSTD is a plugin to Zstandard for accelerating
compression by QAT. ZSTD* is a fast lossless compression algorithm, targeting
real-time compression scenarios at zlib-level and better compression ratios.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
applications that use %{name}.

%package static
Summary:	Static library for %{name}
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}

%description static
The %{name}-static package contains the static %{name} library.

%prep
%autosetup -p1 -n QAT-ZSTD-Plugin-%{version}

# fedora/rhel path fixes
sed -i -e 's|/usr/local|%{_prefix}|g' src/Makefile
sed -i -e 's|$(PREFIX)/lib|%{_libdir}|g' src/Makefile
sed -i -e 's|$(PREFIX)/include|%{_includedir}|g' src/Makefile

%build
%make_build LDFLAGS="$LDFLAGS -lzstd"
make test

%install
%make_install

%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} ./test/test README.md

%files
%license LICENSE
%{_libdir}/libqatseqprod.so.1
%{_libdir}/libqatseqprod.so.%{version}

%files devel
%{_includedir}/qatseqprod.h
%{_libdir}/libqatseqprod.so

%files static
%license LICENSE
%{_libdir}/libqatseqprod.a

%changelog
%autochangelog
