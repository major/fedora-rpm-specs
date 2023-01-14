%global pkgname scscp
%global upname  SCSCP
%global usrname gapd

Name:           gap-pkg-%{pkgname}
Version:        2.4.0
Release:        2%{?dist}
Summary:        Symbolic Computation Software Composability Protocol in GAP

License:        GPL-2.0-or-later
BuildArch:      noarch
ExclusiveArch:  aarch64 ppc64le s390x x86_64 noarch
URL:            https://gap-packages.github.io/scscp/
Source0:        https://github.com/gap-packages/scscp/releases/download/v%{version}/%{upname}-%{version}.tar.gz
Source1:        %{usrname}.sh
Source2:        gap-scscp.service
Source3:        %{usrname}.logrotate
Source4:        %{usrname}.conf
Source5:        %{usrname}.h2m
Source6:        server.g
Source7:        %{name}.sysusers

# Fix a typo in makedoc.g.
Patch0:         %{name}-makedoc.patch

BuildRequires:  gap-devel
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-pkg-io-doc
BuildRequires:  gap-pkg-openmath-doc
BuildRequires:  gap-pkg-smallgrp-doc
BuildRequires:  help2man
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros

%{?systemd_requires}
Requires:       gap-pkg-openmath
Requires:       logrotate

%description
This package implements the Symbolic Computation Software Composability
Protocol (SCSCP) for the GAP system in accordance with the SCSCP
specification, described at https://openmath.org/standard/scscp/, and
OpenMath dictionaries scscp1 and scscp2.

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
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p0 -n %{upname}-%{version}

%build
export LC_ALL=C.UTF-8

# Link to main GAP documentation
ln -s %{gap_libdir}/doc ../../doc
mkdir ../pkg
ln -s ../%{upname}-%{version} ../pkg/%{upname}
gap -l "$PWD/..;" makedoc.g
rm -fr ../../doc ../pkg

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{upname}/doc
cp -a *.g *.sh demo example lib par tracing tst \
   %{buildroot}%{gap_libdir}/pkg/%{upname}
%gap_copy_docs -n %{upname}
cp -a doc/img %{buildroot}%{gap_libdir}/pkg/%{upname}/doc

# Replace upstream's launcher script with our own.
install -p -m 0755 %{SOURCE1} %{buildroot}%{gap_libdir}/pkg/%{upname}

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
help2man -m "GAP SCSCP package" -S "GAP SCSCP (Fedora %{version}-%{release})" \
  -n "GAP Daemon" -I %{SOURCE5} -o %{buildroot}%{_mandir}/man8/%{usrname}.8 \
  -N -s 8 %{SOURCE1}

# Move the config files to their new home
mkdir -p %{buildroot}%{_sysconfdir}/scscp/gap
install -p -m 0644 %{SOURCE6} %{buildroot}%{_sysconfdir}/scscp/gap
mv %{buildroot}%{gap_libdir}/pkg/%{upname}/config.g \
   %{buildroot}%{gap_libdir}/pkg/%{upname}/configpar.g \
   %{buildroot}%{_sysconfdir}/scscp/gap
ln -s %{_sysconfdir}/scscp/gap/config.g %{buildroot}%{gap_libdir}/pkg/%{upname}
ln -s %{_sysconfdir}/scscp/gap/configpar.g %{buildroot}%{gap_libdir}/pkg/%{upname}

%check
export LC_ALL=C.UTF-8

# We only run the offline test as the others require network access and two
# servers to be setup and running.
mkdir ../pkg
ln -s ../%{upname}-%{version} ../pkg/%{upname}
cd tst
gap -l "$PWD/../..;" << EOF
LoadPackage("scscp");
GAP_EXIT_CODE(Test("offline.tst", rec(compareFunction := "uptowhitespace") ));
EOF
cd -
rm -fr ../pkg

%pre
%sysusers_create_package %{usrname} %{SOURCE7}

%preun
%systemd_preun gap-scscp.service

%post
%systemd_post gap-scscp.service

%files
%doc README.md todo.txt
%license COPYING
%{gap_libdir}/pkg/%{upname}/
%exclude %{gap_libdir}/pkg/%{upname}/demo/
%exclude %{gap_libdir}/pkg/%{upname}/doc/
%exclude %{gap_libdir}/pkg/%{upname}/example/
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
%docdir %{gap_libdir}/pkg/%{upname}/demo/
%docdir %{gap_libdir}/pkg/%{upname}/doc/
%docdir %{gap_libdir}/pkg/%{upname}/example/
%{gap_libdir}/pkg/%{upname}/demo/
%{gap_libdir}/pkg/%{upname}/doc/
%{gap_libdir}/pkg/%{upname}/example/

%changelog
* Thu Jan 12 2023 Jerry James <loganjerry@gmail.com> - 2.4.0-2
- Update for split GAP directories

* Sun Dec 11 2022 Jerry James <loganjerry@gmail.com> - 2.4.0-1
- Version 2.4.0

* Thu Nov 10 2022 Jerry James <loganjerry@gmail.com> - 2.3.1-8
- Clarify license of the doc subpackage

* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 2.3.1-8
- Update for gap 4.12.0
- Convert License tag to SPDX
- Use systemd-sysusers to create the daemon user

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Jerry James <loganjerry@gmail.com> - 2.3.1-1
- Version 2.3.1
- Depend on logrotate instead of owning its config directory

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Jerry James <loganjerry@gmail.com> - 2.3.0-1
- New upstream version
- Drop upstreamed -ref patch
- Add -makedoc patch to fix documentation building
- Fix creation of the daemon home dir

* Fri Mar  8 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 2.2.3-6
- Remove obsolete requirement for %%postun scriptlet

* Sat Feb  2 2019 Jerry James <loganjerry@gmail.com> - 2.2.3-5
- Rebuild for gap 4.10.0
- Add -ref patch
- Add -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 26 2017 Jerry James <loganjerry@gmail.com> - 2.2.3-1
- New upstream version

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr  1 2017 Jerry James <loganjerry@gmail.com> - 2.2.2-1
- New upstream version
- New URLs

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jul 20 2016 Jerry James <loganjerry@gmail.com> - 2.1.4-3
- Own the logrotate directory
- Do not delete the user in postun

* Thu May 26 2016 Jerry James <loganjerry@gmail.com> - 2.1.4-2
- Improved service integration

* Fri Apr 22 2016 Jerry James <loganjerry@gmail.com> - 2.1.4-1
- Initial RPM
