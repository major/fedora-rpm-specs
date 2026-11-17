%global extension   blur-my-shell
%global uuid        %{extension}@aunetx

Name:           gnome-shell-extension-%{extension}
Version:        78
Release:        %autorelease
BuildArch:      noarch
Summary:        Adds a blur look to different parts of the GNOME Shell
License:        GPL-3.0-or-later
URL:            https://github.com/aunetx/blur-my-shell

Source:         %{url}/archive/v%{version}/%{extension}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  glib2-devel
Requires:       gnome-shell >= 46
Recommends:     gnome-extensions-app
Provides:       %{extension} = %{version}-%{release}


%description
Adds a blur look to different parts of the GNOME Shell, including the top
panel, dash and overview.


%prep
%autosetup -p 1 -n %{extension}-%{version}


%build
# build stylesheet
cat src/styles/panel.css \
    src/styles/dash.css \
    src/styles/popup/base.css \
    src/styles/popup/transparent.css \
    src/styles/popup/light.css \
    src/styles/popup/dark.css \
    src/styles/popup/menu-items.css \
    src/styles/popup/unblurred.css \
    src/styles/overview.css \
    src/styles/appfolders.css \
    src/styles/panel-light-text.css \
    > stylesheet.css

# build gresource bundle
glib-compile-resources \
    --sourcedir resources \
    --target resources.gresource \
    resources/%{extension}.gresource.xml

# build locale files
for p in po/*.po; do
    f=${p#po/}
    l=${f%.po}
    mkdir -p locale/$l/LC_MESSAGES
    msgfmt -o locale/$l/LC_MESSAGES/%{uuid}.mo $p
    touch -m --reference $p locale/$l/LC_MESSAGES/%{uuid}.mo
done


%install
# install main extension files
install -d -m 0755 %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
cp -r --preserve=timestamps \
    src/components src/conveniences src/dbus src/effects src/pipelines \
    src/preferences src/render src/settings src/styles \
    src/*.js stylesheet.css metadata.json \
    resources.gresource \
    %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}

# install the schema file
install -D -p -m 0644 \
    schemas/org.gnome.shell.extensions.%{extension}.gschema.xml \
    %{buildroot}%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml

# install locale files
cp -r --preserve=timestamps locale %{buildroot}%{_datadir}
%find_lang %{uuid}


%files -f %{uuid}.lang
%license LICENSE
%{_datadir}/gnome-shell/extensions/%{uuid}
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml


%changelog
%autochangelog
