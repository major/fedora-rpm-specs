Name:              dropbear
Version:           2024.86
Release:           3%{?dist}
Summary:           Lightweight SSH server and client
License:           MIT
URL:               https://matt.ucc.asn.au/dropbear/dropbear.html
Source0:           https://matt.ucc.asn.au/%{name}/releases/%{name}-%{version}.tar.bz2
Source1:           https://matt.ucc.asn.au/%{name}/releases/%{name}-%{version}.tar.bz2.asc
Source2:           https://matt.ucc.asn.au/dropbear/releases/dropbear-key-2015.asc
Source4:           dropbear.service
Source5:           dropbear-keygen.service
BuildRequires:     gcc
# for gpg verification
BuildRequires:     gnupg2
BuildRequires:     libtomcrypt-devel
BuildRequires:     libtommath-devel
BuildRequires:     libxcrypt-devel
BuildRequires:     pam-devel
BuildRequires:     systemd
# For triggerun
Requires(post):    systemd-sysv
BuildRequires:     zlib-devel
BuildRequires:     make

%description
Dropbear is a relatively small SSH server and client. It's particularly useful
for "embedded"-type Linux (or other Unix) systems, such as wireless routers.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q

%build
%configure --enable-pam --disable-bundled-libtom

cat > localoptions.h <<EOT
#define SFTPSERVER_PATH "/usr/libexec/openssh/sftp-server"
EOT

%make_build

%install
%make_install
install -d %{buildroot}%{_sysconfdir}/%{name}
install -d %{buildroot}%{_unitdir}
install -pm644 %{S:4} %{buildroot}%{_unitdir}/%{name}.service
install -pm644 %{S:5} %{buildroot}%{_unitdir}/dropbear-keygen.service

%check
# Tests require local network and the running user to be able to login,
# not feasible with mock restrictions

%post
%systemd_post %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%preun
%systemd_preun %{name}.service

%triggerun -- dropbear < 0.55-2
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply dropbear
# to migrate them to systemd targets
systemd-sysv-convert --save dropbear >/dev/null 2>&1 ||:

# Run these because the SysV package being removed won't do them
chkconfig --del dropbear >/dev/null 2>&1 || :
systemctl try-restart dropbear.service >/dev/null 2>&1 || :

%files
%doc CHANGES README.md
%license LICENSE
%dir %{_sysconfdir}/dropbear
%{_unitdir}/dropbear*
%{_bindir}/dropbearkey
%{_bindir}/dropbearconvert
%{_bindir}/dbclient
%{_sbindir}/dropbear
%{_mandir}/man1/*.1*
%{_mandir}/man8/*.8*

%changelog
* Sat Feb 01 2025 Björn Esser <besser82@fedoraproject.org> - 2024.86-3
- Add explicit BR: libxcrypt-devel

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2024.86-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Oct 27 2024 Federico Pellegrin <fede@evolware.org> - 2024.86-1
- Update to 2024.86 (rhbz#2321034)

* Mon Sep 02 2024 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 2024.85-3
- Add GPG signature verification and misc changes

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2024.85-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Apr 29 2024 Federico Pellegrin <fede@evolware.org> - 2024.85-1
- Update to 2024.85 (rhbz#2277102)

* Fri Apr 05 2024 Federico Pellegrin <fede@evolware.org> - 2024.84-1
- Update to 2024.84 (rhbz#2273355)

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2022.83-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2022.83-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 29 2023 Federico Pellegrin <fede@evolware.org> - 2022.83-1
- Update to 2022.83

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.82-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.82-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Oct 30 2022 Christopher Meng <rpm@cicku.me> - 2022.82-1
- Update to 2022.82

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020.80-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020.80-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.80-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2020.80-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.80-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2020.80-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Isaque Galdino <igaldino@gmail.com> - 2020.80-1
- new version 2020.80

* Tue Jun 16 2020 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2020.79-1
- new version 2020.79

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.78-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.78-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 27 2019 Daniel Lara <danniel@fedoraproject.org> - 2019.78.1
- new version 2019.78

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.76-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 2018.76-4
- Rebuilt for libcrypt.so.2 (#1666033)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.76-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun May 06 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2018.76-2
- adjust sftp-server path

* Wed Feb 28 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2018.76-1
- new version 2018.76

* Mon Feb 19 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2017.75-7
- add gcc into buildrequires

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.75-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 2017.75-5
- Rebuilt for switch to libxcrypt

* Mon Oct 23 2017 Simone Caronni <negativo17@gmail.com> - 2017.75-4
- Rebuild for libtomcrypt update.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017.75-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017.75-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May 26 2017 Lennert Buytenhek <buytenh@wantstofly.org> - 2017.75-1
- Update to 2017.75 (#1452738)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.74-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 22 2016 Daniel Lara <danniel@fedoraproject.org> - 2016.74-1
- new version

* Fri Mar 18 2016 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2016.73-1
- new version

* Thu Mar 10 2016 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2016.72-1
- new version

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2015.71-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 04 2015 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2015.71-1
- Update to 2015.71 (#1251704)

* Sun Aug 09 2015 Christopher Meng <rpm@cicku.me> - 2015.68-1
- Update to 2015.68

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2015.67-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Feb 01 2015 Christopher Meng <rpm@cicku.me> - 2015.67-1
- Update to 2015.67

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2014.65-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 08 2014 Christopher Meng <rpm@cicku.me> - 2014.65-1
- Update to 2014.65

* Mon Jul 28 2014 Christopher Meng <rpm@cicku.me> - 2014.64-1
- Update to 2014.64

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2014.63-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 19 2014 Christopher Meng <rpm@cicku.me> - 2014.63-1
- Update to 2014.63

* Wed Dec 04 2013 Christopher Meng <rpm@cicku.me> - 2013.62-1
- Update to 2013.62

* Mon Oct 07 2013 Christopher Meng <rpm@cicku.me> - 2013.59-1
- New version.
- Adapt the version tag to match the actual one.
- Add systemd BR(BZ#992141).
- Unbundle libtom libraries(BZ#992141).
- Add AArch64 support(BZ#925278).
- SPEC cleanup.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.58-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 21 2013 Christopher Meng <rpm@cicku.me> - 0.58-4
- Cleanup systemd unit files.

* Thu May 16 2013 Christopher Meng <rpm@cicku.me> - 0.58-3
- Rebuilt.

* Thu May 16 2013 Christopher Meng <rpm@cicku.me> - 0.58-2
- Force PIE build for security issue.

* Wed May 08 2013 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.58-1
- new version

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.55-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.55-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 22 2012 Jon Ciesla <limburgher@gmail.com> - 0.55-3
- Enable pam support, fix unit file.

* Fri Apr 20 2012 Jon Ciesla <limburgher@gmail.com> - 0.55-2
- Migrate to systemd, BZ 770251.

* Sun Apr 01 2012 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.55-1
- new version 2012.55

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.52-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.52-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Apr 19 2010 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.52-1
- New version 0.5.2

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.50-3
- Autorebuild for GCC 4.3

* Thu Jan 10 2008 Lennert Buytenhek <buytenh@wantstofly.org> - 0.50-2
- Incorporate changes from Fedora package review:
  - Use full URL for Source0.
  - Ship dropbear.init with mode 0644 in the SRPM.
  - Convert CHANGES to utf-8 in %%setup, as the version shipped with
    dropbear 0.50 isn't utf-8 clean (it's in iso-8859-1.)
  - Add a reload entry to the init script, and don't enable the
    service by default.

* Mon Jan  7 2008 Lennert Buytenhek <buytenh@wantstofly.org> - 0.50-1
- Update to 0.50.
- Add init script.

* Fri Aug  3 2007 Lennert Buytenhek <buytenh@wantstofly.org> - 0.49-1
- Initial packaging.
