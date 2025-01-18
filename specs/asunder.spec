Name:		asunder
Summary:	A graphical Audio CD ripper and encoder
Version:	3.0.1
Release:	6%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
URL:		http://littlesvr.ca/asunder
Source0:	http://littlesvr.ca/asunder/releases/asunder-%{version}.tar.bz2
Requires:	cdparanoia
# Supported audio encoders
Requires:	vorbis-tools
Recommends:	lame
Recommends:	flac
Recommends:	opus-tools
# Additional supported audio encoders
Suggests:	wavpack
Suggests:	mppenc
# FDK-AAC encoder is available only in RPM Fusion
#Suggests:	fdkaac
# Monkey’s Audio lossless encoder - available only in RPM Fusion
# (anyway seems to be broken as of Asunder 2.9.2)
#Suggests:	mac

# Versions were taken from the program's website
BuildRequires:	gcc
BuildRequires:	libcddb-devel >= 0.9.5
BuildRequires:	gtk2-devel >= 2.4
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	intltool >= 0.34.90
BuildRequires:	make

%description
It allows to save tracks from an Audio CD as WAV, OGG, MP3, OPUS, FLAC,
Wavpack, Musepack and/or Monkey's Audio, AAC (using third-party software).

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%find_lang %{name}

desktop-file-install --dir %{buildroot}%{_datadir}/applications \
	%if (0%{?fedora} && 0%{?fedora} < 19) || (0%{?rhel} && 0%{?rhel} < 7)
	--vendor fedora \
	%endif
	--add-category X-AudioVideoImport \
	%{buildroot}%{_datadir}/applications/asunder.desktop

%files -f %{name}.lang
%{_bindir}/asunder
%doc AUTHORS ChangeLog README TODO NEWS
%license COPYING
%{_datadir}/applications/*asunder.desktop
%{_datadir}/pixmaps/asunder.png
%{_datadir}/pixmaps/asunder.svg

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 3.0.1-5
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 03 2023 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 3.0.1-1
- Update to 3.0.1 (#2224687)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 30 2021 Marcin Zajaczkowski <szpak ATT wp DOTT pl> - 2.9.7-1
- Update to 2.9.7 (#1906427)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 08 2020 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 2.9.6-1
- Update to 2.9.6 (#1763713)
- Drop patch for aarch64 - supported upstream

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 2.9.5-1
- Update to 2.9.5 (#1763713)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 29 2019 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2.9.4-1
- Update to 2.9.4 (#1747108)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 15 2018 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 2.9.3-4
- Add Opus to package description

* Thu Nov 15 2018 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 2.9.3-3
- Make Opus encoder recommended - Opus has wider usage spectrum over Vorbis

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Apr 14 2018 Filipe Rosset <rosset.filipe@gmail.com> - 2.9.3-1
- update to latest upstream version 2.9.3
- spec cleanup

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 20 2017 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 2.9.2-2
- Modernize encoder dependencies with Recommends/Suggests - more details https://fedoraproject.org/wiki/Packaging:WeakDependencies

* Mon Nov 20 2017 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 2.9.2-1
- Update to 2.9.2 (#1449209)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 12 2017 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 2.8.1-1
- Update to 2.8.1 (#1419920)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Oct 18 2015 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 2.8-1
- Update to 2.8 (#1167637)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 2.5-4
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 16 2014 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 2.5-1
- Update to 2.5

* Sat Mar 01 2014 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 2.4-1
- Update to 2.4
- Fix bogus date in changelog

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 30 2013 Christoph Wickert <cwickert@fedoraproject.org> - 2.3-2
- Fix desktop vendor conditional
- Enable aarch64 support (#925039)

* Thu May 30 2013 Christoph Wickert <cwickert@fedoraproject.org> - 2.3-1
- Update to 2.3 (#964272)
- Make desktop vendor conditional
- Add MimeType scriptlets

* Sun Feb 10 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 2.2-3
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Feb 26 2012 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 2.2-1
- updated to 2.2
- add BuildRequires for intltool to fix a build problem in Koji

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.1-2
- Rebuild for new libpng

* Fri Jun 24 2011 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 2.1-1
- updated to 2.1

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Aug 07 2010 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 2.0-1
- updated to 2.0

* Thu Apr 22 2010 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.9.3-1
- updated to 1.9.3

* Thu Dec 10 2009 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.9.1-1
- updated to 1.9.1

* Wed Sep 23 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.9-2
- Update desktop file according to F-12 FedoraStudio feature

* Fri Sep 18 2009 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.9-1
- updated to 1.9
- added new additional runtime dependencies (Monkey's Audio)
- precised a description (bug 478352 - thanks to Horst H. von Brand)
- removed not needed anymore patch fixing sv locales in .desktop file 

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec 27 2008 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.6.2-1
- updated to 1.6.2

* Tue Sep 16 2008 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.6.1-1
- updated to 1.6.1

* Tue Jul 1 2008 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.6-1
- updated to 1.6
- removed explicit libcddb dependency
- broken too long desciption line

* Sun May 4 2008 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.5-1
- updated to 1.5
- added (commented for now) wavpack dependency

* Mon Feb 4 2008 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.0.2-1
- updated to 1.0.2

* Tue Dec 18 2007 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.0-1
- updated to 1.0

* Fri Nov 09 2007 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.9-2
- applied Michael Schwendt suggestions (all below)
- removed redundant --prefix argument
- used --delete-original to delete .desktop file
- removed minimal required version of libcddb from Requires

* Sat Oct 06 2007 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.9-1
- updated to 0.9

* Mon Sep 03 2007 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.8.1-2
- added libcddv-devel to BuildRequires section
- removed unused patch

* Sat Sep 01 2007 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.8.1-1
- initial release
