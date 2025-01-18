Name:           electrum
Version:        4.5.8
Release:        2%{?dist}
Summary:        A lightweight Bitcoin Client

License:        MIT
URL:            https://electrum.org/
Source0:        https://download.electrum.org/%{version}/Electrum-sourceonly-%{version}.tar.gz
Source1:        https://download.electrum.org/%{version}/Electrum-sourceonly-%{version}.tar.gz.asc
#Wed Feb 01 2017, exported the upstream gpg key using the command:
#gpg2 --export --export-options export-minimal 6694D8DE7BE8EE5631BED9502BD5824B7F9470E6 9EDAFF80E080659604F4A76B2EBB056FD847F8A7 0EEDCFD5CAFB459067349B23CA9EEEC43DF911DC > gpgkey-electrum.gpg
Source2:        gpgkey-%{name}.gpg
Source3:        %{name}.metainfo.xml
Source4:        %{name}.1

Patch0:         relax-protobuf-requirement.patch

BuildArch:      noarch
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  gettext

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  gnupg2
BuildRequires:  protobuf-compiler

Requires:       hicolor-icon-theme

# Unlucky rpm automatic dependency generation doesn't catch this dependency
Requires:       libsecp256k1

# Extra items are not tracked by runtime autodeps yet
Requires:       %{py3_dist cryptography}
Requires:       %{py3_dist pyqt5}

Recommends:     zbar
Recommends:     python3-trezor >= 0.13.0
Recommends:     python3-btchip >= 0.1.32

Conflicts:      python3-trezor < 0.11.2
Conflicts:      python3-btchip < 0.1.32

%description
Electrum is an easy to use Bitcoin client. It protects you from losing
coins in a backup mistake or computer failure, because your wallet can
be recovered from a secret phrase that you can write on paper or learn
by heart. There is no waiting time when you start the client, because
it does not download the Bitcoin block chain.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p0 -n Electrum-%{version}
rm -rf Electrum.egg-info
rm -rf packages

contrib/generate_payreqpb2.sh
contrib/build_locale.sh electrum/locale electrum/locale

%generate_buildrequires
%pyproject_buildrequires -x gui -x crypto

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}

install -Dpm 644 %{SOURCE3} %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
install -Dpm 644 %{SOURCE4} %{buildroot}%{_mandir}/man1/%{name}.1

# Remove shebang lines from .py files that aren't executable, and
# remove executability from .py files that don't have a shebang line:
# Source: dmalcolm.fedorapeople.org/python3.spec
find %{buildroot} -name \*.py \
  \( \( \! -perm /u+x,g+x,o+x -exec sed -e '/^#!/Q 0' -e 'Q 1' {} \; \
  -print -exec sed -i '1d' {} \; \) -o \( \
  -perm /u+x,g+x,o+x ! -exec grep -m 1 -q '^#!' {} \; \
  -exec chmod a-x {} \; \) \)

%check
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{name}.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{pyproject_files}
%doc AUTHORS README.md RELEASE-NOTES
%license LICENCE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/%{name}.metainfo.xml

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Oct 26 2024 Jonathan Schleifer <js@fedoraproject.org> - 4.5.8-1
- Updated to version 4.5.8.

* Tue Oct 22 2024 Jonathan Schleifer <js@fedoraproject.org> - 4.5.7-1
- Updated to version 4.5.7.

* Thu Oct 17 2024 Jonathan Schleifer <js@fedoraproject.org> - 4.5.6-1
- Updated to version 4.5.6.

* Tue Sep 03 2024 Jonathan Schleifer <js@fedoraproject.org> - 4.5.5-3
- Added patch to fix Electrum with python-trezor 0.13.9

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 24 2024 Jonathan Schleifer <js@fedoraproject.org> - 4.5.5-1
- Updated to version 4.5.5.

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 4.5.2-2
- Rebuilt for Python 3.13

* Sun Jan 28 2024 Jonathan Schleifer <js@fedoraproject.org> - 4.5.2-1
- Updated to version 4.5.2.
- Switched to sourceonly tarball.
- Regenerate pb2 files to lower protobuf requirement.

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Sep 24 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 4.3.4-3
- Drop x86 support (leaf package)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 01 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 4.3.4-1
- Updated to version 4.3.4.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 4.3.3-1
- Updated to version 4.3.3.

* Mon Nov 07 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 4.3.2-1
- Updated to version 4.3.2.

* Wed Aug 31 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 4.3.1-1
- Updated to version 4.3.1.
- Converted to 202x-era Python packaging guidelines.
- Switched metainfo to the latest XDG standard.
- Switched to gpgverify macros as required by packaging guidelines.
- Added desktop file check.
- Moved binary file with GPG keys to Fedora look-aside cache.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.2.1-3
- Rebuilt for Python 3.11

* Tue Apr 12 2022 Henrik Nordstrom <henrik@henriknordstrom.net> - 4.2.1-2
- Bump package requirements to match the code

* Sun Mar 27 2022 Jonathan Schleifer <js@fedoraproject.org> - 4.2.1-1
- Updated to 4.2.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Henrik Nordstrom <henrik@henriknordstrom.net> - 4.1.5-1
- Updated to version 4.1.5

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 23 2021 Henrik Nordstrom <henrik@henriknordstrom.net" - 4.1.4-2
- Allow building with current qdarkstyle and dnspython

* Wed Jun 23 2021 Henrik Nordstrom <henrik@henriknordstrom.net> - 4.1.4-0
- Updated to version 4.1.4

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.1.0-2
- Rebuilt for Python 3.10

* Thu Apr 01 2021 Timothy Redaelli <tredaelli@redhat.com> - 4.1.0-1
- Updated to version 4.1.0

* Sun Feb 21 2021 Timothy Redaelli <tredaelli@redhat.com> - 4.0.9-3
- Add python3-cryptography dependency (#1909753)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 04 2021 Timothy Redaelli <tredaelli@redhat.com> - 4.0.9-1
- Updated to version 4.0.9

* Thu Dec 17 2020 Timothy Redaelli <tredaelli@redhat.com> - 4.0.8-1
- Updated to version 4.0.8

* Thu Dec 10 2020 Timothy Redaelli <tredaelli@redhat.com> - 4.0.7-2
- Restore zbar as weak dependency since it's only used for QR scanner (#1766821)
- Fix rpmlint warnings and errors ("E: explicit-lib-dependency libsecp256k" is a false positive)

* Thu Dec 10 2020 Timothy Redaelli <tredaelli@redhat.com> - 4.0.7-1
- Updated to version 4.0.7

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 03 2020 Jonny Heggheim <hegjon@gmail.com> - 4.0.2-1
- Updated to version 4.0.2

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.3.4-7
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3.4-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3.4-4
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 21 2019 Jonny Heggheim <hegjon@gmail.com> - 3.3.4-2
- Allow usage of aiorpcx-0.12

* Wed Apr 03 2019 Jonny Heggheim <hegjon@gmail.com> - 3.3.4-1
- Updated to version 3.3.4

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 16 2019 Jonny Heggheim <hegjon@gmail.com> - 3.2.4-2
- Deactiated requires for typing and qdarkstyle

* Tue Jan 01 2019 Jonny Heggheim <hegjon@gmail.com> - 3.2.4-1
- Downgraded to version 3.2.4. Fedora lacks dependencies for 3.3.2

* Sun Dec 30 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.3.2-3
- Fix typo in pyqt5 requires

* Sun Dec 30 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.3.2-2
- Enable python dependency generator

* Sat Dec 29 2018 Jonny Heggheim <hegjon@gmail.com> - 3.3.2-1
- Updated to version 3.3.2

* Sun Sep 16 2018 Jonny Heggheim <hegjon@gmail.com> - 3.2.3-1
- Updated to version 3.2.3

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Jonny Heggheim <hegjon@gmail.com> - 3.2.2-1
- Updated to version 3.2.2

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.1.3-2
- Rebuilt for Python 3.7

* Fri Apr 20 2018 Jonny Heggheim <hegjon@gmail.com> - 3.1.3-1
- Updated to version 3.1.3

* Mon Mar 26 2018 Jonny Heggheim <hegjon@gmail.com> - 3.1.1-1
- Updated to version 3.1.1

* Mon Feb 19 2018 Jonny Heggheim <hegjon@gmail.com> - 3.0.6-1
- Updated to version 3.0.6

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Jonny Heggheim <hegjon@gmail.com> - 3.0.5-1
- Updated to version 3.0.5

* Sun Jan 07 2018 Jonny Heggheim <hegjon@gmail.com> - 3.0.4-1
- Updated to version 3.0.4

* Thu Dec 14 2017 Jonny Heggheim <hegjon@gmail.com> - 3.0.3-1
- Updated to version 3.0.3

* Sat Dec 09 2017 Jonny Heggheim <hegjon@gmail.com> - 3.0.2-1
- Updated to version 3.0.2

* Sat Aug 12 2017 Jonny Heggheim <hegjon@gmail.com> - 2.9.3-1
- Updated to version 2.9.3

* Thu Aug 10 2017 Jonny Heggheim <hegjon@gmail.com> - 2.9.2-1
- Updated to version 2.9.2

* Tue Aug 01 2017 Jonny Heggheim <hegjon@gmail.com> - 2.9.0-1
- Updated to version 2.9.0

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Jonny Heggheim <hegjon@gmail.com> - 2.8.3-1
- new version

* Mon Apr 10 2017 Jonny Heggheim <hegjon@gmail.com> - 2.8.2-1
- new version

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Jonny Heggheim <hegjon@gmail.com> - 2.7.18-2
- Verify the signature of the source tarball

* Tue Jan 24 2017 Jonny Heggheim <hegjon@gmail.com> - 2.7.18-1
- new version

* Thu Jan 12 2017 Jonny Heggheim <hegjon@gmail.com> - 2.7.17-1
- new version

* Mon Jan 09 2017 Jonny Heggheim <hegjon@gmail.com> - 2.7.13-2
- Added suggests python2-btchip

* Tue Jan 03 2017 Jonny Heggheim <hegjon@gmail.com> - 2.7.13-1
- new version

* Tue Nov 29 2016 Jonny Heggheim <hegjon@gmail.com> - 2.7.12-5
- Include appdata.xml file

* Fri Nov 18 2016 Jonny Heggheim <hegjon@gmail.com> - 2.7.12-4
- Updated license to MIT and BSD

* Tue Nov 15 2016 Jonny Heggheim <hegjon@gmail.com> - 2.7.12-3
- Added Provides: bundled(python-SocksiPy)

* Sun Nov 13 2016 Jonny Heggheim <hegjon@gmail.com> - 2.7.12-2
- Added weak dependency on zbar-pygtk

* Wed Nov 09 2016 Jonny Heggheim <hegjon@gmail.com> - 2.7.12-1
- new version

* Tue Apr 26 2016 gyger@fsfe.org - 2.6.4-2
- Fixed for python2 and new packaging requirements.

* Mon Apr 25 2016 gyger@fsfe.org - 2.6.4-1
- Upgrade to new Version.
- Relicenced to MIT.

* Sat Nov 7 2015 gyger@fsfe.org - 2.5.2-1
- Upgrade to new Version.

* Sat Jul 25 2015 gyger@fsfe.org - 2.3.3-1
- Upgrade to new Version.

* Wed Jan 28 2015 gyger@fsfe.org - 2.0.0-4
- Add Dependency on Pbkdf2

* Wed Jan 28 2015 gyger@fsfe.org - 2.0.0-1
- Packaging the Beta Version.

* Wed Jan 28 2015 gyger@fsfe.org - 1.9.8-1
- Initial Packaging for electrum on Fedora
