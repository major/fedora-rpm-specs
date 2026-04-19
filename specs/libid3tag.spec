Name:           libid3tag
Version:        0.16.4
Release:        %autorelease
Summary:        ID3 tag manipulation library

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://codeberg.org/tenacityteam/libid3tag
Source0:        %url/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  gperf
BuildRequires:  zlib-devel >= 1.1.4

%description
libid3tag is a library for reading and (eventually) writing ID3 tags,
both ID3v1 and the various versions of ID3v2.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
ID3 tag library development files.


%prep
%autosetup -p1 -n %{name}

%build
%cmake
%cmake_build


%install
%cmake_install


%ldconfig_scriptlets

%files
%doc CHANGES CREDITS README.md
%license COPYING COPYRIGHT
%{_libdir}/libid3tag.so.0*

%files devel
%{_includedir}/id3tag.h
%{_libdir}/libid3tag.so
%{_libdir}/cmake/id3tag/
%{_libdir}/pkgconfig/id3tag.pc


%changelog
%autochangelog
