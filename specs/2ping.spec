Name:           2ping
Version:        4.5.1
Release:        %autorelease
Summary:        Bi-directional ping utility
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://www.finnie.org/software/2ping
Source0:        https://www.finnie.org/software/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  systemd

%description
2ping is a bi-directional ping utility. It uses 3-way pings (akin to TCP SYN,
SYN/ACK, ACK) and after-the-fact state comparison between a 2ping listener and
a 2ping client to determine which direction packet loss occurs.

%prep
%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l '*'
install -Dp -m 0644 2ping.service %{buildroot}/%{_unitdir}/2ping.service
install -Dp -m 0644 doc/2ping.1 %{buildroot}/%{_mandir}/man1/2ping.1
install -Dp -m 0644 doc/2ping.1 %{buildroot}/%{_mandir}/man1/2ping6.1

%check
%pyproject_check_import
%{__python3} -mpytest

%post
%systemd_post 2ping.service

%preun
%systemd_preun 2ping.service

%postun
%systemd_postun 2ping.service

%files -f %{pyproject_files}
%doc ChangeLog.md README.md
%{_bindir}/%{name}
%{_bindir}/%{name}6
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}6.1*
%{_unitdir}/2ping.service

%changelog
%autochangelog
