Name:           wmCalClock
Version:        1.26
Release:        %autorelease
Summary:        A Calendar clock with antialiased text

License:        GPL-2.0-or-later
URL:            https://www.dockapps.net/wmcalclock
Source0:        https://www.dockapps.net/download/wmcalclock-%{version}.tar.xz

Patch0:         1.26-fix-KnR-prototypes.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXpm-devel
BuildRequires:  git-core

%description
%{summary}

%prep
%autosetup -n wmcalclock-%{version} -S git

%build
%configure
%make_build
 
%install
%make_install

%files
%doc BUGS CHANGES HINTS README TODO
%license COPYING
%{_bindir}/wmCalClock
%{_mandir}/man1/wmCalClock.1*

%changelog
%autochangelog
