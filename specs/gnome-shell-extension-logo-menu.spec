%global extension       logo-menu
%global uuid            logomenu@aryan_k

Name:           gnome-shell-extension-%{extension}
Version:        24.4
Release:        %autorelease
Summary:        Quick access menu for the GNOME panel
BuildArch:      noarch

# main source is GPL-2.0-only
# selection.js is MIT
License:        GPL-2.0-only
URL:            https://github.com/Aryan20/Logomenu
Source:         %{url}/archive/v%{version}_010326/%{extension}-%{version}.tar.gz

BuildRequires:  gettext
Requires:       gnome-shell >= 46
Recommends:     gnome-extensions-app
Provides:       %{extension} = %{version}-%{release}


%description
This extension gives a simple menu along with the ability to get the icon of
your distro on top left part of the panel for a great look.  The Icon can be
customised through settings, it has both Linux and BSD logos.


%prep
%autosetup -C


%install
# install main extension files
install -d -m 0755 %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
cp -r --preserve=timestamps \
    *.js stylesheet.css metadata.json \
    PrefsLib Resources \
    %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}

# install the schema file
install -D -p -m 0644 \
    schemas/org.gnome.shell.extensions.%{extension}.gschema.xml \
    %{buildroot}%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml

# install locale files
pushd po
for po in *.po; do
    install -d -m 0755 %{buildroot}%{_datadir}/locale/${po%.po}/LC_MESSAGES
    msgfmt -o %{buildroot}%{_datadir}/locale/${po%.po}/LC_MESSAGES/%{extension}.mo $po
done
popd
%find_lang %{extension}


%files -f %{extension}.lang
%license LICENSE
%{_datadir}/gnome-shell/extensions/%{uuid}
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml


%changelog
%autochangelog
