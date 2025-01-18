%global compdir %(pkg-config --variable=completionsdir bash-completion)
%global __requires_exclude .*Acme::Cow.*

%global cowsdir %{_datadir}/%{name}/cows
%global sitecowsdir %{_datadir}/%{name}/site-cows

Name:           cowsay
Version:        3.8.4
Release:        2%{?dist}
Summary:        Configurable speaking/thinking cow
License:        GPL-2.0-or-later
URL:            https://github.com/cowsay-org/cowsay
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        cowsay.bashcomp
Source2:        animalsay

BuildArch:      noarch
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  perl-generators
Requires:       perl-Encode
# introduced /usr/share/bash-completion/...
Requires:       filesystem >= 3.6-1

%description
cowsay is a configurable talking cow, written in Perl.  It operates
much as the figlet program does, and it is written in the same spirit
of silliness.
It generates ASCII pictures of a cow with a message. It can also generate
pictures of other animals.

%prep
%setup -q

%build
echo No need to build anything

%install
# At least for cowsay-3.7.0, replace upstream's "make install" by our
# own installation code.
install -d -m 0755         $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 bin/%{name} $RPM_BUILD_ROOT%{_bindir}
ln -s              %{name} $RPM_BUILD_ROOT%{_bindir}/cowthink

install -d -m 0755           $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m 0644 man/man1/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1
ln -s              %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/cowthink.1

install -d -m 0755              $RPM_BUILD_ROOT%{cowsdir}
install -p -m 0644 share/cowsay/cows/* $RPM_BUILD_ROOT%{cowsdir}

install -d -m 0755              $RPM_BUILD_ROOT%{sitecowsdir}

install -d -m 0755              $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/cowpath.d

# Install actions specific to the Fedora package

# License issue
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/cows/daemon.cow
# animalsay
install -p -m 0755 %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}
# bash completion file
install -d -m 0755            $RPM_BUILD_ROOT%{compdir}
install -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{compdir}/%{name}

%files
%doc CHANGELOG.md LICENSE.txt README README.md
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/cowpath.d
%{_bindir}/animalsay
%{_bindir}/cowsay
%{_bindir}/cowthink
%{_mandir}/man1/cowsay.1*
%{_mandir}/man1/cowthink.1*
%dir %{_datadir}/%{name}
%{cowsdir}
%exclude %{cowsdir}/bong.cow
%exclude %{cowsdir}/head-in.cow
%exclude %{cowsdir}/mutilated.cow
%dir %{sitecowsdir}
%{compdir}/%{name}

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Dec 02 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.8.4-1
- 3.8.4

* Thu Aug 22 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.8.3-1
- 3.8.3

* Tue Aug 20 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.8.2-1
- 3.8.2

* Thu Aug  8 2024 Hans Ulrich Niedermann <hun@n-dimensional.de> - 3.8.1-2
- Install CHANGELOG.md doc file

* Thu Aug 08 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.8.1-1
- 3.8.1

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Mar 18 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.7.0-13
- BR fix for bash-completion

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Perry Myers <pmyers@redhat.com> - 3.7.0-10
- Remove some additional tasteless content missed before

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Feb 28 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.7.0-8
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 22 2022 Hans Ulrich Niedermann <hun@n-dimensional.de> - 3.7.0-6
- ship /etc/cowsay/cowpath.d directory

* Mon Aug 15 2022 Hans Ulrich Niedermann <hun@n-dimensional.de> - 3.7.0-5
- Ensure /usr/bin/animalsay file mode is 0755
- Use "install" command for installing dirs and files
- Change name of bash completion file to just "cowsay"
- Define and use macro for cows directory
- Install empty site-cows directory for site specific cows
- Fix bash completion to look in actual cows/ directory

* Wed Aug 10 2022 Hans Ulrich Niedermann <hun@n-dimensional.de> - 3.7.0-4
- Stop packaging cows in the unsupported *.pm format

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 13 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.7.0-1
- 3.7.0i, new upstream.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.04-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 19 2020 Filipe Brandenburger <filbranden@gmail.com> - 3.04-16
- Add fox cow.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.04-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.04-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.04-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.04-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.04-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Matthew Miller <mattdm@fedoraproject.org> - 3.04-10
- spec file modernization (no group, no rm -rf)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.04-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 20 2017 Gwyn Ciesla <limburgher@gmail.com> - 3.04-8
- Drop tastless content entirely.

* Mon Nov 20 2017 Gwyn Ciesla <limburgher@gmail.com> - 3.04-7
- Split out -tasteless, 1515182.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.04-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 09 2017 Jon Ciesla <limburgher@gmail.com> - 3.04-4
- Require perl-Encode, BZ 1411168.

* Mon Dec 19 2016 Jon Ciesla <limburgher@gmail.com> - 3.04-3
- Fix license tag, BZ 1350114.

* Wed Dec 14 2016 Jon Ciesla <limburgher@gmail.com> - 3.04-2
- Drop bogus Acme::Cow requirement, BZ 1404804.

* Mon Dec 12 2016 Jon Ciesla <limburgher@gmail.com> - 3.04-1
- 3.04, new upstream location, BZ 1403460.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.03-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 17 2016 Hans Ulrich Niedermann <hun@n-dimensional.de> - 3.03-19
- replace %%define by %%global
- avoid license issue with daemon.cow by not shipping it in RPM

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 20 2015 Matthew Miller <mattdm@fedoraproject.org> - 3.03-17
- include unicode and formatting fixes from Debian

* Fri Sep 26 2014 Rahul Sundaram <sundaram@fedoraproject.org> - 3.03-16
- fix location of bash completion script
- don't own /etc/bash_completion.d/
- drop redundant buildroot, defattr and clean

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 3.03-13
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 15 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 3.03-6
- fix license tag to prevent false positive

* Fri May 23 2008 Jon Stanley <jonstanley@gmail.com> - 3.03-5
- Fix license tag

* Tue Oct 09 2007 Michał Bentkowski <mr.ecik at gmail.com> - 3.03-4
- Fix mech-and-cow file (#250844)

* Mon Sep 17 2007 Lubomir Kundrak <lkundrak@redhat.com> - 3.03-3
- Make --help be a bit more sane (#293061)

* Tue Jan 02 2007 Michał Bentkowski <mr.ecik at gmail.com> - 3.03-2
- Use cp -p to keep timestamps
- Fix paths in manpage
- Add animalsay

* Sun Dec 31 2006 Michał Bentkowski <mr.ecik at gmail.com> - 3.03-1
- Initial release
