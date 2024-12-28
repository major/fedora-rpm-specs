Name:           homebank
Version:        5.8.6
Release:        %{autorelease}
Summary:        Free easy personal accounting for all  

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://homebank.free.fr
Source0:        http://homebank.free.fr/public/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  atk-devel cairo-devel desktop-file-utils gettext gtk3-devel
BuildRequires:  intltool libappstream-glib libofx-devel perl(XML::Parser)
BuildRequires:  libsoup3-devel
BuildRequires:  make

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
%autosetup
chmod -x NEWS
chmod -x ChangeLog
chmod -x README
chmod -x AUTHORS
chmod -x COPYING
chmod -x doc/TODO
chmod -x src/*.*

%build
%configure
%make_build

%install
make install DESTDIR=%{buildroot} INSTALL='install -p'
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install                                    \
        --delete-original                               \
        --dir %{buildroot}%{_datadir}/applications   \
        --mode 0644                                     \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/%{name}.appdata.xml

%ldconfig_scriptlets

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README
%license COPYING
%{_bindir}/%{name}
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/images
%{_datadir}/%{name}/icons
%{_datadir}/%{name}/datas
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/mime-info/%{name}.*
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/application-registry/%{name}.applications
%{_datadir}/metainfo/%{name}.appdata.xml

%files doc
%doc doc/TODO
%{_datadir}/%{name}/help

%changelog
%autochangelog
