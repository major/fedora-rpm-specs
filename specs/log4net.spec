%if 0%{?rhel}%{?el6}%{?el7}
# see https://fedorahosted.org/fpc/ticket/395
%global _monodir %{_prefix}/lib/mono
%global _monogacdir %{_monodir}/gac
%endif

Name:	 	log4net
URL:		http://logging.apache.org/log4net/
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:	Apache-2.0
Version:	2.0.8
Release:	22%{?dist}
Summary:	A .NET framework for logging
Source:		http://mirror.reverse.net/pub/apache/logging/log4net/source/%{name}-%{version}-src.zip
Patch0:		log4net-2.0.8-xmlconfigurator.patch

BuildRequires:	dos2unix
BuildRequires:	mono-data-sqlite
BuildRequires:	mono-devel

# Mono only available on these:
ExclusiveArch: %mono_arches

# %define debug_package %{nil}
# This is a mono package

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
%setup -q
dos2unix src/Config/XmlConfigurator.cs
%patch -P0 -p1
sed -i 's/\r//' NOTICE
sed -i 's/\r//' README.txt
sed -i 's/\r//' LICENSE
# Remove prebuilt dll files
rm -rf bin/

# mv src/Layout/XMLLayout.cs src/Layout/XmlLayout.cs
# mv src/Layout/XMLLayoutBase.cs src/Layout/XmlLayoutBase.cs

# Fix for mono 4
find . -name "*.sln" -print -exec sed -i 's/Format Version 10.00/Format Version 11.00/g' {} \;
find . -name "*.csproj" -print -exec sed -i 's#ToolsVersion="3.5"#ToolsVersion="4.0"#g; s#<TargetFrameworkVersion>.*</TargetFrameworkVersion>##g; s#<PropertyGroup>#<PropertyGroup><TargetFrameworkVersion>v4.5</TargetFrameworkVersion>#g' {} \;

# Use system mono.snk key
sed -i -e 's!"..\\..\\..\\log4net.snk")]!"/etc/pki/mono/mono.snk")]!' src/AssemblyInfo.cs
sed -i -e 's!|| SSCLI)!|| SSCLI || MONO)!' src/AssemblyInfo.cs


%build
# ASF recommend using nant to build log4net
xbuild /property:Configuration=Debug /property:DefineConstants=DEBUG,MONO,STRONG src/log4net.vs2010.csproj

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

#gacutil -i bin/mono/*/release/log4net.dll -f -package log4net -root ${RPM_BUILD_ROOT}/%{_prefix}/lib
gacutil -i build/bin/net/*/debug/log4net.dll -f -package log4net -root ${RPM_BUILD_ROOT}/%{_prefix}/lib

%files
%{_monogacdir}/log4net
%{_monodir}/log4net
%doc NOTICE README.txt
%license LICENSE

%files devel
%{_libdir}/pkgconfig/log4net.pc

%changelog
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
