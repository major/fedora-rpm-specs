Name:           multicat
Version:        2.4
Release:        %autorelease
Summary:        Simple and efficient multicast and transport stream manipulation

License:        GPL-2.0-or-later
URL:            https://www.videolan.org/projects/multicat.html
Source0:        https://download.videolan.org/multicat/%{version}/multicat-%{version}.tar.bz2

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  bitstream-devel >= 1.6


%description
Simple and efficient multicast and transport stream manipulation.


%prep
%setup -q
sed -i -e 's|-O3|%{optflags}|' Makefile


%build
%make_build


%install
%make_install PREFIX=%{_prefix}
chmod -x %{buildroot}%{_mandir}/man1/*


%files
%doc AUTHORS Changelog README
%license COPYING
%{_bindir}/aggregartp
%{_bindir}/ingests
%{_bindir}/lasts
%{_bindir}/multicat
%{_bindir}/multicat_validate
%{_bindir}/multilive
%{_bindir}/offsets
%{_bindir}/reordertp
%{_bindir}/smooths
%{_mandir}/man1/aggregartp.1.*
%{_mandir}/man1/ingests.1.*
%{_mandir}/man1/lasts.1.*
%{_mandir}/man1/multicat.1.*
%{_mandir}/man1/offsets.1.*
%{_mandir}/man1/reordertp.1.*


%changelog
%autochangelog
