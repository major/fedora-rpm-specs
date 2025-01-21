%define svn_revision 39
%define snapshot_date 20071107

Name:           upslug2
Version:        0.0
Release:        0.33.%{snapshot_date}.svn%{svn_revision}%{?dist}
Summary:        Firmware update utility for the nslu2
License:        MIT
URL:            http://www.nslu2-linux.org/wiki/Main/UpSlug2
# To recreate:
# svn export -r %{svn_revision} http://svn.nslu2-linux.org/svnroot/upslug2/trunk %{name}
# tar cvfz %{name}-svn-%{svn_revision}.tar.gz %{name}
Source0:        %{name}-svn-%{svn_revision}.tar.gz
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  automake libpcap-devel

%description
upslug2 is a command line program intended to allow the upgrade of a LinkSys
NSLU2 firmware to new or different versions.  Unlike upslug and the LinkSys
(Sercomm) upgrade utilities, upslug2 will synthesise a complete 'image'
from a kernel and a root file system, as such it duplicates part of the
functionality of 'slugimage'.

upslug2 also optimizes the upload to avoid transmitted parts of the image which
need not be written or are 'blank' (set to the erased flash value of all 1's).


%prep
%setup -q -n %{name}
autoreconf -i


%build
%configure --with-libpcap
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man8
install -p -m 644 upslug2.8 $RPM_BUILD_ROOT/%{_mandir}/man8



%files
%doc AUTHORS ChangeLog COPYING README
%{_sbindir}/upslug2
%{_mandir}/man8/upslug2.8.gz


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.33.20071107.svn39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.32.20071107.svn39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.31.20071107.svn39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.30.20071107.svn39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.29.20071107.svn39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.28.20071107.svn39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.27.20071107.svn39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.26.20071107.svn39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.25.20071107.svn39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.24.20071107.svn39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.23.20071107.svn39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.22.20071107.svn39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.21.20071107.svn39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.20.20071107.svn39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.19.20071107.svn39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.18.20071107.svn39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.17.20071107.svn39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.16.20071107.svn39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.15.20071107.svn39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-0.14.20071107.svn39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.0-0.13.20071107.svn39
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-0.12.20071107.svn39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-0.11.20071107.svn39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-0.10.20071107.svn39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-0.9.20071107.svn39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-0.8.20071107.svn39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-0.7.20071107.svn39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-0.6.20071107.svn39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-0.5.20071107.svn39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-0.4.20071107.svn39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.0-0.3.20071107.svn39
- Autorebuild for GCC 4.3

* Wed Nov  7 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.0-0.2.20071107.svn39
- Add snapshot date to release field (bz 350181)
- Do not repeat the package name in the summary (bz 350181)

* Wed Oct 24 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.0-0.1.svn39
- Initial Fedora package
