Name:           tqftpserv
Version:        1.2
Release:        %autorelease
Summary:        Trivial File Transfer Protocol server over AF_QIPCRTR

License:        BSD-3-Clause
URL:            https://github.com/linux-msm/tqftpserv
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(qrtr)
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros

%description
The tqftpserv software is an implementation of a TFTP (Trivial File Transfer
Protocol) server which runs on top of the AF_QIPCRTR (a.k.a QRTR) socket type.

The main purpose of tqftpserv is to serve files from the Linux file system to
other processors on the Qualcomm SoCs as requested.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license LICENSE
%{_bindir}/%{name}
%{_unitdir}/%{name}.service

%changelog
%autochangelog
