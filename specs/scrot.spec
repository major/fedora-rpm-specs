Name:           scrot
Version:        2.0.0
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
BuildRequires:  pkgconfig(imlib2)
BuildRequires:  pkgconfig(libbsd)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xrandr)

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
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/zsh/site-functions/_%{name}



%changelog
%autochangelog
