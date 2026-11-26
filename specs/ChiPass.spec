%global forgeurl https://codeberg.org/ChiPass/ChiPass/

Name:           ChiPass
Version:        2026.09.0
%global tag v%{version}
%forgemeta
Summary:        A Qt6 Password Manager
Release:        %{autorelease}
License:        GPL-2.0-or-later AND BSD-2-Clause AND MIT AND CC0-1.0 AND Apache-2.0 AND LGPL-2.0-only AND LGPL-2.1-only AND OFL-1.1
Group:          Productivity/Security
Url:            https://chipass.org/
Source:         %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  cmake >= 3.10.0
BuildRequires:  appstream
BuildRequires:  ninja-build >= 1.10
BuildRequires:  rubygem(asciidoctor)
BuildRequires:  pkgconfig(Qt6)
BuildRequires:  qt6-qttranslations
# For Fedora Packaging #
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  shared-mime-info
# #
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(botan-3)
BuildRequires:  pkgconfig(libargon2)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(minizip)
BuildRequires:  pkgconfig(libqrencode)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(libpcsclite)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  xclip
BuildRequires:  wl-clipboard
# There is a bug with detecting this. We can add the fedora version repo next release
Provides:       bundled(zxcvbn-c) 
# Qt 6 Components
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Core5Compat)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6SvgWidgets)
BuildRequires:  pkgconfig(Qt6Concurrent)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Linguist)
BuildRequires:  pkgconfig(Qt6Test)
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  cmake(Qt6GuiPrivate)

# ChiPass bundles the ykcore code due to lack of support from Yubico and
# stratification of versions across various operating system distros.
# Additionally, ChiPass has modified the API of ykcore to make it more
# functional when using non-YubiKey keys (ie, OnlyKey).
Provides:       bundled(ykcore)



%description 
A cross-platform password manager for people with extremely high demands
on secure personal data management. It is a fork of KeePassXC which does
not accept any AI contributions.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description doc
Documentation and manuals for %{name}.

# Note that the translations are linked into the compiled binary so a lang pack
# is not needed.

%prep
%setup -b 0 -n chipass

%conf
%cmake \
  -DCHIPASS_WITH_TESTS=OFF \
  -DCHIPASS_WITH_UPDATE_CHECK=OFF \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo

%build
%cmake_build
sed -i /heading/d redhat-linux-build/share/freedesktop/ChiPass.metainfo.xml

%install
%cmake_install

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.chipass.ChiPass.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/*.metainfo.xml
%ctest --exclude-regex gui
# GUI tests must be single-threaded
%__ctest --tests-regex gui \
         --test-dir "%{__cmake_builddir}"
         
%files
%license LICENSE.* COPYING
%doc CHANGELOG.md README.md
# These directories exist due to a bug in ChiPass and will be removed
# upon next release
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/man
%dir %{_datadir}/%{name}/man/man1
%{_datadir}/%{name}/man/man1/%{name}*
# End comment
%{_bindir}/%{name}*
%{_datadir}/icons/hicolor/*/*/*%{name}*
%{_datadir}/applications/org.chipass.ChiPass.desktop
%{_datadir}/metainfo/org.chipass.ChiPass.metainfo.xml
%{_datadir}/mime/packages/org.chipass.ChiPass-application-x-chipass.xml

%files doc
%{_datadir}/%{name}/docs/

%changelog 
* Sun Nov 22 20:28:41 UTC 2026 xc34 <xc34@mailbox.org> - 2026.09.0

- Initial package of ChiPass 2026.09.0 for openSUSE and Fedora
  https://codeberg.org/ChiPass/ChiPass/src/tag/v2026.09.0/CHANGELOG.md
  * Forked from KeePassXC 2.7.10
  * Ported application to Qt6
