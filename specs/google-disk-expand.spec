%global         dracut_modname  50google-disk-expand

%global         srcname     google-disk-expand
%global         forgeurl    https://github.com/GoogleCloudPlatform/guest-diskexpand
Version:        20241214.00
%global         tag         %{version}
%forgemeta

Name:           %{srcname}
Release:        %autorelease
Summary:        Expands root partition in Google Cloud instances

License:        Apache-2.0
URL:            %forgeurl
Source0:        %forgesource
Source1:        0001-Fedora-switched-to-the-btrfs-filesystem-since-Fedora.patch

BuildArch:      noarch

Requires: dracut
Requires: e2fsprogs
Requires: gdisk
Requires: grep
Requires: parted
Requires: util-linux
Requires: gawk
Requires: sed
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
BuildRequires:  systemd


%global _description %{expand:
Expands the root partition in Google Cloud instances.}

%description %{_description}


%prep
%forgeautosetup -p1


%install
install -m0755 -D -p src/expandroot-lib.sh %{buildroot}/usr/lib/dracut/modules.d/%{dracut_modname}/expandroot-lib.sh 
install -m0644 -D -p google-disk-expand.service %{buildroot}%{_unitdir}/google-disk-expand.service
install -m0755 -D -p src/usr/bin/google_disk_expand %{buildroot}/%{_bindir}/google_disk_expand


%post
%systemd_post google-disk-expand.service


%preun
%systemd_preun google-disk-expand.service


%postun
%systemd_postun_with_restart google-disk-expand.service


%files
%license LICENSE
%doc README.md
/usr/lib/dracut/modules.d/%{dracut_modname}/expandroot-lib.sh
%{_unitdir}/google-disk-expand.service
%{_bindir}/google_disk_expand


%changelog
%autochangelog
