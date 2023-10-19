%global forgeurl https://github.com/graysky2/%{name}
%global tag v%{version}

%global shortname psd

Name: profile-sync-daemon
Version: 6.50
%forgemeta
Release: %autorelease
Summary: Symlinks and syncs browser profile dirs to RAM thus reducing HDD/SDD calls

BuildArch: noarch

License: MIT
URL: %{forgeurl}
Source0: %{forgesource}

BuildRequires: make
BuildRequires: rsync
BuildRequires: systemd-rpm-macros

Requires: rsync

%description
Profile-sync-daemon (psd) is a tiny pseudo-daemon designed to manage your
browser's profile in tmpfs and to periodically sync it back to your physical
disc (HDD/SSD). This is accomplished via a symlinking step and an innovative
use of rsync to maintain back-up and synchronization between the two. One of
the major design goals of psd is a completely transparent user experience.


%prep
%forgeautosetup -p1


%build
%make_build


%install
%make_install


%post
%{systemd_user_post %{shortname}.service}

%preun
%{systemd_user_preun %{shortname}.service}

%postun
%{systemd_user_postun_with_restart %{shortname}.service}


%files
%doc README.md
%license MIT LICENSE
%{_bindir}/%{name}
%{_bindir}/%{shortname}
%{_bindir}/%{shortname}-overlay-helper
%{_bindir}/%{shortname}-suspend-sync
%{_datadir}/%{shortname}/
%dir %{_datadir}/zsh/site-functions/
%{_datadir}/zsh/site-functions/_%{shortname}
%{_mandir}/man1/*.1*
%{_userunitdir}/*.{service,timer}


%changelog
%autochangelog
