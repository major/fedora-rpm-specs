# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

# Git submodules
%global qmarkdowntextedit_commit        11e7a3530d4b6e28eee90cd4292c35be4bdd4112
%global qmarkdowntextedit_shortcommit   %(c=%{qmarkdowntextedit_commit}; echo ${c:0:7})

%global qttoolbareditor_commit          ca0728c9924c6464234f7e477aa9509293d0a324
%global qttoolbareditor_shortcommit     %(c=%{qttoolbareditor_commit}; echo ${c:0:7})

%global qtcsv_commit                    ae15c33b066fea9373a07bed5dc898c10b45ce2a
%global qtcsv_shortcommit               %(c=%{qtcsv_commit}; echo ${c:0:7})

%global piwiktracker_commit             810a7e40c87cd736e883720fc11713a110d6a423
%global piwiktracker_shortcommit        %(c=%{piwiktracker_commit}; echo ${c:0:7})

%global qkeysequencewidget_commit       8cbb54a12f33e41bf7c4795405f4235db1ee8ff1
%global qkeysequencewidget_shortcommit  %(c=%{qkeysequencewidget_commit}; echo ${c:0:7})

%global qhotkey_commit                  4ebf343ec5dbae725ee3b3f68186c14a2836fae4
%global qhotkey_shortcommit             %(c=%{qhotkey_commit}; echo ${c:0:7})


%global appname QOwnNotes
%global url1 https://github.com/pbek

Name:           qownnotes
Version:        26.10.8
Release:        %autorelease
Summary:        Plain-text file notepad and todo-list manager with Markdown support

# The entire source code is MIT except bundled libs:
# BSD:          qdarkstyle
#               qkeysequencewidget
#               qmarkdowntextedit
#               singleapplication
#               simplecrypt
# MIT:                  piwiktracker
# GPL-2.0-only:         versionnumber
# GPL-3.0-or-later:     qttoolbareditor
# LGPL-2.1-or-later:    fakevim
# Apache-2.0:           diff_match_patch
License:        MIT AND BSD-2-Clause AND BSD-3-Clause AND GPL-2.0-only AND GPL-3.0-or-later AND LGPL-2.1-or-later AND Apache-2.0
URL:            https://www.qownnotes.org
Source0:        %{url1}/%{appname}/archive/v%{version}/%{appname}-%{version}.tar.gz
Source1:        %{url1}/qmarkdowntextedit/archive/%{qmarkdowntextedit_commit}/qmarkdowntextedit-%{qmarkdowntextedit_shortcommit}.tar.gz
Source2:        %{url1}/Qt-Toolbar-Editor/archive/%{qttoolbareditor_commit}/qttoolbareditor-%{qttoolbareditor_shortcommit}.tar.gz
Source3:        %{url1}/qtcsv/archive/%{qtcsv_commit}/qtcsv-%{qtcsv_shortcommit}.tar.gz
Source5:        %{url1}/qt-piwik-tracker/archive/%{piwiktracker_commit}/piwiktracker-%{piwiktracker_shortcommit}.tar.gz
Source6:        %{url1}/qkeysequencewidget/archive/%{qkeysequencewidget_commit}/qkeysequencewidget-%{qkeysequencewidget_shortcommit}.tar.gz
Source8:        https://github.com/%{name}/QHotkey/archive/%{qhotkey_commit}/qhotkey-%{qhotkey_shortcommit}.tar.gz
# AppData manifest
Source100:      https://raw.githubusercontent.com/flathub/org.qownnotes.%{appname}/master/org.qownnotes.%{appname}.appdata.xml

Patch1000:      system-qtkeychain.patch
Patch1001:      system-md4c.patch

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  libappstream-glib

BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6WebSockets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6Keychain)

BuildRequires:  pkgconfig(botan-3)
BuildRequires:  pkgconfig(md4c-html)

Requires:       hicolor-icon-theme
Requires:       qt6-qtbase%{?_isa}

Recommends:     git-core
Recommends:     hunspell

Provides:       bundled(fakevim) = 0.0.1
Provides:       bundled(qhotkey) = 1.3.0~git%{qhotkey_commit}
Provides:       bundled(qkeysequencewidget) = 1.0.1
Provides:       bundled(qmarkdowntextedit) = 2019.4.0~git%{qmarkdowntextedit_shortcommit}
Provides:       bundled(qt-piwik-tracker) = 0~git%{piwiktracker_shortcommit}
Provides:       bundled(qt-toolbar-editor) = 0~git%{qttoolbareditor_shortcommit}
Provides:       bundled(qtcsv) = 1.2.2

Obsoletes:      %{name}-translations < %{version}-%{release}

%description
QOwnNotes is the open source notepad with Markdown support and todo list manager
for GNU/Linux, macOS and Windows, that works together with Nextcloud Notes and
ownCloud Notes.

You are able to write down your thoughts with QOwnNotes and edit or search for
them later from your mobile device, like with Nextcloud Notes for Android or the
Nextcloud / ownCloud web-service.

The notes are stored as plain text markdown files and are synced with
Nextcloud's/ownCloud's file sync functionality. Of course other software, like
Syncthing or Dropbox can be used too.

If you like the concept of having notes accessible in plain text files, like it
is done in the Nextcloud / ownCloud notes apps to gain a maximum of freedom then
QOwnNotes is for you.


%prep
%setup -q -n %{appname}-%{version} -a1 -a2 -a3 -a5 -a6 -a8
%autopatch -p1

mv qmarkdowntextedit-%{qmarkdowntextedit_commit}/*      src/libraries/qmarkdowntextedit/
mv Qt-Toolbar-Editor-%{qttoolbareditor_commit}/*        src/libraries/qttoolbareditor/
mv qtcsv-%{qtcsv_commit}/*                              src/libraries/qtcsv/
mv qt-piwik-tracker-%{piwiktracker_commit}/*            src/libraries/piwiktracker/
mv qkeysequencewidget-%{qkeysequencewidget_commit}/*    src/libraries/qkeysequencewidget/
mv QHotkey-%{qhotkey_commit}/*                          src/libraries/qhotkey/


%build
%cmake                            \
    -DQON_QT6_BUILD=ON            \
    -DBUILD_WITH_SYSTEM_BOTAN=ON  \
    -S src
%cmake_build


%install
%cmake_install
# AppData manifest
install -D -p -m 0644 %{SOURCE100} -t %{buildroot}%{_metainfodir}/
%find_lang %{appname} --with-qt


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{appname}.lang
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/%{appname}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/scalable/*/*.svg
%{_metainfodir}/*.xml


%changelog
%autochangelog
