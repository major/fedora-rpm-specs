%global debug_package %{nil}
%global gitrev 304d1d
%global gitdate 20110613

Name:		mono-reflection
Version:	0.1
Release:	0.32.%{gitdate}git%{gitrev}%{?dist}
Summary:	Helper library for Mono Reflection support
URL:		https://github.com/jbevain/mono.reflection
License:	MIT
# No source tarball, source from git:
# git clone https://github.com/jbevain/mono.reflection.git
# Use ./mono-reflection-make-git-snapshot.sh script to reproduce
Source0:	mono-reflection-%{gitdate}git%{gitrev}.tar.bz2
Source1:	mono-reflection.pc
Source2:	mono-reflection-make-git-snapshot.sh
Patch0:		mono-reflection-build.patch
BuildRequires: make
BuildRequires:	mono-devel

# Mono only available on these:
ExclusiveArch: %mono_arches

%description
Helper library for Mono Reflection support.

%package devel
Summary:	Development files for Mono.Reflection library
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	pkgconfig

%description devel
Development files for Mono.Reflection library.

%prep
%setup -q -n mono-reflection-%{gitdate}
%patch -P0 -p1
chmod -x README
sed -i 's/\r//' README

# Delete bundled DLL
rm -rf Test/target.dll

%build
# Use the mono system key instead of generating our own here.
cp -a /etc/pki/mono/mono.snk Mono.Reflection.snk
make LIBDIR=%{_libdir}

%install
mkdir -p %{buildroot}%{_libdir}/pkgconfig
cp -p %{SOURCE1} %{buildroot}%{_libdir}/pkgconfig
sed -i -e 's!@libdir@!%{_libdir}!' $RPM_BUILD_ROOT/%{_libdir}/pkgconfig/mono-reflection.pc
mkdir -p %{buildroot}%{_prefix}/lib/mono/gac/
gacutil -i bin/Mono.Reflection.dll -f -package Mono.Reflection -root %{buildroot}%{_prefix}/lib

%files
%doc README
%{_prefix}/lib/mono/gac/Mono.Reflection/
%{_prefix}/lib/mono/Mono.Reflection/

%files devel
%{_libdir}/pkgconfig/mono-reflection.pc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.32.20110613git304d1d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.31.20110613git304d1d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.30.20110613git304d1d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.29.20110613git304d1d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.28.20110613git304d1d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.27.20110613git304d1d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.26.20110613git304d1d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.25.20110613git304d1d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.24.20110613git304d1d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.23.20110613git304d1d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.22.20110613git304d1d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.21.20110613git304d1d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.20.20110613git304d1d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.19.20110613git304d1d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.18.20110613git304d1d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.17.20110613git304d1d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.16.20110613git304d1d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.15.20110613git304d1d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.14.20110613git304d1d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.13.20110613git304d1d
- mono rebuild for aarch64 support

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.12.20110613git304d1d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.11.20110613git304d1d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.1-0.10.20110613git304d1d
- Rebuild (mono4)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.9.20110613git304d1d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.8.20110613git304d1d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.7.20110613git304d1d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.6.20110613git304d1d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.5.20110613git304d1d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.4.20110613git304d1d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 13 2011 Christian Krause <chkr@fedoraproject.org> - 0.1-0.3.20110613git304d1d
- Change paths for mono assemblies according to updated packaging
  guidelines (http://fedoraproject.org/wiki/Packaging:Mono)

* Mon Jun 13 2011 Tom Callaway <spot@fedoraproject.org> - 0.1-0.2.20110613git304d1d
- add script to generate tarball
- correct git revision
- add fully versioned Requires for base package in subpackage
- delete prebuilt DLL during prep

* Thu May 12 2011 Tom Callaway <spot@fedoraproject.org> - 0.1-0.1.201105123git04d1df
- Initial package creation
