Name:           webp-pixbuf-loader
Version:        0.2.7
Release:        %autorelease
Summary:        WebP image loader for GTK+ applications

License:        LGPL-2.0-or-later
URL:            https://github.com/aruiz/webp-pixbuf-loader
Source0:        https://github.com/aruiz/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  libwebp-devel

Requires:       gdk-pixbuf2%{?_isa}

%description
webp-pixbuf-loader contains a plugin to load WebP images in GTK+ applications

%prep
%autosetup

%build
%meson -Dgdk_pixbuf_query_loaders_path=gdk-pixbuf-query-loaders-%{__isa_bits}
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE.LGPL-2
%{_libdir}/gdk-pixbuf-2.0/*/loaders/libpixbufloader-webp.so
%{_datadir}/thumbnailers/webp-pixbuf.thumbnailer

%changelog
%autochangelog
