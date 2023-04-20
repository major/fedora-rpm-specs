Name:           trurl
Version:        0.5
Release:        1%{?dist}
Summary:        Command line tool for URL parsing and manipulation

License:        curl
URL:            https://curl.se/trurl
Source0:        https://github.com/curl/trurl/archive/%{name}-%{version}/%{name}-%{version}.tar.gz

# version: bump to 0.5
Patch0:         https://github.com/curl/trurl/commit/90e0183fe55563012460f8ce46bf95364249b563.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  python3-devel

%description
A small command line tool that parses and manipulates URLs, designed to help
shell script authors everywhere.

%prep
%autosetup -n %{name}-%{name}-%{version}

%build
%make_build CFLAGS="%{build_cflags}"

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
* Tue Apr 18 2023 Gustavo Costa <xfgusta@gmail.com> - 0.5-1
- Update to 0.5 (rhbz#2187771)
- Use python to run tests
- Set CFLAGS
- Add patch to update the version

* Tue Apr 11 2023 Gustavo Costa <xfgusta@gmail.com> - 0.4-1
- Update to 0.4 (rhbz#2185147)

* Sat Apr 08 2023 Gustavo Costa <xfgusta@gmail.com> - 0.3-1
- Update to 0.3
- Add BR perl(Test::More)
- Drop patch
- Change URL
- Add RELEASE-NOTES to doc

* Tue Apr 04 2023 Gustavo Costa <xfgusta@gmail.com> - 0.2-1
- Initial package
