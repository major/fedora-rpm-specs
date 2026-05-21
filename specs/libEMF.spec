Summary:	A library for generating Enhanced Metafiles
Summary(pl):	Biblioteka do generowania plików w formacie Enhanced Metafile
Name:		libEMF
Version:	1.0.14
Release:	%autorelease
# include/libEMF/emf.h: LGPL-2.1-or-later
# libemf/libemf.{cpp,h}: LGPL-2.1-or-later
# src/printemf.c: GPL-2.0-or-later
License:	LGPL-2.1-or-later AND GPL-2.0-or-later
URL:		http://libemf.sourceforge.net/
Source0:	https://downloads.sourceforge.net/project/libemf/libemf/%{version}/libemf-%{version}.tar.gz
BuildRequires:	gcc-c++
BuildRequires: make

%description
libEMF is a library for generating Enhanced Metafiles on systems which
don't natively support the ECMA-234 Graphics Device Interface
(GDI). The library is intended to be used as a driver for other
graphics programs such as Grace or gnuplot. Therefore, it implements a
very limited subset of the GDI.

%description -l pl
libEMF to biblioteka do generowania plików w formacie Enhanced
Metafile na systemach nie obsługujących natywnie systemu graficznego
ECMA-234 GDI. Biblioteka ma służyć jako sterownik dla innych programów
graficznych, takich jak Grace czy gnuplot. Z tego powodu ma
zaimplementowany bardzo ograniczony podzbiór GDI.

%package devel
Summary:	libEMF header files
Summary(pl):	Pliki nagłówkowe libEMF
Requires:	%{name}%{_isa} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
libEMF header files.

%description devel -l pl
Pliki nagłówkowe libEMF.

%prep
%autosetup -n libemf-%{version} -p1

%build
%configure \
	--disable-static \
	--enable-editing

%make_build

%install
export CPPROG="cp -p"
%make_install
rm %{buildroot}%{_libdir}/libEMF.la

%check
%make_build check

%files
%license COPYING COPYING.LIB
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/printemf
%{_libdir}/libEMF.so.1{,.*}

%files devel
%doc doc/doxygen-doc/html/*
%{_libdir}/libEMF.so
%{_includedir}/libEMF

%changelog
%autochangelog
