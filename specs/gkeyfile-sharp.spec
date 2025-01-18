%define tagname GKEYFILE_SHARP_0_1
%define relvers 0
%define tsuffix g07a401a
%define dsuffix 662c5c1

%global debug_package %{nil}

Name:           gkeyfile-sharp
Version:        0.1
Release:        42%{?dist}
Summary:        C# bindings for glib2's keyfile implementation

# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            http://github.com/mono/%{name}
# Releases are tarballs downloaded from a tag at github.
# They are releases, but the file is generated on the fly.
# The actual URL is: http://github.com/mono/$name/tarball/$tagname
Source0:        mono-%{name}-%{tagname}-%{relvers}-%{tsuffix}.tar.gz
# Upstream patch to fix DllImport name of libglib (BZ 692784)
# https://github.com/mono/gkeyfile-sharp/commit/1a1adb8ec4149b4a0a8e55db0e3baa172cbd2c3f
Patch1:         0001-Change-glib-DllImports-to-libglib-2.0-0.dll.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  glib2-devel
BuildRequires:  gtk-sharp2-devel
BuildRequires:  gtk-sharp2-gapi
BuildRequires:  mono-devel
BuildRequires: make

# Mono only available on these:
ExclusiveArch: %mono_arches

%package devel
Summary:        Development files for gkeyfile-sharp
Requires:       pkgconfig
Requires:       %{name} = %{version}-%{release}

%description
C# bindings for glib2's keyfile implementation

%description devel
Development files for gkeyfile-sharp

%prep
%setup -q -n mono-%{name}-%{dsuffix}
sed -i "s#gmcs#mcs#g" configure.in
%patch -P1 -p1 -b dllimport-fix

%build
./autogen.sh
%configure --libdir=%{_prefix}/lib
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
chmod 644 `find $RPM_BUILD_ROOT%{_prefix}/lib/mono -name '*.dll.config'`
rm -f $RPM_BUILD_ROOT%{_prefix}/lib/mono/%{name}/%{name}.dll.config

mkdir -p %{buildroot}%{_libdir}/pkgconfig
test "%{_libdir}" = "%{_prefix}/lib" || mv %{buildroot}%{_prefix}/lib/pkgconfig/*.pc %{buildroot}%{_libdir}/pkgconfig/


%files
%doc AUTHORS ChangeLog LICENSE.LGPL NEWS
%{_prefix}/lib/mono/gac/%{name}
%{_prefix}/lib/mono/%{name}

%files devel
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1-41
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-31
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 31 2019 Tom Callaway <spot@fedoraproject.org> - 0.1-28
- rebuild for auto-provides/requires

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-20
- mono rebuild for aarch64 support

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 28 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 0.1-17
- Build with mono 4

* Tue Mar 24 2015 Than Ngo <than@redhat.com> - 0.1-16
- use %%mono_arches

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Brent Baude <baude@us.ibm.com> - 0.1-13
- Changing ppc64 to power64 macro

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 27 2011 Christian Krause <chkr@fedoraproject.org> - 0.1-8
- Change paths for mono assemblies according to updated packaging
  guidelines (http://fedoraproject.org/wiki/Packaging:Mono)

* Sun May 08 2011 Christian Krause <chkr@fedoraproject.org> - 0.1-7
- Add mono-devel as BR for correct generation of the Requires/Provides

* Sun May 08 2011 Christian Krause <chkr@fedoraproject.org> - 0.1-6
- Fix DllNotFoundException by adding upstream patch (BZ 692784)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 04 2011 Dan Horák <dan[at]danny.cz> - 0.1-4
- updated the supported arch list

* Mon Oct 04 2010 Nathaniel McCallum <nathaniel@natemccallum.com> - 0.1-3
- Fix directory ownership

* Sun Oct 03 2010 Nathaniel McCallum <nathaniel@natemccallum.com> - 0.1-2
- Fix -devel requires (pkgconfig, base package)
- Disable debuginfo

* Wed Sep 29 2010 Nathaniel McCallum <nathaniel@natemccallum.com> - 0.1-1
- Initial version

