%global octpkg communications

Name:           octave-%{octpkg}
Version:        1.2.7
Release:        1%{?dist}
Summary:        Communications for Octave
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://gnu-octave.github.io/packages/communications/
Source0:        https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
# the following are required to build the documentation, and they come from the main octave package
Source1:        mkdoc
Source2:        mktexi

BuildRequires: make
BuildRequires:  octave-devel
BuildRequires:  octave-signal >= 1.0.0
BuildRequires:  octave-image >= 0.0.0
BuildRequires:  hdf5-devel
BuildRequires:  texinfo-tex
# For patches that requires autoreconf
BuildRequires:  automake

Requires:       octave(api) = %{octave_api}
Requires:       octave-signal >= 1.0.0 
Requires:       octave-image >= 0.0.0
Requires(post): octave
Requires(postun): octave

Obsoletes:      octave-forge <= 20090607

# octave-signal not available for s390x
ExcludeArch:    s390x

%description
Digital Communications, Error Correcting Codes (Channel Code), Source Code
functions, Modulation and Galois Fields

%prep
%setup -q -n %{octpkg}-%{version}
cp -p %{SOURCE1} %{SOURCE2} .
chmod a+x mkdoc mktexi
cd src
autoreconf
cd -
make -C doc comms.texi

%build
export MKOCTFILE="mkoctfile -v"
%octave_pkg_build
make -C doc

%install
%octave_pkg_install
# remove doc build junk
rm -rf %{buildroot}/%{octpkgdir}/doc
install -m 0644 doc/comms.info %{buildroot}/%{octpkgdir}
chmod a-x %{buildroot}/%{octpkgdir}/*.m
chmod a-x %{buildroot}/%{octpkgdir}/@galois/*.m

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%{octpkglibdir}

%dir %{octpkgdir}
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/*.m
%{octpkgdir}/@galois/*.m
%{octpkgdir}/packinfo
%{octpkgdir}/comms.info

%changelog
* Thu Jan 30 2025 Thomas Sailer <fedora@tsailer.ch> - 1.2.7-1
- Update to 1.2.7

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Nov 15 2024 Orion Poplawski <orion@nwra.com> - 1.2.6-1
- Update to 1.2.6

* Thu Nov 14 2024 Orion Poplawski <orion@nwra.com> - 1.2.5-8
- Rebuild for octave 9.2

* Fri Oct 25 2024 Orion Poplawski <orion@nwra.com> - 1.2.5-7
- Rebuild for hdf5 1.14.5

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.5-6
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May 08 2023 Thomas Sailer <fedora@tsailer.ch> - 1.2.5-1
- Update to 1.2.5 (#2195935)

* Sat Apr 08 2023 Orion Poplawski <orion@nwra.com> - 1.2.4-5
- Rebuild with octave 8.1.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Orion Poplawski <orion@nwra.com> - 1.2.4-2
- Rebuild for octave 7.1

* Thu Jan 20 2022 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1.2.4-1
- Update to 1.2.4 (#2042742)

* Wed Aug 11 2021 Orion Poplawski <orion@nwra.com> - 1.2.3-3
- Rebuild for hdf5 1.10.7/octave 6.3.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Apr 05 2021 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.2.3-1
- Update to 1.2.3

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 05 2020 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.2.2-1
- Update to 1.2.2

* Thu Nov 07 2019 Orion Poplawski <orion@nwra.com> - 1.2.1-16
- Rebuild with octave 64bit indexes

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.2.1-14
- replace new octave fixes patch

* Mon Mar 18 2019 Orion Poplawski <orion@nwra.com> - 1.2.1-13
- Rebuild for hdf5 1.10.5

* Tue Feb 05 2019 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.2.1-12
- Fix config.h renamed to octave-config.h in octave 4.4

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 11 2018 Orion Poplawski <orion@cora.nwra.com> - 1.2.1-10
- Rebuild for octave 4.4

* Fri Jul 13 2018 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.2.1-9
- rebuild
- disable s390x as octave-signal is not available on this platform

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 10 2016 Orion Poplawski <orion@cora.nwra.com> - 1.2.1-4
- Add two patches from mex-octave for octave 4.2 support

* Fri Dec 09 2016 Orion Poplawski <orion@cora.nwra.com> - 1.2.1-4
- Rebuild for octave 4.2.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Orion Poplawski <orion@cora.nwra.com> - 1.2.1-2
- Rebuild for hdf5 1.8.16

* Mon Jul 6 2015 Orion Poplawski <orion@cora.nwra.com> - 1.2.1-1
- Update to 1.2.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.2.0-3
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.2.0-1
- update to 1.2.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Dec 29 2013 Orion Poplawski <orion@cora.nwra.com> - 1.1.0-9
- Rebuild for octave 3.8.0

* Mon Aug 05 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.1.0-8
- Fix FTBFS

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-5
- Rebuilt for c++ ABI breakage

* Mon Jan 16 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.1.0-4
- rebuild for octave 3.6.0

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec 17 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.1.0-2
- update according to reviewer comments

* Fri Dec 16 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.1.0-1
- update to 1.1.0

* Fri Jun 03 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.0.10-1
- initial package for Fedora
