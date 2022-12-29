Name:       pdd
Version:    1.7
Release:    %autorelease
Summary:    Tiny date, time diff calculator

License:    GPL-3.0-or-later
URL:        https://github.com/jarun/pdd
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:     32.patch

BuildArch:  noarch

BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-dateutil
Requires: python3-dateutil


%description
There are times you want to check how old you are (in years, months, days) or
how long you need to wait for the next flash sale... pdd (python3 date diff)
is a small cmdline utility to calculate date and time difference. If no
program arguments are specified it shows the current date, time and timezone.


%prep
%autosetup -p1 -n %{name}-%{version}
sed -i '1s/env //' pdd

%install
mkdir -p %{buildroot}%{_datadir}/bash-completion/compilations/
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions/
mkdir -p %{buildroot}%{_datadir}/fish/vendor_completions.d/
%make_install PREFIX=%{_prefix}


%files
%doc CHANGELOG README.md
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_datadir}/bash-completion/compilations/pdd
%{_datadir}/fish/vendor_completions.d/pdd.fish
%{_datadir}/zsh/site-functions/_pdd



%changelog
%autochangelog
