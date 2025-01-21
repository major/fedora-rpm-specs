Name:           sddm-conf
Version:	0.3.0
Release:	2%{?dist}
License:	MIT
URL:		https://github.com/qtilities/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Summary:	Qt-based configuration editor for SDDM

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:	desktop-file-utils
BuildRequires:  libappstream-glib

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qtilitools)
BuildRequires:  perl

%description
Configuration editor for SDDM similar to sddm-config-editor, but written in C++.


%package l10n
BuildArch:      noarch
Summary:        Translations for sddm-conf
Requires:       sddm-conf
%description l10n
This package provides translations for the sddm-conf package.

%prep
%autosetup -p1

%build
%cmake -DPROJECT_QT_VERSION=6
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-qt


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/sddm_conf.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml ||:

%files
%license COPYING
%doc AUTHORS README.md
%{_bindir}/sddm-conf
%{_datadir}/applications/sddm_conf.desktop
%{_metainfodir}/sddm_conf.appdata.xml

%files l10n -f %{name}.lang
%license COPYING

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Jan 12 2025 Shawn W. Dunn <sfalken@cloverleaf-linux.org> - 0.3.0-1
- 0.3.0

* Tue Jul 30 2024 Steve Cossette <farchord@gmail.com> - 0.2.0-1
- 0.2.0
