Name:           chafa
Version:        1.18.1
Release:        %autorelease
%global sum     Image-to-text converter for terminal
Summary:        %{sum}
License:        LGPL-3.0-or-later
URL:            https://hpjansson.org/chafa/
Source0:        https://github.com/hpjansson/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz

ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  libavif-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  libwebp-devel
BuildRequires:  make

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}


%description
Chafa is a command-line utility that converts all kinds of images, including
animated image formats like GIFs, into ANSI/Unicode character output that can
be displayed in a terminal.

It is highly configurable, with support for alpha transparency and multiple
color modes and color spaces, combining a range of Unicode characters for
optimal output.


%package libs
Summary:        %{sum} (library)

# Version in libnsgif/README-chafa
Provides:       bundled(libnsgif) = 0.2.1^chafa
# Version in lodepng/lodepng.h
Provides:       bundled(lodepng) = 20220109

%description libs
Shared library for %{name}. Chafa provides a high-performance C API for
converting images to terminal graphics.


%package static
Summary:        %{sum} (static library)

%description static
Static library for %{name}. Chafa provides a high-performance C API for
converting images to terminal graphics.


%package devel
Summary:        %{sum} (development files)
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}, such as headers, needed to develop applications
using the Chafa library.


%package doc
Summary:        %{sum} (documentation)
Recommends:     %{name}-devel
BuildArch:      noarch

%description doc
Documentation for %{name}, such as HTML reference and developer guides.


%prep
%autosetup


%build
autoreconf -ivf
%configure --disable-rpath
%make_build


%install
%make_install
find %{buildroot} -name "*.la" -delete


%check
%make_build check


%files
%doc AUTHORS README* NEWS
%license COPYING.LESSER
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%files libs
%doc AUTHORS
%license COPYING.LESSER
%{_libdir}/lib%{name}.so.0
%{_libdir}/lib%{name}.so.0.*

%files static
%doc AUTHORS
%license COPYING.LESSER
%{_libdir}/lib%{name}.a

%files devel
%doc AUTHORS
%license COPYING.LESSER
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/lib%{name}.so
%{_libdir}/%{name}/include/chafaconfig.h

%files doc
%doc AUTHORS
%license COPYING.LESSER
%doc %{_datadir}/gtk-doc/html/%{name}


%changelog
%autochangelog
