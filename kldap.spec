Name:    kldap
Version: 24.01.80
Release: 3%{?dist}
Summary: The KLDAP Library

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND MIT
URL:     https://api.kde.org/kdepim/kldap/html

Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# https://invent.kde.org/pim/kldap/-/merge_requests/17
Patch0:         move-translations.patch

BuildRequires:  cyrus-sasl-devel
BuildRequires:  openldap-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6Completion)
# Temporarily disabled: docs translations are broken and conflict with kf5-kldap:
# https://invent.kde.org/pim/kldap/-/merge_requests/17#note_837048
# BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Wallet)
BuildRequires:  cmake(KPim6Mbox)
BuildRequires:  cmake(KPim6Mime)

BuildRequires:  qt6-qtbase-devel

BuildRequires:  cmake(Qt6Keychain)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cyrus-sasl-devel%{?_isa}
Requires:       openldap-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version} -p1

# Remove together with move-translations.patch once released
find ./po -type f -name libkldap5.po -execdir mv {} libkldap6.po \;


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*ldap.*
%{_kf6_libdir}/libKPim6LdapCore.so.*
%{_kf6_libdir}/libKPim6LdapWidgets.so.*
%{_kf6_plugindir}/kio/ldap.so

%files devel
%{_includedir}/KPim6/KLDAPCore/
%{_includedir}/KPim6/KLDAPWidgets/
%{_kf6_libdir}/libKPim6LdapCore.so
%{_kf6_libdir}/libKPim6LdapWidgets.so
%{_kf6_libdir}/cmake/KPim6LdapCore/
%{_kf6_libdir}/cmake/KPim6LdapWidgets/


%changelog
* Thu Dec 21 2023 Alessandro Astone <ales.astone@gmail.com> - 24.01.80-3
- Disable docs until translations stop conflicting with kf5-kldap

* Thu Dec 21 2023 Alessandro Astone <ales.astone@gmail.com> - 24.01.80-2
- Backport rename translation files

* Fri Dec 8 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-1
- 24.01.80
