%global opencsd_tag 9b462f77a4e1c6ab363fafe8f1f5d7374f5782b5

Name:           opencsd
Version:        1.8.2
Release:        %autorelease
Summary:        An open source CoreSight(tm) Trace Decode library

License:        BSD-3-Clause
URL:            https://github.com/Linaro/OpenCSD
Source0:        https://github.com/Linaro/OpenCSD/archive/%{opencsd_tag}.tar.gz

Patch0:         0001-hack-test.patch

BuildRequires:  patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  make

%description
This library provides an API suitable for the decode of ARM(r)
CoreSight(tm) trace streams.

%package devel
Summary: Development files for the CoreSight(tm) Trace Decode library
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The opencsd-devel package contains headers and libraries needed
to develop CoreSight(tm) trace decoders.

%prep
%autosetup -p1 -n OpenCSD-%{opencsd_tag}

%build
cd decoder/build/linux
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS"
LIB_PATH=%{_lib} make %{?_smp_mflags}

%install
cd decoder/build/linux
PREFIX=%{buildroot}%{_prefix} LIB_PATH=%{_lib} make install install_man DISABLE_STATIC=1 DEF_SO_PERM=755

%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} decoder/tests/run_pkt_decode_tests.bash -bindir %{buildroot}%{_bindir}/ use-installed

%files
%license LICENSE
%doc HOWTO.md README.md
%{_libdir}/*so\.*
%{_bindir}/*
%{_mandir}/man1/trc_pkt_lister.1.gz

%files devel
%doc decoder/docs/prog_guide/*
%{_includedir}/*
# no man files..
%{_libdir}/*so

#------------------------------------------------------------------------------
%autochangelog
