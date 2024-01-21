%bcond_without lto
%bcond_without openssl

%if %{with lto}
%global optflags        %{optflags} -flto
%global build_ldflags   %{build_ldflags} -flto
%endif

Name:           goaccess
Version:        1.8.1
Release:        2%{?dist}
Summary:        Real-time web log analyzer and interactive viewer
License:        GPLv2+
URL:            https://goaccess.io/
Source0:        https://tar.goaccess.io/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
%if 0%{?fedora} > 36
BuildRequires:  libmaxminddb-devel
%else
BuildRequires:  GeoIP-devel
%endif
BuildRequires:  ncurses-devel
BuildRequires:  gettext-devel
%if %{with openssl}
BuildRequires:  openssl-devel
%endif
BuildRequires:  make

%description
GoAccess is a real-time web log analyzer and interactive viewer that runs in a
terminal in *nix systems. It provides fast and valuable HTTP statistics for
system administrators that require a visual server report on the fly.

Features:
GoAccess parses the specified web log file and outputs the data to terminal.

* General statistics, bandwidth, etc.
* Time taken to serve the request (useful to track pages that are slowing down
your site).
* Metrics for cumulative, average and slowest running requests.
* Top visitors.
* Requested files & static files.
* 404 or Not Found.
* Hosts, Reverse DNS, IP Location.
* Operating Systems.
* Browsers and Spiders.
* Referring Sites & URLs.
* Keyphrases.
* Geo Location - Continent/Country/City.
* Visitors Time Distribution.
* HTTP Status Codes.
* Ability to output JSON and CSV.
* Tailor GoAccess to suit your own color taste/schemes.
* Support for large datasets + data persistence.
* Support for IPv6.
* Output statistics to HTML. 
and more...

GoAccess allows any custom log format string. Predefined options include, but
not limited to:

* Amazon CloudFront (Download Distribution).
* AWS Elastic Load Balancing.
* Apache/Nginx Common/Combined + VHosts.
* Google Cloud Storage.
* W3C format (IIS).

%prep
%autosetup
# Prevent flags being overridden again and again.
#sed -i 's|-pthread|$CFLAGS \0|' configure.ac
sed -i '/-pthread/d' configure.ac

%build
# autoreconf -fiv
# %%configure --enable-debug --enable-geoip --enable-utf8 --enable-tcb=btree --with-getline
%configure \
    --enable-debug \
%if 0%{?fedora} > 36
    --enable-geoip=mmdb \
%else     
    --enable-geoip=legacy \
%endif
    --enable-utf8 \
    --with-getline \
    %{?with_openssl: --with-openssl}
%make_build

%install
%make_install
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%config(noreplace) %{_sysconfdir}/%{name}/browsers.list
%config(noreplace) %{_sysconfdir}/%{name}/podcast.list
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Nov 2 2023 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.8.1-1
- Update to 1.8.1, fixes rhbz#2247712

* Sun Oct 1 2023 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.8-1
- Update to 1.8, fixes rhbz#2241581

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Filipe Rosset <rosset.filipe@gmail.com> - 1.7.2-1
- Update to 1.7.2, fixes rhbz#2183783

* Thu Mar 2 2023 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.7.1-1
- Update to 1.7.1, fixes rhbz#2174504

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 2 2023 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.7-1
- Update to 1.7, fixes rhbz#2157304

* Sat Nov 5 2022 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.6.5-1
- Update to 1.6.5, fixes rhbz#2131437

* Sat Sep 3 2022 Eduardo Echeverria <echevemaster@gmail.com> - 1.6.3-1
- Update to 1.6.3

* Mon Aug 15 2022 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.6.2-1
- Update to 1.6.2, fixes rhbz#2107794

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 10 2022 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.6.1-1
- Update to 1.6.1, fixes rhbz#2103284

* Thu Jun 02 2022 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.6-1
- Update to 1.6, fixes rhbz#2080337

* Sun Apr 03 2022 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.5.6-1
- Update to 1.5.6

* Wed Feb 02 2022 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.5.5-1
- Update to 1.5.5

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 03 2022 Alessio <alciregi@fedoraproject.org> - 1.5.4-1
- Update to 1.5.4

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.4.6-3
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Mar 14 2021 Eduardo Echeverria <echevemaster@gmail.com> - 1.4.6-1
- Update to 1.4.6 

* Sun Feb 14 2021 Eduardo Echeverria <echevemaster@gmail.com> - 1.4.5-1
- Update to 1.4.5 fixes rhbz#1920124

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan  7 2021 Filipe Rosset <rosset.filipe@gmail.com> - 1.4.3-1
- Update to 1.4.3 fixes rhbz#1837101

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 29 2020 Eduardo Echeverria <echevemaster@gmail.com> - 1.3-1
- Upgrade version to 1.3, thanks elxreno@gmail.com

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 22 2017 Eduardo Echeverria <echevemaster@gmail.com> - 1.2-1
- Update to 1.2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 01 2017 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.1.1-1
- Update to 1.1.1

* Sun Oct 09 2016 Eduardo Echeverria <echevemaster@gmail.com> - 1.0.2-2
- Fix typo on the summary

* Sat Oct 08 2016 Eduardo Echeverria <echevemaster@gmail.com> - 1.0.2-1
- Update to 1.0.2 

* Fri Apr 22 2016 Christopher Meng <rpm@cicku.me> - 0.9.8-1
- Update to 0.9.8

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 27 2015 Christopher Meng <rpm@cicku.me> - 0.9.6-1
- Update to 0.9.6

* Wed Sep 09 2015 Christopher Meng <rpm@cicku.me> - 0.9.4-1
- Update to 0.9.4

* Thu Aug 27 2015 Christopher Meng <rpm@cicku.me> - 0.9.3-1
- Update to 0.9.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Dec 5 2014 Eduardo Echeverria <echevemaster@gmail.com> - 0.8.5-1
- Update to 0.8.5

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Christopher Meng <rpm@cicku.me> - 0.8.2-1
- Update to 0.8.2

* Wed Jun 18 2014 Christopher Meng <rpm@cicku.me> - 0.8.1-1
- Update to 0.8.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Christopher Meng <rpm@cicku.me> - 0.8-1
- Update to 0.8

* Thu Feb 20 2014 Christopher Meng <rpm@cicku.me> - 0.7.1-1
- Update to 0.7.1

* Sat Jan 18 2014 Ville Skyttä <ville.skytta@iki.fi> - 0.7-2
- Build with $RPM_OPT_FLAGS, fix -debuginfo.

* Wed Jan 15 2014 Eduardo Echeverria <echevemaster@gmail.com> - 0.7-1
- Update to 0.7

* Wed Nov 20 2013 Christopher Meng <rpm@cicku.me> - 0.6.1-1
- Update to 0.6.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 19 2013 Eduardo Echeverria  <echevemaster@gmail.com> - 0.6-1
- Updated to the new upstream version

* Sat May 25 2013 Eduardo Echeverria  <echevemaster@gmail.com> - 0.5-2
- Fix license field, GPLv2+ is correct
- Add NEWS and Changelog files to %%doc

* Sat May 25 2013 Eduardo Echeverria  <echevemaster@gmail.com> - 0.5-1
- Initial packaging
