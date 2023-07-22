%bcond_with bootstrap

%global multilib_arches %{ix86} x86_64

Name:		libffi3.1
Version:	3.1
# The last libffi-3.1 release was libffi-3.1-27, and so to help with the
# logical transition we label the compat package libffi3.1-3.1-28
# (next NEVRA bump) rather than the more confusing libffi3.1-3.1-1 since
# there was already a 3.1-1 on May 19, 2014.
Release:	36%{?dist}
Summary:	Compatibility package for libffi transition from 3.1 to 3.4.2.
License:	MIT
URL:		http://sourceware.org/libffi

Source0:	ftp://sourceware.org/pub/libffi/libffi-%{version}.tar.gz
Source1:	ffi-multilib.h
Source2:	ffitarget-multilib.h
Patch0:		libffi-3.1-fix-include-path.patch
Patch1:		libffi-3.1-fix-exec-stack.patch
Patch2:		libffi-aarch64-rhbz1174037.patch
Patch3:		libffi-3.1-aarch64-fix-exec-stack.patch
Patch4:		libffi-3.1-libffi_tmpdir.patch
Patch5:		libffi3.1-pkgconfig.patch

BuildRequires: gcc
%if %{without bootstrap}
BuildRequires: gcc-c++
BuildRequires: dejagnu
%endif

%description
The libffi3.1 package contains the libffi 3.1 runtime library to
support the library SONAME transition from 3.1 to 3.4.2. This pacakge
will eventually be removed once the transition is complete.

%prep
%setup -q -n libffi-3.1
%patch0 -p1 -b .fixpath
%patch1 -p1 -b .execstack
%patch2 -p1 -b .aarch64
%patch3 -p1 -b .aarch64execstack
%patch4 -p1 -b .libffitmpdir

%build

%configure --disable-static --includedir=%{_includedir}/libffi3.1
%make_build

%check
%if %{without bootstrap}
%make_build check
%endif

%install
%make_install

# We only need the shared libraries, license, and README.
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm -rf $RPM_BUILD_ROOT%{_libdir}/libffi-%{version}/include/{ffi,ffitarget}.h
rm -rf $RPM_BUILD_ROOT%{_libdir}/libffi.so
find $RPM_BUILD_ROOT%{_mandir} -name 'ffi*' -exec rm -f {} ';'
find $RPM_BUILD_ROOT%{_infodir} -name 'libffi.info*' -exec rm -f {} ';'
rm -rf $RPM_BUILD_ROOT%{_libdir}/pkgconfig/libffi.pc
# We want the LICENSE and README to be in slightly adjusted path.
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/libffi-3.1
cp %{_builddir}/libffi-3.1/README $RPM_BUILD_ROOT/%{_docdir}/libffi-3.1/README
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/licenses/libffi-3.1
cp %{_builddir}/libffi-3.1/LICENSE $RPM_BUILD_ROOT/%{_datadir}/licenses/libffi-3.1/LICENSE

%ldconfig_scriptlets

%files
%license %{_datadir}/licenses/libffi-3.1/LICENSE
%doc %{_docdir}/libffi-3.1/README
%{_libdir}/libffi.so.6.0.2
%{_libdir}/libffi.so.6

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 08 2022 Miro Hrončok <mhroncok@redhat.com> - 3.1-32
- Rebuilt for https://fedoraproject.org/wiki/Changes/LIBFFI34

* Wed Sep 15 2021 Carlos O'Donell <codonell@redhat.com> - 3.1-31
- Rebuilt for https://fedoraproject.org/wiki/Changes/LIBFFI34

* Wed Aug 11 2021 Carlos O'Donell <carlos@redhat.com> 3.1-30
- Simplify compatibility package layout.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Dec 08 2020 Carlos O'Donell <carlos@redhat.com> 3.1-28
- Created compatibility libffi3.1 package.
