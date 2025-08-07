Name:           Zim
Version:        0.76.3
Release:        %autorelease
Summary:        Desktop wiki & notekeeper

# Most source code is GPL-2.0-or-later
# ./zim/plugins/pageindex/generictreemodel,.py is LGPL-2.1-or-later
# Some icons are MIT
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
URL:            http://zim-wiki.org/
Source0:        http://www.zim-wiki.org/downloads/zim-%{version}.tar.gz
# Crashes the test run, and is also disabled for Mac OS in upstream repo
Patch:          0000-Disable-TestPlugins-test.patch
# Install icons even when building Python wheels
Patch:          https://github.com/zim-desktop-wiki/zim-desktop-wiki/pull/2859.patch
BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel
BuildRequires:  python3-gobject
BuildRequires:  gtk3, python3-pyxdg
# for tests
BuildRequires:  /usr/bin/xvfb-run
BuildRequires:  glibc-langpack-en

Requires:       python3-gobject
Requires:       gtk3, python3-pyxdg
Recommends:     libappindicator-gtk3

%description
Zim is a WYSIWYG text editor written in Python which aims to bring the
concept of a wiki to your desktop. Every page is saved as a text file with
wiki markup. Pages can contain links to other pages, and are saved
automatically. Creating a new page is as easy as linking to a non-existing
page. Pages are ordered in a hierarchical structure that gives it the look
and feel of an outliner. This tool is intended to keep track of TODO lists
or to serve as a personal scratch book.

%prep
%autosetup -p1 -n zim-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l zim

%find_lang zim
cat zim.lang >> %{pyproject_files}

desktop-file-validate %{buildroot}%{_datadir}/applications/org.zim_wiki.Zim.desktop

%check
LANG=en_US.UTF-8 xvfb-run ./test.py

%files -f %{pyproject_files}
%doc *.md contrib/
%{_mandir}/man[13]/*.[13]*
%{_bindir}/*
%{_datadir}/zim/
%{_datadir}/applications/*
%{_datadir}/mime/packages/org.zim_wiki.Zim.xml
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/*/mimetypes/*
# No package in Fedora provides such directories
%{_datadir}/icons/ubuntu-mono-*/
%{_datadir}/metainfo/*

%changelog
%autochangelog
