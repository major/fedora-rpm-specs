Name:           libmetalink
Version:        0.1.3
%global so_version 3
Release:        %autorelease
Summary:        Metalink library written in C

License:        MIT
URL:            https://github.com/metalink-dev/libmetalink
Source0:        %{url}/archive/release-%{version}/libmetalink-release-%{version}.tar.gz

# NULL ptr deref in initial_state_start_fun
# https://bugs.launchpad.net/libmetalink/+bug/1888672
Patch:          https://bugs.launchpad.net/libmetalink/+bug/1888672/+attachment/5395227/+files/libmetalink-0.1.3-ns_uri.patch
# Fix few issues found by the Coverity static analysis tool
# https://bugs.launchpad.net/libmetalink/+bug/1784359
# https://github.com/metalink-dev/libmetalink/pull/2
Patch:          https://bugs.launchpad.net/libmetalink/+bug/1784359/+attachment/5169495/+files/0001-fix-covscan-issues.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

BuildRequires:  gcc
BuildRequires:  make

BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(cunit)
# Required for AM_PATH_XML2 m4 macro so we can “autoreconf”; however, expat is
# used preferentially where available.
BuildRequires:  libxml2-devel

%description
libmetalink is a Metalink C library. It adds Metalink functionality such as
parsing Metalink XML files to programs written in C.


%package        devel
Summary:        Files needed for developing with libmetalink

Requires:       libmetalink%{?_isa} = %{version}-%{release}

%description    devel
Files needed for building applications with libmetalink.


%prep
%autosetup -p1 -n libmetalink-release-%{version}


%build
autoreconf --force --install --verbose
%configure --disable-static
%make_build


%check
%make_build check


%install
%make_install
find '%{buildroot}' -type f -name '*la' -print -delete


%files
%license COPYING
%doc AUTHORS
%doc ChangeLog
%doc NEWS
%doc README
%{_libdir}/libmetalink.so.%{so_version}{,.*}


%files devel
%{_includedir}/metalink/
%{_libdir}/libmetalink.so
%{_libdir}/pkgconfig/libmetalink.pc
%{_mandir}/man3/metalink*.3.*


%changelog
%autochangelog
