Name:           ganyremote
Version:        8.1.1
Release:        %autorelease
Summary:        GTK frontend for anyRemote
License:        GPL-3.0-or-later
URL:            https://anyremote.sourceforge.net/
Source:         https://downloads.sourceforge.net/anyremote/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  libappstream-glib
BuildRequires:  make

Requires:       anyremote >= 6.7
Requires:       bluez-deprecated
Requires:       gdk-pixbuf2
Requires:       gtk3
Requires:       python3-bluez >= 0.9.1
Requires:       python3-gobject
Recommends:     libappindicator-gtk3

%description
gAnyRemote package is GTK GUI frontend for anyRemote 
(https://anyremote.sourceforge.net/) - remote control software for applications 
using Bluetooth or Wi-Fi.


%prep
%autosetup


%build
%configure


%install
%make_install

desktop-file-install \
  --add-category="System"                     \
  --delete-original                           \
  --dir=%{buildroot}%{_datadir}/applications/ \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

find %{buildroot}%{_docdir} -delete
%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%license COPYING
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}*.png


%changelog
%autochangelog
