#
# spec file for package sharpfont
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%global libname SharpFont
%global debug_package %{nil}

Name:           sharpfont
Version:        4.0.1
Release:        19%{?dist}
Url:            https://github.com/Robmaister/%{libname}
Summary:        Cross-platform FreeType bindings for .NET
License:        MIT
Source:         %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

ExclusiveArch:  %mono_arches

BuildRequires:  pkgconfig(mono)

%description
SharpFont is a library that provides FreeType bindings for .NET.
Everything from format-specific APIs to the caching subsystem are included.


%package devel
Summary:        Cross-platform FreeType bindings for .NET
Requires:       %{name} = %{version}-%{release}

%description devel
SharpFont is a library that provides FreeType bindings for .NET.
Everything from format-specific APIs to the caching subsystem are included.


%prep
%autosetup -p1 -n%{libname}-%{version}
rm -r Build Dependencies

%build
#make debug
pushd Source/%{libname}
# override the .NET Framework Target for predefined types
# https://stackoverflow.com/questions/27594393/compiled-mono-missing-default-net-libraries-system-object-is-not-defined-or-i
xbuild /p:TargetFrameworkVersion=v4.5 /p:Configuration=Debug

%install
mkdir -p %{buildroot}%{_prefix}/lib/mono/gac/
gacutil -i Binaries/%{libname}/Debug/%{libname}.dll -f -package %{name} -root %{buildroot}%{_prefix}/lib
cp -p Source/%{libname}.dll.config %{buildroot}%{_monodir}/%{name}

mkdir -p %{buildroot}/%{_datadir}/pkgconfig
cat <<EOT >>%{buildroot}/%{_datadir}/pkgconfig/%{name}.pc
Name: %{libname}
Description: %{summary}
Version: 4.0.1
Requires: mono
Libs: -r:%{_monodir}/%{name}/%{libname}.dll
Libraries=%{_monodir}/%{name}/%{libname}.dll
EOT


%files
%license LICENSE
%doc README.md
%doc Source/Examples/
%{_monogacdir}/%{libname}
%{_monodir}/%{name}/%{libname}.dll*
%dir %{_monodir}/%{name}
 

%files devel
%{_datadir}/pkgconfig/%{name}.pc


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 31 2016 Raphael Groner <projects.rg@smart.ms> - 4.0.1-1
- new version

* Tue May 17 2016 Raphael Groner <projects.rg@smart.ms> - 3.1.0-1
- new version
- remove upstreamed patches
- call xbuild directly
- build in debug configuration
- apply specifics of mono packaging
- add LICENSE and README.md
- use Examples as documentation
- add dist tag

* Wed Mar 02 2016 Raphael Groner <projects.rg@smart.ms> - 3.0.1-1
- adjust for Fedora

* Tue Nov 24 2015 Matthias Mailänder <mailaender@opensuse.org> - 3.0.1-0
- initial packaging
