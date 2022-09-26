Name:           clibs-list
Version:        0.4.0
%global so_version 0
Release:        %autorelease
Summary:        C doubly linked list implementation

# SPDX
License:        MIT
URL:            https://github.com/clibs/list
Source0:        %{url}/archive/%{version}/list-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%global common_description %{expand:
%{summary}.}

%description %{common_description}

The clibs-list package contains the clibs/list library.


%package devel
Summary:        Development files for clibs-list

Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel %{common_description}

The clibs-list-devel package contains libraries and header files for developing
applications that use clibs-list.


%prep
%autosetup -n list-%{version} -p1


%build
%set_build_flags
%make_build \
    AR="${AR-gcc-ar}" CC="${CC-gcc}" STRIP=/bin/true \
    CFLAGS="${CFLAGS}" LDFLAGS="${LDFLAGS}" \
    all bin/test


%install
%make_install PREFIX='%{_prefix}' LIBDIR='%{_libdir}'
# We did not want the static library.
rm -vf '%{buildroot}%{_libdir}/libclibs_list.a'


%check
%make_build test


%files
%license LICENSE
%{_libdir}/libclibs_list.so.%{so_version}{,.*}


%files devel
%doc History.md
%doc Readme.md
# This directory should be co-owned with anything else from
# https://github.com/clibs/, e.g. https://github.com/clibs/buffer/, if packaged
# in the future:
%dir %{_includedir}/clibs
%{_includedir}/clibs/list.h
%{_libdir}/libclibs_list.so


%changelog
%autochangelog
