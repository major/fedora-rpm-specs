Name:           qtpass
Version:        1.5.1
Release:        %autorelease
Summary:        Cross-platform GUI for pass

License:        GPL-3.0-only
URL:            https://qtpass.org/
Source0:        https://github.com/IJHack/qtpass/archive/v%{version}.tar.gz
# Wrapper script for GNOME on Wayland
Source1:        qtpass.sh.in

# # https://github.com/IJHack/QtPass/pull/656
# Patch1:         0001-Fix-build-with-Qt6.patch
# # https://github.com/IJHack/QtPass/pull/680
# Patch2:         0002-Update-new-TLDs.patch
# # https://github.com/IJHack/QtPass/pull/681
# Patch3:         0003-Fix-multiple-profiles-issue-for-Qt6.patch
# # https://github.com/IJHack/QtPass/pull/658
# Patch4:         0004-getRecipientListSplitByHash.patch
# # https://github.com/IJHack/QtPass/pull/690
# Patch5:         0005-fix-add-missing-QDirIterator-include.patch

# required tools
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  sed
# required libraries (QT)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-linguist
# install/check desktop files
BuildRequires:  desktop-file-utils
# for ownership of hicolor directories
Requires:       hicolor-icon-theme
# for icons to appear without freedesktop
Requires:       qt6-qtsvg
Requires:       pass

Recommends:     git
Recommends:     gpg2
Recommends:     pwgen

%description
QtPass is a cross-platform GUI for pass, the standard Unix password manager.

%prep
%autosetup -p1 -n QtPass-%{version}
sed -i "s|#include <QDir>|#include <QDir>\n#if QT_VERSION >= QT_VERSION_CHECK(6, 0, 0)\n#include <QStringDecoder>\n#endif|" src/executor.cpp
sed -i '/Version/d' %{name}.desktop

%build
%qmake_qt6 PREFIX=%{_prefix}
%make_build


%install
%make_install INSTALL_ROOT=%{buildroot}
desktop-file-install %{name}.desktop
install -Dpm 644 artwork/icon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/qtpass-icon.svg
install -Dpm 644 %{name}.appdata.xml %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
install -Dpm 644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

# Move the qtpass binary and replace it with the wrapper script
install -Dpm 755 %{buildroot}%{_bindir}/qtpass %{buildroot}%{_libexecdir}/qtpass
sed -e 's,/__PREFIX__,%{_libexecdir},g' %{SOURCE1} > %{buildroot}%{_bindir}/qtpass
chmod 755 %{buildroot}%{_bindir}/qtpass


%files
%doc README.md
%license LICENSE
%{_bindir}/qtpass
%{_libexecdir}/qtpass
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/%{name}-icon.svg
%{_mandir}/man1/%{name}.1*


%changelog
%autochangelog
