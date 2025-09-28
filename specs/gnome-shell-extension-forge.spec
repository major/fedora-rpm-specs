%global extension       forge
%global uuid            %{extension}@jmmaranan.com
%global commit          26c98190079dd9364bbe7315bece29db3263676d
%global shortcommit     %{sub %{commit} 1 7}

Name:           gnome-shell-extension-%{extension}
Version:        88^1.%{shortcommit}
Release:        %autorelease
Summary:        Tiling and window manager for GNOME Shell
# main source code: GPL-3.0-or-later
# lib/css/index.js (installed as css.js): MIT
License:        GPL-3.0-or-later AND MIT
URL:            https://github.com/forge-ext/forge
BuildArch:      noarch

Source:         %{url}/archive/%{commit}/%{extension}-%{shortcommit}.tar.gz
# downstream-only
Patch:          0001-Adjust-makefile-for-Fedora.patch

BuildRequires:  make
BuildRequires:  gettext
Requires:       gnome-shell >= 45
Recommends:     gnome-extensions-app
Provides:       %{extension} = %{version}-%{release}


%description
Forge is a GNOME Shell extension that provides tiling/window management.


%prep
%autosetup -p 1 -n %{extension}-%{commit}

# relocate files we don't want to ship in the extension directory
mv lib/css/LICENSE LICENSE-css
mv lib/css/README.md README-css.md


%build
%make_build


%install
# install main extension files
%make_install

# install the schema file
install -D -p -m 0644 \
    schemas/org.gnome.shell.extensions.%{extension}.gschema.xml \
    %{buildroot}%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml

# install locale files
mv locale %{buildroot}%{_datadir}/locale
%find_lang %{extension}


%files -f %{extension}.lang
%license LICENSE LICENSE-css
%doc README.md
%{_datadir}/gnome-shell/extensions/%{uuid}
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml


%changelog
%autochangelog
