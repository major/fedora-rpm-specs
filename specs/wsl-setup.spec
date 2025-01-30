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


%check
grep "defaultName = %{default_name}" %{buildroot}%{_sysconfdir}/wsl-distribution.conf


%files
%config(noreplace) %{_sysconfdir}/wsl.conf
%{_prefix}/lib/wsl-distribution.conf
%{_sysconfdir}/wsl-distribution.conf
%{_libexecdir}/wsl/oobe.sh
%license LICENSE


%changelog
%autochangelog
