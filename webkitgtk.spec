# https://bugs.webkit.org/show_bug.cgi?id=249368
%global _lto_cflags %{nil}

## NOTE: Lots of files in various subdirectories have the same name (such as
## "LICENSE") so this short macro allows us to distinguish them by using their
## directory names (from the source tree) as prefixes for the files.
%global add_to_license_files() \
        mkdir -p _license_files ; \
        cp -p %1 _license_files/$(echo '%1' | sed -e 's!/!.!g')

# No libmanette in RHEL
%if !0%{?rhel}
%global with_gamepad 1
%endif

# Build documentation by default (use `rpmbuild --without docs` to override it).
# This is used by Coverity. Coverity injects custom compiler warnings, but
# any warning during WebKit docs build is fatal!
%bcond_without docs

Name:           webkitgtk
Version:        2.39.3
Release:        %autorelease
Summary:        GTK web content engine library

License:        LGPLv2
URL:            https://www.webkitgtk.org/
Source0:        https://webkitgtk.org/releases/webkitgtk-%{version}.tar.xz
Source1:        https://webkitgtk.org/releases/webkitgtk-%{version}.tar.xz.asc
# Use the keys from https://webkitgtk.org/verifying.html
# $ gpg --import aperez.key carlosgc.key
# $ gpg --export --export-options export-minimal D7FCF61CF9A2DEAB31D81BD3F3D322D0EC4582C3 5AA3BC334FD7E3369E7C77B291C559DBE4C9123B > webkitgtk-keys.gpg
Source2:        webkitgtk-keys.gpg

BuildRequires:  bison
BuildRequires:  bubblewrap
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gi-docgen
BuildRequires:  git
BuildRequires:  gnupg2
BuildRequires:  gperf
BuildRequires:  hyphen-devel
BuildRequires:  libatomic
BuildRequires:  ninja-build
BuildRequires:  openssl-devel
BuildRequires:  perl(English)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(JSON::PP)
BuildRequires:  python3
BuildRequires:  ruby
BuildRequires:  rubygems
BuildRequires:  rubygem-json
BuildRequires:  unifdef
BuildRequires:  xdg-dbus-proxy

BuildRequires:  pkgconfig(atspi-2)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(enchant-2)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libavif)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libtasn1)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwoff2dec)
BuildRequires:  pkgconfig(libxslt)
%if 0%{?with_gamepad}	
BuildRequires:  pkgconfig(manette-0.2)
%endif
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wpe-1.0)
BuildRequires:  pkgconfig(wpebackend-fdo-1.0)
BuildRequires:  pkgconfig(xt)

# Filter out provides for private libraries
%global __provides_exclude_from ^(%{_libdir}/webkit2gtk-4\\.0/.*\\.so|%{_libdir}/webkit2gtk-4\\.1/.*\\.so|%{_libdir}/webkitgtk-6\\.0/.*\\.so)$

%description
WebKitGTK is the port of the WebKit web rendering engine to the
GTK platform.

%package -n     webkitgtk6.0
Summary:        WebKitGTK for GTK 4
Requires:       javascriptcoregtk6.0%{?_isa} = %{version}-%{release}
Requires:       bubblewrap
Requires:       xdg-dbus-proxy
Recommends:     geoclue2
Recommends:     gstreamer1-plugins-bad-free
Recommends:     gstreamer1-plugins-good
Recommends:     xdg-desktop-portal-gtk
Provides:       bundled(angle)
Provides:       bundled(pdfjs)
Provides:       bundled(xdgmime)
Obsoletes:      webkit2gtk5.0 < %{version}-%{release}

%description -n webkitgtk6.0
WebKitGTK is the port of the WebKit web rendering engine to the
GTK platform. This package contains WebKitGTK for GTK 4.

%package -n     webkit2gtk4.1
Summary:        WebKitGTK for GTK 3 and libsoup 3
Requires:       javascriptcoregtk4.1%{?_isa} = %{version}-%{release}
Requires:       bubblewrap
Requires:       xdg-dbus-proxy
Recommends:     geoclue2
Recommends:     gstreamer1-plugins-bad-free
Recommends:     gstreamer1-plugins-good
Recommends:     xdg-desktop-portal-gtk
Provides:       bundled(angle)
Provides:       bundled(pdfjs)
Provides:       bundled(xdgmime)

%description -n webkit2gtk4.1
WebKitGTK is the port of the WebKit web rendering engine to the
GTK platform. This package contains WebKitGTK for GTK 3 and libsoup 3.

%package -n     webkit2gtk4.0
Summary:        WebKitGTK for GTK 3 and libsoup 2
Requires:       javascriptcoregtk4.0%{?_isa} = %{version}-%{release}
Requires:       bubblewrap
Requires:       xdg-dbus-proxy
Recommends:     geoclue2
Recommends:     gstreamer1-plugins-bad-free
Recommends:     gstreamer1-plugins-good
Recommends:     xdg-desktop-portal-gtk
Provides:       bundled(angle)
Provides:       bundled(pdfjs)
Provides:       bundled(xdgmime)
Obsoletes:      webkitgtk4 < %{version}-%{release}
Provides:       webkitgtk4 = %{version}-%{release}
Obsoletes:      webkit2gtk3 < %{version}-%{release}
Provides:       webkit2gtk3 = %{version}-%{release}

%description -n webkit2gtk4.0
WebKitGTK is the port of the WebKit web rendering engine to the
GTK platform. This package contains WebKitGTK for GTK 3 and libsoup 2.

%package -n     webkitgtk6.0-devel
Summary:        Development files for webkitgtk6.0
Requires:       webkitgtk6.0%{?_isa} = %{version}-%{release}
Requires:       javascriptcoregtk6.0%{?_isa} = %{version}-%{release}
Requires:       javascriptcoregtk6.0-devel%{?_isa} = %{version}-%{release}
Obsoletes:      webkit2gtk5.0-devel < %{version}-%{release}

%description -n webkitgtk6.0-devel
The webkitgtk6.0-devel package contains libraries, build data, and header
files for developing applications that use webkitgtk6.0.

%package -n     webkit2gtk4.1-devel
Summary:        Development files for webkit2gtk4.1
Requires:       webkit2gtk4.1%{?_isa} = %{version}-%{release}
Requires:       javascriptcoregtk4.1%{?_isa} = %{version}-%{release}
Requires:       javascriptcoregtk4.1-devel%{?_isa} = %{version}-%{release}

%description -n webkit2gtk4.1-devel
The webkit2gtk4.1-devel package contains libraries, build data, and header
files for developing applications that use webkit2gtk4.1.

%package -n     webkit2gtk4.0-devel
Summary:        Development files for webkit2gtk4.0
Requires:       webkit2gtk4.0%{?_isa} = %{version}-%{release}
Requires:       javascriptcoregtk4.0%{?_isa} = %{version}-%{release}
Requires:       javascriptcoregtk4.0-devel%{?_isa} = %{version}-%{release}
Obsoletes:      webkitgtk4-devel < %{version}-%{release}
Provides:       webkitgtk4-devel = %{version}-%{release}
Obsoletes:      webkit2gtk3-devel < %{version}-%{release}
Provides:       webkit2gtk3-devel = %{version}-%{release}

%description -n webkit2gtk4.0-devel
The webkit2gtk4.0-devel package contains libraries, build data, and header
files for developing applications that use webkit2gtk4.0.

%if %{with docs}
%package -n     webkitgtk6.0-doc
Summary:        Documentation files for webkit2gtk5.0
BuildArch:      noarch
Requires:       webkitgtk6.0 = %{version}-%{release}
Obsoletes:      webkit2gtk5.0-doc < %{version}-%{release}
Recommends:     gi-docgen-fonts

%description -n webkitgtk6.0-doc
This package contains developer documentation for webkitgtk6.0.

%package -n     webkit2gtk4.1-doc
Summary:        Documentation files for webkit2gtk4.1
BuildArch:      noarch
Requires:       webkit2gtk4.1 = %{version}-%{release}
Recommends:     gi-docgen-fonts

%description -n webkit2gtk4.1-doc
This package contains developer documentation for webkit2gtk4.1.

%package -n     webkit2gtk4.0-doc
Summary:        Documentation files for webkit2gtk4.0
BuildArch:      noarch
Requires:       webkit2gtk4.0 = %{version}-%{release}
Obsoletes:      webkitgtk4-doc < %{version}-%{release}
Provides:       webkitgtk4-doc = %{version}-%{release}
Obsoletes:      webkit2gtk3-doc < %{version}-%{release}
Provides:       webkit2gtk3-doc = %{version}-%{release}
Recommends:     gi-docgen-fonts

%description -n webkit2gtk4.0-doc
This package contains developer documentation for webkit2gtk4.0.
%endif

%package -n     javascriptcoregtk6.0
Summary:        JavaScript engine from webkitgtk6.0
Obsoletes:      javascriptcoregtk5.0 < %{version}-%{release}

%description -n javascriptcoregtk6.0
This package contains the JavaScript engine from webkitgtk6.0.

%package -n     javascriptcoregtk4.1
Summary:        JavaScript engine from webkit2gtk4.1
Obsoletes:      webkit2gtk4.1-jsc < %{version}-%{release}

%description -n javascriptcoregtk4.1
This package contains the JavaScript engine from webkit2gtk4.1.

%package -n     javascriptcoregtk4.0
Summary:        JavaScript engine from webkit2gtk4.0
Obsoletes:      webkitgtk4-jsc < %{version}-%{release}
Provides:       webkitgtk4-jsc = %{version}-%{release}
Obsoletes:      webkit2gtk3-jsc < %{version}-%{release}
Provides:       webkit2gtk3-jsc = %{version}-%{release}

%description -n javascriptcoregtk4.0
This package contains the JavaScript engine from webkit2gtk4.0.

%package -n     javascriptcoregtk6.0-devel
Summary:        Development files for JavaScript engine from webkitgtk6.0
Requires:       javascriptcoregtk6.0%{?_isa} = %{version}-%{release}
Obsoletes:      javascriptcoregtk5.0-devel < %{version}-%{release}

%description -n javascriptcoregtk6.0-devel
The javascriptcoregtk6.0-devel package contains libraries, build data, and header
files for developing applications that use JavaScript engine from webkitgtk-6.0.

%package -n     javascriptcoregtk4.1-devel
Summary:        Development files for JavaScript engine from webkit2gtk4.1
Requires:       javascriptcoregtk4.1%{?_isa} = %{version}-%{release}
Obsoletes:      webkit2gtk4.1-jsc-devel < %{version}-%{release}

%description -n javascriptcoregtk4.1-devel
The javascriptcoregtk4.1-devel package contains libraries, build data, and header
files for developing applications that use JavaScript engine from webkit2gtk-4.1.

%package -n     javascriptcoregtk4.0-devel
Summary:        Development files for JavaScript engine from webkit2gtk4.0
Requires:       javascriptcoregtk4.0%{?_isa} = %{version}-%{release}
Obsoletes:      webkitgtk4-jsc-devel < %{version}-%{release}
Provides:       webkitgtk4-jsc-devel = %{version}-%{release}
Obsoletes:      webkit2gtk3-jsc-devel < %{version}-%{release}
Provides:       webkit2gtk3-jsc-devel = %{version}-%{release}

%description -n javascriptcoregtk4.0-devel
The javascriptcoregtk4.0-devel package contains libraries, build data, and header
files for developing applications that use JavaScript engine from webkit2gtk-4.0.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n webkitgtk-%{version}

%build
# Increase the DIE limit so our debuginfo packages can be size-optimized.
# This previously decreased the size for x86_64 from ~5G to ~1.1G, but as of
# 2022 it's more like 850 MB -> 675 MB. This requires lots of RAM on the
# builders, so only do this for x86_64 to avoid overwhelming non-x86_64
# builders.
# https://bugzilla.redhat.com/show_bug.cgi?id=1456261
%global _dwz_max_die_limit_x86_64 250000000

# Require 32 GB of RAM per vCPU for debuginfo processing. 16 GB is not enough.
%global _find_debuginfo_opts %limit_build -m 32768

# Remove debuginfo from 32-bit builds to reduce memory consumption even more.
# No amount of optimizing is going to work here.
# https://bugs.webkit.org/show_bug.cgi?id=140176
# https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/I6IVNA52TXTBRQLKW45CJ5K4RA4WNGMI/
%ifarch %{ix86}
%global optflags %(echo %{optflags} | sed 's/-g /-g1 /')
%endif

%define _vpath_builddir %{_vendor}-%{_target_os}-build/webkitgtk-6.0
%cmake \
  -GNinja \
  -DPORT=GTK \
  -DCMAKE_BUILD_TYPE=Release \
  -DUSE_GTK4=ON \
%if %{without docs}
  -DENABLE_DOCUMENTATION=OFF \
%endif
%if !0%{?with_gamepad}
  -DENABLE_GAMEPAD=OFF \
%endif
%if 0%{?rhel}
%ifarch aarch64
  -DUSE_64KB_PAGE_BLOCK=ON \
%endif
%endif
  %{nil}

%define _vpath_builddir %{_vendor}-%{_target_os}-build/webkit2gtk-4.1
%cmake \
  -GNinja \
  -DPORT=GTK \
  -DCMAKE_BUILD_TYPE=Release \
  -DENABLE_WEBDRIVER=OFF \
%if %{without docs}
  -DENABLE_DOCUMENTATION=OFF \
%endif
%if !0%{?with_gamepad}
  -DENABLE_GAMEPAD=OFF \
%endif
%if 0%{?rhel}
%ifarch aarch64
  -DUSE_64KB_PAGE_BLOCK=ON \
%endif
%endif
  %{nil}

%define _vpath_builddir %{_vendor}-%{_target_os}-build/webkit2gtk-4.0
%cmake \
  -GNinja \
  -DPORT=GTK \
  -DCMAKE_BUILD_TYPE=Release \
  -DUSE_SOUP2=ON \
  -DENABLE_WEBDRIVER=OFF \
%if %{without docs}
  -DENABLE_DOCUMENTATION=OFF \
%endif
%if !0%{?with_gamepad}
  -DENABLE_GAMEPAD=OFF \
%endif
%if 0%{?rhel}
%ifarch aarch64
  -DUSE_64KB_PAGE_BLOCK=ON \
%endif
%endif
  %{nil}

%define _vpath_builddir %{_vendor}-%{_target_os}-build/webkitgtk-6.0
export NINJA_STATUS="[1/3][%f/%t %es] "
%cmake_build %limit_build -m 3072

%define _vpath_builddir %{_vendor}-%{_target_os}-build/webkit2gtk-4.1
export NINJA_STATUS="[2/3][%f/%t %es] "
%cmake_build %limit_build -m 3072

%define _vpath_builddir %{_vendor}-%{_target_os}-build/webkit2gtk-4.0
export NINJA_STATUS="[3/3][%f/%t %es] "
%cmake_build %limit_build -m 3072

%install
%define _vpath_builddir %{_vendor}-%{_target_os}-build/webkitgtk-6.0
%cmake_install

%define _vpath_builddir %{_vendor}-%{_target_os}-build/webkit2gtk-4.1
%cmake_install

%define _vpath_builddir %{_vendor}-%{_target_os}-build/webkit2gtk-4.0
%cmake_install

%find_lang WebKitGTK-6.0
%find_lang WebKitGTK-4.1
%find_lang WebKitGTK-4.0

# Finally, copy over and rename various files for %%license inclusion
%add_to_license_files Source/JavaScriptCore/COPYING.LIB
%add_to_license_files Source/ThirdParty/ANGLE/LICENSE
%add_to_license_files Source/ThirdParty/ANGLE/src/common/third_party/smhasher/LICENSE
%add_to_license_files Source/ThirdParty/ANGLE/src/third_party/libXNVCtrl/LICENSE
%add_to_license_files Source/WebCore/LICENSE-APPLE
%add_to_license_files Source/WebCore/LICENSE-LGPL-2
%add_to_license_files Source/WebCore/LICENSE-LGPL-2.1
%add_to_license_files Source/WebInspectorUI/UserInterface/External/CodeMirror/LICENSE
%add_to_license_files Source/WebInspectorUI/UserInterface/External/Esprima/LICENSE
%add_to_license_files Source/WebInspectorUI/UserInterface/External/three.js/LICENSE
%add_to_license_files Source/WTF/icu/LICENSE
%add_to_license_files Source/WTF/wtf/dtoa/COPYING
%add_to_license_files Source/WTF/wtf/dtoa/LICENSE

%files -n webkitgtk6.0 -f WebKitGTK-6.0.lang
%license _license_files/*ThirdParty*
%license _license_files/*WebCore*
%license _license_files/*WebInspectorUI*
%license _license_files/*WTF*
%{_libdir}/libwebkitgtk-6.0.so.0*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/WebKit-6.0.typelib
%{_libdir}/girepository-1.0/WebKitWebExtension-6.0.typelib
%{_libdir}/webkitgtk-6.0/
%{_libexecdir}/webkitgtk-6.0/
%exclude %{_libexecdir}/webkitgtk-6.0/MiniBrowser
%exclude %{_libexecdir}/webkitgtk-6.0/jsc
%{_bindir}/WebKitWebDriver

%files -n webkit2gtk4.1 -f WebKitGTK-4.1.lang
%license _license_files/*ThirdParty*
%license _license_files/*WebCore*
%license _license_files/*WebInspectorUI*
%license _license_files/*WTF*
%{_libdir}/libwebkit2gtk-4.1.so.0*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/WebKit2-4.1.typelib
%{_libdir}/girepository-1.0/WebKit2WebExtension-4.1.typelib
%{_libdir}/webkit2gtk-4.1/
%{_libexecdir}/webkit2gtk-4.1/
%exclude %{_libexecdir}/webkit2gtk-4.1/MiniBrowser
%exclude %{_libexecdir}/webkit2gtk-4.1/jsc

%files -n webkit2gtk4.0 -f WebKitGTK-4.0.lang
%license _license_files/*ThirdParty*
%license _license_files/*WebCore*
%license _license_files/*WebInspectorUI*
%license _license_files/*WTF*
%{_libdir}/libwebkit2gtk-4.0.so.37*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/WebKit2-4.0.typelib
%{_libdir}/girepository-1.0/WebKit2WebExtension-4.0.typelib
%{_libdir}/webkit2gtk-4.0/
%{_libexecdir}/webkit2gtk-4.0/
%exclude %{_libexecdir}/webkit2gtk-4.0/MiniBrowser
%exclude %{_libexecdir}/webkit2gtk-4.0/jsc

%files -n webkitgtk6.0-devel
%{_libexecdir}/webkitgtk-6.0/MiniBrowser
%{_includedir}/webkitgtk-6.0/
%exclude %{_includedir}/webkitgtk-6.0/JavaScriptCore
%exclude %{_includedir}/webkitgtk-6.0/jsc
%{_libdir}/libwebkitgtk-6.0.so
%{_libdir}/pkgconfig/webkitgtk-6.0.pc
%{_libdir}/pkgconfig/webkitgtk-web-extension-6.0.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/WebKit-6.0.gir
%{_datadir}/gir-1.0/WebKitWebExtension-6.0.gir

%files -n webkit2gtk4.1-devel
%{_libexecdir}/webkit2gtk-4.1/MiniBrowser
%{_includedir}/webkitgtk-4.1/
%exclude %{_includedir}/webkitgtk-4.1/JavaScriptCore
%exclude %{_includedir}/webkitgtk-4.1/jsc
%{_libdir}/libwebkit2gtk-4.1.so
%{_libdir}/pkgconfig/webkit2gtk-4.1.pc
%{_libdir}/pkgconfig/webkit2gtk-web-extension-4.1.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/WebKit2-4.1.gir
%{_datadir}/gir-1.0/WebKit2WebExtension-4.1.gir

%files -n webkit2gtk4.0-devel
%{_libexecdir}/webkit2gtk-4.0/MiniBrowser
%{_includedir}/webkitgtk-4.0/
%exclude %{_includedir}/webkitgtk-4.0/JavaScriptCore
%exclude %{_includedir}/webkitgtk-4.0/jsc
%{_libdir}/libwebkit2gtk-4.0.so
%{_libdir}/pkgconfig/webkit2gtk-4.0.pc
%{_libdir}/pkgconfig/webkit2gtk-web-extension-4.0.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/WebKit2-4.0.gir
%{_datadir}/gir-1.0/WebKit2WebExtension-4.0.gir

%files -n javascriptcoregtk6.0
%license _license_files/*JavaScriptCore*
%{_libdir}/libjavascriptcoregtk-6.0.so.0*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/JavaScriptCore-6.0.typelib

%files -n javascriptcoregtk4.1
%license _license_files/*JavaScriptCore*
%{_libdir}/libjavascriptcoregtk-4.1.so.0*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/JavaScriptCore-4.1.typelib

%files -n javascriptcoregtk4.0
%license _license_files/*JavaScriptCore*
%{_libdir}/libjavascriptcoregtk-4.0.so.18*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/JavaScriptCore-4.0.typelib

%files -n javascriptcoregtk6.0-devel
%{_libexecdir}/webkitgtk-6.0/jsc
%dir %{_includedir}/webkitgtk-6.0
%{_includedir}/webkitgtk-6.0/JavaScriptCore/
%{_includedir}/webkitgtk-6.0/jsc/
%{_libdir}/libjavascriptcoregtk-6.0.so
%{_libdir}/pkgconfig/javascriptcoregtk-6.0.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/JavaScriptCore-6.0.gir

%files -n javascriptcoregtk4.1-devel
%{_libexecdir}/webkit2gtk-4.1/jsc
%dir %{_includedir}/webkitgtk-4.1
%{_includedir}/webkitgtk-4.1/JavaScriptCore/
%{_includedir}/webkitgtk-4.1/jsc/
%{_libdir}/libjavascriptcoregtk-4.1.so
%{_libdir}/pkgconfig/javascriptcoregtk-4.1.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/JavaScriptCore-4.1.gir

%files -n javascriptcoregtk4.0-devel
%{_libexecdir}/webkit2gtk-4.0/jsc
%dir %{_includedir}/webkitgtk-4.0
%{_includedir}/webkitgtk-4.0/JavaScriptCore/
%{_includedir}/webkitgtk-4.0/jsc/
%{_libdir}/libjavascriptcoregtk-4.0.so
%{_libdir}/pkgconfig/javascriptcoregtk-4.0.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/JavaScriptCore-4.0.gir

%if %{with docs}
%files -n webkitgtk6.0-doc
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/javascriptcoregtk-6.0/
%{_datadir}/gtk-doc/html/webkitgtk-6.0/
%{_datadir}/gtk-doc/html/webkitgtk-web-extension-6.0/

%files -n webkit2gtk4.1-doc
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/javascriptcoregtk-4.1/
%{_datadir}/gtk-doc/html/webkit2gtk-4.1/
%{_datadir}/gtk-doc/html/webkit2gtk-web-extension-4.1/

%files -n webkit2gtk4.0-doc
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/javascriptcoregtk-4.0/
%{_datadir}/gtk-doc/html/webkit2gtk-4.0/
%{_datadir}/gtk-doc/html/webkit2gtk-web-extension-4.0/
%endif

%changelog
%autochangelog
