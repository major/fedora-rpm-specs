Name:           flickcurl
Version:        1.26
Release:        %autorelease
Summary:        C library for the Flickr API
License:        LGPL-2.1-or-later OR GPL-2.0-or-later OR Apache-2.0
URL:            http://librdf.org/flickcurl
Source0:        http://download.dajobe.org/%{name}/%{name}-%{version}.tar.gz
Patch0: flickcurl-configure-c99.patch
Patch1: flickcurl-gcc14.patch
BuildRequires:  chrpath
BuildRequires:  libcurl-devel
BuildRequires:  libxml2-devel
BuildRequires:  raptor2-devel
BuildRequires:  gcc
BuildRequires: make

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%description
Flickcurl is a C library for the Flickr API, handling creating the requests, 
signing, token management, calling the API, marshalling request parameters 
and decoding responses. It uses libcurl to call the REST web service and 
libxml2 to manipulate the XML responses. Flickcurl supports all of the API 
including the functions for photo/video uploading, browsing, searching, 
adding and editing comments, groups, notes, photosets, categories, activity, 
blogs, favorites, places, tags, machine tags, institutions, pandas and 
photo/video metadata. It also includes a program flickrdf to turn photo 
metadata, tags, machine tags and places into an RDF triples description.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libcurl-devel%{?_isa}
Requires:       libxml2-devel%{?_isa}
Requires:       raptor2-devel%{?_isa}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete -print

#removing rpaths with chrpath
chrpath --delete %{buildroot}%{_bindir}/flickcurl
chrpath --delete %{buildroot}%{_bindir}/flickrdf

%ldconfig_scriptlets

%files
%doc AUTHORS README NOTICE
%license LICENSE-2.0.txt LICENSE.html
%{_bindir}/flickcurl
%{_bindir}/flickrdf
%{_libdir}/libflickcurl.so.*
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/flickrdf.1*

%files devel
%license COPYING COPYING.LIB
%doc coverage.html ChangeLog README.html NEWS.html
%{_bindir}/flickcurl-config
%{_datadir}/gtk-doc/html/*
%{_includedir}/*
%{_libdir}/libflickcurl.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man1/%{name}-config.1*

%changelog
%autochangelog
