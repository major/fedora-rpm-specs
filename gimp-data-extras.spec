%global gimpdatadir %(%___build_pre; %{_bindir}/gimptool --gimpdatadir || echo blah)

Summary: Extra files for GIMP
Name: gimp-data-extras
Version: 2.0.4
Release: %autorelease
License: GPL-3.0-or-later
URL: https://www.gimp.org/
Source0: https://download.gimp.org/pub/gimp/extras/gimp-data-extras-%{version}.tar.bz2
Source1: org.gimp.GIMP.data_extras.metainfo.xml
BuildArch: noarch
BuildRequires: gimp-devel-tools
BuildRequires: gimp-devel >= 2:2.0
BuildRequires: make
Requires: gimp >= 2:2.0

%description
Patterns, gradients, and other extra files for GIMP.

%prep
%setup -q

%build
%configure
make

%install
make DESTDIR=%{buildroot} install

install -d -m 0755 %{buildroot}%{_datadir}/metainfo
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/metainfo/

%files
%doc AUTHORS ChangeLog NEWS README
%license COPYING
%{gimpdatadir}/*
%{_datadir}/metainfo/*.metainfo.xml

%changelog
%autochangelog
