Name: subscription-manager-rhsm-certificates
Version: 20220623
Release: 6%{?dist}
Summary: Certificates required to communicate with a Red Hat Unified Entitlement Platform
URL: https://www.candlepinproject.org/
%if 0%{?suse_version}
Group: Development/Libraries/Python
License: GPL-2.0
%else
License: GPL-2.0-only
%endif

# How to create the source tarball:
#
# git clone https://github.com/candlepin/subscription-manager-rhsm-certificates.git
# dnf install tito
# tito build --tag subscription-manager-rhsm-certificates-$VERSION-$RELEASE --tgz
Source0: %{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: make
BuildRequires: openssl

%description
This package contains certificates required for communicating with the REST interface
of a Red Hat Unified Entitlement Platform, used for the management of system entitlements
and to receive access to content.

%prep
%setup -q

%build
# Nothing to do for building

%install
%make_install \
    PREFIX=%{_prefix} \
    SYSCONFDIR=%{_sysconfdir}

%check
make check

%files
%license COPYING
%dir %{_sysconfdir}/rhsm
%dir %{_sysconfdir}/rhsm/ca
%{_sysconfdir}/rhsm/ca/*.pem

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20220623-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20220623-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20220623-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20220623-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20220623-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jun 23 2022 Jiri Hnidek <jhnidek@redhat.com> 20220623-1
- Fix issue with missing {?dist} in Release. (jhnidek@redhat.com)

* Wed Jun 15 2022 Jiri Hnidek <jhnidek@redhat.com> 20220425-1
- Use the same version and release as Fedora already use

* Wed Jun 08 2022 Jiri Hnidek <jhnidek@redhat.com> 20220608-1
- New package built with tito
- Using new version pattern for subscription-manager-rhsm-certificates

