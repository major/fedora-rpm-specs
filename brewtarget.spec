# force out-of-tree build for spec compatibility with older releases
%undefine __cmake_in_source_build

%global forgeurl https://github.com/Brewtarget/brewtarget

%global _description %{expand:
Brewtarget is an open source beer recipe creation tool. It automatically
calculates color, bitterness, and other parameters for you while you drag and
drop ingredients into the recipe. Brewtarget also has many other tools such as
priming sugar calculators, OG correction help, and a unique mash designing tool.
It also can export and import recipes in BeerXML.}

Name:           brewtarget
Version:        3.0.3
Release:        1%{?dist}
Summary:        An open source beer recipe creation tool 🍺
%forgemeta
# BSD-2-Clause: cmake/modules/FindPhonon.cmake
# WTFPL: images/flag* images/bubbles.svg images/convert.svg images/grain2glass.svg
# CC-BY-SA-3.0 OR LGPL-3.0-only: images/edit-copy.png images/document-print-preview.png
#     images/merge.png images/preferences-other.png images/printer.png
#     images/server-database.png images/kbruch.png images/help-contents.png
# LGPL-2.1-only: images/backup.png
License:    GPL-3.0-or-later AND BSD-2-Clause AND WTFPL AND (CC-BY-SA-3.0 OR LGPL-3.0-only) AND LGPL-2.1-only
URL:        %{forgeurl}
Source0:    %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  qt5-qtbase-devel, qt5-qtwebkit-devel, qt5-qtsvg-devel
BuildRequires:  qt5-qtmultimedia-devel, qt5-linguist
BuildRequires:  boost-devel, xerces-c-devel, xalan-c-devel
BuildRequires:  desktop-file-utils
Requires:       sqlite

%description %_description

%prep
%setup -q -n %{name}-%{version}

%build
%cmake -DDO_RELEASE_BUILD:BOOL=ON
%cmake_build

%install
%cmake_install
# Remove generated files. We use what's provided in tarball.
rm %buildroot/%{_docdir}/%{name}/{RelaseNotes.markdown,changelog.Debian.gz,copyright}
gzip doc/brewtarget.1
/usr/bin/install -m 0644 -Dp doc/brewtarget.1.gz %buildroot%{_mandir}/man1/brewtarget.1.gz
# symlink manual, which is accessible in application
rm %buildroot/%{_datadir}/%{name}/manual-en.pdf
pushd %buildroot/%{_datadir}/%{name}
ln -s ../doc/%{name}/manual-en.pdf .
popd

%check
desktop-file-validate %buildroot%{_datadir}/%{name}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/brewtarget*
%doc CHANGES.markdown README.markdown doc/manual-en.pdf
%license COPYRIGHT COPYING.GPLv3 COPYING.WTFPL

%changelog
%autochangelog
