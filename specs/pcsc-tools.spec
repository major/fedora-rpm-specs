Name:           pcsc-tools
Version:        1.7.5
Release:        %autorelease
Summary:        Tools to be used with smart cards and PC/SC

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://pcsc-tools.apdu.fr/
Source0:        https://pcsc-tools.apdu.fr/%{name}-%{version}.tar.bz2
Source1:        https://pcsc-tools.apdu.fr/%{name}-%{version}.tar.bz2.asc
Source2:        https://pcsc-tools.apdu.fr/smartcard_list.txt
Source3:        LICENCE

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  pcsc-lite-devel >= 1.2.9
BuildRequires:  perl-generators
BuildRequires:  gettext
Requires:       pcsc-lite

%description
The pcsc-tools package contains some useful tools for a PC/SC user:
pcsc_scan regularly scans connected PC/SC smart card readers and
prints detected events, ATR_analysis analyzes smart card ATRs (Anwser
To Reset), and scriptor sends commands to a smart card.

%package gscriptor
Summary:        GUI tool to send command to a smart card
Requires:       %{name} = %{version}-%{release}

%description gscriptor
The pcsc-tools-gscriptor package contains graphical tool gscriptor which
can send commands to a smart card. It has GTK user interface.


%prep
%setup -q
[ -f LICENCE ] || cp -a %{SOURCE3} LICENCE
cp -a %{SOURCE2} smartcard_list.txt


%build
%configure
make %{?_smp_mflags} CPPFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_OPT_FLAGS"


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
desktop-file-install --mode=644 \
  --dir=$RPM_BUILD_ROOT%{_datadir}/applications gscriptor.desktop
# TODO: icon
%find_lang %{name}

%files -f %{name}.lang
%license LICENCE
%doc Changelog README
%{_bindir}/ATR_analysis
%{_bindir}/pcsc_scan
%{_bindir}/scriptor
%{_datadir}/pcsc/
%{_mandir}/man1/ATR_analysis.1*
%{_mandir}/man1/pcsc_scan.1*
%{_mandir}/man1/scriptor.1*

%files gscriptor
%license LICENCE
%{_bindir}/gscriptor
%{_mandir}/man1/gscriptor.1*
%{_datadir}/applications/*gscriptor.desktop


%changelog
%autochangelog
