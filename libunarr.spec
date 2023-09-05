Name:           libunarr
Version:        1.1.0
Release:        %autorelease
Summary:        Decompression library for rar, tar and zip archives

License:        LGPLv3+
URL:            https://github.com/selmf/unarr
Source0:        %{url}/releases/download/v%{version}/unarr-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  gcc

BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(zlib)

%description
(lib)unarr is a decompression library for RAR, TAR, ZIP and 7z* archives.

It was forked from unarr, which originated as a port of the RAR extraction
features from The Unarchiver project required for extracting images from comic
book archives. Zeniko wrote unarr as an alternative to libarchive which didn't
have support for parsing filters or solid compression at the time.

While (lib)unarr was started with the intent of providing unarr with a proper
cmake based build system suitable for packaging and cross-platform
development, it's focus has now been extended to provide code maintenance and
to continue the development of unarr, which no longer is maintained.


%package        devel
Summary:        Development files for %{name}

Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.


%prep
%autosetup -n unarr-%{version} -p1

# wrong-file-end-of-line-encoding fix
sed -i 's/\r$//' README.md


%build
%cmake
%cmake_build


%install
%cmake_install


%files
%license COPYING
%doc CHANGELOG.md README.md AUTHORS
%{_libdir}/%{name}.so.1*

%files devel
%{_includedir}/unarr.h
%{_libdir}/%{name}.so
%{_libdir}/cmake/unarr/unarr-*.cmake
%{_libdir}/pkgconfig/%{name}.pc


%changelog
%autochangelog
