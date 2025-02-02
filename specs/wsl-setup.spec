%if 0%{?eln}
  %global default_name ELN
%else
  %global default_name Fedora
%endif


Name:           wsl-setup
Version:        1.0.0
Release:        %autorelease
Summary:        Windows Subsystem for Linux setup script and configuration
License:        MIT
URL:            https://src.fedoraproject.org/rpms/wsl-setup
BuildArch:      noarch

Source1:        LICENSE
Source2:        wsl.conf
Source3:        wsl-distribution.conf
Source4:        wsl-oobe.sh
Source5:        firstboot-override.conf
Source6:        wsl-setup-tmpfiles.conf
Source7:        wsl-setup-user-tmpfiles.conf

BuildRequires:  systemd-rpm-macros


%description
Provides WSL specific configuration files and first-time setup script.


%prep
%if 0%{?fedora}
sed -i 's,$NAME,Fedora,' %{SOURCE3}
%else
sed -i 's,$NAME,ELN,' %{SOURCE3}
%endif


%build


%install
install -pm 0644 %{SOURCE1} LICENSE
install -Dpm0644 -t %{buildroot}%{_sysconfdir}/ %{SOURCE2}
install -Dpm0644 -t %{buildroot}%{_prefix}/lib/ %{SOURCE3}
install -Dpm0755 -T %{SOURCE4} %{buildroot}%{_libexecdir}/wsl/oobe.sh
ln -s ..%{_prefix}/lib/wsl-distribution.conf %{buildroot}%{_sysconfdir}/wsl-distribution.conf

# WSL provides a socket for x11, but we need to ensure its linked to in /tmp.
# The official recommendation is to disable tmpfiles entirely, but it would be
# nice to work with it, instead.
# https://learn.microsoft.com/en-us/windows/wsl/build-custom-distro#systemd-recommendations
install -Dpm0644 %{SOURCE6} %{buildroot}%{_tmpfilesdir}/%{name}.conf

# WSL provides a Wayland and PulseAudio docket as well, which are expected to be in
# the user's runtime directory. This configuration sets up the links for each user.
install -Dpm0644 %{SOURCE7} %{buildroot}%{_user_tmpfilesdir}/%{name}.conf

# Currently systemd-firstboot hangs forever attempting to acquire the console; this is
# problematic since many other services wait for it to complete before starting, including
# things like the system D-Bus. Configure it to not run in WSL (a preset didn't seem to work)
# until we can see about adjusting either WSL or systemd to make it behave.
install -Dpm0644 %{SOURCE5} %{buildroot}%{_unitdir}/systemd-firstboot.service.d/override.conf

%check
grep "defaultName = %{default_name}" %{buildroot}%{_sysconfdir}/wsl-distribution.conf


%files
%config(noreplace) %{_sysconfdir}/wsl.conf
%{_prefix}/lib/wsl-distribution.conf
%{_sysconfdir}/wsl-distribution.conf
%{_libexecdir}/wsl/oobe.sh
%{_tmpfilesdir}/%{name}.conf
%{_user_tmpfilesdir}/%{name}.conf
%{_unitdir}/systemd-firstboot.service.d/override.conf
%license LICENSE


%changelog
%autochangelog
