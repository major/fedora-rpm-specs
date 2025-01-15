Name:           sasl-xoauth2
Version:        0.26
Release:        1%{?dist}
Summary:        The xoauth2 plugin for cyrus-sasl

License:        Apache-2.0
URL:            https://github.com/tarickb/%{name}
Source0:        https://github.com/tarickb/%{name}/archive/refs/tags/release-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libcurl-devel
%if 0%{?rhel} < 8
BuildRequires:  cmake3
%else
BuildRequires:  cmake
%endif
BuildRequires:  cyrus-sasl-devel
BuildRequires:  jsoncpp-devel
BuildRequires:  sqlite-devel
BuildRequires:  pandoc
BuildRequires:  argparse-manpage
BuildRequires:  python3-msal
# dependency on cyrus-sasl is not enforced by the resolver
# The package is a plugin for cyrus-sasl so it does not make any sense without
Requires:       cyrus-sasl-lib
Requires:       python3-msal

%description
sasl-xoauth2 is a SASL plugin that enables client-side use of OAuth 2.0.

Among other things it enables the use of Gmail or Outlook/Office 365 SMTP
relays from Postfix.

%prep
%setup -q -n %{name}-release-%{version}

%build
%if 0%{?rhel} < 8
%cmake3 -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir}
%cmake3_build
%else
%cmake -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir}
%cmake_build
%endif


%install
%if 0%{?rhel} < 8
%cmake3_install
%else
%cmake_install
%endif


%check
%ctest


%files
%doc README.md
%license COPYING
%dir %{_libdir}/sasl-xoauth2
%{_libdir}/sasl-xoauth2/test-config
%dir %{_libdir}/sasl2
%{_libdir}/sasl2/libsasl-xoauth2.so
%{_bindir}/sasl-xoauth2-tool
%config(noreplace) %{_sysconfdir}/sasl-xoauth2.conf
%{_mandir}/man5/%{name}.conf.5.gz
%{_mandir}/man1/%{name}-tool.1.gz

%changelog
* Mon Jan 13 2025 Jakub Jelen <jjelen@redhat.com> - 0.26-1
- New upstream release (#2337235)

* Fri Nov 01 2024 Jakub Jelen <jjelen@redhat.com> - 0.25-1
- New upstream release (#2323128)

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri May 17 2024 Jakub Jelen <jjelen@redhat.com> - 0.24-3
- Add explicit requires on python3-msal (#2280925)

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Aug 7 2023 Jakub Jelen <jjelen@redhat.com> - 0.24-1
- First package in Fedora (#2208250)
