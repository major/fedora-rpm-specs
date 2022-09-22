%global pkgname scscp
%global PKGNAME SCSCP
%global usrname gapd

Name:           gap-pkg-%{pkgname}
Version:        2.3.1
Release:        7%{?dist}
Summary:        Symbolic Computation Software Composability Protocol in GAP

License:        GPLv2+
URL:            https://gap-packages.github.io/scscp/
BuildArch:      noarch
Source0:        https://github.com/gap-packages/%{pkgname}/releases/download/v%{version}/%{PKGNAME}-%{version}.tar.gz
Source1:        %{usrname}.sh
Source2:        gap-scscp.service
Source3:        %{usrname}.logrotate
Source4:        %{usrname}.conf
Source5:        %{usrname}.h2m
Source6:        server.g

# Fix a typo in makedoc.g.
Patch0:         %{name}-makedoc.patch

BuildRequires:  gap-devel
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-pkg-io-doc
BuildRequires:  gap-pkg-openmath-doc
BuildRequires:  gap-pkg-smallgrp-doc
BuildRequires:  help2man
BuildRequires:  systemd

%{?systemd_requires}
Requires(pre):  shadow-utils
Requires:       gap-pkg-openmath
Requires:       logrotate

%description
This package implements the Symbolic Computation Software Composability
Protocol (SCSCP) for the GAP system in accordance with the SCSCP
specification, described at https://openmath.org/standard/scscp/, and
OpenMath dictionaries scscp1 and scscp2.

%package doc
Summary:        SCSCP documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-pkg-io-doc
Requires:       gap-pkg-openmath-doc
Requires:       gap-pkg-smallgrp-doc

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p0 -n %{PKGNAME}-%{version}

%build
# Link to main GAP documentation
ln -s %{_gap_dir}/doc ../../doc
mkdir ../pkg
ln -s ../%{PKGNAME}-%{version} ../pkg/%{PKGNAME}
ln -s %{_gap_dir}/pkg/io-* ../pkg
ln -s %{_gap_dir}/pkg/OpenMath-* ../pkg
ln -s %{_gap_dir}/pkg/SmallGrp-* ../pkg
gap -l "$PWD/..;%{_gap_dir}" makedoc.g
rm -fr ../../doc ../pkg

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{PKGNAME}-%{version} %{buildroot}%{_gap_dir}/pkg/%{PKGNAME}
rm -f %{buildroot}%{_gap_dir}/pkg/%{PKGNAME}/{COPYING,README.md,todo.txt}
rm -f %{buildroot}%{_gap_dir}/pkg/%{PKGNAME}/doc/*.{aux,bbl,blg,brf,idx,ilg,ind,log,out,pnr,tex}

# Replace upstream's launcher script with our own.
install -p -m 0755 %{SOURCE1} %{buildroot}%{_gap_dir}/pkg/%{PKGNAME}

# Make the daemon's home directory
mkdir -p %{buildroot}%{_sharedstatedir}/%{usrname}

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
mv %{buildroot}%{_gap_dir}/pkg/%{PKGNAME}/config.g \
   %{buildroot}%{_gap_dir}/pkg/%{PKGNAME}/configpar.g \
   %{buildroot}%{_sysconfdir}/scscp/gap

# Tell the package where to look for its configuration
sed -e 's,ReadPackage("scscp/\(config\.g\)"),Read("/etc/scscp/gap/\1"),' \
    -e 's,ReadPackage("scscp/\(configpar\.g\)"),Read("/etc/scscp/gap/\1"),' \
    -i %{buildroot}%{_gap_dir}/pkg/%{PKGNAME}/init.g
touch -r init.g %{buildroot}%{_gap_dir}/pkg/%{PKGNAME}/init.g

%check
# We only run the offline test as the others require network access and two
# servers to be setup and running.
mkdir ../pkg
ln -s ../%{PKGNAME}-%{version} ../pkg/%{PKGNAME}
pushd tst
gap -l "$PWD/../..;%{_gap_dir}" << EOF
LoadPackage("scscp");
GAP_EXIT_CODE(Test("offline.tst", rec(compareFunction := "uptowhitespace") ));
EOF
popd
rm -fr ../pkg

%pre
getent passwd %{usrname} >/dev/null || \
  useradd -c "GAP SCSCP server daemon" -d %{_sharedstatedir}/%{usrname} \
  -r -s /sbin/nologin -U %{usrname} || :

%preun
%systemd_preun gap-scscp.service

%post
%systemd_post gap-scscp.service

%posttrans
chown %{usrname}:%{usrname} %{_sharedstatedir}/%{usrname}

%files
%doc README.md todo.txt
%license COPYING
%{_gap_dir}/pkg/%{PKGNAME}/
%exclude %{_gap_dir}/pkg/%{PKGNAME}/demo/
%exclude %{_gap_dir}/pkg/%{PKGNAME}/doc/
%exclude %{_gap_dir}/pkg/%{PKGNAME}/example/
%{_mandir}/man8/%{usrname}.8*
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
%docdir %{_gap_dir}/pkg/%{PKGNAME}/demo/
%docdir %{_gap_dir}/pkg/%{PKGNAME}/doc/
%docdir %{_gap_dir}/pkg/%{PKGNAME}/example/
%{_gap_dir}/pkg/%{PKGNAME}/demo/
%{_gap_dir}/pkg/%{PKGNAME}/doc/
%{_gap_dir}/pkg/%{PKGNAME}/example/

%changelog
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
