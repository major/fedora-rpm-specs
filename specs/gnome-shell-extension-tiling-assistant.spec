%global pkgname Tiling-Assistant
%global lowername %{lower:%{pkgname}}
%global uuid %{lowername}@leleat-on-github

%global forgeurl https://github.com/ubuntu/%{pkgname}

Version:        56

%forgemeta

Name:           gnome-shell-extension-%{lowername}
Release:        %autorelease
Summary:        An extension which adds a Windows-like snap assist to GNOME
BuildArch:      noarch

License:        GPL-2.0-or-later
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gettext

Requires:       gnome-shell >= 48
Recommends:     gnome-extensions-app

%description
%{summary}.

%prep
%autosetup -n %{pkgname}-%{version}

%build
for FILE in translations/*.po; do
    LANG=$(basename "$FILE" .po)
    mkdir -p "locale/$LANG/LC_MESSAGES"
    msgfmt -c "$FILE" -o "locale/$LANG/LC_MESSAGES/%{uuid}.mo"
done

%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
mkdir -p %{buildroot}%{_datadir}/glib-2.0/schemas

install -Dp -m 0644 %{uuid}/{extension.js,metadata.json,stylesheet.css,prefs.js} \
    %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/

cp -rp %{uuid}/src %{uuid}/media \
    %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/

install -Dp -m 0644 %{uuid}/schemas/org.gnome.shell.extensions.%{lowername}.gschema.xml \
    %{buildroot}%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{lowername}.gschema.xml

mv locale %{buildroot}%{_datadir}/locale
%find_lang %{uuid}

%files -f %{uuid}.lang
%license LICENSE
%doc README.md CHANGELOG.md
%{_datadir}/gnome-shell/extensions/%{uuid}/
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{lowername}.gschema.xml

%changelog
%autochangelog

