Name:           trurl
Version:        0.2
Release:        1%{?dist}
Summary:        Command line tool for URL parsing and manipulation

License:        curl
URL:            https://github.com/curl/trurl
Source0:        %{url}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz

# Makefile: use 0644 for the manpage install
Patch0:         %{url}/commit/38ad284770efb9387ccbe9bb03c66f056486eeda.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(libcurl)

%description
A small command line tool that parses and manipulates URLs, designed to help
shell script authors everywhere.

%prep
%autosetup -n %{name}-%{name}-%{version}

%build
%make_build

%check
make test

%install
%make_install PREFIX=%{_prefix}

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Tue Apr 04 2023 Gustavo Costa <xfgusta@gmail.com> - 0.2-1
- Initial package
