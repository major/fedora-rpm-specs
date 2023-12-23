Name:    ksmtp
Version: 24.01.80
Release: 2%{?dist}
Summary: KDE SMTP libraries

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:     https://invent.kde.org/frameworks/%{name}/

Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

## upstream patches
# https://invent.kde.org/pim/ksmtp/-/merge_requests/18
Patch0:         move-translations.patch

## upstreamable patches

BuildRequires: extra-cmake-modules
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)

BuildRequires: cmake(Qt6Network)

BuildRequires: cmake(KPim6Mime)

BuildRequires: pkgconfig(libsasl2)

# runtime sasl plugins
Suggests: cyrus-sasl-gssapi%{?_isa}
Recommends: cyrus-sasl-md5%{?_isa}
Requires: cyrus-sasl-plain%{?_isa}

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6CoreAddons)
Requires:       cmake(KPim6Mime)
%description    devel
%{summary}.


%prep
%autosetup -n %{name}-%{version} -p1

# Remove together with move-translations.patch once released
find ./po -type f -name libksmtp5.po -execdir mv {} libksmtp6.po \;


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --all-name --with-html


%files -f %{name}.lang
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_kf6_libdir}/libKPim6SMTP.so.*

%files devel
%{_kf6_libdir}/libKPim6SMTP.so
%{_kf6_libdir}/cmake/KPim6SMTP/
%{_includedir}/KPim6/KSMTP/


%changelog
* Thu Dec 21 2023 Alessandro Astone <ales.astone@gmail.com> - 24.01.80-2
- Backport rename translation files

* Wed Dec 6 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-1
- 24.01.80
