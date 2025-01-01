Name:           zcfan
Version:        1.4.0
Release:        %autorelease
Summary:        Zero-configuration fan daemon for ThinkPads

License:        MIT
URL:            https://github.com/cdown/zcfan
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd-rpm-macros

ExclusiveArch:  x86_64

%description
zcfan is a zero-configuration fan control daemon for ThinkPads.

%prep
%autosetup

%build
%set_build_flags
%make_build

%install
%make_install DESTDIR=%{buildroot} prefix=%{_prefix}

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_unitdir}/%{name}.service

%changelog
%autochangelog
