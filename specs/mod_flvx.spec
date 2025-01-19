%{!?_httpd_apxs: %{expand: %%global _httpd_apxs %%{_sbindir}/apxs}}
%{!?_httpd_mmn: %{expand: %%global _httpd_mmn %%(cat %{_includedir}/httpd/.mmn || echo 0-0)}}
%{!?_httpd_confdir:    %{expand: %%global _httpd_confdir    %%{_sysconfdir}/httpd/conf.d}}
# /etc/httpd/conf.d with httpd < 2.4 and defined as /etc/httpd/conf.modules.d with httpd >= 2.4
%{!?_httpd_modconfdir: %{expand: %%global _httpd_modconfdir %%{_sysconfdir}/httpd/conf.d}}
%{!?_httpd_moddir:     %{expand: %%global _httpd_moddir     %%{_libdir}/httpd/modules}}

%global gitver  48bb878

Summary:        FLV progressive download streaming for the Apache HTTP Server
Name:           mod_flvx
Version:        0
Release:        0.32.20100525git%{?dist}
License:        Apache-2.0
URL:            https://tperspective.blogspot.com/2009/02/apache-flv-streaming-done-right.html
# https://github.com/osantana/mod_flvx/tarball/48bb8781945dfa2e94b2814e9bae5e7d0cc8f29d
Source0:        osantana-%{name}-%{gitver}.tar.gz
Source1:        flvx.conf
Patch0:         mod_flvx-c99.patch
BuildRequires:  gcc, httpd-devel >= 2.0.39
Requires:       httpd-mmn = %{_httpd_mmn}

%description
FLV streaming means it can be sought to any position during video, and
browser (Flash player) will buffer only from this position to the end.
Thus streaming allows to skip boring parts or see video ending without
loading the whole file, which simply saves bandwidth. Even H264 is more
efficient, FLV is still a common container format for videos, because
H264 is supported by Flash since version 9.115.

For using FLV streaming on the web, a pseudo-streaming compliant Flash
player, such as Flowplayer, is needed. Streaming requires that the FLV
has embedded key-frame markers (meta-data), that can be injected by any
supported tool, e.g. flvtool2.

%prep
%autosetup -p1 -n osantana-%{name}-%{gitver}

%build
%{_httpd_apxs} -Wc,-Wall -c %{name}.c

%install
install -D -p -m 755 .libs/%{name}.so $RPM_BUILD_ROOT%{_httpd_moddir}/%{name}.so

head -n 5 %{SOURCE1} > 10-flvx.conf
sed -e '4,5d' %{SOURCE1} > flvx.conf
touch -c -r %{SOURCE1} 10-flvx.conf flvx.conf
install -D -p -m 644 10-flvx.conf $RPM_BUILD_ROOT%{_httpd_modconfdir}/10-flvx.conf
install -D -p -m 644 flvx.conf $RPM_BUILD_ROOT%{_httpd_confdir}/flvx.conf

# Fix incorrect end-of-line encoding
sed -e 's/\r//' README.md > README
touch -c -r README.md README

%files
%doc README
%{_httpd_moddir}/%{name}.so
%config(noreplace) %{_httpd_confdir}/flvx.conf
%config(noreplace) %{_httpd_modconfdir}/10-flvx.conf

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.32.20100525git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.31.20100525git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.30.20100525git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.29.20100525git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.28.20100525git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Feb 25 2023 Florian Weimer <fweimer@redhat.com> - 0-0.27.20100525git
- Port to C99

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.26.20100525git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.25.20100525git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.24.20100525git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.23.20100525git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.22.20100525git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.21.20100525git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20.20100525git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19.20100525git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18.20100525git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.20100525git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.20100525git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.20100525git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.20100525git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.20100525git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.20100525git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.11.20100525git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.10.20100525git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.9.20100525git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 23 2014 Joe Orton <jorton@redhat.com> - 0-0.8.20100525git
- fix _httpd_mmn expansion in absence of httpd-devel

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.20100525git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.20100525git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 17 2012 Robert Scheck <robert@fedoraproject.org> 0-0.5.20100525git
- Updated spec file to match with Apache 2.4 policy (#808560)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.20100525git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0-0.3.20100525git
- Bump build so rawhide is higher than F-17

* Fri Mar 30 2012 Joe Orton <jorton@redhat.com> - 0-0.1.20100525git
- fix build with httpd 2.4

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.20100525git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Mar 15 2011 Robert Scheck <robert@fedoraproject.org> 0-0.1.20100525git
- Upgrade to GIT 20100525
- Initial spec file for Fedora and Red Hat Enterprise Linux
