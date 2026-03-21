%global commit0 850bdb747b234d6a89f9547fbc6dfa1cf2a6722d
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20251204

Name:           libspatialaudio
Version:        4.0
Release:        %autorelease
Summary:        Ambisonic encoding / decoding and binauralization library

License:        LGPL-2.1-or-later
URL:            https://github.com/videolabs/libspatialaudio
Source0:        %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
Patch0:           0001-Drop-config.h-install.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libmysofa)


%description
libspatialaudio is an open-source and cross-platform C++ library for
Ambisonic encoding and decoding, filtering and binaural rendering. It is
targetted to render High-Order Ambisonic (HOA) and VR/3D audio samples
in multiple environments, from headphones to classic loudspeakers. Its
binaural rendering can be used for classical 5.1/7.1 spatial channels
as well as Ambisonics inputs.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# sofa_hrtf.h includes mysofa.h
Requires:       pkgconfig(libmysofa)

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{name}-%{commit0}


%build
%cmake \
  -DBUILD_STATIC_LIBS=OFF

%cmake_build


%install
%cmake_install



%files
%license LICENSE
%doc README.md
%{_libdir}/libspatialaudio.so.2*

%files devel
%{_includedir}/*
%{_libdir}/libspatialaudio.so
%{_libdir}/pkgconfig/spatialaudio.pc


%changelog
%autochangelog
