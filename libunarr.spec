%global forgeurl https://github.com/selmf/%{upstream_package_name}
%global tag v%{version}
%global upstream_package_name unarr

Name:           lib%{upstream_package_name}
Version:        1.1.1
%forgemeta
Release:        %autorelease
Summary:        Decompression library for rar, tar and zip archives

License:        LGPL-3.0-or-later
URL:            %{forgeurl}
Source0:        %{forgesource}

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
%forgeautosetup -p1

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
%{_includedir}/%{upstream_package_name}.h
%{_libdir}/%{name}.so
%{_libdir}/cmake/%{upstream_package_name}/%{upstream_package_name}-*.cmake
%{_libdir}/pkgconfig/%{name}.pc


%changelog
%autochangelog
