%bcond check 1
%global repo image-editor

Name:           deepin-image-editor
Version:        1.0.46
Release:        %autorelease
Summary:        Public library for deepin-image-viewer and deepin-album
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/image-editor
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz
# fix to support the detection of dtkwidget version for fedora
Patch0:         fix-for-fedora.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5LinguistTools)

BuildRequires:  pkgconfig(dtkwidget)
BuildRequires:  pkgconfig(dtkcore)
BuildRequires:  pkgconfig(dtkgui)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libmediainfo)
BuildRequires:  pkgconfig(dfm-io)
BuildRequires:  pkgconfig(libffmpegthumbnailer)
BuildRequires:  libtiff-devel
BuildRequires:  freeimage-devel

%if %{with check}
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  dbus-x11
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  pkgconfig(gio-qt)
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  gtest-devel
BuildRequires:  gmock-devel
BuildRequires:  libXext-devel
BuildRequires:  libexif-devel
BuildRequires:  pkgconfig(udisks2-qt5)
BuildRequires:  libasan
BuildRequires:  libubsan
%endif

%description
%{summary}.

%package -n     libimageviewer
Summary:        The libimageviewer library

%description -n libimageviewer
This package contains the libraries for Deepin Image editor.

%package -n     libimageviewer-devel
Summary:        Development files for libimageviewer
Requires:       libimageviewer%{?_isa} = %{version}-%{release}

%description -n libimageviewer-devel
This package contains development files for libimageviewer.

%package -n     libimagevisualresult
Summary:        The libimagevisualresult library
Requires:       libimagevisualresult-data%{?_isa} = %{version}-%{release}

%description -n libimagevisualresult
A Toolkit of libimagevisualresult.

%package -n     libimagevisualresult-devel
Summary:        Development files for libimagevisualresult
Requires:       libimagevisualresult%{?_isa} = %{version}-%{release}

%description -n libimagevisualresult-devel
This package contains development files for libimagevisualresult.

%package -n     libimagevisualresult-data
Summary:        Data files for libimagevisualresult
Requires:       libimagevisualresult%{?_isa} = %{version}-%{release}

%description -n libimagevisualresult-data
This package provides data files for libimagevisualresult.

%prep
%autosetup -p1 -n %{repo}-%{version}
# use Fedora build flags
sed -i '/-O3/d' \
    libimageviewer/CMakeLists.txt \
    libimagevisualresult/CMakeLists.txt

sed -i 's/CMAKE_CXX_STANDARD 11/CMAKE_CXX_STANDARD 17/' tests/CMakeLists.txt
sed -i 's/std=c++11/std=c++17/' tests/CMakeLists.txt

%build
# TODO: Please submit an issue to upstream (rhbz#2380536)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -GNinja -DCMAKE_BUILD_TYPE=RelWithDebInfo \
%if %{with check}
    -DDOTEST=ON
%endif
%cmake_build

%install
%cmake_install
rm %{buildroot}%{_datadir}/libimagevisualresult/filter_cube/null.dat
%find_lang libimageviewer --all-name --with-qt

%if %{with check}
%check
# memory leaks and core dumped in s390x
%ifnarch s390x
xvfb-run -a dbus-launch --exit-with-session bash -c "%{_vpath_builddir}/tests/image-editor-test ||:"
%endif
%endif

%files -n libimageviewer -f libimageviewer.lang
%license LICENSE.txt
%doc README.md
%{_libdir}/libimageviewer.so.0.1*
%dir %{_datadir}/libimageviewer
%dir %{_datadir}/libimageviewer/translations

%files -n libimageviewer-devel
%{_includedir}/libimageviewer/
%{_libdir}/libimageviewer.so
%{_libdir}/pkgconfig/libimageviewer.pc

%files -n libimagevisualresult
%license LICENSE.txt
%doc README.md
%{_libdir}/libimagevisualresult.so.0.1*

%files -n libimagevisualresult-devel
%{_includedir}/libimagevisualresult/
%{_libdir}/libimagevisualresult.so
%{_libdir}/pkgconfig/libimagevisualresult.pc

%files -n libimagevisualresult-data
%dir %{_datadir}/libimagevisualresult
%{_datadir}/libimagevisualresult/filter_cube/

%changelog
%autochangelog
