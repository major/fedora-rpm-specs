# Define destination dir.
%global destdir     %{_datadir}/%{name}

# Setup _pkgdocdir if not defined already.
%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}

# Define available languages.
%global avail_langs us uk fr de it es
%global lang_list   %(echo "%{?avail_langs}" | %{__sed} -e 's! !,!g')

# Define common part of source-url.
%global src_url     http://downloads.sf.net/scummvm/%{name}-

# Define commonly used description.
%global common_desc                                                \
Ryan, a bartender from a dystopian future can't sleep peacefully   \
for months.  His nights are sequences of nightmares and strange    \
dreams, days with frequent black-outs with strange visions, until  \
one night a figure in monk attire appears to him, and tells him the \
story of the seven evil ones, uniting to destroy to Dreamweb, the   \
only barrier between the world and darkness.  The monk makes a      \
proposition:  Ryan becomes the "deliverer":  the one who would keep \
the Dreamweb safe by killing those who try to destroy it.           \
                                                                    \
Descending into paranoia and just wanting dreams to stop, Ryan      \
accepts the mission, then wakes up in a puddle of cold sweat, next  \
to his beloved girlfriend in her house, and late for work.  Again.  \
                                                                    \
DreamWeb is a top-down adventure game set in a gritty futuristic    \
dystopian city.  Each location takes only a small portion of the    \
screen without panning (except an optional small zoom window in the \
corner that follows the cursor), with the player interacting with   \
objects and people by simply clicking them.  Ryan has a limited     \
inventory space, and as a lot of objects can be picked up (many     \
without any use), the player must rationalize what might be useful  \
and what just serves as filler.                                     \
                                                                    \
Dialogue is straightforward, with no options, but still required    \
to advance in the game (to find new locations, for instance).  In   \
situations where many adventure games usually feature an indirect   \
approach to solve a problem, Ryan often faces himself with          \
situations where it's "killed or be killed", which result in deaths \
(sometimes of innocents).


Name:           dreamweb
Version:        1.1
Release:        20%{?dist}
Summary:        Click-and-point adventure with the look and feel of Ridley Scott's Blade Runner

# The license-file included in the sources says:
#
# Dreamweb PC DOS version. Version 1.1
# (C) 1994 Neil Dodwell and David Dew trading as Creative Reality
# ---------------------------------------------------------------------------
#
# Changelog:
# v1.1 Added manual and diary scans. With help from
#      Simon Sawatzki (SimSaw@gmx.de)
# v1.0 Initial freeware release
#
#
# LICENSE:
#
#  1) You may distribute this game for free on any medium, provided this
#     license and all associated copyright notices and disclaimers are left
#     intact.
#
#  2) You may charge a reasonable copying fee for this archive, and may
#     distribute it in aggregate as part of a larger & possibly commercial
#     software distribution (such as a Linux distribution or magazine
#     coverdisk).  You must provide proper attribution and ensure this
#     license and all associated copyright notices, and disclaimers are
#     left intact.
#
#  3) You may not charge a fee for the game itself.  This includes reselling
#     the game as an individual item.
#
#  4) All game content is (C) Neil Dodwell and David Dew trading as Creative
#     Reality.  The ScummVM engine is (C) The ScummVM Team (www.scummvm.org).
#
#  5) THE GAMEDATA IN THIS ARCHIVE IS PROVIDED "AS IS" AND WITHOUT ANY
#     EXPRESS OR IMPLIED WARRANTIES, INCLUDING AND NOT LIMITED TO ANY
#     IMPLIED WARRANTIES OF MERCHANTIBILITY AND FITNESS FOR A PARTICULAR
#     PURPOSE.
#
# According to some discussion with Tom "spot" Callaway about 10 years ago,
# this should be free enough for distribution within Fedora. For further
# reference have a look at:
# http://www.redhat.com/archives/fedora-extras-list/2006-November/msg00030.html
#
License:        Redistributable, no modification permitted
URL:            http://www.mobygames.com/game/%{name}
Source0:        %{src_url}cd-us-%{version}.zip

# Other localizations.
Source10:       %{src_url}cd-uk-%{version}.zip
Source11:       %{src_url}cd-fr-%{version}.zip
Source12:       %{src_url}cd-de-%{version}.zip
Source13:       %{src_url}cd-it-%{version}.zip
Source14:       %{src_url}cd-es-%{version}.zip

# Documentation / Manuals.
Source90:       %{src_url}manuals-en-highres.zip
Source91:       %{src_url}manuals-en-lores.zip

BuildArch:      noarch

BuildRequires:  desktop-file-utils dos2unix fdupes vorbis-tools

%description
%{?common_desc}


%package common
Summary:        Common files used by %{name}

# The files inside this sub-pkg are pretty useless without the files
# shipped with the other packages.
Requires:       %{name}        == %{version}-%{release}
Requires:       filesystem
Requires:       scummvm

%description common
This package contains common files used by %{name}.

%{?common_desc}


%package doc
Summary:        Documentation files for %{name}

%description doc
This package contains documentation files used by %{name}. The
documentation contains manuals and other stuff delivered with the
retail package in high and low resolution quality.  Additionally
it contains translated versions for all available language
versions of the game from those documents.

%{?common_desc}


%package us
Summary:        US-English language version of %{name}

Requires:       %{name}-common == %{version}-%{release}

# This package provides the localized content of the main-pkg.  This is
# also needed to satisfy the Requires of the common sub-pkg.
Provides:       %{name}        == %{version}-%{release}

%description us
This package contains the US-English language version of %{name}, a
click-and-point adventure with the look and feel of Ridley Scott's
Blade Runner.

%{?common_desc}


%package uk
Summary:        UK-English language version of %{name}

Requires:       %{name}-common == %{version}-%{release}

# This package provides the localized content of the main-pkg.  This is
# also needed to satisfy the Requires of the common sub-pkg.
Provides:       %{name}        == %{version}-%{release}

%description uk
This package contains the UK-English language version of %{name}, a
click-and-point adventure with the look and feel of Ridley Scott's
Blade Runner.

%{?common_desc}


%package fr
Summary:        French language version of %{name}

Requires:       %{name}-common == %{version}-%{release}

# This package provides the localized content of the main-pkg.  This is
# also needed to satisfy the Requires of the common sub-pkg.
Provides:       %{name}        == %{version}-%{release}

%description fr
This package contains the French language version of %{name}, a
click-and-point adventure with the look and feel of Ridley Scott's
Blade Runner.

%{?common_desc}


%package de
Summary:        German language version of %{name}

Requires:       %{name}-common == %{version}-%{release}

# This package provides the localized content of the main-pkg.  This is
# also needed to satisfy the Requires of the common sub-pkg.
Provides:       %{name}        == %{version}-%{release}

%description de
This package contains the German language version of %{name}, a
click-and-point adventure with the look and feel of Ridley Scott's
Blade Runner.

%{?common_desc}


%package it
Summary:        Italian language version of %{name}

Requires:       %{name}-common == %{version}-%{release}

# This package provides the localized content of the main-pkg.  This is
# also needed to satisfy the Requires of the common sub-pkg.
Provides:       %{name}        == %{version}-%{release}

%description it
This package contains the Italian language version of %{name}, a
click-and-point adventure with the look and feel of Ridley Scott's
Blade Runner.

%{?common_desc}


%package es
Summary:        Spanish language version of %{name}

Requires:       %{name}-common == %{version}-%{release}

# This package provides the localized content of the main-pkg.  This is
# also needed to satisfy the Requires of the common sub-pkg.
Provides:       %{name}        == %{version}-%{release}

%description es
This package contains the Spanish language version of %{name}, a
click-and-point adventure with the look and feel of Ridley Scott's
Blade Runner.

%{?common_desc}


%prep
# Create empty builddir and subdirs.
%setup -cqT
%{__mkdir} -p common %{?avail_langs}                           \
              doc/{common,manuals_hq,manuals_lq,%{?lang_list}}

# Setup sources in subdirs.  Move documentation-files into seperate subdir.
_file="%(echo %{SOURCE0} | %{__sed} -e 's!-us-.*$!!g')"
for _dir in %{?avail_langs}
do
  %{__unzip} -q -LL ${_file}-${_dir}-%{version}.zip -d ${_dir}
  for _doc in $(%{_bindir}/find ${_dir} -type f -name '*.htm*')
  do
    %{__mv} -f $(%{_bindir}/dirname ${_doc}) doc/${_dir}
  done
done

# Setup additional documentation-files.
%{__unzip} -q -LL %{SOURCE90} -d doc/manuals_hq
%{__unzip} -q -LL %{SOURCE91} -d doc/manuals_lq

# Change mode of all files to 0644, all dirs to 0755.
%{_bindir}/find . -type f -print0 | %{_bindir}/xargs -0 /bin/chmod -c 0644
%{_bindir}/find . -type d -print0 | %{_bindir}/xargs -0 /bin/chmod -c 0755


%build
# Remove files we intentionally don't ship.
%{_bindir}/find . -type f -name '*.exe' -print -delete

# The license-file is an identical copy inside all source-archives.
%{__mv} -f us/license.txt COPYING
%{_bindir}/find . -type f -name 'license*' -print -delete
%{__mv} -f COPYING license.txt

# Create desktop-files.
for _lang in %{?avail_langs}
do
  cat > %{name}-${_lang}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=DreamWeb (${_lang})
Comment=Adventure Game
Exec=%{_bindir}/scummvm -q ${_lang} -f -p /usr/share/%{name}/${_lang} %{name}
Icon=scummvm
Terminal=false
Type=Application
Categories=Game;AdventureGame;
StartupNotify=false
EOF
done

# Move duplicate files to common-dir.
_common_dir="%{?destdir}/common"

# The file 'track01.flac' is a flac-compressed version of 'dreamweb.wav',
# so we can safely remove and soft-link it to save ~25 MBytes of diskspace.
# ScummVM is able to play the uncompressed PCM-wave as well.
for _dir in %{?avail_langs}
do
  %{__rm} -f ${_dir}/track1.flac ${_dir}/track01.flac
  %{__ln_s} -f ${_common_dir}/dreamweb.wav ${_dir}/track01.wav
done

# Soft-link duplicate files into _common_dir.
for _file in $(%{_bindir}/fdupes -r1 . | %{__sed} -e '/doc\//d')
do
  _filename="$(/bin/basename ${_file})"
  %{__mv} -f ${_file} common/${_filename}
  %{__ln_s} -f ${_common_dir}/${_filename} ${_file}
done

pushd doc
# Move duplicate files to common-dir.
_common_dir="%{?_pkgdocdir}/common"

# Fix end-of-line-encoding.
%{_bindir}/find . -type f -name '*.txt' -print0 | \
  %{_bindir}/xargs -0 %{_bindir}/dos2unix -k

# Soft-link duplicate files into _common_dir.
for _file in $(%{_bindir}/fdupes -r1 .)
do
  _filename="$(/bin/basename ${_file})"
  %{__mv} -f ${_file} common/${_filename}
  %{__ln_s} -f ${_common_dir}/${_filename} ${_file}
done

# Soft-link duplicate files inside documentation.
%fdupes -s .
popd

pushd common
# Encode the PCM-wave with hq-theora.  That will save another
# ~ 42 MBytes of disk-space.
%{_bindir}/oggenc -q8 dreamweb.wav
/bin/touch -r dreamweb.wav dreamweb.ogg
%{__mv} -f dreamweb.ogg dreamweb.wav

# Soft-link duplicate files inside common.
%fdupes -s .
popd


%install
# Install the game-files.
%{__mkdir} -p %{buildroot}%{_datadir}/applications               \
              %{buildroot}%{?destdir} %{buildroot}%{?_pkgdocdir}
%{__cp} -a common %{?avail_langs} %{buildroot}%{?destdir}

# Install the documentation-files.
%{__cp} -a license.txt doc/* %{buildroot}%{?_pkgdocdir}

# Install the desktop-files.
for _lang in %{?avail_langs}
do
  %{_bindir}/desktop-file-install              \
    --dir=%{buildroot}%{_datadir}/applications \
    %{name}-${_lang}.desktop
done


%files common
%dir %{?destdir}
%doc %dir %{?_pkgdocdir}
%doc %{?_pkgdocdir}/common
%license license.txt
%{?destdir}/common

%files doc
%doc %{?_pkgdocdir}
%license license.txt

%files us
%doc %{?_pkgdocdir}/us
%{_datadir}/applications/%{name}-us.desktop
%{?destdir}/us

%files uk
%doc %{?_pkgdocdir}/uk
%{_datadir}/applications/%{name}-uk.desktop
%{?destdir}/uk

%files fr
%doc %{?_pkgdocdir}/fr
%{_datadir}/applications/%{name}-fr.desktop
%{?destdir}/fr

%files de
%doc %{?_pkgdocdir}/de
%{_datadir}/applications/%{name}-de.desktop
%{?destdir}/de

%files it
%doc %{?_pkgdocdir}/it
%{_datadir}/applications/%{name}-it.desktop
%{?destdir}/it

%files es
%doc %{?_pkgdocdir}/es
%{_datadir}/applications/%{name}-es.desktop
%{?destdir}/es


%changelog
* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Björn Esser <besser82@fedoraproject.org> - 1.1-9
- Modernize spec file

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Feb 22 2015 Björn Esser <bjoern.esser@gmail.com> - 1.1-1
- initial rpm release (#1206901)
