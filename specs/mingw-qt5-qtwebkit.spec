%{?mingw_package_header}

%global qt_module qtwebkit
%global pre alpha4

#global commit bd0657f98aff85b9f06d85a8cf4da6a27f61a56e
#global shortcommit %(c=%{commit}; echo ${c:0:7})

%if 0%{?commit:1}
%global source_folder %{qt_module}-%{commit}
%else
%global source_folder %{qt_module}-%{version}%{?pre:-%{pre}}
%endif

## NOTE: Lots of files in various subdirectories have the same name (such as
## "LICENSE") so this short macro allows us to distinguish them by using their
## directory names (from the source tree) as prefixes for the files.
%global add_to_license_files() \
        mkdir -p _license_files ; \
        cp -p %1 _license_files/$(echo '%1' | sed -e 's!/!.!g')

Name:           mingw-qt5-%{qt_module}
Version:        5.212.0
Release:        0.36%{?pre:.%pre}%{?commit:.git%{shortcommit}}%{?dist}
Summary:        Qt5 for Windows - QtWebKit component

License:        LGPL-2.1-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://github.com/qtwebkit/qtwebkit

%if 0%{?commit:1}
Source0:        https://github.com/%{qt_module}/%{qt_module}/archive/%{commit}/%{qt_module}-%{commit}.tar.xz
%else
Source0:        https://github.com/%{qt_module}/%{qt_module}/releases/download/%{qt_module}-%{version}%{?pre:-%pre}/%{qt_module}-%{version}%{?pre:-%pre}.tar.xz
%endif

# Patch for new CMake policy CMP0071 to explicitly use old behaviour.
Patch1:         qtwebkit_cmake_cmp0071.patch
# Don't override import lib suffix
Patch2:         qtwebkit_libsuffix.patch
# Backport python 3.9 build fix
Patch3:         qtwebkit_python.patch
# Fix build with bison 3.7
Patch4:         qtwebkit-bison37.patch
# From https://github.com/WebKit/WebKit/commit/c7d19a492d97f9282a546831beb918e03315f6ef
# Ruby 3.2 removes Object#=~ completely
Patch5:         webkit-offlineasm-warnings-ruby27.patch
# Correctly test ICU return status with U_SUCCESS rather than comparing to U_ZERO_ERROR which fails on warnings
Patch6:         qtwebkit_icu-success.patch
# Fix gcc13 build
Patch7:         qtwebkit_gcc13.patch
# Fix build against recent libxml2
Patch8:         qtwebkit_libxml.patch
# Fix gcc14 build
Patch9:         qtwebkit-fix-build-gcc14.patch
# Switch to -std=c++17 (fixes build with recent icu)
# Drop backported c++14 stl features om StdLibExtras.h
Patch10:        qtwebkit-c++17.patch

BuildArch:      noarch

BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  gperf
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  python3
BuildRequires:  ruby-devel
BuildRequires:  rubygems
# workaround bad embedded png files, https://bugzilla.redhat.com/1639422
BuildRequires:  findutils
BuildRequires:  pngcrush

BuildRequires:  mingw32-filesystem >= 96
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-pkg-config

BuildRequires:  mingw32-dlfcn
BuildRequires:  mingw32-fontconfig
BuildRequires:  mingw32-icu
BuildRequires:  mingw32-libjpeg-turbo
BuildRequires:  mingw32-libpng
BuildRequires:  mingw32-libwebp
BuildRequires:  mingw32-libxslt
BuildRequires:  mingw32-qt5-qtbase
BuildRequires:  mingw32-qt5-qtdeclarative
BuildRequires:  mingw32-qt5-qtsensors
BuildRequires:  mingw32-qt5-qtlocation
BuildRequires:  mingw32-qt5-qtmultimedia
BuildRequires:  mingw32-qt5-qtwebchannel
BuildRequires:  mingw32-sqlite
BuildRequires:  mingw32-zlib


BuildRequires:  mingw64-filesystem >= 96
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-pkg-config

BuildRequires:  mingw64-dlfcn
BuildRequires:  mingw64-angleproject
BuildRequires:  mingw64-fontconfig
BuildRequires:  mingw64-icu
BuildRequires:  mingw64-libjpeg-turbo
BuildRequires:  mingw64-libpng
BuildRequires:  mingw64-libwebp
BuildRequires:  mingw64-libxslt
BuildRequires:  mingw64-qt5-qtbase
BuildRequires:  mingw64-qt5-qtdeclarative
BuildRequires:  mingw64-qt5-qtsensors
BuildRequires:  mingw64-qt5-qtlocation
BuildRequires:  mingw64-qt5-qtmultimedia
BuildRequires:  mingw64-qt5-qtwebchannel
BuildRequires:  mingw64-sqlite
BuildRequires:  mingw64-zlib



%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win32
%package -n mingw32-qt5-%{qt_module}
Summary:        Qt5 for Windows - QtWebkit component
Provides:       bundled(angle)
Provides:       bundled(brotli)
Provides:       bundled(woff2)

%description -n mingw32-qt5-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win64
%package -n mingw64-qt5-%{qt_module}
Summary:        Qt5 for Windows - QtWebkit component
Provides:       bundled(angle)
Provides:       bundled(brotli)
Provides:       bundled(woff2)

%description -n mingw64-qt5-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{source_folder}

# find/fix pngs with "libpng warning: iCCP: known incorrect sRGB profile"
find -name \*.png | xargs -n1 pngcrush -ow -fix


%build
# Make sure the native pkg-config files aren't used (RPM sets this environment variable automatically)
unset PKG_CONFIG_PATH

# Reduce debuginfo verbosity to decrease memory usage
mingw32_cflags_="%(echo %mingw32_cflags | sed 's/-g /-g1 /')"
mingw64_cflags_="%(echo %mingw64_cflags | sed 's/-g /-g1 /')"

# -D_WIN32_WINNT=0x0600 Needed for GetTickCount64
export MINGW32_CFLAGS="$mingw32_cflags_ -D_WIN32_WINNT=0x0600"
export MINGW32_CXXFLAGS="$mingw32_cflags_ -D_WIN32_WINNT=0x0600"
export MINGW64_CFLAGS="$mingw64_cflags_ -D_WIN32_WINNT=0x0600"
export MINGW64_CXXFLAGS="$mingw64_cflags_ -D_WIN32_WINNT=0x0600"

# TODO
# --  USE_LIBHYPHEN                             OFF
%mingw_cmake -DPORT=Qt \
    -DRUBY_CONFIG_INCLUDE_DIR:PATH=/usr/include \
    -DRUBY_LIBRARY:FILEPATH=/usr/lib64/libruby.so \
    -DRUBY_INCLUDE_DIR:PATH=/usr/include

%mingw_make_build


%install
%mingw_make_install

# Copy over and rename various files for %%license inclusion
%add_to_license_files Source/JavaScriptCore/COPYING.LIB
%add_to_license_files Source/JavaScriptCore/icu/LICENSE
%add_to_license_files Source/ThirdParty/ANGLE/LICENSE
%add_to_license_files Source/ThirdParty/ANGLE/src/third_party/compiler/LICENSE
%add_to_license_files Source/ThirdParty/ANGLE/src/third_party/murmurhash/LICENSE
%add_to_license_files Source/WebCore/icu/LICENSE
%add_to_license_files Source/WebCore/LICENSE-APPLE
%add_to_license_files Source/WebCore/LICENSE-LGPL-2
%add_to_license_files Source/WebCore/LICENSE-LGPL-2.1
%add_to_license_files Source/WebInspectorUI/UserInterface/External/CodeMirror/LICENSE
%add_to_license_files Source/WebInspectorUI/UserInterface/External/Esprima/LICENSE
%add_to_license_files Source/WTF/icu/LICENSE
%add_to_license_files Source/WTF/wtf/dtoa/COPYING
%add_to_license_files Source/WTF/wtf/dtoa/LICENSE

# Move executables installed to the wrong location
mv %{buildroot}%{mingw32_libdir}/qt5/bin/*.exe %{buildroot}%{mingw32_bindir}
mv %{buildroot}%{mingw64_libdir}/qt5/bin/*.exe %{buildroot}%{mingw64_bindir}
rmdir %{buildroot}%{mingw32_libdir}/qt5/bin/
rmdir %{buildroot}%{mingw64_libdir}/qt5/bin/


# Win32
%files -n mingw32-qt5-%{qt_module}
%license LICENSE.LGPLv21 _license_files/*
%{mingw32_bindir}/QtWebNetworkProcess.exe
%{mingw32_bindir}/QtWebProcess.exe
%{mingw32_bindir}/QtWebStorageProcess.exe
%{mingw32_bindir}/Qt5WebKit.dll
%{mingw32_bindir}/Qt5WebKitWidgets.dll
%{mingw32_includedir}/qt5/QtWebKit/
%{mingw32_includedir}/qt5/QtWebKitWidgets/
%{mingw32_libdir}/libQt5WebKit.dll.a
%{mingw32_libdir}/libQt5WebKitWidgets.dll.a
%{mingw32_libdir}/cmake/Qt5WebKit/
%{mingw32_libdir}/cmake/Qt5WebKitWidgets/
%{mingw32_libdir}/pkgconfig/Qt5WebKit.pc
%{mingw32_libdir}/pkgconfig/Qt5WebKitWidgets.pc
%{mingw32_libdir}/qt5/qml/QtWebKit/
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_webkit.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_webkit_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_webkitwidgets.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_webkitwidgets_private.pri

# Win64
%files -n mingw64-qt5-%{qt_module}
%license LICENSE.LGPLv21 _license_files/*
%{mingw64_bindir}/QtWebNetworkProcess.exe
%{mingw64_bindir}/QtWebProcess.exe
%{mingw64_bindir}/QtWebStorageProcess.exe
%{mingw64_bindir}/Qt5WebKit.dll
%{mingw64_bindir}/Qt5WebKitWidgets.dll
%{mingw64_includedir}/qt5/QtWebKit/
%{mingw64_includedir}/qt5/QtWebKitWidgets/
%{mingw64_libdir}/libQt5WebKit.dll.a
%{mingw64_libdir}/libQt5WebKitWidgets.dll.a
%{mingw64_libdir}/cmake/Qt5WebKit/
%{mingw64_libdir}/cmake/Qt5WebKitWidgets/
%{mingw64_libdir}/pkgconfig/Qt5WebKit.pc
%{mingw64_libdir}/pkgconfig/Qt5WebKitWidgets.pc
%{mingw64_libdir}/qt5/qml/QtWebKit/
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_webkit.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_webkit_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_webkitwidgets.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_webkitwidgets_private.pri


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.212.0-0.36.alpha4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 08 2024 Sandro Mani <manisandro@gmail.com> - 5.212.0-0.35.alpha4
- Add qtwebkit-c++14.patch

* Fri Dec 06 2024 Sandro Mani <manisandro@gmail.com> - 5.212.0-0.34.alpha4
- Rebuild (mingw-icu)

* Fri Dec 06 2024 Sandro Mani <manisandro@gmail.com> - 5.212.0-0.33.alpha4
- Rebuild (mingw-icu)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.212.0-0.32.alpha4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Feb 05 2024 Sandro Mani <manisandro@gmail.com> - 5.212.0-0.31.alpha4
- Rebuild (icu)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.212.0-0.30.alpha4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.212.0-0.29.alpha4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.212.0-0.28.alpha4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 18 2023 Sandro Mani <manisandro@gmail.com> - 5.212.0-0.27.alpha4
- Rebuild (mingw-icu)

* Fri Jan 20 2023 Sandro Mani <manisandro@gmail.com> - 5.212.0-0.26.alpha4
- Add qtwebkit_icu-success.patch

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.212.0-0.25.alpha4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 16 2023 Sandro Mani <manisandro@gmail.com> - 5.212.0-0.24.alpha4
- Rebuild

* Tue Jan 03 2023 Sandro Mani <manisandro@gmail.com> - 5.212.0-0.23.alpha4
- Rebuild (mingw-icu)

* Tue Oct 18 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.212.0-0.22.alpha4
- Patch for offlineasm to support ruby 3.2 wrt Object#=~ removal

* Fri Aug 05 2022 Sandro Mani <manisandro@gmail.com> - 5.212.0-0.21.alpha4
- Rebuild (icu)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.212.0-0.20.alpha4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar 28 2022 Sandro Mani <manisandro@gmail.com> - 5.212.0-0.19.alpha4
- Drop -DSHARED_CORE=ON

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 5.212.0-0.18.alpha4
- Rebuild with mingw-gcc-12

* Mon Mar 14 2022 Sandro Mani <manisandro@gmail.com> - 5.212.0-0.17.alpha4
- Fix lib install dir at cmake level

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.212.0-0.16.alpha4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.212.0-0.15.alpha4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Sandro Mani <manisandro@gmail.com> - 5.212.0-0.14.alpha4
- Rebuild (icu)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.212.0-0.13.alpha4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 20:13:25 CET 2020 Sandro Mani <manisandro@gmail.com> - 5.212.0-0.12.alpha4
- Rebuild (qt5)

* Wed Oct  7 14:44:56 CEST 2020 Sandro Mani <manisandro@gmail.com> - 5.212.0-0.11.alpha4
- Rebuild (qt5)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.212.0-0.10.alpha4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 19 2020 Sandro Mani <manisandro@gmail.com> - 5.212.0-0.9.alpha4
- Rebuild (icu)

* Fri Apr 10 2020 Sandro Mani <manisandro@gmail.com> - 5.212.0-0.8.alpha4
- Update to 5.212.0-alpha4

* Thu Apr 09 2020 Sandro Mani <manisandro@gmail.com> - 5.212.0-0.7.alpha3
- Rebuild (Qt5)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.212.0-0.6.alpha3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 16 2019 Sandro Mani <manisandro@gmail.com> - 5.212.0-0.5.alpha3
- Rebuild (qt5)

* Tue Nov 05 2019 Sandro Mani <manisandro@gmail.com> - 5.212.0-0.4.alpha3
- Rebuild (icu)

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 5.212.0-0.3.alpha3
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Sep 26 2019 Sandro Mani <manisandro@gmail.com> - 5.212.0-0.2.alpha3
- Rebuild (qt5)

* Wed Aug 28 2019 Sandro Mani <manisandro@gmail.com> - 5.212.0-0.1.alpha3
- Update to 5.212.0-alpha3

* Tue Aug 27 2019 Sandro Mani <manisandro@gmail.com> - 5.9.4-0.12.gitbd0657f
- Rebuild to fix pkg-config files (#1745257)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.4-0.11.gitbd0657f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 19 2019 Sandro Mani <manisandro@gmail.com> - 5.9.4-0.10.gitbd0657f
- Rebuild for mingw-qt5-5.12.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.4-0.9.gitbd0657f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Sandro Mani <manisandro@gmail.com> - 5.9.4-0.8.gitbd0657f
- Rebuild for mingw-qt5-5.11.3

* Sun Sep 23 2018 Sandro Mani <manisandro@gmail.com> - 5.9.4-0.7.gitbd0657f
- Rebuild for mingw-qt5-5.11.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.4-0.6.gitbd0657f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 31 2018 Sandro Mani <manisandro@gmail.com> - 5.9.4-0.5.gitbd0657f
- Rebuild for mingw-qt5-5.11.0

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 5.9.4-0.4.gitbd0657f
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 16 2018 Sandro Mani <manisandro@gmail.com> - 5.9.4-0.3.gitbd0657f
- Rebuild for mingw-qt5-5.10.1

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.4-0.2.gitbd0657f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Sandro Mani <manisandro@gmail.com> - 5.9.4-0.1.gitbd0657f
- Update to git bd0657f

* Wed Dec 20 2017 Sandro Mani <manisandro@gmail.com> - 5.9.3-0.2.gitfdafce4
- Rebuild for mingw-qt5-5.10.0

* Mon Nov 27 2017 Sandro Mani <manisandro@gmail.com> - 5.9.3-0.1.gitfdafce4
- Update to latest git

* Wed Oct 11 2017 Sandro Mani <manisandro@gmail.com> - 5.9.2-2
- Fix huge Qt5WebKit.dll due to debuginfo extraction failure

* Wed Oct 11 2017 Sandro Mani <manisandro@gmail.com> - 5.9.2-1
- Update to 5.9.2

* Sat Sep 09 2017 Sandro Mani <manisandro@gmail.com> - 5.9.1-3
- Fix debug files in main package

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 11 2017 Sandro Mani <manisandro@gmail.com> - 5.9.1-1
- Update to 5.9.1

* Fri Jun 30 2017 Sandro Mani <manisandro@gmail.com> - 5.9.0-1
- Update to 5.9.0

* Tue May 09 2017 Sandro Mani <manisandro@gmail.com> - 5.8.0-2
- Rebuild for dropped 0022-Allow-usage-of-static-version-with-CMake.patch in qtbase

* Thu May 04 2017 Sandro Mani <manisandro@gmail.com> - 5.8.0-1
- Update to 5.8.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 04 2017 Sandro Mani <manisandro@gmail.com> - 5.7.1-1
- Update to 5.7.1

* Wed Feb 01 2017 Sandro Mani <manisandro@gmail.com> - 5.5.1-4
- Rebuild (libwebp)

* Sat May  7 2016 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.5.1-3
- Add BuildRequires: rubygems to fix FTBFS

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 30 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.5.1-1
- Update to 5.5.1

* Wed Dec 30 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.5.0-2
- Rebuild against mingw-libwebp-0.5.0

* Fri Aug  7 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.5.0-1
- Update to 5.5.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 22 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.4.1-1
- Update to 5.4.1
- Fix URLs visited during private browsing showing up in WebpageIcons.db (RHBZ #1204798 #1204799)
- Fix FTBFS against gcc 5 (QTBUG-44829)

* Mon Dec 29 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.4.0-1
- Update to 5.4.0

* Sat Sep 20 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.3.2-1
- Update to 5.3.2

* Tue Jul  8 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.3.1-1
- Update to 5.3.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 25 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.3.0-1
- Update to 5.3.0

* Thu May 22 2014 Kalev Lember <kalevlember@gmail.com> - 5.2.1-3
- Rebuilt with libwebp 0.4.0

* Thu Mar  6 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.2.1-2
- Use virtual BuildRequires for the perl requirements (fixes build on F19)

* Sat Feb  8 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.2.1-1
- Update to 5.2.1

* Sun Jan  5 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.2.0-1
- Update to 5.2.0
- Dropped manual rename of import libraries

* Fri Nov 29 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.2.0-0.1.rc1
- Update to 5.2.0 RC1

* Sun Sep 22 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.1.1-1
- Update to 5.1.1
- Added license files

* Wed Jul 24 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.1.0-2
- Fix detection of native tools which started to fail as of QtWebkit 5.1.0
- Avoid 'too many sections' build failure

* Sun Jul 14 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.1.0-1
- Update to 5.1.0

* Sat May 18 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.2-2
- Bumped the BR: mingw{32,64}-angleproject to >= 0-0.5.svn2215.20130517
- Don't use the bundled ANGLE libraries any more
- Applied some upstream patches to prevent flooding the logs with
  compiler warnings when using gcc 4.8
- Added BR: mingw32-qt5-qtmultimedia mingw64-qt5-qtmultimedia
- Added BR: mingw32-libwebp mingw64-libwebp

* Fri May 10 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.2-1
- Update to 5.0.2
- Added BR: flex perl-version perl-Digest-MD5

* Sun Jan  6 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.0-1
- Update to QtWebKit 5.0.0 Final
- Workaround linker failure caused by recent QWebKit/QWebKitWidgets split
- Use the Qt4 unicode API as the mingw-qt5-qtbase currently doesn't use ICU
- Added BR: mingw32-pkg-config mingw64-pkg-config mingw32-sqlite mingw64-sqlite
- Added BR: mingw32-angleproject mingw64-angleproject
- Use the bundled ANGLE libraries for now as qtwebkit depends on non-public symbols

* Mon Nov 12 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.0-0.2.beta1.git20121112.23037105
- Update to 20121112 snapshot (rev 23037105)
- Rebuild against latest mingw-qt5-qtbase
- Dropped pkg-config rename hack as it's unneeded now
- Dropped upstreamed patch
- Added BR: python
- Added BR: ruby

* Wed Sep 12 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.0-0.1.beta1
- Initial release

