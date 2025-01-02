# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

# Git submodules
%global qmarkdowntextedit_commit        561167b58d19160140750b7c3b4567e00eb858b3
%global qmarkdowntextedit_shortcommit   %(c=%{qmarkdowntextedit_commit}; echo ${c:0:7})

%global qttoolbareditor_commit          ca0728c9924c6464234f7e477aa9509293d0a324
%global qttoolbareditor_shortcommit     %(c=%{qttoolbareditor_commit}; echo ${c:0:7})

%global qtcsv_commit                    ae15c33b066fea9373a07bed5dc898c10b45ce2a
%global qtcsv_shortcommit               %(c=%{qtcsv_commit}; echo ${c:0:7})

%global piwiktracker_commit             e7ee1fa6a130453b474be8bca455e27b0e25dfb9
%global piwiktracker_shortcommit        %(c=%{piwiktracker_commit}; echo ${c:0:7})

%global qkeysequencewidget_commit       8cbb54a12f33e41bf7c4795405f4235db1ee8ff1
%global qkeysequencewidget_shortcommit  %(c=%{qkeysequencewidget_commit}; echo ${c:0:7})

%global md4c_commit                     c64ee9ab326c53962b5bd8cca98c086461bbdd6b
%global md4c_shortcommit                %(c=%{md4c_commit}; echo ${c:0:7})

%global qhotkey_commit                  998c76c21bef8645802804d77e60a7dc8efcaf6f
%global qhotkey_shortcommit             %(c=%{qhotkey_commit}; echo ${c:0:7})


%global appname QOwnNotes
%global url1 https://github.com/pbek
%global forgeurl %{url1}/%{appname}

Name:           qownnotes
Version:        25.1.0
%forgemeta
Release:        %autorelease
Summary:        Plain-text file markdown note taking with Nextcloud integration

# The entire source code is MIT except bundled libs:
# BSD:          qdarkstyle
#               qkeysequencewidget
#               qmarkdowntextedit
#               singleapplication
#               simplecrypt
# MIT:                  piwiktracker
#                       md4c
# GPL-2.0-only:         versionnumber
# GPL-3.0-or-later:     qttoolbareditor
# LGPL-2.1-or-later:    fakevim
# Apache-2.0:           diff_match_patch
License:        MIT AND BSD-2-Clause AND BSD-3-Clause AND GPL-2.0-only AND GPL-3.0-or-later AND LGPL-2.1-or-later AND Apache-2.0
URL:            https://www.qownnotes.org
Source0:        %{forgesource}
Source1:        %{url1}/qmarkdowntextedit/archive/%{qmarkdowntextedit_commit}/qmarkdowntextedit-%{qmarkdowntextedit_shortcommit}.tar.gz
Source2:        %{url1}/Qt-Toolbar-Editor/archive/%{qttoolbareditor_commit}/qttoolbareditor-%{qttoolbareditor_shortcommit}.tar.gz
Source3:        %{url1}/qtcsv/archive/%{qtcsv_commit}/qtcsv-%{qtcsv_shortcommit}.tar.gz
Source5:        %{url1}/qt-piwik-tracker/archive/%{piwiktracker_commit}/piwiktracker-%{piwiktracker_shortcommit}.tar.gz
Source6:        %{url1}/qkeysequencewidget/archive/%{qkeysequencewidget_commit}/qkeysequencewidget-%{qkeysequencewidget_shortcommit}.tar.gz
Source7:        https://github.com/%{name}/md4c/archive/%{md4c_commit}/md4c-%{md4c_shortcommit}.tar.gz
Source8:        https://github.com/%{name}/QHotkey/archive/%{qhotkey_commit}/qhotkey-%{qhotkey_shortcommit}.tar.gz

BuildRequires:  cmake3
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  make

BuildRequires:  cmake(Qt5)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5WebSockets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(Qt5XmlPatterns)

# Switch to 'botan2'
# * https://github.com/pbek/QOwnNotes/issues/1263
%if 0%{?fedora} >= 32
BuildRequires:  pkgconfig(botan-2) >= 2.12.0
%endif

Requires:       hicolor-icon-theme
Requires:       qt5-qtbase%{?_isa}

Recommends:     %{name}-translations = %{version}-%{release}
Recommends:     hunspell

Provides:       bundled(fakevim) = 0.0.1
Provides:       bundled(md4c) = 0.4.2~git%{md4c_shortcommit}
Provides:       bundled(qhotkey) = 1.3.0~git%{qhotkey_commit}
Provides:       bundled(qkeysequencewidget) = 1.0.1
Provides:       bundled(qmarkdowntextedit) = 2019.4.0~git%{qmarkdowntextedit_shortcommit}
Provides:       bundled(qt-piwik-tracker) = 0~git%{piwiktracker_shortcommit}
Provides:       bundled(qt-toolbar-editor) = 0~git%{qttoolbareditor_shortcommit}
Provides:       bundled(qtcsv) = 1.2.2

%if 0%{?fedora} < 32
Provides:       bundled(botan) = 2.12.0
%endif

%description
QOwnNotes is the open source notepad with markdown support and todo list manager
for GNU/Linux, Mac OS X and Windows, that works together with the default notes
application of ownCloud and Nextcloud.

You are able to write down your thoughts with QOwnNotes and edit or search for
them later from your mobile device, like with CloudNotes or the
ownCloud/Nextcloud web-service.

The notes are stored as plain text files and are synced with
ownCloud's/Nextcloud's file sync functionality. Of course other software, like
Syncthing or Dropbox can be used too.

I like the concept of having notes accessible in plain text files, like it is
done in the ownCloud/Nextcloud notes apps, to gain a maximum of freedom, but I
was not able to find a decent desktop note taking tool or a text editor, that
handles them well. Out of this need QOwnNotes was born.


%package        translations
Summary:        Translations files for %{name}
BuildArch:      noarch

Requires:       %{name} = %{version}-%{release}

%description    translations
Translations files for %{name}.


%prep
%forgeautosetup -p1
%autosetup -n %{appname}-%{version} -D -T -a1
%autosetup -n %{appname}-%{version} -D -T -a2
%autosetup -n %{appname}-%{version} -D -T -a3
%autosetup -n %{appname}-%{version} -D -T -a5
%autosetup -n %{appname}-%{version} -D -T -a6
%autosetup -n %{appname}-%{version} -D -T -a7
%autosetup -n %{appname}-%{version} -D -T -a8

mv qmarkdowntextedit-%{qmarkdowntextedit_commit}/*      src/libraries/qmarkdowntextedit/
mv Qt-Toolbar-Editor-%{qttoolbareditor_commit}/*        src/libraries/qttoolbareditor/
mv qtcsv-%{qtcsv_commit}/*                              src/libraries/qtcsv/
mv qt-piwik-tracker-%{piwiktracker_commit}/*            src/libraries/piwiktracker/
mv qkeysequencewidget-%{qkeysequencewidget_commit}/*    src/libraries/qkeysequencewidget/
mv md4c-%{md4c_commit}/*                                src/libraries/md4c/
mv QHotkey-%{qhotkey_commit}/*                          src/libraries/qhotkey/
mkdir -p src/%{_target_platform}


%build
# Build translations
# * https://github.com/pbek/QOwnNotes/issues/1744
lrelease-qt5 src/%{appname}.pro

pushd src/%{_target_platform}
%qmake_qt5                        \
    PREFIX=%{buildroot}%{_prefix} \
    %if 0%{?fedora} >= 32
    USE_SYSTEM_BOTAN=1            \
    %endif
    ..
popd
%make_build -C src/%{_target_platform}


%install
%make_install -C src/%{_target_platform}
install -m 0644 -Dp obs/%{name}.appdata.xml %{buildroot}/%{_metainfodir}/%{name}.appdata.xml
%find_lang %{appname} --with-qt


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/%{appname}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/scalable/*/*.svg
%{_metainfodir}/*.xml

%files -f %{appname}.lang translations
%if 0%{?fedora} <= 34
%{_datadir}/qt5/translations/%{appname}_ceb.qm
%{_datadir}/qt5/translations/%{appname}_fil.qm
%{_datadir}/qt5/translations/%{appname}_hil.qm
%endif

%changelog
%autochangelog
