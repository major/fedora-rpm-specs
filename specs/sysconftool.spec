Summary:	Macros for aclocal to install configuration files
Summary(pl):	Makra dla aclocal do instalacji plików konfiguracyjnych
Name:		sysconftool
Version:	0.22
Release:	%autorelease
# Automatically converted from old format: GPLv3 with exceptions - review is highly recommended.
License:	LicenseRef-Callaway-GPLv3-with-exceptions
Source0:	https://downloads.sourceforge.net/project/courier/sysconftool/%{version}/%{name}-%{version}.tar.bz2
Source1:	https://downloads.sourceforge.net/project/courier/sysconftool/%{version}/%{name}-%{version}.tar.bz2.sig
Source2:	https://www.courier-mta.org/KEYS.bin
URL:		https://www.courier-mta.org/sysconftool/
BuildArch:	noarch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnupg2
BuildRequires:  make
BuildRequires:	perl-generators

%description
sysconftool is a development utility that helps to install application
configuration files. sysconftool allows an existing application to be
upgraded without losing the older version's configuration settings.

%description -l pl
sysconftool jest narzędziem, które pomaga instalować pliki
konfiguracyjne aplikacji. sysconftool pozwala na wymienienie
istniejących aplikacji na nowsze wersje bez straty starszych wersji
plików konfiguracyjnych.

%prep
%{gpgverify} --keyring='%{S:2}' --signature='%{S:1}' --data='%{S:0}'
%setup -q

%build
autoreconf -fiv
%configure
%make_build

%install
%make_install

# make the symlinks relative
ln -sf ../share/sysconftool/sysconftoolcheck %{buildroot}%{_bindir}/
ln -sf ../share/sysconftool/sysconftoolize.pl %{buildroot}%{_bindir}/sysconftoolize

%check
%make_build check

%files
%license COPYING
%doc AUTHORS ChangeLog *.html NEWS
%{_bindir}/sysconftoolcheck
%{_bindir}/sysconftoolize
%{_datadir}/sysconftool
%{_mandir}/man1/sysconftool.1*
%{_mandir}/man1/sysconftoolcheck.1*
%{_mandir}/man1/sysconftoolize.1*
%{_mandir}/man7/sysconftool.7*
%{_datadir}/aclocal/sysconftool.m4

%changelog
%autochangelog
