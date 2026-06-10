Name:           homebank
Version:        5.10.1
Release:        %{autorelease}
Summary:        Free easy personal accounting for all
License:        GPL-2.0-or-later
URL:            https://gethomebank.org/
Source:         https://gethomebank.org/public/sources/%{name}-%{version}.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  perl(XML::Parser)
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libofx)
BuildRequires:  pkgconfig(libsoup-3.0)

%description
HomeBank is the free software you have always wanted to manage your personal
accounts at home. The main concept is to be light, simple and very easy to use.
It brings you many features that allows you to analyze your finances in a
detailed way instantly and dynamically with powerful report tools based on
filtering and graphical charts.

%package doc
Summary: Documentation files for homebank
BuildArch: noarch
Requires: %{name} = %{version}-%{release}
%description doc
Documentation files for homebank


%prep
%autosetup -p1 -n %{name}-%{version}
chmod -x AUTHORS ChangeLog COPYING NEWS README doc/TODO src/*.*

%build
%configure
%make_build

%install
%make_install
rm -rf %{buildroot}%{_datadir}/mime-info/
rm -rf %{buildroot}%{_datadir}/application-registry/
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README
%{_bindir}/%{name}
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/images/
%{_datadir}/%{name}/icons/
%{_datadir}/%{name}/datas/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/mime/packages/%{name}.xml
%{_metainfodir}/%{name}.appdata.xml

%files doc
%license COPYING
%doc doc/TODO
%{_datadir}/%{name}/help/

%changelog
%autochangelog
