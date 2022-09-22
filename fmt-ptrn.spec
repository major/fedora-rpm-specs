Name: fmt-ptrn
Version: 1.3.22
Release: %autorelease
License: GPLv2+
Source: http://www.flyn.org/projects/%name/%{name}-%{version}.tar.gz
URL: http://www.flyn.org
Summary: A simple template system
Requires: zlib
# No more gcj in Fedora?
#BuildRequires: glib2-devel, zlib-devel, java-1.8.0-gcj-devel, libgcj-devel, junit
BuildRequires:  gcc
BuildRequires: glib2-devel, zlib-devel
BuildRequires: make

%description 
New is a template system, especially useful in conjunction with a 
simple text editor such as vi. The user maintains templates which 
may contain format strings. At run time, nf replaces the format 
strings in a template with appropriate values to create a new file.

For example, given the following template:


//   FILE: %%(FILE)
// AUTHOR: %%(FULLNAME)
//   DATE: %%(DATE)

// Copyright (C) 1999 %%(FULLNAME) %%(EMAIL)
// All rights reserved.
nf will create:


//   FILE: foo.cpp
// AUTHOR: W. Michael Petullo
//   DATE: 11 September 1999

// Copyright (C) 1999 W. Michael Petullo new@flyn.org
// All rights reserved.
on my computer.

The program understands plaintext or gziped template files.

The fmt-ptrn system also provides a shared library which allows a 
programmer access to nf's functionality. The system was developed to 
be light and fast. Its only external dependencies are the C library, 
glib2 and zlib.



%files 
%{_bindir}/*
%{_libdir}/libnewfmt-ptrn.so.1
%{_libdir}/libnewfmt-ptrn.so.%{version}
%{_libdir}/libnewtemplate.so.1
%{_libdir}/libnewtemplate.so.%{version}
%{_datadir}/fmt-ptrn
%{_mandir}/*/*
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README FAQ


%post
/sbin/ldconfig



%postun
/sbin/ldconfig


%package devel
Summary: Files needed to develop applications using fmt-ptrn's libraries
Requires: fmt-ptrn = %{version}-%{release}, glib2-devel, zlib-devel

%description devel
New is a template system, especially useful in conjunction with a 
simple text editor such as vi. The user maintains templates which 
may contain format strings. At run time, nf replaces the format 
strings in a template with appropriate values to create a new file. 
This package provides the libraries, include files, and other 
resources needed for developing applications using fmt-ptrn's API.



%files devel
%{_libdir}/pkgconfig/fmt-ptrn.pc
%{_includedir}/fmt-ptrn
%{_libdir}/libnewfmt-ptrn.so
%{_libdir}/libnewtemplate.so





#%package java
#Summary: Files needed to develop applications using fmt-ptrn's Java classes
#Group: Development/Libraries
#Requires: fmt-ptrn = %{version}-%{release}
#
#%description java
#New is a template system, especially useful in conjunction with a 
#simple text editor such as vi. The user maintains templates which 
#may contain format strings. At run time, nf replaces the format 
#strings in a template with appropriate values to create a new file. 
#This package provides the resources needed for developing applications 
#using fmt-ptrn's Java classes.
#
#
#
#%files java
#%defattr(-, root, root, -)
#%{_libdir}/libnewfmt-ptrnjni.so*
#%{_libdir}/libnewfmt-ptrnjava.so*
#%{_datadir}/java/*
#
#
#%post -n fmt-ptrn-java
#/sbin/ldconfig
#
#
#
#%postun -n fmt-ptrn-java
#/sbin/ldconfig


%prep


%setup -q


%build
 %configure  --disable-static --disable-java
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm -f ${RPM_BUILD_ROOT}%{_libdir}/libnewfmt-ptrn.la
rm -f ${RPM_BUILD_ROOT}%{_libdir}/libnewfmt-ptrnjni.la
rm -f ${RPM_BUILD_ROOT}%{_libdir}/libnewfmt-ptrnjava.la
rm -f ${RPM_BUILD_ROOT}%{_libdir}/libnewtemplate.la
# Delete the following 2 lines for building Java:
#rm -f ${RPM_BUILD_ROOT}%{_libdir}/libnewfmt-ptrnjni.*
#rm -f ${RPM_BUILD_ROOT}%{_datadir}/java/libnewfmt-ptrnjava.jar

%changelog
%autochangelog
