%global gitdate       20260129
%global commit        3e96cfe21771d282b9caba2959145fc2835bd9da
%global short_commit  %(c="%{commit}"; echo ${c:0:7})

Name:           deepin-image-editor
Version:        6.5.2^%{gitdate}git%{short_commit}
Release:        %autorelease
Summary:        Public library for deepin-image-viewer and deepin-album
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/image-editor
Source0:        %{url}/archive/%{commit}/%{name}-%{short_commit}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6SvgWidgets)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6LinguistTools)

BuildRequires:  pkgconfig(dtk6widget)
BuildRequires:  pkgconfig(dtk6core)
BuildRequires:  pkgconfig(dtk6gui)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libmediainfo)
BuildRequires:  pkgconfig(dfm6-io)

BuildRequires:  libtiff-devel
BuildRequires:  ffmpegthumbnailer-devel

%description
%{summary}.

%package -n     libimageviewer6
Summary:        The libimageviewer6 library

%description -n libimageviewer6
This package contains the libraries for Deepin Image editor.

%package -n     libimageviewer6-devel
Summary:        Development files for libimageviewer6
Requires:       libimageviewer6%{?_isa} = %{version}-%{release}

%description -n libimageviewer6-devel
This package contains development files for libimageviewer6.

%package -n     libimagevisualresult6
Summary:        The libimagevisualresult6 library
Requires:       libimagevisualresult6-data%{?_isa} = %{version}-%{release}

%description -n libimagevisualresult6
This package contains the libraries for Deepin Image editor.

%package -n     libimagevisualresult6-devel
Summary:        Development files for libimagevisualresult6
Requires:       libimagevisualresult6%{?_isa} = %{version}-%{release}

%description -n libimagevisualresult6-devel
This package contains development files for libimagevisualresult6.

%package -n     libimagevisualresult6-data
Summary:        Data files for libimagevisualresult6
Requires:       libimagevisualresult6%{?_isa} = %{version}-%{release}

%description -n libimagevisualresult6-data
This package provides data files for libimagevisualresult6.

%prep
%autosetup -p1 -C

%build
%cmake -GNinja -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
%cmake_install

%find_lang libimageviewer6 --with-qt --all-name

%files -n libimageviewer6 -f libimageviewer6.lang
%license LICENSE.txt
%doc README.md
%{_libdir}/libimageviewer6.so.0.1*
%dir %{_datadir}/libimageviewer6

%files -n libimageviewer6-devel
%{_includedir}/libimageviewer6/
%{_libdir}/libimageviewer6.so
%{_libdir}/pkgconfig/libimageviewer6.pc

%files -n libimagevisualresult6
%license LICENSE.txt
%doc README.md
%{_libdir}/libimagevisualresult6.so.0.1*

%files -n libimagevisualresult6-devel
%{_includedir}/libimagevisualresult6/
%{_libdir}/libimagevisualresult6.so
%{_libdir}/pkgconfig/libimagevisualresult6.pc

%files -n libimagevisualresult6-data
%dir %{_datadir}/libimagevisualresult6
%{_datadir}/libimagevisualresult6/filter_cube/

%changelog
%autochangelog
