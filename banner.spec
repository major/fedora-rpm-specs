Name:           banner
Summary:        Prints a short string to the console in very large letters

Version:        1.3.6
Release:        %autorelease

License:        GPL-2.0-only
BuildRequires:  gcc
BuildRequires:  make
URL:            https://github.com/pronovic/banner
Source0:        https://github.com/pronovic/banner/releases/download/BANNER_V%{version}/banner-%{version}.tar.gz

%description
Classic-style banner program similar to the one found in Solaris or AIX.
The banner program prints a short string to the console in very large
letters.

%prep
%autosetup

%build
%configure
%make_build


%install
%make_install

%files
%license COPYING
%doc AUTHORS README ChangeLog
%{_bindir}/banner
%{_mandir}/man1/banner*

%changelog
%autochangelog
