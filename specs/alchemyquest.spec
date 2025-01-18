Name:           alchemyquest
Version:        0.5.2
Release:        16%{?dist}
Summary:        Reflection game
# Code is GPLv2+ and graphics are CC-BY-SA
# Automatically converted from old format: GPLv2+ and CC-BY-SA - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-CC-BY-SA
URL:            http://identicalsoftware.com/alchemyquest/

Source0:        %{url}/%{name}-%{version}.tgz

BuildRequires: boost-devel
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: expat-devel
BuildRequires: gcc-c++
BuildRequires: libgamerzilla-devel
BuildRequires: libappstream-glib
BuildRequires: libzip-devel
BuildRequires: make
BuildRequires: SDL2-devel
BuildRequires: SDL2_image-devel
BuildRequires: SDL2_mixer-devel
Requires:      hicolor-icon-theme
Provides:      openalchemist = 0.4-34
Obsoletes:     openalchemist < 0.4-34


%description
Alchemy Quest is a new reflection game which looks like classic falling block
games but where you can take your time. Be a crazy alchemist and try to make
new objects from those you get from the sky.


%prep
%setup -q


%build
%cmake
%cmake_build


%install
%cmake_install

rm -f %{buildroot}%{_datadir}/alchemyquest/{CODE-LICENSE,GRAPHICS-LICENSE}

# Running alchemyquest through an openalchemist symlink will launch the game
# in openalchemist mode w/o needing a command line option.
pushd %{buildroot}%{_bindir} && ln -s alchemyquest openalchemist && popd

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/16x16/apps
install -p -m 644 icons/16x16/apps/alchemyquest.png \
    %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/alchemyquest.png
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 icons/32x32/apps/alchemyquest.png \
    %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/alchemyquest.png
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 icons/48x48/apps/alchemyquest.png \
    %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/alchemyquest.png

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -p -m 644 data/logo_svg.svg \
    %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/openalchemist.svg
desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
    alchemyquest.desktop
desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
    openalchemist.desktop

mkdir -p %{buildroot}%{_metainfodir}
install -p -m 644 %{name}.appdata.xml \
    %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
install -p -m 644 openalchemist.appdata.xml \
    %{buildroot}%{_metainfodir}/openalchemist.metainfo.xml
appstream-util validate-relax --nonet \
    %{buildroot}%{_metainfodir}/*.metainfo.xml


%files
%doc AUTHORS ChangeLog README.md
%license CODE-LICENSE GRAPHICS-LICENSE
%{_bindir}/alchemyquest
%{_bindir}/openalchemist
%{_datadir}/alchemyquest
%{_datadir}/icons/hicolor/scalable/apps/openalchemist.svg
%{_datadir}/icons/hicolor/*/apps/alchemyquest.png
%{_metainfodir}/%{name}.metainfo.xml
%{_metainfodir}/openalchemist.metainfo.xml
%{_datadir}/applications/openalchemist.desktop
%{_datadir}/applications/alchemyquest.desktop


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.2-15
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Jonathan Wakely <jwakely@redhat.com> - 0.5.2-10
- Rebuilt for Boost 1.83

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 0.5.2-8
- Rebuilt for Boost 1.81

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 0.5.2-5
- Rebuilt for Boost 1.78

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jul 17 2021 Dennis Payne <dulsi@identicalsoftware.com> - 0.5.2-3
- Correct obsoletes/provides

* Mon Jun 28 2021 Dennis Payne <dulsi@identicalsoftware.com> - 0.5.2-2
- Convert to metainfo.xml and all appstream-util-validate

* Sat Jun 26 2021 Dennis Payne <dulsi@identicalsoftware.com> - 0.5.2-1
- Changed directories to alchemyquest
- Obsoletes/provides because alchemyquest is an updated version of the code
    base and can still run the original game.

* Sun May 02 2021 Dennis Payne <dulsi@identicalsoftware.com> - 0.5.1-1
- Initial build
