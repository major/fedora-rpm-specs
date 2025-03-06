Summary:      Platform independent library for scheme
Name:         slib
Version:      3c1
Release:      %autorelease
License:      LicenseRef-SLIB
BuildArch:    noarch
Source0:      http://groups.csail.mit.edu/mac/ftpdir/scm/slib-%{version}.zip
URL:          http://swissnet.ai.mit.edu/~jaffer/SLIB.html

%description
"SLIB" is a portable library for the programming language Scheme.
It provides a platform independent framework for using "packages" of
Scheme procedures and syntax.  As distributed, SLIB contains useful
packages for all Scheme implementations.  Its catalog can be
transparently extended to accommodate packages specific to a site,
implementation, user, or directory.

%prep
%autosetup -n %{name}
sed -r -i "s,/usr/(local/)?lib/slib,%{_datadir}/slib,g" *.init

%build

%install
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/slib
cp *.scm *.init *.xyz *.txt *.dat *.ps ${RPM_BUILD_ROOT}%{_datadir}/slib
mkdir -p ${RPM_BUILD_ROOT}%{_infodir}
install -m644 slib.info $RPM_BUILD_ROOT%{_infodir}

%files
%dir %{_datadir}/slib
%doc ANNOUNCE README COPYING FAQ ChangeLog
%{_datadir}/slib/*
%{_infodir}/slib.*

%changelog
%autochangelog
