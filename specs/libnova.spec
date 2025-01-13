%global gittag v0.16

Name:       libnova
Version:    0.16.0
Release:    %autorelease
Summary:    Libnova is a general purpose astronomy & astrodynamics library
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:    LicenseRef-Callaway-LGPLv2+
URL:        http://sourceforge.net/projects/libnova/
# Sources cloned from upstream tag with attached script
Source0:    %{name}-%{gittag}.tar.zst
Source1:    download_sftag.sh

BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make

%description
Libnova is a general purpose, double precision, celestial mechanics, 
astrometry and astrodynamics library


%package devel
Summary:    Development files for libnova
Requires:   %{name} = %{version}-%{release}

%description devel
Contains library and header files for libnova


%prep
%setup -q -n %{name}-%{gittag}


%build
autoreconf -vif
%configure --disable-static
make CFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -delete


%files
%doc ChangeLog README AUTHORS NEWS COPYING
%{_libdir}/libnova-0.16.so.0.0.0
%{_libdir}/libnova-0.16.so.0
%{_bindir}/libnovaconfig

%files devel
%doc COPYING examples/*.c
%{_includedir}/libnova
%{_libdir}/libnova.so


%changelog
%autochangelog
