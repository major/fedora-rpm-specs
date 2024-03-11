%global extension       just-perfection
%global uuid            %{extension}-desktop@%{extension}

Name:           gnome-shell-extension-%{extension}
Version:        28.0
Release:        %autorelease
Summary:        GNOME Shell extension to change behavior and disable UI elements
License:        GPL-3.0-only
URL:            https://gitlab.gnome.org/jrahmatzadeh/just-perfection
BuildArch:      noarch

Source:         %{url}/-/archive/%{version}/%{extension}-%{version}.tar.gz

BuildRequires:  gettext

Requires:       gnome-shell >= 45
Recommends:     gnome-extensions-app
Provides:       %{extension} = %{version}-%{release}


%description
%{summary}.


%prep
%autosetup -n %{extension}-%{version}

# we will be putting the schema xml file into a different location
mv src/schemas .

# fix spurious-executable-perm and script-without-shebang rpmlint warnings/errors
find -type f -print -exec chmod 644 {} \;


%install
# install main extension files
install -d -m 0755 %{buildroot}%{_datadir}/gnome-shell/extensions
cp -r --preserve=timestamps src %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}

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
%doc CHANGELOG.md
%{_datadir}/gnome-shell/extensions/%{uuid}
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml


%changelog
%autochangelog
