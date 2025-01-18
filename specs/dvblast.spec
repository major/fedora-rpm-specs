Name:           dvblast
Version:        3.4
Release:        16%{?dist}
Summary:        Simple and powerful streaming application

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://www.videolan.org/projects/dvblast.html
Source0:        https://downloads.videolan.org/pub/videolan/dvblast/%{version}/dvblast-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  bitstream-devel >= 1.4
BuildRequires:  libev-devel
BuildRequires: make


%description
DVBlast is a simple and powerful streaming application based on the
linux-dvb API. It opens a DVB device, tunes it, places PID filters,
configures a CAM module, and demultiplexes the packets to several RTP
outputs. It supports the new S2API of linux-dvb (compile option).


%prep
%setup -q
# Prepare dvbiscovery
sed -i -e 's|/usr/local|/usr|' extra/dvbiscovery/dvbiscovery.sh
install -pm 0644 extra/dvbiscovery/README README.dvbiscovery



%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{?__global_ldflags}"
%make_build V=1


%install
%make_install PREFIX=%{_prefix}

# Add missing dvbiscovery scripts
mkdir -p %{buildroot}%{_datadir}/%{name}/dvbiscovery
install -pm 0644 extra/dvbiscovery/*.conf \
  %{buildroot}%{_datadir}/%{name}/dvbiscovery
install -pm 0755 extra/dvbiscovery/dvbiscovery.sh %{buildroot}%{_bindir}



%files
%doc AUTHORS COPYING NEWS README TODO
%doc README.dvbiscovery
%license COPYING
%{_bindir}/dvbiscovery.sh
%{_bindir}/dvblast
%{_bindir}/dvblastctl
%{_bindir}/dvblast_mmi.sh
%{_mandir}/man1/dvblast.1.*
%{_datadir}/%{name}

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 3.4-15
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 24 2018 Nicolas Chauvet <kwizart@gmail.com> - 3.4-1
- Update to 3.4

* Tue Jul 17 2018 Nicolas Chauvet <kwizart@gmail.com> - 3.3-3
- Add missing cc

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 04 2018 Nicolas Chauvet <kwizart@gmail.com> - 3.3-1
- Update to 3.3

* Tue Feb 06 2018 Nicolas Chauvet <kwizart@gmail.com> - 3.1-2
- Rebuilt for bitsteam 1.3

* Thu Sep 14 2017 Nicolas Chauvet <kwizart@gmail.com> - 3.1-1
- Update to 3.1

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Oct 04 2016 Nicolas Chauvet <kwizart@gmail.com> - 3.0-3
- Add dvbiscovery scripts

* Tue Oct 04 2016 Nicolas Chauvet <kwizart@gmail.com> - 3.0-2
- Backport fix for LDFLAGS from upstream

* Thu Sep 15 2016 Nicolas Chauvet <kwizart@gmail.com> - 3.0-1
- Update to 3.0

* Thu Aug 23 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.2-1
- Update to 2.2

* Mon Jan 16 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.1.0-1
- Update to 2.1.0

* Sat Apr 24 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 1.2-1
- Update to 1.2

* Mon Nov 30 2009 Nicolas Chauvet <kwizart@fedoraproject.org> - 1.1-1
- Initial spec file

