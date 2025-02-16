%global extension   no-overview
%global uuid        %{extension}@fthx

Name:           gnome-shell-extension-%{extension}
Version:        48
Release:        %autorelease
Summary:        GNOME Shell extension for no overview at start-up
License:        GPL-3.0-only
URL:            https://extensions.gnome.org/extension/4099/no-overview/
Source0:        https://github.com/fthx/no-overview/archive/refs/tags/v%{version}.zip#/no-overview-%{version}.zip

Source1:        https://raw.githubusercontent.com/fthx/no-overview/main/LICENSE#/%{extension}-LICENSE
Source2:        https://raw.githubusercontent.com/fthx/no-overview/main/README.md#/%{extension}-README.md
#Patch0:         %%{name}-HEAD.patch
BuildArch:      noarch
# rhbz#2001561 Delete to require gnome-shell-extension-common
#Requires:       gnome-shell-extension-common
Recommends:     gnome-extensions-app
BuildRequires:  git


%description
GNOME Shell extension for no overview at start-up. For GNOME Shell 40+.

%prep
%autosetup -n %{extension}-%{version} -S git

%build
# Nothing to build here

%install
install -d -m 0755 %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}

# install main extension files
cp -rp *.js metadata.json \
  %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}

%files
%doc README.md
%license LICENSE
%{_datadir}/gnome-shell/extensions/%{uuid}


%changelog
%autochangelog

