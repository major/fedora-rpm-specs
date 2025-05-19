Name:           trurl
Version:        0.16.1
Release:        %autorelease
Summary:        Command line tool for URL parsing and manipulation

License:        curl
URL:            https://curl.se/trurl
Source0:        https://github.com/curl/trurl/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  python3-devel

%description
A small command line tool that parses and manipulates URLs, designed to help
shell script authors everywhere.

%prep
%autosetup

%build
%make_build

%check
make test

%install
%make_install PREFIX=%{_prefix}

%files
%license COPYING
%doc README.md RELEASE-NOTES
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
