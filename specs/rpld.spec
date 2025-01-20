Name:           rpld
Version:        1.8
Release:        0.45.beta1%{?dist}
Summary:        RPL/RIPL remote boot daemon
# No version specified.
License:        GPL-1.0-or-later
URL:            http://gimel.esc.cam.ac.uk/james/rpld/index.html
Source0:        http://gimel.esc.cam.ac.uk/james/rpld/src/rpld-1.8-beta-1.tar.gz
Source2:	%{name}.sysconfig
Source3:	%{name}.service
Patch0:         rpld_1.8beta1-6.diff.gz
Patch1:         rpld-1.8-makefile.patch
Patch2:         rpld-c99.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  byacc flex systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
Daemon to net-boot IBM style RPL boot ROMs (this is not the
same as the Novell IPX-style RPL protocol, despite the
name).

%post
%systemd_post rpld.service

%preun
%systemd_preun rpld.service

%postun
%systemd_postun rpld.service

%prep
%setup -q
%patch -P0 -p1

for I in debian/patches/* ;
do
  patch -p1 -i ${I}
done

%patch -P1 -p1
%patch -P2 -p1

%build
make OPT="-fPIE -pie $RPM_OPT_FLAGS" %{?_smp_mflags}
make OPT="-fPIE -pie $RPM_OPT_FLAGS" %{?_smp_mflags}
mv LICENCE LICENSE

%install
# mkdir -p $RPM_BUILD_ROOT/usr/{sbin,share/man/man{8,5}}
mkdir -p $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man{8,5}}
make install DESTDIR=$RPM_BUILD_ROOT BINMODE=755 MANMODE=644

find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

install -d $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
install -m 0644 %SOURCE2 $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}
install -d $RPM_BUILD_ROOT%{_unitdir}
install -m 0644 %SOURCE3 $RPM_BUILD_ROOT%{_unitdir}/%{name}.service

%files
%doc README LICENSE INSTALL rpld.conf.sample
%{_sbindir}/*
%{_mandir}/man[^3]/*
%{_sysconfdir}/sysconfig/%{name}
%{_unitdir}/%{name}.service

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-0.45.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-0.44.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 17 2024 Miroslav Suchý <msuchy@redhat.com> - 1.8-0.43.beta1
- convert license to SPDX

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-0.42.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-0.41.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 09 2024 Florian Weimer <fweimer@redhat.com> - 1.8-0.40.beta1
- Fix more C compatibility issues (#2186219)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-0.39.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Apr 12 2023 Arjun Shankar <arjun@redhat.com> - 1.8-0.38.beta1
- Port to C99 (#2186219)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-0.37.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-0.36.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-0.35.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-0.34.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-0.33.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-0.32.beta1
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-0.31.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-0.30.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-0.29.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-0.28.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-0.27.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-0.26.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-0.25.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-0.24.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-0.23.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-0.22.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-0.21.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-0.20.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-0.19.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Sep 01 2013 i@stingr.net - 1.8-0.18.beta1
- bz#850299
- get rid of compatibility ifs

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-0.17.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-0.16.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-0.15.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 21 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.8-0.14.beta1
- Fix unitdir for FTBFS

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-0.13.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 28 2011 Paul P. Komkoff Jr <i@stingr.net> - 1.8-0.12.beta1
- fixing the systemd/initscript

* Mon Oct 31 2011 Paul P. Komkoff Jr <i@stingr.net> - 1.8-0.11.beta1
- fixes for specfile and init script

* Tue Jul 5 2011 Paul P. Komkoff Jr <i@stingr.net> - 1.8-0.10.beta1
- add pre/postinstall stuff

* Thu Jun 2 2011 Paul P. Komkoff Jr <i@stingr.net> - 1.8-0.9.beta1
- add systemd service file

* Thu Jun 2 2011 Paul P. Komkoff Jr <i@stingr.net> - 1.8-0.8.beta1
- add initscript

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-0.7.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-0.6.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-0.5.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.8-0.4.beta1
- fix license tag

* Sun Feb 24 2008 Paul P Komkoff Jr <i@stingr.net> - 1.8-0.3.beta1
- make rpld a PIE

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.8-0.2.beta1
- Autorebuild for GCC 4.3

* Sat Oct 14 2006 Paul P Komkoff Jr <i@stingr.net> - 1.8-0.1.beta1
- Preparing for submission to fedora extras
