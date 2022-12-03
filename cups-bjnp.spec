Summary		: CUPS backend for the Canon BJNP network printers 
Name		: cups-bjnp
Version		: 2.0.3
Release		: 7%{?dist}
License		: GPLv2+
Source		: http://downloads.sourceforge.net/cups-bjnp/cups-bjnp-%{version}.tar.gz
Patch0          : cups-bjnp-configure-c99.patch
Group		: System Environment/Daemons
URL		: https://sourceforge.net/projects/cups-bjnp/

# cups is required so we can check that the backend directory is really correct
BuildRequires:	gcc
BuildRequires: 	cups
BuildRequires:	cups-devel
BuildRequires: make
Requires: cups

%global cups_backend_dir %{_exec_prefix}/lib/cups/backend
%description
This package contains a backend for CUPS for Canon printers using the 
proprietary BJNP network protocol.

%prep
%autosetup -p1

%build
%configure --prefix=%{_exec_prefix} --with-cupsbackenddir=%{cups_backend_dir} --disable-Werror
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p" install

%files
%{cups_backend_dir}/bjnp
%doc COPYING ChangeLog TODO NEWS README README.levels

%changelog
* Thu Dec  1 2022 Florian Weimer <fweimer@redhat.com> - 2.0.3-7
- Port configure script to C99

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 12 2020 Louis Lagendijk <llagendijk@users.sourceforge.net> - 2.0.3-1
- New upstream version 2.0.3 
- Fixes FTBS
- Increased status buffer for compatibility with new printers

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Louis Lagendijk <llagendijk@users.sourceforge.net> - 2.0.1-1
- New release changed to GPLv2+. Added BR gcc. No other changes

* Thu Jan 07 2016 Louis Lagendijk <llagendijk@users.sourceforge.net> - 2.0-4
- removed defattr
- corrected previous changelog entry that had incorrect version

* Thu Jan 07 2016 Louis Lagendijk <llagendijk@users.sourceforge.net> - 2.0-3
- Fixed specfile to use global instead of define

* Sat Sep 06 2014 Louis Lagendijk <llagendijk@users.sourceforge.net> - 1.9.2-1
- New upstream release 2.0
- Adds ink level reporting
- improved printer error handling

* Sat Apr 12 2014 Louis Lagendijk <llagendijk@users.sourceforge.net> - 1.9.2-1
- New upstream release 1.9.2
- Simplified error handling

* Sat Mar 29 2014 Louis Lagendijk <llagendijk@users.sourceforge.net> - 1.9.1-1
- New upstream release 1.9.1
- fixes out of paper reporting
- Fixes an incompatibility with xml status reports from newer printers

* Thu Mar 20 2014 Louis Lagendijk <llagendijk@users.sourceforge.net> - 1.9.0-1
- New upstream release 1.9.0
- Adds ink-level reporting
- improved out-of-paper handling 

* Wed Jan 22 2014  Louis Lagendijk <llagendijk@users.sourceforge.net> - 1.2.2-1
- new upstream release 1.2.2
- Fix crash with newer printers that send an xml-document for printer status
- Fix possible buffer overflow on response buffer

* Sat Feb 23 2013 Louis Lagendijk <llagendijk@users.sourceforge.net> - 1.2.1-1
  New upstream release. Fixes hang with MX270 and possibly other printers (bug
  introduced with version 1.1)

* Tue Nov 27 2012 Louis Lagendijk <llagendijk@users.sourceforge.net> - 1.2-1
- new upstream release 1.2, fixes compilation error on EL6

* Sat Sep 29 2012 Louis Lagendijk <llagendijk@users.sourceforge.net> - 1.1-1
- New upstream release 1.1
- Fixes "Failed to read side channel" error message
- Supports printing over IPv6
