%global debug_package %{nil}

Name:           mono-bouncycastle
Version:        1.8.10
Release:        10%{?dist}
Summary:        Bouncy Castle Crypto Package for Mono

# Files in crypto/bzip2/ are ASL 2.0 licensed,
# everything else is MIT.
# Automatically converted from old format: MIT and ASL 2.0 - review is highly recommended.
License:        LicenseRef-Callaway-MIT AND Apache-2.0
URL:            http://www.bouncycastle.org/csharp/
Source0:        https://github.com/bcgit/bc-csharp/archive/release-%{version}.tar.gz

BuildRequires:  mono-devel, nant, log4net
BuildRequires:  unzip

# Mono only available on these:
ExclusiveArch: %mono_arches
# nant is not available on armv7hl, see
# https://bugzilla.redhat.com/show_bug.cgi?id=1923663
ExcludeArch:    armv7hl

%description
The Bouncy Castle Crypto package is a C# implementation of cryptographic
algorithms. It is a port of the Bouncy Castle Java APIs, with
approximately 80% of the functionality ported. The C# API is constantly
kept up to date with bug fixes and new test cases from the Java build
(and vice versa sometimes), thus benefiting from the large user base
and real-world use the Java version has seen.

%prep
%setup -q -n bc-csharp-release-%{version}
sed -i 's/set-mono-4.0-framework-props/set-mono-4.5-framework-props/g' crypto/NBuild.build

%build
# Use the mono system key instead of generating our own here.
cp -a /etc/pki/mono/mono.snk BouncyCastle.snk
pushd crypto/
nant -D:use-strong-name=true compile-release
popd

%install
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/mono/gac/
gacutil -i crypto/api/bin/release/BouncyCastle.Crypto.dll -f -package bouncycastle -root $RPM_BUILD_ROOT%{_prefix}/lib

%files
%license crypto/License.html
%doc crypto/Contributors.html
%doc crypto/Readme.html
%{_prefix}/lib/mono/gac/*/
%{_prefix}/lib/mono/bouncycastle/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.8.10-9
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 23 2021 Kalev Lember <klember@redhat.com> - 1.8.10-1
- Update to 1.8.10

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 26 2019 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 1.8.5-4
- fix to build with fixed NAnt which now properly supports mono-4.5 target framework

* Fri Aug 09 2019 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 1.8.5-3
- add BuildRequires for log4net

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 08 2019 Kalev Lember <klember@redhat.com> - 1.8.5-1
- Update to 1.8.5
- Use license macro for License.html

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-0.10.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-0.9.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-0.8.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-0.7.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-0.6.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-0.5.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-0.4.rc1
- mono rebuild for aarch64 support

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-0.3.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 19 2015 Kalev Lember <kalevlember@gmail.com> - 1.8.0-0.1.rc1
- Update to 1.8.0 rc1

* Mon May 18 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.7-9
- Rebuild (mono4)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 21 2011 Christian Krause <chkr@fedoraproject.org> - 1.7-2
- Change paths for mono assemblies according to updated packaging
  guidelines (http://fedoraproject.org/wiki/Packaging:Mono)

* Sun Jun 26 2011 Kalev Lember <kalev@smartlink.ee> - 1.7-1
- Update to 1.7
- Cleaned up the spec file for modern rpmbuild
- Updated the supported arch list

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 08 2010 Kalev Lember <kalev@smartlink.ee> - 1.6.1-1
- Update to 1.6.1
- Dropped upstreamed patches

* Sun Feb 07 2010 Kalev Lember <kalev@smartlink.ee> - 1.6-3
- Applied upstream patch to fix AssemblyInfo for 1.6

* Sat Feb 06 2010 Kalev Lember <kalev@smartlink.ee> - 1.6-2
- Updated strongname.patch to the version sent for upstream inclusion

* Sat Feb 06 2010 Kalev Lember <kalev@smartlink.ee> - 1.6-1
- Update to version 1.6
- Use upstream source zip now that IDEA code is removed
- Removed patches which were merged upstream
- Added patch to strongname sign the resulting assembly
- ASL 1.1 files were relicensed to ASL 2.0, so now
  the license tag reads 'MIT and ASL 2.0'

* Sat Jan 23 2010 Kalev Lember <kalev@smartlink.ee> - 1.5-6
- Removed bundled mono.snk key

* Fri Dec 11 2009 Kalev Lember <kalev@smartlink.ee> - 1.5-5
- Updated mono-nopatents.patch to the version sent upstream

* Wed Dec 02 2009 Kalev Lember <kalev@smartlink.ee> - 1.5-4
- Updated License tag to read 'MIT and ASL 1.1'

* Wed Dec 02 2009 Kalev Lember <kalev@smartlink.ee> - 1.5-3
- Temporarily bundle mono.snk with this package to fix build on < F-13

* Tue Dec 01 2009 Kalev Lember <kalev@smartlink.ee> - 1.5-2
- Use the system mono.snk key instead of regenerating on every build

* Fri Nov 13 2009 Kalev Lember <kalev@smartlink.ee> - 1.5-1
- Initial RPM release.
