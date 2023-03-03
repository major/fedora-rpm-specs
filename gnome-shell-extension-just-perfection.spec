%global extension   just-perfection
%global uuid        %{extension}-desktop@%{extension}
# Define a commit here to switch to snapshot versioning.  Note that just adding
# a `#` to the beginning of this line is insufficient to disable snapshot
# versioning, as RPM allows you to define macros anywhere, even in comments.
#global commit      3f4d08d70aad022b231467b71dc495286a06b27b
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           gnome-shell-extension-%{extension}
Version:        24.0%{?commit:^1.%{shortcommit}}
Release:        %autorelease
Summary:        Extension to Customize GNOME Shell and Disable UI Elements
License:        GPL-3.0-only
URL:            https://gitlab.gnome.org/jrahmatzadeh/just-perfection
%if %{defined commit}
Source:         %{url}/-/archive/%{commit}/%{extension}-%{shortcommit}.tar.gz
%else
Source:         %{url}/-/archive/%{version}/%{extension}-%{version}.tar.gz
%endif

BuildArch:      noarch
BuildRequires:  gettext
Requires:       gnome-shell >= 3.36
Recommends:     gnome-extensions-app
Provides:       %{extension} = %{version}-%{release}


%description
%{summary}.


%prep
%autosetup -n %{extension}-%{?commit:%{commit}}%{!?commit:%{version}}

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
