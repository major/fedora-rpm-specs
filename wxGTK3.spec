%global srcname wxWidgets
%global wxgtkname wxGTK3
%global wxbasename wxBase3
%global wxwidgetsgtk2 compat-wxWidgets-gtk2
%global wxgtk2name compat-wxGTK3-gtk2
%global wxbasegtk2name compat-wxBase3-gtk2
%global gtk2dir bld_gtk2
%global gtk3dir bld_gtk3

#For git snapshots, set to 0 to use release instead:
%global usesnapshot 0
%if 0%{?usesnapshot}
%global commit0 e4293e9e39d2d6e7757ed5907ce66d2847d8e16a
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global snapshottag .git%{shortcommit0}
%endif
%global builddocs 1

Name:           %{wxgtkname}
Version:        3.0.5.1
Release:        9%{?snapshottag}%{?dist}
Summary:        GTK port of the wxWidgets GUI library
License:        wxWidgets
URL:            https://www.wxwidgets.org/

%if 0%{?usesnapshot}
Source0:        https://github.com/%{srcname}/%{srcname}/archive/%{commit0}.tar.gz#/%{srcname}-%{shortcommit0}.tar.gz
%else
Source0:        https://github.com/%{srcname}/%{srcname}/releases/download/v%{version}/%{srcname}-%{version}.tar.bz2
%endif
%if ! 0%{?builddocs}
Source1:        https://github.com/%{srcname}/%{srcname}/releases/download/v%{version}/%{srcname}-%{version}-docs-html.tar.bz2
%endif
Source10:       wx-config
# https://bugzilla.redhat.com/show_bug.cgi?id=1225148
# remove abort when ABI check fails
# Backport from wxGTK
Patch0:         %{name}-3.0.3-abicheck.patch
Patch1:         fix-filename-test.patch
Patch2:         fix-vararg-test.patch
Patch3:         force-x11-for-wxgl.patch
Patch4: wxGTK-configure-c99.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel
BuildRequires:  gtk3-devel
BuildRequires:  webkit2gtk3-devel
BuildRequires:  zlib-devel
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  expat-devel
BuildRequires:  SDL2-devel
BuildRequires:  libGLU-devel
BuildRequires:  libSM-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  gettext
BuildRequires:  cppunit-devel
BuildRequires:  libmspack-devel
BuildRequires:  doxygen
BuildRequires:  graphviz

Provides:       %{srcname} = %{version}-%{release}
Provides:       bundled(scintilla) = 3.2.1
Requires:       %{wxbasename}%{?_isa} = %{version}-%{release}
Requires:       %{name}-i18n = %{version}-%{release}

%description
wxWidgets is the GTK port of the C++ cross-platform wxWidgets
GUI library, offering classes for all common GUI controls as well as a
comprehensive set of helper classes for most common application tasks,
ranging from networking to HTML display and image manipulation.


%package -n     %{wxgtk2name}
Summary:        GTK port of the wxWidgets GUI library
Provides:       %{wxwidgetsgtk2} = %{version}-%{release}
Provides:       bundled(scintilla) = 3.2.1
Requires:       %{wxbasename}%{?_isa} = %{version}-%{release}
Requires:       %{name}-i18n = %{version}-%{release}

%description -n %{wxgtk2name}
wxWidgets is the GTK port of the C++ cross-platform wxWidgets
GUI library, offering classes for all common GUI controls as well as a
comprehensive set of helper classes for most common application tasks,
ranging from networking to HTML display and image manipulation.


%package -n     %{wxbasename}-devel
Summary:        Development files for the wxBase3 library
Requires:       %{wxbasename}%{?_isa} = %{version}-%{release}
Requires(post): /usr/sbin/update-alternatives
Requires(postun): /usr/sbin/update-alternatives

%description -n %{wxbasename}-devel
This package include files needed to link with the wxBase3 library.
wxWidgets is the GTK port of the C++ cross-platform wxWidgets
GUI library, offering classes for all common GUI controls as well as a
comprehensive set of helper classes for most common application tasks,
ranging from networking to HTML display and image manipulation.


%package        devel
Summary:        Development files for the wxGTK3 library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-gl = %{version}-%{release}
Requires:       %{name}-media = %{version}-%{release}
Requires:       %{name}-webview = %{version}-%{release}
Requires:       %{wxbasename} = %{version}-%{release}
Requires:       %{wxbasename}-devel%{?_isa} = %{version}-%{release}
Requires:       gtk3-devel
Requires:       libGLU-devel
Provides:       %{srcname}-devel = %{version}-%{release}

%description devel
This package include files needed to link with the wxGTK3 library.
wxWidgets is the GTK port of the C++ cross-platform wxWidgets
GUI library, offering classes for all common GUI controls as well as a
comprehensive set of helper classes for most common application tasks,
ranging from networking to HTML display and image manipulation.


%package -n     %{wxgtk2name}-devel
Summary:        Development files for the wxGTK3 library
Requires:       %{wxgtk2name}%{?_isa} = %{version}-%{release}
Requires:       %{wxgtk2name}-gl = %{version}-%{release}
Requires:       %{wxgtk2name}-media = %{version}-%{release}
Requires:       %{wxbasename} = %{version}-%{release}
Requires:       %{wxbasename}-devel%{?_isa} = %{version}-%{release}
Requires:       gtk2-devel
Requires:       libGLU-devel
Provides:       %{wxwidgetsgtk2}-devel = %{version}-%{release}

%description -n %{wxgtk2name}-devel
This package include files needed to link with the wxGTK3 library.
wxWidgets is the GTK port of the C++ cross-platform wxWidgets
GUI library, offering classes for all common GUI controls as well as a
comprehensive set of helper classes for most common application tasks,
ranging from networking to HTML display and image manipulation.


%package        gl
Summary:        OpenGL add-on for the wxWidgets library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description gl
OpenGL (a 3D graphics API) add-on for the wxWidgets library.
wxWidgets is the GTK port of the C++ cross-platform wxWidgets
GUI library, offering classes for all common GUI controls as well as a
comprehensive set of helper classes for most common application tasks,
ranging from networking to HTML display and image manipulation.


%package -n     %{wxgtk2name}-gl
Summary:        OpenGL add-on for the wxWidgets library
Requires:       %{wxgtk2name}%{?_isa} = %{version}-%{release}

%description -n %{wxgtk2name}-gl
OpenGL (a 3D graphics API) add-on for the wxWidgets library.
wxWidgets is the GTK port of the C++ cross-platform wxWidgets
GUI library, offering classes for all common GUI controls as well as a
comprehensive set of helper classes for most common application tasks,
ranging from networking to HTML display and image manipulation.


%package        i18n
Summary:        i18n message catalogs for the wxWidgets library
BuildArch:      noarch

%description i18n
i18n message catalogs for the wxWidgets library.
wxWidgets is the GTK port of the C++ cross-platform wxWidgets
GUI library, offering classes for all common GUI controls as well as a
comprehensive set of helper classes for most common application tasks,
ranging from networking to HTML display and image manipulation.


%package        media
Summary:        Multimedia add-on for the wxWidgets library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description media
Multimedia add-on for the wxWidgets library.
wxWidgets is the GTK port of the C++ cross-platform wxWidgets
GUI library, offering classes for all common GUI controls as well as a
comprehensive set of helper classes for most common application tasks,
ranging from networking to HTML display and image manipulation.


%package -n     %{wxgtk2name}-media
Summary:        Multimedia add-on for the wxWidgets library
Requires:       %{wxgtk2name}%{?_isa} = %{version}-%{release}

%description -n %{wxgtk2name}-media
Multimedia add-on for the wxWidgets library.
wxWidgets is the GTK port of the C++ cross-platform wxWidgets
GUI library, offering classes for all common GUI controls as well as a
comprehensive set of helper classes for most common application tasks,
ranging from networking to HTML display and image manipulation.


%package        webview
Summary:        WebView add-on for the wxWidgets library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description webview
WebView add-on for the wxWidgets library.
wxWidgets is the GTK port of the C++ cross-platform wxWidgets
GUI library, offering classes for all common GUI controls as well as a
comprehensive set of helper classes for most common application tasks,
ranging from networking to HTML display and image manipulation.


%package -n     %{wxbasename}
Summary:        Non-GUI support classes from the wxWidgets library
Provides:       %{wxbasegtk2name} = %{version}-%{release}
Obsoletes:      %{wxbasegtk2name} < %{version}-%{release}

%description -n %{wxbasename}
Every wxWidgets application must link against this library. It contains
mandatory classes that any wxWidgets code depends on (like wxString) and
portability classes that abstract differences between platforms. wxBase can
be used to develop console mode applications -- it does not require any GUI
libraries or the X Window System.


%package        docs
Summary:        Documentation for the wxGTK3 library
Requires:       %{name} = %{version}-%{release}
Provides:       %{srcname}-docs = %{version}-%{release}
Provides:       %{wxwidgetsgtk2}-docs = %{version}-%{release}
Provides:       %{wxgtk2name}-docs = %{version}-%{release}
Obsoletes:      %{wxgtk2name}-docs < %{version}-%{release}
# Remove when F29 EOL
Obsoletes:      %{name}-xmldocs < %{version}-%{release}
Obsoletes:      %{srcname}-xmldocs < %{version}-%{release}
Obsoletes:      %{wxgtk2name}-xmldocs < %{version}-%{release}
BuildArch:      noarch

%description docs
This package provides documentation for the %{srcname} library.


%prep
%if 0%{?usesnapshot}
%autosetup -n %{srcname}-%{commit0} %{!?builddocs:-a 1} -p1
%else
%autosetup -n %{srcname}-%{version} %{!?builddocs:-a 1} -p1
%endif

# patch some installed files to avoid conflicts with 2.8.*
sed -i -e 's|aclocal)|aclocal/wxwin3.m4)|' Makefile.in
sed -i -e 's|wxstd.mo|wxstd3.mo|' Makefile.in
sed -i -e 's|wxmsw.mo|wxmsw3.mo|' Makefile.in

# fix plugin dir for 64-bit
sed -i -e 's|/usr/lib\b|%{_libdir}|' wx-config.in configure
sed -i -e 's|/lib|/%{_lib}|' src/unix/stdpaths.cpp


%build
# likely still dereferences type-punned pointers
CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
CXXFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
# fix unused-direct-shlib-dependency error:
export LDFLAGS="-Wl,--as-needed"

%if 0%{?usesnapshot}
#For snapshots, mo files need to be generated
pushd locale
make allmo
popd
%endif

%global _configure ../configure

mkdir %{gtk2dir}
pushd %{gtk2dir}
%configure \
  --with-gtk=2 \
  --with-opengl \
  --with-sdl \
  --with-gnomeprint \
  --with-libmspack \
  --enable-intl \
  --enable-no_deps \
  --disable-rpath \
  --enable-ipv6

%make_build
popd

mkdir %{gtk3dir}
pushd %{gtk3dir}
%configure \
  --with-gtk=3 \
  --with-opengl \
  --with-sdl \
  --with-gnomeprint \
  --with-libmspack \
  --enable-intl \
  --enable-no_deps \
  --disable-rpath \
  --enable-ipv6

%make_build
popd

#Docs
%if 0%{?builddocs}
WX_SKIP_DOXYGEN_VERSION_CHECK=1 docs/doxygen/regen.sh html
mv docs/doxygen/out/html .
%else
mv %{srcname}-%{version} html
%endif

%install
pushd %{gtk2dir}
%makeinstall
popd

pushd %{gtk3dir}
%makeinstall
popd

# install our multilib-aware wrapper
##Remove installed
rm %{buildroot}%{_bindir}/wx-config
##Install new and symlink
install -p -D -m 755 %{SOURCE10} %{buildroot}%{_libexecdir}/%{name}/wx-config
sed -i -e 's|=/usr|=%{_prefix}|' %{buildroot}%{_libexecdir}/%{name}/wx-config
ln -s ../..%{_libexecdir}/%{name}/wx-config %{buildroot}%{_bindir}/wx-config-3.0
touch %{buildroot}%{_bindir}/wx-config

#Alternatives setup with wxrc
mv %{buildroot}%{_bindir}/wxrc* %{buildroot}%{_libexecdir}/%{name}
ln -s ../..%{_libexecdir}/%{name}/wxrc-3.0 %{buildroot}%{_bindir}/wxrc-3.0
touch %{buildroot}%{_bindir}/wxrc

# move bakefiles to avoid conflicts with 2.8.*
mkdir %{buildroot}%{_datadir}/bakefile/presets/wx3
mv %{buildroot}%{_datadir}/bakefile/presets/*.* %{buildroot}%{_datadir}/bakefile/presets/wx3

%find_lang wxstd3
%find_lang wxmsw3
cat wxmsw3.lang >> wxstd3.lang

%check
pushd %{gtk2dir}/tests
make %{?_smp_mflags}
LD_LIBRARY_PATH=%{buildroot}%{_libdir} TZ=UTC ./test
popd

pushd %{gtk3dir}/tests
make %{?_smp_mflags}
LD_LIBRARY_PATH=%{buildroot}%{_libdir} TZ=UTC ./test
popd

%post -n %{wxbasename}-devel
if [ -f %{_bindir}/wx-config ] && [ ! -h %{_bindir}/wx-config ] ; then
  rm %{_bindir}/wx-config
fi
/usr/sbin/update-alternatives --install %{_bindir}/wx-config \
  wx-config %{_libexecdir}/%{name}/wx-config 30
/usr/sbin/update-alternatives --install %{_bindir}/wxrc \
  wxrc %{_libexecdir}/%{name}/wxrc 30

%postun -n %{wxbasename}-devel
if [ $1 -eq 0 ] ; then
  /usr/sbin/update-alternatives --remove wx-config %{_libexecdir}/%{name}/wx-config
  /usr/sbin/update-alternatives --remove wxrc %{_libexecdir}/%{name}/wxrc
fi

%files
%doc docs/changes.txt docs/gpl.txt docs/lgpl.txt docs/licence.txt
%doc docs/licendoc.txt docs/preamble.txt docs/readme.txt
%{_libdir}/libwx_gtk3u_adv-*.so.*
%{_libdir}/libwx_gtk3u_aui-*.so.*
%{_libdir}/libwx_gtk3u_core-*.so.*
%{_libdir}/libwx_gtk3u_html-*.so.*
%{_libdir}/libwx_gtk3u_propgrid-*.so.*
%{_libdir}/libwx_gtk3u_qa-*.so.*
%{_libdir}/libwx_gtk3u_ribbon-*.so.*
%{_libdir}/libwx_gtk3u_richtext-*.so.*
%{_libdir}/libwx_gtk3u_stc-*.so.*
%{_libdir}/libwx_gtk3u_xrc-*.so.*

%files -n %{wxgtk2name}
%doc docs/changes.txt docs/gpl.txt docs/lgpl.txt docs/licence.txt
%doc docs/licendoc.txt docs/preamble.txt docs/readme.txt
%{_libdir}/libwx_gtk2u_adv-*.so.*
%{_libdir}/libwx_gtk2u_aui-*.so.*
%{_libdir}/libwx_gtk2u_core-*.so.*
%{_libdir}/libwx_gtk2u_html-*.so.*
%{_libdir}/libwx_gtk2u_propgrid-*.so.*
%{_libdir}/libwx_gtk2u_qa-*.so.*
%{_libdir}/libwx_gtk2u_ribbon-*.so.*
%{_libdir}/libwx_gtk2u_richtext-*.so.*
%{_libdir}/libwx_gtk2u_stc-*.so.*
%{_libdir}/libwx_gtk2u_xrc-*.so.*

%files -n %{wxbasename}-devel
%ghost %{_bindir}/wx-config
%ghost %{_bindir}/wxrc
%{_bindir}/wxrc-3.0
%{_bindir}/wx-config-3.0
%{_includedir}/wx-3.0
%{_libdir}/libwx_baseu*.so
%dir %{_libdir}/wx
%dir %{_libdir}/wx/config
%dir %{_libdir}/wx/include
%{_datadir}/aclocal/wxwin3.m4
%{_datadir}/bakefile/presets/wx3
#Exclude some python bitecode
%exclude %{_datadir}/bakefile/presets/wx3/*.pyc
%exclude %{_datadir}/bakefile/presets/wx3/*.pyo
%{_libexecdir}/%{name}

%files devel
%{_libdir}/libwx_gtk3u_*.so
%{_libdir}/wx/config/gtk3-unicode-3.0
%{_libdir}/wx/include/gtk3-unicode-3.0

%files -n %{wxgtk2name}-devel
%{_libdir}/libwx_gtk2u_*.so
%{_libdir}/wx/config/gtk2-unicode-3.0
%{_libdir}/wx/include/gtk2-unicode-3.0

%files gl
%{_libdir}/libwx_gtk3u_gl-*.so.*

%files -n %{wxgtk2name}-gl
%{_libdir}/libwx_gtk2u_gl-*.so.*

%files i18n -f wxstd3.lang

%files media
%{_libdir}/libwx_gtk3u_media-*.so.*

%files -n %{wxgtk2name}-media
%{_libdir}/libwx_gtk2u_media-*.so.*

%files webview
%{_libdir}/libwx_gtk3u_webview-*.so.*
%dir %{_libdir}/wx
%{_libdir}/wx/3.0

%files -n %{wxbasename}
%doc docs/changes.txt docs/gpl.txt docs/lgpl.txt docs/licence.txt
%doc docs/licendoc.txt docs/preamble.txt docs/readme.txt
%{_libdir}/libwx_baseu-*.so.*
%{_libdir}/libwx_baseu_net-*.so.*
%{_libdir}/libwx_baseu_xml-*.so.*

%files docs
%doc html

%changelog
* Mon Jan 09 2023 Florian Weimer <fweimer@redhat.com> - 3.0.5.1-9
- Port configure script to C99

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 06 2021 Orion Poplawski <orion@nwra.com> - 3.0.5.1-6
- Drop unused BR on GConf2-devel

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 06 2021 Scott Talbert <swt@techie.net> - 3.0.5.1-4
- Adobt Debian patch to avoid warning on C++ ABI mismatches (#1957142)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 10 2020 Scott Talbert <swt@techie.net> - 3.0.5.1-1
- Update to new upstream release 3.0.5.1

* Fri Mar 13 2020 Scott Talbert <swt@techie.net> - 3.0.4-15
- Bring back alternatives system for wx-config and wxrc

* Fri Jan 31 2020 Scott Talbert <swt@techie.net> - 3.0.4-14
- Update wx-config error message when wxGTK3-devel is missing (#1795500)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 22 2019 Scott Talbert <swt@techie.net> - 3.0.4-12
- Incorporate patch from Debian to force X11 when using wxGLCanvas

* Thu Sep 19 2019 Scott Talbert <swt@techie.net> - 3.0.4-11
- Force timezone to UTC when running tests (#1753405)

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Scott Talbert <swt@techie.net> - 3.0.4-9
- Add graphviz to BR to fix 'dot' not found error (#1721702)

* Thu Mar 07 2019 Scott Talbert <swt@techie.net> - 3.0.4-8
- Avoid crashing when wxGLCanvas is used on Wayland

* Fri Feb 08 2019 Kalev Lember <klember@redhat.com> - 3.0.4-7
- Remove the alternatives system for wx-config and wxrc

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 21 2018 Scott Talbert <swt@techie.net> - 3.0.4-5
- Remove Group tags
- Remove xmldocs subpackage (never used)
- Remove cppunit workaround (no longer needed)
- Actually run the tests (but not the GUI ones, yet)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Scott Talbert <swt@techie.net> - 3.0.4-3
- Remove ldconfig scriptlets (no longer needed on F28+)

* Sun Mar 18 2018 Richard W.M. Jones <rjones@redhat.com> - 3.0.4-2
- Port wx-config script to RISC-V architecture.

* Fri Mar 09 2018 Scott Talbert <swt@techie.net> - 3.0.4-1
- New upstream release 3.0.4

* Mon Feb 19 2018 Scott Talbert <swt@techie.net> - 3.0.3-10
- Add missing BR for gcc-c++

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Karsten Hopp <karsten@redhat.com> - 3.0.3-8
- fix some conditionals

* Fri Jan 12 2018 Tomas Popela <tpopela@redhat.com> - 3.0.3-7
- Adapt to the webkitgtk4 rename

* Tue Sep 05 2017 Scott Talbert <swt@techie.net> - 3.0.3-6
- Merge with compat-wxGTK3-gtk2

* Wed Aug 30 2017 Scott Talbert <swt@techie.net> - 3.0.3-5
- Add upstream patch for avoiding destruction of TLWs that were never created
- Fixes assert during Filezilla startup (#1484955)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Wed May 03 2017 Scott Talbert <swt@techie.net> - 3.0.3-1
- New upstream release 3.0.3
- Update to latest WebKit2 patch (#1428997)

* Mon Apr 17 2017 Scott Talbert <swt@techie.net> - 3.0.3-0.8.gite4293e9
- Rebuild against SDL2

* Wed Mar 08 2017 Scott Talbert <swt@techie.net> - 3.0.3-0.7.gite4293e9
- Update to newer git snapshot
- Remove GStreamer patch as it has been incorporated upstream

* Sun Mar 05 2017 Scott Talbert <swt@techie.net> - 3.0.3-0.6.gitf90b768
- Add temporary patch for webkit2 port in rawhide, re-enable webview subpackage

* Thu Mar 02 2017 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.3-0.5.gitf90b768
- Disable webview subpackage in rawhide for now

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-0.4.gitf90b768
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 30 2016 Scott Talbert <swt@techie.net> - 3.0.3-0.3.gitf90b768
- Switch to use GStreamer 1.0 (#1402628)

* Wed Dec 28 2016 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.3-0.2.gitf90b768
- Update to newer git snapshot

* Sat Dec 10 2016 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.3-0.1.git9518d52
- Update to git snapshot

* Mon Nov 21 2016 Scott Talbert <swt@techie.net> - 3.0.2-30
- Fix poedit regression in -29 - add paint clipping region patch (#1396747)
- Add patch to change ~wxPGChoicesData from private to protected

* Mon Nov 14 2016 Scott Talbert <swt@techie.net> - 3.0.2-29
- Fix some sizing problems with GTK3 (#1392102)
- Fix non-default window background color with GTK+ >= 3.20 (#1393847)

* Mon Oct 10 2016 Scott Talbert <swt@techie.net> - 3.0.2-28
- Fix rename issues in Filezilla with overlay scrollbars disabled (#1381765)

* Sat Oct 08 2016 Scott Talbert <swt@techie.net> - 3.0.2-27
- Add a -webview subpackage in F26+

* Tue Oct 04 2016 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.2-26
- Memory leak in last patch, add patch to fix it
- Change last patch to 3.0 branch for consistency

* Tue Oct 04 2016 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.2-25
- Add patch to fix bug 1381767
- Clean up spec file with autosetup

* Sat Sep 24 2016 Scott Talbert <swt@techie.net> - 3.0.2-24
- Add patch to fix crash in wxGCDC::DrawEllipticArc()

* Mon Sep 19 2016 Scott Talbert <swt@techie.net> - 3.0.2-23
- Fix alternatives implementation

* Mon Sep 19 2016 Scott Talbert <swt@techie.net> - 3.0.2-22
- Add patch to fix runtime link error due to previous patches

* Tue Sep 13 2016 Scott Talbert <swt@techie.net> - 3.0.2-21
- Add patch to resolve wxGetKeyState() crash on Wayland (#1266743)
- Add patch to fix wxFontEnumerator stop function
- Add patch to fix wxNativeFontInfo::InitFromFont()

* Sun Aug 28 2016 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.2-20
- Fix alternatives with wxGTK (#1077718)

* Mon Apr  4 2016 Tom Callaway <tcallawa@redhat.com> - 3.0.2-19
- Add patch to resolve window sizing issue with gtk 3.19+

* Sun Mar 20 2016 Scott Talbert <swt@techie.net> - 3.0.2-18
- Add patch for wxEVT_MEDIA_XXX event types (for Phoenix)

* Wed Feb 24 2016 Scott Talbert <swt@techie.net> - 3.0.2-17
- Add patch to resolve issue with wxStaticText growing, fixes RH#1282142
- Add patches to resolve issues under Wayland with window sizing, RH#1294229

* Tue Feb 23 2016 Scott Talbert <swt@techie.net> - 3.0.2-16
- Add -xmldocs subpackage containing XML documentation (needed for Phoenix)

* Tue Feb 23 2016 Scott Talbert <swt@techie.net> - 3.0.2-15
- Add GCC6 patches for STC and strings tests
- Adapt cppunit to use pkg-config (cppunit-config has been removed in F24)
- Fixes FTBFS in F24 Rawhide, RH#1308244

* Mon Feb 22 2016 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.2-14
- Should actually fix RH#1294712

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 31 2015 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.2-12
- Remove python artifacts in bakefile dir, causes multilib devel conflict RH#1294712
- Fix package devel not owning created wx3 backfile preset dir
- Add support for MIPS to wx-config RH#1294895
- Wayland Patch

* Thu Nov 5 2015 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.2-11
- Added patch to fix checkbox and radio button issues for f21 onwards

* Sun Nov 1 2015 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.2-10
- Removed depreciated/retired libgnomeprintui22

* Sat Aug 22 2015 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.2-9
- Include spinbutton patch from upstream

* Mon Jun 22 2015 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.2-8
- Include some upstream patches to fix crashes and warnings

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 28 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.2-6
- Don't abort on ABI check, backport from wxGTK

* Mon May 04 2015 Jason L Tibbitts III <tibbs@math.uh.edu> - 3.0.2-5
- Indicate that this package bundles scintilla 3.2.1.

* Thu Feb 26 2015 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.2-4
- Bump to rebuild, fix bug #1210239

* Thu Feb 26 2015 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.2-3
- Bump to rebuild for gcc 5.0 to fix some issues

* Tue Nov 04 2014 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.2-2
- Moving things around again, hopefully fixing RH#1124402
- Adding symlinks to avoid breaking things

* Tue Nov 04 2014 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.2-1
- Update to 3.0.2

* Mon Nov 03 2014 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 3.0.1-5
- Add aarch64 and ppc64le to list of 64-bit architectures

* Tue Sep 30 2014 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.1-4
- Add conflict with wxgtk-devel again, temporary fix until it can be resolved

* Tue Sep 30 2014 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.1-3
- Avoid gtk warnings, fixes RH#1147995
- Moving wxrc and wx-config to libexec instead of renaming
- Misc changes and spec error fixes, fixes RH#1124402

* Sat Jul 5 2014 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.1-1
- Bump to 3.0.1 RH#1076617

* Tue Mar 18 2014 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.0-6
- Removed disable-catch_segvs, see RH#1076617

* Mon Mar 17 2014 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.0-5
- Renable combat28 - without it causes bugs RH#1076617 and a few others

* Wed Feb 19 2014 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.0-4
- Fixed GTK3 bug with wx-config
- Fixed a unused-direct-shlib-dependency error

* Mon Feb 17 2014 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.0-3
- Added patch to avoid build fail on gtk 3.10+
- Reverted patching to make devel package compatible with wxGTK-devel
- Added combatibility for RHEL 6+
- Changed all mention of GTK3 and GTK2 to GTK for consistency

* Mon Feb 10 2014 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.0-2
- Changed to build against gtk3
- Add webkit to build requires
- Removed patching to make devel package compatible with wxGTK-devel
- Disable 2.8.* combatibility (redundant functionality)

* Sat Jan 4 2014 Jeremy Newton <alexjnewt AT hotmail DOT com> - 3.0.0-1
- Initial build of wxwidgets version 3, mostly based on wxGTK spec
