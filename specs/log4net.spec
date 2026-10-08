%if 0%{?rhel}%{?el6}%{?el7}
# see https://fedorahosted.org/fpc/ticket/395
%global _monodir %{_prefix}/lib/mono
%global _monogacdir %{_monodir}/gac
%endif

# This is a mono package
%define debug_package %{nil}

Name:	 	log4net
URL:		http://logging.apache.org/log4net/
License:	Apache-2.0
Version:	3.5.0
Release:	1%{?dist}
Summary:	A .NET framework for logging
Source:		https://downloads.apache.org/logging/log4net/%{version}/apache-log4net-source-%{version}.zip
Patch0:		RollingFileAppender-count-assignment.patch
# Remove build-only NuGet dependencies (SourceLink + analyzers) so a net462-only
# build restores offline against Mono's reference assemblies only.
Patch1:		log4net-remove-build-only-deps.patch
BuildRequires:	dotnet-host, dotnet-sdk-10.0
BuildRequires:	mono-data-sqlite
BuildRequires:	mono-devel

# DotNet SDK not available on i686
ExcludeArch:	i686

%description
log4net is a tool to help the programmer output log statements to a
variety of output targets. log4net is a port of the excellent log4j
framework to the .NET runtime

%package devel
Summary:	A .NET framework for logging
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig

%description devel
log4net is a tool to help the programmer output log statements to a
variety of output targets. log4net is a port of the excellent log4j
framework to the .NET runtime

%prep
%setup -q -c
%patch -P0 -p1
%patch -P1 -p1
# Force a fully offline NuGet restore: no package sources are permitted, so the
# build cannot reach the network. Reference assemblies come from Mono (see %%build),
# not from NuGet, so no packages need to be restored at all.
cat > nuget.config <<'EOF'
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <config>
    <add key="globalPackagesFolder" value="packages-cache" />
  </config>
  <packageSources>
    <clear />
  </packageSources>
</configuration>
EOF
sed -i 's/\r//' NOTICE
sed -i 's/\r//' README.md
sed -i 's/\r//' LICENSE
# Remove prebuilt dll files
rm -rf bin/

%build
export DOTNET_CLI_TELEMETRY_OPTOUT=1
export DOTNET_NOLOGO=1
# Build net462 only (the assembly that is installed into the Mono GAC).
#  - TargetFrameworks=net462 (plural) collapses the restore graph to the single
#    target, avoiding the netstandard2.0 NuGet chain.
#  - AutomaticallyUseReferenceAssemblyPackages=false stops the SDK from trying to
#    restore the proprietary Microsoft.NETFramework.ReferenceAssemblies package.
#  - FrameworkPathOverride points the compiler at Mono's (FOSS) reference
#    assemblies shipped by mono-devel.
#  - GeneratePackageOnBuild=false: we want the DLL, not a .nupkg.
#  - PublicSign=true: embed the strong-name public key (preserving the assembly
#    identity / public key token) WITHOUT computing the RSA strong-name signature.
#    Real strong-name signing uses SHA-1 RSA via OpenSSL, which fails under the
#    FIPS/crypto-policy restrictions of the mock build root
#    ("error:03000098 ... invalid digest"). Public signing avoids that crypto call.
dotnet build src/log4net/log4net.csproj -c Release \
    -p:TargetFrameworks=net462 \
    -p:AutomaticallyUseReferenceAssemblyPackages=false \
    -p:FrameworkPathOverride=/usr/lib/mono/4.7.1-api \
    -p:GeneratePackageOnBuild=false \
    -p:PublicSign=true

%install
# install pkgconfig file
cat > %{name}.pc <<EOF
Name: log4net
Description: log4net - .Net logging framework
Version: %{version}
Libs: -r:%{_monodir}/log4net/log4net.dll
EOF

mkdir -p $RPM_BUILD_ROOT/%{_libdir}/pkgconfig
cp %{name}.pc $RPM_BUILD_ROOT/%{_libdir}/pkgconfig
mkdir -p $RPM_BUILD_ROOT/%{_monogacdir}

# The assembly was public-signed during %%build (the Roslyn SHA-1 RSA strong-name
# signing fails under the mock crypto policy). Complete the strong name here with
# Mono's own sn tool, which does not use the restricted OpenSSL path. gacutil
# refuses to install a delay/public-signed assembly ("Strong name cannot be
# verified for delay-signed assembly"); after this it verifies and installs.
sn -R build/Release/net462/log4net.dll log4net.snk

gacutil -i build/Release/net462/log4net.dll -f -package log4net -root ${RPM_BUILD_ROOT}/%{_prefix}/lib

%files
%{_monogacdir}/log4net
%{_monodir}/log4net
%doc NOTICE README.md
%license LICENSE

%files devel
%{_libdir}/pkgconfig/log4net.pc

%changelog
* Wed Oct  7 2026 Tom Callaway <spot@fedoraproject.org> 3.5.0-1
- update to 3.5.0

* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.8-21
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 15 2020 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 2.0.8-10
- apply security fix for xml configurator: [CVE-2018-1285] XXE vulnerability in Apache log4net

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 21 2019 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 2.0.8-8
- Rebuilt with new mono package so that the Provides is fixed again
- don't require nant for building

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 14 2017 Tom Callaway <spot@fedoraproject.org> - 2.0.8-1
- update to 2.0.8

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Tom Callaway <spot@fedoraproject.org> - 2.0.7-1
- update to 2.0.7

* Thu Oct 13 2016 Peter Robinson <pbrobinson@fedoraproject.org> - 1.2.15-4
- aarch64 bootstrap

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Tom Callaway <spot@fedoraproject.org> - 1.2.15-2
- spec file cleanups

* Mon Dec 14 2015 Tom Callaway <spot@fedoraproject.org> - 1.2.15-1
- update to 1.2.15

* Wed Nov 11 2015 Tom Callaway <spot@fedoraproject.org> - 1.2.14-1
- update to 1.2.14

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 13 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 1.2.13-4
- Build with mono 4
- Use mono_arches
- Use xbuild insted nant for prevent recursive required. Nant need log4net.
- Fix uppercase name problem

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jun  2 2014 Tom Callaway <spot@fedoraproject.org> - 1.2.13-1
- update to 1.2.13

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.10-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.10-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.10-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.10-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 20 2011 Christian Krause <chkr@fedoraproject.org> - 1.2.10-17
- Change paths for mono assemblies according to updated packaging
  guidelines (http://fedoraproject.org/wiki/Packaging:Mono)

* Tue Apr 19 2011 Dan Horák <dan[at]danny.cz> - 1.2.10-16
- updated the supported arch list

* Fri Apr 08 2011 Kalev Lember <kalev@smartlink.ee> - 1.2.10-15
- Fixed build with mono 2.10

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 30 2010 Dan Horák <dan[at]danny.cz> - 1.2.10-13
- bump NVR

* Tue Dec  1 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.2.10-10
- use system mono.snk key instead of generating our own on each build

* Sun Nov 29 2009 Christopher Brown <snecklifter@gmail.com> - 1.2.10-9
- Fix pkg-config file location

* Mon Oct 26 2009 Dennis Gilmore <dennis@ausil.us> - 1.2.10-8
- Exclude sparc64  no mono

* Thu Jul 30 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.2.10-7
- rebuild to get nant cooking again

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Apr 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.2.10-4
- excludearch ppc (nant doesn't work on ppc)
- delete bundled binary bits

* Mon Feb 25 2008 Christopher Brown <snecklifter@gmail.com> - 1.2.10-3
- Bump for upgrade path now nant is in rawhide

* Wed Feb 20 2008 Christopher Brown <snecklifter@gmail.com> - 1.2.10-1
- Add excludearch for ppc64
- File ownership cleanup

* Fri Sep  7 2007 Christopher Brown <snecklifter@gmail.com> - 1.2.10-1
- switch to nant for build

* Mon Sep  3 2007 Christopher Brown <snecklifter@gmail.com> - 1.2.9-70.1
- initial cleanup for Fedora

* Thu Mar 29 2007 rguenther@suse.de
- add unzip BuildRequires
* Mon May 22 2006 jhargadon@novell.com
- fix for bug 148685 This was a remotely triggerable vulnerability
  issue where the syslog() function from glibc was used incorrectly.
* Wed Apr 26 2006 wberrier@suse.de
- Change to noarch package, remove unnecessary deps
* Sat Feb 25 2006 aj@suse.de
- Do not build as root
- Reduce BuildRequires.
* Tue Feb  7 2006 ro@suse.de
- drop self obsoletes
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Thu Jan 12 2006 ro@suse.de
- modified neededforbuild (use mono-devel-packages)
* Mon Nov 28 2005 cgaisford@novell.com
- Initial package creation
