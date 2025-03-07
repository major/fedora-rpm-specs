%global sover 1

Name:           dtkmultimedia
Version:        6.0.0
Release:        %autorelease
Summary:        Development Tool Kit Multimedia

# most of the files are under GPL-2.0-or-later AND LGPL-3.0-or-later, except:

# src/ocr/ppocr/postprocess_op.cpp: Apache-2.0
# src/ocr/ppocr/postprocess_op.h: Apache-2.0
# src/ocr/ppocr/utility.cpp: Apache-2.0
# src/ocr/ppocr/utility.h: Apache-2.0

# src/ocr/ppocr/clipper.cpp: BSL-1.0
# src/ocr/ppocr/clipper.hpp: BSL-1.0
License:        Apache-2.0 AND BSL-1.0 AND GPL-2.0-or-later AND LGPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dtkmultimedia
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Port to FFmpeg 7
# https://github.com/linuxdeepin/dtkmultimedia/pull/61
Patch0:         dtkmultimedia-ffmpeg7.patch
Patch1:         https://github.com/linuxdeepin/dtkmultimedia/pull/67.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6MultimediaWidgets)

BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Widget)

BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(ncnn)
BuildRequires:  pkgconfig(opencv)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)

BuildRequires:  systemd-devel
BuildRequires:  pkgconfig(mpv)
BuildRequires:  pkgconfig(libffmpegthumbnailer)
BuildRequires:  libusb1-devel
BuildRequires:  portaudio-devel
BuildRequires:  libv4l-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  libXtst-devel

BuildRequires:  doxygen

%description
Development Tool Kit (DtkMultimedia) is the base development tool of all C++/Qt
Developer work on Deepin.

%package -n     libdtk6multimedia
Summary:        Deepin Multimedia Toolkit libraries

%description -n libdtk6multimedia
Deepin Multimedia Toolkit is the base devlopment tool of all C++/Qt Developer
work on Deepin.

%package -n     libdtk6multimediawidgets
Summary:        Deepin Multimedia Widgets Toolkit libraries

%description -n libdtk6multimediawidgets
Deepin Multimedia Widgets Toolkit is the base devlopment tool of all C++/Qt
Developer work on Deepin.

%package -n     libdtk6ocr
Summary:        Deepin Multimedia OCR Toolkit libraries
Requires:       libdtk6ocr-data = %{version}-%{release}

%description -n libdtk6ocr
Deepin Multimedia OCR Toolkit is the base devlopment tool of all C++/Qt
Developer work on Deepin.

%package -n     libdtk6ocr-data
Summary:        Data files for libdtk6ocr
BuildArch:      noarch

%description -n libdtk6ocr-data
This package contains data files for libdtk6ocr.

%package        devel
Summary:        Development files for dtkmultimedia
Requires:       libdtk6multimedia%{?_isa} = %{version}-%{release}
Requires:       libdtk6multimediawidgets%{?_isa} = %{version}-%{release}
Requires:       libdtk6ocr%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for dtkmultimedia.

%prep
%autosetup -p1
# '-Wl,--as-needed' already included in LDFLAGS when building on Fedora
sed -i '/-Wl,--as-needed/d' CMakeLists.txt
sed -i 's/opencv_mobile/opencv4/g' src/ocr/CMakeLists.txt

%build
# fix build with gcc 15
export CFLAGS="%{build_cflags} -std=gnu17"
%cmake -DENABLE_Qt6=ON -DQCH_INSTALL_DESTINATION=%{_qt6_docdir}
%cmake_build

%install
%cmake_install

%files -n libdtk6multimedia
%license LICENSES/*
%doc README.md
%{_libdir}/libdtk6multimedia.so.%{sover}*

%files -n libdtk6multimediawidgets
%license LICENSES/*
%doc README.md
%{_libdir}/libdtk6multimediawidgets.so.%{sover}*

%files -n libdtk6ocr
%license LICENSES/*
%doc README.md
%{_libdir}/libdtk6ocr.so.%{sover}*

%files -n libdtk6ocr-data
%dir %{_datadir}/libdtk6ocr
%{_datadir}/libdtk6ocr/dtkocrmodels/

%files devel
%{_libdir}/libdtk6multimedia.so
%{_libdir}/libdtk6multimediawidgets.so
%{_libdir}/libdtk6ocr.so
%{_includedir}/dtk6multimedia/
%{_includedir}/dtk6multimediawidgets/
%{_includedir}/dtk6ocr/
%{_libdir}/cmake/dtk6multimedia/
%{_libdir}/cmake/dtk6ocr/
%{_libdir}/pkgconfig/dtk6multimedia.pc
%{_libdir}/pkgconfig/dtk6ocr.pc
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_dtk6multimedia.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_dtk6ocr.pri
%{_qt6_docdir}/dtk6multimedia.qch

%changelog
%autochangelog
