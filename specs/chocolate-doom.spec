Name:		chocolate-doom
Summary:	Historically compatible Doom engine
License:	GPL-2.0-or-later

%global rtld org.chocolate_doom
URL:		http://chocolate-doom.org/

Version:	3.1.0
Release:	5%{?dist}

%global git_tag %{name}-%{version}
Source0:	https://github.com/chocolate-doom/chocolate-doom/archive/%{git_tag}/%{git_tag}.tar.gz

# Always use the system python3 instead of asking /usr/bin/env first.
Patch1:		0001-use-python3.patch

# Historically, chocolate-doom's build scripts did not explicitly set the -std= option.
# When GCC15 came along and made C23 the default, the program failed to build because
# it declares its custom "bool" type. After some debate, upstream decided that rather
# than try to make the project compatible with different standards, they will use C99.
#
# Backport from upstream:
# https://github.com/chocolate-doom/chocolate-doom/pull/1723
Patch2:		0002-use-c99.patch

# Fix missing includes.
# Submitted upstream: https://github.com/chocolate-doom/chocolate-doom/pull/1725
Patch3:		0003-missing-includes.patch

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc
BuildRequires:	fluidsynth-devel
BuildRequires:	libpng-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	make
BuildRequires:	SDL2-devel
BuildRequires:	SDL2_mixer-devel
BuildRequires:	SDL2_net-devel

BuildRequires:	python3
BuildRequires:	python3dist(pillow)

BuildRequires:	desktop-file-utils
BuildRequires:	libappstream-glib

#Provides:	bundled(md5-plumb)
Provides:	bundled(sha1-gnupg)

%description
Chocolate Doom is a game engine that aims to accurately reproduce the experience 
of playing vanilla Doom. It is a conservative, historically accurate Doom source 
port, which is compatible with the thousands of mods and levels that were made 
before the Doom source code was released. Rather than flashy new graphics, 
Chocolate Doom's main features are its accurate reproduction of the game as it
was played in the 1990s. 


%prep
%autosetup -p1 -n %{name}-%{git_tag}
autoreconf -vif


%build
export PYTHON=%{_bindir}/python3

# Despite AC_PROC_CC_C99 inside configure.ac,
# -std= does not seem to be set when building
export CFLAGS="${CFLAGS} -std=gnu99"

%configure
%make_build


%install
export PYTHON=%{_bindir}/python3
%make_install DESTDIR=%{buildroot} \
     iconsdir="%{_datadir}/icons/hicolor/64x64/apps" \
     docdir="%{_pkgdocdir}"

# The program installs a .desktop file for a generic "chocolate-setup"
# executable, even though each game ships with its own setup executable.
# Create separate desktop files for each of those.
for GAME in Doom Heretic Hexen Strife; do
	EXEC="chocolate-$(echo "${GAME}" | tr '[A-Z]' '[a-z]')-setup"
	FILE="%{buildroot}%{_datadir}/applications/%{rtld}.${GAME}-Setup.desktop"

	cp -p %{buildroot}%{_datadir}/applications/%{rtld}.Setup.desktop "${FILE}"
	desktop-file-edit \
		--set-key=Exec --set-value="${EXEC}" \
		--set-name="Chocolate ${GAME} setup" \
		--set-comment="Setup tool for Chocolate ${GAME}" \
		"${FILE}"
done
rm %{buildroot}%{_datadir}/applications/%{rtld}.Setup.desktop


%check
for GAME in Doom Heretic Hexen Strife; do
	desktop-file-validate %{buildroot}/%{_datadir}/applications/%{rtld}.${GAME}.desktop
	desktop-file-validate %{buildroot}/%{_datadir}/applications/%{rtld}.${GAME}-Setup.desktop
	appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{rtld}.${GAME}.metainfo.xml
done
desktop-file-validate %{buildroot}/%{_datadir}/applications/screensavers/%{rtld}.Doom_Screensaver.desktop


%files
%doc %{_docdir}/chocolate*
%{_datadir}/bash-completion
%{_bindir}/chocolate-doom
%{_bindir}/chocolate-doom-setup
%{_bindir}/chocolate-heretic
%{_bindir}/chocolate-heretic-setup
%{_bindir}/chocolate-hexen
%{_bindir}/chocolate-hexen-setup
%{_bindir}/chocolate-server
%{_bindir}/chocolate-strife
%{_bindir}/chocolate-strife-setup
%{_datadir}/applications/%{rtld}.Doom.desktop
%{_datadir}/applications/%{rtld}.Doom-Setup.desktop
%{_datadir}/applications/%{rtld}.Heretic.desktop
%{_datadir}/applications/%{rtld}.Heretic-Setup.desktop
%{_datadir}/applications/%{rtld}.Hexen.desktop
%{_datadir}/applications/%{rtld}.Hexen-Setup.desktop
%{_datadir}/applications/%{rtld}.Strife.desktop
%{_datadir}/applications/%{rtld}.Strife-Setup.desktop
%{_datadir}/applications/screensavers/%{rtld}.Doom_Screensaver.desktop
%{_datadir}/icons/hicolor/64x64/apps/chocolate-doom.png
%{_datadir}/icons/hicolor/64x64/apps/chocolate-heretic.png
%{_datadir}/icons/hicolor/64x64/apps/chocolate-hexen.png
%{_datadir}/icons/hicolor/64x64/apps/chocolate-setup.png
%{_datadir}/icons/hicolor/64x64/apps/chocolate-strife.png
%{_metainfodir}/%{rtld}.Doom.metainfo.xml
%{_metainfodir}/%{rtld}.Heretic.metainfo.xml
%{_metainfodir}/%{rtld}.Hexen.metainfo.xml
%{_metainfodir}/%{rtld}.Strife.metainfo.xml
%{_mandir}/man5/chocolate-doom.cfg.5*
%{_mandir}/man5/chocolate-heretic.cfg.5*
%{_mandir}/man5/chocolate-hexen.cfg.5*
%{_mandir}/man5/chocolate-strife.cfg.5*
%{_mandir}/man5/default.cfg.5*
%{_mandir}/man5/heretic.cfg.5*
%{_mandir}/man5/hexen.cfg.5*
%{_mandir}/man5/strife.cfg.5*
%{_mandir}/man6/chocolate-doom.6*
%{_mandir}/man6/chocolate-doom-setup.6*
%{_mandir}/man6/chocolate-heretic-setup.6*
%{_mandir}/man6/chocolate-heretic.6*
%{_mandir}/man6/chocolate-hexen-setup.6*
%{_mandir}/man6/chocolate-hexen.6*
%{_mandir}/man6/chocolate-server.6*
%{_mandir}/man6/chocolate-strife-setup.6*
%{_mandir}/man6/chocolate-strife.6*


%changelog
* Fri Jan 24 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 3.1.0-5
- Fix crash during startup

* Thu Jan 16 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 3.1.0-4
- Fix build failure with gcc15

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 27 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 3.1.0-2
- Fix installing .desktop files for non-existent executables

* Tue Aug 13 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 3.1.0-1
- Update to v3.1.0
- Drop Patch0 (duplicate definitions in code - backport from this release)
- Drop Fedora-specific metainfo file (now provided by upstream)

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 3.0.1-8
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Feb 02 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 3.0.1-1
- Update to v3.0.1
- Add a patch to fix python-related build failures
- Move validating desktop files to %%check
- Add validation for the appdata.xml file
- Do not assume man pages will be gzipped

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 19 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.0.0-5
- GCC 10 patch to fix FTBFS.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 24 2018 Filipe Rosset <rosset.filipe@gmail.com> - 3.0.0-1
- update to new upstream release 3.3.0 fixes rhbz #1543425
- spec cleanup and modernization

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 05 2017 Filipe Rosset <rosset.filipe@gmail.com> - 2.3.0-1
- Rebuilt for new upstream release 2.3.0 fixes rhbz #1446935
- Fix Provides replace bundled md5 for sha1 rhbz #1249213

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 06 2016 Filipe Rosset <rosset.filipe@gmail.com> - 2.2.1-1
- Update to new upstream release 2.2.1 fixes RHBZ #1307376

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 13 2015 Rahul Sundaram <sundaram@fedoraproject.org> - 2.2.0
- update to 2.2.0

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.6.0-10
- Add an AppData file for the software center

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Dec 31 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.6.0-7
- Install docs into %%pkgdocdir.
- BR: %%{__python} (Address FTBFS RHBZ #992055).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Aug 20 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 1.6.0-2
- use dist tag and added provides on bundled(md5-plumb) as per review

* Tue Aug 16 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 1.6.0-1
- initial spec 
