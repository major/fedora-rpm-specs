Name:           dracut-sshd
Version:        0.7.1
Release:        %autorelease
Summary:        OpenSSH initramfs dracut integration

License:        GPL-3.0-or-later
URL:            https://github.com/gsauthof/%{name}
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       dracut
Requires:       dracut-network
Requires:       openssh-server


%description
dracut-sshd provides SSH access to initramfs early user space.

It allows for remote unlocking of a fully encrypted root filesystem and remote
access to the Dracut emergency shell (i.e. early userspace).


%prep
%autosetup -p1


%build
# nothing to do


%install
install -p -d       %{buildroot}%{_prefix}/lib/dracut/modules.d/46sshd
install -p -m644 -t %{buildroot}%{_prefix}/lib/dracut/modules.d/46sshd 46sshd/{motd,profile,sshd_config,sshd.service}
install -p -t       %{buildroot}%{_prefix}/lib/dracut/modules.d/46sshd 46sshd/module-setup.sh

mkdir -p %{buildroot}%{_sysconfdir}/dracut-sshd
touch    %{buildroot}%{_sysconfdir}/dracut-sshd/sshd_config


%files
%{_prefix}/lib/dracut/modules.d/46sshd/
%doc README.md example/

%dir                      %{_sysconfdir}/dracut-sshd
%ghost %config(noreplace) %{_sysconfdir}/dracut-sshd/sshd_config


%changelog
%autochangelog
