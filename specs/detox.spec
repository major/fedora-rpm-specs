Name:		detox
Version:	3.0.1
Release:	%autorelease
Summary:	Utility to replace problematic characters in file names

License:	BSD-3-Clause
URL:		https://github.com/dharple/detox
Source0:	https://github.com/dharple/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	flex-static
BuildRequires:	gcc
BuildRequires:	make

%description
Detox is a utility designed to clean up file names. It replaces difficult to
work with characters, such as spaces, with standard equivalents. It will also
clean up file names with UTF-8 or Latin-1 (or CP-1252) characters in them.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%check
%make_build check

%files
%config(noreplace) %{_sysconfdir}/%{name}rc
%{_bindir}/%{name}
%{_bindir}/inline-%{name}
%{_datadir}/%{name}
%doc README.md BUILD.md CHANGELOG.md THANKS.md
%license %{_docdir}/detox/LICENSE
%{_mandir}/man5/detox*
%{_mandir}/man1/inline-detox.1.gz
%{_mandir}/man1/detox*

%changelog
%autochangelog
