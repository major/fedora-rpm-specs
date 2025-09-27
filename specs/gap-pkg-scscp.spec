%global gap_pkgname scscp
%global gap_upname  SCSCP
%global usrname     gapd
%global giturl      https://github.com/gap-packages/scscp

Name:           gap-pkg-%{gap_pkgname}
Version:        2.4.4
Release:        %autorelease
Summary:        Symbolic Computation Software Composability Protocol in GAP

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/scscp/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz
Source1:        %{usrname}.sh
Source2:        gap-scscp.service
Source3:        %{usrname}.logrotate
Source4:        %{usrname}.conf
Source5:        %{usrname}.h2m
Source6:        server.g
Source7:        %{name}.sysusers

# Fix a typo in makedoc.g.
Patch:          %{name}-makedoc.patch

BuildArch:      noarch
BuildSystem:    gap
BuildOption(build): --packagedirs ..
BuildOption(install): *.sh demo example lib par tracing tst
BuildOption(check): tst/testall.g

BuildRequires:  gap-devel
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-pkg-io-doc
BuildRequires:  gap-pkg-openmath-doc
BuildRequires:  gap-pkg-smallgrp-doc
BuildRequires:  help2man
BuildRequires:  systemd-rpm-macros

%{?systemd_requires}
Requires:       gap-pkg-io
Requires:       gap-pkg-openmath
Requires:       logrotate

%description
This package implements the Symbolic Computation Software Composability
Protocol (SCSCP) for the GAP system in accordance with the SCSCP
specification, described at https://openmath.org/standard/scscp/, and OpenMath
dictionaries scscp1 and scscp2.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        GPL-2.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        SCSCP documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-pkg-io-doc
Requires:       gap-pkg-openmath-doc
Requires:       gap-pkg-smallgrp-doc

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -p0 -n %{gap_upname}-%{version}

%install -a
cp -a doc/img %{buildroot}%{gap_libdir}/pkg/%{gap_upname}/doc

# Replace upstream's launcher script with our own.
install -p -m 0755 %{SOURCE1} %{buildroot}%{gap_libdir}/pkg/%{gap_upname}

# Make the daemon's home directory
mkdir -p %{buildroot}%{_sharedstatedir}/%{usrname}

# Install the sysusers file
mkdir -p %{buildroot}%{_sysusersdir}
cp -p %{SOURCE7} %{buildroot}%{_sysusersdir}/%{usrname}.conf

# Install the systemd unit
mkdir -p %{buildroot}%{_unitdir}
install -p -m 0644 -p %{SOURCE2} %{buildroot}%{_unitdir}

# Install the logrotate script
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -p -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

# Install the daemon config file
mkdir -p %{buildroot}%{_sysconfdir}
install -p -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}

# Install the man page
mkdir -p %{buildroot}%{_mandir}/man8
help2man -m 'GAP SCSCP package' -S 'GAP SCSCP (Fedora %{version}-%{release})' \
  -n 'GAP Daemon' -I %{SOURCE5} -o %{buildroot}%{_mandir}/man8/%{usrname}.8 \
  -N -s 8 %{SOURCE1}

# Move the config files to their new home
mkdir -p %{buildroot}%{_sysconfdir}/scscp/gap
install -p -m 0644 %{SOURCE6} %{buildroot}%{_sysconfdir}/scscp/gap
mv %{buildroot}%{gap_libdir}/pkg/%{gap_upname}/config.g \
   %{buildroot}%{gap_libdir}/pkg/%{gap_upname}/configpar.g \
   %{buildroot}%{_sysconfdir}/scscp/gap
ln -s %{_sysconfdir}/scscp/gap/config.g %{buildroot}%{gap_libdir}/pkg/%{gap_upname}
ln -s %{_sysconfdir}/scscp/gap/configpar.g %{buildroot}%{gap_libdir}/pkg/%{gap_upname}

%check
# We only run the offline test as the others require network access and two
# servers to be setup and running.
cd tst
gap --packagedirs ../.. << EOF
LoadPackage("scscp");
GAP_EXIT_CODE(Test("offline.tst", rec(compareFunction := "uptowhitespace") ));
EOF
cd -

%pre
%sysusers_create_package %{usrname} %{SOURCE7}

%preun
%systemd_preun gap-scscp.service

%post
%systemd_post gap-scscp.service

%files
%doc README.md todo.txt
%license COPYING
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/*.sh
%{gap_libdir}/pkg/%{gap_upname}/lib/
%{gap_libdir}/pkg/%{gap_upname}/par/
%{gap_libdir}/pkg/%{gap_upname}/tracing/
%{gap_libdir}/pkg/%{gap_upname}/tst/
%{_mandir}/man8/%{usrname}.8*
%{_sysusersdir}/%{usrname}.conf
%{_unitdir}/gap-scscp.service
%dir %{_sysconfdir}/scscp/
%dir %{_sysconfdir}/scscp/gap/
%config(noreplace) %{_sysconfdir}/scscp/gap/config.g
%config(noreplace) %{_sysconfdir}/scscp/gap/configpar.g
%config(noreplace) %{_sysconfdir}/scscp/gap/server.g
%config(noreplace) %{_sysconfdir}/%{usrname}.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%attr(755,%{usrname},%{usrname}) %{_sharedstatedir}/%{usrname}/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/demo/
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%docdir %{gap_libdir}/pkg/%{gap_upname}/example/
%{gap_libdir}/pkg/%{gap_upname}/demo/
%{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/example/

%changelog
%autochangelog
