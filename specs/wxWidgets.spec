%global wxver 3.3
%global wxstablever 3.4
%global wxname wxWidgets%{wxstablever}
%global wxbasename wxBase%{wxstablever}
%global wxgtkname wxGTK%{wxstablever}
%global wxqtname wxQt%{wxstablever}
%global gtk3dir bld_gtk3
%global qt6dir bld_qt6
%global sover 4
%bcond_without tests

Name:           wxWidgets
Version:        3.3.4
Release:        1%{?dist}
Summary:        wxWidgets GUI library
License:        LGPL-2.0-or-later WITH WxWindows-exception-3.1
URL:            https://www.wxwidgets.org/

Source0:        https://github.com/wxWidgets/wxWidgets/releases/download/v%{version}/wxWidgets-%{version}.tar.bz2
# https://bugzilla.redhat.com/show_bug.cgi?id=1225148
# remove abort when ABI check fails
# Backport from wxGTK
Patch:          wxGTK-3.1.6-abicheck.patch
Patch:          fix-ipc-big-endian.patch
Patch:          webview-test-delay.patch
Patch:          webview-test-crash.patch

BuildRequires:  cmake
BuildRequires:  cppunit-devel
BuildRequires:  doxygen
BuildRequires:  expat-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  graphviz
BuildRequires:  gstreamer1-plugins-bad-free-devel
BuildRequires:  gtk3-devel
BuildRequires:  libcurl-devel
BuildRequires:  libGLU-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libmspack-devel
BuildRequires:  libpng-devel
BuildRequires:  libsecret-devel
BuildRequires:  libSM-devel
BuildRequires:  libtiff-devel
BuildRequires:  make
BuildRequires:  SDL2-devel
BuildRequires:  webkit2gtk4.1-devel
BuildRequires:  zlib-devel
# For wxQt
BuildRequires:  qt6-qtbase-devel
# For Tests
%if %{with tests}
BuildRequires:  glibc-langpack-en
BuildRequires:  mesa-libEGL
BuildRequires:  python3-httpbin
BuildRequires:  vulkan-loader
BuildRequires:  xclock
BuildRequires:  xorg-x11-server-Xvfb
%endif

Provides:       bundled(lunasvg) = 3.5.0
Provides:       bundled(scintilla) = 5.0.0
Requires:       %{wxbasename}%{?_isa} = %{version}-%{release}
Requires:       %{wxname}-i18n = %{version}-%{release}

%description
wxWidgets is a C++ cross-platform GUI library, offering classes for all
common GUI controls as well as a comprehensive set of helper classes for
most common application tasks, ranging from networking to HTML display and
image manipulation.


%package -n     %{wxgtkname}
Summary:        %{summary}

%description -n %{wxgtkname}
wxGTK is the GTK port of the C++ cross-platform wxWidgets GUI library,
offering classes for all common GUI controls as well as a comprehensive
set of helper classes for most common application tasks, ranging from
networking to HTML display and image manipulation.


%package -n     %{wxqtname}
Summary:        %{summary}

%description -n %{wxqtname}
wxQt is the Qt port of the C++ cross-platform wxWidgets GUI library,
offering classes for all common GUI controls as well as a comprehensive
set of helper classes for most common application tasks, ranging from
networking to HTML display and image manipulation.


%package -n     %{wxbasename}-devel
Summary:        Development files for the wxBase library
Requires:       %{wxbasename}%{?_isa} = %{version}-%{release}
Requires(post): /usr/sbin/update-alternatives
Requires(postun): /usr/sbin/update-alternatives

%description -n %{wxbasename}-devel
This package include files needed to link with the wxBase library.
wxWidgets is the C++ cross-platform GUI library, offering classes for all
common GUI controls as well as a comprehensive set of helper classes for
most common application tasks, ranging from networking to HTML display
and image manipulation.


%package -n     %{wxgtkname}-devel
Summary:        Development files for the wxGTK library
Requires:       %{wxgtkname}%{?_isa} = %{version}-%{release}
Requires:       %{wxgtkname}-gl = %{version}-%{release}
Requires:       %{wxgtkname}-media = %{version}-%{release}
Requires:       %{wxgtkname}-webview = %{version}-%{release}
Requires:       %{wxbasename} = %{version}-%{release}
Requires:       %{wxbasename}-devel%{?_isa} = %{version}-%{release}
Requires:       gtk3-devel
Requires:       libGLU-devel
Requires(post): /usr/sbin/update-alternatives
Requires(postun): /usr/sbin/update-alternatives

%description -n %{wxgtkname}-devel
This package include files needed to link with the wxGTK library.
wxGTK is the GTK port of the C++ cross-platform wxWidgets GUI library,
offering classes for all common GUI controls as well as a comprehensive
set of helper classes for most common application tasks, ranging from
networking to HTML display and image manipulation.


%package -n     %{wxqtname}-devel
Summary:        Development files for the wxGTK library
Requires:       %{wxqtname}%{?_isa} = %{version}-%{release}
Requires:       %{wxqtname}-gl = %{version}-%{release}
Requires:       %{wxqtname}-media = %{version}-%{release}
Requires:       %{wxbasename} = %{version}-%{release}
Requires:       %{wxbasename}-devel%{?_isa} = %{version}-%{release}
Requires(post): /usr/sbin/update-alternatives
Requires(postun): /usr/sbin/update-alternatives

%description -n %{wxqtname}-devel
This package include files needed to link with the wxQt library.
wxQt is the Qt port of the C++ cross-platform wxWidgets GUI library,
offering classes for all common GUI controls as well as a comprehensive
set of helper classes for most common application tasks, ranging from
networking to HTML display and image manipulation.


%package -n     %{wxgtkname}-gl
Summary:        OpenGL add-on for the wxWidgets library
Requires:       %{wxgtkname}%{?_isa} = %{version}-%{release}

%description -n %{wxgtkname}-gl
OpenGL (a 3D graphics API) add-on for the wxWidgets library.
wxGTK is the GTK port of the C++ cross-platform wxWidgets GUI library,
offering classes for all common GUI controls as well as a comprehensive
set of helper classes for most common application tasks, ranging from
networking to HTML display and image manipulation.


%package -n     %{wxqtname}-gl
Summary:        OpenGL add-on for the wxWidgets library
Requires:       %{wxqtname}%{?_isa} = %{version}-%{release}

%description -n %{wxqtname}-gl
OpenGL (a 3D graphics API) add-on for the wxWidgets library.
wxQt is the Qt port of the C++ cross-platform wxWidgets GUI library,
offering classes for all common GUI controls as well as a comprehensive
set of helper classes for most common application tasks, ranging from
networking to HTML display and image manipulation.


%package -n     %{wxname}-i18n
Summary:        i18n message catalogs for the wxWidgets library
BuildArch:      noarch

%description -n %{wxname}-i18n
i18n message catalogs for the wxWidgets library.
wxWidgets is the C++ cross-platform wxWidgets GUI library, offering classes
for all common GUI controls as well as a comprehensive set of helper classes
for most common application tasks, ranging from networking to HTML display
and image manipulation.


%package -n     %{wxgtkname}-media
Summary:        Multimedia add-on for the wxWidgets library
Requires:       %{wxgtkname}%{?_isa} = %{version}-%{release}

%description -n %{wxgtkname}-media
Multimedia add-on for the wxWidgets library.
wxGTK is the GTK port of the C++ cross-platform wxWidgets GUI library,
offering classes for all common GUI controls as well as a comprehensive
set of helper classes for most common application tasks, ranging from
networking to HTML display and image manipulation.


%package -n     %{wxqtname}-media
Summary:        Multimedia add-on for the wxWidgets library
Requires:       %{wxqtname}%{?_isa} = %{version}-%{release}

%description -n %{wxqtname}-media
Multimedia add-on for the wxWidgets library.
wxQt is the Qt port of the C++ cross-platform wxWidgets GUI library,
offering classes for all common GUI controls as well as a comprehensive
set of helper classes for most common application tasks, ranging from
networking to HTML display and image manipulation.


%package -n     %{wxgtkname}-webview
Summary:        WebView add-on for the wxWidgets library
Requires:       %{wxgtkname}%{?_isa} = %{version}-%{release}

%description -n %{wxgtkname}-webview
WebView add-on for the wxWidgets library.
wxGTK is the GTK port of the C++ cross-platform wxWidgets GUI library,
offering classes for all common GUI controls as well as a comprehensive
set of helper classes for most common application tasks, ranging from
networking to HTML display and image manipulation.


%package -n     %{wxbasename}
Summary:        Non-GUI support classes from the wxWidgets library

%description -n %{wxbasename}
Every wxWidgets application must link against this library. It contains
mandatory classes that any wxWidgets code depends on (like wxString) and
portability classes that abstract differences between platforms. wxBase can
be used to develop console mode applications -- it does not require any GUI
libraries or the X Window System.


%package -n     %{wxname}-docs
Summary:        Documentation for the wxWidgets library
BuildArch:      noarch

%description -n %{wxname}-docs
This package provides documentation for the wxWidgets library.


%prep
%autosetup -n wxWidgets-%{version} -p1

# patch some installed files to avoid conflicts with 2.8.*
sed -i -e 's|aclocal)|aclocal/wxwin33.m4)|' Makefile.in

# fix plugin dir for 64-bit
sed -i -e 's|/usr/lib\b|/usr/%{_lib}|' wx-config.in configure
sed -i -e 's|/lib|/%{_lib}|' src/unix/stdpaths.cpp
sed -i -e 's|wxT("lib")|wxT("%{_lib}")|' src/common/dynlib.cpp


%conf
%global _vpath_builddir %{gtk3dir}
%cmake -DwxBUILD_TOOLKIT=gtk3 -DwxBUILD_TESTS=ALL -DwxUSE_LIBLZMA=ON \
       -DwxUSE_LUNASVG=builtin -DwxUSE_ARTPROVIDER_TANGO=OFF

%global _vpath_builddir %{qt6dir}
%cmake -DwxBUILD_TOOLKIT=qt -DwxBUILD_TESTS=ALL -DwxUSE_LIBLZMA=ON \
       -DwxUSE_LUNASVG=builtin


%build
%global _vpath_builddir %{gtk3dir}
%cmake_build

%global _vpath_builddir %{qt6dir}
%cmake_build

#Docs
WX_SKIP_DOXYGEN_VERSION_CHECK=1 docs/doxygen/regen.sh html
mv docs/doxygen/out/html .


%install
%global _vpath_builddir %{gtk3dir}
%cmake_install
mv %{buildroot}%{_libdir}/cmake/wxWidgets-%{wxver} %{buildroot}%{_libdir}/cmake/wxWidgets-%{wxver}-gtk3

%global _vpath_builddir %{qt6dir}
%cmake_install
mv %{buildroot}%{_libdir}/cmake/wxWidgets-%{wxver} %{buildroot}%{_libdir}/cmake/wxWidgets-%{wxver}-qt

# install our multilib-aware wrapper
##Remove installed
rm %{buildroot}%{_bindir}/wx-config
##Install new and symlink
#install -p -D -m 755 %{SOURCE10} %{buildroot}%{_bindir}/wx-config
#sed -i -e 's|=/usr|=%{_prefix}|' %{buildroot}%{_bindir}/wx-config
touch %{buildroot}%{_bindir}/wx-config

#Alternatives setup with wxrc
mkdir -p %{buildroot}%{_libexecdir}/%{name}
mv %{buildroot}%{_bindir}/wxrc* %{buildroot}%{_libexecdir}/%{name}
ln -s ../..%{_libexecdir}/%{name}/wxrc-%{wxver} %{buildroot}%{_bindir}/wxrc-%{wxver}
touch %{buildroot}%{_bindir}/wxrc

%find_lang wxstd-%{wxver}

%check
%if %{with tests}
python3 -m httpbin.core &

pushd %{gtk3dir}/lib
LD_LIBRARY_PATH=%{buildroot}%{_libdir} TZ=UTC wxUSE_XVFB=1 \
  WX_TEST_WEBREQUEST_URL="http://localhost:5000" xvfb-run -a ./test_base ~[.] \
  ~LZMAStream::Input_Peek ~wxFileName::GetSizeSpecial

LD_LIBRARY_PATH=%{buildroot}%{_libdir} wxUSE_XVFB=1 xvfb-run -a \
  ./test_gui ~[.] \
%ifarch s390x
  ~WebView \
%endif
  ~wxHtmlPrintout::Pagination ~EventPropagationTestCase ~EnterLeaveEvents ~ListCtrl::Visible
popd  

pushd %{qt6dir}/lib
LD_LIBRARY_PATH=%{buildroot}%{_libdir} TZ=UTC wxUSE_XVFB=1 \
  WX_TEST_WEBREQUEST_URL="http://localhost:5000" xvfb-run -a ./test_base ~[.] \
  ~LZMAStream::Input_Peek ~wxFileName::GetSizeSpecial
# Not running gui tests for wxQt due to too many failures currently
popd  
%endif

%post -n %{wxbasename}-devel
/usr/sbin/update-alternatives --install %{_bindir}/wxrc \
  wxrc %{_libexecdir}/%{name}/wxrc 30

%postun -n %{wxbasename}-devel
if [ $1 -eq 0 ] ; then
  /usr/sbin/update-alternatives --remove wxrc %{_libexecdir}/%{name}/wxrc
fi

%post -n %{wxgtkname}-devel
if [ -f %{_bindir}/wx-config ] && [ ! -h %{_bindir}/wx-config ] ; then
  rm %{_bindir}/wx-config
fi
/usr/sbin/update-alternatives --install %{_bindir}/wx-config \
  wx-config %{_libdir}/wx/config/gtk3-unicode-%{wxver} 30

%postun -n %{wxgtkname}-devel
if [ $1 -eq 0 ] ; then
  /usr/sbin/update-alternatives --remove wx-config %{_libdir}/wx/config/gtk3-unicode-%{wxver}
fi

%post -n %{wxqtname}-devel
if [ -f %{_bindir}/wx-config ] && [ ! -h %{_bindir}/wx-config ] ; then
  rm %{_bindir}/wx-config
fi
/usr/sbin/update-alternatives --install %{_bindir}/wx-config \
  wx-config %{_libdir}/wx/config/qt-unicode-%{wxver} 29

%postun -n %{wxqtname}-devel
if [ $1 -eq 0 ] ; then
  /usr/sbin/update-alternatives --remove wx-config %{_libdir}/wx/config/qt-unicode-%{wxver}
fi

%files -n %{wxgtkname}
%doc docs/changes.txt docs/readme.txt
%license docs/gpl.txt docs/lgpl.txt docs/licence.txt docs/licendoc.txt
%license docs/preamble.txt
%{_libdir}/libwx_gtk3u_adv-%{wxver}.so.%{sover}{,.*}
%{_libdir}/libwx_gtk3u_aui-%{wxver}.so.%{sover}{,.*}
%{_libdir}/libwx_gtk3u_core-%{wxver}.so.%{sover}{,.*}
%{_libdir}/libwx_gtk3u_html-%{wxver}.so.%{sover}{,.*}
%{_libdir}/libwx_gtk3u_propgrid-%{wxver}.so.%{sover}{,.*}
%{_libdir}/libwx_gtk3u_qa-%{wxver}.so.%{sover}{,.*}
%{_libdir}/libwx_gtk3u_ribbon-%{wxver}.so.%{sover}{,.*}
%{_libdir}/libwx_gtk3u_richtext-%{wxver}.so.%{sover}{,.*}
%{_libdir}/libwx_gtk3u_stc-%{wxver}.so.%{sover}{,.*}
%{_libdir}/libwx_gtk3u_xrc-%{wxver}.so.%{sover}{,.*}

%files -n %{wxqtname}
%doc docs/changes.txt docs/readme.txt
%license docs/gpl.txt docs/lgpl.txt docs/licence.txt docs/licendoc.txt
%license docs/preamble.txt
%{_libdir}/libwx_qtu_adv-%{wxver}.so.%{sover}{,.*}
%{_libdir}/libwx_qtu_aui-%{wxver}.so.%{sover}{,.*}
%{_libdir}/libwx_qtu_core-%{wxver}.so.%{sover}{,.*}
%{_libdir}/libwx_qtu_html-%{wxver}.so.%{sover}{,.*}
%{_libdir}/libwx_qtu_propgrid-%{wxver}.so.%{sover}{,.*}
%{_libdir}/libwx_qtu_qa-%{wxver}.so.%{sover}{,.*}
%{_libdir}/libwx_qtu_ribbon-%{wxver}.so.%{sover}{,.*}
%{_libdir}/libwx_qtu_richtext-%{wxver}.so.%{sover}{,.*}
%{_libdir}/libwx_qtu_stc-%{wxver}.so.%{sover}{,.*}
%{_libdir}/libwx_qtu_xrc-%{wxver}.so.%{sover}{,.*}

%files -n %{wxbasename}-devel
%ghost %{_bindir}/wxrc
%{_bindir}/wxrc-%{wxver}
%{_includedir}/wx-%{wxver}
%{_libdir}/libwx_baseu*.so
%dir %{_libdir}/wx
%dir %{_libdir}/wx/config
%dir %{_libdir}/wx/include
%{_libexecdir}/%{name}

%files -n %{wxgtkname}-devel
%ghost %{_bindir}/wx-config
%{_libdir}/libwx_gtk3u_*.so
%{_libdir}/wx/config/gtk3-unicode-%{wxver}
%{_libdir}/wx/include/gtk3-unicode-%{wxver}
%{_libdir}/cmake/wxWidgets-%{wxver}-gtk3

%files -n %{wxqtname}-devel
%ghost %{_bindir}/wx-config
%{_libdir}/libwx_qtu_*.so
%{_libdir}/wx/config/qt-unicode-%{wxver}
%{_libdir}/wx/include/qt-unicode-%{wxver}
%{_libdir}/cmake/wxWidgets-%{wxver}-qt

%files -n %{wxgtkname}-gl
%{_libdir}/libwx_gtk3u_gl-%{wxver}.so.%{sover}{,.*}

%files -n %{wxqtname}-gl
%{_libdir}/libwx_qtu_gl-%{wxver}.so.%{sover}{,.*}

%files -n %{wxname}-i18n -f wxstd-%{wxver}.lang

%files -n %{wxgtkname}-media
%{_libdir}/libwx_gtk3u_media-%{wxver}.so.%{sover}{,.*}

%files -n %{wxqtname}-media
%{_libdir}/libwx_qtu_media-%{wxver}.so.%{sover}{,.*}

%files -n %{wxgtkname}-webview
%{_libdir}/libwx_gtk3u_webview-%{wxver}.so.%{sover}{,.*}
%dir %{_libdir}/wx
%{_libdir}/wx/%{version}

%files -n %{wxbasename}
%doc docs/changes.txt docs/readme.txt
%license docs/gpl.txt docs/lgpl.txt docs/licence.txt docs/licendoc.txt
%license docs/preamble.txt
%{_libdir}/libwx_baseu-%{wxver}.so.%{sover}{,.*}
%{_libdir}/libwx_baseu_net-%{wxver}.so.%{sover}{,.*}
%{_libdir}/libwx_baseu_xml-%{wxver}.so.%{sover}{,.*}

%files -n %{wxname}-docs
%doc html

%changelog
* Sun Nov 01 2026 Scott Talbert <swt@techie.net> - 3.3.4-1
- Initial packaging of wxWidgets 3.3.x (dev version) (#2443717)
