Name:     libopusenc
Version:  0.3
Release:  %autorelease
Summary:  A library that provides an easy way to encode Ogg Opus files
# Automatically converted from old format: BSD - review is highly recommended.
License:  LicenseRef-Callaway-BSD
URL:      https://opus-codec.org/

Source0:  https://archive.mozilla.org/pub/opus/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: doxygen
BuildRequires: opus-devel
BuildRequires: make

%description
A library that provides an easy way to encode Ogg Opus files.

%package  devel
Summary:  Development package for libopusenc
Requires: opus-devel
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with libopusenc.

%prep
%setup -q

%build
%configure --disable-static

%make_build

%install
%make_install

# Remove libtool archives
find %{buildroot} -type f -name "*.la" -delete
rm -rf %{buildroot}%{_datadir}/doc/libopusenc/

%check
make check %{?_smp_mflags} V=1

%ldconfig_scriptlets

%files
%license COPYING
%{_libdir}/libopusenc.so.*

%files devel
%doc doc/html
%{_includedir}/opus/opusenc.h
%{_libdir}/libopusenc.so
%{_libdir}/pkgconfig/libopusenc.pc

%changelog
%autochangelog
