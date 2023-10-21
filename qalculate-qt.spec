Name:           qalculate-qt
Summary:        A multi-purpose desktop calculator for GNU/Linux
Version:        4.8.1
Release:        %autorelease

# The entire source is GPL-2.0-or-later, except:
#   - data/io.github.Qalculate.qalculate-qt.metainfo.xml is CC0-1.0, which is
#     allowed for content only
License:        GPL-2.0-or-later AND CC0-1.0
URL:            https://qalculate.github.io/
Source:         https://github.com/Qalculate/qalculate-qt/releases/download/v%{version}/qalculate-qt-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%global app_id io.github.Qalculate.qalculate-qt

BuildRequires:  gcc-c++

BuildRequires:  make
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-linguist

BuildRequires:  pkgconfig(libqalculate) >= %{version}
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(mpfr)

BuildRequires:  desktop-file-utils
# Still required by guidelines for now
# (https://pagure.io/packaging-committee/issue/1053):
BuildRequires:  libappstream-glib
# Matches what gnome-software and others use:
BuildRequires:  appstream

# For %%{_datadir}/icons/hicolor and its subdirectories:
Requires:       hicolor-icon-theme

# Upstream renamed/rewrote qalculate-kde as qalculate-qt. This package replaces
# qalculate-kde, and qalculate-kde is retired, beginning with F37. The
# Provides/Obsoletes could be removed no earlier than F40.
Provides:       qalculate-kde = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      qalculate-kde < 0.9.7.10-34

%description
Qalculate! is a multi-purpose cross-platform desktop calculator. It is simple
to use but provides power and versatility normally reserved for complicated
math packages, as well as useful tools for everyday needs (such as currency
conversion and percent calculation). Features include a large library of
customizable functions, unit calculations and conversion, symbolic calculations
(including integrals and equations), arbitrary precision, uncertainty
propagation, interval arithmetic, plotting, and a user-friendly interface.

This package provides a Qt graphical interface for Qalculate! 


%prep
%autosetup


%build
%qmake_qt6 \
    PREFIX='%{_prefix}' \
    DESKTOP_DIR='%{_datadir}/applications' \
    DESKTOP_ICONS_DIR='%{_datadir}/icons' \
    APPDATA_DIR='%{_metainfodir}' \
    MAN_DIR='%{_mandir}'
%make_build


%install
%make_install INSTALL_ROOT='%{buildroot}'

%find_lang qalculate-qt --with-qt


%check
desktop-file-validate '%{buildroot}%{_datadir}/applications/%{app_id}.desktop'
# Still required by guidelines for now
# (https://pagure.io/packaging-committee/issue/1053):
appstream-util validate-relax --nonet \
    '%{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml'
# Matches what gnome-software and others use:
appstreamcli validate --nonet \
    '%{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml'


%files -f qalculate-qt.lang
%license COPYING
%doc AUTHORS
%doc README

%{_bindir}/qalculate-qt
%{_mandir}/man1/qalculate-qt.1*

%{_datadir}/icons/hicolor/*/*/qalculate*

%{_datadir}/applications/%{app_id}.desktop
%{_metainfodir}/%{app_id}.metainfo.xml

%dir %{_datadir}/qalculate-qt
# See qalculate-qt.lang for the files in this directory:
%dir %{_datadir}/qalculate-qt/translations


%changelog
%autochangelog
