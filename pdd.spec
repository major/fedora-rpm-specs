Name:       pdd
Version:    1.6
Release:    %autorelease
Summary:    Tiny date, time diff calculator

License:    GPL-3.0-or-later
URL:        https://github.com/jarun/pdd
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:  noarch

BuildRequires:  make
Requires: python3-dateutil


%description
There are times you want to check how old you are (in years, months, days) or
how long you need to wait for the next flash sale... pdd (python3 date diff)
is a small cmdline utility to calculate date and time difference. If no
program arguments are specified it shows the current date, time and timezone.


%prep
%autosetup -p1 -n %{name}-%{version}
sed -i '1s/env //' pdd


%build
# Nothing to do


%install
%make_install PREFIX=%{_prefix}


%files
%doc CHANGELOG README.md
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*


%changelog
%autochangelog
