%global repo util-dfm

Name:           deepin-util-dfm
Version:        1.3.9
Release:        %autorelease
Summary:        Utilities of deepin file manager
# the library is mainly under GPL-3.0-or-later, except:
# src/dfm-burn/3rdparty/udfclient: ClArtistic AND BSD-3-Clause AND BSD-4-Clause
License:        GPL-3.0-or-later AND ClArtistic AND BSD-3-Clause AND BSD-4-Clause
URL:            https://github.com/linuxdeepin/util-dfm
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Widgets)

BuildRequires:  pkgconfig(udisks2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(mount)
BuildRequires:  pkgconfig(libmediainfo)
BuildRequires:  pkgconfig(libisoburn-1)

%description
A Toolkit of libdfm-io, libdfm-mount and libdfm-burn, developed by UnionTech
Software Technology Co., Ltd.

%package -n     dfm-burn
Summary:        The dfm-burn libraries

%description -n dfm-burn
A Toolkit of dfm-burn.

%package -n     dfm-burn-devel
Summary:        Development tools for dfm-burn
Requires:       dfm-burn%{?_isa} = %{version}-%{release}

%description -n dfm-burn-devel
This package contains development files for dfm-burn.

%package -n     dfm-io
Summary:        The dfm-io libraries

%description -n dfm-io
A Toolkit of dfm-io.

%package -n     dfm-io-devel
Summary:        Development tools for dfm-io
Requires:       dfm-io%{?_isa} = %{version}-%{release}

%description -n dfm-io-devel
This package contains development files for dfm-io.

%package -n     dfm-mount
Summary:        The dfm-mount libraries

%description -n dfm-mount
A Toolkit of dfm-mount.

%package -n     dfm-mount-devel
Summary:        Development tools for dfm-mount
Requires:       dfm-mount%{?_isa} = %{version}-%{release}

%description -n dfm-mount-devel
This package contains development files for dfm-mount.

%prep
%autosetup -p1 -n %{repo}-%{version}
# use Fedora build flags
sed -i 's/-O0//; s/-O3//' \
    src/dfm-io/CMakeLists.txt \
    src/dfm-burn/CMakeLists.txt

%build
%cmake \
    -GNinja \
    -DPROJECT_VERSION=%{version} \
%cmake_build

%install
%cmake_install

%files -n dfm-burn
%license LICENSES/*
%doc README.md
%{_libdir}/libdfm-burn.so.1
%{_libdir}/libdfm-burn.so.1.0.0

%files -n dfm-io
%license LICENSES/*
%doc README.md
%{_libdir}/libdfm-io.so.1
%{_libdir}/libdfm-io.so.1.0.0

%files -n dfm-mount
%license LICENSES/*
%doc README.md
%{_libdir}/libdfm-mount.so.1
%{_libdir}/libdfm-mount.so.1.0.0

%files -n dfm-burn-devel
%{_includedir}/dfm-burn/
%{_libdir}/libdfm-burn.so
%{_libdir}/pkgconfig/dfm-burn.pc
%{_libdir}/cmake/dfm-burn/

%files -n dfm-io-devel
%{_includedir}/dfm-io/
%{_libdir}/libdfm-io.so
%{_libdir}/pkgconfig/dfm-io.pc
%{_libdir}/cmake/dfm-io/

%files -n dfm-mount-devel
%{_includedir}/dfm-mount/
%{_libdir}/libdfm-mount.so
%{_libdir}/pkgconfig/dfm-mount.pc
%{_libdir}/cmake/dfm-mount/

%changelog
%autochangelog
