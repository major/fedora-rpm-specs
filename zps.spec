Name:           zps
Version:        2.0.0
Release:        %autorelease
Summary:        A small utility for listing and cleaning up zombie processes

License:        GPL-3.0-only
URL:            https://github.com/orhun/zps
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  desktop-file-utils

%description
zps lists the running processes with theirs stats and indicates/reaps the 
zombie processes.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install
install -Dpm 0644 man/%{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1
desktop-file-install --dir=%{buildroot}/%{_datadir}/applications .application/%{name}.desktop

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/%{name}.desktop

%changelog
%autochangelog
