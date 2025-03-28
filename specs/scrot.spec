Name:           scrot
Version:        1.12
Release:        %autorelease
Summary:        Command line screen capture utility

License:        MIT
URL:            https://github.com/resurrecting-open-source-projects/%{name}
Source0:        %{URL}/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  pkgconfig(imlib2) pkgconfig(libbsd) pkgconfig(x11) pkgconfig(xext) pkgconfig(xcomposite) pkgconfig(xinerama)

%description
scrot is a simple command line screen capture utility.

%prep
%setup -q


%build
autoreconf -if

%configure
%make_build


%install
%make_install


%files
%doc AUTHORS ChangeLog README.md scrot.png FAQ.md CONTRIBUTING.md TODO.md
%license COPYING
%{_bindir}/*
%{_mandir}/man1/*



%changelog
%autochangelog
