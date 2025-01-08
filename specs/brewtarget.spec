Name:           brewtarget
Version:        4.0.15
Release:        %{autorelease}
Summary:        An open source beer recipe creation tool 🍺

%global forgeurl https://github.com/Brewtarget/brewtarget
%forgemeta

# BSD-2-Clause: cmake/modules/FindPhonon.cmake
# WTFPL: images/flag* images/bubbles.svg images/convert.svg images/grain2glass.svg
# CC-BY-SA-3.0 OR LGPL-3.0-only: images/edit-copy.png images/document-print-preview.png
#     images/merge.png images/preferences-other.png images/printer.png
#     images/server-database.png images/kbruch.png images/help-contents.png
# LGPL-2.1-only: images/backup.png
License:    GPL-3.0-or-later AND BSD-2-Clause AND WTFPL AND (CC-BY-SA-3.0 OR LGPL-3.0-only) AND LGPL-2.1-only
URL:        %{forgeurl}
Source:     %{forgesource}
# Downstream only patches
Patch:      0001-Modify-boost-requirements-for-Fedora.patch
Patch:      0002-Fix-name-of-lupdate-executable.patch
Patch:      0003-Use-system-installed-valijson.patch

BuildRequires:  boost-devel
BuildRequires:  cmake(qt6core)
BuildRequires:  cmake(qt6linguisttools)
BuildRequires:  cmake(qt6multimedia)
BuildRequires:  cmake(qt6svg)
BuildRequires:  cmake(valijson)
BuildRequires:  cmake(xalanc)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  meson
BuildRequires:  pkgconfig(xerces-c)
BuildRequires:  pandoc
BuildRequires:  xorg-x11-server-Xvfb

Requires:       sqlite

# Stop building for i686
# See: https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%global _description %{expand:
Brewtarget is an open source beer recipe creation tool. It automatically
calculates color, bitterness, and other parameters for you while you drag and
drop ingredients into the recipe. Brewtarget also has many other tools such as
priming sugar calculators, OG correction help, and a unique mash designing tool.
It also can export and import recipes in BeerXML.}

%description %_description


%prep
%autosetup -n %{name}-%{version} -S git
# Crude way of disabling testLogRotation
sed -i -e '/testLogRotation/d' meson.build


%build
%meson
%meson_build


%install
%meson_install


%check
# Run in minimal graphical env (thanks @ankursinha).
# We need to pass the Meson test command as a script to xvfb-run.
cat > mesontest.sh << EOF
#!/bin/sh
mkdir %{_builddir}/%{name}-%{version}/brewtarget-test
export TMPDIR="%{_builddir}/%{name}-%{version}/brewtarget-test"
%meson_test --verbose --timeout-multiplier 2
EOF
chmod a+x ./mesontest.sh
xvfb-run ./mesontest.sh
desktop-file-validate %buildroot%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man1/brewtarget*
%{_docdir}/%{name}/*.markdown
%{_docdir}/%{name}/copyright
%doc CHANGES.markdown README.md doc/manual-en.pdf
%license COPYRIGHT COPYING.GPLv3 LICENSE

%changelog
%autochangelog
