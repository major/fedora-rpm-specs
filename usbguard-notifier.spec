Name:           usbguard-notifier
Version:        0.1.0
Release:        1%{?dist}
Summary:        A tool for detecting usbguard policy and device presence changes

License:        GPLv2+
URL:            https://github.com/Cropi/%{name}
Source0:        https://github.com/Cropi/usbguard-notifier/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz

Requires: systemd

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: autoconf automake libtool make
BuildRequires: usbguard-devel
BuildRequires: librsvg2-devel
BuildRequires: libnotify-devel
BuildRequires: asciidoc
BuildRequires: catch1-devel
BuildRequires: systemd-rpm-macros

%description
USBGuard Notifier software framework detects usbguard policy modifications
as well as device presence changes and displays them as pop-up notifications.

%prep
%setup -q

%build
mkdir -p ./m4
autoreconf -i -f -v --no-recursive ./

export CXXFLAGS="$RPM_OPT_FLAGS"

%configure \
    --disable-silent-rules \
    --without-bundled-catch \
    --enable-debug-build

%set_build_flags
make %{?_smp_mflags}

%check
make check

%install
make install INSTALL='install -p' DESTDIR=%{buildroot}

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%postun
%systemd_user_postun_with_restart %{name}.service

%files
%doc README.md CHANGELOG.md
%license LICENSE
%{_bindir}/usbguard-notifier
%{_bindir}/usbguard-notifier-cli
%{_mandir}/man1/usbguard-notifier.1.gz
%{_mandir}/man1/usbguard-notifier-cli.1.gz
%{_userunitdir}/usbguard-notifier.service


%changelog
* Tue Dec 20 2022 Attila Lakatos <alakatos@redhat.com> - 0.1.0-1
- Rebase to 0.1.0

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Attila Lakatos <alakatos@redhat.com> - 0.0.6-5
- Merge notifications when inserting a usb device
  resolves: rhbz#1972505

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 15 2021 Radovan Sroka <rsroka@redhat.com> - 0.0.6-3
- Rebuild with the usbguard 1.0.0 - soname bump

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 29 2020 Attila Lakatos <alakatos@redhat.com> 0.0.6-1
- Rebase to 0.0.6

* Fri Feb 21 2020 Attila Lakatos <alakatos@redhat.com> 0.0.5-1
- Initial package
