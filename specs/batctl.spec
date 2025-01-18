Name:           batctl
Version:        2024.2
Release:        3%{?dist}
Summary:        B.A.T.M.A.N. advanced control and management tool

License:        GPL-2.0-only AND MIT AND ISC
URL:            http://www.open-mesh.org/
Source0:        http://downloads.open-mesh.org/batman/stable/sources/batctl/%{name}-%{version}.tar.gz

# Require the batman-adv kernel module for convenience here
# It's not available on EL so make this conditional
# Also, Fedora < 21 doesn't support direct dependencies on kmods
%if 0%{?fedora} >= 21
Requires:       kmod(batman-adv.ko)
%endif
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libnl3-devel

%description
batctl offers a convenient way to configure the batman-adv kernel module
as well as displaying debug information such as originator tables,
translation tables and the debug log. In combination with a bat-hosts
file batctl allows the use of host names instead of MAC addresses.

B.A.T.M.A.N. advanced operates on layer 2. Thus all hosts participating
in the virtual switched network are transparently connected together
for all protocols above layer 2. Therefore the common diagnosis tools
do not work as expected. To overcome these problems batctl contains the
commands ping, traceroute, tcpdump which provide similar functionality
to the normal ping(1), traceroute(1), tcpdump(1) commands, but modified
to layer 2 behavior or using the B.A.T.M.A.N. advanced protocol.


%prep
%setup -q


%build
make %{?_smp_mflags} CFLAGS="%{optflags} -I%{_prefix}/include/libnl3" V=s


%install
%make_install PREFIX=%{_prefix} install


%files
%doc CHANGELOG.rst README.rst bat-hosts.sample
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}.8.gz


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2024.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2024.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 02 2024 John W. Linville <linville@tuxdriver.com> - 2024.2-1
- update to 2024.2

* Thu Feb 01 2024 John W. Linville <linville@tuxdriver.com> - 2024.0-1
- update to 2024.0

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 John W. Linville <linville@tuxdriver.com> - 2023.3-1
- update to 2023.3

* Sat Sep 09 2023 Felix Kaechele <heffer@fedoraproject.org> - 2023.2-2
- convert License tag to SPDX, add missing licenses

* Thu Aug 17 2023 Felix Kaechele <heffer@fedoraproject.org> - 2023.2-1
- update to 2023.2

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2023.1-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed May 31 2023 John W. Linville <linville@tuxdriver.com> - 2023.1-1
- update to 2023.1

* Thu Jan 26 2023 John W. Linville <linville@tuxdriver.com> - 2023.0-1
- update to 2023.0

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 10 2022 Felix Kaechele <heffer@fedoraproject.org> - 2022.3-1
- update to 2022.3

* Tue Jul 26 2022 John W. Linville <linville@tuxdriver.com> - 2022.2-1
- update to 2022.2

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2022.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat May 07 2022 Felix Kaechele <heffer@fedoraproject.org> - 2022.1-1
- update to 2022.1

* Fri Feb 04 2022 Felix Kaechele <heffer@fedoraproject.org> - 2022.0-1
- update to 2022.0

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 19 2021 Felix Kaechele <heffer@fedoraproject.org> - 2021.4-1
- update to 2021.4

* Tue Sep 14 2021 Felix Kaechele <heffer@fedoraproject.org> - 2021.3-1
- update to 2021.3

* Sat Aug 21 2021 Felix Kaechele <heffer@fedoraproject.org> - 2021.2-1
- update to 2021.2

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2021.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 19 2021 Felix Kaechele <heffer@fedoraproject.org> - 2021.1-1
- update to 2021.1

* Thu Jan 28 2021 Felix Kaechele <heffer@fedoraproject.org> - 2021.0-1
- update to 2021.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 27 2020 Felix Kaechele <heffer@fedoraproject.org> - 2020.4-1
- update to 2020.4

* Fri Sep 04 2020 Felix Kaechele <heffer@fedoraproject.org> - 2020.3-1
- update to 2020.3

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2020.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Felix Kaechele <heffer@fedoraproject.org> - 2020.2-1
- update to 2020.2

* Fri Apr 24 2020 Felix Kaechele <heffer@fedoraproject.org> - 2020.1-1
- update to 2020.1

* Thu Mar 05 2020 Felix Kaechele <heffer@fedoraproject.org> - 2020.0-1
- update to 2020.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Felix Kaechele <heffer@fedoraproject.org> - 2019.5-1
- update to 2019.5

* Mon Oct 28 2019 Felix Kaechele <heffer@fedoraproject.org> - 2019.4-1
- update to 2019.4

* Thu Aug 01 2019 Felix Kaechele <heffer@fedoraproject.org> - 2019.3-1
- update to 2019.3

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Felix Kaechele <heffer@fedoraproject.org> - 2019.2-1
- update to 2019.2

* Tue Apr 02 2019 Felix Kaechele <heffer@fedoraproject.org> - 2019.1-1
- update to 2019.1

* Sun Feb 17 2019 Felix Kaechele <heffer@fedoraproject.org> - 2019.0-1
- update to 2019.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 23 2018 Felix Kaechele <heffer@fedoraproject.org> - 2018.4-1
- update to 2018.4

* Mon Sep 17 2018 Felix Kaechele <heffer@fedoraproject.org> - 2018.3-1
- update to 2018.3

* Fri Jul 20 2018 Felix Kaechele <heffer@fedoraproject.org> - 2018.2-1
- update to 2018.2

* Thu Jul 19 2018 John W. Linville <linville@redhat.com> - 2018.1-3
- Add previously unnecessary BuildRequires for gcc

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 30 2018 Felix Kaechele <heffer@fedoraproject.org> - 2018.1-1
- update to 2018.1

* Fri Mar 02 2018 Felix Kaechele <heffer@fedoraproject.org> - 2018.0-1
- update to 2018.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 04 2018 Felix Kaechele <heffer@fedoraproject.org> - 2017.4-1
- update to 2017.4
- added CHANGELOG.rst
- README became README.rst

* Wed Oct 04 2017 Felix Kaechele <heffer@fedoraproject.org> - 2017.3-1
- update to 2017.3

* Tue Sep 05 2017 Felix Kaechele <heffer@fedoraproject.org> - 2017.2-1
- update to 2017.2

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 24 2017 Felix Kaechele <heffer@fedoraproject.org> - 2017.1-1
- update to 2017.1

* Tue Feb 28 2017 Felix Kaechele <heffer@fedoraproject.org> - 2017.0-1
- update to 2017.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Felix Kaechele <heffer@fedoraproject.org> - 2016.5-1
- update to 2016.5

* Sun Nov 20 2016 Felix Kaechele <heffer@fedoraproject.org> - 2016.4-1
- update to 2016.4

* Tue Sep 27 2016 Felix Kaechele <heffer@fedoraproject.org> - 2016.3-1
- update to 2016.3

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2016.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 30 2016 Felix Kaechele <heffer@fedoraproject.org> - 2016.0-1
- update to 2016.0

* Fri Jan 01 2016 Felix Kaechele <heffer@fedoraproject.org> - 2015.2-1
- update to 2015.2

* Sun Oct 25 2015 Felix Kaechele <heffer@fedoraproject.org> - 2015.1-1
- update to 2015.1

* Tue Jul 28 2015 Felix Kaechele <heffer@fedoraproject.org> - 2015.0-1
- update to 2015.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2014.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 10 2015 Felix Kaechele <heffer@fedoraproject.org> - 2014.4.0-3
- dependency on kmods only works for Fedora >= 21

* Mon Mar 02 2015 Felix Kaechele <heffer@fedoraproject.org> - 2014.4.0-2
- make dependency on kmod conditional

* Tue Feb 24 2015 Felix Kaechele <heffer@fedoraproject.org> - 2014.4.0-1
- update to 2014.4.0
- added dependency on kmod(batman-adv.ko) as batctl is useless without it

* Sat Dec  6 2014 Felix Kaechele <heffer@fedoraproject.org> - 2014.3.0-1
- update to 2014.3.0
- added libnl3 BuildRequires
- clean spec

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed May 25 2011 John W. Linville <linville@redhat.com> - 2012.2.0-1
- Update for latest upstream version

* Wed May 25 2011 John W. Linville <linville@redhat.com> - 2011.1.0-1
- Initial release for Fedora
