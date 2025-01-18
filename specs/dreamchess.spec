%undefine __cmake_in_source_build

#global commit0 5db249cfb09b40cd80a933da8aa2fb8431054a35
#global cdate0  20190318

%global engine  dreamer

Name:           dreamchess
Version:        0.3.0%{?cdate0:~%{cdate0}git}
Release:        4%{?dist}
Summary:        Portable chess game
# GPLv2+ generally for most of sources
# but BSD for dreamchess/src/include/gamegui/queue.h
License:        GPLv3+ and BSD
URL:            https://www.%{name}.org/
%if 0%{?cdate0}
Source0:        https://github.com/%{name}/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{commit0}.tar.gz
%else
Source0:        https://github.com/%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
%endif

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  bison flex

BuildRequires:  SDL2-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  expat-devel
BuildRequires:  glew-devel
BuildRequires:  help2man
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

# icons get installed into hicolor folders
Requires:       hicolor-icon-theme

Requires:       chessprogram

%if 0%{?fedora}
Suggests:       %{name}-engine
Suggests:       gnuchess
%endif

Requires:       %{name}-data = %{version}-%{release}

%description
DreamChess is an open source chess game.

Features:
- 3D OpenGL graphics
- various chess board sets: from classic wooden to flat figurines
- music, sound effects
- on-screen move lists using SAN notation
- undo functionality
- save-games in PGN format

A moderately strong chess engine as a sub-package: Dreamer.


%package engine
Summary:        A moderately strong chess engine for the game DreamChess
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
Provides:       chessprogram

%if 0%{?fedora}
Supplements:    %{name}
%endif

%description engine
Should this chess engine be too weak for you, then you can use any other
XBoard-compatible chess engine, including the popular Crafty and GNU Chess.


%package data
Summary:        Data files for the game DreamChess
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description data
Data files for the game DreamChess:
Boards, Pieces, Sounds, Styles, Themes.


%prep
%autosetup %{?cdate0:-n %{name}-%{commit0}}

%build
%cmake \
 -DCMAKE_INSTALL_DOCDIR=%{_docdir}/%{name}
%cmake_build
# generate manpage
help2man -o %{name}.1 --no-discard-stderr \
 --version-string='%{version}' -v'%{release}' \
 %{_vpath_builddir}/%{name}/src/%{name}

%install
%cmake_install
install -D -t %{buildroot}%{_mandir}/man1 %{name}.1

mkdir -p %{buildroot}%{_metainfodir}
cat <<EOF > %{buildroot}%{_metainfodir}/%{name}.appdata.xml
<?xml version="1.0" encoding="UTF-8"?>
<component type="desktop-application">
    <id>org.dreamchess.dreamchess</id>
    <name>DreamChess</name>
    <summary>Portable Chess Game</summary>
    <metadata_license>FSFAP</metadata_license>
    <project_license>GPL-3.0-or-later</project_license>
    <description>
        <p>
            DreamChess is an open source chess game. DreamChess features 3D 
            OpenGL graphics and provides various chess board sets, ranging from 
            classic wooden to flat figurines.
        </p>
        <p>
            A moderately strong chess engine is included: Dreamer. However,
            should this engine be too weak for you, then you can use any other 
            XBoard-compatible chess engine, including GNU Chess.
        </p>
        <p>
            Other features include music, sound effects, on-screen move lists 
            using SAN notation, undo functionality, and savegames in PGN format.
        </p>
    </description>
    <launchable type="desktop-id">%{name}.desktop</launchable>
    <provides>
        <binary>%{name}</binary>
    </provides>
    <content_rating type="oars-1.1"/>
    <developer_name>DreamChess project</developer_name>
    <releases>
        <release version="%{version}" date="%(date +%F -r %{SOURCE0})" />
    </releases>
    <screenshots>
        <screenshot type="default">
            <caption>Classic Wooden theme</caption>
            <image>https://www.dreamchess.org/assets/images/screenshots/classic.png</image>
        </screenshot>
        <screenshot>
            <caption>Opposing Elements theme</caption>
            <image>https://www.dreamchess.org/assets/images/screenshots/elements.png</image>
        </screenshot>
        <screenshot>
            <caption>Figurine theme</caption>
            <image>https://www.dreamchess.org/assets/images/screenshots/figurine.png</image>
        </screenshot>
        <screenshot>
            <caption>Sketch theme</caption>
            <image>https://www.dreamchess.org/assets/images/screenshots/sketch.png</image>
        </screenshot>
        <screenshot>
            <caption>Title screen</caption>
            <image>https://www.dreamchess.org/assets/images/screenshots/title.png</image>
        </screenshot>
    </screenshots>
    <url type="homepage">%{url}</url>
</component>
EOF

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml


%files
%license LICENSE.txt
%doc README.md NEWS.md AUTHORS.txt LICENSE.txt
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man*/%{name}.*
%{_metainfodir}/%{name}.appdata.xml

%files engine
%license LICENSE.txt
%doc AUTHORS.txt
%{_bindir}/%{engine}
%{_mandir}/man*/%{engine}.*

%files data
%license LICENSE.txt
%{_datadir}/%{name}/


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3.0-3
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 0.3.0-1
- Update to 0.3.0 final
- Add AppStream data

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-0.18.20180601git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-0.17.20180601git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-0.16.20180601git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-0.15.20180601git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-0.14.20180601git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 10 2022 Orion Poplawski <orion@nwra.com> - 0.3.0-0.13.20180601git
- Rebuild for glew 2.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-0.12.20180601git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-0.11.20180601git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-0.10.20180601git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-0.9.20180601git
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-0.8.20180601git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-0.7.20180601git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-0.6.20180601git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-0.5.20180601git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.3.0-0.4.20180601git
- Rebuilt for glew 2.1.0

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 0.3.0-0.3.20180601git
- Rebuild with fixed binutils

* Sun Jul 29 2018 Raphael Groner <projects.rg@smart.ms> - 0.3.0-0.2.20180601git
- drop accidently duplicated files

* Sat Jul 28 2018 Raphael Groner <projects.rg@smart.ms> - 0.3.0-0.1.20180601git
- new version, use latest snapshot
- switch to cmake
- add new build dependencies, e.g. SDL2
- cleanup generally

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-20.RC2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-19.RC2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.1-18.RC2
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-17.RC2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-16.RC2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-15.RC2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 0.2.1-14.RC2
- Rebuild for glew 2.0.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-13.RC2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 0.2.1-12.RC2
- Rebuild for glew 1.13

* Mon Aug 31 2015 Raphael Groner <projects.rg@smart.ms> - 0.2.1-11.RC2
- upstream moved to GitHub

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-10.RC2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan 28 2015 Raphael Groner <projects.rg [AT] smart.ms> - 0.2.1-9.RC2
- introduce license macro

* Sat Jan 03 2015 Raphael Groner <projects.rg [AT] smart.ms> - 0.2.1-8.RC2
- add manpage

* Sat Dec 27 2014 Raphael Groner <projects.rg [AT] smart.ms> - 0.2.1-7.RC2
- add glew as dependency
- add icon cache scriptlets

* Tue Dec 23 2014 Raphael Groner <projects.rg [AT] smart.ms> - 0.2.1-6.RC2
- v0.2.1 RC2
- use proper download url
- honor icons & desktop file from make install

* Tue Oct 07 2014 Raphael Groner <projects.rg [AT] smart.ms> - 0.2.1-5.1.RC1
- temporarily, disable weak dependencies due to unclear policy

* Mon Sep 29 2014 Raphael Groner <projects.rg [AT] smart.ms> - 0.2.1-5.RC1
- use desktop file from source tarball
- enable Suggests (rpm 4.12)

* Sun Sep 14 2014 Raphael Groner <projects.rg [AT] smart.ms> - 0.2.1-4.RC1
- fix folder owner

* Sun Sep 14 2014 Raphael Groner <projects.rg [AT] smart.ms> - 0.2.1-3.RC1
- fix Requires with right version
- rename dreamer sub-package to just engine
- licence of engine sub-package
- spelling for rpmlint

* Sat Sep 13 2014 Raphael Groner <projects.rg [AT] smart.ms> - 0.2.1-2.RC1
- dreamer engine provides chessprogram as a sub-package
- description mentions features
- manpages should not be in doc
- general cleanup for review
- proper licences
- tag for pre-release

* Wed Sep 10 2014 Raphael Groner <projects.rg [AT] smart.ms> - 0.2.1-1
- initial
