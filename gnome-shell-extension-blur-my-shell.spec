%global extension   blur-my-shell
%global uuid        %{extension}@aunetx
# Define a commit here to switch to snapshot versioning.  Note that just adding
# a `#` to the beginning of this line is insufficient to disable snapshot
# versioning, as RPM allows you to define macros anywhere, even in comments.
%global commit      28a669d1558659c714bfa1c1ac8661fde69ca9d8
%global shortcommit %{lua:print(macros.commit:sub(1,7))}

Name:           gnome-shell-extension-%{extension}
Version:        47%{?commit:^1.%{shortcommit}}
Release:        %autorelease
Summary:        Adds a blur look to different parts of the GNOME Shell
License:        GPL-3.0-or-later
URL:            https://github.com/aunetx/blur-my-shell
%if %{defined commit}
Source:         %{url}/archive/%{commit}/%{extension}-%{shortcommit}.tar.gz
%else
Source:         %{url}/archive/v%{version}/%{extension}-%{version}.tar.gz
%endif

BuildArch:      noarch
BuildRequires:  gettext
Requires:       gnome-shell >= 42
Requires:       hicolor-icon-theme
Recommends:     gnome-extensions-app
Provides:       %{extension} = %{version}-%{release}


%description
Adds a blur look to different parts of the GNOME Shell, including the top
panel, dash and overview.


%prep
%if %{defined commit}
%autosetup -n %{extension}-%{commit}
%else
%autosetup -n %{extension}-%{version}
%endif


%install
# install main extension files
install -d -m 0755 %{buildroot}%{_datadir}/gnome-shell/extensions
cp -p -r src %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
cp -p -r resources/ui %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/ui
cp -p -r resources/icons %{buildroot}%{_datadir}/icons
install -D -p -m 0644 metadata.json %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/metadata.json

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
%{_datadir}/icons/hicolor/scalable/actions/*.svg


%changelog
%autochangelog
