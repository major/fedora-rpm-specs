Name:           trurl
Version:        0.3
Release:        1%{?dist}
Summary:        Command line tool for URL parsing and manipulation

License:        curl
URL:            https://curl.se/trurl
Source0:        https://github.com/curl/trurl/archive/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  perl(Test::More)

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
%doc README.md RELEASE-NOTES
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Sat Apr 08 2023 Gustavo Costa <xfgusta@gmail.com> - 0.3-1
- Update to 0.3
- Add BR perl(Test::More)
- Drop patch
- Change URL
- Add RELEASE-NOTES to doc

* Tue Apr 04 2023 Gustavo Costa <xfgusta@gmail.com> - 0.2-1
- Initial package
