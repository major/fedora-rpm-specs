Name:           cegui06
Version:        0.6.2
Release:        48%{?dist}
Summary:        CEGUI library 0.6 for apps which need this specific version
# Automatically converted from old format: MIT and LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-MIT AND LicenseRef-Callaway-LGPLv2+
URL:            http://www.cegui.org.uk
# This is
# http://downloads.sourceforge.net/crayzedsgui/CEGUI-0.6.2b.tar.gz
# with the bundled GLEW: RendererModules/OpenGLGUIRenderer/GLEW
# removed as its an older GLEW version which contains
# parts under then non Free SGI OpenGL and GLX licenses
# To regenerate do:
# wget http://downloads.sourceforge.net/crayzedsgui/CEGUI-0.6.2b.tar.gz
# tar xvfz CEGUI-0.6.2b.tar.gz'
# rm -r CEGUI-0.6.2/RendererModules/OpenGLGUIRenderer/GLEW
# tar cvfz CEGUI-0.6.2b-clean.tar.gz
Source0:        CEGUI-0.6.2b-clean.tar.gz
# Both submitted upstream: http://www.cegui.org.uk/mantis/view.php?id=197
Patch1:         cegui-0.6.0-release-as-so-ver.patch
Patch2:         cegui-0.6.0-userverso.patch
# TODO: submit upstream
Patch3:         cegui-0.6.2-new-DevIL.patch
Patch4:         cegui-0.6.2-new-tinyxml.patch
Patch5:         cegui-0.6.2-gcc46.patch
Patch6:         cegui-0.6.2-pcre2.patch
BuildRequires:  gcc-c++
BuildRequires:  expat-devel
BuildRequires:  freetype-devel > 2.0.0
BuildRequires:  libICE-devel
BuildRequires:  libGLU-devel
BuildRequires:  libSM-devel
BuildRequires:  pcre2-devel
BuildRequires:  glew-devel
BuildRequires:  freeimage-devel
BuildRequires:  make

%description
Crazy Eddie's GUI System is a free library providing windowing and widgets for
graphics APIs / engines. This package contains the older version 0.6 for
apps which cannot be easily ported to 0.7. As such this version has been build
without additional image codecs or xml parsers.


%package devel
Summary:        Development files for cegui06
Requires:       %{name} = %{version}-%{release}
Requires:       libGLU-devel

%description devel
Development files for cegui06


%prep
%autosetup -p1 -n CEGUI-%{version}

# Permission fixes for debuginfo RPM
chmod -x include/falagard/*.h

# Encoding fixes
iconv -f iso8859-1 AUTHORS -t utf8 > AUTHORS.conv && mv -f AUTHORS.conv AUTHORS
iconv -f iso8859-1 TODO -t utf8 > TODO.conv && mv -f TODO.conv TODO
iconv -f iso8859-1 README -t utf8 > README.conv && mv -f README.conv README

# Make makefile happy even though we've removed the (unused) included copy of
# GLEW due to license reasons
mkdir -p RendererModules/OpenGLGUIRenderer/GLEW/GL
touch RendererModules/OpenGLGUIRenderer/GLEW/GL/glew.h
touch RendererModules/OpenGLGUIRenderer/GLEW/GL/glxew.h
touch RendererModules/OpenGLGUIRenderer/GLEW/GL/wglew.h
touch RendererModules/OpenGLGUIRenderer/GLEW/GLEW-LICENSE


%build
# configure part of pcre2 change, easier/cleaner to do with sed
sed -i 's|libpcre|libpcre2-8|g' configure
%configure --disable-static --disable-samples --disable-lua-module \
    --disable-corona --disable-devil --disable-silly \
    --disable-irrlicht-renderer --disable-directfb-renderer \
    --disable-xerces-c --disable-libxml --disable-tinyxml \
    --with-default-xml-parser=ExpatParser \
    --with-default-image-codec=FreeImageImageCodec \
    --with-pic
# We do not want to get linked against a system copy of ourselves!
sed -i 's|-L%{_libdir}||g' RendererModules/OpenGLGUIRenderer/Makefile
# Don't use rpath!
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# Move some things around to make cegui06-devel co-exist peacefully with
# cegui-devel
mkdir -p %{buildroot}/%{_libdir}/CEGUI-0.6
for i in libCEGUIBase libCEGUIExpatParser libCEGUIFalagardWRBase \
         libCEGUIOpenGLRenderer libCEGUITGAImageCodec \
         libCEGUIFreeImageImageCodec; do
    rm %{buildroot}/%{_libdir}/$i.so
    ln -s ../$i-%{version}.so %{buildroot}/%{_libdir}/CEGUI-0.6/$i.so
done
mv %{buildroot}/%{_includedir}/CEGUI %{buildroot}/%{_includedir}/CEGUI-0.6
mv %{buildroot}/%{_datadir}/CEGUI %{buildroot}/%{_datadir}/CEGUI-0.6
sed -e 's|/CEGUI|/CEGUI-0.6|g' \
    -e 's|libdir=%{_libdir}|libdir=%{_libdir}/CEGUI-0.6|g' \
    -i %{buildroot}/%{_libdir}/pkgconfig/*.pc
for i in %{buildroot}/%{_libdir}/pkgconfig/*.pc; do
    mv $i `echo $i | sed 's|\.pc\$|-0.6.pc|'`
done


%ldconfig_scriptlets


%files
%doc AUTHORS ChangeLog COPYING README TODO
%{_libdir}/libCEGUI*-%{version}.so

%files devel
%{_libdir}/CEGUI-0.6
%{_libdir}/pkgconfig/CEGUI-OPENGL-0.6.pc
%{_libdir}/pkgconfig/CEGUI-0.6.pc
%{_includedir}/CEGUI-0.6
%{_datadir}/CEGUI-0.6


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 0.6.2-47
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep 30 2022 Hans de Goede <hdegoede@redhat.com> - 0.6.2-40
- Port to PCRE2 (rhbz#2128275)
- CEGUI is no longer maintained upstream and should not be used for new
  projects, drop the -devel-doc sub-package

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 10 2022 Orion Poplawski <orion@nwra.com> - 0.6.2-38
- Rebuild for glew 2.2

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.6.2-30
- Rebuilt for glew 2.1.0

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 0.6.2-24
- Rebuild for glew 2.0.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 0.6.2-22
- Rebuild for glew 1.13

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.6.2-20
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 Hans de Goede <hdegoede@redhat.com> - 0.6.2-18
- Enable building of the freeimage image-codec and make it the default, so
  that we get support for image formats other then just tga

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Nov 18 2013 Dave Airlie <airlied@redhat.com> - 0.6.2-16
- rebuilt for GLEW 1.10

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 13 2012 Adam Jackson <ajax@redhat.com> - 0.6.2-13
- Rebuild for glew 1.9.0

* Thu Jul 26 2012 Hans de Goede <hdegoede@redhat.com> - 0.6.2-12
- Rebuilt for new GLEW

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 0.6.2-10
- Rebuild against PCRE 8.30

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 ajax@redhat.com - 0.6.2-8
- Rebuild for new glew soname

* Sun Feb 13 2011 Hans de Goede <hdegoede@redhat.com> - 0.6.2-7
- Fix building with gcc-4.6

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 07 2011 Bruno Wolff III <bruno@wolff.to> - 0.6.2-5
- Rebuild against ogre that uses boost instead of poco.

* Tue Jan 04 2011 Bruno Wolff III <bruno@wolff.to> - 0.6.2-4
- Fix requires to be cegui06-devel rather than cegui-devel

* Mon Jan  3 2011 Hans de Goede <hdegoede@redhat.com> 0.6.2-3
- Update License tag to "MIT and LGPLv2+" and some files did not have
  their copyright header updated when upstream moved from LGPLv2+ to MIT.
  This is fixed in the 0.7.x (and later) versions of cegui.

* Tue Nov  9 2010 Hans de Goede <hdegoede@redhat.com> 0.6.2-2
- Switch to new upstream 0.6.2b tarbal (#650643)

* Sun Nov  7 2010 Hans de Goede <hdegoede@redhat.com> 0.6.2-1
- First release of CEGUI-0.6.2 as cegui06
