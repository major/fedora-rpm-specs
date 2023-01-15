Name:           flickcurl
Version:        1.26
Release:        19%{?dist}
Summary:        C library for the Flickr API
License:        LGPL-2.1-or-later OR GPL-2.0-or-later OR Apache-2.0
URL:            http://librdf.org/flickcurl
Source0:        http://download.dajobe.org/%{name}/%{name}-%{version}.tar.gz
Patch0: flickcurl-configure-c99.patch
BuildRequires:  chrpath
BuildRequires:  libcurl-devel
BuildRequires:  libxml2-devel
BuildRequires:  raptor2-devel
BuildRequires:  gcc
BuildRequires: make

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
* Fri Jan 13 2023 Florian Weimer <fweimer@redhat.com> - 1.26-19
- Port configure script to C99

* Tue Dec 06 2022 Michael J Gruber <mjg@fedoraproject.org> - 1.26-18
- SPDX migration

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 08 2018 Michael J Gruber <mjg@fedoraproject.org> - 1.26-8
- Adjust to new guidelines (BR gcc)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Aug 19 2014 Christopher Meng <rpm@cicku.me> - 1.26-1
- Update to 1.26

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Sep 30 2013 Christopher Meng <rpm@cicku.me> - 1.25-1
- Update to 1.25

* Sun Aug 25 2013 Christopher Meng <rpm@cicku.me> - 1.24-1
- Update to new version.
- SPEC cleanup and update the description.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.22-1
- Update to 1.22, build against raptor2 (bz#838709).

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed May 05 2010 Rakesh Pandit <rakesh@fedoraproject.org> - 1.18-1
- Updated to 1.18

* Sat Jan 30 2010 Rakesh Pandit <rakesh@fedoraproject.org> - 1.16-1
- Updated to 1.16

* Thu Dec 03 2009 Rakesh Pandit <rakesh@fedoraproject.org> - 1.14-1
- Updated to 1.14

* Thu Aug 06 2009 Rakesh Pandit <rakesh@fedoraproject.org> - 1.13-1
- Updated to 1.13

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 24 2009 Rakesh Pandit <rakesh@fedoraproject.org> 1.10-3
- Added pkgconfig as devel sub package BR
- Fixed %%files folder *gtk-doc/html ownership

* Wed May 06 2009 Rakesh Pandit <rakesh@fedoraproject.org> 1.10-2
- Added raptor-devel require.

* Wed May 06 2009 Rakesh Pandit <rakesh@fedoraproject.org> 1.10-1
- Initial package
