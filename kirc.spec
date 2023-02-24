Name:           kirc
Version:        0.3.2
Release:        %autorelease
Summary:        Tiny IRC client written in POSIX C99

License:        MIT
URL:            https://github.com/mcpcpc/kirc
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%description
kirc ("KISS for IRC") is a tiny open-source Internet Relay Chat (IRC) client
designed with usability and cross-platform compatibility in mind.

%prep
%autosetup

%build
%set_build_flags
%make_build

%install
%make_install PREFIX="%{_prefix}"

%files
%license LICENSE
%doc README.md
%{_bindir}/kirc
%{_mandir}/man1/kirc.1*

%changelog
%autochangelog
