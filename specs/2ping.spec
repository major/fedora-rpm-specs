Name:           2ping
Version:        4.6.1
Release:        %autorelease
Summary:        Bi-directional ping utility

# Main code is MPL-2.0
# Documentation and some other files are CC-BY-SA-4.0
License:        MPL-2.0 AND CC-BY-SA-4.0
URL:            https://www.finnie.org/software/2ping
Source0:        https://www.finnie.org/software/%{name}/%{name}-%{version}.tar.gz
Source1:        2ping.service
Patch0:         2ping-add-build-system.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  systemd-rpm-macros
# For tests
BuildRequires:  python3-pytest

%description
2ping is a bi-directional ping utility. It uses 3-way pings (akin to TCP SYN,
SYN/ACK, ACK) and after-the-fact state comparison between a 2ping listener and
a 2ping client to determine which direction packet loss occurs.

%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l '*'

# Install systemd service
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_unitdir}/2ping.service

# Install man pages from doc/ directory in tarball
install -Dpm 0644 doc/2ping.1 %{buildroot}%{_mandir}/man1/2ping.1
# 2ping6 is a symlink or script pointing to same logic, man page is same
echo ".so 2ping.1" > %{buildroot}%{_mandir}/man1/2ping6.1

# Install bash completion
install -Dpm 0644 2ping.bash_completion %{buildroot}%{_datadir}/bash-completion/completions/2ping
ln -s 2ping %{buildroot}%{_datadir}/bash-completion/completions/2ping6

%check
%pyproject_check_import
%pytest

%post
%systemd_post 2ping.service

%preun
%systemd_preun 2ping.service

%postun
%systemd_postun 2ping.service

%files -f %{pyproject_files}
%doc ChangeLog.md README.md
%{_bindir}/2ping
%{_bindir}/2ping6
%{_mandir}/man1/2ping.1*
%{_mandir}/man1/2ping6.1*
%{_unitdir}/2ping.service
%{_datadir}/bash-completion/completions/2ping
%{_datadir}/bash-completion/completions/2ping6

%changelog
%autochangelog
