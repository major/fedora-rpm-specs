%global prj_name time-services

Name:		qcom-time-services
Version:	0.1.2
Release:	%autorelease
Summary:	Qualcomm time daemon

License:	BSD-3-Clause
URL:		https://github.com/quic/time-services
Source0:	%{url}/archive/v%{version}/%{prj_name}-%{version}.tar.gz
Source1:	%{name}.service

# https://github.com/quic/time-services/commit/d726bee9b484b0d72150a1f34b2e9781bad78630
Patch0:		d726bee9b484b0d72150a1f34b2e9781bad78630.patch

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc
BuildRequires:	libtool
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(qmi-framework)
BuildRequires:	systemd

%description
%{name} daemon synchronizes time from the modem to the applications
processor and maintains time offsets across reboots, once set from any source.

%prep
%autosetup -p1 -n %{prj_name}-%{version}

%conf
autoreconf -fiv
%configure

%build
%make_build

%install
%make_install

mkdir -p %{buildroot}%{_unitdir}
install -p -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license LICENSE
%doc README.md
%{_bindir}/time_daemon
%{_unitdir}/%{name}.service

%changelog
%autochangelog
