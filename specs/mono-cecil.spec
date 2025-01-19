%if 0%{?rhel}%{?el6}%{?el7}
# see https://fedorahosted.org/fpc/ticket/395
%define _monodir %{_prefix}/lib/mono
%define _monogacdir %{_monodir}/gac
%endif

# see https://bugzilla.redhat.com/show_bug.cgi?id=1224565
%global debug_package %{nil}

Name:           mono-cecil
Version:        0.10.4
Release:        13%{?dist}
Summary:        Library to generate and inspect programs and libraries in the ECMA CIL form
License:        MIT
URL:            http://www.mono-project.com/Cecil
Source0:        https://github.com/jbevain/cecil/archive/%{version}/cecil-%{version}.tar.gz
Source1:        %{name}.pc
# JIT only available on these:
ExclusiveArch:  %mono_arches
BuildRequires:  mono(xbuild)
Requires:       mono-core

%global configuration net_462_Release

%description
Cecil is a library written by Jb Evain to generate and inspect programs and
libraries in the ECMA CIL format. It has full support for generics, and support
some debugging symbol format.

In simple English, with Cecil, you can load existing managed assemblies, browse
all the contained types, modify them on the fly and save back to the disk the
modified assembly.

Today it is used by the Mono Debugger, the bug-finding and compliance checking
tool Gendarme, MoMA, DB4O, as well as many other tools.

%package devel
Summary:        pkgconfig file for Mono.Cecil
Requires:       mono-cecil = %{version}-%{release}
Requires:       pkgconfig

%description devel
This package contains the cecil.pc file
which is required by other packages that reference Mono.Cecil.dll

%prep
%setup -qn cecil-%{version}

%build

export NoCompilerStandardLib=false
xbuild Mono.Cecil.sln /p:Configuration=%{configuration}

%install
mkdir -p %{buildroot}%{monogacdir}/
cd bin/%{configuration}/
gacutil -i Mono.Cecil.dll -f -package Mono.Cecil -root %{buildroot}/usr/lib
gacutil -i Mono.Cecil.Mdb.dll -f -package Mono.Cecil -root %{buildroot}/usr/lib
gacutil -i Mono.Cecil.Pdb.dll -f -package Mono.Cecil -root %{buildroot}/usr/lib
gacutil -i Mono.Cecil.Rocks.dll -f -package Mono.Cecil -root %{buildroot}/usr/lib
cd -
mkdir -p %{buildroot}/%{_libdir}/pkgconfig/
%{__install} -m0644 %{SOURCE1} %{buildroot}%{_libdir}/pkgconfig/cecil.pc

%files
%doc
%{_monogacdir}/Mono.Cecil*
%{_monodir}/Mono.Cecil*

%files devel
%{_libdir}/pkgconfig/cecil.pc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 08 2019 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 0.10.4-1
- Another fix to the mono-cecil.pc file

* Thu Aug 08 2019 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 0.10.4-0
- Upgrade to Cecil 0.10.4

* Mon Jul 29 2019 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 0.10.3-1
- forgot to update the mono-cecil.pc file with the latest version

* Mon Jul 29 2019 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 0.10.3-0
- Upgrade to Cecil 0.10.3, and fix for building with xbuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Peter Robinson <pbrobinson@fedoraproject.org> - 0.9.6-6
- aarch64 bootstrap

* Sat Aug 06 2016 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 0.9.6-5
- add cecil.pc

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 26 2015 Miro Hrončok <mhroncok@redhat.com> - 0.9.6-2
- Disabling debuginfo (#1224565)

* Mon May 11 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> 0.9.6-1
- Build for Mono 4
- Update to 0.9.6

* Sat Oct 25 2014 Miro Hrončok <mhroncok@redhat.com> - 0.9.5-3.20140924git6d1b7d0
- Updated
- Remove bundled nunit
- Patch Mono.Cecil.sln not to build tests

* Thu Feb 27 2014 Miro Hrončok <mhroncok@redhat.com> - 0.9.5-2.20131105git8425de4
- Define %%monodir
- Require mono-core for monodir/gac dependency
- Define %%configuration

* Mon Jan 27 2014 Miro Hrončok <mhroncok@redhat.com> - 0.9.5-1
- New package
