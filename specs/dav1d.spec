Name:           dav1d
Version:        1.5.1
Release:        %autorelease
Summary:        AV1 cross-platform Decoder

# src/ext/x86/x86inc.asm is ISC
# tools/compat/getopt.c is ISC
License:        BSD-2-Clause AND ISC
URL:            https://code.videolan.org/videolan/dav1d
Source:         %{url}/-/archive/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  nasm >= 2.14
BuildRequires:  meson >= 0.49.0
BuildRequires:  pkgconfig(libxxhash)

Requires:       libdav1d%{?_isa} = %{version}-%{release}

%description
dav1d is a new AV1 cross-platform Decoder, open-source, and focused on speed
and correctness.

%package     -n libdav1d
Summary:        Library files for dav1d

%description -n libdav1d
Library files for dav1d, the AV1 cross-platform Decoder.

%package     -n libdav1d-devel
Summary:        Development files for dav1d
Requires:       libdav1d%{?_isa} = %{version}-%{release}

%description -n libdav1d-devel
Development files for dav1d, the AV1 cross-platform Decoder.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc CONTRIBUTING.md NEWS README.md
%{_bindir}/dav1d

%files -n libdav1d
%license COPYING doc/PATENTS
%{_libdir}/libdav1d.so.7{,.*}

%files -n libdav1d-devel
%{_includedir}/dav1d/
%{_libdir}/libdav1d.so
%{_libdir}/pkgconfig/dav1d.pc

%changelog
%autochangelog
