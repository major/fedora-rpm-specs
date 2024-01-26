Name:		cwdaemon
Version:	0.10.2
Release:	19%{?dist}
Summary:	Morse daemon for the parallel or serial port

License:	GPLv2+
URL:		http://cwdaemon.sourceforge.net
Source0:	http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:	cwdaemon.sysconfig
Source2:	cwdaemon.service
Patch1:		cwdaemon-examples-fix.patch

BuildRequires:  gcc
BuildRequires:	perl-generators
BuildRequires:	unixcw-devel pkgconfig systemd
BuildRequires: make
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd


%description
Cwdaemon is a small daemon which uses the pc parallel or serial port
and a simple transistor switch to output morse code to a transmitter
from a text message sent to it via the udp internet protocol.

%prep
%setup -q
%patch1 -p1 -b .examples-fix

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

#remove the test.c we don't know why it is here, if we figure it out we will fix it
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/cwtest.*
#prevent this files to be packed twice
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/*_circuit.*
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/cwdaemon.png
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/cwsetup.sh
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/example.*
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/Makefile*
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/README
sed -i -e "s/schematics directory/documentation directory/g" %{_builddir}/%{name}-%{version}/README
mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
mkdir -p %{buildroot}%{_unitdir}
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/cwdaemon
#install -m 755 %%{SOURCE2} %%{buildroot}%%{_sysconfdir}/rc.d/init.d/cwdaemon
install -m 755 %{SOURCE2} %{buildroot}%{_unitdir}/cwdaemon.service


%post
%systemd_post cwdaemon.service

%preun
%systemd_preun cwdaemon.service

%postun
%systemd_postun_with_restart cwdaemon.service

%files
%doc AUTHORS ChangeLog COPYING README TODO cwdaemon.png doc/schematics/parallelport_circuit.ps doc/schematics/serialport_circuit.ps doc/schematics/parallelport_circuit.jpg doc/schematics/serialport_circuit.jpg cwsetup.sh examples/example.{c,pl,sh}
%{_sbindir}/%{name}
%{_unitdir}/cwdaemon.service
%config(noreplace) %{_sysconfdir}/sysconfig/cwdaemon
%{_mandir}/man8/%{name}.8.gz

%changelog
* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.10.2-12
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Lucian Langa <lucilanga@gnome.eu.org> - 0.10.2-1
- update to latest upstream

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 23 2015 Lucian Langa <lucilanga@gnome.eu.org> - 0.10.1-1
- sync with latest upstream

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 28 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.9.4-19
- Cleanup spec
- fix FTBFS

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 14 2012 Jon Ciesla <limburgher@gmail.com> - 0.9.4-14
- Migrate to systemd, BZ 771724.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep 03 2008 Lucian Langa <cooly@gnome.eu.org> - 0.9.4-9
- fix sysvinit script

* Wed Aug 20 2008 Lucian Langa <cooly@gnome.eu.org> - 0.9.4-8
- added postun scriptlet

* Sun Aug 10 2008 Lucian Langa <cooly@gnome.eu.org> - 0.9.4-7
- Add sysinit script and default configuration file
- Misc cleanups

* Mon Feb 18 2008 Robert 'Bob' Jensen <bob@bobjensen.com> 0.9.4-6
- fix manpage macro
- remove -devel package section and files including test.c

* Mon Feb 18 2008 Robert 'Bob' Jensen <bob@bobjensen.com> 0.9.4-5
- remove symlink from files section

* Mon Feb 18 2008 Robert 'Bob' Jensen <bob@bobjensen.com> 0.9.4-4
- Fix a few things from initial review
- Use sbin macro
- add simlink for second README location

* Sat Feb 16 2008 Robert 'Bob' Jensen <bob@bobjensen.com> 0.9.4-3
- Submit for review

* Mon Nov 19 2007 Sindre Pedersen Bjørdal <foolish@guezz.net> 0.9.4-2
- Update License tag
- Add missing doc files
- Don't package README twice
- Fix permissions for scripts

* Sun Apr 29 2007 Robert 'Bob' Jensen <bob@bobjensen.com> 0.9.4-0
- Initial spec file
