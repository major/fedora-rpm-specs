%define __cmake_in_source_build 1

Name:		stratagus
Summary:	Real-time strategy gaming engine
Version:	3.3.2
Release:	%autorelease
License:	GPL-2.0-only
URL:		https://github.com/Wargus/Stratagus
Source0:	https://github.com/Wargus/Stratagus/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:		stratagus-0001-Fix-binaries-path.patch
BuildRequires:	SDL2-devel
BuildRequires:	SDL2_image-devel
BuildRequires:	SDL2_mixer-devel
BuildRequires:	bzip2-devel
BuildRequires:	cmake
BuildRequires:	compat-lua-devel
BuildRequires:	compat-tolua++-devel
BuildRequires:	dos2unix
BuildRequires:	gcc-c++
BuildRequires:	libmng-devel
BuildRequires:	libpng-devel
BuildRequires:	libtheora-devel
BuildRequires:	libvorbis-devel
BuildRequires:	make
BuildRequires:	sqlite-devel
BuildRequires:	zlib-devel
Provides:	bundled(guichan)


%description
Stratagus is a free cross-platform real-time strategy gaming engine. It
includes support for playing over the internet/LAN, or playing a
computer opponent. The engine is configurable and can be used to create
games with a wide-range of features specific to your needs.


%package devel
Summary:       Development files for %{name}
BuildArch:     noarch
Requires:      %{name} = %{version}-%{release}

%description devel
This package contains development files for %{name}.


%prep
%autosetup -p1
iconv -f iso8859-1 -t utf8 doc/guichan-copyright.txt > doc/guichan-copyright.utf8 && mv -f doc/guichan-copyright.{utf8,txt}

%build
mkdir build
pushd build
%cmake .. -DENABLE_DEV=ON -DLUA_INCLUDE_DIR=%{_includedir}/lua-5.1
make %{?_smp_mflags}
popd


%install
make install -C build DESTDIR=%{buildroot}


%files
%license COPYING
%doc README.md doc/
%{_bindir}/%{name}
%{_bindir}/png2%{name}


%files devel
%{_includedir}/%{name}*

%changelog
%autochangelog
