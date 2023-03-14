Name:           dateutils
Version:        0.4.10
Release:        %autorelease
Summary:        Command-line date and time calculation, conversion, and comparison

License:        BSD-3-Clause
URL:            http://www.fresse.org/dateutils/
Source0:        https://github.com/hroptatyr/dateutils/releases/download/v%{version}/%{name}-%{version}.tar.xz

# https://github.com/hroptatyr/dateutils/issues/148
# issue related to tzdata-2022g and change to Singapore timezone
# This patch is from upstream. See:
Patch0:         841c635bf283e4b023bd98fbff9ebda1f340b024.patch

BuildRequires:  gcc
BuildRequires: make

# Tests won't pass woth older tzdata!
Requires: tzdata
Conflicts: tzdata < tzdata-2022g

%description
Tools which revolve around fiddling with dates and times on the command
line, with a strong focus on use cases that arise when dealing with large
amounts of financial data.


%prep
%autosetup -p1


%build
%configure --disable-silent-rules --without-old-links
# see note in configure script for why we're passing CFLAGS explicitly here
make %{?_smp_mflags} CFLAGS="$CFLAGS"


%install
%make_install

rm -f %{buildroot}%{_infodir}/dir
# this is duplicated otherwise
rm -f %{buildroot}%{_datadir}/doc/%{name}/LICENSE


%check
make check

%files
%license LICENSE
%doc README.md
%{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/%{name}*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.tzmcc
%{_datadir}/%{name}/locale


%changelog
%autochangelog
