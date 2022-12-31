%global srcname TITools
%global commit cc7dc08d831beaf6c4f865c3acd49a2be58df5a9
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20160515

Name:           titools
Version:        0.2^%{date}g%{shortcommit}
Release:        %autorelease
Summary:        Command-line programs for communicating with a TI calculator

License:        GPL-3.0-or-later
URL:            https://github.com/Jonimoose/%{srcname}
Source0:        %{url}/archive/%{commit}/%{srcname}-%{commit}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  tilibs-devel

%description
This package contains a collection of simple command-line tools for
communicating with TI graphing calculators.  These tools are based on
the excellent libticalcs2 library developed by the TiLP project (or
the equivalent libcalcprotocols library.)

%prep
%autosetup -n %{srcname}-%{commit}

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc README
%{_bindir}/ti*
%{_mandir}/man1/ti*.1*

%changelog
%autochangelog
