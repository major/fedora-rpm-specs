%define service cargo_vendor
Name:           obs-service-%{service}
Summary:        An OBS source service: Download, verify and vendor Rust crates (libraries)
License:        GPLv2
URL:            https://github.com/openSUSE/obs-service-%{service}
Version:        0.4.3
Release:        %autorelease
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  python3
Requires:       gzip
Requires:       tar
Requires:       cargo
BuildArch:      noarch

%description
An OBS Source Service that will download,
verify and vendor Rust crates (libraries)

%prep
%autosetup

%build

%install
mkdir -p %{buildroot}%{_prefix}/lib/obs/service
mkdir -p %{buildroot}%{_prefix}/lib/obs/service
install -m 0755 %{service} %{buildroot}%{_prefix}/lib/obs/service
install -m 0644 %{service}.service %{buildroot}%{_prefix}/lib/obs/service

%files
%doc README.md
%license LICENSE
%dir %{_prefix}/lib/obs
%dir %{_prefix}/lib/obs/service
%{_prefix}/lib/obs/service/*

%changelog
%autorelease
