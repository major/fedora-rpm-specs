Name:           libXISF
Version:        0.2.5
Release:        %autorelease
Summary:        Library to load and write XISF format
License:        GPL-3.0-or-later
URL:            https://gitea.nouspiro.space/nou/libXISF
Source0:        %{url}/archive/v%{version}.tar.gz
# Backports from upstream to fix pkgconfig file and so fix deps
# https://gitea.nouspiro.space/nou/libXISF/commit/5dcc383090dc5e17982ee6f4371de700e1790320
Patch0:         0001-Fix-generating-pkgconfig-file.patch
# https://gitea.nouspiro.space/nou/libXISF/commit/0ddff094ef2a20bba5d749b23758471791a9d62a
Patch1:         0002-Fix-generating-pkgconfig-file.patch

BuildRequires:  cmake >= 3.14
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(pugixml)
BuildRequires:  pkgconfig(zlib)


%description
LibXISF is C++ library to load and save images in XISF format that
is native format PixInsight astronomical image processing program.
It implements XISF 1.0 specifications.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n libxisf

# remove bundled libraries
for d in "lz4" "pugixml" "zlib"
do
  rm -rf $d
done


%build
%cmake \
    -DBUILD_SHARED_LIBS=ON \
    -DUSE_BUNDLED_LIBS=OFF
%cmake_build


%install
%cmake_install


%check
%ctest


%files
%license LICENSE
%doc README.md
%{_libdir}/%{name}.so.0
%{_libdir}/%{name}.so.%{version}


%files devel
%{_includedir}/%{name}_global.h
%{_includedir}/libxisf.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/libxisf.pc


%changelog
%autochangelog
