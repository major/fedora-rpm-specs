Name:       wv
Summary:    MSWord 6/7/8/9 binary file format to HTML converter
Version:    1.2.9
Release:    %autorelease
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:    GPL-2.0-or-later
URL:        http://www.abisource.com/downloads/wv/
Source:     http://www.abisource.com/downloads/wv/%{version}/wv-%{version}.tar.gz
Patch1:     wv-aarch64.patch
Patch2:     format-security.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires: glib2-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libxml2-devel
BuildRequires: ImageMagick-devel
BuildRequires: pkgconfig
BuildRequires: libgsf-devel >= 1.11.2
Provides:   wvware = %{version}-%{release}

%description
Wv is a program that understands the Microsoft Word 6/7/8/9
binary file format and is able to convert Word
documents into HTML, which can then be read with a browser.


%package        devel
Summary:        MSWord format converter - development files
Requires:       %{name} = %{version}-%{release}

%description    devel
Wv is a program that understands the Microsoft Word 6/7/8/9
binary file format and is able to convert Word
documents into HTML, which can then be read with a browser.
This package contains the development files


%prep
%setup -q
%patch -P1 -p1
%patch -P2 -p1

%build
%configure --disable-static

make %{?_smp_mflags}

%install
%make_install
find $RPM_BUILD_ROOT%{_libdir} -name "*.la" -exec rm -f {} \;


%ldconfig_scriptlets


%files
%doc COPYING README
%{_bindir}/wv*
%{_datadir}/wv
%{_mandir}/man1/*
%{_libdir}/libwv*.so.*

%files      devel
%{_includedir}/wv
%{_libdir}/libwv*.so
%{_libdir}/pkgconfig/*


%changelog
%autochangelog
