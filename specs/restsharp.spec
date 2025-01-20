%global libname RestSharp

# mono is without any packagable debuginfo
%global debug_package %{nil}

Name:           restsharp
Version:        105.2.3
Release:        29%{?dist}
Summary:        Simple REST and HTTP API Client

# Main license is Apache 2.0, but MIT/X11 for Extensions/MonoHttp and SimpleJson
# Automatically converted from old format: ASL 2.0 and MIT - review is highly recommended.
License:        Apache-2.0 AND LicenseRef-Callaway-MIT
URL:            http://restsharp.org 
Source0:        https://github.com/%{name}/%{libname}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# some cosmetics to the csproj configuraton, e.g. mono has case sensitivity
Patch0:         %{name}-case.patch
Patch1:         %{name}-unbundle-nunit.patch
Patch2:         %{name}-disable-nuget.patch

BuildRequires:  mono-devel
# versioned binary of nunit console command
BuildRequires:  nunit2 = 2.6.4

ExclusiveArch: %{mono_arches}

# nunit2 fails to build on armv7hl. Mono crashes. see bug 1923663
# it is too much work to switch to nunit (version 3) at the moment.
ExcludeArch:    armv7hl

%description
%{summary}.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.


%prep
%setup -qn%{libname}-%{version}
%patch -P0
%patch -P1
# FIXME check why last hunk gets rejected
#%patch2
find . -name \*.csproj |xargs sed -i \
 -e /nuget/d -e /NuSpecUpdateTask.cs/d \
 -e 's#,1658##g'
# disable sloppy tests, https://github.com/restsharp/RestSharp/issues/767
sed -i -r 's,.*Can_Deserialize_DateTime_With_DateTimeStyles,[Ignore("broken")]\n\0,' %{libname}.Tests/JsonTests.cs
sed -i -r -e 's,.*Can_Deserialize_DateTimeOffset,[Ignore("broken")]\n\0,' \
 -e 's,.*Can_Deserialize_TimeSpan,[Ignore("broken")]\n\0,' \
 %{libname}.Tests/XmlAttributeDeserializerTests.cs %{libname}.Tests/XmlDeserializerTests.cs


%build
pushd %{libname}.Net45
xbuild %{libname}.Net45.Signed.csproj


%install
mkdir -p %{buildroot}/%{_monogacdir}
gacutil -i %{libname}.Net45/bin/DebugSigned/%{libname}.dll -f -package %{name} -root %{buildroot}/usr/lib
# pkgconfig
mkdir -p %{buildroot}/%{_libdir}/pkgconfig
cat <<EOT >>%{buildroot}/%{_libdir}/pkgconfig/%{name}.pc
Name: %{libname}
Description: %{summary}
Version: %{version}
Requires: mono
Libs: -r:%{_monodir}/%{name}/%{libname}.dll
Libraries=%{_monodir}/%{name}/%{libname}.dll
EOT


%check
pushd %{libname}.Tests

%ifnarch s390x
# override the .NET Framework Target for predefined types
# https://stackoverflow.com/questions/27594393/compiled-mono-missing-default-net-libraries-system-object-is-not-defined-or-i
xbuild /p:TargetFrameworkVersion=v4.5 %{libname}.Tests.csproj
nunit-console26 -labels -stoponerror bin/Debug/%{libname}.Tests.dll
%endif

%files
%license LICENSE.txt
%doc *.markdown readme.txt
%{_monogacdir}/%{libname}
%dir %{_monodir}/%{name}
%{_monodir}/%{name}/%{libname}.dll

%files devel
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 105.2.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 105.2.3-28
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 105.2.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 105.2.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 105.2.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 105.2.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 105.2.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 105.2.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 105.2.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 05 2021 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 105.2.3-20
- disable arch armv7hl

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 105.2.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 105.2.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 105.2.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 03 2020 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 105.2.3-16
- disable tests for s390x arch due to SIGSEGV

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 105.2.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 105.2.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 105.2.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 105.2.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 105.2.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 105.2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 105.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 105.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 105.2.3-7
- mono rebuild for aarch64 support

* Wed Aug 31 2016 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 105.2.3-6
- build with nunit2

* Tue Mar 08 2016 Raphael Groner <projects.rg@smart.ms> - 105.2.3-5
- fix FTBFS with newer CSC, rhbz#1315057

* Thu Feb 18 2016 Dan Horák <dan[at]danny.cz> - 105.2.3-4
- add ExclusiveArch

* Thu Feb 04 2016 Raphael Groner <projects.rg@smart.ms> - 105.2.3-3
- split devel subpackage, add mono as requirement in pkgconfig
- fix folder ownership of _monodir/name
- add license breakdown

* Wed Oct 14 2015 Raphael Groner <projects.rg@smart.ms> - 105.2.3-2
- use patches for csproj preparation
- unbundle + enable nunit

* Sat Oct 10 2015 Raphael Groner <projects.rg@smart.ms> - 105.2.3-1
- initial
