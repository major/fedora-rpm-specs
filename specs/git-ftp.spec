Name:		git-ftp
Version:	1.6.0
Release:	%autorelease
Summary:	Git powered FTP client written as shell script
License:	GPL-3.0-only
URL:		https://github.com/git-ftp
Source0:	https://github.com/git-ftp/git-ftp/archive/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	pandoc
Requires:	curl
Requires:	git

%description
A shell script for pushing git tracked changed files to a
remote host by FTP

%prep
%autosetup -n %{name}-%{version}
# Avoid running mandb which creates CACHEDIR.TAG and is not allowed/needed in Fedora packages
sed -i '/mandb/d' Makefile

%build
# Nothing to build

%install
make install-all bindir=%{buildroot}%{_bindir} mandir=%{buildroot}%{_mandir}/man1

%check
# The testing environment expects to have Xampp installed
# not applicable in this case

%files
%license LICENSE
%doc README.md AUTHORS CHANGELOG.md
%{_bindir}/%{name}
%{_mandir}/man1/git-ftp.1*

%changelog
%autochangelog

