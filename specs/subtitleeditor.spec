%global commit 75fa38b2f20a3ec9ff6c5458a7754bcef693a584
%global date 20220919
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           subtitleeditor
Version:        0.54.0
Release:        23.%{date}git%{shortcommit}%{?dist}
Summary:        GTK+3 tool to edit subtitles for GNU/Linux/*BSD

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://kitone.github.io/subtitleeditor/
Source0:        https://github.com/kitone/subtitleeditor/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  gettext-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-good
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  gtkmm30-devel
BuildRequires:  glibmm24-devel >= 2.16.3
BuildRequires:  libappstream-glib
BuildRequires:  libxml++-devel >= 2.20
BuildRequires:  libtool
BuildRequires:  intltool
BuildRequires:  ccache
BuildRequires:  gstreamermm-devel

# For spell checking (Optional)
BuildRequires:  enchant2-devel >= 2.2.0
# ISO-CODES 639 + 3166 (Optional)
BuildRequires:  iso-codes-devel

%global __provides_exclude_from ^%{_libdir}/%{name}/plugins/.*/lib.*\\.so$

%description
Subtitle Editor is a GTK+3 tool to edit subtitles for GNU/Linux/*BSD. It can be
used for new subtitles or as a tool to transform, edit, correct and refine
existing subtitle. This program also shows sound waves, which makes it easier
to synchronize subtitles to voices.

%prep
%setup -q -n %{name}-%{commit}

%build
autoreconf -fiv
%configure \
       --disable-debug \
       --disable-static \
       --disable-gl \
       --enable-ccache

%make_build

%install
%make_install

#remove .la's
find %{buildroot} -name "*.la" -exec %{__rm} -f '{}' \;

#remove useless development files
%{__rm} -f %{buildroot}%{_libdir}/lib%{name}.so

%find_lang %{name}

desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications             \
  --mode 0644                                            \
  %{buildroot}%{_datadir}/applications/org.kitone.%{name}.desktop

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.kitone.%{name}.appdata.xml

%ldconfig_scriptlets

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README TODO
%license COPYING
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/pixmaps/%{name}.svg
%{_datadir}/%{name}/
%{_datadir}/metainfo/org.kitone.%{name}.appdata.xml
%{_datadir}/applications/org.kitone.%{name}.desktop
%{_mandir}/man1/%{name}.1.*
%{_libdir}/lib%{name}.so.*
%{_libdir}/%{name}/

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.0-23.20220919git75fa38b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.54.0-22.20220919git75fa38b
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.0-21.20220919git75fa38b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.0-20.20220919git75fa38b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.0-19.20220919git75fa38b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.0-18.20220919git75fa38b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 13 2023 Dominik 'Rathann' Mierzejewski <dominik@greysector.net> - 0.54.0-17.20220919git75fa38b
- update to current git HEAD
- switch to enchant2 (enchant is EOL, last release in 2010)
- filter auto-generated Provides: for plugins

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 17 2022 Kevin Fenzi <kevin@scrye.com> - 0.54.0-14
- Rebuild for hiredis 1.0.2

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.0-11
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 06 2020 Leigh Scott <leigh123linux@gmail.com> - 0.54.0-9
- Switch BuildRequires to gstreamer1
- Validate appdata
- Clean up spec file and drop dead patches

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.54.0-5
- Fix build
- Remove unneeded macros

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.54.0-3
- Add gcc to BR
- Use license macro
- Use buildroot macro instead of RPM_BUILD_ROOT

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.54.0-2
- Escape macros in %%changelog

* Wed Feb  7 2018 Haïkel Guémar <hguemar@fedoraproject.org> - 0.%{minor}.%{maintenance}-1
- Upstream 0.54.0
- Fix URL

* Wed Feb  7 2018 Haïkel Guémar <hguemar@fedoraproject.org> - 0.%{minor}.%{maintenance}-6
- Rebuild against newer gstreammermm

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.53.0-5
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.53.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.53.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.53.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jul 30 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.53.0-1
- Update to 0.53.0

* Thu Jul 28 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.52.1-1
- Update to latest upstream release

* Fri Jun 10 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> - .41.0-11
- Rebuild spec bump

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.41.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 10 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.41.0-9
- define -> global

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.41.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.41.0-7
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.41.0-6
- Add an AppData file for the software center

* Thu Jan 29 2015 Artur Szymczak <artur.szymczak@nadzieja.pl> - 0.41.0-5
- Added patches for rhbz #1187152 (upstream #22857 and #23018)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.41.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.41.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Jan 19 2014 Martin Sourada <mso@fedoraproject.org> - 0.41.0-2
- Added patch for rhbz #1017469 (upstream #21501 and #20653)

* Thu Jan 16 2014 Artur Szymczak <artur.szymczak@nadzieja.pl> - 0.41.0-1
- Updated to latest release.
- Dropping the temporary patch (%%{name}-0.40.0-glib.patch) - Fixed upstream.
- Added patch for rhbz #906226 (upstream #20793)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 24 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.40.0-4
- Remove --vendor from desktop-file-install for F19+. https://fedorahosted.org/fesco/ticket/1077

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 14 2012 Martin Sourada <mso@fedoraproject.org> - 0.40.0-1
- Update to latest release.
  * Lots of bugfixes.
  * Adds ability to seek by frames.
  * Adds default ASS/SSA style in config file.
  * Adds support for DLP Cinema Subtitle format.
  * Adds 'recent files' for Video and Wave Frame.

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.39.0-4
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.39.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.39.0-2
- Rebuild for new libpng

* Mon Jul 18 2011 Martin Sourada <mso@fedoraproject.org> - 0.39.0-1
- New upstream release 0.39.0
- adds support for SAMI subtitle format
- detects movie fps
- various fixes and improvements

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 14 2010 Martin Sourada <mso@fedoraproject.org> - 0.37.1-1
- rhbz #583343 (upstream #16016) fixed upstream, dropping the temporary patch
- displays saving dialog after generating waveforms or keyframes
- adds support for .stl subtitle format (Spruce STL)
- adds an option to scall all subtitles
- fixes a crash at "find and replace" with regexp (upstream #16058)

* Mon Jun 21 2010 Martin Sourada <mso@fedoraproject.org> - 0.36.2-2
- Updated patch for rhbz #583343 (upstream #16016)

* Sun Jun 06 2010 Martin Sourada <mso@fedoraproject.org> - 0.36.2-1
- New subtitle format SBV
- Build with gl waveform renderer now works, we'll keep Cairo based one though
- Fixes non-working video playback (upstream #15525)
- Fixes some segfaults on waveform generation (upstream #15464)
- Add temporary patch for rhbz #583343 (upstream #16016)

* Sun Feb 14 2010 Martin Sourada <mso@fedoraproject.org> - 0.36.0-1
- disable gl waveform renderer (fails to build, cairo based is good enough)
- two new plugins : sortsubtitles, typewriter
- various fixes
- fixes rhbz#564215 and its duplicates

* Sun Jan 10 2010 Martin Sourada <mso@fedoraproject.org> - 0.35.1-2
- Fix source URL

* Thu Dec 31 2009 Martin Sourada <mso@fedoraproject.org> - 0.35.1-1
- New release
- improvements to waveform editor
- video player rewritten, should fix rhbz#538382
- various bug fixes

* Sun Oct 25 2009 Martin Sourada <mso@fedoraproject.org> - 0.34.0-1
- New release
- supports pulsesink now
- new plugin 'textcorrection'
- new plugin 'keyframesmanagement'
- spell checking plugin completely rewrite
- find and replace plugin completely rewrite
- libglademm -> Gtk::Builder
- new translations
- various bug fixes
- fix for upstream bug #12649 has been included in tarbal

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Martin Sourada <mso@fedoraproject.org> - 0.30.0-4
- Fix build on rawhide

* Thu Dec 11 2008 Martin Sourada <mso@fedoraproject.org> - 0.30.0-3
- Apply patch to upstream bug 12649 (lubek)
- Various changes to spec file (lubek)

* Sat Dec 06 2008 Martin Sourada <mso@fedoraproject.org> - 0.30.0-2
- Add intltool to BuildRequires

* Sat Dec 06 2008 Martin Sourada <mso@fedoraproject.org> - 0.30.0-1
- Drop rhbz #459792 workaround
- New upstream release
 - Each function work around extension system (enable/disable/configure)
 - Add 'Generate Wavefrom From Video'
 - Add line break policy option: soft, hard, intelligent (ASS/SSA)
 - Add 'Wavefrom & Media' filter in the wavefrom dialog
 - The subtitle format system was completely rewritten
 - Update the UI when files are open.
 - Add option --enable-profiling
 - New Error Checking tool.
 - New options to set default document values.
 - Add "Edit Cell" and "Edit Next Cell".
 - Another characters coding can be selected if it fails.
 - Waveform Renderer use now Pango to draw subtitle text.

* Mon Aug 25 2008 Martin Sourada <martin.sourada@gmail.com> - 0.22.3-1
- New upstream release
- Don't build with cppunit testing (rhbz #458607)
- Workaround rhbz #459792

* Thu Jul 03 2008 Martin Sourada <martin.sourada@gmail.com> - 0.21.3-1
- New upstream release
 - Add option -f --file for open a file
 - Add MimeType in desktop file.
 - Update Czech translation
 - Fix: Play/Pause button
 - Fix: #10494 (upstream)

* Thu Jun 19 2008 Martin Sourada <martin.sourada@gmail.com> - 0.21.2-1
- New upstream release

* Wed May 28 2008 Martin Sourada <martin.sourada@gmail.com> - 0.21.1-3
- Enable unit testing

* Tue May 27 2008 Martin Sourada <martin.sourada@gmail.com> - 0.21.1-2
- Update the icon cache update scriplet to follow the packaging guidelines
- Add BR: gstreamer-plugins-good

* Tue May 27 2008 Martin Sourada <martin.sourada@gmail.com> - 0.21.1-1
- Initial Fedora RPM package

