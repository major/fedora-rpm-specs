%global repo util-dfm

Name:           deepin-util-dfm
Version:        1.3.47
Release:        %autorelease
Summary:        Utilities of deepin file manager
# the library is mainly under GPL-3.0-or-later, except:
# src/dfm-burn/3rdparty/udfclient: ClArtistic AND BSD-3-Clause AND BSD-4-Clause
License:        GPL-3.0-or-later AND ClArtistic AND BSD-3-Clause AND BSD-4-Clause
URL:            https://github.com/linuxdeepin/util-dfm
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz
Patch0:         https://github.com/linuxdeepin/util-dfm/pull/256.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  cmake(Dtk6Core)

BuildRequires:  boost-devel
BuildRequires:  pkgconfig(udisks2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(mount)
BuildRequires:  pkgconfig(libmediainfo)
BuildRequires:  pkgconfig(libisoburn-1)
BuildRequires:  pkgconfig(liblucene++)
BuildRequires:  pkgconfig(liblucene++-contrib)

%description
Deepin File Manager utilities (libdfm-io, libdfm-mount and libdfm-burn)
developed by UnionTech Software Technology Co., Ltd

%package -n     dfm6-burn
Summary:        The dfm6-burn libraries
%description -n dfm6-burn
A Toolkit of dfm6-burn.

%package -n     dfm6-burn-devel
Summary:        Development files for dfm6-burn
Requires:       dfm6-burn%{?_isa} = %{version}-%{release}
%description -n dfm6-burn-devel
This package contains development files for dfm6-burn.

%package -n     dfm6-io
Summary:        The dfm6-io libraries
%description -n dfm6-io
A Toolkit of dfm6-io.

%package -n     dfm6-io-devel
Summary:        Development files for dfm6-io
Requires:       dfm6-io%{?_isa} = %{version}-%{release}
%description -n dfm6-io-devel
This package contains development files for dfm6-io.

%package -n     dfm6-mount
Summary:        The dfm6-mount libraries
%description -n dfm6-mount
A Toolkit of dfm6-mount.

%package -n     dfm6-mount-devel
Summary:        Development files for dfm6-mount
Requires:       dfm6-mount%{?_isa} = %{version}-%{release}
%description -n dfm6-mount-devel
This package contains development files for dfm6-mount.

%package -n     dfm6-search
Summary:        The dfm6-search libraries
%description -n dfm6-search
A Toolkit of dfm6-search.

%package -n     dfm6-search-devel
Summary:        Development files for dfm6-search
Requires:       dfm6-search%{?_isa} = %{version}-%{release}
# https://github.com/linuxdeepin/util-dfm/blob/master/misc/dfm-search/dfm-searchConfig.cmake.in
Requires:       boost-devel
Requires:       pkgconfig(liblucene++)
Requires:       pkgconfig(liblucene++-contrib)
%description -n dfm6-search-devel
This package contains development files for dfm6-search.

%prep
%autosetup -p1 -n %{repo}-%{version}

sed -i 's|Boostsystem Threads||' misc/dfm-search/dfm-search.pc.in

%build
%cmake -DVERSION=%{version}
%cmake_build

%install
%cmake_install

%files -n dfm6-burn
%license LICENSES/*
%doc README.md
%{_libdir}/libdfm6-burn.so.1*

%files -n dfm6-burn-devel
%{_includedir}/dfm6-burn/
%{_libdir}/libdfm6-burn.so
%{_libdir}/pkgconfig/dfm6-burn.pc
%{_libdir}/cmake/dfm6-burn/

%files -n dfm6-io
%license LICENSES/*
%doc README.md
%{_libdir}/libdfm6-io.so.1*

%files -n dfm6-io-devel
%{_includedir}/dfm6-io/
%{_libdir}/libdfm6-io.so
%{_libdir}/pkgconfig/dfm6-io.pc
%{_libdir}/cmake/dfm6-io/

%files -n dfm6-mount
%license LICENSES/*
%doc README.md
%{_libdir}/libdfm6-mount.so.1*

%files -n dfm6-mount-devel
%{_includedir}/dfm6-mount/
%{_libdir}/libdfm6-mount.so
%{_libdir}/pkgconfig/dfm6-mount.pc
%{_libdir}/cmake/dfm6-mount/

%files -n dfm6-search
%license LICENSES/*
%doc README.md
%{_libdir}/libdfm6-search.so.1*
%{_libexecdir}/dfm6-search-client

%files -n dfm6-search-devel
%{_includedir}/dfm6-search/
%{_libdir}/libdfm6-search.so
%{_libdir}/pkgconfig/dfm6-search.pc
%{_libdir}/cmake/dfm6-search/

%changelog
%autochangelog
