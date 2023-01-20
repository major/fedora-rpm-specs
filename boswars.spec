Name:           boswars
Version:        2.7
Release:        29.svn160110%{?dist}
Summary:        Bos Wars is a futuristic real-time strategy game
License:        GPLv2
URL:            http://www.boswars.org/
Source0:        ftp://ftp.nluug.nl/pub/os/Linux/distr/debian/pool/main/b/boswars/boswars_2.7+svn160110.orig.tar.xz
Source1:        %{name}.desktop
Source2:        %{name}-48.png
Source3:        %{name}-128.png
Source4:        %{name}.appdata.xml
Source5:        %{name}.6
Patch0:         boswars-2.4.1-SConstruct.patch
# incomplete patch to port boswars to the system guichan-0.6 instead of
# using the included guichan-0.4. Incomplete, NOT finished and NOT working!
#Patch1:         boswars-2.4.1-guichan26.patch
# Incomplete Lua 5.2 patch, this fixes the C-code but not the actual lua scripts
#Patch2:         boswars-2.6.1-lua-5.2.patch
# Use compat-lua51 for now
Patch3:         boswars-2.7-compat-lua-5.1.patch
Patch4:         boswars-2.7-sconstruct-py3.patch
BuildRequires:  gcc gcc-c++
BuildRequires:  libtheora-devel libvorbis-devel SDL-devel libGL-devel
BuildRequires:  compat-tolua++-devel libpng-devel python3-scons
BuildRequires:  libappstream-glib desktop-file-utils
Requires:       hicolor-icon-theme

%description
Bos Wars is a futuristic real-time strategy game. It is possible to play
against human opponents over LAN, internet, or against the computer.
Bos Wars aims to create a completly original and fun open source RTS game.


%prep
%autosetup -p1 -n %{name}
iconv -f ISO-8859-1 -t UTF8 doc/guichan-copyright.txt > guichan-copyright.txt
find campaigns engine maps -type f -executable -exec chmod -x {} ';'
# we want to use the system version of these
rm engine/tolua/*.h engine/tolua/tolua_*.cpp


%build
scons-3 %{?_smp_mflags} opengl=1 CC="gcc $RPM_OPT_FLAGS" CXX="g++ $RPM_OPT_FLAGS" LIBPATH=%{_libdir}


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/languages
install -m 755 build/boswars-release $RPM_BUILD_ROOT%{_bindir}/%{name}
install -p -m 644 languages/*.po languages/*.pot \
  $RPM_BUILD_ROOT%{_datadir}/%{name}/languages
cp -a campaigns graphics intro maps scripts sounds units patches \
  $RPM_BUILD_ROOT%{_datadir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -p -m 644 %{SOURCE3} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6
install -p -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_mandir}/man6


%files
%doc README.txt CHANGELOG doc/*.html
%license COPYRIGHT.txt LICENSE.txt guichan-copyright.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man6/%{name}.6*


%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-29.svn160110
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-28.svn160110
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-27.svn160110
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-26.svn160110
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-25.svn160110
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Adam Jackson <ajax@redhat.com> - 2.7-24.svn160110
- Drop long-unnecessary Requires: xorg-x11-utils

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-23.svn160110
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar  4 2020 Hans de Goede <hdegoede@redhat.com> - 2.7-22.svn160110
- Replace 128x128 icon with a better version
- Restore original 48x48 icon for cases where we need a lower res icon

* Sun Feb 16 2020 Hans de Goede <hdegoede@redhat.com> - 2.7-21.svn160110
- Fix FTBFS with scons-3.0.4 (rhbz#1799199)
- Replace icon with 128x128 icon

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-20.svn160110
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-19.svn160110
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 18 2019 Hans de Goede <hdegoede@redhat.com> - 2.7-18.svn160110
- Fix FTBFS with scons-3.0.4 (rhbz#1674710)
- Switch to python3-scons

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-17.svn160110
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-16.svn160110
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-15.svn160110
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.7-14.svn160110
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-13.svn160110
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-12.svn160110
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-11.svn160110
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Hans de Goede <hdegoede@redhat.com> - 2.7-10.svn160110
- Update to upstream svn snapshot to bring in some bugfixes + extra maps
- Fix some stray executable permissions (rpmlint)
- Add higher res icon
- Add appdata
- Add manpage

* Mon Feb 01 2016 Tim Niemueller <tim@niemueller.de> - 2.7-9
- rebuild for updated tolua++

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.7-7
- Rebuilt for GCC 5 C++11 ABI change

* Mon Feb 23 2015 Hans de Goede <hdegoede@redhat.com> - 2.7-6
- Build against compat-tolua++-5.1 as boswars is not compatible with lua 5.2

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 13 2013 Hans de Goede <hdegoede@redhat.com> - 2.7-3
- Replace a number of broken png images (rhbz#995862)

* Sat Aug  3 2013 Hans de Goede <hdegoede@redhat.com> - 2.7-2
- Build with compat-lua-devel on f20+

* Fri Aug  2 2013 Hans de Goede <hdegoede@redhat.com> - 2.7-1
- New upstream release 2.7 (rhbz#970057)

* Mon May 13 2013 Tom Callaway <spot@fedoraproject.org> - 2.6.1-9
- lua 5.2

* Thu Feb 14 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 2.6.1-8
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-5
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 06 2011 Bruno Wolff III <bruno@wolff.to> - 2.6.1-3
- Rebuild for libpng 1.5

* Wed Apr 27 2011 Hans de Goede <hdegoede@redhat.com> - 2.6.1-2
- Fix missing patches / textures (#691251)

* Sun Mar 13 2011 Hans de Goede <hdegoede@redhat.com> - 2.6.1-1
- New upstream release 2.6.1

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Apr 16 2010 Hans de Goede <hdegoede@redhat.com> 2.6-1
- New upstream release 2.6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 21 2009 Hans de Goede <hdegoede@redhat.com> 2.5-2
- Fix build with gcc 4.4

* Sun Mar  2 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 2.5-1
- New upstream release 2.5

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.4.1-5
- Autorebuild for GCC 4.3

* Sat Jan 12 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 2.4.1-4
- Fix compilation with gcc 4.3
- Drop workaround for intel graphics crash, this is "fixed" in SDL now

* Tue Oct 30 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.4.1-3
- Add workaround for boswars crashing on intel integrated video (bz 310841)

* Mon Sep 10 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.4.1-2
- Add missing BuildRequires libpng-devel

* Sun Sep  9 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.4.1-1
- Initial Fedora package
