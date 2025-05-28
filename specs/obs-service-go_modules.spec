%define service go_modules
Name:           obs-service-%{service}
Version:        0.6.8
Release:        %autorelease
Summary:        An OBS source service: Download, verify and vendor Go module dependencies
License:        GPL-2.0-or-later
URL:            https://github.com/openSUSE/obs-service-%{service}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  go-md2man
Requires:       python3-libarchive-c
Requires:       golang-go >= 1.21
BuildArch:      noarch
BuildRequires:  python3

%description
An OBS Source Service that will download,
verify and vendor Go module dependency sources.

Using go.mod and go.sum present in a Go application,
the source service will call Go tools in sequence:

go mod download
go mod verify
go mod vendor

Then create a vendor.tar.gz populated with the contents of
vendor/

%prep
%autosetup

%build
# nothing to build

%install
mkdir -p %{buildroot}%{_prefix}/lib/obs/service
install -m 0755 go_modules %{buildroot}%{_prefix}/lib/obs/service
install -m 0644 go_modules.service %{buildroot}%{_prefix}/lib/obs/service

go-md2man -in README.md -out %{name}.1
install -D -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc README.md
%license LICENSE
%dir %{_prefix}/lib/obs
%dir %{_prefix}/lib/obs/service
%{_prefix}/lib/obs/service/%{service}
%{_prefix}/lib/obs/service/%{service}.service
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
