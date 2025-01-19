Name:           libzfcphbaapi
Summary:        HBA API for the zFCP device driver
Version:        3.0.2
Release:        2%{?dist}
License:        EPL-1.0
URL:            https://github.com/ibm-s390-linux/libzfcphbaapi
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:         %{name}-3.0.2-fedora.patch

ExclusiveArch:  s390 s390x

BuildRequires:  gcc
BuildRequires:  automake autoconf libtool
BuildRequires:  doxygen
BuildRequires:  sg3_utils-devel
BuildRequires:  make
Requires(post): grep sed

%description
zFCP HBA API Library is an implementation of FC-HBA (see www.t11.org) for
the zFCP device driver.


%package devel
Summary:  Development files for zFCP HBA API Library
Requires: %{name} = %{version}-%{release}
Conflicts: libhbaapi-devel

%description devel
Development files for the zFCP HBA API Library.

%package docs
Summary:  Documentation for zFCP HBA API Library
Requires: %{name} = %{version}-%{release}

%description docs
Documentation in HTML format for the zFCP HBA API Library.


%prep
%autosetup


%build
autoreconf -vif

%configure --disable-static
%make_build EXTRA_CFLAGS="-fno-strict-aliasing"


%install
%makeinstall docdir=%{buildroot}%{_docdir}/%{name}
# keep only html docs
rm -rf %{buildroot}%{_docdir}/%{name}/latex


%post
# remove old entry from hba.conf on upgrade
if [ $1 == 2 -a -f /etc/hba.conf ]; then
    grep -q -e "^libzfcphbaapi" /etc/hba.conf &&
        sed -i.orig -e "/^libzfcphbaapi/d" /etc/hba.conf
fi
:


%files
%license LICENSE
%doc README COPYING ChangeLog AUTHORS
%{_bindir}/zfcp_ping
%{_bindir}/zfcp_show
%{_libdir}/%{name}.so.*
%{_mandir}/man3/libzfcphbaapi.3*
%{_mandir}/man3/SupportedHBAAPIs.3*
%{_mandir}/man3/UnSupportedHBAAPIs.3*
%{_mandir}/man8/zfcp_ping.8*
%{_mandir}/man8/zfcp_show.8*

%files devel
%{_mandir}/man3/hbaapi.h.3*
%{_libdir}/%{name}.so
%{_includedir}/hbaapi.h

%files docs
%{_docdir}/%{name}/html


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Dec 13 2024 Dan Horák <dan[at]danny.cz> - 3.0.2-1
- updated to 3.0.2 from github

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 11 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 2.2.0-22
- Rebuilt for sg3_utils 1.48

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 27 2023 Florian Weimer <fweimer@redhat.com> - 2.2.0-18
- Fix C99 compatibility issues (#2165019)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Apr 14 2022 Dan Horák <dan[at]danny.cz> - 2.2.0-15
- add devel subpackage

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Apr 06 2021 Tomas Bzatek <tbzatek@redhat.com> - 2.2.0-12
- rebuilt for sg3_utils 1.46

* Mon Mar 01 2021 Dan Horák <dan[at]danny.cz> - 2.2.0-11
- drop superfluous BR

* Tue Feb 02 2021 Dan Horák <dan[at]danny.cz> - 2.2.0-10
- build with libzfcphbaapi as standalone library to avoid dependency on obsolete libhbaapi (#1922413)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 12 2020 Florian Weimer <fweimer@redhat.com> - 2.2.0-8
- Trigger rebuild to avoid DT_INIT/DT_FINI with zero values

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 20 2020 Dan Horák <dan@danny.cz> - 2.2.0-6
- rebuilt for sg3_utils 1.45 (#1809392)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 27 2019 Dan Horák <dan[at]danny.cz> - 2.2.0-4
- fix scriptlets so they work correctly on upgrades

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar  8 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 2.2.0-2
- Fix requirement for %%preun (instead of %%postun) scriptlet

* Thu Feb 28 2019 Dan Horák <dan[at]danny.cz> - 2.2.0-1
- updated to 2.2.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 05 2014 Dan Horák <dan@danny.cz> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 14 2014 Dan Horák <dan[at]danny.cz> - 2.1.1-1
- updated to 2.1.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 29 2013 Dan Horák <dan[at]danny.cz> - 2.1-2
- add missing compatibility Provides
- exclude plugin soname from Provides

* Thu May 16 2013 Dan Horák <dan[at]danny.cz> - 2.1-1
- move libzfcphbaapi to own package from s390utils
