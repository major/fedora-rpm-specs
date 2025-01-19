%{?mingw_package_header}

%global mingw_build_win32 1
%global mingw_build_win64 1

%global mingw_pkg_name wxWidgets

Summary:       MinGW port of the wxWidgets GUI library
Name:          mingw-%{mingw_pkg_name}
Version:       2.8.12
Release:       40%{?dist}
License:       LGPL-2.0-or-later WITH WxWindows-exception-3.1

URL:           http://wxwidgets.org
Source:        http://prdownloads.sourceforge.net/wxwindows/wxWidgets-%{version}.tar.gz
Patch0:        wxWidgets-2.8.12-mingw64-1.patch
Patch1:        wxWidgets-2.8.12-strtoull.patch
BuildArch:     noarch
BuildRequires: make
BuildRequires: mingw32-filesystem >= 68
BuildRequires: mingw64-filesystem >= 68
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw32-expat
BuildRequires: mingw64-expat
BuildRequires: mingw32-libjpeg
BuildRequires: mingw64-libjpeg
BuildRequires: mingw32-libpng
BuildRequires: mingw64-libpng
BuildRequires: mingw32-libtiff
BuildRequires: mingw64-libtiff
BuildRequires: mingw32-zlib
BuildRequires: mingw64-zlib
BuildRequires: gettext

%description
wxWidgets is the C++ cross-platform GUI library, offering classes for all
common GUI controls as well as a comprehensive set of helper classes for most
common application tasks, ranging from networking to HTML display and image
manipulation.

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:		%{summary}

%description -n mingw32-%{mingw_pkg_name}
wxWidgets is the C++ cross-platform GUI library, offering classes for all
common GUI controls as well as a comprehensive set of helper classes for most
common application tasks, ranging from networking to HTML display and image
manipulation.

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:		%{summary}

%description -n mingw64-%{mingw_pkg_name}
wxWidgets is the C++ cross-platform GUI library, offering classes for all
common GUI controls as well as a comprehensive set of helper classes for most
common application tasks, ranging from networking to HTML display and image
manipulation.

# Mingw32 static
%package -n mingw32-%{mingw_pkg_name}-static
Summary:  Static libraries for mingw32-%{mingw_pkg_name} development
Requires: mingw32-%{mingw_pkg_name} = %{version}-%{release}

%description -n mingw32-%{mingw_pkg_name}-static
The mingw32-%{mingw_pkg_name}-static package contains static library for
mingw32-%{mingw_pkg_name} development.

# Mingw64 static
%package -n mingw64-%{mingw_pkg_name}-static
Summary:  Static libraries for mingw64-%{mingw_pkg_name} development
Requires: mingw64-%{mingw_pkg_name} = %{version}-%{release}

%description -n mingw64-%{mingw_pkg_name}-static
The mingw64-%{mingw_pkg_name}-static package contains static library for
mingw64-%{mingw_pkg_name} development.

%{?mingw_debug_package}

%prep
%setup -q -n wxWidgets-%{version}
%patch -P0 -p1 -b .mingw64
%patch -P1 -p1 -b .strtoull

#==========================================
%build
export MINGW32_CXXFLAGS="%{mingw32_cflags} -Wno-narrowing"
export MINGW64_CXXFLAGS="%{mingw64_cflags} -Wno-narrowing"

#========= Shared Libraries ==========
export MINGW_BUILDDIR_SUFFIX=_shared
%mingw_configure --enable-shared \
  --with-msw \
  --with-sdl \
  --enable-unicode \
  --enable-optimise \
  --with-regex=builtin \
  --disable-rpath \
  --without-subdirs

#Try to reduce linker memory footprint
sed -e 's|^CXXFLAGS = |CXXFLAGS = -fpermissive -fno-keep-inline-dllexport |' < build_win64_shared/Makefile > build_win64_shared/Makefile.xx
mv build_win64_shared/Makefile.xx build_win64_shared/Makefile

%mingw_make %{?_smp_mflags}

#========= Static Libraries ==========
export MINGW_BUILDDIR_SUFFIX=_static
%mingw_configure --disable-shared \
  --with-msw \
  --with-sdl \
  --enable-unicode \
  --enable-optimise \
  --with-regex=builtin \
  --disable-rpath \
  --without-subdirs

#TODO verify this doesn't overwrite anything from the shared build
%mingw_make %{?_smp_mflags}

#========= Locale ====================
make -C locale allmo

#==========================================
%install
export MINGW_BUILDDIR_SUFFIX=_shared
%mingw_make install DESTDIR=$RPM_BUILD_ROOT
export MINGW_BUILDDIR_SUFFIX=_static
%mingw_make install DESTDIR=$RPM_BUILD_ROOT
if ls $RPM_BUILD_ROOT%{mingw32_libdir}/*.dll ; then
  mv $RPM_BUILD_ROOT%{mingw32_libdir}/*.dll $RPM_BUILD_ROOT%{mingw32_bindir}
else
  echo "No 32bit shared libraries found."
fi
if ls $RPM_BUILD_ROOT%{mingw64_libdir}/*.dll ; then
  mv $RPM_BUILD_ROOT%{mingw64_libdir}/*.dll $RPM_BUILD_ROOT%{mingw64_bindir}
else
  echo "No 32bit shared libraries found."
fi

# we need to modify the absolute wx-config link to be relative or rpm complains
# (and our package wouldn't be relocatable)
wx_config_filename=$(basename $RPM_BUILD_ROOT%{mingw32_libdir}/wx/config/%{mingw32_target}-*-release-[0-9]*)
ln -sf ../lib/wx/config/$wx_config_filename $RPM_BUILD_ROOT%{mingw32_bindir}/wx-config
wx_config_filename=$(basename $RPM_BUILD_ROOT%{mingw64_libdir}/wx/config/%{mingw64_target}-*-release-[0-9]*)
ln -sf ../lib/wx/config/$wx_config_filename $RPM_BUILD_ROOT%{mingw64_bindir}/wx-config

# remove bakefiles for now until we have a working bakefile setup for mingw32
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/bakefile
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/bakefile

# find locale files
%find_lang wxstd
%find_lang wxmsw

%files -n mingw32-%{mingw_pkg_name} -f wxstd.lang -f wxmsw.lang
%doc docs/licence.txt docs/licendoc.txt docs/lgpl.txt docs/gpl.txt
%{mingw32_bindir}/wx-config
%{mingw32_bindir}/wxbase28u_gcc_custom.dll
%{mingw32_bindir}/wxbase28u_net_gcc_custom.dll
%{mingw32_bindir}/wxbase28u_xml_gcc_custom.dll
%{mingw32_bindir}/wxmsw28u_adv_gcc_custom.dll
%{mingw32_bindir}/wxmsw28u_aui_gcc_custom.dll
%{mingw32_bindir}/wxmsw28u_core_gcc_custom.dll
%{mingw32_bindir}/wxmsw28u_html_gcc_custom.dll
%{mingw32_bindir}/wxmsw28u_qa_gcc_custom.dll
%{mingw32_bindir}/wxmsw28u_richtext_gcc_custom.dll
%{mingw32_bindir}/wxmsw28u_xrc_gcc_custom.dll
%{mingw32_includedir}/wx-2.8
%{mingw32_libdir}/libwx_baseu-2.8-%{mingw32_target}.dll.a
%{mingw32_libdir}/libwx_baseu_net-2.8-%{mingw32_target}.dll.a
%{mingw32_libdir}/libwx_baseu_xml-2.8-%{mingw32_target}.dll.a
%{mingw32_libdir}/libwx_mswu_adv-2.8-%{mingw32_target}.dll.a
%{mingw32_libdir}/libwx_mswu_aui-2.8-%{mingw32_target}.dll.a
%{mingw32_libdir}/libwx_mswu_core-2.8-%{mingw32_target}.dll.a
%{mingw32_libdir}/libwx_mswu_html-2.8-%{mingw32_target}.dll.a
%{mingw32_libdir}/libwx_mswu_qa-2.8-%{mingw32_target}.dll.a
%{mingw32_libdir}/libwx_mswu_richtext-2.8-%{mingw32_target}.dll.a
%{mingw32_libdir}/libwx_mswu_xrc-2.8-%{mingw32_target}.dll.a
%dir %{mingw32_libdir}/wx
%dir %{mingw32_libdir}/wx/config
%{mingw32_libdir}/wx/config/%{mingw32_target}-msw-unicode-release-2.8
%dir %{mingw32_libdir}/wx/include
%{mingw32_libdir}/wx/include/%{mingw32_target}-msw-unicode-release-2.8
%{mingw32_datadir}/aclocal/wxwin.m4
#{mingw32_datadir}/bakefile
#{mingw32_datadir}/bakefile/presets
#{mingw32_datadir}/bakefile/presets/wx.bkl
#{mingw32_datadir}/bakefile/presets/wx_unix.bkl
#{mingw32_datadir}/bakefile/presets/wx_win32.bkl

%files -n mingw32-%{mingw_pkg_name}-static
%{mingw32_libdir}/libwx_baseu-2.8-%{mingw32_target}.a
%{mingw32_libdir}/libwx_baseu_net-2.8-%{mingw32_target}.a
%{mingw32_libdir}/libwx_baseu_xml-2.8-%{mingw32_target}.a
%{mingw32_libdir}/libwx_mswu_adv-2.8-%{mingw32_target}.a
%{mingw32_libdir}/libwx_mswu_aui-2.8-%{mingw32_target}.a
%{mingw32_libdir}/libwx_mswu_core-2.8-%{mingw32_target}.a
%{mingw32_libdir}/libwx_mswu_html-2.8-%{mingw32_target}.a
%{mingw32_libdir}/libwx_mswu_qa-2.8-%{mingw32_target}.a
%{mingw32_libdir}/libwx_mswu_richtext-2.8-%{mingw32_target}.a
%{mingw32_libdir}/libwx_mswu_xrc-2.8-%{mingw32_target}.a
%{mingw32_libdir}/libwxregexu-2.8-%{mingw32_target}.a
%{mingw32_libdir}/wx/config/%{mingw32_target}-msw-unicode-release-static-2.8
%{mingw32_libdir}/wx/include/%{mingw32_target}-msw-unicode-release-static-2.8

%files -n mingw64-%{mingw_pkg_name} -f wxstd.lang -f wxmsw.lang
%doc docs/licence.txt docs/licendoc.txt docs/lgpl.txt docs/gpl.txt
%{mingw64_bindir}/wx-config
%{mingw64_bindir}/wxbase28u_gcc_custom.dll
%{mingw64_bindir}/wxbase28u_net_gcc_custom.dll
%{mingw64_bindir}/wxbase28u_xml_gcc_custom.dll
%{mingw64_bindir}/wxmsw28u_adv_gcc_custom.dll
%{mingw64_bindir}/wxmsw28u_aui_gcc_custom.dll
%{mingw64_bindir}/wxmsw28u_core_gcc_custom.dll
%{mingw64_bindir}/wxmsw28u_html_gcc_custom.dll
%{mingw64_bindir}/wxmsw28u_qa_gcc_custom.dll
%{mingw64_bindir}/wxmsw28u_richtext_gcc_custom.dll
%{mingw64_bindir}/wxmsw28u_xrc_gcc_custom.dll
%{mingw64_includedir}/wx-2.8
%{mingw64_libdir}/libwx_baseu-2.8-%{mingw64_target}.dll.a
%{mingw64_libdir}/libwx_baseu_net-2.8-%{mingw64_target}.dll.a
%{mingw64_libdir}/libwx_baseu_xml-2.8-%{mingw64_target}.dll.a
%{mingw64_libdir}/libwx_mswu_adv-2.8-%{mingw64_target}.dll.a
%{mingw64_libdir}/libwx_mswu_aui-2.8-%{mingw64_target}.dll.a
%{mingw64_libdir}/libwx_mswu_core-2.8-%{mingw64_target}.dll.a
%{mingw64_libdir}/libwx_mswu_html-2.8-%{mingw64_target}.dll.a
%{mingw64_libdir}/libwx_mswu_qa-2.8-%{mingw64_target}.dll.a
%{mingw64_libdir}/libwx_mswu_richtext-2.8-%{mingw64_target}.dll.a
%{mingw64_libdir}/libwx_mswu_xrc-2.8-%{mingw64_target}.dll.a
%dir %{mingw64_libdir}/wx
%dir %{mingw64_libdir}/wx/config
%{mingw64_libdir}/wx/config/%{mingw64_target}-msw-unicode-release-2.8
%dir %{mingw64_libdir}/wx/include
%{mingw64_libdir}/wx/include/%{mingw64_target}-msw-unicode-release-2.8
%{mingw64_datadir}/aclocal/wxwin.m4
#{mingw64_datadir}/bakefile
#{mingw64_datadir}/bakefile/presets
#{mingw64_datadir}/bakefile/presets/wx.bkl
#{mingw64_datadir}/bakefile/presets/wx_unix.bkl
#{mingw64_datadir}/bakefile/presets/wx_win32.bkl

%files -n mingw64-%{mingw_pkg_name}-static
%{mingw64_libdir}/libwx_baseu-2.8-%{mingw64_target}.a
%{mingw64_libdir}/libwx_baseu_net-2.8-%{mingw64_target}.a
%{mingw64_libdir}/libwx_baseu_xml-2.8-%{mingw64_target}.a
%{mingw64_libdir}/libwx_mswu_adv-2.8-%{mingw64_target}.a
%{mingw64_libdir}/libwx_mswu_aui-2.8-%{mingw64_target}.a
%{mingw64_libdir}/libwx_mswu_core-2.8-%{mingw64_target}.a
%{mingw64_libdir}/libwx_mswu_html-2.8-%{mingw64_target}.a
%{mingw64_libdir}/libwx_mswu_qa-2.8-%{mingw64_target}.a
%{mingw64_libdir}/libwx_mswu_richtext-2.8-%{mingw64_target}.a
%{mingw64_libdir}/libwx_mswu_xrc-2.8-%{mingw64_target}.a
%{mingw64_libdir}/libwxregexu-2.8-%{mingw64_target}.a
%{mingw64_libdir}/wx/config/%{mingw64_target}-msw-unicode-release-static-2.8
%{mingw64_libdir}/wx/include/%{mingw64_target}-msw-unicode-release-static-2.8


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.12-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.12-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.12-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.12-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.12-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.12-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 2.8.12-34
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.12-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.12-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.12-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 03 2020 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.8.12-30
- rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.12-30
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.12-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.12-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 2.8.12-27
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.12-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.12-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.12-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.12-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.12-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.12-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.12-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 12 2015 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.8.12-19
- rebuild due to __GXX_ABI_VERSION change from 1008 to 1009

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.12-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Feb 19 2015 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.8.12-17
- make wxString::ToULongLong work

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.12-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.12-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 13 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.8.12-14
- Rebuild against libpng 1.6

* Sun Jan 27 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.8.12-13
- Rebuild against mingw-gcc 4.8 (win64 uses SEH exceptions now)

* Sat Aug 25 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.8.12-12
- Rebuild against latest libtiff

* Mon Aug 13 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.8.12-11
- enable 64bit build

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.8.12-9
- Rebuild against the mingw-w64 toolchain

* Tue Jan 31 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.8.12-8
- Rebuild for libpng 1.5
- Dropped the png patch
- Dropped the dependency extraction overrides as that's done automatically as of RPM 4.9

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 22 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.8.12-6
- reinstate italian mo file

* Sun Jun 19 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.8.12-5
- build mo files (reported by Fritz Elfert)

* Fri Jun 03 2011 Kalev Lember <kalev@smartlink.ee> - 2.8.12-4
- Rebuilt with mingw32-libjpeg-turbo, dropped jpeg_boolean patch (#604702)

* Mon May 23 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.8.12-3
- transition to new package naming scheme

* Thu May  5 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.8.12-2
- include license file

* Wed May  4 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.8.12-1
- update to 2.8.12
- remove buildroot, defattr, clean

* Tue Apr 19 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.8.11-1
- update to 2.8.11

* Tue Sep 8 2009 Michael Ansel <michael.ansel@gmail.com> - 2.8.10-1
- update to 2.8.10

* Tue Sep 8 2009 Michael Ansel <michael.ansel@gmail.com> - 2.8.9-3
- Adjust to Fedora packaging guidelines

* Wed Aug 26 2009 Michael Ansel <michael.ansel@gmail.com> - 2.8.9-2
- update for Fedora 11 (mingw -> mingw32)
- use mingw32 macros
- add static subpackage

* Thu Dec 18 2008 Keiichi Takahashi <bitwalk@users.soureforge.net> - 2.8.9-1
- update to 2.8.9

* Tue Aug 12 2008 Keiichi Takahashi <bitwalk@users.soureforge.net> - 2.8.8-1
- update to 2.8.8

* Sat Mar 15 2008 Keiichi Takahashi <bitwalk@users.soureforge.net> - 2.8.7-2
- rebuilt with current libraries.
- add BuildPrereq and Requires more explicitly.

* Thu Feb 28 2008 Keiichi Takahashi <bitwalk@users.soureforge.net> - 2.8.7-1
- initial release

