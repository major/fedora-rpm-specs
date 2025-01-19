%global octpkg signal

Name:           octave-%{octpkg}
Version:        1.4.6
Release:        3%{?dist}
Summary:        Signal processing tools for Octave
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://octave.sourceforge.net/signal/
Source0:        http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz

# buildsys seems broken for s390x
ExcludeArch:    s390x

BuildRequires:  octave-devel >= 6:3.8.0
BuildRequires:  octave-control >= 2.4.5

Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave
Requires:       octave-control >= 2.4.5


%description
Signal processing tools, including filtering, windowing and display

%prep
%setup -q -n %{octpkg}-%{version}
for i in inst/*.m; do
  iconv -f iso8859-1 -t utf-8 $i > $i.conv && mv -f $i.conv $i
done;

%build
#octave pkg build dependency check does not work
#https://bugzilla.redhat.com/show_bug.cgi?id=733615
%octave_pkg_build
#octave_cmd pkg build '-verbose' '-nodeps' %{_tmppath}/%{name}-%{version}-%{release}.%{_arch} %{_builddir}/%{buildsubdir}

%install
%octave_pkg_install

%check
%octave_pkg_check

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
%{octpkgdir}/private/*.m
%{octpkgdir}/packinfo
%doc %{octpkgdir}/packinfo/COPYING
%{_metainfodir}/io.sourceforge.octave.signal.metainfo.xml
%{octpkgdir}/PKG_ADD
%{octpkgdir}/PKG_DEL
%doc %{octpkgdir}/doc


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Nov 14 2024 Orion Poplawski <orion@nwra.com> - 1.4.6-2
- Rebuild for octave 9.2

* Sat Sep 21 2024 Thomas Sailer <fedora@tsailer.ch> - 1.4.6-1
- update to 1.4.6

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4.5-5
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jul 24 2023 Thomas Sailer <fedora@tsailer.ch> - 1.4.5-1
- update to 1.4.5

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed May 17 2023 Thomas Sailer <fedora@tsailer.ch> - 1.4.4-1
- update to 1.4.4

* Sat Apr 08 2023 Orion Poplawski <orion@nwra.com> - 1.4.3-3
- Rebuild with octave 8.1.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Oct 28 2022 Thomas Sailer <fedora@tsailer.ch> - 1.4.3-1
- update to 1.4.3

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Orion Poplawski <orion@nwra.com> - 1.4.2-2
- Rebuild for octave 7.1

* Sat Apr 23 2022 Thomas Sailer <fedora@tsailer.ch> - 1.4.2-1
- update to 1.4.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 11 2021 Orion Poplawski <orion@nwra.com> - 1.4.1-10
- Rebuild for octave 6.3.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 07 2019 Orion Poplawski <orion@nwra.com> - 1.4.1-5
- Rebuild with octave 64bit indexes

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Orion Poplawski <orion@nwra.com> - 1.4.1-3
- Rebuild for octave 5.1

* Sun Apr 21 2019 Colin B. Macdonald <cbm@m.fsf.org> - 1.4.1-2
- Enable tests

* Fri Apr 05 2019 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.4.1-1
- update to 1.4.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Orion Poplawski <orion@cora.nwra.com> - 1.4.0-5
- Rebuild for octave 4.4

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 1.4.0-4
- Rebuild with fixed binutils

* Fri Jul 27 2018 Orion Poplawski <orion@nwra.com> - 1.4.0-3
- Add appdata file

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 07 2018 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.4.0-1
- update to 1.4.0

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 07 2016 Orion Poplawski <orion@cora.nwra.com> - 1.3.2-3
- Rebuild for octave 4.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 07 2015 Orion Poplawski <orion@cora.nwra.com> - 1.3.2-1
- Update to 1.3.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.3.0-4
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 30 2014 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.3.0-1
- update to 1.3.0

* Sun Dec 29 2013 Orion Poplawski <orion@cora.nwra.com> - 1.2.2-3
- Rebuild for octave 3.8.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 26 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.2.2-1
- update to 1.2.2

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov  8 2012 Orion Poplawski <orion@cora.nwra.com> - 1.2.0-1
- Update to 1.2.0
- Rebase nostrip patch
- New requires

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 15 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.1.3-1
- update to 1.1.3

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for c++ ABI breakage

* Wed Jan 18 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.1.2-1
- update to 1.1.2

* Mon Jan 16 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.1.1-4
- rebuild for octave 3.6.0

* Sat Jan 14 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.1.1-3
- fix gcc 4.7 compilation

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov  8 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.1.1-1
- update to 1.1.1

* Sat Nov  5 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.1.0-1
- update to 1.1.0

* Fri Aug 26 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.0.11-2
- review input

* Fri Jun 03 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.0.11-1
- initial package for Fedora
