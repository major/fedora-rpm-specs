%global selinuxtype targeted
%global moduletype contrib
%global modulename authlogin_duo

# Disable by default as the tests require root and write to /etc/pam.d
%bcond_with tests

Name:           duo_unix
Version:        1.12.1
Release:        12%{?dist}
Summary:        Duo two-factor authentication for UNIX systems

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://www.duosecurity.com/
Source:         https://dl.duosecurity.com/%{name}-%{version}.tar.gz

Suggests:       %{name}-doc = %{version}-%{release}

BuildRequires:  bzip2
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  selinux-policy-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig

%if %{with tests}
BuildRequires:  python3
%endif

# The third-party Duo package provided by the vendor ships pam_duo in the
# duo_unix package; we recommend the subpackage here to avoid lockout issues
# for systems accidentally being upgraded from the vendor package to this one
# See RHBZ#2134160 for more details.
Recommends:     pam_duo = %{version}-%{release}

%description
Duo provides simple two-factor authentication as a service via:

    1.  Phone callback
    2.  SMS-delivered one-time passcode
    3.  Duo mobile app to generate one-time passcode
    4.  Duo mobile app for smartphone push authentication
    5.  Duo hardware token to generate one-time passcode

This package allows an admin (or ordinary user) to quickly add Duo
authentication to any UNIX login without setting up secondary user
accounts, directory synchronization, servers, or hardware.

%package        doc
Summary:        Documentation and license files for %{name}
BuildArch:      noarch

%description    doc
Documentation and license files for %{name}

%package -n     pam_duo
Summary:        A PAM module for duo authentication
Suggests:       %{name}-doc = %{version}-%{release}
Requires:       pam
Requires:       (%{name}-selinux if selinux-policy-%{selinuxtype})

%description -n pam_duo
A PAM module for duo authentication

%package        devel
Summary:        Development files and documentation for duo_unix
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pam_duo%{?_isa} = %{version}-%{release}

%description    devel
Development files and documentation for duo_unix

%package        selinux
Summary:        SELinux rules for %{name}
Requires:       selinux-policy-%{selinuxtype}
Requires(post): selinux-policy-%{selinuxtype}
Requires:       pam_duo%{?_isa} = %{version}-%{release}
%{?selinux_requires}

%description    selinux
%{summary}.

%prep
%setup -q

%build
%configure \
  --with-pam=%{_libdir}/security \
  --sysconfdir=%{_sysconfdir}/duo \
  --includedir=%{_includedir}/duo
%make_build
%make_build -C pam_duo semodule

%install
%make_install
%make_install -C pam_duo semodule-install

rm %{buildroot}%{_defaultdocdir}/%{name}/LICENSE
%if 0%{?rhel} || 0%{?fc35}
rm %{buildroot}%{_libdir}/security/pam_duo.la
%endif

%if %{with tests}
%check
make check
%endif

%files
%license LICENSE
%dir %{_sysconfdir}/duo
# This generates a non-readable rpmlint error, but this permission set is
# required for security. The Duo secrets are set in this file and allowing
# broader access risks exposing the secrets to other users on the system.
# sshd is the owner here since that user will run login_duo for SSH connections
# (the typical case) and this allows read access if capabilities aren't
# correctly set.
%attr(0600, sshd, root) %config(noreplace) %{_sysconfdir}/duo/login_duo.conf
%attr(0755, root, root) %caps(cap_dac_read_search=ep) %{_sbindir}/login_duo
# This will generate no-manual-page-for-binary but Duo does not provide any
# manual page. This is intended to be run when seeking support from Duo.
%{_sbindir}/duo_unix_support.sh
%{_mandir}/man8/login_duo.8*

%files -n pam_duo
%license LICENSE
%dir %{_sysconfdir}/duo
%dir %{_libdir}/security
%{_libdir}/security/pam_duo.so
# This generates a non-readable rpmlint error, but this permission set is
# required for security. The Duo secrets are set in this file and allowing
# broader access risks exposing the secrets to other users on the system.
%config(noreplace) %attr(0600, root, root) %{_sysconfdir}/duo/pam_duo.conf
%{_mandir}/man8/pam_duo.8*

%files doc
%license LICENSE
%doc README.md AUTHORS CHANGES
%doc %{_defaultdocdir}/%{name}

%files devel
%exclude %{_includedir}/duo/unity.h
%exclude %{_includedir}/duo/duo_private.h
%exclude %{_includedir}/duo/common_ini_test.h
%dir %{_includedir}/duo
%{_includedir}/duo/duo.h
%{_includedir}/duo/util.h
%{_includedir}/duo/shell.h
%{_libdir}/pkgconfig/libduo.pc
%{_mandir}/man3/duo.3*

%files selinux
%{_datadir}/selinux/packages/%{modulename}.pp.bz2

%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install %{_datadir}/selinux/packages/%{modulename}.pp.bz2

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall %{_datadir}/selinux/packages/%{modulename}.pp.bz2
fi

%posttrans selinux
%selinux_relabel_post -s %{selinuxtype}

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.12.1-11
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Oct 14 2022 Ben Boeckel <mathstuf@gmail.com> - 1.12.1-5
- Add selinux subpackage
- Also package up docs from the source

* Wed Oct 12 2022 Davide Cavalca <dcavalca@fedoraproject.org> - 1.12.1-4
- Add Recommends for pam_duo to the main package to prevent potential lockout
  issues (Fixes: RHBZ#2134160)

* Fri Oct 07 2022 Davide Cavalca <dcavalca@fedoraproject.org> - 1.12.1-3
- Fix EPEL build

* Fri Oct 07 2022 Davide Cavalca <dcavalca@fedoraproject.org> - 1.12.1-2
- Update openssl BR
- Fix duplicate license file
- Add check section and conditionally run tests

* Tue Sep 06 2022 Davide Cavalca <dcavalca@fedoraproject.org> - 1.12.1-1
- Update to 1.12.1
- Make doc subpackage noarch
- Drop unnecessary Requires
- Misc specfile fixes to comply with the latest guidelines
- Fix changelog formatting

* Thu May 05 2022 Joel Goguen <contact@jgoguen.ca> - 1.12.0-1
- Initial Fedora package
