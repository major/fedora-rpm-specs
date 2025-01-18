# This is the date of the latest upstream git commit.
%global verdate 20150501

Name:           avgtime
Version:        0.5.1
Release:        0.46.git%{verdate}%{?dist}
Summary:        Time a command and print average, standard deviation

# Automatically converted from old format: Boost - review is highly recommended.
License:        BSL-1.0
URL:            https://github.com/jmcabo/avgtime

# There are no upstream source tarballs.  The source tarball
# here was constructed as follows:
#
#   git clone https://github.com/jmcabo/avgtime.git
#   cd avgtime
#   d=YYYYMMDD  # date of latest upstream git commit
#   git archive -o /tmp/avgtime-$d.tar.gz --prefix=avgtime-$d/ HEAD
#
Source0:        avgtime-%{verdate}.tar.gz

ExclusiveArch:  %{ldc_arches}

BuildRequires:  ldc


%description
'avgtime' works like the Linux 'time' command, except it runs the
command repeatedly and displays statistics:

- median
- average
- standard deviation
- 95% and 99% confidence intervals


%prep
%setup -q -n avgtime-%{verdate}


%build
ldc2 %{_d_optflags} avgtime.d


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp -a avgtime $RPM_BUILD_ROOT%{_bindir}


%files
%license LICENSE_1_0.txt
%doc README.md
%{_bindir}/avgtime


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-0.46.git20150501
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 18 2024 Kalev Lember <klember@redhat.com> - 0.5.1-0.45.git20150501
- Rebuilt for ldc 1.40

* Tue Aug 06 2024 Kalev Lember <klember@redhat.com> - 0.5.1-0.44.git20150501
- Rebuilt for ldc 1.39

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.1-0.43.git20150501
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-0.42.git20150501
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-0.41.git20150501
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-0.40.git20150501
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 17 2023 Kalev Lember <klember@redhat.com> - 0.5.1-0.39.git20150501
- Rebuilt for ldc 1.35

* Mon Jul 24 2023 Kalev Lember <klember@redhat.com> - 0.5.1-0.38.git20150501
- Rebuilt for ldc 1.33

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-0.37.git20150501
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 15 2023 Kalev Lember <klember@redhat.com> - 0.5.1-0.36.git20150501
- Rebuilt for ldc 1.32

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-0.35.git20150501
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 27 2022 Kalev Lember <klember@redhat.com> - 0.5.1-0.34.git20150501
- Rebuilt for ldc 1.30

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-0.33.git20150501
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-0.32.git20150501
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 17 2021 Kalev Lember <klember@redhat.com> - 0.5.1-0.31.git20150501
- Rebuilt for ldc 1.27

* Wed Jul 21 2021 Richard W.M. Jones <rjones@redhat.com> - 0.5.1-0.30.git20150501
- Remove rpath.

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-0.29.git20150501
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb 22 2021 Kalev Lember <klember@redhat.com> - 0.5.1-0.28.git20150501
- Rebuilt for ldc 1.25

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-0.27.git20150501
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 21 2020 Kalev Lember <klember@redhat.com> - 0.5.1-0.26.git20150501
- Rebuilt for ldc 1.23

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-0.25.git20150501
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 10 2020 Kalev Lember <klember@redhat.com> - 0.5.1-0.24.git20150501
- Rebuilt for ldc 1.20

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-0.23.git20150501
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-0.22.git20150501
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 09 2019 Kalev Lember <klember@redhat.com> - 0.5.1-0.21.git20150501
- Rebuilt for ldc 1.15

* Mon Feb 18 2019 Kalev Lember <klember@redhat.com> - 0.5.1-0.20.git20150501
- Rebuilt for ldc 1.14

* Wed Feb 06 2019 Richard W.M. Jones <rjones@redhat.com> - 0.5.1-0.19.git20150501
- Bump release and rebuild against latest ldc.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-0.18.git20150501
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 14 2018 Kalev Lember <klember@redhat.com> - 0.5.1-0.17.git20150501
- Rebuilt for ldc 1.12

* Tue Aug 21 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.5.1-0.16.git20150501
- Use %%license
- Rebuild for aarch64

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 0.5.1-0.15.git20150501
- Rebuild with fixed binutils

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-0.14.git20150501
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Kalev Lember <klember@redhat.com> - 0.5.1-0.13.git20150501
- Rebuilt for ldc 1.11

* Mon Feb 19 2018 Kalev Lember <klember@redhat.com> - 0.5.1-0.12.git20150501
- Rebuilt for ldc 1.8

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-0.11.git20150501
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 13 2017 Kalev Lember <klember@redhat.com> - 0.5.1-0.10.git20150501
- Rebuilt for ldc 1.4

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-0.9.git20150501
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-0.8.git20150501
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Kalev Lember <klember@redhat.com> - 0.5.1-0.7.git20150501
- Rebuilt for new ldc compiler

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-0.6.git20150501
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 28 2016 Richard W.M. Jones <rjones@redhat.com> - 0.5.1-0.5.git20150501
- Bump and rebuild for new compiler.

* Sun Oct 30 2016 Kalev Lember <klember@redhat.com> - 0.5.1-0.4.git20150501
- Use new ldc_arches macro

* Mon Oct 24 2016 Kalev Lember <klember@redhat.com> - 0.5.1-0.3.git20150501
- Enable arm and i686 architectures now that ldc is available there

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-0.2.git20150501
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 21 2015 Richard W.M. Jones <rjones@redhat.com> - 0.5.1-0.1.git20150501
- Rebuild for latest D incompatibility.
- Update to latest git version.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.15.git20141110
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Feb 02 2015 Richard W.M. Jones <rjones@redhat.com> - 0-0.14.git20141110
- Bump to fix latest D library brokenness.
- Disable 32 bit x86 which is broken.

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.12.git20130201
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.11.git20130201
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 20 2014 Richard W.M. Jones <rjones@redhat.com> - 0-0.10.git20130201
- Bump again to try to fix latest D library brokenness.

* Sat Aug  3 2013 Richard W.M. Jones <rjones@redhat.com> - 0-0.9.git20130201
- ExcludeArch armv7hl.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.git20130201
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul  7 2013 Richard W.M. Jones <rjones@redhat.com> - 0-0.7.git20130201
- Bump yet again to try to fix latest D library brokenness.

* Mon Jun 17 2013 Richard W.M. Jones <rjones@redhat.com> - 0-0.6.git20130201
- Move to latest upstream git.
- Bump and rebuild again to fix broken dependency.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.git20120724
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 10 2012 Richard W.M. Jones <rjones@redhat.com> - 0-0.4.git20120724
- Try bump and rebuild again to fix broken dependency.

* Thu Sep 27 2012 Richard W.M. Jones <rjones@redhat.com> - 0-0.3.git20120724
- Bump and rebuild.

* Thu Jul 26 2012 Richard W.M. Jones <rjones@redhat.com> - 0-0.2.git20120724
- Rebuild against fixed ldc.
- Add _d_optflags (thanks Jonathan Mercier).

* Wed Jul 25 2012 Richard W.M. Jones <rjones@redhat.com> - 0-0.1.git20120724
- Initial release.
