Name:           scratch
Version:        1.4.0.7
Release:        32%{?dist}
Summary:        Programming language learning environment for stories, games, music and art

License:        GPL-2.0-only AND GPL-3.0-only AND MIT AND CC-BY-SA-3.0
URL:            http://scratch.mit.edu
Source0:        http://download.scratch.mit.edu/%{name}-%{version}.src.tar.gz
# The following source file is not used in the build process, but together
# with Scratch.image and src/Scratch.changes comprises the preferred means
# of modification -- see the included README. This file is under the MIT
# and Apache 2.0 licenses.
Source1:        http://ftp.squeak.org/2.0/SqueakV2.sources.gz
Source2:        50-wedo.rules
Source3:		scratch.appdata.xml
Patch0:         scratch-1.4.0.7-use-fedora-squeak.patch
Patch1:         scratch-1.4.0.6-desktopfile-semicolon.patch

BuildArch:	noarch

BuildRequires: desktop-file-utils
BuildRequires: systemd

Requires:       scratch-image
Requires:       scratch-media, scratch-projects
Requires:       scratch-help, scratch-i18n


%description
Scratch is a programming language that makes it easy to create your own
interactive stories, animations, games, music, and art -- and share your
creations on the web.

As young people create and share Scratch projects, they learn important
mathematical and computational ideas, while also learning to think
creatively, reason systematically, and work collaboratively.

This package brings in all of the various subpackages which comprise the
full Scratch distribution.


%package image
Summary: The Scratch programming environment
License: GPL-2.0-only AND GPL-3.0-only AND MIT
Requires: squeak-vm >= 4.10.2.2593
BuildArch: noarch

%description image
Scratch is a programming language that makes it easy to create your own
interactive stories, animations, games, music, and art -- and share your
creations on the web.

This package contains the core Scratch programming environment.


%package help
Summary: Documentation for the Scratch programming language
License: CC-BY-SA-3.0
BuildArch: noarch

%description help
This package contains HTML and PDF documentation for scratch. The HTML
documentation is referenced in the Scratch menu, and the PDFs are linked
from that.


%package media
Summary: The standard distribution of sprites and media for Scratch
License: CC-BY-SA-3.0
BuildArch: noarch

%description media
This package contains the standard collection of images and sounds for the
Scratch programming language.


%package projects
Summary: The standard distribution of Scratch projects
License: CC-BY-SA-3.0
BuildArch: noarch

%description projects
This package contains the standard collection of sample projects for the
Scratch programming language.


%package i18n
Summary: Translations for the Scratch programming environment
License: GPL-2.0-only
BuildArch: noarch

%description i18n
This package contains international support for the Scratch programming
environment. If it is not installed, Scratch will only be available in
English


%prep
%setup -q -n %{name}-%{version}.src
%patch -P0 -p1
%patch -P1 -p1

# this project is under CC-BY-NC-2.5 that is not allowed in Fedora
rm "Projects/Sensors and Motors/WeDo 3 Castle.sb"

%build
# since the Squeak VM version 4.10.2.2593 and greater includes all the
# plugins previously included as part of Scratch, we don't need to build
# anything here.


%install
install -m 755 -d %{buildroot}%{_datadir}/%{name}
install -m 644 Scratch.image %{buildroot}%{_datadir}/%{name}/
install -m 644 Scratch.ini %{buildroot}%{_datadir}/%{name}/

install -m 755 -d %{buildroot}%{_datadir}/%{name}/Help/en/images
install -m 644 Help/en/*.pdf %{buildroot}%{_datadir}/%{name}/Help/en/
install -m 644 Help/en/*.html %{buildroot}%{_datadir}/%{name}/Help/en/
install -m 644 Help/en/*.gif %{buildroot}%{_datadir}/%{name}/Help/en/
install -m 644 Help/en/images/*.gif %{buildroot}%{_datadir}/%{name}/Help/en/images/

install -m 755 -d %{buildroot}%{_datadir}/%{name}/locale
install -m 644 locale/* %{buildroot}%{_datadir}/%{name}/locale/

cp -R Media  %{buildroot}%{_datadir}/%{name}/

install -m 755 -d %{buildroot}%{_datadir}/%{name}/Projects/Animation
install -m 644 Projects/Animation/*.sb %{buildroot}%{_datadir}/%{name}/Projects/Animation/
install -m 755 -d %{buildroot}%{_datadir}/%{name}/Projects/Games
install -m 644 Projects/Games/*.sb %{buildroot}%{_datadir}/%{name}/Projects/Games/
install -m 755 -d %{buildroot}%{_datadir}/%{name}/Projects/Greetings
install -m 644 Projects/Greetings/*.sb %{buildroot}%{_datadir}/%{name}/Projects/Greetings/
install -m 755 -d %{buildroot}%{_datadir}/%{name}/Projects/Interactive\ Art
install -m 644 Projects/Interactive\ Art/*.sb %{buildroot}%{_datadir}/%{name}/Projects/Interactive\ Art/
install -m 755 -d %{buildroot}%{_datadir}/%{name}/Projects/Music\ and\ Dance
install -m 644 Projects/Music\ and\ Dance/*.sb %{buildroot}%{_datadir}/%{name}/Projects/Music\ and\ Dance/
install -m 755 -d %{buildroot}%{_datadir}/%{name}/Projects/Names
install -m 644 Projects/Names/*.sb %{buildroot}%{_datadir}/%{name}/Projects/Names/
install -m 755 -d %{buildroot}%{_datadir}/%{name}/Projects/Sensors\ and\ Motors
install -m 644 Projects/Sensors\ and\ Motors/*.sb %{buildroot}%{_datadir}/%{name}/Projects/Sensors\ and\ Motors/
install -m 755 -d %{buildroot}%{_datadir}/%{name}/Projects/Simulations
install -m 644 Projects/Simulations/*.sb %{buildroot}%{_datadir}/%{name}/Projects/Simulations/
install -m 755 -d %{buildroot}%{_datadir}/%{name}/Projects/Speak\ Up
install -m 644 Projects/Speak\ Up/*.sb %{buildroot}%{_datadir}/%{name}/Projects/Speak\ Up/
install -m 755 -d %{buildroot}%{_datadir}/%{name}/Projects/Stories
install -m 644 Projects/Stories/*.sb %{buildroot}%{_datadir}/%{name}/Projects/Stories/

install -m 755 -d %{buildroot}%{_bindir}/
install -m 755 src/scratch %{buildroot}%{_bindir}/

install -m 755 -d %{buildroot}%{_mandir}/man1
install -m 644 src/man/scratch.1.gz %{buildroot}%{_mandir}/man1/

install -m 755 -d %{buildroot}%{_datadir}/applications
desktop-file-install --dir=%{buildroot}%{_datadir}/applications src/%{name}.desktop

install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
install -m 644 src/icons/48x48/scratch.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
install -m 644 src/icons/128x128/scratch.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/
install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/48x48/mimetypes
install -m 644 src/icons/48x48/gnome-mime-application-x-scratch-project.png %{buildroot}%{_datadir}/icons/hicolor/48x48/mimetypes/
install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/128x128/mimetypes
install -m 644 src/icons/128x128/gnome-mime-application-x-scratch-project.png %{buildroot}%{_datadir}/icons/hicolor/128x128/mimetypes/

install -m 755 -d %{buildroot}%{_datadir}/mime/packages
install -m 644 src/%{name}.xml %{buildroot}%{_datadir}/mime/packages/

install -m 755 -d %{buildroot}%{_udevrulesdir}
install -m 644 %{SOURCE2} %{buildroot}%{_udevrulesdir}/

mkdir -p %{buildroot}%{_datadir}/appdata
cp -a %{SOURCE3} %{buildroot}%{_datadir}/appdata/

%files
%license LICENSE gpl-2.0.txt TRADEMARK_POLICY
%doc KNOWN-BUGS ACKNOWLEDGEMENTS NOTICE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*.1*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/hicolor/48x48/apps/*
%{_datadir}/icons/hicolor/48x48/mimetypes/*
%{_datadir}/icons/hicolor/128x128/apps/*
%{_datadir}/icons/hicolor/128x128/mimetypes/*
%{_udevrulesdir}/50-wedo.rules
%{_datadir}/appdata/%{name}.appdata.xml

%files image
%license LICENSE gpl-2.0.txt
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/Scratch.image
%{_datadir}/%{name}/Scratch.ini

%files help
%license LICENSE
%dir %{_datadir}/%{name}/Help
%{_datadir}/%{name}/Help/*

%files media
%license LICENSE
%dir %{_datadir}/%{name}/Media
%{_datadir}/%{name}/Media/*

%files projects
%license LICENSE
%dir %{_datadir}/%{name}/Projects
%{_datadir}/%{name}/Projects/*

%files i18n
%license LICENSE gpl-2.0.txt
%{_datadir}/%{name}/locale


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0.7-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0.7-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4.0.7-30
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0.7-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0.7-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0.7-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0.7-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0.7-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0.7-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4.0.7-15
- Remove obsolete scriptlets

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 20 2017 msuchy@redhat.com - 1.4.0.7-13
- build require systemd to recognize udev macro

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 09 2016 msuchy@redhat.com - 1.4.0.7-11
- 1161108 - add appdata file
- 1173319 - add udev rule for Lego WeDo

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 1.4.0.7-8
- add mime scriptlets, fix icon scriptlets

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Nov 24 2012 Matthew Miller <mattdm[@]mattdm.org> - 1.4.0.7-5
- delete SQ_DIR code from scratch launch script -- not needed since
  we're using distro-provided packages and we know where our own stuff
  lives.

* Wed Nov  7 2012 Matthew Miller <mattdm[@]mattdm.org> - 1.4.0.7-4
- new squeak-vm now includes the plugins needed here (including the
  Scratch plugin), so we don't need to build them here.
- update startup script to not refer to plugins from this package 
- move xshm change to single fedora squeak patch, for simplicity
- move startup script and icons to main package
- remove pulseaudio hack since that should now just work

* Fri Sep 28 2012 Matthew Miller <mattdm[@]mattdm.org> - 1.4.0.7-3
- xshm extension has been reported to cause problems with newer squeak,
  and definitely breaks remote use. Does not appear to give a noticeable
  performance benefit, so let's not use it.


* Fri Sep 28 2012 Matthew Miller <mattdm[@]mattdm.org> - 1.4.0.7-2
- add source file and license info for squeak vm
- use buildroot macro consistently
- add rpm scripts for icon cache refresh
- install desktop file properly

* Fri Sep 14 2012 Matthew Miller <mattdm[@]mattdm.org> - 1.4.0.7-1
- update to 1.4.0.7, which removes the mp3 issue thanks to upstream

* Mon Sep 10 2012 Matthew Miller <mattdm[@]mattdm.org> - 1.4.0.6-15
- work around possible missing pulse plugin for squeak

* Mon Sep 10 2012 Matthew Miller <mattdm[@]mattdm.org> - 1.4.0.6-14
- right name for the camera plugin

* Mon Sep 10 2012 Matthew Miller <mattdm[@]mattdm.org> - 1.4.0.6-13
- license files for all!
- proper license for different subpackages

* Mon Sep 10 2012 Matthew Miller <mattdm[@]mattdm.org> - 1.4.0.6-12
- whoops forgot to require the camera plugin

* Mon Sep 10 2012 Matthew Miller <mattdm[@]mattdm.org> - 1.4.0.6-11
- use santized source file (no included pre-built binaries)

* Mon Sep 10 2012 Matthew Miller <mattdm[@]mattdm.org> - 1.4.0.6-10
- fix whine about invalid desktop file due to missing ;
- de-dot the summaries

* Mon Sep 10 2012 Matthew Miller <mattdm[@]mattdm.org> - 1.4.0.6-9
- missing defattr -- whoops
- put docs in both image and main wrapper package

* Mon Sep 10 2012 Matthew Miller <mattdm[@]mattdm.org> - 1.4.0.6-8
- delete mp3s since they won't work without support
- remove binary plugins in prep stage
- move more things to noarch subpackages -- now only plugins and
  main "wrapper" package are arch-specific

* Mon Sep 10 2012 Matthew Miller <mattdm[@]mattdm.org> - 1.4.0.6-7
- split plugins into subpackages
- split help and media into subpackages

* Mon Sep 10 2012 Matthew Miller <mattdm[@]mattdm.org> - 1.4.0.6-5
- remove MIDI plugin, which is part of the main squeak vm package
- remove MP3 plugin, which is a) a binary in the source distribution,
  b) missing source, and c) not allowed in Fedora

* Mon Sep 10 2012 Matthew Miller <mattdm[@]mattdm.org> - 1.4.0.6-4
- update layout to deal with arch issues
- set cflags; get proper debuginfo packages

* Fri Sep  7 2012 Matthew Miller <mattdm[@]mattdm.org> - 1.4.0.6-1
- update to gplv2 version
- tweak source filename and build dir to match upstream
- update patch to point to system squeak vm

* Mon Jan 17 2011 W. Michael Petullo <mike[@]flyn.org> - 1.4.0.1-1
- Initial package
