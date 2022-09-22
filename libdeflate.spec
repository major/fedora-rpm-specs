Name:          libdeflate
Version:       1.9
Release:       %autorelease
Summary:       Fast implementation of DEFLATE, gzip, and zlib
License:       MIT
URL:           https://github.com/ebiggers/libdeflate
Source0:       https://github.com/ebiggers/%{name}/archive/v%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make

%description
libdeflate is a library for fast, whole-buffer DEFLATE-based compression and
decompression, supporting DEFLATE, gzip, and zlib.

%package devel
Summary:       Development files for libdeflate
License:       MIT
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for libdeflate.

%package utils
Summary:       Binaries from libdeflate
License:       MIT
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description utils
Binaries from libdeflate.

%prep
%autosetup
sed -r -i 's/-O2 -fomit-frame-pointer -std=c99/-std=c99/' Makefile

%build
%make_build CFLAGS="%optflags -fpic -pie -g" USE_SHARED_LIB=1 LIBDIR=%{_libdir} PREFIX=%{_prefix}

%install
%make_install CFLAGS="%optflags -fpic -pie -g" USE_SHARED_LIB=1 LIBDIR=%{_libdir} PREFIX=%{_prefix}
rm %{buildroot}/%{_libdir}/*.a

%files
%doc NEWS.md README.md
%license COPYING
%{_libdir}/libdeflate.so.0

%files devel
%{_includedir}/libdeflate.h
%{_libdir}/libdeflate.so
%{_libdir}/pkgconfig/*

%files utils
%{_bindir}/libdeflate-gzip
%{_bindir}/libdeflate-gunzip

%changelog
%autochangelog
