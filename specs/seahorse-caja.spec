Summary:        PGP encryption and signing for caja
Name:           seahorse-caja
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Version:        1.18.5
Release:        7%{?dist}
URL:            https://github.com/darkshram/%{name}
Source0:        https://github.com/darkshram/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires: make
BuildRequires: mate-common
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(gcr-3)
BuildRequires: gnupg2
BuildRequires: gpgme-devel >= 1.0
BuildRequires: pkgconfig(libcaja-extension)
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(cryptui-0.0)
BuildRequires: pkgconfig(libnotify)

%if 0%{?rhel}
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
%endif

%description
Seahorse caja is an extension for caja which allows encryption
and decryption of OpenPGP files using GnuPG.


%prep
%setup -q

%build
%configure \
    --disable-silent-rules \
    --disable-gpg-check

make %{?_smp_mflags} V=1


%install
%{make_install}

find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
find %{buildroot} -type f -name "*.a" -exec rm -f {} ';'

desktop-file-validate %{buildroot}%{_datadir}/applications/mate-seahorse-pgp-encrypted.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/mate-seahorse-pgp-keys.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/mate-seahorse-pgp-signature.desktop

%find_lang %{name} --with-gnome --all-name


%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS
%{_bindir}/mate-seahorse-tool
%{_libdir}/caja/extensions-2.0/libcaja-seahorse.so
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/org.mate.seahorse.caja.*gschema.xml
%{_datadir}/seahorse-caja/
%{_mandir}/man1/mate-seahorse-tool.1*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.18.5-6
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jul 31 2022 Wolfgang Ulbrich <fedora@raveit.de> - 1.18.5-1
- update to 1.18.5

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 14 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1.18.1-2
- update rpm scriplets

* Sat Oct 14 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1.18.1-1
- initial package
