Name: libmaa
Version: 1.5.1
Release: 3%{?dist}
Summary: Library that implements some basic data structures and algorithms
URL: https://github.com/cheusov/libmaa
License: MIT

Source0: https://github.com/cheusov/libmaa/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: mk-configure
BuildRequires: gcc
BuildRequires: pkgconfig(zlib)

%description
This library implements some basic data structures and algorithms such
as command line arguments handling, base26 and base64 routines, bits
manipulation, debugging and error reporting routines, hash tables,
sets, lists, stacks, skip lists, string pool routines, memory
management routines, parsing routines, process management routines,
source code management routines and timer support.

%package devel
Summary: Development files for libmaa
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files (Headers, etc) for libmaa.

%global env \
        export MKSTATICLIB=no \
        export NOSUBDIR=doc

%prep
%autosetup -p1

%build
%{env}
%mkcmake

%install
%{env}
%mkcmake install DESTDIR=%{buildroot}
chmod +x %{buildroot}/%{_libdir}/*.so.*

%check
%mkcmake test

%files
%license doc/LICENSE
%doc README doc/NEWS
%{_libdir}/libmaa.so.4{,.*}

%files devel
%{_includedir}/maa*
%{_libdir}/libmaa.so

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 17 2024 Carlos Rodriguez-Fernandez <carlosrodrifernandez@gmail.com> - 1.5.1-1 
- Update to 1.5.1, closes fedora#2283998
* Sun Jan 7 2024 Carlos Rodriguez-Fernandez <carlosrodrifernandez@gmail.com> - 1.4.7-1
- First release
