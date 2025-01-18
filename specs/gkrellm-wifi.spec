Name:           gkrellm-wifi
Version:        0.9.12
Release:        41%{?dist}
Summary:        Wireless monitor plugin for the GNU Krell Monitors
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.gkrellm.net/
# upsteam is dead, no URL
Source0:        %{name}-%{version}.tar.gz
Patch0:         %{name}-%{version}.patch
Patch1:         gkrellm-wifi-0.9.12-asm_h.patch
Patch2:         gkrellm-wifi-0.9.12-kernel-2.6.26.patch
Patch3:         gkrellm-wifi-0.9.12-bz650345.patch
BuildRequires:  gcc
BuildRequires:  gkrellm-devel
BuildRequires: make
Requires:       gkrellm >= 2.2, gkrellm < 3
# Unfortunate, but nescesarry this plugin used to be (wrongly) packaged in the
# same specfile as gkrellm itself, with the wrong namae gkrellm-wireless and
# causing it to have version 2.2.9 :(
Obsoletes:      gkrellm-wireless <= 2.2.9-3
Provides:       gkrellm-wireless = 2.2.9-4
ExcludeArch:    s390 s390x

%description
Plug-in for gkrellm (a system monitor) which monitors the wireless LAN cards in
your PC and displays a graph of the link quality percentage for each card.


%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1 -z .asm_h
%patch -P2 -p1
%patch -P3 -p1


%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -fPIC \
  `pkg-config gkrellm --cflags` -DG_LOG_DOMAIN=\\\"gkrellm-wifi\\\""


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}/gkrellm2/plugins
install -m 755 %{name}.so $RPM_BUILD_ROOT%{_libdir}/gkrellm2/plugins



%files
%doc AUTHORS COPYING ChangeLog NEWS README THEMING TODO
%{_libdir}/gkrellm2/plugins/%{name}.so


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.12-40
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.12-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.12-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.12-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.12-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.12-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.12-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.12-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.9.12-13
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov  7 2010 Hans de Goede <hdegoede@redhat.com> - 0.9.12-11
- Don't flood the log with errors when a cards driver won't allow us to
  do SIOCGIWRANGE (rhbz#650345)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat May 31 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.12-8
- Fix compiling with mix of latest glibc + kernel headers (avoid header
  conflict)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.12-7
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.12-6
- Fix Source0 URL

* Tue Aug  7 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.12-5
- Update License tag for new Licensing Guidelines compliance

* Mon Feb 19 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.12-4
- Add #include <asm/types.h> to fix compile with recent kernel-headers

* Mon Aug 28 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.12-3
- FE6 Rebuild

* Mon Jul 17 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.12-2
- Use pristine upstream source and put changes found in the Core package
  tarbal in a patch
- Require gkrellm >= 2.2, gkrellm < 3
- Add ExcludeArch: s390 s390x

* Fri Jul  7 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.12-1
- Initial Fedora Extras Package
