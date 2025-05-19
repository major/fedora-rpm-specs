%global branch 1.28

Name:          mozo
Version:       %{branch}.0
Release:       %autorelease
Summary:       MATE Desktop menu editor
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:       LicenseRef-Callaway-LGPLv2+
URL:           http://mate-desktop.org
Source0:       http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: make
BuildRequires: mate-common 
BuildRequires: mate-menus-devel
BuildRequires: pkgconfig(pygobject-3.0)
BuildRequires: python3-devel

Requires:      mate-menus

BuildArch:     noarch

%description
MATE Desktop menu editor

%prep
%autosetup -p1

%build
%configure

make %{?_smp_mflags} V=1

%install
%{make_install}

desktop-file-install                                  \
        --dir=%{buildroot}%{_datadir}/applications    \
%{buildroot}%{_datadir}/applications/mozo.desktop

%find_lang %{name} --with-gnome --all-name


%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_bindir}/mozo
%{_datadir}/icons/hicolor/*x*/apps/mozo.png
%{_datadir}/mozo/
%{_datadir}/applications/mozo.desktop
%{_mandir}/man1/mozo.1.*
%dir %{python3_sitelib}/Mozo
%{python3_sitelib}/Mozo/*


%changelog
%autochangelog
