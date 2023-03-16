%global extension   vertical-workspaces
%global uuid        %{extension}@G-dH.github.com
# Define a commit here to switch to snapshot versioning.  Note that just adding
# a `#` to the beginning of this line is insufficient to disable snapshot
# versioning, as RPM allows you to define macros anywhere, even in comments.
#global commit      0a0e31475ea3516cdf5a4e588ad6530383a01320
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           gnome-shell-extension-%{extension}
Version:        26%{?commit:^1.%{shortcommit}}
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

Requires:       gnome-shell >= 42
Recommends:     gnome-extensions-app
Provides:       %{extension} = %{version}-%{release}


%description
Customize your GNOME Shell UX to suit your workflow, whether you like
horizontally or vertically stacked workspaces.


%prep
%autosetup -n %{extension}-%{?commit:%{commit}}%{!?commit:%{version}}


%install
# install main extension files
install -d -m 0755 %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
cp -p *.js stylesheet.css metadata.json \
    %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/

# install the schema file
install -D -p -m 0644 \
    schemas/org.gnome.shell.extensions.%{extension}.gschema.xml \
    %{buildroot}%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml


%files
%license LICENSE
%doc CHANGELOG.md
%{_datadir}/gnome-shell/extensions/%{uuid}
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml


%changelog
%autochangelog
