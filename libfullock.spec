#
# FULLOCK - Fast User Level LOCK library
#
# Copyright 2015 Yahoo Japan Corporation.
#
# FULLOCK is fast locking library on user level by Yahoo! JAPAN.
# FULLOCK is following specifications.
#
# For the full copyright and license information, please view
# the license file that was distributed with this source code.
#
# AUTHOR:   Takeshi Nakatani
# CREATE:   Thu 16 Jul 2015
# REVISION:
#

#
# Local macros/define
#
%if %{undefined package_revision}
%global package_revision 1
%endif

%if %{undefined make_build}
%global make_build %{__make} %{?_smp_mflags}
%endif

%if %{undefined autosetup}
%global autosetup %setup -q
%endif

%global gittag v1.0.48

%if %{undefined make_check}
%global make_check 1
%endif

#
# main package
#
Summary: Fast User Level LOCK (FULLOCK) library for C/C++
Name: libfullock
Version: 1.0.48
Release: %{package_revision}%{?dist}
License: MIT

URL: https://github.com/yahoojapan/fullock
Source0: https://github.com/yahoojapan/fullock/archive/%{gittag}/fullock-%{version}.tar.gz
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
* Fri Feb 24 2023 Hirotaka Wakabayashi <hiwkby@yahoo.com> - 1.0.48-1
- Updates to libfullock-1.0.48

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.44-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.44-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Feb 11 2022 Hirotaka Wakabayashi <hiwkby@yahoo.com> - 1.0.44-1
- Updates to libfullock-1.0.44

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.39-1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.39-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.39-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 18 2020 Hirotaka Wakabayashi <hiwkby@yahoo.com> - 1.0.39-1
- Update to libfullock-1.0.39

* Wed Nov 18 2020 Hirotaka Wakabayashi <hiwkby@yahoo.com> - 1.0.38-1
- Update to libfullock-1.0.38

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.36-1.4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.36-1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.36-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.36-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 15 2019 Hirotaka Wakabayashi <hiwkby@yahoo.com>   1.0.36-1
- Update to libfullock-1.0.36

* Tue Dec 04 2018 Takeshi Nakatani <ggtakec@gmail.com>   1.0.32-1
- Fixed RPM packaging about configure.ac and spec file
- Updated some scripts related to packaging

* Tue Nov 27 2018 Takeshi Nakatani <ggtakec@gmail.com>   1.0.31
- Changed to strict packaging and changed documents

* Wed Oct 17 2018 Takeshi Nakatani <ggtakec@gmail.com>   1.0.30
- Fixed lintian error in man page about wrong word(2)

* Wed Oct 17 2018 Takeshi Nakatani <ggtakec@gmail.com>   1.0.29
- Fixed lintian error in man page about wrong word

* Fri Jun 29 2018 Takeshi Nakatani <ggtakec@gmail.com>   1.0.28
- avoid static object initialization order problem(SIOF) - #4

* Tue May 15 2018 Takeshi Nakatani <ggtakec@gmail.com>   1.0.27
- Updated make discription script for packaging
- Fixed a bug about packaging for debian

* Tue May 15 2018 Takeshi Nakatani <ggtakec@gmail.com>   1.0.26
- Fixed a bug about packaging for debian

* Tue May 15 2018 Takeshi Nakatani <ggtakec@gmail.com>   1.0.25
- Cleanup credit comments in sources
- Changed build logic to new for rpm/debian packaging
- Updated the man page

* Mon Mar 13 2017 Takeshi Nakatani <ggtakec@gmail.com>   1.0.24
- Added lib_version_for_link option to make_valiables.sh
- Refixed a bug about deadlock at forking - #1

* Mon Feb 13 2017 Takeshi Nakatani <ggtakec@gmail.com>   1.0.23
- Fixed a bug about deadlock at forking

* Mon Feb 06 2017 Takeshi Nakatani <ggtakec@gmail.com>   1.0.22
- Changed exclusive control more strictly

* Wed Dec 07 2016 Takeshi Nakatani <ggtakec@gmail.com>   1.0.21
- First version of open source on Github
