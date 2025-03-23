# norootforbuild

Name:		screengrab
Version:	1.2.1
Release:	8%{?dist}
License:	GPLv2
URL:		https://github.com/DOOMer/screengrab
Source0:	https://github.com/DOOMer/screengrab/archive/1.2.1.tar.gz/#/%{name}-%{version}.tar.gz
Patch0:		%{name}-%{version}.patch
Summary:	Screen grabber
BuildRequires:	cmake, pkgconfig(QtGui), libqxt-devel, desktop-file-utils

%description
This is a crossplatform application designed to quickly get screenshots ScreenGrab created using the Qt Framework.
Main features:
* Get desktop screenshots
* Get active window screenshots
* Get secreenshots of desktop selection area
* Copy screenshot to clipboard
* Saving your image files in formats PNG or JPEG or BMP
* Ability to set delay in getting screenshots (from 1 to 90 seconds)
* Hiding the main window (with recovery) ScreenGrab at the time of the screenshot
* Ability to minimize application to system tray, and control via context menu
* Getting screenshots using global shortcuts
* Auto-save screenshot when received
* Ability to insert the current date and time in filename and save

%prep
%setup -q
%patch 0 -p0
# be assured
%{__rm} -rf src/3rdparty

%build
mkdir build
pushd build
%cmake -DCMAKE_BUILD_TYPE=release -DSG_USE_SYSTEM_QXT=ON -DBUILD_SHARED_LIBS:BOOL=OFF ..
make %{?_smp_mflags}
popd

%install
pushd build
make DESTDIR=%{buildroot} install
popd
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%find_lang %{name} --with-qt --without-mo
# hack
rm -rf %{buildroot}/%{_datadir}/doc/

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
BugReportURL: https://github.com/DOOMer/screengrab/issues/57
SentUpstream: 2014-09-18
-->
<application>
  <id type="desktop">screengrab.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Capture screenshots</summary>
  <description>
    <p>
      Screengrab is a utility to take screenshots of your desktop.
      With Screengrab you can take a shot of your whole desktop, a specific window,
      or you can select the area you want to capture by dragging a rectangle with the mouse.
      Additionally it features the ability to copy the screenshot to the clipboard,
      set a delay before the screenshot is taken and save with filenames
      containing the current date and time.
    </p>
  </description>
  <url type="homepage">http://screengrab.doomer.org/</url>
  <screenshots>
    <screenshot type="default">http://i.imgur.com/VfdeqYo.png</screenshot>
  </screenshots>
</application>
EOF

%ldconfig_scriptlets

%files -f %{name}.lang
%license docs/LICENSE.txt
%doc README.md docs/ChangeLog.txt
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%dir %{_datadir}/%{name}/

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 28 2016 TI_Eugene <ti.eugene@gmail.com> 1.2.1-1
- Version bump
- Changed source URL
- Clean up docs

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.2-3
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.2-2
- Add an AppData file for the software center

* Mon Jan 19 2015 TI_Eugene <ti.eugene@gmail.com> 1.2-1
- Version bump

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 16 2013 TI_Eugene <ti.eugene@gmail.com> 1.0-1
- Version bump
- %%find_lang added

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.96-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 16 2013 TI_Eugene <ti.eugene@gmail.com> 0.9.96-3
- User CXXFLAGS patch improved

* Fri Mar 08 2013 TI_Eugene <ti.eugene@gmail.com> 0.9.96-2
- src/3rdparty removed (built-in qxt)

* Fri Mar 08 2013 TI_Eugene <ti.eugene@gmail.com> 0.9.96-1
- next version - 0.9.96
- spec fix: License set to GPLv2
- spec fix: Group tag removed
- spec fix: %%description copy/pasted from project home webpage
- spec fix: %%install - 'rm buildroot' removed; 'rm' changed to %%{__rm}

* Thu Mar 07 2013 TI_Eugene <ti.eugene@gmail.com> 0.9.1-3
- spec fix: License tag changed to GPL+LGPL+BSD
- spec fix: cmake call changed to %%cmake macro with BUILD_SHARED_LIBS=OFF
- spec fix: Source0 tag changed to URL
- spec fix: previous changelog record expanded

* Thu Mar 07 2013 TI_Eugene <ti.eugene@gmail.com> 0.9.1-2
- spec fix: gcc-c++ removed from BuildRequires
- spec fix: description wraped
- spec fix: %%clean section removed
- spec fix: %%defattr removed
- spec fix: desktop-file-validate added
- spec fix: Vendor tag removed
- spec fix: changelog cutted up to starting in Fedora
- spec fix: Source tag changed to non-URL with comments
- spec fix: License set to GPLv2

* Thu Mar 07 2013 TI_Eugene <ti.eugene@gmail.com> 0.9.1-1
- initial packaging for Fedora
