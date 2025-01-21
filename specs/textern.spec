%global debug_package   %nil

# this enforces us to create non-noarch package
%global native_dir      %_libdir/mozilla/native-messaging-hosts

%global __brp_python_bytecompile :

Name:           textern
Version:        0.8
Release:        6%{?dist}
Summary:        Firefox add-on for editing text in your favorite external editor

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/jlebon/textern

Source0:        %url/archive/v%{version}/%{name}-%{version}.tar.gz

Patch0:         textern-0.7-system-inotify-simple.patch

Requires:       mozilla-filesystem
Requires:       python3-inotify_simple

BuildRequires:  make
BuildRequires:  python3-devel

%description
Textern is a Firefox add-on that allows you to edit text areas in web pages
using an external editor.  It is similar in functionality to the popular
It's All Text! add-on, though makes use of the WebExtension API and is thus
fully compatible with multiprocessing and supported beyond Firefox 57.

This is not a self-standing Firefox add-on, it's only the "native" application
used by Add-on named "textern".  Please install the Add-on manually.


%prep
%autosetup -p1


%build


%install
make native-install \
    PREFIX=/usr \
    MOZILLA_NATIVE=%native_dir \
    DESTDIR=%buildroot


%files
%license LICENSE
%doc README.md
%dir %native_dir
%native_dir/textern.json
%dir %_libexecdir/textern
%_libexecdir/textern/textern.py


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.8-5
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 12 2023 Pavel Raiskup <praiskup@redhat.com> - 0.8-1
- new upstream release

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Pavel Raiskup <praiskup@redhat.com> - 0.7-1
- new upstream release

* Tue Feb 18 2020 Pavel Raiskup <praiskup@redhat.com> - 0-0.8.20180821git5339fb6
- compat with new inotify simple

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20180821git5339fb6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20180821git5339fb6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20180821git5339fb6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 22 2018 Pavel Raiskup <praiskup@redhat.com> - 0-0.4.20180821git5339fb6
- fix spec License to GPLv3+, per rhbz#1619528

* Tue Aug 21 2018 Pavel Raiskup <praiskup@redhat.com> - 0-0.3.20180821git5339fb6
- fix versioning and other problems spotted by Robert-André Mauchin
  and Lukáš Tyrychtr (rhbz#1619528)

* Tue Aug 21 2018 Pavel Raiskup <praiskup@redhat.com> - 0.git5339fb6-3
- actually drop noarch, but don't generate debuginfo

* Tue Aug 21 2018 Pavel Raiskup <praiskup@redhat.com> - 0.git5339fb6-2
- s/simple_inotify/inotify_simple/

* Tue Aug 21 2018 Pavel Raiskup <praiskup@redhat.com> - 0.git5339fb6-1
- initial rpm packaging
