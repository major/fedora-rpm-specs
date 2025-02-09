%if %{undefined package_revision}
%global package_revision 1
%endif

%if %{undefined make_build}
%global make_build %{__make} %{?_smp_mflags}
%endif

%if %{undefined autosetup}
%global autosetup %setup -q
%endif

%global release_version 1.0.62
%global gittag v%{release_version}

%if %{undefined make_check}
%global make_check 1
%endif

#
# main package
#
Summary: Fast User Level LOCK (FULLOCK) library for C/C++
Name: libfullock
Version: %{release_version}
Release: %autorelease
License: MIT

URL: https://github.com/yahoojapan/fullock
Source0: https://github.com/yahoojapan/fullock/archive/%{gittag}/fullock-%{release_version}.tar.gz
BuildRequires: git-core gcc-c++ make libtool

%description
fullock is an open-source software for user level lock library sup-
ported by Yahoo! JAPAN. It runs on user level and provides two types
lock. One is a shared reader/writer lock which has the same function-
ality with pthread_rwlock. Another is a shared mutex lock which also
has the same functionality with pthread_mutex.

Here is primary fullock features:

1. fullock is a thread safety library which can be used for multi-
processing as well as for multi-threading.

2. fullock releases a mutex lock safely even if a lock owner
process exit with 0 in which case OS doesn't release the lock.

3. fullock provides a shared reader/writer lock. A lock owner
thread can get another lock again without deadlock.

Please visit our website and get more details at:

https://github.com/yahoojapan/fullock

%prep
%autosetup -n fullock-%{version}

%build
./autogen.sh
%configure --disable-static 
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%if %{make_check}
%check
%{__make} check
%endif

%if %{defined ldconfig_scriptlets}
%ldconfig_scriptlets
%else
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%endif

%files
%if 0%{?rhel} == 6
%doc COPYING
%defattr(-,root,root)
%else
%license COPYING
%endif
%doc README AUTHORS ChangeLog
%{_libdir}/libfullock.so.1*
%{_mandir}/man3/*

#
# devel package
#
%package devel
Summary: Fast User Level LOCK (FULLOCK) library for C/C++ (development)
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development package for building with libfullock shared library.
This package has header files and symbols for it.

%files devel
%if 0%{?rhel} == 6
%defattr(-,root,root)
%endif
%doc README AUTHORS ChangeLog
%{_includedir}/*
%{_libdir}/libfullock.so
%{_libdir}/pkgconfig/*.pc

%changelog
%autochangelog
