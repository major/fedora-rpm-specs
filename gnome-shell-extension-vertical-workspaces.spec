%global extension   vertical-workspaces
%global uuid        %{extension}@G-dH.github.com
# Define a commit here to switch to snapshot versioning.  Note that just adding
# a `#` to the beginning of this line is insufficient to disable snapshot
# versioning, as RPM allows you to define macros anywhere, even in comments.
%global commit      b9220e967d830e19866d15eff70adb5091e2a39c
%global shortcommit %{lua:print(macros.commit:sub(1,7))}

Name:           gnome-shell-extension-%{extension}
Version:        37.5%{?commit:^2.%{shortcommit}}
Release:        %autorelease
Summary:        Customize your GNOME Shell UX to suit your workflow
License:        GPL-3.0-only
URL:            https://github.com/G-dH/vertical-workspaces
BuildArch:      noarch

%if %{defined commit}
Source:         %{url}/archive/%{commit}/%{extension}-%{shortcommit}.tar.gz
%else
Source:         %{url}/archive/v%{version}/%{extension}-%{version}.tar.gz
%endif

BuildRequires:  gettext
Requires:       (gnome-shell >= 45~ with gnome-shell < 46~)
Recommends:     gnome-extensions-app
Provides:       %{extension} = %{version}-%{release}


%description
Customize your GNOME Shell UX to suit your workflow, whether you like
horizontally or vertically stacked workspaces.


%prep
%autosetup -n %{extension}-%[ %{defined commit} ? "%{commit}" : "%{version}" ]


%install
# install main extension files
install -d -m 0755 %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
cp -rp lib *.js stylesheet.css metadata.json \
    %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/

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
