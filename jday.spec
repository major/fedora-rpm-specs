Name:		jday
Version:        2.4
Release:        %autorelease
Summary:        A simple command to convert calendar dates to julian dates
License:        BSD-3-Clause
URL:            http://sourceforge.net/projects/jday/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch:		configure.patch

# https://bugzilla.redhat.com/797815
Conflicts: netatalk

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:  gcc-c++
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:  make

%description
A simple command to convert calendar dates to julian dates. Quite
useful in timing situations where you need elapsed time between dates.
Also useful for astronomy applications.

%package devel
Summary:        Development files for jday
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Contains library and header files for developing applications that use
jday.

%prep
%setup -q
%autopatch


%build
autoreconf --install
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%doc ChangeLog README AUTHORS NEWS
%{_bindir}/dbd
%{_bindir}/j2d
%{_bindir}/jday
%{_mandir}/man1/jday.1*
%{_libdir}/libjday.so.2.0.4
%{_libdir}/libjday.so.2

%files devel
%{_includedir}/jday.h
%{_libdir}/libjday.so
%{_libdir}/pkgconfig/jday.pc

%changelog
%autochangelog
