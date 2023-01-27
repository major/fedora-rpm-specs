%bcond_with devel

# This spec file has been automatically updated
Version:	1.0
Release: %{?autorelease}%{!?autorelease:1%{?dist}}
Name: libunistring1.0
Summary: Compatibility version of GNU Unicode string library
License: GPL-2.0-or-later or LGPL-3.0-or-later
URL: https://www.gnu.org/software/libunistring/
Source0: https://ftp.gnu.org/gnu/libunistring/libunistring-%{version}.tar.xz
BuildRequires: gcc
BuildRequires: make
Provides: bundled(gnulib)
Conflicts: libunistring < 1.1
Provides: deprecated()

%description
This portable C library implements Unicode string types in three flavours:
(UTF-8, UTF-16, UTF-32), together with functions for character processing
(names, classifications, properties) and functions for string processing
(iteration, formatted output, width, word breaks, line breaks, normalization,
case folding and regular expressions).

This package contains the libunistring library version 1.0 and is
intended for compatibility reasons only.  Users are advised to update
to a newer version of libunistring.

%if %{with devel}
%package devel
Summary: GNU Unicode string library - development files
Requires: %{name}%{?_isa} = %{version}-%{release}
Conflicts: libunistring-devel
Provides: deprecated()

%description devel
Development files for programs using libunistring.

This package contains the libunistring library version 1.0 and is
intended for compatibility reasons only.  Users are advised to update
to a newer version of libunistring.
%endif

%prep
%autosetup -n libunistring-%{version}

%build
%configure --disable-static --disable-rpath
%make_build

%install
%make_install
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm -f $RPM_BUILD_ROOT%{_libdir}/libunistring.la
# Move staged docs so not picked up by %%doc in main package
mv $RPM_BUILD_ROOT%{_datadir}/doc/libunistring __doc

%if !%{with devel}
rm -f $RPM_BUILD_ROOT%{_infodir}/libunistring.info*
rm -f $RPM_BUILD_ROOT%{_libdir}/libunistring.so
rm -fr $RPM_BUILD_ROOT%{_includedir}/unistring
rm -f $RPM_BUILD_ROOT%{_includedir}/*.h
%endif

%files
%license COPYING COPYING.LIB
%doc AUTHORS NEWS README
%{_libdir}/libunistring.so.2*

%if %{with devel}
%files devel
%doc HACKING DEPENDENCIES THANKS ChangeLog
%doc __doc/*
%{_infodir}/libunistring.info*
%{_libdir}/libunistring.so
%{_includedir}/unistring
%{_includedir}/*.h
%endif

%changelog
%autochangelog

