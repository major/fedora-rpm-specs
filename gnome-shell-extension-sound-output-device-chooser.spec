%global extension   sound-output-device-chooser
%global uuid        %{extension}@kgshank.net

Name:           gnome-shell-extension-%{extension}
Version:        43
Release:        %autorelease
Summary:        GNOME Shell extension for selecting sound devices
License:        GPL-3.0-or-later
BuildArch:      noarch
URL:            https://github.com/kgshank/gse-sound-output-device-chooser
Source:         %{url}/archive/%{version}/%{extension}-%{version}.tar.gz

BuildRequires:  gettext

Requires:       gnome-shell
Requires:       python3

Recommends:     gnome-extensions-app


%description
Shows a list of sound output and input devices (similar to gnome sound
settings) in the status menu below the volume slider.  Various active ports
like HDMI, speakers, etc. of the same device are also displayed for selection.


%prep
%autosetup -n gse-%{extension}-%{version} -p 1

# relocate things we don't want copied into the extensions directory
mv %{uuid}/locale .
mv %{uuid}/schemas .

# fix wrong-file-end-of-line-encoding rpmlint warning
sed -e 's/\r$//' -i CHANGELOG.md


%install
install -d -m 0755 %{buildroot}%{_datadir}/gnome-shell/extensions

# install main extension files
cp -r --preserve=mode,timestamps %{uuid} %{buildroot}%{_datadir}/gnome-shell/extensions

# install the schema file
install -D -p -m 0644 \
    schemas/org.gnome.shell.extensions.%{extension}.gschema.xml \
    %{buildroot}%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml

# install locale files
for po in locale/*/LC_MESSAGES/*.po; do
    install -d -m 0755 %{buildroot}%{_datadir}/$(dirname $po)
    msgfmt --output-file %{buildroot}%{_datadir}/${po%.po}.mo $po
done
%find_lang %{extension}


%files -f %{extension}.lang
%license LICENSE
%doc README.md CHANGELOG.md
%{_datadir}/gnome-shell/extensions/%{uuid}
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml


%changelog
%autochangelog
