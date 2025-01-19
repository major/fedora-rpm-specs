Name:           inxi
Version:        3.3.37
Release:        2%{?dist}
Summary:        A full featured system information script

License:        GPL-3.0-or-later
URL:            https://smxi.org/docs/inxi.htm
Source0:        https://codeberg.org/smxi/inxi/archive/%{version}-1.tar.gz

BuildArch:      noarch

BuildRequires:  perl-generators

Requires:       iproute
Requires:       pciutils
Requires:       procps
Requires:       lm_sensors
Requires:       usbutils
Requires:       hddtemp
Requires:       xdpyinfo xprop xrandr
Requires:       bind-utils
Requires:       ipmitool
Requires:       freeipmi
Requires:       wmctrl
# inxi can use any one of Cpanel::JSON::XS, JSON::XS or JSON::PP, but
# Cpanel::JSON::XS seems to be its preference, so let's go with that
Requires:       perl(Cpanel::JSON::XS)
# The debugger requires all of these, but the requirements are hedged
# around upstream to try and gracefully handle them being missing,
# so the dependency generator misses them. I tried
# https://codeberg.org/smxi/pinxi/pulls/2 , but upstream was not
# interested, so these need to be explicitly specified
Requires:       perl(Time::HiRes)
Requires:       perl(File::Copy)
Requires:       perl(File::Find)
Requires:       perl(Net::FTP)
# inxi does not actually use Spec::Functions at all - only Spec -
# but the debugger refuses to run if it cannot load it. specify
# both the actual functional requirement, and the bogus checked
# requirement
Requires:       perl(File::Spec)
Requires:       perl(File::Spec::Functions)
# the debugger also requires tar to create the debug archive
Requires:       tar
# inxi documents that this isn't strictly required and works without
# it, you just can't output to XML, so let's call it Recommends:
Recommends:     perl(XML::Dumper)
# inxi likes to use these for downloading, but will use curl or wget
# if they are not present
Recommends:     perl(HTTP::Tiny) perl(IO::Socket::SSL)
# inxi defends against this not being present by falling back to
# a subshell of 'hostname', so it will work without it
Recommends:     perl(Sys::Hostname)

%description
Inxi offers a wide range of built-in options, as well as a good number of extra
features which require having the script recommends installed on the system.


%prep
%autosetup -n %{name}
#Disable update option
sed -i 's/my ($b_sysctl_disk,$b_update,$b_weather) = (1,1,1);/my ($b_sysctl_disk,$b_update,$b_weather) = (1,0,1);/' inxi
#Correct shebang
sed -i 's|/usr/bin/env perl|/usr/bin/perl|' inxi

%build
#Nothing to build


%install
install -p -D -m 755 %{name} %{buildroot}/%{_bindir}/%{name}
gzip %{name}.1
install -p -D -m 644 %{name}.1.gz %{buildroot}/%{_mandir}/man1/%{name}.1.gz

%files
%doc %{name}.changelog README.txt
%license LICENSE.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan 09 2025 Vasiliy N. Glazov <vascom2@gmail.com> - 3.3.37-1
- Update to 3.3.37

* Mon Oct 07 2024 Vasiliy N. Glazov <vascom2@gmail.com> - 3.3.36-1
- Update to 3.3.36

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr 16 2024 Vasiliy N. Glazov <vascom2@gmail.com> - 3.3.34-1
- Update to 3.3.34

* Thu Feb 15 2024 Vasiliy N. Glazov <vascom2@gmail.com> - 3.3.33-1
- Update to 3.3.33

* Tue Feb 06 2024 Vasiliy N. Glazov <vascom2@gmail.com> - 3.3.32-1
- Update to 3.3.32

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.31-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 12 2024 Adam Williamson <awilliam@redhat.com> - 3.3.31-2
- BuildRequire perl-generators
- Add several missing hard and soft dependencies

* Thu Nov 02 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 3.3.31-1
- Update to 3.3.31

* Sun Oct 01 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 3.3.30-1
- Update to 3.3.30

* Thu Aug 17 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 3.3.29-1
- Update to 3.3.29

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 23 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 3.3.27-1
- Update to 3.3.27

* Mon Apr 03 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 3.3.26-1
- Update to 3.3.26

* Sat Mar 11 2023 Fabio Valentini <decathorpe@gmail.com> - 3.3.25-2
- Rebuild for https://pagure.io/releng/issue/11327

* Thu Feb 09 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 3.3.25-1
- Update to 3.3.25

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 15 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 3.3.24-1
- Update to 3.3.24

* Tue Nov 15 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 3.3.23-1
- Update to 3.3.23

* Sat Oct 29 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 3.3.22-1
- Update to 3.3.22

* Mon Sep 19 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 3.3.21-1
- Update to 3.3.21

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 3.3.19-1
- Update to 3.3.19

* Tue May 24 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 3.3.16-1
- Update to 3.3.16

* Sat Apr 02 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 3.3.14-1
- Update to 3.3.14

* Sun Feb 27 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 3.3.13-1
- Update to 3.3.13

* Wed Jan 26 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 3.3.12-1
- Update to 3.3.12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 11 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 3.3.11-1
- Update to 3.3.11

* Thu Nov 25 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 3.3.09-1
- Update to 3.3.09
- Add perl-Data-Dumper requires

* Tue Jul 27 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 3.3.06-1
- Update to 3.3.06

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Apr 05 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 3.3.03-1
- Update to 3.3.03

* Wed Mar 17 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 3.3.02-1
- Update to 3.3.02

* Mon Feb 22 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 3.3.01-1
- Update to 3.3.01

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 3.2.01-1
- Update to 3.2.01

* Thu Dec 17 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 3.2.00-1
- Update to 3.2.00

* Wed Oct 21 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 3.1.08-1
- Update to 3.1.08

* Thu Aug 20 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 3.1.06-1
- Update to 3.1.06

* Tue Jul 28 2020 Adam Jackson <ajax@redhat.com> - 3.1.03-3
- Require xdpyinfo xprop xrandr, not xorg-x11-utils

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 13 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 3.1.03-1
- Update to 3.1.03

* Sun Apr 26 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 3.1.00-1
- Update to 3.1.00

* Thu Apr 16 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 3.0.38-2
- Add dependency File::Find

* Mon Mar 16 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 3.0.38-1
- Update to 3.0.38

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 20 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 3.0.37-1
- Update to 3.0.37

* Thu Aug 15 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 3.0.36-1
- Update to 3.0.36

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 3.0.35-1
- Update to 3.0.35

* Mon May 06 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 3.0.34-1
- Update to 3.0.34

* Fri Feb 15 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 3.0.32-1
- Update to 3.0.32

* Thu Feb 07 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 3.0.31-1
- Update to 3.0.31

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 11 2018 Vasiliy N. Glazov <vascom2@gmail.com> 3.0.29-1
- Update to 3.0.29

* Thu Dec 06 2018 Vasiliy N. Glazov <vascom2@gmail.com> 3.0.28-1
- Update to 3.0.28

* Wed Oct 17 2018 Vasiliy N. Glazov <vascom2@gmail.com> 3.0.27-1
- Update to 3.0.27

* Mon Oct 08 2018 Vasiliy N. Glazov <vascom2@gmail.com> 3.0.26-1
- Update to 3.0.26

* Wed Sep 12 2018 Vasiliy N. Glazov <vascom2@gmail.com> 3.0.24-1
- Update to 3.0.24

* Mon Sep 10 2018 Vasiliy N. Glazov <vascom2@gmail.com> 3.0.23-1
- Update to 3.0.23

* Tue Sep 04 2018 Vasiliy N. Glazov <vascom2@gmail.com> 3.0.22-1
- Update to 3.0.22

* Tue Aug 28 2018 Vasiliy N. Glazov <vascom2@gmail.com> 3.0.21-1
- Update to 3.0.21

* Wed Aug 01 2018 Vasiliy N. Glazov <vascom2@gmail.com> 3.0.20-1
- Update to 3.0.20

* Thu Jul 19 2018 Vasiliy N. Glazov <vascom2@gmail.com> 3.0.18-1
- Update to 3.0.18

* Fri Jul 13 2018 Vasiliy N. Glazov <vascom2@gmail.com> 3.0.17-1
- Update to 3.0.17

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 04 2018 Vasiliy N. Glazov <vascom2@gmail.com> 3.0.15-1
- Update to 3.0.15

* Thu Jun 28 2018 Vasiliy N. Glazov <vascom2@gmail.com> 3.0.14-1
- Update to 3.0.14

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.56-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.56-1
- Update to 2.3.56

* Wed Dec 13 2017 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.53-1
- Update to 2.3.53

* Wed Nov 22 2017 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.45-1
- Update to 2.3.45

* Fri Nov 03 2017 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.43-1
- Update to 2.3.43

* Tue Oct 03 2017 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.40-1
- Update to 2.3.40

* Tue Sep 12 2017 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.38-1
- Update to 2.3.38

* Wed Aug 23 2017 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.36-1
- Update to 2.3.36

* Tue Aug 01 2017 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.31-1
- Update to 2.3.31

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.23-1
- Update to 2.3.23

* Mon Jun 19 2017 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.22-1
- Update to 2.3.22

* Mon Jun 19 2017 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.21-1
- Update to 2.3.21

* Thu Jun 01 2017 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.11-1
- Update to 2.3.11

* Tue May 30 2017 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.9-1
- Update to 2.3.9

* Wed May 17 2017 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.8-3
- Remove deprecated net-tools dependency

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 20 2017 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.8-1
- Update to 2.3.8

* Sat Jan 07 2017 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.7-1
- Update to 2.3.7

* Thu Dec 08 2016 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.5-1
- Update to 2.3.5

* Mon Nov 21 2016 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.4-1
- Update to 2.3.4

* Fri Oct 28 2016 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.3-1
- Update to 2.3.3

* Thu Sep 15 2016 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.1-1
- Update to 2.3.1

* Thu Apr 21 2016 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.0-1
- Update to 2.3.0

* Mon Apr 18 2016 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.38-1
- Update to 2.2.38

* Thu Mar 17 2016 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.35-1
- Update to 2.2.35

* Fri Feb 26 2016 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.34-1
- Update to 2.2.34
- Added Requires bind-utils
- Added readme and license files

* Thu Feb 04 2016 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.33-1
- Update to 2.2.33

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.32-1
- Update to 2.2.32

* Fri Nov 20 2015 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.31-1
- Update to 2.2.31

* Thu Aug 27 2015 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.28-1
- Update to 2.2.28

* Fri Jun 19 2015 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.25-1
- Update to 2.2.25

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 15 2015 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.21-1
- Update to 2.2.21

* Thu Nov 06 2014 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.16-1
- Update to 2.2.16

* Mon Sep 29 2014 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.14-1
- Update to 2.2.14

* Mon Sep 22 2014 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.8-1
- Update to 2.2.8

* Fri Aug 22 2014 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.1-1
- Update to 2.2.1

* Tue Aug 12 2014 Vasiliy N. Glazov <vascom2@gmail.com> 2.1.90-1
- Update to 2.1.90

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 06 2014 Vasiliy N. Glazov <vascom2@gmail.com> 2.1.28-1
- Update to 2.1.28

* Fri Apr 18 2014 Vasiliy N. Glazov <vascom2@gmail.com> 2.1.20-1
- Update to 2.1.20

* Mon Mar 31 2014 Vasiliy N. Glazov <vascom2@gmail.com> 2.1.13-1
- Update to 2.1.13

* Mon Feb 10 2014 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.18-1
- Update to 1.9.18

* Thu Dec 26 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.17-1
- Update to 1.9.17

* Fri Aug 23 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.14-2
- Correct sources

* Thu Aug 22 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.14-1
- Update to new version
- Disable builtin update

* Mon Aug 19 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.13-1
- Update to new version

* Thu Aug 08 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.12-5
- Correct executable permissions

* Wed Aug 07 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.12-4
- Removed unnecessary Requires

* Tue Aug 06 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.12-3
- Change source0 link
- Added Requires

* Tue Aug 06 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.12-2
- Correct spec and descriptions

* Wed Jul 03 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.12-1
- Update to 1.9.12

* Tue Jun 18 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.9-1
- Update to 1.9.9

* Tue Jun 04 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.7-1
- Update to 1.9.7

* Tue May 07 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.8.47-1
- Update to 1.8.47

* Mon Apr 22 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.8.45-1
- Initial release
