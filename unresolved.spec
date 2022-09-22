%global forgeurl0 %{url}

Name:           unresolved
Version:        0.1
Release:        %autorelease
Summary:        Remove systemd-resolved and have still working network

License:        GPLv3
URL:            https://github.com/pemensik/unresolved

%forgemeta
Source0:        %{forgesource0}

Requires:       systemd
BuildArch:      noarch

%description
Simple tool fixing DNS resolution on system, when systemd-resolved
is no longer welcome. Disable or unistall the service, but also fix
network resolution to working state.

%package force
Summary:        Keep systemd-resolved out of your system
Conflicts:      systemd-resolved
BuildArch:      noarch

%description force
Make sure systemd-resolved is not allowed back to the system.
Use unresolved purge to uninstall it first.

%prep
%forgeautosetup -p1

%build
:

%install
install -m 755 unresolved -pD %{buildroot}%{_sbindir}/unresolved

%files
%license LICENSE
%doc README.md
%{_sbindir}/unresolved

%files force
%license LICENSE

%changelog
%autochangelog
