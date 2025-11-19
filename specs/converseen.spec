Name:		converseen
Version:	0.15.1.1
Release:	%autorelease
Summary:	A batch image conversion tool written in C++ with Qt5 and Magick++
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:	GPL-3.0-only
URL:		https://converseen.fasterland.net/
Source0:	https://downloads.sourceforge.net/converseen/%{name}-%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:	libappstream-glib
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	pkgconfig(MagickCore)
BuildRequires:	pkgconfig(MagickWand)
BuildRequires:	pkgconfig(Magick++)

%description
Converseen is a batch image conversion tool and resizer written in C++ with Qt5
and Magick++.  Converseen allows you to convert images in more than 100
different formats!

%prep
%autosetup

%build
%cmake -DUSE_QT6:BOOL=ON
%cmake_build

%install
%cmake_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/net.fasterland.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%files
%{_bindir}/%{name}
%{_datadir}/applications/net.fasterland.%{name}.desktop
%{_datadir}/converseen
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/kio/servicemenus/%{name}_import.desktop
%{_metainfodir}/%{name}.appdata.xml

%changelog
%autochangelog
