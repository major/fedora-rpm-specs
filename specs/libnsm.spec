%global crate aws-nitro-enclaves-nsm-api

Name:           libnsm
Version:        0.5.2
Release:        %{autorelease}
Summary:        C library for AWS Nitro Secure Module (NSM) API

SourceLicense:  Apache-2.0
# These are the licenses of statically-linked Rust dependencies, from the
# output of %%{cargo_license_summary}.
#
# Apache-2.0
# Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
%global additional_rust_licenses %{shrink:
    MIT AND
    (Apache-2.0 OR MIT)
    }
License:        Apache-2.0 AND %{additional_rust_licenses}
URL:            https://github.com/aws/%{crate}
Source0:        %{url}/archive/v%{version}/%{crate}-%{version}.tar.gz

BuildRequires:  cargo-rpm-macros
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  patchelf

ExcludeArch:  %{ix86}

%global _description %{expand:
C library for Nitro Secure Module (NSM).}

%description
%{summary}.

%package devel
Summary: Header files and library for libnsm development
Requires: %{name}%{?_isa} = %{version}-%{release}

# This subpackage contains no statically linked Rust dependencies
License:         Apache-2.0

%description devel
The libnsm-devel package contains the library and headers needed to
develop programs that use the libnsm Nitro Secure Module (NSM) C library.

# The static library is required by the libkrun-awsnitro init binary. The init
# binary runs as an initramfs within constrained environments and requires
# libnsm before a root file system (and thus a libnsm shared library) is
# available.
%package static
Summary: Header files and static library for libnsm development
Requires: %{name}-devel%{?_isa} = %{version}-%{release}

%description static
The libnsm-static package contains the static version of the libnsm Nitro
Secure Module (NSM) C library.

%prep
%autosetup -n %{crate}-%{version}
%{cargo_prep}

%generate_buildrequires
%cargo_generate_buildrequires

%build
%make_build nsm-lib
cd nsm-lib
%{cargo_license_summary -a}
%{cargo_license -a} > ../LICENSE.dependencies

%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir} INCLUDEDIR=%{_includedir}

%files
%license LICENSE
%{_libdir}/libnsm.so.%{version}
%{_libdir}/libnsm.so.0
%license LICENSE.dependencies

%files devel
%{_includedir}/nsm.h
%{_libdir}/pkgconfig/libnsm.pc
%{_libdir}/libnsm.so

%files static
%{_libdir}/libnsm.a

%changelog
%autochangelog
